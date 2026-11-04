# Website design and building: what's current
## What juries reward
- Award winners combine three things: a specific art direction, directed motion and real-device speed. Sites that miss one of these tend to score in the mid-7s (hontran.dev)
- Static frames must work without motion, and motion has a "director": choreographed reveals and continuous transitions, not hard cuts or plain fades (hontran.dev)
- Penalised: 3D heroes that drop frames on mid-range Android, heavy pages (~9MB), templates with effects bolted on, missing reduced-motion paths (hontran.dev)
- Lovie Silver (Best Web Design, Aesthetic) went to a VFX studio site with time-of-day lighting and camera-move transitions (kota.co.uk)
- Webby categories to aim at: Best Home Page, Visual Design (Function and Aesthetic), Navigation/Structure, UX (webbyawards.com)
- Awwwards scoring is design ~40, usability ~30, creativity ~20, content ~10, plus a separate Developer Award (awwwards.com)
## Platform and tools
- Now Baseline: scroll-driven animations (animation-timeline: scroll()/view()), @starting-style entry animations, relative colour oklch(from …), @scope (modern-css.com)
- New and usable: contrast-color() for auto-accessible text, shape() responsive clip-paths, sibling-index() for CSS-only stagger, field-sizing: content, :open (modern-css.com)
- Still rolling out (use only with fallbacks): cross-document view transitions (no Firefox), grid lanes/masonry, gap decorations, @mixin (modern-css.com)
- GSAP is 100% free for commercial use, including SplitText, ScrollSmoother, MorphSVG and DrawSVG (unpkg.com/gsap)
- Framer 3.0 adds in-canvas AI agents, branching, and external agents (Claude Code, Codex, Cursor) (alternativeto.net)
## What's NOT working
- AI-built sameness: indigo gradients, Inter, light grey, rounded cards with faint shadows, three-icon feature grids, gradient hero text (dev.to)
- Fix: name the palette in hex, pick the typeface, describe the layout, and work from a reference or design system (dev.to)
## Market angles
- UAE: bilingual done properly. Design for Arabic from the start, use logical CSS properties, /en/ and /ar/ folders with hreflang, Arabic fonts (IBM Plex Sans Arabic, Tajawal, Cairo), a visible language switcher, and WhatsApp CTAs in both languages (element8.ae)
- Africa: WhatsApp Business Platform service replies inside the 24h window are now billable; in Nigeria that's about $0.01 per utility message and $0.06 per marketing message (msmeafricaonline.com)
- Africa, what that means: the website has to answer questions, show prices and take bookings itself, so fewer chats are needed (msmeafricaonline.com)
- Holographik DeepBook (Awwwards SOTD): black + one blue, isometric 3D icons, monitors in a dark room for the reveal; celebrate awards with a collage post (behance.net/Holographik)
## How we use it
- Every concept: one art-direction idea that works as a still, then motion layered on. Test at 4x CPU throttle on a 390 mobile; hold 60fps or cut the 3D.
- Use native CSS first (scroll-driven reveals, @starting-style, sibling-index stagger); bring in GSAP/Lenis only for choreography CSS can't do. Always ship a prefers-reduced-motion path.
- Before shipping, run a sameness check: no indigo, no Inter default, no 3-card icon grid. Name the hex palette and typeface in every brief.
- Page transitions should feel like camera moves (continuous), never hard cuts. Use same-document View Transitions where possible.
- UAE pitches: bilingual EN/AR built RTL-first, shown side by side in the reel (mirror moment).
- Africa pitches: "a site that answers before WhatsApp has to", with FAQ, prices, booking and order status on-page. Sell it as cutting message costs.
- Build every concept as real HTML, record a scroll reel and a flow prototype; mockups only through the preflight.
## Tools
- GSAP official agent skills (MIT): `npx skills add https://github.com/greensock/gsap-skills` (core, timeline, scrolltrigger, plugins, performance)
- Already vendored: brand/tools/ui-skills, brand/tools/ui-ux-pro-max
