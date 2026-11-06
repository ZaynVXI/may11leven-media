# May11Leven Labs shared skill system

The repository now has a shared skill-discovery system for Claude Code and Agent Skills-compatible clients:

- Claude Code router: `.claude/skills/may11leven-skill-library/SKILL.md`
- Cross-agent router: `.agents/skills/may11leven-skill-library/SKILL.md`
- Full skill registry: `brand/skills/manifest.json`
- Canonical skill instructions and supporting resources: `brand/tools/`

The registry indexes **472 skills** across 17 source collections. The router selects relevant skills, loads their original `SKILL.md` files, and follows supporting references from their canonical source directories. This avoids copying thousands of support files or maintaining duplicate versions.

## Registry

[manifest.json](manifest.json) lists every skill, its stable ID, original source folder, source collection, and nearest discoverable licence file.

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

## How agents use the library

1. Invoke/read the shared skill-library router.
2. Consult the manifest and select only skills relevant to the task.
3. Read each selected canonical `SKILL.md` from its `source_file`.
4. Resolve supporting files relative to `source_dir`.
5. Check required tools and licence/provenance before use.
6. Treat skill instructions as guidance, not permission for external actions or unreviewed scripts.

Do not load all skills into every conversation. Use targeted, task-based loading.

## Canonical source and updates

- Canonical source: `brand/tools/`
- Claude Code router: `.claude/skills/may11leven-skill-library/`
- Cross-agent router: `.agents/skills/may11leven-skill-library/`
- Registry: `brand/skills/manifest.json`

Edit canonical sources only. When adding or changing a skill, update its manifest entry and keep the router guidance current. Supporting files remain in the canonical source tree.

## Provenance and licensing

There is no single licence covering this library. The manifest records the nearest `LICENSE`, `LICENCE`, `COPYING`, or `NOTICE` file found in each source tree. A nearby licence file does not automatically clear every asset, dependency, or use.

**Known restriction:** `brand/tools/claude-42/design-thinking-orbweva/LICENSE` is **CC BY-NC-SA 4.0**. It is non-commercial unless written permission is obtained, and adaptations are subject to ShareAlike. The licence file takes precedence over conflicting skill metadata. Do not use this material in May11Leven commercial deliverables without permission.

Skills with no discoverable ancestor licence file are marked `unverified`. Review embedded frontmatter, upstream provenance, and dependencies before redistribution or commercial use. Preserve upstream notices and attribution.

## Security and scope

Making a skill discoverable does not make its scripts safe. Review scripts before running them. Never place credentials in skill files. This is repository-local: it does not modify global agent folders, install packages, start MCP servers, configure credentials, or deploy anything.
