# Harvey II redesign (six clips Zayn sent): how a product team explains design decisions

Harvey is a legal AI platform. Their redesign was posted as a series of short loops (6–9 s, 720x900, no sound), one design decision per clip. Frame sheets are in `brand/refs/harvey/`.

## The format
- **Top two-thirds:** a looping UI clip on a grey (or dark) backdrop, cropped tight on the one detail being explained. Motion shows the before and after, or builds the detail: the nav switching from a light to a dark theme, a word being typed and the serif swapping in, corner radii drawn with construction circles, a cyan padding overlay fading away.
- **Bottom third:** white, with a serif title in sentence case ("Softer, friendlier corners") and 2–3 lines of plain sans explanation of *why* ("Rounded, but not too round, to balance the precision of our typefaces").
- **Footer:** the small mark plus the series name ("Harvey II Redesign"), the same on every clip.
- One decision per post. The title is the decision, the body is the reason.

## The six decisions (what they teach us)
1. **Unmistakable interface:** a new foundation that feels precise, premium and cohesive, "everything you need and nothing you don't".
2. **Cohesive navigation:** as the product grew, they regrouped and sharpened the nav.
3. **Refined type system:** a serif and a sans built on identical metrics, so they sit together on any surface. Typing animation shows the swap.
4. **Softer corners:** a radius chosen to balance the typefaces, shown with construction geometry (circle guides, dashed grids).
5. **Fewer containers, clearer focus:** fewer boxes mean more room. Colour pulls the key UI forward and the rest recedes.
6. **Roomier padding:** they heard users found screens cluttered and answered with space. The padding overlay makes the spacing visible.

## How we use it (steal like an artist, never copy)
- **A new series for our UI/UX and app or website design and development services: "Design decisions".** One decision per post, as a 6–8 s loop with silent or quiet instrumental audio.
- **Our version, not theirs:**
  - the clip sits on our cool grey or the concept's colour world
  - the explanation goes in Inter Tight or Hanken Grotesk (our serif accent only for one word)
  - our Plex Mono series label and the 11 mark in the footer
- **Topics from our own concepts:**
  - why fade.'s queue number is so big
  - why the Inzu booking takes three steps
  - why the Kora Dental assistant offers time chips instead of free text
  - why the Imisozi shop picks origin before grind
  - why the services carousel uses one colour per service
- **Show the craft visibly:** construction lines, spacing overlays (8 px grid in a single accent), before/after toggles, type metrics. This is proof of process, which clients buy.
- **Explain with user reasons, not taste words:** "people couldn't find X, so…", "on a slow phone…". Never invent user research; for concepts, say "we designed it so…".
- **Accessibility as a decision post:** contrast, tap targets of 44 px or more, the l and 1 problem in our own emails.
- Build the loops with Playwright recordings of real HTML states (hyperframes or our prototype recorder), then compose them in our layout. 720x900 or 1080x1350 (4:5).

## Tools noted
- Savee (savee.com) has an MCP server (https://mcp.savee.com/mcp, OAuth), but it **requires a paid Savee subscription**, so we don't connect it under our free-tools rule. Savee can still be browsed for mood boards.
- Mobbin's MCP also needs a paid plan. We use our own screens and free references instead.
