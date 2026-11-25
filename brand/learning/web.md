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

## Holographik CoMinVi lessons (web)
- Industry sites can be premium: one cinematic 3D hero, then calm white cards. Dark for drama, white for reading.
- Turn the client's product into the interface: a mineral list that swaps a 3D rock; clients as a wheel picker; operations on a dark map with one lit region.
- Numbers as design: big figure + mono caption + tiny line icon, hairline above.
- Section system: boxed index (S.01) + black pill label; same everywhere, so it feels engineered.
- Photo-filled headline type for the story section.

## Satto lessons (web templates)
- Index-first portfolio: a numbered table (Num, Project, Client, Role, Year) where hovering a row floats its image; active row inverted black.
- Header as a grid of small cells (page name, studio ©, email, nav) instead of a classic navbar.
- Present sites as a stacked pair of screens on a blurred photo from the same project.

## Deep dive: the price-first property site (Wed)
What the category does: almost every developer site hides the unit price ("From X, check brochure", "call for price"). Of ten top real-estate sites reviewed by toimi.pro, only 111 West 57th had a unit selector with a stated price range; Airbnb's upfront total price is the trust move the rest of the web learned from.
- Africa (Kigali, Nairobi, Dar, Kampala): buyers include the diaspora, who browse at night from Europe and the Gulf with nobody to call. A Kigali listing like The ONE Residence (Kimihurura) shows only "From 374,000,000 RWF" and a 30% deposit. Angle: a developer site that lists every unit with price, size, floor and status, plus the deposit and handover split in RWF, works on a mid-range phone and has a Kinyarwanda / Swahili toggle in the nav, not the footer. Practice piece today: Ikiyaga.
- The Gulf: bilingual EN/AR is the baseline. From element8.ae: mirror navigation, arrows, sliders and forms with CSS logical properties (inline-start/end); keep Western Arabic numerals (1, 2, 3) for prices and phone numbers and never mix systems on one page; give Arabic more line-height and never track it (it disconnects joined letters); use fonts built for Arabic (IBM Plex Sans Arabic is already in our library); the language switch is visible, one click from anywhere, and remembered, never guessed from IP. Angle: the same price ladder, mirrored, with the price column on the left in Arabic.
- Rest of the world: the 2026 trend reports agree on minimal copy and "TL;DR" first screens (Webflow: Ruul, Flabbergast) and warn against bento grids for single-message pages (Orbix). Angle: sell price transparency as the design idea itself, the way Compass leaves colour to the photos and Airbnb leads with the total.
- Build notes: list as an ordered list (not a table of pills); status as text plus tone plus strike-through; tabular numerals; one selected row drives the detail strip; one CTA naming the unit ("Book a viewing of 5B").

## Deep dive: required notices as part of the design (Wed)
The parts of a site the law makes you show (cookie consent, age, delivery limits) are usually a template bar bolted on at the end. Today's view: design them as content, in the brand's voice, with refusing as easy as accepting.
- Africa: Kenya's Data Protection Act 2019 has no cookie-specific clause; a consent vendor's guide (flexyconsent.com, Kenya DPA guide) reads the ODPC's guidance as requiring a clear opt-in for non-essential cookies and a first-layer "reject" as prominent as "accept". That's a vendor's reading, so check the ODPC text before a client build. Nigeria has its own regime (NDPA 2023 and the GAID 2025 directive, ndpc.gov.ng); not read yet, read it before any Nigerian site. Angle: a Nairobi shop or hotel site whose notice says in one plain line what it keeps and why, with two equal buttons, and still works if you say no (Miwa practice piece).
- The Gulf: Saudi Arabia and the UAE both have a PDPL, and consent platforms now ship banners made for each (osano.com, "new Saudi Arabia, UAE banners"; cookieyes.com has an Arabic PDPL page). Angle: the notice in Arabic and English, mirrored with logical properties, the two buttons equal in both directions, and the language choice remembered.
- Rest of the world: WCAG 2.2 SC 2.4.11 fails any sticky banner that fully hides a focused control; scroll padding or keeping the notice in the page flow fixes it. Godly's feed shows the same idea from the craft side: small states like a security check or a badge are now worth a whole post. Angle: a "details" post of one notice done well, before and after.
- Build notes: notice in the page flow, never fixed over content; one sentence on what is kept, one question; "No thanks" and "Yes" the same size and weight of border; the site works fully after "No".
