#!/bin/sh
# GIMP 2.10 batch helper for finishing passes (free, runs headless).
# usage: gimp.sh <op> in.jpg out.jpg [args]
#   sharpen  in out [radius=1.2 amount=0.35 threshold=2]   unsharp mask for final export
#   levels   in out [low=0 high=255 gamma=1.0]             tonal range on the whole image
#   desat    in out                                        luminosity greyscale
#   scale    in out W H                                    high-quality resize (NoHalo)
#   grain    in out [amount=0.04]                          fine film grain (HSV noise)
# Use for retouch-style finishing after Blender/PIL/HTML; keep edits subtle and check at 100%.
op=$1; in=$2; out=$3; shift 3
load="(img (car (gimp-file-load RUN-NONINTERACTIVE \"$in\" \"$in\"))) (dr (car (gimp-image-get-active-drawable img)))"
save="(gimp-image-flatten img) (set! dr (car (gimp-image-get-active-drawable img))) (gimp-file-save RUN-NONINTERACTIVE img dr \"$out\" \"$out\")"
case $op in
  sharpen) body="(plug-in-unsharp-mask RUN-NONINTERACTIVE img dr ${1:-1.2} ${2:-0.35} ${3:-2})";;
  levels)  body="(gimp-drawable-levels dr HISTOGRAM-VALUE $(echo "${1:-0}/255" | bc -l) $(echo "${2:-255}/255" | bc -l) TRUE ${3:-1.0} 0 1 TRUE)";;
  desat)   body="(gimp-drawable-desaturate dr DESATURATE-LUMINANCE)";;
  scale)   body="(gimp-context-set-interpolation INTERPOLATION-NOHALO) (gimp-image-scale img $1 $2)";;
  grain)   body="(plug-in-hsv-noise RUN-NONINTERACTIVE img dr 2 0 0 $(echo "${1:-0.04}*255/1" | bc))";;
  *) echo "unknown op $op"; exit 1;;
esac
gimp-console -i -d -f -b "(let* ($load) $body $save (gimp-quit 0))" 2>&1 | grep -v -E "GEGL|leaked|batch command" || true
[ -f "$out" ] && echo "ok $out"
