# Web build stack (from the "Claude + design skills" reel)

The reel (format study only, no faces): it claims "Claude just killed web design agencies", then lists the stack:
1. Emil Kowalski design skills for motion, easing and fluid feel. Installed: brand/tools/emil-skills (apple-design + emil-design-eng).
2. Impeccable (Paul Bakaus, Apache-2.0): about 23 commands covering layout, type and spacing. Installed: brand/tools/impeccable.
3. Taste Skill (Leonxlnx, MIT): stops the generic look. Installed: brand/tools/taste-skill.
4. Figma MCP + Playwright to design, build and test. Both are connected here (Figma connector on the Starter plan; Playwright with Chromium).
CTA: "comment KILLED for the guide". It's the same keyword-comment funnel as our "comment 11".

## What each tool does for us
- **Taste** (`node brand/tools/taste-skill/scripts/draw.mjs`) deals 3 researched art directions per brief, drawn from 247 award sites. Then it deals the full sheet: type, palette, hero and section blueprints. `inspect.mjs` checks the house rules in a real browser. Run: inventory of the subject, then the argument (claims and proof), then draw, then the idea sentence, then build, then screenshots at 3 widths, then fix.
  - Test: for an agro-exporter brief it dealt "page-is-the-object", which is our "the sack is the brand" idea.
- **Impeccable** (`sh brand/tools/impeccable/scripts/impeccable context`): modes (Persuade / Operate / Read / Experience) and commands (shape, critique, audit, polish, bolder, quieter, distill, harden, typeset, layout, animate, clarify, adapt, optimize). Read reference/craft-floor.md before any UI edit.
- **Emil design-eng**: the animation decision framework (should it animate, its purpose, easing, speed), never scale from 0, origin-aware popovers, clip-path reveals, @starting-style enters, hold-to-delete, comparison sliders.

## Where these clash with our standards (our standards win; noted honestly)
- Impeccable bans eyebrows/kickers above headings and 01/02/03 section numbers unless the sequence carries meaning. Our "11.01 + tag" index is a deliberate brand device on OUR social posts (Holographik lesson). On client websites, follow Impeccable: no eyebrow by default.
- "Monospace as a costume" is refused. We use Plex Mono only for data, measurements, codes and prices, never as decoration.
- Taste warns that taking ornaments away leaves a thin page. Minimal for us means fewer, bigger, real things (real renders, real data, whole colour fields), not emptiness.

## Positioning lesson
Tools now give anyone a decent template site for free. Our value is what they can't do alone: brand strategy, a world taken from the client's own place and product, Blender product renders, local payments and markets (MoMo, M-Pesa), accessibility, and the judgement to choose. We sell outcomes (bookings, orders, buyer trust), not pages.
