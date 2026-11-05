# Moodboards: where they come from and what passes

Zayn's rule: the screenshots and videos he sends ARE our moodboards, above everything else, especially Motto, .raw, Nuevo.Tokyo and every other minimalist piece he shares. Outside sources (Savee and the rest) are only for topping up, and only with work in our style.

## 1. Primary moodboard: Zayn's references (always first)
- **House sheet:** `brand/refs/moodboard-house.jpg`. Motto workbooks and shelf, Nuevo.Tokyo, Holographik (ANI.AI, CoMinVi), Artemii Lebedev, Satto, Aperios and Harvey II on one page. Open it before every job.
- **Folders:** `brand/refs/motto/`, `nuevo-*`, `holographik-*`, `cominvi-*`, `lebedev-*`, `satto-*`, `aperios/`, `harvey/`, `obrazur-*`, `blacklead-*`, `wob-*`, and the reel frame sheets in `brand/refs/reels/` (.raw, WOB, Obrazur, Holographik, Lebedev, Satto and more).
- Every new minimalist piece Zayn sends goes into `brand/refs/<studio>/` and onto the house sheet the same day. Rebuild the sheet with the snippet at the bottom of this file.
- Use it per job: pick 3+ that match the task (a product still, a type page, a UI decision, a reel), and write the steal list (the thinking, never the surface).

## 2. Top-up sources (only when the primary set doesn't cover the job)
- Savee (savee.com; browsing only, since its MCP needs a paid plan)
- Refero Styles
- Minimal Gallery
- Awwwards (Sites of the Day)
- The Brand Identity
- The Logo Archive
- Behance and Dribbble curated pages of the studios above
- Pinterest only through boards of those same studios

Save anything kept to `brand/refs/external/<source>-<name>.jpg`, with its URL and studio in `brand/refs/external/SOURCES.md`. Never use people's faces from these in our work, and never copy a layout.

## 3. The style filter (an outside image must pass ALL of these)
1. **Minimal and calm:** lots of air (about 60% empty), one focal point, nothing shouty.
2. **Restrained colour:** greys, white, black or one material colour, plus at most one accent. No neon gradients, no rainbow palettes.
3. **Refined type:** one neo-grotesk or a refined serif, small mono labels, sentence case. No heavy condensed sentences, no novelty fonts.
4. **Real material and real light:** objects on grey or stone, window light or one soft key. No glossy AI renders, no stock-photo smiles.
5. **A system you can see:** grids, hairlines, construction lines, consistent labels (Motto workbooks, Lebedev's grid, Harvey's overlays).
6. **Product truth:** real UI states and real data, not dribbble-shot fantasy UI.
7. **Would it sit on the house sheet without looking out of place?** If not, drop it.

Reject on sight:
- maximalist collage
- 3D blobs and chrome for their own sake
- glassmorphism stacks
- busy gradient meshes
- "AI art" aesthetics
- trend posters with no idea behind them
- anything that looks like a template

## 4. Rebuild the house sheet
```
cd brand/refs && python3 - <<'EOF'
from PIL import Image; import glob
pick=sorted(glob.glob('motto/*.jpg'))[:9]+sorted(glob.glob('nuevo-*'))[:6]+sorted(glob.glob('holographik-0*'))[:5]+sorted(glob.glob('lebedev-0*'))[:4]+sorted(glob.glob('satto-0*'))[:4]+sorted(glob.glob('aperios/*'))[:4]+sorted(glob.glob('harvey/*'))[:2]+sorted(glob.glob('cominvi-0*'))[:3]
W,H=270,340;cols=8;rows=(len(pick)+cols-1)//cols;s=Image.new('RGB',(cols*W,rows*H),(236,234,228))
for k,x in enumerate(pick):
    im=Image.open(x).convert('RGB');r=max(W/im.width,H/im.height);im=im.resize((int(im.width*r)+1,int(im.height*r)+1));l=(im.width-W)//2;t=(im.height-H)//2
    s.paste(im.crop((l,t,l+W,t+H)),((k%cols)*W,(k//cols)*H))
s.save('moodboard-house.jpg',quality=88)
EOF
```
