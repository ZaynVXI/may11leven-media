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

## Lesson: alt text for a data graphic (WCAG 1.1.1, nightingaledvs.com)
- A chart's alt text says three things: the chart type, what it measures, and the point it makes. The source link goes in the caption, not in the alt text.
- Applied to the Zanzibar tile: "Timeline chart from 0 to 12 seconds of how long independent Zanzibar hotel websites take to show their main content on a mid-range phone. The median is 9.6 seconds, well past Google's poor line at 4 seconds. The first thing appears at 3.5 seconds."
- Contrast: webaudit on the tile returned no failures (grey #8F8F8F: 6.1:1 on #0B0B0B; on the #161616 zone 5.6:1, checked by hand because the audit reads the page background, not the zone; smallest text 20 px). The infrared line is never the only carrier: the 9.6 s value is also written as text.

## Lesson: target size, WCAG 2.2 SC 2.5.8 (getstark.co, deque)
- AA minimum is a 24x24 CSS-px target, OR a target smaller than that with enough space that a 24px circle centred on it doesn't overlap a neighbour's circle. Exceptions: inline links in a sentence, an equivalent larger control elsewhere on the page, and where a platform convention sets the size. Native iOS/Android still expect 44x44pt / 48x48dp, which is the stronger bar we design to.
- Applied to Mita: the amount chips were 44px tall but sat in a 4-up row - at 390px wide that's ~86px each with 8px gaps, so both the 24px-circle spacing rule and the 44pt native bar pass. The four nav tabs are 64px wide boxes, well clear. The "Why units vary" link is an inline text link, so it's exempt from the 24px rule but still sits on its own 44px row. Checked: webaudit returns 0 contrast failures; ink on the green block is 11.4:1 by hand (the audit reads the page ground, not the coloured block).
