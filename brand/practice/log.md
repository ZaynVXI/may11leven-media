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
- **Imisozi phones:** the phone screens floated as rounded cards with no hardware, and the status bar was a text stub. Fixed by rebuilding the screens at @3x inside drawn iPhone frames (titanium rim, Dynamic Island, side buttons, home indicator) with real signal, wifi and battery icons.

## 09 Editorial infographic: Zanzibar 9.6 s (practice/thu-zanzibar-96-before.jpg -> -after.jpg, code brand/code/practice/zanzibar-96)
Data: research/zanzibar/FINDINGS.md (our own reviewed study; totals only, no business named). Takeaway: the median independent Zanzibar hotel site takes 9.6 s to show its main content on a mid-range phone.
Steal list (the thinking, not the look), refs: motto/workbook-02, nuevo-03, satto-07, holographik-12, reel-0148ef71.
- The grid is the cover (Motto): the cells hold the type and the number, nothing decorates.
- The number is the image (Nuevo.Tokyo): one huge figure and a plain line, no illustration.
- One thing breaks the system (Satto's inverted row, .raw's one expressive form): here it's the infrared 9.6 s line.
- Before scores: idea 4 · type 3 · colour 4 · air 4 · fidelity 3 · finish 3 · usability 3 · truth 4. Gaps: the grid lines ran through the lede and the footer, and the columns meant nothing; "good" and "poor" were two floating ticks with no zone; the line said "typical" where the data says median; tracking -0.045em was close to welding the numerals (anti-slop crushed-tracking).
- Fix: the six columns became the time axis (2 s each); rows give each block its own cell, so no line crosses text. The poor zone over 4 s is a shaded band. Added the 3.5 s "first thing appears" mark so the wait shows. The lede now says "median" and "independent". Tracking set to -0.02em, one weight (Regular) throughout, and "86% past the poor line" in the footer.
- After scores: idea 4 · type 4 · colour 4 · air 4 · fidelity 4 · finish 4 · usability 4 · truth 5.
- Checks run: webaudit contrast (0 failures) plus a hand check on the zone (5.6:1); anti-slop by hand against references/rules.md (the npx detector was blocked from downloading here). Fixed crushed-tracking; still flagged: overused-font-stack (Inter) and single-font-page, both kept on purpose. Writing: no em dashes, no filler.
- Still missing: a real-world plate. Next time show the tile beside a phone that's still loading, or as a 6 s reel where the counter runs and the photo lands at 9.6.

## 10 App: Mita prepaid-meter home screen (practice/fri-mita-before.jpg -> -after.jpg, code brand/code/practice/mita)
Concept, not a client. The one job: show what a prepaid electricity token actually bought, so the opaque KPLC top-up becomes understandable. Its own brand (name Mita = "meter" in Swahili, Archivo condensed numeral + IBM Plex Mono data, Bone ground, one owned LCD-green accent), never our house system.
Data truth (today's research): a KPLC unit is ~KES 12, "about 16 with taxes"; up to 20% of a purchase can clear arrears first (peopledaily.digital, kenyans.co.ke). So KES 1,000 -> 35.2 kWh with the split energy 683 / taxes+levies 317 / arrears 0 is a believable breakdown, not invented precision.
Steal list (the thinking, not the look): Motto Performance Golf (reframe the chore into understanding; one owned accent on neutral), Nuevo.Tokyo (name the artefact with a bracketed qualifier; opaque surfaces, one accent), Satto/Holographik (one big numeral is the image; the block IS the reading, not a card around it).
- Before scores: idea 4 · type 3 · colour 4 · air 3 · fidelity 3 · finish 3 · usability 3 · truth 4. Gaps: the "kWh" unit and "Last token" label collided with the token string (a layout bug - the decorative big-number small tag overlapped the section below); the numeral leaned on weight 500; the buy button floated mid-screen instead of anchoring above the tabs; only two parts of the split shown (no arrears, the part that actually explains missing units); status bar missing wifi.
- Fix: moved the unit label up into the block corner so nothing overlaps; numeral to one weight (Regular, condensed 78%) at 188px so size/position carry it, not bold; the token purchase split now shows all three parts (energy / taxes / arrears) - that third part is the whole point; buy button anchored above the tab bar; added the wifi glyph. One weight across the whole screen (Minimalism principle 2); the green block is the reading itself, nothing decorates it (principle 3, quiet-object test).
- After scores: idea 4 · type 4 · colour 4 · air 4 · fidelity 4 · finish 4 · usability 4 · truth 5.
- Checks run: webaudit on the built HTML returned 0 contrast failures; ink on the LCD-green block checked by hand at 11.4:1 (the audit reads the page ground, not the coloured block). Target size (SC 2.5.8): chips ~86px, tabs 64px, all clear of both the 24px rule and the 44pt native bar. Anti-slop by hand against references/rules.md (the npx detector was blocked from downloading here): fixed the overlap/underline/weight tells; still flagged on purpose - single-font-page (Archivo display + Plex mono is deliberate), safe-green-default (the LCD green is the owned brand accent, not a Tailwind fallback), underlined-text on the "Why units vary" link (kept: it's a genuine inline text link). Writing: no em dashes, no filler, "median/arrears" used literally.
- Still missing: a real-world plate - the screen in a phone on a Nairobi surface (concrete + coloured cable, Blacklead style) rather than a plain frame, and the before/after as a 6 s reel where the paper token flips to the clean split. Next session: the device scene + the reel cover.

## 11 Web: Ikiyaga Residences availability page (practice/wed-ikiyaga-before.jpg -> -after.jpg, code brand/code/practice/nyandungu)
Concept, not a client: eleven flats beside the Nyandungu wetland in Kigali, every price on the first screen. Research in brand/code/practice/nyandungu/RESEARCH.md (price truth from a real Kimihurura listing: ~RWF 4.1M per m² there; we priced the wetland side at ~RWF 2.9–3.2M per m², 30% deposit, which is the local norm in listings).
Visual language: Warm editorial, turned cool (real credited photo of the place, one ink, a list as hero). Last piece was Mita (LCD utility app), so this is a different language.
Steal list (the thinking, not the look), refs: holographik-13, lebedev-14, satto-07, motto/workbook-02, nuevo-03.
- The list of prices is the image; one value lifted, the rest set back by tone (Holographik).
- Colour comes from the place, one ink only (Lebedev Haven).
- One inverted row, nothing else decorates; the structure is the cover (Satto, Motto).
Matching reference: holographik-13 (price ladder).
- Before scores: idea 3 · type 3 · colour 3 · air 4 · fidelity 3 · finish 3 · usability 3 · truth 4. Gaps: it looked like every real-estate template (cream + serif, flagged by the anti-slop cream-default-wash rule); three coloured status pills made three accents; a glass "Concept" pill floated on the photo; a shadow on the button; no focal point, every row equal; the idea ("every price shown") was said, not shown; no deposit or per-m² figure for the unit you'd pick; the photo credit was white on grass (1.1:1); webaudit flagged 12 contrast failures (greys at 3.4–3.7:1).
- Fix: the price ladder became the hero (26 px tabular numerals, one weight); one selected row in reed green drives a detail strip (per m² 3,131,700, deposit 97,710,000, handover 227,990,000, all checked by hand: 325,700,000 / 104 m², x0.3, x0.7); status written in words, sold prices also struck through; ground and ink taken from the photo (sky #E8EDF0, reeds #3E4E2A, ink #1B2416); serif cut, one grotesk (Hanken Grotesk Regular); credit on a solid strip with "Concept" said once; one CTA naming the unit; EN / RW toggle in the nav.
- After scores: idea 4 · type 4 · colour 4 · air 4 · fidelity 4 · finish 4 · usability 4 · truth 4.
- Checks run: webaudit on after.html returned 0 failures (before: 12). Gesso `npx @gessobuild/anti-slop check` could not run here (the download was blocked by the workspace), so the rules were checked by hand from brand/tools/claude-42/anti-slop-design/references/rules.md: cream-default-wash, heavy-box-shadow, floating-hero-card and missing text-wrap fixed; still flagged on purpose: single-font-page (one face is the system). Writing: slopbeth deslop_lint on the page copy returned 0 phrase, structure or dash hits.
- Still missing: the 390 px mobile version and a scroll state (the ladder should stay pinned while the photo changes per floor). Next: the mobile ladder and the 8 s reel in reels.md.

## 12 App component: Tuma name check (practice/thu-tuma-before.jpg -> -after.jpg, side by side with PXDX: thu-tuma-vs-pxdx.jpg, code brand/code/practice/tuma)
Concept, not a client. The one job: before mobile money leaves your phone, show whose name it goes to and make "Not them" as easy as "Yes". Research in brand/code/practice/tuma/RESEARCH.md: Safaricom's Hakikisha redesign (name first, plain Yes / No) cut daily reversal requests from about 12,000 to 4,000 (techcabal.com).
Visual language: Soft glass and aura (last piece Ikiyaga was warm editorial). Colour from Nairobi in November: jacaranda violet as the one accent on dusk ink. Type: Atkinson Hyperlegible Next (built so 0/O and 1/l can't be confused) + Geist Mono for numbers.
Steal list (the thinking, not the look), refs: pxdx-player, pxdx-dribbble/podcast-ui-details, qclay/17-aura-glass, lebedev-02, motto/workbook-02.
- One component, numbered real states, each changing one thing (PXDX player).
- Money as a calm sentence, one colour mood behind frosted surfaces (Qclay aura); one question, one answer (Lebedev question card).
- The structure is the cover; nothing decorates (Motto workbooks).
PXDX move applied: hero state + numbered strip 01 Check / 02 Sending / 03 Sent / 04 Stopped, practice count in the caption.
- Before scores: idea 4 · type 3 · colour 2 · air 3 · fidelity 3 · detail 3 · motion 1 · finish 3 · usability 3 · truth 4. Gaps: the amount was the biggest thing, but the research says the name must be; the name was 24 px capitals. The "Yes, send" button was a violet-to-amber gradient with a second amber aura blob: two accents and a slop tell. The strip showed four bare icons (avatar, spinner, tick, cross) that said nothing about the flow and had no labels. Heavy black shadow and a decorative glass panel around everything. Bold 700 everywhere.
- Fix: the name became the hero (52 px, sentence case, weight 600), the amount moved below a hairline at 36 px Regular; one accent (jacaranda #B9A2E6), solid, amber removed; the two choices are equal halves of one nested track (outer radius 44, padding 8, inner 36); the strip became four mini cards of the real component, labelled, each changing only the footer; the glass panel removed.
- Anti-slop pass (by hand against brand/tools/claude-42/anti-slop-design/references/rules.md; the npx detector isn't installed here): fixed dark-glow (violet shadows on the card and the button, removed), ghost-card (hairline + wide halo on one surface, kept the hairline), over-rounded-card (40 -> 32 px card, 28 -> 24 px tiles), gradient-fill (gone). Kept on purpose and declared: purple-violet-wash (violet is the jacaranda accent, set once as --accent with --slop-allow).
- A11y check (own script: contrast measured on a render with the text hidden, since /home/claude/a11y and webaudit aren't present this session): grey text 7.8:1 on the card and ≥ 6.7:1 on the brightest aura behind the caption (first pass was 4.1:1 there, so the grey went from #B4ABC1 to #C2BACE); "Yes, send" label 8.3:1; non-text: "Not them" border 3.2:1, "Yes" fill 7.0:1 against the track; status icons always paired with a word.
- After scores: idea 4 · type 4 · colour 4 · air 4 · fidelity 4 · detail 4 · motion 1 · finish 4 · usability 4 · truth 5.
- Still missing: motion (the PXDX reference is a loop; ours is a still) and a real-world plate. Next: a 6 s loop where the card stays centred and the four states cut behind it on the beat (reels.md, Obrazur dock idea), each state change a 0.5 s dim cross-dissolve, with a soft tick per cut.

## Try to break it No. 01, v1 (rebuilt)
- What fell short: I designed from my notes without opening the reference screenshots. I skipped the steal list, the judgement brief and the side-by-side Pass 0. The result was 8 flat text slides with no material, no device and no photo, which breaks motto-maisa rule 2 (at most one text slide).
- Fix to the process: no design work starts until posts/<piece>/BRIEF.md exists, with a reference contact sheet (at least 3 studios from brand/refs, opened and looked at), a steal list, the 7-line judgement brief and a slide plan that lists one presentation type per slide. Pass 0 is scored against that sheet, side by side.
