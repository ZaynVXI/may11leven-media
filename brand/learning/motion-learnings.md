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
- Reels run about 20 seconds, like PXDX's (Zayn, 19 Nov). Product motion reels: 18–25 s, built as two or three loops of the product (open, use, a second state), not one 10 s loop. Short 6–12 s loops only for single widgets inside a carousel.
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
