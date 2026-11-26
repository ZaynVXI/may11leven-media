---
name: prism-warp-ui-reel
description: A 10 s Instagram UI showcase reel signed "prism warp" (sent by Zayn), studied frame by frame. What makes clean UI feel detailed, and the rules we take for our own UI reels and slides.
---

# "prism warp" UI reel: what makes clean UI feel detailed

**Source:** a 10.3 s reel at 960x720 that Zayn found on Instagram. Frames without faces are saved in `brand/refs/prism-warp/`. Frames with people or avatar photos weren't saved, because the repo is public.

## What happens
Fourteen product moments in about 10 s, one cut every 0.6–0.8 s, ending on the logo with a glassy warp. The products:
- fintech "Send money"
- a dark users dashboard
- sleep tracking
- a team analytics dashboard
- dark messages
- a split-bill sheet
- two empty states
- a digital-assets library
- a morning dashboard with a zoom lens

## Why it reads as "clean but detailed"
1. **One big number carries each screen:** $248.00, "5 hr 48 min", $248,610, 2,184. Everything else is small and quiet. The detail sits in the small type: "Balance $12,480.20 · No fee", "Synced 07:24 · Ring", "48,920 assets · 312 GB · 96% linked to products".
2. **Real states, not happy paths:** "Sending to Maria…" with a little money icon flying; an empty state ("All caught up. Nothing new here.") with a line-drawn bell and one action; "Nothing here anymore · 18 assets moved to Holiday Drop · FW26 · Open folder". The empty and after-action states are designed as carefully as the full ones.
3. **Each product has its own data graphic, made for its data:** sleep stages as coloured bars on a time axis; tasks shipped as an isometric dot heatmap; utilisation as stacked dots; revenue as a single line with a hover card. No generic donut charts.
4. **One accent per product** on a neutral base: violet for sleep, orange-red for analytics, black for fintech.
5. **The UI floats in a photographed world, with no device frame:** a flat card over a hazy classical arcade, a dashboard over a wheat field, a phone screen over a film-grain shot of a coat. Grain and warm light on the photo; crisp, flat UI on top. (Lebedev does the same idea with the client's world; here the photos are pure mood.)
6. **Motion shows interaction:** a cursor clicks the date picker, a sheet slides up, a lens zooms on a chart, stickers sparkle when a folder is dropped. Each cut shows the product being used.
7. **The breadcrumb and meta text are real:** "Workspace / Digital Assets", "Q4 2026", "4 people · equally". That's what makes it feel shipped.

## What we take
- **The UI we build gets a hero number, a designed empty state and an after-action state** (Term has the paid stamp; After hours has the refused slip; keep doing this).
- **Data graphics made for the data,** never stock charts.
- **For a studio reel or a "Built from points" style showcase,** a cut every 0.6–0.8 s across many screens works for a highlight reel. Product reels stay 20–40 s (motion-learnings.md).
- **UI over a graded photo with no device frame** is a fourth presentation type to add beside device-on-material, flat page on a field and the UI crop. Use it for one slide, not every slide.

## What we don't take
- **Two-tone headings** ("All caught up." black + "Nothing new here." grey) are on our anti-slop list as an AI tell when overused. One per product at most.
- **Photos of people as avatars:** use initials or our own illustrated avatars, and no faces from references.
- **Mood photos that have nothing to do with the product** (classical arches behind a sleep app). Our rule stays: B-roll from the client's own world.
