# Motto × Ivo: how a product case study is presented

References: `brand/refs/reels/motto-ivo/` (5 slide videos from one post, plus the caption). Ivo is legal-contract AI. Motto designed the website and product.

## The slides (each one a short looping video)
1. **Phone on a warm surface with window-light shadows**, dead front-on. A real flow plays out: type a question → "Generating report…" → report → table. It's one complete task in about 12 seconds.
2. **Content cards scrolling sideways:** illustration, portrait and quote cards on warm grey. It shows the editorial world (commissioned illustration, real people).
3. **One component on the brand's field green:** "Create AI Field" → type a question → Generate → a table with Yes/No pills. A single interaction, zoomed in, on the brand colour.
4. **The navigation itself as a micro-interaction:** three icons (one mark, three expressions), with a hover tooltip ("Review", "Assistant") and a green selected state. It's a 6-second loop of nothing but hover.
5. **A data idea drawn as a diagram:** contract versions (Mutual-NDA.docx → Vendor-Agreement_Draft → Executed) linked by labelled pills ("Supports negotiation", "Supersedes"), branching into child documents. It's the product's logic, animated step by step.

## Why it's so clean
- **One idea per slide.** Each video shows exactly one thing: a task, a component, a nav, a relationship.
- **Real content in every state:** real filenames, dates and questions ("Does this contract grant us rights to use the counterparty's logo?").
- **Colour has a job.** Ivy green is the field and the action colour. Soft lime is the selected state. Red and green pills are No and Yes. Lilac and amber are relationship types. Everything else is warm white and grey.
- **The motion is slow and functional:** a cursor, a hover, a typing caret, a state change. Nothing decorative moves.
- **The caption sells the problem and the decisions:** "an information architecture problem before it's a design problem". It names the type pairing and the colour system with reasons, credits the illustrator, gives one real result ("winning 85% of competitive trials"), and ends with the case-study link.

## What we do with it
- **Our product case studies become 5 loops:** (1) the full task on a phone in a real scene, (2) the content or editorial world, (3) one key component on the project's field colour, (4) the nav or a micro-interaction, (5) the system logic as an animated diagram.
- Record real HTML with Playwright video (cursor, typing, state changes). Never mock up motion we didn't build.
- Captions follow the Ivo pattern: the problem → the decisions as → bullets → type and colour with reasons → one true result (or "concept") → a link.
- **First one to build: Check** (`tools/check/`). It's a real tool, so every state is real.
