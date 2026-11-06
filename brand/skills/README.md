# May11Leven Labs shared skill system

All **472 existing skills** are exposed through two project-local agent locations:

- `.claude/skills/` — Claude Code project skills.
- `.agents/skills/` — Agent Skills-compatible project skills (including Codex-style discovery).

Each host-visible folder contains a lightweight `SKILL.md` entry point that routes the agent to the full canonical skill and supporting resources under `brand/tools/`. This avoids copying thousands of support files, keeps original sources intact, and gives both agent systems the same source of truth.

## Registry

[manifest.json](manifest.json) lists every skill, its stable install ID, original source folder, source collection, and nearest discoverable licence file.

| Source collection | Skills |
|---|---:|
| `everything-claude-code` | 314 |
| `blender-skills` | 94 |
| `claude-42` | 35 |
| `replica` | 11 |
| `ui-skills` | 4 |
| `earshot` | 2 |
| `emil-skills` | 2 |
| `gimp-reference-levybytes` | 1 |
| `hallmark` | 1 |
| `headroom` | 1 |
| `img2threejs` | 1 |
| `impeccable` | 1 |
| `playwright-cli` | 1 |
| `real-sfx` | 1 |
| `refero` | 1 |
| `taste-skill` | 1 |
| `ui-ux-pro-max` | 1 |
| **Total** | **472** |

The separate `brand/tools/everything-claude-code/AGENTS.md` file is an agent instruction document, not a skill.

## How to use the library
1. Consult the registry and select skills relevant to the task.
2. Open the matching entry under `.claude/skills/` or `.agents/skills/`.
3. Read the canonical `SKILL.md` path embedded in that entry.
4. Resolve supporting files relative to the canonical source folder.
5. Check required CLI tools, MCP servers, models, packages, and external services before relying on them.
6. Treat skill instructions as guidance, not permission for external actions or unreviewed scripts.

Do not load all 472 skills into every conversation. Use targeted, task-based loading.

## Canonical source and updates
- Canonical source: `brand/tools/`
- Claude Code entries: `.claude/skills/`
- Cross-agent entries: `.agents/skills/`
- Registry: `brand/skills/manifest.json`

Edit canonical sources only. When adding or changing a skill, update its manifest entry and both lightweight host entry points in the same reviewed change. Supporting files remain in the canonical source tree.

## Provenance and licensing
There is no single licence covering this library. The manifest records the nearest `LICENSE`, `LICENCE`, `COPYING`, or `NOTICE` file found in each source tree. A nearby licence file does not automatically clear every asset, dependency, or use.

**Known restriction:** `brand/tools/claude-42/design-thinking-orbweva/LICENSE` is **CC BY-NC-SA 4.0**. It is non-commercial unless written permission is obtained, and adaptations are subject to ShareAlike. The licence file takes precedence over conflicting skill metadata. Do not use this material in May11Leven commercial deliverables without permission.

Skills with no discoverable ancestor licence file are marked `unverified`. Review embedded frontmatter, upstream provenance, and dependencies before redistribution or commercial use. Preserve upstream notices and attribution.

## Security and scope
Making a skill discoverable does not make its scripts safe. Review scripts before running them. Never place credentials in skill files. This is repository-local: it does not modify global agent folders, install packages, start MCP servers, configure credentials, or deploy anything.
