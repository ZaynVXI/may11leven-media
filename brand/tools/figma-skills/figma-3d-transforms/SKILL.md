---
name: figma-3d-transforms
description: 'Add or edit 3D transforms in Figma: depth, perspective, z-axis rotation, tilt, isometric, card flips and parallax that flat 2D rotation cannot express. Use whenever a Figma request reaches into the third dimension ("make it 3D", "add depth/perspective", "tilt it back", "isometric", "flip it like a card", "parallax").'
---

# Figma 3D transforms (official Figma skill, cached)

The canonical, always-current text lives on the Figma MCP server. Before any 3D work in Figma, read it with the Figma tool `get_figma_skill`:
- skill://figma/figma-3d-transforms/SKILL.md
- skill://figma/figma-3d-transforms/references/carousels.md
- skill://figma/figma-3d-transforms/references/cubes.md

Load figma-use as well, and pass both names in skillNames.

## Key rules (summary of the official skill)
- Three fields: `node.transform3d` (per-element pose: FIXED_ORDER with translateZ, rotateX, rotateY, rotateZ required; optional backfaceVisible, visible), `node.scene3d` (containers only: perspective, preserve3d required), `node.transformOrigin` (the pivot, in PERCENT or PIXELS).
- Perspective lives only on the container (scene3d). Never put scene3d perspective and transform3d on the same layer: outer frame holds perspective, an intermediate frame carries the transform, children sit inside.
- Filled parent: keep it at preserve3d false (it can still carry perspective) and wrap the 3D children in a transparent preserve3d frame, so they don't cut through its fill.
- translateZ moves along the parent's Z axis; there is no X/Y translation in transform3d (use node.x / node.y). Assigning transform3d or scene3d replaces the whole object: spread the current value when changing one field.
- Perspective: honour an explicit choice; add it automatically for physical depth, popping out, or a single X/Y tilt; otherwise default to none (-1). Start at about 80% of the longest dimension or more.
- Signs: "tilt back" is positive rotateX; "tilt forward" negative. Hinges (doors, book pages, fans) need transformOrigin moved to the hinge first.
- Card flip: front 0°, back 180°, both backfaceVisible false. Carousel: rotate transparent preserve-3D slots, translateZ only on the item.
- Opacity, blend and effects don't render on a preserve-3D frame itself: put them on a flat ancestor.
- If transform3d reads back undefined, 3D isn't enabled: say so, don't fake it.
- Always read back the values and export an image to check the pose looks right.

## For May11Leven
Use it for page-wall reels (pages flipping like cubes), tilted screen layouts, card fans and parallax stacks in Figma, in the spirit of Obys's presentation, with our own motif.
