# OpenAlternative — free, open-source tools in place of paid ones

Source: https://openalternative.co/alternatives (directory of open-source alternatives to paid software).
Why it matters to us: our rule is no paid tools. Check here first before reaching for any paid app.
The site has no agent skills of its own; it is a tool directory. Agent tools listed there with skills or MCP support (Goose, Cline, Qwen Code, Zero) are not needed, since we already work in Claude.

## Our stack, mapped to free tools
| Paid tool | Free alternative we use or keep in reserve | Use for |
|---|---|---|
| Photoshop | GIMP (installed here), Pillow scripts (mm.py) | retouch, comps, grain |
| Illustrator | Inkscape, Graphite (browser, node-based) | logos, vector marks, label flats |
| Figma | Penpot (self-hostable, handoff), OpenPencil (MIT, headless CLI), Grida (Figma import) | UI mockups, design systems |
| Canva | Penpot, Graphite | social layouts (we mostly build in HTML/Pillow) |
| CapCut / Premiere | ffmpeg (installed), Shotcut, Kdenlive, OpenShot, OpenCut (browser), LosslessCut | reels, cuts, remux without re-encode |
| 3D / product renders | Blender (bpy, already our main tool) | bottles, packaging, props |
| Notion / Miro | listed (23 and 6 alternatives) | not needed now |
| Web analytics | Web Analytics category (16 tools) | for client sites we build |

## Rules
- Before using any paid app or credits, look up its row here or on openalternative.co and use the free one.
- Free tools still have to meet our standards: references first, minimal, high fidelity, preflight.
- Ads on the site (for example sponsored schedulers) are not listings; ignore them.

## Jitter (jitter.video): checked
- A web motion design tool with Figma import, 4K/GIF/Lottie export on paid plans, AI agents and a Jitter MCP.
- Free plan: 720p at 30 fps, 3 workspace files, limited AI credits. Watermark removal is Pro-only, so free exports likely carry a watermark.
- Verdict: not good enough for our posts (we ship 1080x1920 and 1080x1350, unwatermarked), and its AI generation conflicts with our no-AI-imagery rule. Use it only for inspiration (its templates and motion ideas).
- Our free motion stack does the same jobs: HyperFrames (HTML to video), GSAP/CSS in HTML recorded with Playwright and ffmpeg, the Pillow reel pipeline and Blender. Lottie export is possible via lottie-web workflows when a client needs it.
