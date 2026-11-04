"""Accessibility hook for our Pillow post scripts.
Import before running a post script. Every ImageDraw.text call is checked:
- background = median colour of the pixels under the text box (before drawing)
- needs 4.5:1, or 3:1 when the font is large (>= 48 px on a 1080 canvas)
Mode FIX=1 nudges the text colour toward black or white until it passes,
keeping its hue (so the opacity hierarchy survives, just with a floor).
Also enforces a minimum font size (MINPX, default 20) for readability on phones.
"""
import os, json, atexit
import numpy as np
from PIL import ImageDraw, ImageFont

FIX = os.environ.get('FIX', '0') == '1'
MINPX = int(os.environ.get('MINPX', '20'))
LOG = os.environ.get('A11YLOG', '/home/claude/a11y/log.jsonl')
_rows = []

def _lin(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)

def lum(rgb):
    r, g, b = _lin(np.array(rgb[:3], dtype=float))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + 0.05) / (y + 0.05)

def _mix(a, b, t):
    return tuple(int(round(a[i] * (1 - t) + b[i] * t)) for i in range(3))

_orig_text = ImageDraw.ImageDraw.text
_orig_truetype = ImageFont.truetype

def _truetype(font=None, size=10, *a, **k):
    if size < MINPX:
        size = MINPX
    return _orig_truetype(font, size, *a, **k)
ImageFont.truetype = _truetype

def _text(self, xy, text, fill=None, font=None, *a, **k):
    try:
        if fill is not None and isinstance(fill, tuple) and len(fill) >= 3 and str(text).strip() and self.im is not None:
            img = getattr(self, '_image', None)
            f = font or self.getfont()
            bb = self.textbbox(xy, text, font=f, anchor=k.get('anchor'))
            W, H = self.im.size
            x0, y0 = max(0, int(bb[0])), max(0, int(bb[1]))
            x1, y1 = min(W, int(bb[2]) + 1), min(H, int(bb[3]) + 1)
            if x1 > x0 and y1 > y0 and img is not None:
                reg = np.asarray(img.convert('RGB').crop((x0, y0, x1, y1))).reshape(-1, 3)
                bg = tuple(int(v) for v in np.median(reg, axis=0))
                size = getattr(f, 'size', 12)
                need = 3.0 if size >= 48 else 4.5
                r0 = ratio(fill, bg)
                newfill = fill
                if r0 < need and FIX:
                    first = (0, 0, 0) if lum(bg) > 0.18 else (255, 255, 255)
                    for tgt in (first, (255, 255, 255) if first == (0, 0, 0) else (0, 0, 0)):
                        t = 0.0; newfill = fill[:3]
                        while ratio(newfill, bg) < need and t < 1:
                            t += 0.02
                            newfill = _mix(fill[:3], tgt, t)
                        if ratio(newfill, bg) >= need: break
                    if len(fill) == 4:
                        newfill = newfill + (fill[3],)
                if r0 < need:
                    _rows.append(dict(script=os.environ.get('A11YNAME', '?'), text=str(text)[:40], size=size,
                                      fill=fill[:3], bg=bg, ratio=round(r0, 2), need=need,
                                      fixed=newfill[:3] if FIX else None, after=round(ratio(newfill,bg),2)))
                fill = newfill
    except Exception as e:
        _rows.append(dict(script=os.environ.get('A11YNAME', '?'), error=str(e)[:80]))
    return _orig_text(self, xy, text, fill, font, *a, **k)
ImageDraw.ImageDraw.text = _text

# keep a handle on the image for each Draw
_orig_init = ImageDraw.ImageDraw.__init__
def _init(self, im, mode=None):
    _orig_init(self, im, mode)
    self._image = im
ImageDraw.ImageDraw.__init__ = _init

_busy = [False]
_orig_text2 = ImageDraw.ImageDraw.text
def _text_guard(self, xy, text, fill=None, font=None, *a, **k):
    if _busy[0]:
        return _orig_text(self, xy, text, fill, font, *a, **k)
    return _orig_text2(self, xy, text, fill, font, *a, **k)
ImageDraw.ImageDraw.text = _text_guard

def _check_fill(d, x, y, s, f, fill):
    """Return a passing fill for a whole string drawn with mm.tt."""
    if not (isinstance(fill, tuple) and len(fill) >= 3 and s.strip()):
        return fill
    img = d._image
    W, H = img.size
    wpx = f.getlength(s) * 1.25 + 4
    bb = f.getbbox(s)
    x0, y0, x1, y1 = max(0, int(x)), max(0, int(y + bb[1])), min(W, int(x + wpx)), min(H, int(y + bb[3]) + 1)
    if x1 <= x0 or y1 <= y0:
        return fill
    reg = np.asarray(img.convert('RGB').crop((x0, y0, x1, y1))).reshape(-1, 3)
    # worst case: the background pixel closest in luminance to the text
    lums = np.array([lum(p) for p in reg[::max(1, len(reg)//600)]])
    lf = lum(fill)
    # contrast of each background pixel vs the original fill; take the 20th percentile
    # so thin same-colour borders (tags, rules) don't count, but busy photos do
    rat = (np.maximum(lums, lf) + 0.05) / (np.minimum(lums, lf) + 0.05)
    bgl = lums[np.argsort(rat)[int(len(rat) * 0.2)]]
    bg = tuple(int(v) for v in np.median(reg, axis=0))
    def rr(c):
        a_, b_ = sorted([lum(c), bgl], reverse=True); return (a_ + 0.05) / (b_ + 0.05)
    need = 3.0 if f.size >= 48 else 4.5
    r0 = rr(fill)
    nf = fill
    if r0 < need and FIX:
        first = (0, 0, 0) if lum(bg) > 0.18 else (255, 255, 255)
        for tgt in (first, (255, 255, 255) if first == (0, 0, 0) else (0, 0, 0)):
            t = 0.0; nf = fill
            while rr(nf) < need and t < 1:
                t += 0.02
                nf = _mix(fill[:3], tgt, t) + tuple(fill[3:4])
            if rr(nf) >= need: break
    if r0 < need:
        _rows.append(dict(script=os.environ.get('A11YNAME', '?'), text=s[:40], size=f.size, fill=fill[:3], bg=bg,
                          ratio=round(r0, 2), need=need, fixed=nf[:3] if FIX else None, after=round(rr(nf),2)))
    return nf

def patch_mm():
    import sys
    sys.path.insert(0, '/home/claude/remake/v3')
    import mm
    orig_tt = mm.tt
    def tt(d, x, y, s, f, fill, tr=0.0):
        fill2 = _check_fill(d, x, y, s, f, fill)
        _busy[0] = True
        try:
            orig_tt(d, x, y, s, f, fill2, tr)
        finally:
            _busy[0] = False
    mm.tt = tt
patch_mm()

@atexit.register
def _dump():
    with open(LOG, 'a') as fh:
        for r in _rows:
            fh.write(json.dumps(r) + '\n')
