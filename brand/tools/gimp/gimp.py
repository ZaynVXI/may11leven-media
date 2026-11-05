#!/usr/bin/env python3
"""May11Leven GIMP 2.10 finishing driver (headless). Chains steps in ONE gimp-console run.
Every PDB name used here is checked against brand/tools/gimp/pdb-2.10.tsv (the installed GIMP's real list).

usage:
  gimp.py in.png out.jpg  step[:args] step[:args] ...
  gimp.py --xcf master.xcf in.png out.jpg ...      also keeps a layered master
steps (args are comma separated, all optional):
  sharpen:radius,amount,threshold      unsharp mask at export size (default 1.0,0.3,2)
  highpass:opacity                     high-pass sharpen on a separate overlay layer (default 35)
  levels:low,high,gamma                tonal range 0-255 (default 4,250,1.0)
  curve:strength                       gentle S-curve, 0-40 (default 12)
  lift:amount                          lift blacks for a matte film look, 0-40 (default 10)
  warm:amount / cool:amount            colour balance in midtones, 0-30 (default 6)
  sat:amount                           saturation -100..100 (default -10)
  mono                                 luminance greyscale
  denoise                              wavelet denoise (photos only)
  grain:amount                         fine monochrome grain, 0-60 (default 18)
  vignette:strength                    soft radial darkening, 0-100 (default 25)
  shadow:x,y,blur,opacity              drop shadow behind a cut-out layer (default 0,24,60,35)
  round:radius                         rounded corners on a transparent canvas (default 40)
  scale:w,h                            NoHalo resize (keep aspect if h=0)
  crop:x,y,w,h                         crop rectangle
  canvas:w,h,hex,fill                  place the image centred on a w x h canvas of colour hex, scaled down to fit within fill (default 0.86)
  flatten
"""
import os, subprocess, sys, shlex
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def num(a, i, d):
    try: return float(a[i]) if a[i] != '' else d
    except IndexError: return d
def step(name, a):
    # each returns Script-Fu using variables img and dr (active drawable)
    if name == 'sharpen':
        return f'(plug-in-unsharp-mask RUN-NONINTERACTIVE img dr {num(a,0,1.0)} {num(a,1,0.3)} {int(num(a,2,2))})'
    if name == 'highpass':
        op = num(a, 0, 35)
        return f'''(let* ((hp (car (gimp-layer-copy dr FALSE))))
  (gimp-image-insert-layer img hp 0 -1) (gimp-drawable-desaturate hp DESATURATE-LUMINANCE)
  (let* ((bl (car (gimp-layer-copy hp FALSE)))) (gimp-image-insert-layer img bl 0 -1)
    (plug-in-gauss RUN-NONINTERACTIVE img bl 6 6 0) (gimp-layer-set-mode bl LAYER-MODE-GRAIN-EXTRACT)
    (set! hp (car (gimp-image-merge-down img bl EXPAND-AS-NECESSARY))))
  (gimp-layer-set-mode hp LAYER-MODE-OVERLAY) (gimp-layer-set-opacity hp {op}) (gimp-item-set-name hp "high-pass")
  (set! dr (car (gimp-image-merge-down img hp EXPAND-AS-NECESSARY))))'''
    if name == 'levels':
        lo, hi, g = num(a, 0, 4) / 255, num(a, 1, 250) / 255, num(a, 2, 1.0)
        return f'(gimp-drawable-levels dr HISTOGRAM-VALUE {lo:.4f} {hi:.4f} TRUE {g} 0 1 TRUE)'
    if name == 'curve':
        s = num(a, 0, 12) / 255
        pts = [0, 0, .25, .25 - s, .5, .5, .75, .75 + s, 1, 1]
        return f'(gimp-drawable-curves-spline dr HISTOGRAM-VALUE {len(pts)} #({" ".join(f"{p:.4f}" for p in pts)}))'
    if name == 'lift':
        l = num(a, 0, 10) / 255
        return f'(gimp-drawable-curves-spline dr HISTOGRAM-VALUE 6 #(0 {l:.4f} 0.5 0.5 1 0.98))'
    if name in ('warm', 'cool'):
        v = num(a, 0, 6) * (1 if name == 'warm' else -1)
        return f'(gimp-drawable-color-balance dr TRANSFER-MIDTONES TRUE {v} 0 {-v})'
    if name == 'sat':
        return f'(gimp-drawable-hue-saturation dr HUE-RANGE-ALL 0 0 {num(a,0,-10)} 0)'
    if name == 'mono':
        return '(gimp-drawable-desaturate dr DESATURATE-LUMINANCE)'
    if name == 'denoise':
        return '(plug-in-wavelet-denoise RUN-NONINTERACTIVE img dr)'
    if name == 'grain':
        g = int(num(a, 0, 18))
        return f'''(let* ((w (car (gimp-image-width img))) (h (car (gimp-image-height img)))
       (gl (car (gimp-layer-new img w h RGBA-IMAGE "grain" 100 LAYER-MODE-OVERLAY))))
  (gimp-image-insert-layer img gl 0 -1) (gimp-context-set-foreground '(128 128 128)) (gimp-drawable-fill gl FILL-FOREGROUND)
  (plug-in-rgb-noise RUN-NONINTERACTIVE img gl FALSE FALSE {g/255:.4f} {g/255:.4f} {g/255:.4f} 0)
  (gimp-drawable-desaturate gl DESATURATE-LUMINANCE) (plug-in-gauss RUN-NONINTERACTIVE img gl 0.6 0.6 0)
  (set! dr (car (gimp-image-merge-down img gl EXPAND-AS-NECESSARY))))'''
    if name == 'vignette':
        s = num(a, 0, 25)
        return f'''(let* ((w (car (gimp-image-width img))) (h (car (gimp-image-height img)))
       (vl (car (gimp-layer-new img w h RGBA-IMAGE "vignette" {s} LAYER-MODE-MULTIPLY))))
  (gimp-image-insert-layer img vl 0 -1) (gimp-context-set-foreground '(0 0 0)) (gimp-context-set-background '(255 255 255))
  (gimp-context-set-gradient-fg-bg-rgb) (gimp-drawable-edit-gradient-fill vl GRADIENT-RADIAL 0 FALSE 1 0 TRUE (/ w 2) (/ h 2) (* (max w h) 0.75) (/ h 2))
  (gimp-drawable-invert vl FALSE)
  (set! dr (car (gimp-image-merge-down img vl EXPAND-AS-NECESSARY))))'''
    if name == 'shadow':
        x, y, b, o = num(a, 0, 0), num(a, 1, 24), num(a, 2, 60), num(a, 3, 35)
        return f"(script-fu-drop-shadow img dr {x} {y} {b} '(0 0 0) {o} TRUE) (set! dr (car (gimp-image-get-active-drawable img)))"
    if name == 'round':
        r = int(num(a, 0, 40))
        return f"(script-fu-round-corners img dr {r} FALSE 0 0 0 FALSE FALSE) (set! dr (car (gimp-image-get-active-drawable img)))"
    if name == 'scale':
        w, h = int(num(a, 0, 1080)), int(num(a, 1, 0))
        hs = f'{h}' if h else f'(round (* {w} (/ (car (gimp-image-height img)) (car (gimp-image-width img)))))'
        return f'(gimp-context-set-interpolation INTERPOLATION-NOHALO) (gimp-image-scale img {w} {hs})'
    if name == 'crop':
        return f'(gimp-image-crop img {int(num(a,2,0))} {int(num(a,3,0))} {int(num(a,0,0))} {int(num(a,1,0))})'
    if name == 'canvas':
        w, h = int(num(a, 0, 1080)), int(num(a, 1, 1440)); c = a[2] if len(a) > 2 else 'ECEAE4'
        rgb = ' '.join(str(int(c[i:i + 2], 16)) for i in (0, 2, 4))
        m = num(a, 3, 0.86)  # largest share of the canvas the image may fill
        return f'''(let* ((ow (car (gimp-image-width img))) (oh (car (gimp-image-height img)))
       (k (min 1 (/ (* {w} {m}) ow) (/ (* {h} {m}) oh))))
  (if (< k 1) (begin (gimp-context-set-interpolation INTERPOLATION-NOHALO) (gimp-image-scale img (round (* ow k)) (round (* oh k)))
                     (set! ow (car (gimp-image-width img))) (set! oh (car (gimp-image-height img)))))
  (gimp-image-resize img {w} {h} (/ (- {w} ow) 2) (/ (- {h} oh) 2))
  (let* ((bg (car (gimp-layer-new img {w} {h} RGB-IMAGE "bg" 100 LAYER-MODE-NORMAL))))
    (gimp-image-insert-layer img bg 0 (car (gimp-image-get-item-position img dr))) (gimp-context-set-foreground '({rgb})) (gimp-drawable-fill bg FILL-FOREGROUND)
    (gimp-image-lower-item-to-bottom img bg)))'''
    if name == 'flatten':
        return '(set! dr (car (gimp-image-flatten img)))'
    raise SystemExit(f'unknown step {name}')
def main():
    args = sys.argv[1:]; xcf = None
    if args and args[0] == '--xcf': xcf, args = args[1], args[2:]
    src, out, steps = args[0], args[1], args[2:]
    body = '\n'.join(step(s.split(':')[0], s.split(':')[1].split(',') if ':' in s else []) for s in steps)
    save = ''
    if xcf: save += f'(gimp-xcf-save RUN-NONINTERACTIVE img dr {q(xcf)} {q(xcf)})\n'
    ext = out.lower().rsplit('.', 1)[-1]
    if ext in ('jpg', 'jpeg'):
        save += f'(set! dr (car (gimp-image-flatten img))) (file-jpeg-save RUN-NONINTERACTIVE img dr {q(out)} {q(out)} 0.94 0 1 1 "" 2 1 0 0)'
    else:
        save += f'(set! dr (car (gimp-image-merge-visible-layers img CLIP-TO-IMAGE))) (file-png-save2 RUN-NONINTERACTIVE img dr {q(out)} {q(out)} FALSE 9 FALSE FALSE FALSE FALSE FALSE FALSE FALSE)'
    sf = f'''(let* ((img (car (gimp-file-load RUN-NONINTERACTIVE {q(src)} {q(src)})))
       (dr (car (gimp-image-get-active-drawable img))))
  (gimp-image-undo-disable img)
  {body}
  {save}
  (gimp-image-delete img))
(gimp-quit 0)'''
    if os.environ.get('GIMP_DEBUG'): print(sf)
    r = subprocess.run(['gimp-console', '-i', '-d', '-f', '-b', sf], capture_output=True, text=True, timeout=600)
    err = [l for l in (r.stdout + r.stderr).splitlines() if ('Error' in l or 'error' in l) and 'deprecated' not in l]
    if err or not os.path.exists(out): print('\n'.join(err) or 'no output'); sys.exit(1)
    print('ok', out)
if __name__ == '__main__': main()
