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
        mpesa: /m-?pesa|mobile money|airtel money|tigo ?pesa|halopesa/.test(text),
        priceShown: /(\$|usd|us\$|€|eur|tzs|tsh)\s?\d|\d+\s?(usd|eur|tzs)/.test(text),
        bookWords: /book now|check availability|reserve|book your stay|book direct/.test(text),
        directPerk: /book direct|best rate guarantee|best price guarantee|direct booking/.test(text),
        title: document.title,
        blocked: /you have been blocked|security check|checking your browser|access denied|attention required|just a moment|verify you are human|something went wrong|maintenance mode|under maintenance|site is undergoing maintenance|coming soon|account suspended|domain (is )?for sale/.test(text) || /just a moment|attention required|access denied/i.test(document.title),
        waAnywhere: /wa\.me|api\.whatsapp|whatsapp/i.test(document.documentElement.outerHTML),
        snippet: text.slice(0, 400),
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
    Object.assign(r, { overflowX: d.overflowX, viewportMeta: d.viewportMeta, mpesa: d.mpesa, priceShown: d.priceShown, bookWords: d.bookWords, directPerk: d.directPerk, title: d.title, words: d.words, blocked: d.blocked, waAnywhere: d.waAnywhere, snippet: d.snippet });
    await page.screenshot({ path: `out/shots/${s.host.replace(/[^a-z0-9.-]/gi, '_')}.jpg`, quality: 60 });
  } catch (e) { r.error = String(e.message || e).slice(0, 160); }
  await ctx.close();
  out.push(r);
  console.log(r.host, r.error ? 'ERR ' + r.error : `${r.loadMs}ms ${r.engines}`);
}
await browser.close();
fs.writeFileSync('out/audit.json', JSON.stringify(out, null, 1));
