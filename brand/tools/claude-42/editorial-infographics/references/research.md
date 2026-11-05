# Research notes

Research question:

> What combination of information structure, evidence, art direction, and QA produces social infographics that feel human-designed and remain useful when created by an agent?

## Sources reviewed

- [Vercel Labs skills CLI](https://github.com/vercel-labs/skills) for the public Agent Skill format and install flow.
- [GitHub repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) for discoverability.
- [Baoyu Infographic](https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-infographic) for layout/style separation, source preservation, and prompt receipts.
- [AntV chart visualization skills](https://github.com/antvis/chart-visualization-skills) for deterministic, topology-led infographic structures.
- [Visual Storytelling Design](https://github.com/lyndonkl/claude/tree/main/skills/visual-storytelling-design) for context → problem → evidence → insight, annotations, and honest framing.
- Practitioner discussions about generic AI infographics and cookie-cutter visual systems on [r/SaaS](https://www.reddit.com/r/SaaS/comments/1r75ecf/has_anyone_found_an_ai_infographic_tool_that/) and [r/graphic_design](https://www.reddit.com/r/graphic_design/comments/1ugxd13/is_anyone_else_getting_exhausted_by_the/).

## Synthesis

Strong existing systems already know how to classify information, preserve source facts, and select an aspect ratio. Their common gap is allowing the generator to invent both the visual language and the information presentation at once. That produces plausible but repetitive output.

The process here adds four controls:

1. a mandatory visual job;
2. evidence before art direction;
3. a batch-level diversity rule;
4. a rejection gate that penalizes generic AI motifs and title-only graphics.

Reddit was used as qualitative signal, not as proof of performance. No source supports a guarantee of virality. The defensible goal is clearer comprehension, stronger credibility, and more reasons to save or share the piece.

