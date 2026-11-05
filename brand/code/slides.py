"""'What we do' services carousel. 9 slides 1080x1440. Bone base; each service owns its series accent."""
import asyncio, os
from playwright.async_api import async_playwright
F = '/home/claude/fonts-lab/node_modules/@fontsource/'; K = '/home/claude/kit/'; D = '/home/claude/svc/'
OUT = D + 'out/'; os.makedirs(OUT, exist_ok=True); N = 10
BONE, INK, ASH = '#ECEAE4', '#141213', '#5E5B57'
CSS = f"""
@font-face{{font-family:IT;src:url({K}fonts/InterTight-Regular.ttf)}}
@font-face{{font-family:IT;src:url({K}fonts/InterTight-Medium.ttf);font-weight:500}}
@font-face{{font-family:HK;src:url({F}hanken-grotesk/files/hanken-grotesk-latin-400-normal.woff2)}}
@font-face{{font-family:HK;src:url({F}hanken-grotesk/files/hanken-grotesk-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:IS;src:url({K}fonts/InstrumentSerif-Italic.ttf);font-style:italic}}
@font-face{{font-family:PM;src:url({K}fonts2/PlexMono.ttf)}}
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1440px;position:relative;overflow:hidden;font-family:IT;background:var(--bg);color:var(--fg)}}
.lab{{position:absolute;top:86px;font-family:PM;font-size:21px;letter-spacing:.12em;text-transform:uppercase;color:var(--mid)}}
.l{{left:64px}}.r{{right:64px}}
h1{{position:absolute;left:64px;right:64px;font-weight:400;font-size:84px;line-height:1.03;letter-spacing:-.03em}}
h1 i{{font-family:IS;font-style:italic;font-size:1.12em;letter-spacing:-.01em}}
p{{position:absolute;left:64px;font-family:HK;font-size:30px;line-height:1.42;color:var(--mid);max-width:860px}}
.num{{position:absolute;left:64px;top:200px;width:112px;height:112px;border-radius:14px;display:flex;align-items:center;justify-content:center;font:500 46px IT;letter-spacing:-.02em}}
.card{{position:absolute;left:64px;top:620px;width:952px;height:560px;border-radius:24px;overflow:hidden}}
.dl{{position:absolute;left:64px;top:1226px;display:flex;gap:34px;font-family:PM;font-size:21px;letter-spacing:.1em;text-transform:uppercase;color:{INK}}}
.dl span{{display:flex;align-items:center;gap:12px}}.dl span:before{{content:"";width:12px;height:12px;border-radius:50%;background:var(--ac)}}
.free{{position:absolute;left:64px;top:1306px;font-family:HK;font-size:28px;color:{INK}}}
.free b{{font-weight:500;border-bottom:3px solid var(--ac);padding-bottom:2px}}
.tag{{position:absolute;right:64px;bottom:62px;font-family:PM;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:var(--mid)}}
"""
def page(i, body, bg=BONE, fg=INK, mid=ASH, ac='#FF4A1C'):
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}body{{--bg:{bg};--fg:{fg};--mid:{mid};--ac:{ac};--hr:{'#2A2826' if bg==INK else '#D6D3CC'}}}</style></head><body>
<div class="lab l">May11Leven Labs · What we do</div><div class="lab r">{i:02d}/{N:02d}</div><div style="position:absolute;left:64px;right:64px;top:136px;height:2px;background:var(--hr)"></div>{body}</body></html>"""
SV = [  # num, name, accent, digit colour, outcome, deliverables, free way in, proof html, concept tag
 ('01', 'Brand identity', '#B4532A', '#FFFFFF', 'A name, a mark and a system that still works at 16 px and on a shopfront.',
  ['Logo and marks', 'Colour and type', 'Brand guide'], 'Brand clinic for your logo',
  f'<div class="card" style="background:url({D}clinic_wide.png) center/cover"></div>', 'Concept mark'),
 ('02', 'Website design<br>and development', '#2F5D8A', '#FFFFFF', 'Fast, mobile-first sites, designed and built to take bookings and orders while you sleep.',
  ['Design', 'Development', 'Booking, shop, SEO'], 'Homepage review',
  f'''<div class="card" style="background:#DCDDD8;display:flex;align-items:center;justify-content:center"><div style="width:740px;border-radius:14px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.14)">
  <div style="height:40px;background:#F6F6F3;display:flex;align-items:center;gap:8px;padding:0 16px"><i style="width:11px;height:11px;border-radius:50%;background:#D0CFCA"></i><i style="width:11px;height:11px;border-radius:50%;background:#D0CFCA"></i><i style="width:11px;height:11px;border-radius:50%;background:#D0CFCA"></i>
  <span style="margin-left:18px;flex:1;height:24px;border-radius:7px;background:#ECECE8;font:14px PM;color:#6A6A66;display:flex;align-items:center;padding-left:12px">inzu-lakehouse.com</span></div>
  <img src="{D}../kivu/desk_hero.png" style="display:block;width:740px"></div></div>''', 'Concept · Inzu Lake House'),
 ('03', 'App design<br>and development', '#2A45E8', '#FFFFFF', 'iOS, Android and web apps people understand on the first tap, from UX flows to launch.',
  ['UX and UI', 'Development', 'Launch and support'], 'App idea for your business',
  f'''<div class="card" style="background:#E2E5F7"><div style="position:absolute;left:350px;top:18px;width:252px;height:526px;border-radius:42px;background:#111;padding:9px;box-shadow:0 30px 60px rgba(0,0,0,.2)">
  <img src="{D}../remake/hifi/s1.png" style="width:234px;height:508px;object-fit:cover;object-position:top;border-radius:34px;display:block"></div></div>''', 'Concept · fade. barber app'),
 ('04', 'Packaging and 3D', '#C9922E', '#141213', 'Products that look ready to sell before the first unit is made.',
  ['Packaging', '3D product shots', 'Launch reels'], 'Product visual idea',
  f'<div class="card" style="background:url({D}../ata2/ata_wide.png) center 74%/cover"></div>', 'Concept · ata pepper oil'),
 ('05', 'AI automation', '#4F6B3A', '#FFFFFF', 'Assistants that answer, book and take payment on WhatsApp, with your team one tap away.',
  ['Booking bots', 'Payments', 'Staff take over'], 'Sketch of your first chat flow',
  f'''<div class="card" style="background:#E3E8DF"><div style="position:absolute;left:350px;top:18px;width:252px;height:526px;border-radius:42px;background:#111;padding:9px;box-shadow:0 30px 60px rgba(0,0,0,.2)">
  <img src="{D}chat.png" style="width:234px;height:508px;object-fit:cover;object-position:top;border-radius:34px;display:block"></div></div>''', 'Concept · Kora Dental'),
 ('06', 'AI agents', '#1F5E5A', '#FFFFFF', 'Agents that read every enquiry, sort it and draft the reply, so nothing waits until morning.',
  ['Enquiry agents', 'Follow-ups', 'You approve'], 'Agent task map',
  f'''<div class="card" style="background:#DCE6E3"><div style="position:absolute;left:0;top:68px;width:904px;height:424px;border-radius:0 14px 14px 0;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.14);background:#F5F5F2">
  <img src="{D}agent.png" style="display:block;width:1102px;margin-left:-190px"></div></div>''', 'Concept · Lumen Homes'),
 ('07', 'Social and content', '#E8D23A', '#141213', 'A feed that looks like one brand, and content that brings people into your DMs.',
  ['Content systems', 'Reels', 'Feed design'], 'Feed audit',
  f'<div class="card" style="background:url({D}grid.png) center/cover"></div>', 'Our own feed'),
]
S = {}
S[2] = page(2, f"""
<h1 style="top:250px">One studio.<br>Seven ways we help<br>a business <i>grow.</i></h1>
""" + ''.join(f"""<div style="position:absolute;left:64px;right:64px;top:{650+k*92}px;height:2px;background:#D6D3CC"></div>
<div style="position:absolute;left:64px;top:{672+k*92}px;display:flex;align-items:center;gap:22px;font:400 40px IT;letter-spacing:-.02em">
<span style="width:46px;height:46px;border-radius:10px;background:{a}"></span>{n.replace('<br>',' ')}</div>
<div style="position:absolute;right:64px;top:{686+k*92}px;font:21px PM;letter-spacing:.12em;color:{ASH}">{num}</div>""" for k, (num, n, a, *_r) in enumerate(SV)) + f"""
<div style="position:absolute;left:64px;right:64px;top:{650+7*92}px;height:2px;background:#D6D3CC"></div>
<p style="top:1336px;font-size:26px">Every service has its own colour on our page. Swipe for what you get.</p>""")
for k, (num, name, ac, dg, out, dls, free, proof, tag) in enumerate(SV):
    S[3 + k] = page(3 + k, f"""
<div class="num" style="background:{ac};color:{dg}">{num}</div>
<h1 style="top:{340 if '<br>' in name else 360}px;font-size:{70 if '<br>' in name else 84}px">{name}</h1>
<p style="top:{505 if '<br>' in name else 470}px">{out}</p>
{proof}
<div style="position:absolute;left:64px;right:64px;top:1206px;height:2px;background:#D6D3CC"></div><div class="dl" style="top:1236px">{''.join(f'<span>{d}</span>' for d in dls)}</div>
<div class="free">Start free: <b>{free}</b></div>
<div class="tag">{tag}</div>""", ac=ac)
S[10] = page(10, f"""
<svg style="position:absolute;left:64px;top:250px" width="92" height="92" viewBox="0 0 92 92"><rect x="18" y="10" width="16" height="72" fill="#FF4A1C"/><rect x="50" y="20" width="16" height="72" fill="#FF4A1C"/></svg>
<h1 style="top:470px">Pick one.</h1>
<h1 style="top:566px;color:#A8A49D">Or bring us <i style="color:#ECEAE4">all seven.</i></h1>
<p style="top:780px;color:#A8A49D">Comment 11 and the number you need, 01 to 07. Every project starts with a free first look.</p>
<div style="position:absolute;left:64px;top:930px;font:500 34px HK;line-height:1.55;color:{BONE}">hello@may11levenlabs.com<br>may11leven.labs@gmail.com</div>
<div style="position:absolute;left:64px;bottom:72px;font:21px PM;letter-spacing:.12em;color:#8C8884">YOUR TASTE. OUR MACHINES.</div>""", bg=INK, fg=BONE, mid='#A8A49D')
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1440})
        for i, h in S.items():
            f = OUT + f's{i}.html'; open(f, 'w').write(h); await pg.goto('file://' + f); await pg.wait_for_timeout(350)
            await pg.screenshot(path=OUT + f'svc-{i}.png')
        await b.close()
asyncio.run(main()); print('ok')
