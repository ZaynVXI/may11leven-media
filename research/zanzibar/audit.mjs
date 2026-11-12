// Phone-view audit of each site: what a guest on a mid-range phone actually meets. Public pages only, read-only.
import { chromium, devices } from 'playwright';
import fs from 'fs';
const sites = JSON.parse(fs.readFileSync('out/sites.json', 'utf8'));
const ENGINES = {
  'booking.com': /booking\.com/i, siteminder: /siteminder|thebookingbutton|direct-book/i, cloudbeds: /cloudbeds/i,
  nightsbridge: /nightsbridge/i, littlehotelier: /littlehotelier/i, sabre: /synxis|sabre/i, ezee: /ezee|yanolja/i,
  beds24: /beds24/i, hotelrunner: /hotelrunner/i, mews: /mews\.(com|li)/i, profitroom: /profitroom/i,
  reservhotel: /reservhotel/i, simplebooking: /simplebooking/i, bookingsync: /bookingsync|smily/i, resrequest: /resrequest/i,
  lodgify: /lodgify/i, airbnb: /airbnb/i, expedia: /expedia/i, tripadvisor: /tripadvisor/i, pesapal: /pesapal|reserveport/i
};
const phone = devices['Moto G4'] ? { ...devices['Moto G4'] } : { viewport: { width: 360, height: 640 }, isMobile: true, hasTouch: true };
const browser = await chromium.launch();
const out = [];
for (const s of sites) {
  const r = { ...s };
  const ctx = await browser.newContext({ ...phone, ignoreHTTPSErrors: false });
  const page = await ctx.newPage();
  const reqHosts = new Set();
  page.on('request', q => { try { reqHosts.add(new URL(q.url()).host); } catch {} });
  try {
    const t0 = Date.now();
    const resp = await page.goto(s.url, { waitUntil: 'load', timeout: 45000 });
    r.loadMs = Date.now() - t0;
    r.status = resp ? resp.status() : null;
    r.finalUrl = page.url();
    r.https = r.finalUrl.startsWith('https://');
    await page.waitForTimeout(2500);
    const d = await page.evaluate(() => {
      const links = [...document.querySelectorAll('a[href]')].map(a => ({ href: a.href, text: (a.innerText || '').trim().toLowerCase().slice(0, 60) }));
      const frames = [...document.querySelectorAll('iframe[src]')].map(f => f.src);
      const text = (document.body?.innerText || '').toLowerCase();
      return {
        links, frames,
        overflowX: document.documentElement.scrollWidth > window.innerWidth + 2,
        viewportMeta: !!document.querySelector('meta[name=viewport]'),
        mpesa: /m-?pesa|mobile money|airtel money|tigo ?pesa|halopesa|mixx by yas/.test(text),
        priceShown: /(\$|usd|us\$|€|eur|tzs|tsh)\s?\d|\d+\s?(usd|eur|tzs)/.test(text),
        bookWords: /book now|check availability|reserve|book your stay|book direct/.test(text),
        directPerk: /book direct|best rate guarantee|best price guarantee|direct booking/.test(text),
        title: document.title,
        blocked: /you have been blocked|security check|checking your browser|access denied|attention required|just a moment|verify you are human|something went wrong|maintenance mode|under maintenance|site is undergoing maintenance|coming soon|account suspended|domain (is )?for sale/.test(text) || /just a moment|attention required|access denied/i.test(document.title),
        waAnywhere: /wa\.me|api\.whatsapp|whatsapp/i.test(document.documentElement.outerHTML),
        snippet: text.slice(0, 400),
        priceCtx: (text.match(/.{0,50}((\$|usd|us\$|€|eur|£|tzs|tsh)\s?\d[\d,.]*|\d[\d,.]*\s?(usd|eur|tzs|\$|€)|\d+\s?(per|\/)\s?night).{0,50}/g) || []).slice(0, 4),
        perkCtx: (text.match(/.{0,80}(book direct|best rate guarantee|best price guarantee|direct booking).{0,80}/g) || []).slice(0, 3),
        moneyCtx: (text.match(/.{0,40}(m-?pesa|mobile money|airtel money|tigo ?pesa|halopesa|mixx by yas).{0,40}/g) || []).slice(0, 3),
        waVisible: [...document.querySelectorAll('a,button,div,span,img')].some(e => { const t = ((e.getAttribute('href')||'') + ' ' + (e.getAttribute('aria-label')||'') + ' ' + (e.getAttribute('alt')||'') + ' ' + (e.className && e.className.baseVal === undefined ? e.className : '') + ' ' + (e.id||'')).toLowerCase(); if (!/whatsapp|wa\.me|joinchat|wa-chat|wa_btn|click-to-chat/.test(t)) return false; const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; }),
        bookTargets: [...document.querySelectorAll('a[href],button,[onclick]')].filter(e => /book|reserv|availab|check in|stay/i.test((e.innerText || e.getAttribute('aria-label') || '').trim())).map(e => e.getAttribute('href') || (e.closest('a') && e.closest('a').href) || (e.closest('form') && e.closest('form').action) || '').filter(Boolean).map(h => { try { return new URL(h, location.href).href; } catch { return ''; } }).filter(h => h && !/^(mailto|tel|javascript):/i.test(h) && !/facebook|instagram|twitter|x\.com|tiktok|youtube|linkedin|pinterest|wa\.me|whatsapp/i.test(h)).slice(0, 12),
        words: text.split(/\s+/).length
      };
    });
    const all = [...d.links.map(l => l.href), ...d.frames, ...reqHosts].join(' ');
    r.engines = Object.entries(ENGINES).filter(([, re]) => re.test(all)).map(([k]) => k);
    r.otaLinks = d.links.filter(l => /booking\.com|tripadvisor|airbnb|expedia|agoda/i.test(l.href)).length;
    r.whatsapp = d.links.some(l => /wa\.me|whatsapp\.com|api\.whatsapp/i.test(l.href));
    r.instagram = d.links.some(l => /instagram\.com/i.test(l.href));
    r.bookLinks = d.links.filter(l => /book|reserv|availab/.test(l.text)).map(l => l.href).slice(0, 5);
    r.bookLeavesSite = r.bookLinks.length ? r.bookLinks.every(h => { try { return !new URL(h).host.endsWith(new URL(r.finalUrl).host.replace(/^www\./, '')); } catch { return false; } }) : null;
    Object.assign(r, { overflowX: d.overflowX, viewportMeta: d.viewportMeta, mpesa: d.mpesa, priceShown: d.priceShown, bookWords: d.bookWords, directPerk: d.directPerk, title: d.title, words: d.words, blocked: d.blocked, waAnywhere: d.waAnywhere, snippet: d.snippet, priceCtx: d.priceCtx, perkCtx: d.perkCtx, moneyCtx: d.moneyCtx, waVisible: d.waVisible, bookTargets: d.bookTargets });
    await page.screenshot({ path: `out/shots/${s.host.replace(/[^a-z0-9.-]/gi, '_')}.jpg`, quality: 60 });
  } catch (e) { r.error = String(e.message || e).slice(0, 160); }
  await ctx.close();
  out.push(r);
  console.log(r.host, r.error ? 'ERR ' + r.error : `${r.loadMs}ms ${r.engines}`);
}
await browser.close();
fs.writeFileSync('out/audit.json', JSON.stringify(out, null, 1));
