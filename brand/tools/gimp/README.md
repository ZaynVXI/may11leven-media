# GIMP in the May11Leven workflow (GIMP 2.10.36, headless)

## What is installed here
- GIMP 2.10.36 (`gimp-console`), plus `gimp-plugin-registry` (Eg-AddFilmGrain, smart sharpen, high-pass sharpen, colour temperature, B&W film simulation, wavelet denoise and more) and G'MIC 2.9.4 (`gimp-gmic` plug-in and `gmic` CLI).
- GIMP 3 is not available in this workspace (Ubuntu 24.04 ships 2.10; gimp.org is blocked). Scripts must use 2.10 PDB names.

## Files
- `gimp.py`: our driver. It chains steps in one GIMP run (sharpen, highpass, levels, curve, lift, warm, cool, sat, mono, denoise, grain, vignette, shadow, round, scale, crop, canvas, flatten), with `--xcf` for a layered master. Every step was tested on a real photo. Run `python3 gimp.py` with no arguments for the full usage.
- `pdb-2.10.tsv`: every procedure installed here (1,602 lines: name, blurb, argument names). **Look names up here, never guess.** Online examples are often GIMP 3 or Python-Fu 2 and break here.
- `../gimp-reference-levybytes/`: Apache-2.0 reference skill (GIMP 3.2) by LevyBytes. Use it for concepts: layers and modes, masks, selections, curves, ICC, filters and export settings. Its PDB names are GIMP 3, so translate them with `pdb-2.10.tsv`.
- Also studied: Anthonyyp/Ai-Skills gimp-image-editor (no licence, so not copied). Its best idea, dumping the real API before scripting, is what `pdb-2.10.tsv` does.

## Recipes (tested)
```
# finishing pass on a Blender render (export size first, then sharpen last)
python3 gimp.py render.png out.jpg scale:1080 levels:4,250,1.0 curve:10 grain:12 sharpen:1.0,0.3,2
# a cool, matte stock photo for a studio post
python3 gimp.py photo.jpg out.jpg cool:5 sat:-12 lift:10 curve:8 grain:16 sharpen
# B&W archival look (Destockd footage stills, editorial)
python3 gimp.py still.png out.jpg mono curve:16 grain:24 vignette:20
# a UI screenshot mockup card: rounded corners, soft shadow, on a colour canvas, keeping a layered master
python3 gimp.py --xcf card.xcf screen.png card.png round:28 shadow:0,24,60,30 canvas:1600,1100,E6E3EE
# photo on a post-size canvas
python3 gimp.py photo.jpg post.jpg canvas:1080,1440,ECEAE4 grain:14
```

## Clean-up limits (be honest)
- `gmic in.png mask.png inpaint[0] [1],0 keep[0] o out.png` (or `inpaint_morpho`) removes dust, specks and tiny marks on flat or soft areas. On objects it leaves streaks or blur (tested), so don't use it for that; choose another photo instead.
- Never use generative fill or AI object removal on our posts: the image would count as AI-altered.
- Never alter faces, bodies or identity in stock photos. Only crop, tone and remove specks.
- Check every edit at 100% (crop the area and look) before export.
