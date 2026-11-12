---
name: figma-motion
description: Animating brand assets inside Figma's motion timeline through the Figma connection (the "motion design is changing" workflow). Read before animating a logo, mark or brand board.
---

# Figma Motion through the Figma connection

## What the reference video shows
- A static brand system (mark of four petals, wordmark, palette of paper, ink, orange and lime, a case-study board) lives in Figma.
- Claude, connected to Figma, is given the file link and a plain instruction, for example "Animate the petals, then reveal the wordmark. Use a soft ease."
- The keyframes appear on the Figma timeline. The designer then refines them by hand ("slow the petals down").
- The same file gives many outputs: logo reveal, palette wipes, construction-line grid, case-study boards in motion.
- The point: motion becomes part of the brand file, so every asset can move without After Effects.

## What we already have
- Figma connector (create_session, use_figma, get_motion_context, export_video).
- Skills: figma-use + figma-use-motion (keyframes, animation styles, easing, text stagger, timeline duration), figma-implement-motion (turning Figma motion into code).
- Motion APIs may not be switched on for every account. If use_figma returns "is not a supported API", stop and use our own pipeline (HTML/CSS + Playwright frame capture, or Remotion).

## How we use it
1. Build the static system in Figma first (mark, wordmark, palette, one board).
2. One instruction per move, with the order and the ease ("mark draws in over 0.8 s, wordmark follows 0.2 s later, soft ease out").
3. Check with export_video at low size and 5 fps, pull 4–6 frames with ffmpeg, fix everything in one pass, then render full size.
4. Motion rules still apply (may11leven-motion): one orchestrated move per piece, calm, no bounces unless the brand calls for it.
5. First test: our two-bar "11" mark (bars slide in on the offset, then the wordmark).
