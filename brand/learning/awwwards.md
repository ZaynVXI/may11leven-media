---
name: awwwards
description: The living Awwwards file. Who won recently, what the winners do, and the current rules every May11Leven web, app and brand project applies. Updated by the daily craft run; read before any site, app or identity work.
---

# Awwwards: what's winning, and what we take

## How to study it from here (the method)
- **awwwards.com blocks our workspace** (both the page fetch and Playwright fail). Don't try to bypass it.
  1. Search for "Awwwards Site of the Day <month year>" to get the current list. The result snippets carry the names, studios and dates.
  2. For two winners a day, read the project write-up: the studio's case-study page, the European Design Awards page, Behance or the studio site, whichever appears in search results.
  3. When this session is linked to Zayn's computer, open awwwards.com in the built-in browser to see the sites and the score breakdowns.
- **Record:** the site, studio, date and award; the problem; the idea; three design decisions; interactions; type and colour if known; and one rule for us.
- **Then change the work:** add or update a line under "Current rules" below. Every project reads that section.

## Current rules (read before every site, app or identity job)
1. **Design the sale, not just the look.** Floema's principle: "sales can, and should, be designed". Catalogue and checkout are one product-first system, and the brand, catalogue and site are designed together. For our hotel and product clients, the site must take the booking, order or enquiry itself.
2. **Give each product a real 3D or real photo, and let people configure it.** Floema has a web-optimised 3D model for each of its 230 products, and orders go straight to the client's CRM. For our packaging and 3D service, offer the Blender model as a web-ready asset, not just a render.
3. **Time and season as interaction.** Floema's header changes with the seasons, from snow to full greenery, and its film was shot over a whole year. For After hours and Kusi, use day and night, high and low season, the same idea in our own world.
4. **Proof through material, not slogans, and say what the number is not.** Floema puts sustainability last and quiet, shown through materials and everyday use, not loud claims. The same goes for our safety and trust claims: show the mechanism (the slip, the source, the receipt). 197 Historias Ilustradas names itself after a number and says on its own page that 197 is the count of approved complaints, not the total of the disappeared. Every headline figure we use gets its source and its limit beside it (median not typical, concept not client, "about").
5. **Personality can be honest about machines.** Büro's site has a navigation "böt" that says it isn't AI: it's "a human pretending to think like a machine". For our AI agent work, label clearly what's automated and what isn't; a wink is fine, pretending is not.
6. **Restraint wins in serious sectors; show precision, don't claim it.** Polpharma Biologics (Nov 25, 7.36) opens on "Biosimilarity isn't discovered. It's engineered." and then proves it with exact behaviour: one teal family (#005453 to #E6EFEF), headline words that change from mist to teal as you scroll, and a single warm red (#F55D5D) kept for Contact only. Bright Biotech did the same with two colours. Trust sectors win with calm layouts, real material and strict palettes, the direction of Lebedev's Nova; the one warm colour belongs to the one action.
7. **Our mentors keep winning.** Holographik won again with DeepBook (Nov 3) and earlier Slush, CoMinVi and Permian. Studying them is studying the award bar.
8. **One real object carries the whole story** (Better Off, MotiveOne, nominated). A 3D model of the client's real place stays on screen while the copy changes, and each service appears as a layer on it (lines, cutaway). Pair it with proof cards (step counter, mono label, giant light numeral, a source line) and a search that is never empty. Full study: `brand/learning/betteroff.md`.
9. **One motion vocabulary per product.** Both of today's winners use one ease, one duration and one reveal for everything (expo.out, 1.1 s, a 14 to 16% rise), and keep WebGL for one hero moment, loaded only when near and paused off screen. Write it as tokens before any screen (--ease, --dur, --rise) and use the same values in the reel cut, so site, app and post move the same way. Reduced motion is part of the token set, not a patch.
10. **The award look is not the audit.** A teardown of Polpharma's winning build found 35 of 36 images without alt text, "Get in touch" buttons a keyboard can't reach, reduced motion ignored in most scroll scenes, two scroll videos (5.6 MB and 6.6 MB) loading at once, and debug code and a 364 KB source map left in production (animorio.com). It still won. Ours ship with alt text, keyboard reach, reduced motion, lazy media and no debug files, checked before the handover, and we keep their good habit: a cheaper fallback (CSS shapes) when the frame rate drops below 30.

## Log (newest first)

### Polpharma Biologics (Widelab): Site of the Day, 25 Nov 2026 (7.36, from our earlier search snippets); CSS Design Awards Website of the Day, 3 Nov 2026 (8.52)
- Source read: animorio.com/en/journal/polpharma-biologics-how-its-made/ (a third-party build teardown, 13 Nov 2026). We have not seen the site; this is from the write-up only. The write-up does not mention Awwwards.
- **Problem:** a biosimilar manufacturer has to look as exact as its labs, for partners and regulators who distrust hype. (The brief itself isn't published; this is what the site answers.)
- **Idea:** "Biosimilarity isn't discovered. It's engineered." The site shows precision through glass and exact motion rather than explaining it.
- **Decisions:**
  - a long scroll story (about 29 screens) where the headline's lines fold into a label as you scroll, then a diamond turns 90° and the next block rises
  - a menu drawn as one SVG shape, five pill links joined by narrow necks, that takes the colour of the section under it
  - four product bottles fanned at set scales (1.40, 1.15, 0.90, 0.70), so the range reads as one family
- **Interactions:** opening glass lenses on a five-stop shader gradient (lens in over 2 s, background at 40% of scroll speed); lines rise from 115% over 0.8 s with 0.1 s stagger; word colour mist #E6EFEF to teal #005453 between 15% and 37.5% of the scroll; page transitions 1.2 s on one custom ease (0.7, 0.05, 0.13, 1); three.js glass with a CSS fallback below 30 fps. Stack: Webflow, GSAP (ScrollTrigger, SplitText, Flip), Barba, Lenis, Unicorn Studio, Swiper, three.js.
- **Type and colour:** Concrette M for headlines at -0.04em, Season Sans for body; #005453, #16ABA9, #C6ECEB, #E6EFEF, #161517, and #F55D5D as the only warm colour (Contact).
- **What the jury didn't see (the teardown's list):** missing alt text on 35 of 36 images, unreachable buttons, reduced motion only partly respected, heavy videos loaded at once, debug and staging code in production.
- **Fits:** 02 web, 01 brand (a sector palette), 04 3D (glass product scenes).
- **Rule for us:** rules 6 and 10.

### 197 Historias Ilustradas (++hellohello): Site of the Day, 20 Nov 2026 (date from our earlier search snippets, not confirmed today)
- Source read: 197historiasilustradas.com/sobre-nosotros (the project's own "about" page). No build write-up was found; we have not seen the site's motion or type.
- **Problem:** to pass on the memory of people detained and disappeared in Uruguay (1960s to 1980s) to a generation that the team found needed a different language: "Queríamos crear un proyecto que tradujera la memoria colectiva a las nuevas generaciones."
- **Idea:** each illustrator portrays one person and is linked to them by something they share (a neighbourhood, a hobby, a football team). Stories are built from records, family testimony and photographs, and the page says plainly that truth and fiction are intertwined.
- **Decisions:**
  - the number is the name, and the page states its limit: 197 is the count of complaints approved by the national human rights institution, not the total of the missing
  - an artist directory with search, each entry naming the artist and the person they portrayed, with "Conocer" (meet) as the action
  - Spanish and English from the start
- **Interactions, type, colour:** not stated on the page we read.
- **Fits:** 02 web, 07 social (a story told one person at a time), 01 brand (a project named for its number).
- **Rule for us:** rule 4 (say what the number is not).

### Note on the fromanother and Minh Pham picks
The late-November winners (Polpharma Biologics, Two26 Studio) have no write-up we could reach: the agency pages refused the fetch, and the only Polpharma case page found (flyingbisons.com) is an older corporate rebuild with no award or design notes. So today's two are 2026 Sites of the Day whose builders published how they made them. We read the write-ups only; we have not seen either site.

### fromanother (artist-led creative agency): Site of the Day, 14 May 2026 (7.44), Developer Award (7.25), FWA of the Day
- Source: hontran.dev/blog/fromanother-award-winning-creative-agency-website (developer's own build note, 1 Jul 2026).
- **Problem:** an agency's site is its pitch, so it has to out-craft the portfolio it shows, and the team must add work and roles without a developer.
- **Idea:** one shared motion system across the site, WebGL kept for hero moments only, and a headless CMS the studio runs.
- **Decisions:** Prismic as the CMS, so a new project is a content entry, not code; WebGL mounted only when near the viewport (IntersectionObserver, 200 px margin) and disposed when it leaves; one reveal grammar for everything (expo.out, 1.1 s, rise of 16%, fade from 0, starts at 85% of the viewport), animating only transform and opacity.
- **Type and colour:** not stated.
- **Fits:** 02 web, 07 social (the studio's own site as content).
- **Rule for us:** rule 9 below.

### Minh Pham portfolio (designer at Fantasy): Site of the Day (7.37), developer score 7.77
- Source: hontran.dev/blog/minh-pham-portfolio-case-study (build note, 27 Jun 2026). Date of the award not given.
- **Problem:** a designer's portfolio where spacing, type scale and easing must match the design file exactly, and work images must stay at full quality.
- **Idea:** "designed, not decorated": one ease and one timing scale for the whole site.
- **Decisions:** fluid type tokens with clamp() (display from 3rem to 9rem); one scroll reveal (expo.out, 1.1 s, rise of 14%, fires once); a WebGL transition that displaces between two full-resolution images, with device pixel ratio capped at 2; reduced motion handled with gsap.matchMedia; the WebGL loop pauses off screen.
- **Type and colour:** not stated.
- **Fits:** 02 web, 01 brand (a portfolio is an identity).
- **Rule for us:** rule 9 below.

### Late November 2026 winners
**Sites of the Day:**
- Polpharma Biologics (widelab.co, Nov 25, score 7.36)
- Two26 Studio (ZzStudio, Nov 24)
- La boite à slides (Sparkk, Nov 23)
- 197 Historias Ilustradas (++hellohello, Nov 20)
- Carter Ogunsola (Nov 19)
- PSP Production (Lynksen, Nov 18)
- Sweet Tape (bikebear, Nov 17)
- Bulletproof (Nov 16)
- Preymaker (DashDigital, Nov 14)
- Delta Cafés (Bürocratik, Nov 13)
- Justin Jefferson (LayerTwo, Nov 7)
- DeepBook (Holographik, Nov 3)
- Grids (Obys, Nov 2)

**Honorable Mentions** around Nov 2–3: Monument (SERIOUS.BUSINESS), Arc'teryx System 0 (Teacher), Superscript (Joyful Talk), Flyshare.

**Pattern:** studio and portfolio sites, sports personalities, food and drink brands, and serious B2B (biotech, fintech and crypto). Almost all carry the Developer Award, so motion and build quality count as much as the look.

### Floema (Bürocratik): Site of the Month, May 2026, and Gold at the European Design Awards 2026
- **Problem:** genuinely sustainable makers get lost in a crowded "green" market. Floema makes signage, furniture and equipment for natural and urban spaces.
- **Idea:** a product-first site joining catalogue and sales, for two audiences: people who want specs, and people who relate through nature and city life. Brand, catalogues and site were built as one system over two years ("Made for Life").
- **Decisions:**
  - collections as the main structure (Urban, Golf, rePlastic, Nature, Details)
  - an editorial layout taken from the print catalogue
  - a 3D WebGL model per product, with customisation and orders sent to the CRM
  - calm brand sections, with sustainability placed last
- **Interactions:** WebGL foliage moving as you scroll, header audio on the About page, seasonal headers, and a film shot across a full year.
- **Our rule:** rules 1–4 above.

### Bürocratik's own site ("We are Büro", 18 years): Gold at the European Design Awards 2025
- Video-first: the reel is the interaction. A navigation "böt" in the menu bar explains what's on screen, and openly says it isn't AI.
- **Our rule:** rule 5 above.
