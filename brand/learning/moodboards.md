# Moodboards: where they come from and what passes

Zayn's rule: the screenshots and videos he sends ARE our moodboards, above everything else, especially Motto, .raw, Nuevo.Tokyo and every other minimalist piece he shares. Outside sources (Savee and the rest) are only for topping up, and only with work in our style.

## 1. Primary moodboard: Zayn's references (always first)
- **House sheet:** `brand/refs/moodboard-house.jpg`. Motto workbooks and shelf, Nuevo.Tokyo, Holographik (ANI.AI, CoMinVi), Artemii Lebedev, Satto, Aperios and Harvey II on one page. Open it before every job.
- **Folders:** `brand/refs/motto/`, `nuevo-*`, `holographik-*`, `cominvi-*`, `lebedev-*`, `satto-*`, `aperios/`, `harvey/`, `obrazur-*`, `blacklead-*`, `wob-*`, and the reel frame sheets in `brand/refs/reels/` (.raw, WOB, Obrazur, Holographik, Lebedev, Satto and more).
- Every new minimalist piece Zayn sends goes into `brand/refs/<studio>/` and onto the house sheet the same day. Rebuild the sheet with the snippet at the bottom of this file.
- Use it per job: pick 3+ that match the task (a product still, a type page, a UI decision, a reel), and write the steal list (the thinking, never the surface).

## 2. Top-up sources (when the primary set doesn't cover the job)
Zayn's list: Savee, Pinterest, Mobbin, Awwwards, Behance, Cosmos, Destockd and every site he sends. Our own finds have been added below, each picked because its curation leans minimal.

| Source | Best for | Notes |
|---|---|---|
| Savee (savee.com) | mood, art direction, product stills | browsing only; the MCP needs a paid plan |
| Cosmos (cosmos.so) + Public Work (public.work) | calm visual boards; public-domain images | Public Work images are public domain, so usable as texture or reference |
| Pinterest | quick boards | only via boards of studios we trust; lots of noise |
| Mobbin (mobbin.com) | real app screens and flows | free web browsing; the MCP needs a paid plan |
| Awwwards (Sites of the Day) | web craft, motion | design 40 / usability 30 / creativity 20 / content 10 |
| Behance | full case studies | follow Holographik, Lebedev, Motto-level studios only |
| Refero Styles | UI styles and tokens | vendored skill in brand/tools/refero |
| Minimal Gallery, Siteinspire, Httpster, Admire the Web, Dead Simple Sites | minimal websites | our closest web taste |
| Godly, Land-book, Lapa Ninja | web and landing pages | filter hard, many are trendy |
| Storefront, Siiimple, Tiny Blocks | e-commerce pages | for shop concepts (Imisozi-type) |
| Unsection, Design Spells | single sections, micro-interactions | for UI decision posts |
| Fonts In Use | type in real projects | check type pairings before choosing |
| Minimalissimo | minimal objects, architecture, products | close to our product-on-grey look |
| The Brand Identity, The Logo Archive, BP&O | identity systems, marks | logo and brand work |
| Eyecannndy | camera moves and visual effects | reel shot ideas (not to copy) |
| Destockd (destockd.com) | archival film footage you can USE, not just look at | 41,000+ public-domain shots from US government films (FedFlix), with visual search (describe what you see). Free. Good for grainy B&W cutaways (machines, hands, factories, landscapes, skies) in reels. Check its Legal page per clip; no identifiable faces in our work; grade to our world |
| It's Nice That, Ignant, Frame | editorial, spaces | studio-world and set ideas |

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

## 4. Building our own style and identity (keeps evolving)
Moodboards feed our identity; they don't replace it. Each week:
1. Pick the 3 strongest new references (from Zayn first, then our own finds).
2. Write one line in `brand/learning/style.md` under "Identity log": the decision we're taking into our system. Examples:
   - "hairline rules under labels on every carousel (from Motto workbooks and Lebedev's grid)"
   - "one colour per service across the feed"
   - "decision posts with construction lines (from the Harvey clips)"
3. Try it once in a post. If it works, propose it into the matching skill (typography, feed-aesthetic, color, minimalism).
4. Every month, rebuild the house sheet and put our own last 9 posts beside it. Ours should read as one studio and hold up next to them, without copying any of them.

## 5. Rebuild the house sheet
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
