---
name: ui-details
description: The small UI details that make a component feel finished, studied from PXDX's "UI Details" posts. Read before designing any component, screen or product reel, and check every piece against the list at the end.
---

# UI details: the small things that make it look real

Zayn: "Pay attention to tiny details… they make a lot of difference."
Source: five PXDX "UI Details" posts (Bauhaus sheet, folder, add-name button, dropdown, components), saved in `brand/refs/pxdx-ui-details/`. Study only; we never copy their components.

## The details (what they do, and the rule we take)

1. **Corners nest.** A white tile sitting inside a grey track, a round button inside a search field, a highlighted row inside a dropdown: the inner corner is always the outer radius minus the gap. Rule: `inner radius = outer radius − padding`. Never the same radius inside and out.
2. **Equal gaps around nested parts.** The search button sits the same distance from the top, bottom and right edge of its field. Rule: one gap value per component, used on every side.
3. **Selected state is lifted, not just coloured.** In the alignment control the chosen option is a white tile with a soft shadow, raised out of a sunken grey track; the others are grey lines. Rule: selected = raised surface plus dark icon; unselected = flat and grey.
4. **Status is tone-on-tone.** "Available" and "Active" use a pale mint fill (#CCF8DF), a saturated green dot (#34E28D) with a darker ring, and dark green text (#0E9955). Rule: status chips use one hue in three strengths, never a grey chip with coloured text.
5. **Dots carry a ring.** The online dot on the avatar has a white stroke so it separates from the photo. Rule: any badge or dot that overlaps something gets a 2–3 px ring in the surface colour.
6. **Labels live inside the control.** "Delete" is a lighter pill inside the red button; "Notify" is a black pill under the alarm icon, inside the tile; "32 photos" is a frosted pill on the folder. Rule: when a control needs a word, nest it in its own small pill, so the control still reads as one object.
7. **Shadows take the object's colour.** The blue folder casts a blue glow, the red delete button a warm shadow. Grey shadows only under white things. Rule: coloured surfaces get a shadow tinted with their own hue at low opacity, large blur, slight drop.
8. **Images are framed by their container.** The chair photo inside the blue pill has a blue ring; the avatar sits in a red squircle. Rule: a photo inside a coloured control gets a thin ring of that colour, never a bare edge.
9. **Glass shows what's behind it.** The folder's front flap is frosted: you see the photos through it, blurred. Rule: use glass only where something real sits behind it.
10. **Dashed means empty or droppable.** "Upload files", "Add name" and the grouping box are dashed; filled things are solid. Rule: dashed borders are for placeholders, drop zones and empty slots only.
11. **Inactive is quieter, not hidden.** In the dropdown, idle rows have grey icons and grey text; the hovered row goes dark on a light fill. Rule: two text strengths in a list (idle and active), one icon weight.
12. **One icon set, one stroke.** Every icon uses the same stroke weight and round caps. Rule: never mix icon sets in a product.
13. **Microcopy has a voice.** The sign-out button says "BYE BYE". Rule: one line per product may have personality, and it goes on the least serious action (sign out, empty state), never on money or errors.
14. **The component fits the type.** "Hello, [+ Add Name]" — the dashed pill sits on the headline's baseline at about cap height, so the sentence and the control read as one line. Rule: inline controls align to the text they complete.

## How they present a detail
- One component per frame, small in a huge field, often inside a soft circle or ring (#ECEBE7 on #F8F8F6).
- A two-weight caption at the bottom centre: bold "UI Details", grey category ("Folder", "Button").
- Warm off-white, never pure white or flat grey. No device, no noise; the detail is the hero.

## For us
- **Every product gets a details pass** before it's called done: go through rules 1–14 on each component.
- **Term, now:** the "covered" chip goes tone-on-tone in chalk yellow; each child's card casts a shadow in its school colour; the paybill row nests "Pay school" as an inner pill; "Add a child" is a dashed slot; the term switcher (Term 1 / 2 / 3) uses the raised-tile selection; radii are recomputed so every nested corner follows rule 1.
- **A possible series:** "Details", one of our own components per post, presented our way (Ink or Bone field, Plex Mono caption, our own components from our concepts). Needs Zayn's go-ahead before it joins the plan.

## Check before shipping (add to preflight Pass 2)
- [ ] Nested radii follow outer − padding
- [ ] Gaps equal on every side of nested parts
- [ ] Selected states raised; idle states quiet
- [ ] Status chips tone-on-tone
- [ ] Overlapping dots ringed
- [ ] Coloured shadows on coloured surfaces
- [ ] Photos in coloured controls ringed
- [ ] Dashed only for empty or droppable
- [ ] One icon set, one stroke
