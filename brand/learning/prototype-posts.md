---
name: prototype-posts
description: How to show a product as a working prototype in motion, not as static frames. Learned from the Pixie and Dixie "Figma Motion + Claude" posts Zayn sent. Read before presenting any app, widget or site.
---

# Show products working, not as frames (Zayn, 18 Nov)

Zayn: our products were shared as frames; studios share them like a real product or a working prototype. Reference: Pixie and Dixie's design experiments (Figma Motion + Claude), 12 reels and 6 stills in brand/refs/pixie-dixie/ (frame sheets A.jpg, B.jpg). Their faces and photos are references only, never used.

## What they do
- Every post is motion, 6–27 s, 4:5 (720x900). Most loop seamlessly in 12 s.
- The UI is alive: numbers tick (14° to 17°), rings fill, a pill grows into a card and the card morphs into the next product, a play button turns to pause.
- A wall of many widgets in one system, each moving a little, so the account reads as a product family.
- A cursor-style "explore" circle moves over a gallery like someone is using it.
- One tight system: black cards, one blue glow, big name plus grey sub-line ("H.Plan / Mon"), a short line of body copy at the bottom.
- Stills are the hero frames of the same motion, and a corner label says what it is ("Card · UI design · Experimentation phase (17)").
- Caption: short, human, a series name and number, what tools made it.

## Our rule from now on
1. Every product concept is built as a working prototype first (real HTML/CSS/JS states and interactions), then recorded.
2. The feed post for a product is a 4:5 motion piece (10–20 s, loops) showing it working: state changes, numbers moving, a tap, a transition. Static carousels become the secondary format (detail and story).
3. Show a family: several widgets or screens of the same product moving together, then one hero interaction up close.
4. Tools: HyperFrames for the recorded motion, the live prototype published as an artifact link for Behance/LinkedIn, Figma for the master frames.
5. Label: series name and number ("Working demos 02 · Term · concept").

## How they present one concept app (pxdx "Conversation Tone Assistant", carousel, 1,613 likes, 407 shares)
1. **Hero (motion):** a real photo (a hand holding a phone, no face) inside one big rounded oval, the product's widgets floating around it, one line of UI text on the phone screen ("Hey, Annie").
2. **The whole system:** a 3x3 grid of every component, each on its own background tone (fog gradient, paper, dark grey), one component per tile.
3. **Component close-ups:** one component large, cropped by the frame, with a two-line label in a corner: name plus component type ("Real-Time Voice Analysis / Popover", "Payment authorization / Notification").
4. **States:** the same component in two states on consecutive slides (recording, then the "Cold assertiveness" result).
5. **Collage:** the components overlapping inside the oval again, as a family.
- Palette: fog blue-grey to black, warm paper, one hot accent (orange-red) used only for data and the card.
- Type: one grotesk for UI, one monospace for transcript text.
- Caption: product name, "First draft of UI (01)", then a two-line sign-off. No hashtags, no hard sell.

## Our version for each product
Hero motion (photo plus floating widgets) → system grid → 2–3 component close-ups with name and type labels → one state change → family collage → our offer slide. Hands and objects only, no faces; photos from Unsplash or Pexels through the connector.

## Why PXDX's AI-made UI looks better than ours (honest review, 18 Nov)
PXDX Studio, Wrocław (pxdx.pl blocked here; Dribbble: dribbble.com/PXDX). Product, UI and web design; AI tools, audio apps, booking apps, e-commerce, 3D.
1. **They design in Figma first, then let Claude animate inside Figma (Figma Motion).** AI moves their designs; it doesn't invent them. We have been generating every product from blank HTML.
2. **They taught Claude their style once, as a skill, and keep improving that skill** ("Improve your skill as you go"). Every new piece starts from the same rules. We restart the look every time.
3. **One component language across everything:** the same pills, rounded cards, grotesk plus mono, fog gradients and one glow. Seventeen "experimentation phases" in, it is a recognisable system.
4. **Small units:** one card or widget per post, perfected and animated. We try to tell a whole story with headlines in six slides.
5. **Almost no words on the design.** The UI and a two-line label carry it; the caption is one line.
6. **Real photography** (hands, silhouettes, objects), graded to the palette.

## Our fix
- Build a May11Leven UI kit in Figma (pills, cards, widgets, type, glows, grain) as the base every concept starts from.
- Write our own motion skill on top of figma-use-motion, with our timing and easing rules, and improve it after every piece.
- Run a numbered series of small experiments ("Lab 01, 02 …"): one component, designed in Figma, animated, posted with a one-line caption. Bigger concept launches use the pxdx presentation order above.

## PXDX on Dribbble: what their whole portfolio teaches (16 shots studied, brand/refs/pxdx-dribbble/)
Shots: SAMUR.AI assistant builder, podcast app, AI creator subscriptions, NOAL soft-drink bar, tennis court booking, McStar's planner, T.029 audio card, LAQ furniture, HUSH jewellery, Bento Box record label, Ramen delivery, antivirus, Ramu culinary, dark vs light, Dormy app.
1. **Every product lives in its own world.** The UI floats over one full-bleed scene from that product's life: a samurai for an AI "warrior" builder, a desert room for a calm podcast app, the actual tennis court, a red classic car and a negroni for a no-alcohol bar, a sunlit bedroom for furniture, a bowl of ramen for delivery. The scene sets the mood before you read a word.
2. **No two products share a look.** Pixel font for the AI tool, bold condensed type for the drinks bar, editorial serif for food, soft neumorphic grey for the audio card. Palette comes from the scene.
3. **Cards, not full screens.** Two to five UI cards grouped like a dashboard of the product, overlapping slightly, often frosted over the photo.
4. **Real product detail inside every card:** prices, times, order numbers, court numbers, ratings, a progress bar, a selected state.
5. **Bento layouts for websites:** big wordmark, three or four tiles, one strong colour block.
6. **A phone in a real place** (Dormy on concrete, banking app on green silk) when it is a mobile app.
Caution: some of their imagery looks AI-generated (portraits). We get the same effect with free stock photos through the Unsplash connector, Blender scenes and our own grading, never AI images.

### Our rule
Before building any product, pick its world: one hero scene (photo or Blender) from the product's real life, a palette from that scene, a typeface that fits it, then design 2–5 cards that float over it. Motion comes after, in Figma.

## Case study: PXDX "Rosie" (one post, about 7 slides) — Zayn, 19 Nov
Refs: `brand/refs/pxdx-rosie/`, loops in `brand/motion-refs/reference-4/5-rosie-*.mp4`. Their people and renders look AI-made; we take the structure, never the imagery or faces.

**Why it works:** they invented a product that answers a real modern problem (endless scrolling) and showed it as a whole world: a device, an app, a voice, notifications. The post sells their skill by showing a finished product, not a design.

**The slides, in order**
1. Hero (video): phone held in a hand against a big soft light disc, the app's widget grid on screen.
2. Manifesto: black, one paragraph saying what the product does and for whom, then the next line in grey ("Hi, Rosie…"), the voice orb and a "Let's talk" pill. Copy as a slide.
3. Split 50/50: top, a human moment with a spoken line over it; bottom, the object, with a UI pill ("Rosie connected") floating on its shadow.
4. One full app screen on flat grey: the device inside the app, real states (OFF, Disconnected, battery 68, Saving mode on, Product test 5 steps), "swipe to start" slider.
5. Split again: top, a landscape with a live pill ("Rosie speaking 03:48"); bottom, the object in another state.
6. Loop, 10 s: the camera drifts off the object, a pill grows into a "HYDRATE" card, text types on, it folds back, the object returns. First frame = last frame.
7. Loop, 11 s: "ROSIE" types on in dot-matrix with a cursor over a dot grid, a toolbar slides in, then it types off.

**Details that make it one product**
- One colour world (lilac, violet, teal) on every slide, phone, object, landscape and grade.
- A signature display face (dot-matrix) used only for the product's voice: OFF, 68, 2h, HYDRATE, ROSIE. Body UI stays plain sans.
- One mark (the orb with dots) repeats everywhere: button, avatar, slider handle, notification, device top.
- Every screen shows a state, never an empty layout.
- Split slides carry two ideas each (moment + object), so 7 slides feel like 14.
- Microcopy with warmth in one place ("You're a badass today!", "swipe to start").

**Caption:** one line saying what it is ("Interface design for voice assistant device"), two or three sentences of the product story (what it does, the human benefit), a sign-off themed to the product ("Lots of quality time, Pixie and Dixie"), five hashtags.

**Our rule (Zayn):** a good product gets a full carousel, about 7 to 10 slides mixing stills and short loops, not 3 to 4 frames. Order: hero loop → manifesto → split moments → full screens with states → feature loops → system or detail slide → offer. Our caption keeps its own rules (lowercase, comment 11, both emails) and adds a themed sign-off as May11Leven Labs.

- **Add to the skill (PXDX NOAL):** required notices (cookies, age, allergens, delivery area) go inside the hero as a small band or toast in the product's voice, with "no" the same size as "yes" and nothing hidden under it. Never a sticky bar across the bottom.
