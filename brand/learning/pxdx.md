---
name: pxdx
description: Daily study notes on Pixie and Dixie (PXDX, @pxdx.baddies), our first mentor. One heading per piece, newest first. Read before any product post.
---

# PXDX study log

## Player experiment and podcast UI details: one component, numbered variants
Refs: brand/refs/pxdx-player/ (frames from brand/motion-refs/reference-3-player.mp4, 12 s, 720x900) and brand/refs/pxdx-dribbble/podcast-ui-details.jpg (Dribbble "UI details of podcast app"; faces in the thumbnails pixelated on our copy). Nothing new on dribbble.com/PXDX since our last sweep (newest is still SAMUR.AI), so today is a deep read of two saved pieces.
- **Product idea:** the player is not a product, it's a training rep: one control (play/pause) explored until it feels right. The podcast piece is a calm desktop podcast app whose problem is clutter: the sidebar collapses to an icon rail and keeps the same state (badge "3", downloading 77%, a profile with a notification dot).
- **Structure:** the player is one 4:5 frame: a light stadium shape on black, the hero control in the middle, the title "Player", three grey lines under it ("Interaction design / Experimentation phase (57) / Figma Motion + Claude"), then four small numbered variants, 01 to 04. Each variant changes ONE property: 01 adds a track label, 02 a ring around the button, 03 a waveform under it, 04 a tick dial. The podcast shot shows the expanded and collapsed sidebar side by side over one scene (a concrete room with a desert behind glass and glowing spheres).
- **UI details (checked against ui-details.md):** nested radii everywhere (player tile, orb, track; the selected nav row's icon sits in its own circle, rule 1); status tone-on-tone (red badge only for the count that matters, grey badge for "2", rule 4); the Dark/Light segmented control uses the raised-tile selection (rule 3); the collapsed rail keeps the notification dot with a ring (rule 5); label inside control ("AirPods" next to its own glyph, rule 6); idle rows grey, active row white (rule 11).
- **Motion:** play turns to pause through a dim cross-dissolve of about 0.5 s (the icon fades down to grey, the new glyph fades up), never a flip. The orb glow breathes; the side ticks pulse like a level meter while playing. Nothing else moves. 12 s loop.
- **Caption and workflow:** the frame itself is the caption: "Experimentation phase (57)" says this is the 57th rep and "Figma Motion + Claude" names the tools. They show the count openly, which turns practice into content.
- **How they train Claude:** reps, not one big prompt. One component, many numbered variations, each one a single change, kept as a numbered set.
- **Our move:** show a component as a hero state plus a numbered strip of real states, each tile changing one thing, and put our practice count in the caption ("Practice (12)"). Ours differs: the strip is the component's real states in a real flow (check, sending, sent, stopped), not decorative variations, and the frame carries the product's problem in one line. Used today in brand/practice/thu-tuma-after.jpg.
- **What would beat this?** Their variants are pretty but say nothing about the user. A strip where each tile is a moment in someone's day (the Hakikisha-style name check: check, sending, sent, stopped) explains the product in one glance, and in motion each tile would play its own 2 s state loop.

## "Just UI details" with one message (peace post, 5+ slides)
Refs: brand/refs/pxdx-peace-details/. Every component in the post carries the same idea (peace): interaction cards ("How was your sleep?" then "Is it because of bad news?"), a text container shown mid-edit with a Figma selection box, a folder list, a wallet module, a confirmation dialog where "yes" is disabled and the cursor gets a no-entry badge, a content card. Caption: "Just UI details. We wish everything could be this simple…" then the themed sign-off.
**Details worth taking:** one brand gradient (indigo to rust) reused on every accent (pill, folder, wallet, card top); cards sit inside a faint outer halo frame (a second, larger rounded shape at low opacity: nested radius again); photo tiles tilted a few degrees, stacked, with thick white borders; black pill buttons with a long soft shadow; the disabled state told as a story (cursor + badge); a tiny centred caption naming each component; dark silk and light grey backgrounds alternate slide to slide.
**Our move:** a details post can carry one human message from our markets (for example "rest" for hospitality, "pay on time" for fintech), told through real states of our own components. One gradient per post taken from the product's world.

## Silhouette hand hero (Annie, Rosie)
Refs: brand/refs/pxdx-silhouette/. The hand holding the phone is pure black against one big shape of soft light (Rosie: a glowing disc; Annie: a tall arch). Only the screen is lit, so the eye goes straight to the product. Widgets float around it at different depths, a line of the product's voice ("Hey, Annie") sits over the hand.
**Our move:** our hero is a silhouette hand in front of a light shape taken from the client's place (After hours: a Lamu doorway arch in warm sand light). Cut the hand from free stock with GrabCut, draw the phone body ourselves, warp our UI onto the screen. Done in posts/after-hours/v2/hero_sil.py.

## UI Color Set series (8 posts)
Refs: brand/refs/pxdx-color-sets/. One fixed template, a new palette each post: a hero photo card with a serif title ("UI Color Set") and a glass name pill (Texas Sunset, Candy Golf, Night Ride), a "Colors" pill, a tilted swatch card with a circle photo, four dots and a Copy button, a small tilted photo tile with a check badge, a tall rounded bar and a big circle in the palette's two accents, and a 5 x 3 hex grid at the bottom (each column a colour with two lighter tints). Light posts and dark posts alternate.
**Why it works:** useful (people save palettes), repeatable, every post looks different but the frame never changes.
**Our move (needs Zayn's OK as a series):** "Colour from a place": one palette per post taken from a real African or Gulf place or material (Lamu limestone, Kigali red earth, Zanzibar indigo cloth), shown on our own components, hex grid with tints, free stock photos only, no faces in the hero.

## Dark and light fintech (Johnny)
Refs: brand/refs/pxdx-rosie/08-09. The same screen in dark and light mode over one abstract silk background in the app's colour; a two-weight label beside the phone ("UI design / Dark mode"). Three slides: dark, light, detail.
**Our move:** for any app concept, show the dark and light version of the key screen back to back, same background.

## 3D UI effect (tutorial)
Refs: brand/refs/pxdx-3d-ui/. Turned into the skill may11leven-3d-ui (recipe and CSS proof in brand/tools/may11leven-3d-ui/).

## The bar for the next project (Zayn, 19 Nov: "our next project should be better than these")
After hours and Term v2 set the floor, not the target. Gaps against PXDX that the next product has to close:
1. **One signature move per product.** PXDX products each have a thing you remember (a 3D glass key, an ASCII face, a colour set). Ours had good screens but no single move. Pick it in the brief, from the 3D UI, ASCII or transitions skills or something new.
2. **Motion with physics, not fades.** Our loops ease in and out. PXDX uses springs, overshoot and stagger, and things touch each other. Use spring curves and let one element push another.
3. **Fewer flat text slides.** Our manifesto and offer slides are type on a dark field. PXDX makes even the text slides visual (UI cropped huge, a detail magnified). At most one pure-text slide per carousel.
4. **A hero nobody has used.** Check `hero-ledger.md`. Build the set, props and light for this product only.
5. **Colour from a place, chosen first.** Write the product's colour set (4–6 swatches with names) before any screen, PXDX colour-set style.
6. **Sound.** PXDX reels carry designed UI sound. Add soft clicks, ticks and a landing sound to the reel cut.
7. **Daily check.** Each morning's PXDX study ends with one line in this file: "What would beat this?" The next project's brief quotes the best three.
