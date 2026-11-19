---
name: design-systems
description: What seven public design systems (Fluent 2, Spectrum, Uber Base, Gestalt, Lightning, Wise, Geist) teach about tokens, components, motion and docs, and the May11Leven system we built from them. Read before any website, app or brand-system work.
---

# Seven public design systems, and ours

Zayn's tip: pick one component (button, card, toast) and open it in all seven. Seven answers to one problem.

## What each one does (measured from their public token files and docs)
| System | What to steal | Measured |
|---|---|---|
| Fluent 2 (Microsoft) | Named motion tokens. Every animation picks a duration and a curve by name | Durations 50, 100, 150, 200, 250, 300, 400, 500 ms. Decelerate (enter) cubic-bezier(0.1,0.9,0.2,1); accelerate (exit) (0.9,0.1,1,0.2); ease (0.33,0,0.67,1). Spacing 2, 4, 6, 8, 10, 12, 16, 20, 24, 32. Type 10 to 68 px, each size with its own line height |
| Spectrum (Adobe) | T-shirt names for size (xs to xxl); one live playground per component, wired to the code | Docs start at "attention hierarchy" (what the eye sees first), then components. React and Web Components builds |
| Base (Uber) | Restraint. Mostly black and white, one blue only for safety and trust moments | One typeface (Uber Move) for everything; icons share shapes with the type; the grid comes from the logo |
| Gestalt (Pinterest) | Three token layers: base → semantic → component. Names say the job, not the colour | Space 4 px steps (4 to 64). Rounding 0, 4, 8, 12, 16 … pill, circle. Opacity 0.04, 0.2, 0.4, 0.8, 0.9. Semantic names like color.text.subtle, color.icon.error |
| Lightning (Salesforce) | Durations named by feeling, not by number | instantly 0 s, immediately 0.05 s, quickly 0.1 s, promptly 0.2 s, slowly 0.4 s, paused 3.2 s. Spacing 2, 4, 8, 12, 16, 24, 32, 48 px |
| Wise | A brand with one loud colour that is still calm: flat, hairlines, no shadows, no gradients | Forest #163300 + lime #9FE870 accent on white and fog #E8EBE6. Display 105 px at 0.85 line height, tight tracking. Pills for buttons, 10 px cards. Never two filled buttons side by side |
| Geist (Vercel) | Colour steps with fixed jobs | Each colour has 10 steps: 100–300 backgrounds (default, hover, active), 400–600 borders, 700–800 solid fills, 900–1000 text. Two backgrounds only |

## The one lesson they share
A system is names with jobs. Nobody picks "#8C8884" in a design; they pick "text.subtle". Change the value once, everything follows.

## The May11Leven system (v1, in the Figma brand file)
Minimal like Motto: few tokens, each with one job.

**Colour roles** (Gestalt naming, Geist jobs, Uber restraint)
- bg.default Bone #ECEAE4 · bg.inverse Ink #141213 · bg.panel Sage white #EBF0EC
- text.default Ink · text.subtle Ash #8C8884 · text.inverse Bone
- border.default Ash at 40% (hairline 1 px)
- accent Infrared #FF4A1C: one word, one object or the main button. Under 10% of any screen (Wise, Uber)
- Each client project swaps the accent and keeps the jobs.

**Space** (4 px base, Gestalt and Fluent): 4, 8, 12, 16, 24, 32, 48, 64, 96. Page edge 32 px on posts.

**Radius**: 0 for posts and editorial, 8 for cards and inputs, pill for buttons and tags (Wise). Never more than two radii on one screen.

**Motion** (Fluent values, Lightning names)
- quickly 100 ms: hover, press
- promptly 200 ms: toggles, tabs, toasts in
- gently 300 ms: cards, sheets, page parts
- slowly 500 ms: hero reveals only
- Enter with decelerate cubic-bezier(0.1,0.9,0.2,1). Exit with accelerate, 30% shorter. Respect prefers-reduced-motion: fade only.

**Type** (Uber: one family carries the UI; Wise: huge, tight display)
- Display: Instrument Serif or Inter Tight Medium, line height 0.95–1.0, tracking −2 to −4%
- UI and body: Inter Tight, 16–22 px, line height 1.4
- Labels: IBM Plex Mono, uppercase, 18 px on posts, 12 px in UI, tracking +4%
- Copy rules stay: labels ≤ 3 words, headlines ≤ 8, lines ≤ 15

**Three components, seven answers → ours**
- Button: pill, one filled per screen (Wise), Ink fill on Bone, accent only for the main action. Text link for the second action. Press = 100 ms scale 0.98.
- Card: hairline border, no shadow (Wise, Geist), 8 px radius, 24 px padding, label top-left in mono, answer below.
- Toast: Ink pill bottom-centre, one line, enters 200 ms decelerate, leaves after 4 s, never the only place an error lives (Gestalt accessibility).

**Docs** (Spectrum, Gestalt): every component page has what it is for, when not to use it, the states, and a live example. Ours live in the Figma brand file and brand/learning.

Sources: github.com/microsoft/fluentui (packages/tokens), github.com/pinterest/gestalt (gestalt-design-tokens), github.com/salesforce-ux/design-system (design-tokens), spectrum.adobe.com, uber.com/careers/design/work/2018-redesign, styles.refero.design (Wise), vercel.com/geist/colors.
