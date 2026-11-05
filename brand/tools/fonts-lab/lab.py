"""Font lab: coverage for African Latin, Arabic, Ge'ez and our currencies + a confusable-letter legibility score.
usage: python3 lab.py  -> report.md, report.json, sheet.png"""
import glob, json, os, numpy as np
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
NM = '/home/claude/fonts-lab/node_modules/@fontsource/'
SETS = {
 'Yoruba': 'ẹọṣẸỌṢńŃ̀́',
 'Igbo': 'ịọụṅỊỌỤṄ',
 'Hausa': 'ɓɗƙƴƁƊƘƳ',
 'Akan/Ewe/Lingala/Wolof': 'ɛɔŋƐƆŊɖʋɣƒ',
 'Currency ₦ ₵': '₦₵€£',
 'Arabic': 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي٠١٢٣',
 'Ge\'ez (Amharic)': 'ሀለሐመሠረሰ',
}
def cmap_of(fam):
    cps = set(); files = [f for f in glob.glob(NM + fam + '/files/*-400-normal.woff2')]
    if not files: files = glob.glob(NM + fam + '/files/*-normal.woff2')[:6]
    for f in files:
        try: cps |= set(TTFont(f).getBestCmap().keys())
        except Exception: pass
    return cps, files
def ttf_for_render(files):
    # prefer the latin subset for the legibility test
    lat = [f for f in files if '-latin-400' in f] or files
    t = TTFont(lat[0]); p = '/tmp/claude-0/-home-claude/9bb6ffdd-e2cc-582d-b0a9-f807871f658c/scratchpad/' + os.path.basename(lat[0]) + '.ttf'
    t.flavor = None; t.save(p); return p
def glyph(font, ch, S=160):
    im = Image.new('L', (S, S), 0); d = ImageDraw.Draw(im); d.text((S // 2, S // 2), ch, font=font, fill=255, anchor='mm')
    a = np.array(im) > 128; ys, xs = np.nonzero(a)
    if len(xs) == 0: return np.zeros((64, 64), bool)
    c = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    return np.array(Image.fromarray(c.astype(np.uint8) * 255).resize((64, 64))) > 128
def sim(a, b): return (a & b).sum() / max(1, (a | b).sum())
PAIRS = [('I', 'l'), ('l', '1'), ('I', '1'), ('O', '0'), ('rn', 'm'), ('b', 'd'), ('cl', 'd')]
out = []
for fam in sorted(os.listdir(NM)):
    cps, files = cmap_of(fam)
    if not files: continue
    cov = {k: round(sum(ord(c) in cps for c in v) / len(v) * 100) for k, v in SETS.items()}
    f = ImageFont.truetype(ttf_for_render(files), 120)
    conf = {f'{a}/{b}': round(float(sim(glyph(f, a), glyph(f, b))), 2) for a, b in PAIRS}
    # x-height ratio
    tt = TTFont(files[0]); os2 = tt['OS/2']; upm = tt['head'].unitsPerEm
    xh = round(getattr(os2, 'sxHeight', 0) / upm, 3) if getattr(os2, 'sxHeight', 0) else None
    worst = max(conf['I/l'], conf['l/1'], conf['I/1'])
    out.append(dict(font=fam, coverage=cov, confusable=conf, worst_Il1=worst, x_height=xh))
json.dump(out, open('report.json', 'w'), indent=1)
L = ['| font | x-height | I/l/1 worst (lower = clearer) | O/0 | rn/m | ' + ' | '.join(SETS) + ' |', '|' + '---|' * (5 + len(SETS))]
for r in sorted(out, key=lambda r: r['worst_Il1']):
    L.append(f"| {r['font']} | {r['x_height']} | {r['worst_Il1']} | {r['confusable']['O/0']} | {r['confusable']['rn/m']} | " + ' | '.join(f"{r['coverage'][k]}%" for k in SETS) + ' |')
open('report.md', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L))
# specimen sheet: Il1 0O rn m + Yoruba/Hausa line for every font
fs = sorted(out, key=lambda r: r['worst_Il1']); H = 120 * len(fs) + 40
sh = Image.new('RGB', (2000, H), (244, 244, 242)); d = ImageDraw.Draw(sh)
mono = ImageFont.truetype('/home/claude/kit/fonts/IBMPlexMono-Regular.ttf', 22) if os.path.exists('/home/claude/kit/fonts/IBMPlexMono-Regular.ttf') else ImageFont.load_default()
for i, r in enumerate(fs):
    cps, files = cmap_of(r['font']); ff = [x for x in files if 'latin-ext-400' in x] or files
    p = ttf_for_render(files); y = 30 + i * 120
    d.text((30, y + 34), r['font'], font=mono, fill=(90, 90, 88))
    f = ImageFont.truetype(p, 64); d.text((420, y), 'Il1 O0 rn m  Ọjà ẹ̀wà · ɓarna', font=f, fill=(20, 20, 20))
sh.save('sheet.png'); print('sheet ok')
