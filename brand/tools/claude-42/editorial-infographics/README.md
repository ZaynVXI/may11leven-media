# Editorial Infographics — an agent skill against AI slop

An open Agent Skill for creating original, evidence-led infographics and social graphics.

It is designed for a common failure mode: technically polished graphics that all look the same — oversized headline, rounded cards, glowing gradient, generic icons, and no real information.

This skill makes an agent choose the **information structure before the style**, use evidence, vary the composition across a batch, and pass an explicit anti-slop quality gate.

## What it creates

- editorial infographics;
- news and data cards;
- Pinterest pins;
- social explainers and carousels;
- annotated charts;
- real product screenshots with callouts;
- process, hierarchy, overlap, and comparison diagrams.

## Install

```bash
npx skills add aosoficial/agent-infographic-skill --skill editorial-infographics -g -y
```

The format works with Codex, Claude Code, Cursor, OpenCode, and the other agents supported by the open [`skills`](https://github.com/vercel-labs/skills) CLI.

## Use

Ask your agent for something like:

> Create an evidence-led Pinterest infographic from this article. It must explain one idea in five seconds, use a composition that matches the information topology, and pass the anti-slop gate.

Or:

> Turn these five posts into five original social visuals. Use at least three layout families and do not repeat the same card-grid template.

## The system

```text
source → evidence → takeaway → information topology → art direction → render → thumbnail QA → receipt
```

The visual must do one job: **explain, prove, compare, map, or humanize**. If it only repeats the title, it fails.

## Design principles

- one dominant visual idea;
- large areas of intentional negative space;
- typography and geometry over decorative widgets;
- one functional accent color;
- real data and real UI when making factual or product claims;
- generated illustration only when the metaphor adds meaning;
- deterministic text and charts;
- platform-native layouts, never stretched masters;
- batch-level diversity, not five variants of one template.

The skill includes:

- [`SKILL.md`](SKILL.md) — the agent workflow;
- [`references/design-language.md`](references/design-language.md) — the visual grammar;
- [`references/layout-families.md`](references/layout-families.md) — structure selection;
- [`references/quality-gate.md`](references/quality-gate.md) — anti-slop QA;
- [`references/platforms.md`](references/platforms.md) — platform formats;
- [`references/publishing-gate.md`](references/publishing-gate.md) — spacing and scheduler QA;
- [`templates/visual-brief.md`](templates/visual-brief.md) — reproducible brief and receipt;
- [`examples/cfo-capacity/brief.md`](examples/cfo-capacity/brief.md) — a worked example.

## Why this exists

The useful parts of current infographic systems are their structure taxonomies, data integrity rules, and platform adaptation. The gap is that many workflows still allow style-first generation and repetitive template output. This skill adds evidence, editorial art direction, batch diversity, and a hard rejection gate.

See [research notes](references/research.md) for the sources and synthesis that informed the process.

## License

MIT. The workflow is maintained by [DÍA UNO](https://diauno.io).
