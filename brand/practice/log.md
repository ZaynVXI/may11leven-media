# Practice log (never posted)
## 01: minimal redesign of the four week-2/3 posts
Files: thu-brand-clinic.jpg, fri-barber-app.jpg, sun-inzu-web.jpg (code in brand/code/v3, kit mm.py).
Scores (1-5): idea 4 · type 4 · colour 4 · air 4 · finish 3 · truth 5.
Feedback: "okay", not yet top studio.
Honest gaps vs Holographik:
- Statement cards, tags and close cards repeat the same template across all four posts, so the products still feel alike. Holographik changes the whole system per project.
- No hero object: they always have one real thing (a 3D rock, a coin between hands, a mirror cube). Ours lean on text cards and line diagrams.
- Diagrams are correct but schematic; theirs are data that looks like art (constellations, map glow, wireframe machines).
- Photos are borrowed warm stock-like scenes; theirs feel shot or rendered for the project.
Fixes to practise next:
- Give each concept its own layout system and type behaviour, not just new colours.
- Build one hero object per project (Blender or 3D in code) and make it the cover.
- Push one data graphic per post until it reads as art at thumbnail size.
## 02: barber app UI rebuilt at high fidelity
Feedback: the app screen looked low fidelity and basic. Rebuilt as a dark product UI (brand/code/hifi/app.html): live-queue tick ring with big numeral, real queue states, busy-hours chart, service rows with real photo thumbnails from the shoot, quiet-hour slots with discounts, M-Pesa checkout with countdown ring, iOS status bar, tab bar with icons. Re-composited into the phone photo; slide 5 is now a three-screen collage.
Lesson: show finished product states, never wireframe-level screens.
## 03: Bathu rebrand concept rebuilt
Old post: heavy condensed type, outline letters, flat laptop. New: 3D rendered soles (ink + gum rubber, tread with the wordmark) on concrete as the hero, a question card in a visible grid (Lebedev), the mark constructed with dashed lines, a dot map of South Africa from Alexandra (CoMinVi), a named street palette, rendered shoeboxes.
Fixes during lookdev: sole outline faceted -> Chaikin smoothing; tread streaks on side walls -> bump only on top faces; pale lid print -> decal specular off (grazing-angle Fresnel).
## 04: ata reel and Imisozi rebuilt
- ata: same renders, new minimal type, a spec page for the label, cover without text.
- Imisozi: 3D coffee pouches rendered in Blender (bevelled block, flat seal, label via Generated coords), a full shop (home, shop all, product, bag with MoMo) in HTML at 2x/3x, presented Lebedev/Satto-style as stacked pages on a blurred hills photo.
## 05: ata bottle re-rendered at full fidelity
Feedback: the bottle still looked low quality. New scene (brand/code/ata2/bottle2.py): 3 mm solidified glass with micro bump, oil with meniscus and volume absorption (density 140), knurled cap with coat, paper label with fibre bump, lobed wrinkled scotch bonnet with subsurface and coat, basalt slab, two tall strip lights for glass edges, a backlight through the oil, AgX, 24 bounces, 64 samples + denoise.

## 06 Accessibility pass
Built a contrast checker into the render pipeline and re-rendered every scheduled post. Two bugs caught on review: tag borders read as background (fixed with a 20th-percentile background), and tag boxes not growing with bigger text (mm.tag now sizes from the font).

## 07 Reel: opacity list (practice/reels/opacity-list-v1.mp4 -> v2.mp4)
After Holographik's CoMinVi values list. 8 s, Bone, six services, active row Ink, rest 18%, Infrared dot, counter, 11 mark, loop.
- v1 scores: idea 3 · type 4 · colour 4 · air 4 · fidelity 3 · finish 3 · truth 5. Gaps: soft 4-frame crossfades and an eased dot made it feel like a slideshow (Holographik steps hard); the list flew up and left ~0.5 s of empty grid; the mark was small; "/ 06" floated far from the numeral.
- Fix (v2): hard 1-frame state changes, dot snaps in 3 frames, list fades in place, mark 440 px 0.2 s after exit with "comment 11", label tight to the numeral.
- v2 scores: idea 3 · type 4 · colour 4 · air 4 · fidelity 4 · finish 4 · truth 5. Still missing: a real-world plate (they show the list on a laptop on stone); next time put it on a device scene.
## 08 Work index page (practice/thu-work-index-before.jpg -> -after.jpg, code brand/code/practice/index)
After Satto's Pulvinar index (satto-07). Black page, 13 px grotesk, list + preview, one inverted row.
- Before scores: idea 3 · type 4 · colour 4 · air 4 · fidelity 3 · finish 3 · truth 4. Gaps: 4-dot grid and list columns not snapped to it; the preview was the full ata render, dark on black, so the tile vanished; "Concept" repeated in every row as noise.
- Fix: 7-dot column grid with every column snapped to it; Imisozi row selected so the preview is a light tile, cropped tight and abstract like Satto's; last column = market code (KE/NG/RW/ZA); "Concept" said once in the footer; 4 px row padding.
- After scores: idea 3 · type 4 · colour 4 · air 4 · fidelity 4 · finish 4 · truth 5. Next: the preview crop is upscaled and slightly soft at 2x; render a dedicated square crop.
## 09 Availability page: Kilele Residences, Nairobi (practice/wed-kilele-before.jpg -> -after.jpg, side by side with satto-07 in wed-kilele-vs-satto07.jpg; code brand/code/practice/kilele)
Fictional residential building in Kileleshwa. High-fidelity HTML at 1440x900: unit table (unit, type, area, floor, status, KES) beside an SVG plan of floor 6, one unit active. After Motto's Attend (one family, tint hierarchy), Nuevo.Tokyo (mono codes, one signal colour) and Satto's Pulvinar index.
- Before scores: idea 4 · type 4 · colour 3 · air 3 · fidelity 2 · finish 3 · usability 3 · truth 3.
- Honest gap: the plan is the focal point but read as a wireframe (boxes, no walls, windows or doors, a salmon fill), so the one thing meant to carry the page was the weakest. Also: secondary text at 45% failed contrast (2.94:1); Sold/Reserved hid in the price column; the spec strip repeated the table; the header link was a default underline.
- Fix: redrew the plan as a real drawing at 28 px per metre: poché walls, glazed west facade (6.7 m on 6B), entry door swing, core, room names with areas that sum to 96 m², 6A hatched as sold, Infrared outline only (no fill). Added a status column with strike-through for sold/reserved, a single action strip (summary, price, 44 px button), tint raised to 62%, labels to 12 px, focus ring, SVG label.
- Checks run: brand/code/a11y/webaudit.js (v1: 50 failures, v2: 0); Gesso rules checked by hand against the rule catalogue (the npx detector could not be fetched in this run): fixed underlined-text, added font-smoothing and text-wrap blocks, no gradients, shadows, emoji or eyebrows; writing lint by hand (no em dashes, no puffery).
- After scores: idea 4 · type 4 · colour 4 · air 4 · fidelity 4 · finish 4 · usability 4 · truth 4.
- Review fix (Codex): the 13 px "6B" plan label was Infrared #FF4A1C on Bone, 2.82:1. webaudit skipped SVG text entirely (no offsetParent, and it read color instead of fill), so v2's "0 failures" missed it. Fixed the tool (SVG text now checked by fill; v1 now shows 57 failures), set the label to Ink, and used deep Infrared #D9380F (3.9:1) for the outline, dot and focus ring on Bone. Added a main landmark.
- Next gap: still no real material or light. Motto and Nuevo always show the product in a real scene. Next time: a Blender daylight study of the 6B living room looking west, placed as the preview when a unit is selected.
