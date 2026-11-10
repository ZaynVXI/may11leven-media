# Agent handoff board (Claude <-> ChatGPT)

Both agents read this file at the start of work (see AGENTS.md) and update it at the end. Zayn owns all decisions; neither agent publishes, posts, spends money or contacts anyone without his approval. Work on branches, open pull requests, never push to main.

## Rule from Zayn
Never wait on the other agent. If a task is not picked up or ChatGPT is unavailable, Claude does it directly and notes it here.

## How to use
- Add a task under **Open** with: who it is for, what "done" means, and the files involved.
- When you pick it up, move it to **In progress** with your name and branch.
- When finished, move it to **Done** with the PR link and what you checked.
- Ask the other agent for a review in the PR description or with a PR comment.

## Open
- [x] **For ChatGPT: review PR #2 (branch `feat/skills-luxury-founder-nng`).** Check the manifest update (485 skills, 13 added under `founder-skill` and `juliobsz-skills`), licence notes (design-thinking is CC BY-NC-SA, so non-commercial), and that `setup.sh` and `software/check.sh` are safe to run. Report problems as PR comments; don't merge.
- [ ] **For ChatGPT: keep the skill router current.** When new skill folders appear under `brand/tools/`, regenerate `brand/skills/manifest.json` and the counts in README, CLAUDE.md, AGENTS.md and both routers. A script for this (`brand/skills/build_manifest.py`) would help.
- [ ] **For ChatGPT: second opinion on the merch v1 renders** (`merch/v1/`): compare against `brand/refs/motto/maisa/` and list the three biggest realism gaps.

## In progress
- Claude: merch range and Instagram presentation in the new Motto style (Figma studio file, Merch page).

## Done
- Codex reviewed PR #2: one P2 finding (check.sh always exited 0). Fixed by Claude: check.sh now exits 1 on any missing tool; setup.sh uses pipefail.
- Claude: Figma studio file (tokens, project palettes, devices, merch range), software list and setup script, colour-per-project rule (PR #2).
