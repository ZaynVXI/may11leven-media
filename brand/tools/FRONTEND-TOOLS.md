# The "5 free tools for Claude's front end" (from the reel Zayn sent), as installed here

| Tool | Where | What we use it for |
|---|---|---|
| Taste | `brand/tools/taste-skill` (MIT) | design rules against generic AI looks; `node brand/tools/taste-skill/scripts/draw.mjs --sector … --options 3` |
| Impeccable | `brand/tools/impeccable` (Apache) | critique, audit, polish for sites and app screens; `sh brand/tools/impeccable/scripts/impeccable context` |
| Playwright CLI | `npm i -g @playwright/cli` (Apache), skill in `brand/tools/playwright-cli/skills/` | agent browser: open pages, snapshot the DOM with element refs, click, type, screenshot at several viewports, check that everything works |
| Awesome DESIGN.md | `brand/tools/awesome-design-md/design-md/<brand>/DESIGN.md` (MIT, 84 brands) | real design systems written out: type, spacing, colour, buttons, layout. Read for structure and rigour, never to copy a brand's look |
| img2threejs | `brand/tools/img2threejs` (Apache), `SKILL.md` | rebuild an object from a reference image as a procedural, animatable Three.js model in code, for interactive 3D on websites |

## Setup notes for this workspace
- **Playwright CLI:** Chromium refuses to run as root with the sandbox on, so the config lives at `~/.playwright/cli.config.json` (a copy is in `brand/tools/playwright-cli/cli.config.json`): `chromiumSandbox: false` plus the pre-installed Chromium path. `file://` URLs are blocked, so serve pages first: `python3 -m http.server 8765 --directory <dir>`, then `playwright-cli open http://localhost:8765/page.html`. Use `--device "iphone 15"` for mobile checks.
- **img2threejs:** read `SKILL.md` and follow its staged pipeline (`forge/next.py`). Use the built-in `generic` profile only; domain plugins need Zayn's go-ahead because they change the machine. The output is a Three.js scene in code, so it pairs with our web stack (may11leven-web-stack). For realistic stills, Blender is still the tool.
- **Awesome DESIGN.md:** useful brands for our taste include apple, linear.app, vercel, stripe, notion, framer, raycast, superhuman, mercury, claude and figma. Take the discipline (token scales, spacing rhythm, component states); our colours, type and minimal style stay ours. Never copy a brand's look.

## Where they fit the workflow
- **Step 1 (skills):** Taste, Impeccable, the Playwright CLI skill, img2threejs.
- **Step 3 (research):** Awesome DESIGN.md, for how real products write their design systems.
- **Before shipping web or app work:** Playwright CLI checks at 1440, 390 and a phone emulation; Impeccable audit; webaudit.js contrast.
