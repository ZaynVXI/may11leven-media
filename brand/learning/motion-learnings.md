---
name: motion-learnings
description: Running log of what worked and what didn't in May11Leven motion and UI pieces, plus every correction Zayn gives. Read before every motion piece; add to it after every piece.
---

# Motion and UI learnings (newest first)

Each line: what we learned, from which piece, and the rule it creates. Zayn's corrections always win and stay forever.

## How we train (the PXDX method, read from their tutorial frames)
1. Three reference videos plus one sentence make the skill: "The motion should be calm and smooth." Our training set is brand/motion-refs/.
2. Every refinement Zayn gives ends as "Add to the skill: …" and goes into this file the same turn, so it applies to all future animations ("make fixes apply to all animations").
3. Short prompts, small pieces, many rounds. They were on experiment 17; we are on 1.

## Zayn's standing corrections
- Reel length follows the product and how much there is to show, never one fixed number (Zayn, 19 Nov). Before building, list the moments the reel must show, give each 3–5 s (enough to read and see it work), and add them up. Guide: one widget or detail 6–12 s; a product with one flow 15–25 s (PXDX product reels sit around 20 s); a product with several flows or a before-and-after 25–40 s; a case study or process story 30–60 s. Cut any second where nothing new happens.
- Show products working, like a real product or prototype, never as static frames.
- Each product gets its own look; never the same style twice in a row.
- Learn the PXDX way: design first, let the tools animate, keep one style skill and improve it after every piece.
- Research trends and references before every product.

## Lab 01 · Term deposit (Figma Motion, 10 s loop)
- Works: pill-to-card morph (WIDTH, HEIGHT, CORNER_RADIUS plus TRANSLATION to keep it centred), number change as a crossfade of two text layers with a 16 px slide, chart growth with PATH_TRIM_END and the dot following.
- Fix next time: the "7 Fridays left" pill sat too close to the amount; keep 40 px minimum between stacked elements inside a card.
- Fix next time: a 4 s hold with nothing moving felt dead; something small should move every 1.5–2 s (a pill, a tick, a glow drift).
- Fix next time: top-of-frame labels collide with notifications; hide or move the label while a notification shows.
- Export: Figma export_video at 1080x1350, 30 fps, quality high, about 10 s; check with an ffmpeg frame sheet before showing anyone.

## Add to the skill: UI details (Zayn, 19 Nov)
"Pay attention to tiny details… they make a lot of difference." Before any component goes into a reel, run the 14-point details pass in `brand/learning/ui-details.md` (nested radii, equal gaps, raised selection, tone-on-tone status, ringed dots, coloured shadows, ringed photos, dashed only for empty, one icon set). Motion makes these visible: a raised tile sliding along its track, a dot ring catching the light, a tinted shadow moving with its card.

## Add to the skill: hero loop in a real photo (After hours v2)
For a PXDX-style hero, put the live UI inside a free stock photo of a hand holding a phone: render the screen HTML frame by frame with a render(t) function, warp each frame onto the screen corners (measured at 4x zoom), cool and dim it slightly, add a faint sheen and grain, and encode at CRF 22 (grain makes CRF 17 files huge). Curved screens need the side edges pushed out a few pixels so none of the original screen shows. End every loop where it began.

## Add to the skill: silhouette hero (Zayn, 19 Nov)
Zayn pointed out PXDX's hands are completely black. Hero rule: the hand is a silhouette against one shape of soft light from the client's world; only the screen is lit. Draw the phone body as a clean rounded shape (never trust a cut-out's corners), keep rim light very faint, no outline glow.

## Never repeat a hero (Zayn, 19 Nov)
"Don't keep using the same hand for all products... I hate when everything looks the same." I reused the After hours silhouette hand for Term and called it a signature. That was wrong: a technique can repeat, a presentation can't. Before building a hero, check the ledger in `brand/learning/hero-ledger.md`, pick a presentation no other product in the last 12 posts used, and take the prop from the product's own world (Lebedev's colour-matched prop, Holographik's phone on ore, .raw's laptop on stone, Motto's type-led covers).

## Upgrade what hasn't shipped (Zayn, 19 Nov)
Whenever a skill or learning note is updated, go back over every piece not yet released (scheduled posts, drafts, concepts) and apply the upgrade where it fits. If a scheduled post changes, re-upload with commit-pinned URLs and edit the Buffer post before its slot. Log what changed in this file.
- 19 Nov, after the PXDX bar: Term deposit loop, Term hero and After hours pay loop moved from ease-in-out to a damped spring (zeta .65, omega 8, about 7% overshoot, settled by the end of each move). In the Term deposit loop the landing KES 750 now nudges the card 10px and it springs back. After hours: the "Check your phone" and "Booked" layers start earlier so the springier box is never shown empty. Loops still close on frame 0. Gotcha: spring values above 1 broke CSS blur (negative radius is ignored, so the old blur stuck); clamp anything that can't go past 1.
- 19 Nov, same pass: stories f5/f6 and both LinkedIn documents checked against the ui-details checklist; nothing fell short, so no changes. Term s2 already carries a visual (fanned cards), so the "at most one pure-text slide" rule holds; left as is. Buffer: After hours IG and Term IG now point at the spring versions (commit bcfecd1); schedules unchanged.

## Add to the skill: one component, numbered states (PXDX player, 19 Nov)
For a component study, build a hero state plus a strip of 3 to 5 numbered tiles; each tile changes exactly one thing, and each tile is a real state of the flow (idle, working, done, stopped). State changes cross-dissolve through a dimmed glyph in about 0.5 s; nothing else on the frame moves at the same time. Put the practice count in the caption.

### Upgrade log: Term v3 (before release)
- Founder: v2 "too generic". The cause was a borrowed fintech pattern (gradient cards, donut, pills) instead of the product's own world.
- Fix: one world (the exercise book), with primitives from it (name tape, register, red-pen tick, rubber stamp), one signature move (the tick written with a pen-like ease: down-stroke, a beat, long up-stroke) and a "what if" slide for failure modes.
- Rule: before any product post, name its world and three primitives, and write the "what if it goes wrong" answers. No glossy gradient cards unless the product's world calls for them.
