# Accessibility — study and standards

Accessibility is part of quality. Minimal design and accessible design want the same things: clear hierarchy, readable type, honest contrast, calm motion.

## The standard
- Build to WCAG 2.2 AA. WCAG 3 is still a working draft (latest update March 2026), so it isn't the target yet. Watch its contrast model (APCA-style) but don't design to it.
- European Accessibility Act: in force since 28 June 2025 for e-commerce, banking, booking/transport, e-books and similar consumer services sold to EU customers, including companies outside the EU. Exempt only if fewer than 10 staff AND under EUR 2m turnover. Standard: EN 301 549 (WCAG 2.1 AA now, moving to 2.2 AA). Needs an accessibility statement. Fines are set per country (Germany up to EUR 100k).
- Selling point for clients: EU shop/booking clients need it by law; African and Gulf clients selling to Europe need it too. We build it in from day one, never as a bolt-on.

## Our rules (designers)
- Contrast: body and small text at least 4.5:1; large text (24px+, or 19px+ bold) and icons, borders of controls and focus rings at least 3:1.
- Hierarchy by opacity, with a floor: muted text no lighter than ink at about 62% on light backgrounds, or paper at about 50% on dark. Below that, only for decoration, never for words people need.
- Colour is never the only signal: errors get text and an icon, selected states get weight or a mark, not just a colour change.
- Type: body 16-17px on web (never under 14px), line height about 1.5, line length 45-75 characters. Left-aligned body copy.
- Touch targets at least 44x44 px; WCAG 2.2 minimum is 24x24 with spacing.
- Focus: visible focus ring on everything clickable (2px, offset, 3:1). Never remove outlines without a replacement.
- Motion: respect prefers-reduced-motion (cross-fade instead of slides/springs); nothing flashes more than 3 times a second; anything that moves for over 5 s can be paused.
- Glass layers: keep text legible; respect prefers-reduced-transparency (solid fallback).

## Our rules (build)
- Semantic HTML first: header, nav, main, footer, h1-h6 in order, button for actions, a for links, label for every input. ARIA only as a fallback.
- lang attribute, descriptive page titles, alt text on meaningful images (alt="" on decorative ones), icon buttons get aria-label.
- Forms: visible labels (not placeholders), autocomplete attributes, errors described in text next to the field, status messages in an aria-live region.
- Keyboard: everything reachable with Tab in reading order, Escape closes dialogs, focus trapped in modals and returned on close, a skip link.
- Layout reflows at 320px width and survives 200% text zoom (rem/em spacing).
- Video on sites: captions; no autoplay with sound.
- Test before handover: axe-core or pa11y run (free), keyboard-only pass, a screen reader pass (VoiceOver or NVDA), contrast check of every token pair. Publish an accessibility statement for EU-facing clients.

## Our rules (social)
- Reels: burned-in captions/on-screen text big enough (48-60px+ on a 1080 canvas), strong contrast, inside the middle safe zone, each block held 2-4 s.
- Add alt text to image posts and reel covers where the tool allows (Instagram app: Advanced settings, Write alt text).
- Hashtags in CamelCase (#BrandIdentity) so screen readers read them properly.
- No flashing; text not baked into busy photo areas without a shade band.

## Self-check on our recent work
- Imisozi muted grey #8A837A: 3.24:1 on paper and 2.88:1 on tile. Fails for small text. Fix: #6A635A (5.13:1 paper, 4.56:1 tile).
- ata reel MID #78746E on paper: 4.04:1. Fails for small labels; fine for 24px+ headings. Use about #6A665F for small text.
- Imisozi hairlines #DCD5CA: 1.26:1. Fine as decorative dividers, but never as the only edge of a button or input (needs 3:1).
- Ink on paper (14.95:1), closing-card grey on ink (5.46:1), MoMo button (5.74:1) and the stock pill (7.61:1) pass.

## Free tools
axe-core / @axe-core/playwright, pa11y, Lighthouse, WebAIM contrast checker, VoiceOver (Mac/iOS), NVDA (Windows), TalkBack (Android). Local references: the design-skills accessibility-audit skill and the design-superpowers accessibility knowledge file.

Sources: W3C WAI (WCAG 3 draft, March 2026), testparty.ai EAA checklist, OpusClip reels captions guide.

## Pass on all scheduled posts (done)
- Tool: brand/code/a11y (Pillow hook + HTML audit). 7 posts fixed: brand clinic, barber app, three-lights reel, Inzu, Bathu, ata reel, Imisozi.
- Fixed: muted greys and faded list items below 4.5:1; white labels over light photo areas; labels on clay/moss/gum swatches; text under 20 px on posts (24 px on reels); Imisozi site grey #8A837A to #6A635A and labels 10-11 px to 12 px; Inzu booking button clay to #9E5532.
- Reels: three-lights labels moved out of Instagram's bottom caption zone; stronger shade bands so white text stays white over bright shots (fix photos with shade, not by recolouring text).
- Every post now has alt text per slide and CamelCase hashtags.
- Lessons: measure the bulk of the background, not thin borders of the same colour; component boxes must size from the actual font size.

## Lesson: quiet text still has a floor; targets and focus (WCAG 2.2 AA)
- 1.4.3 Contrast: secondary text in an opacity hierarchy must still reach 4.5:1. On Bone #EEEBE4, Ink at 45% is 2.94:1 (fail); 60% is 4.68:1 (pass). Our tint floor on Bone is now 62%.
- 2.5.8 Target Size (Minimum): pointer targets at least 24x24 CSS px, or spaced so a 24 px circle around each doesn't touch another. Our buttons are 44 px tall; table rows used as links are 41 px.
- 2.4.11 Focus Not Obscured (Minimum): a focused control must not be fully hidden by author content (sticky headers, cookie bars). Keep sticky bars short and add scroll-padding-top.
- Also: plans and diagrams are images; give the SVG role="img" and a label that says what is highlighted and why, not "floor plan".
- Applied today on the Kilele page: dim tint 45% to 62%, mono labels 11 px to 12 px, a visible 2 px Infrared focus ring, SVG label naming 6B, its size and its west facade. webaudit: v1 had 50 failures, v2 has 0.
- Source: W3C WAI "What's new in WCAG 2.2".
