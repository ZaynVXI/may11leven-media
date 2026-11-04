# Refero Styles — style systems from real product sites

Site: https://styles.refero.design (2,000+ style systems, each with a DESIGN.md: colours with roles, type scale, spacing, radius, components, do/don't).
Free use: the style pages read openly. The Refero MCP (live search) needs a paid plan, so we don't use it. The Refero skill (MIT) works without it and is vendored at brand/tools/refero.
How we use it: pick 3–4 styles that fit the client's world, choose ONE as the lead, keep its sharp traits, borrow 1–2 details from the others. Never copy one site.

## Styles studied (first pass)
### teenage engineering — industrial catalogue
- Canvas #F6F8F7, ink #000, carbon bands #0F0E12, rules #E5E5E5, muted #B2B2B2. Colour almost absent.
- Very light type: body weight 100 at 13px, headings 300 at 40px, lh 1.11. Always left aligned.
- 0 radius everywhere. 1px hairlines organise sections. No shadows, no gradients.
- Product photos fill the grid cell edge to edge; name + text buy link below. Dark full-bleed band with one product and a small label bottom-left.
- Lesson for us: the product is the only rich element; lightness of weight is a style in itself.

### monopo saigon — agency, black and white
- #000 / #FFF only; greys #6D6D6D, #181818. The only colour is one iridescent hero texture (mint → orange → oxblood), used as media, never UI.
- Roobert 300/400. Display 225px, big headings 94px at lh 0.76. Tracking 0.
- Radius rule: pills 75px for buttons/tags, 0 for everything else, nothing in between.
- Alternating white and black bands; single-column project list, full-width image, title below at 16–18px.
- Motion: cubic-bezier(0.19,1,0.22,1), 0.8–1.25 s.
- Lesson for us: closest to our studio voice. Huge display type plus one colour moment per page.

### Apple iPhone — product-first gallery
- White canvas, #F5F5F7 bands, ink #1D1D1F, secondary #707070. Blue split by role: #0066CC links, #0071E3 filled pills only.
- Hero 80px/600, tracking -1.2px. Body 17px, lh 1.47. Section gap 90px.
- Cards and media 28px radius, no shadow; media may crop past the card edge.
- Hardware large on white or warm neutral; leave big space around it.
- Lesson for us: product renders on clean white with one blue role is the benchmark for our Blender work.

### Raycast — dark power tool
- Canvas #040506, panels #07080A, hairline #363739. One coral #FF6363 for logo/badge/active row only.
- Inter 400 at 56px hero (regular weight on purpose); Geist Mono for metadata with pipe separators.
- "Keyboard-key" card stack: inset top highlight 5% white, 1px ring 25% white, inset bottom shade.
- Lesson for us: our Plex Mono labels match this; dark posts can use inset hairlines instead of shadows.

## Rules taken from the Refero skill (fit our standards)
- Research before design; name the references and what each one gives.
- Reference lock before building: lead reference, 3–5 traits to keep, 1–2 borrowed details, what to reject.
- Don't average references into a safe middle (dark becomes cream, acid becomes clay). Pick one and stay sharp.
- A token's role is part of the token: a CTA colour stays CTA-only.
- Keep image roles: if the style is photo- or product-led, use real renders, never weak CSS fakes.
- No indigo/violet, no cards by default, no emoji icons, no decorative left stripes, no one-word italic serif swaps.
- Watch "calm editorial on autopilot": cream canvas + clay/olive + airy serif. Use it only when the client's world calls for it.
- Decision ledger: every big choice traces to a reference, the brief or a craft rule.

## Self-check against our recent work
- Imisozi (cream, clay, moss) sits near the "calm editorial" pattern. It is justified (coffee, soil, lake, hills), but the next posts should go in a sharper direction (e.g. monopo-style black/white with one colour moment, or teenage-engineering lightness) so the grid doesn't settle into earth tones.

## Skipped
- Accessibility parts of the skill (our rule: we don't study accessibility).
- Paid Refero MCP.
