import json
g = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'a.json')))
S = 0.36  # font units -> px
W, H = 1080, 1350
X0 = (W - g['adv'] * S) / 2; BASE = 900
def tx(x, y): return (X0 + x * S, BASE - y * S)
d = []; pts_on = []; pts_off = []; handles = []; last = None
for op, args in g['ops']:
    if op == 'moveTo':
        x, y = tx(*args[0]); d.append(f'M{x:.1f},{y:.1f}'); pts_on.append((x, y)); last = (x, y)
    elif op == 'lineTo':
        x, y = tx(*args[0]); d.append(f'L{x:.1f},{y:.1f}'); pts_on.append((x, y)); last = (x, y)
    elif op == 'qCurveTo':
        P = [tx(*a) for a in args]
        # expand implied on-curve points for TrueType quadratics
        segs = []; ctrl = P[:-1]; end = P[-1]
        for i, c in enumerate(ctrl):
            nxt = end if i == len(ctrl) - 1 else ((c[0] + ctrl[i + 1][0]) / 2, (c[1] + ctrl[i + 1][1]) / 2)
            d.append(f'Q{c[0]:.1f},{c[1]:.1f} {nxt[0]:.1f},{nxt[1]:.1f}')
            handles.append((last, c)); handles.append((c, nxt)); pts_off.append(c); last = nxt
        pts_on.append(end)
    elif op == 'curveTo':
        c1, c2, e = [tx(*a) for a in args]
        d.append(f'C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {e[0]:.1f},{e[1]:.1f}')
        handles += [(last, c1), (c2, e)]; pts_off += [c1, c2]; pts_on.append(e); last = e
    elif op in ('closePath', 'endPath'):
        d.append('Z')
path = ' '.join(d)
guides = [('BASELINE', 0), ('X-HEIGHT', g['xh']), ('CAP HEIGHT', g['cap'])]
gl = ''.join(f'<line x1="72" x2="1008" y1="{BASE - v * S:.1f}" y2="{BASE - v * S:.1f}" class="g"/><text x="72" y="{BASE - v * S - 12:.1f}" class="m">{n} · {v}</text>' for n, v in guides)
hl = ''.join(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" class="h"/>' for a, b in handles)
on = ''.join(f'<rect x="{x - 6:.1f}" y="{y - 6:.1f}" width="12" height="12" class="on"/>' for x, y in pts_on)
off = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="off"/>' for x, y in pts_off)
css = '''
@font-face{font-family:IT;src:url(../../brand/fonts/InterTight-Medium.ttf);font-weight:500}
@font-face{font-family:IT;src:url(../../brand/fonts/InterTight-Regular.ttf);font-weight:400}
@font-face{font-family:IT;src:url(../../brand/fonts/InterTight-Light.ttf);font-weight:300}
@font-face{font-family:IS;src:url(../../brand/fonts/InstrumentSerif-Italic.ttf)}
@font-face{font-family:PM;src:url(../../brand/fonts/PlexMonoMed.ttf)}
*{margin:0;box-sizing:border-box} body{width:1080px;height:1350px;background:#EDEDEF;color:#141213;font-family:IT;position:relative;overflow:hidden}
.lab{position:absolute;top:72px;left:72px;right:72px;display:flex;justify-content:space-between;font:22px PM;letter-spacing:.08em;color:#141213;opacity:.72}
.foot{position:absolute;bottom:72px;left:72px;right:72px;display:flex;justify-content:space-between;font:22px PM;letter-spacing:.08em;opacity:.72}
svg text.m{font:20px PM;letter-spacing:.06em;text-transform:uppercase;fill:#B8321A}
.g{stroke:#FF4A1C;stroke-width:1.5;stroke-dasharray:7 7}
.h{stroke:#141213;stroke-width:1.2;opacity:.55}
.on{fill:#141213}.off{fill:#EDEDEF;stroke:#141213;stroke-width:1.6}
'''
def page(name, body, tag):
    open(name, 'w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{css}</style></head><body><div class="lab"><span>MAY11LEVEN LABS</span><span>{tag}</span></div>{body}</body></html>')
page('s1.html', f'<svg width="1080" height="1350" style="position:absolute;inset:0">{gl}<path d="{path}" fill="none" stroke="#141213" stroke-width="2"/>{hl}{on}{off}</svg><div class="foot"><span>INTER TIGHT MEDIUM · LOWERCASE A</span><span>01 / 05</span></div>', 'TYPE STUDY')
spec = ''.join(f'<div style="display:flex;align-items:baseline;gap:40px;border-top:1px solid rgba(20,18,19,.18);padding:26px 0"><span style="font:20px PM;letter-spacing:.08em;width:190px;opacity:.72">{lab}</span><span style="font-weight:{w};font-size:{sz}px;letter-spacing:-.03em;line-height:1">{t}</span></div>' for lab, w, sz, t in [('LIGHT 300', 300, 120, 'Quiet'), ('REGULAR 400', 400, 120, 'work'), ('MEDIUM 500', 500, 120, 'that'), ('SERIF ITALIC', 0, 0, '')])
spec = spec.replace('<span style="font-weight:0;font-size:0px;letter-spacing:-.03em;line-height:1"></span>', '<span style="font-family:IS;font-size:132px;line-height:1">sells.</span>')
page('s2.html', f'<div style="position:absolute;left:72px;right:72px;top:250px">{spec}</div><div class="foot"><span>ONE GROTESK · ONE SERIF · ONE MONO</span><span>02 / 05</span></div>', 'TYPE STUDY')
s = 3.0; bw, gap, bh, off = 41 * s, 29 * s, 181 * s, 30 * s
x1 = (1080 - (2 * bw + gap)) / 2; x2 = x1 + bw + gap; top = 390
dim = lambda x1_, y1_, x2_, y2_, t, tx_, ty_: f'<line x1="{x1_}" y1="{y1_}" x2="{x2_}" y2="{y2_}" stroke="#141213" stroke-width="1.2"/><text x="{tx_}" y="{ty_}" class="d">{t}</text>'
grid = ''.join(f'<line x1="{x1 + i * bw / 2:.1f}" x2="{x1 + i * bw / 2:.1f}" y1="300" y2="1080" class="gr"/>' for i in range(0, 7)) + ''.join(f'<line y1="{top + j * 30 * s:.1f}" y2="{top + j * 30 * s:.1f}" x1="200" x2="880" class="gr"/>' for j in range(0, 8))
svg3 = f'''<svg width="1080" height="1350" style="position:absolute;inset:0"><style>.gr{{stroke:#141213;stroke-width:.8;opacity:.14}} text.d{{font:20px PM;letter-spacing:.06em;fill:#141213}}</style>{grid}
<rect x="{x1:.1f}" y="{top}" width="{bw:.1f}" height="{bh:.1f}" fill="#FF4A1C"/><rect x="{x2:.1f}" y="{top + off:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="#FF4A1C"/>
{dim(x1, top - 40, x1 + bw, top - 40, '41', x1 + bw / 2 - 12, top - 54)}{dim(x1 + bw, top - 40, x2, top - 40, '29', x1 + bw + gap / 2 - 12, top - 54)}
{dim(x1 - 40, top, x1 - 40, top + bh, '181', x1 - 96, top + bh / 2)}{dim(x2 + bw + 40, top + bh, x2 + bw + 40, top + bh + off, '30', x2 + bw + 54, top + bh + off / 2 + 7)}</svg>'''
page('s3.html', svg3 + '<div style="position:absolute;left:72px;right:72px;top:1110px;font:500 44px IT;letter-spacing:-.02em;line-height:1.1">Two bars. One offset.<br><span style="font-family:IS;font-weight:400;font-size:52px">The eleven, measured.</span></div><div class="foot"><span>MARK · UNITS IN PX AT 1X</span><span>03 / 05</span></div>', 'MARK STUDY')
page('s5.html', '<div style="position:absolute;left:72px;right:72px;top:400px;font:500 92px IT;letter-spacing:-.035em;line-height:1">People judge a business<br><span style="font-family:IS;font-weight:400;font-size:106px">before they read a word.</span></div><div style="position:absolute;left:72px;right:72px;top:820px;font:400 30px IT;line-height:1.4;max-width:860px">We measure the letters, the mark and the system so your brand looks as trustworthy as the work behind it. Brand identity, websites, apps, 3D, automation, AI agents and content.<br><br>Comment 11 for a free first look at yours.</div><div class="foot"><span>HELLO@MAY11LEVENLABS.COM</span><span>05 / 05</span></div>', 'MAY11LEVEN LABS')
