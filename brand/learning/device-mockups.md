# Device mockups that look real (study of Zayn's camera-app references)

References: `brand/refs/device-mockups/camera-app-main.jpg`, `camera-app-style.jpg`, `camera-app-wb.jpg`. A film-camera app shown on a regular phone and on a foldable, side by side.

## Why they look real and premium
1. **Dead front-on, no perspective.** Nothing to warp, so there are no projection mistakes. The device reads like a product photo, not a 3D stunt.
2. **Correct hardware details.** Side buttons sit on the frame edge, both cameras appear (with the tiny green privacy dot), the foldable hinge bar shows on the left edge, and the bezel is even all round. Each device is a recognisable real model with its own corner radius, and the screen radius follows the body radius.
3. **The screen sits inside the glass.** There's a black inner border before the UI starts, and the UI never touches the frame.
4. **A quiet stage.** A flat cool grey (measured #EDEDEF) with a very soft contact shadow under each device. No props, no gradient, no reflections.
5. **Same app, two form factors.** The phone runs a stacked layout and the foldable a side panel (the settings rail moves to the right). The layout itself shows the design is responsive and thought through. This is proof, not decoration.
6. **Real states and real content.** A real landscape photo, and real values (1/60, ISO 100, 5,600K, Weak or Strong selected, Look Intensity 100). Every screen in the set shows a different state of the same app (main, style, white balance).
7. **One accent, used for state only.** Red (#FE001C) marks the selected value and section labels; everything else is white on near-black. Labels are small caps with wide tracking.
8. **Series consistency.** Three tiles: same stage, same scale, same device positions, so only the UI changes. That makes a strong carousel.

## How we use it
- Default device presentation for app work: front-on, real hardware details, cool grey or the concept's own neutral, a soft contact shadow, 2 form factors where it makes sense (phone plus foldable or tablet).
- Build the device in Blender (may11leven-blender), or as a precise SVG or CSS frame for flat front-on shots: correct radii, side buttons, camera and inner border. Composite the real HTML UI at @3x.
- Show 3 states across a carousel, with fixed device positions.
- Preflight: check button positions against the real model, that the screen radius matches the body, that nothing touches the frame, and that the shadow is barely there.
