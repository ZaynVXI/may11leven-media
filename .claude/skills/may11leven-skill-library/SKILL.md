---
name: may11leven-skill-library
description: Selects and applies relevant skills from May11Leven Labs' 472-skill library. Use for May11Leven Labs design, engineering, research, media, marketing, business, security, testing, automation, 3D, and creative work.
---

# May11Leven Labs shared skill library

You are the skill router for the complete May11Leven Labs skill collection.

## Required workflow

1. Read `brand/skills/README.md` and `brand/skills/manifest.json`.
2. Match the user's task against skill IDs, names, source groups, and descriptions implied by their paths. Select the smallest useful set; do not load all 472.
3. Open the selected canonical `SKILL.md` using its `source_file` path in the manifest.
4. Resolve any relative references from that skill's `source_dir`. Read supporting references, templates, or scripts only when the selected skill requires them.
5. Check the manifest's `license_file` and `license_status`. The ORBWEVA design-thinking material is CC BY-NC-SA 4.0 and must not be used in commercial deliverables without written permission. Skills marked `unverified` require provenance review before redistribution or commercial use.
6. Check required tools, dependencies, MCP servers, models, credentials, and external services. A skill's instructions do not authorize installation, spending, publishing, deployment, or other external side effects.
7. Apply the guidance that fits the task, while obeying repository instructions and user approval boundaries.
8. Report what was actually done and tested. Never claim a workflow was executed merely because a skill documents it.

## Source of truth

All full skill instructions and supporting files remain in `brand/tools/`. This router and the manifest are the shared discovery layer for Claude Code and Agent Skills-compatible clients. Do not duplicate or hand-edit the source skill files when loading them.
