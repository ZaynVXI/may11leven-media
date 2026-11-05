# The 42 add-ons (from Charlie Hills' carousel) and where each stands for May11Leven

These are our install notes and how to use each one. To restore the skills in a new session, copy every folder here into `~/.claude/skills/`, then run `pip install graphifyy --break-system-packages` and `graphify install --platform claude`.

## Installed and tested
| # | Add-on | Status | How we use it |
|---|---|---|---|
| 01 | Superpowers (obra, MIT) | 9 skills installed: brainstorming, writing-plans, executing-plans, systematic-debugging, verification-before-completion, test-driven-development, requesting-code-review, dispatching-parallel-agents, writing-skills | Brainstorm before any new site or app build. Write a plan for multi-step builds. Debug systematically instead of guessing. Verify with real output before saying "done". |
| 03 | graphify (Apache) | `graphify` CLI plus skill | `graphify update brand/code` maps our scripts (224 parts, 441 links). `graphify explain "gimp.py"` or `graphify path "A" "B"` shows what connects to what. Use it before changing shared code and for client codebases. Code mapping is free and local; docs and images use the model. |
| 15 | Remotion (skills, plus npm) | 13 skills installed, plus a starter in `brand/code/remotion-starter/` | React to video. Render with `npx remotion render src/index.ts <Comp> out.mp4 --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell` (tested at 1080x1350). Good for data, UI and type animation. Licence: free for individuals and small companies (check remotion.pro/license as we grow). |
| 22 | last30days (MIT) | skill installed | Its method: what people said in the last 30 days on Reddit, HN, X and YouTube, ranked by engagement. This workspace can't reach those sites from the shell, so run its queries through WebSearch (extended), or run it on Zayn's computer. |
| 24 | humanizer (blader) | already installed, plus **slopbeth**, **slopgent** (ehmo/slopkit, MIT), **stop-slop** (MIT) | See the anti-slop gate below. |
| 40 | find-skills (vercel-labs) | installed | Search skills.sh for a skill before building a method by hand. |
| 10–13 | ui-ux-pro-max, impeccable, taste-skill, emil-design-eng | already in `brand/tools/` | Design references and anti-slop passes for UI. |
| 14 | HyperFrames | already installed | HTML to video for reels. |
| 06, 16, 29, 32, 33, 41 | Playwright, ffmpeg, Puppeteer, Whisper, Python, Node | already in the workspace (Playwright replaces Puppeteer; faster-whisper replaces Whisper) | Rendering, video, transcripts and data. |
| 04 | GitHub CLI | `gh` installed and in use | Media repo, skill research. |
| 09, 19, 25, 30, 34, 35 | Figma, Claude in Chrome, Metricool, Google Drive, Notion, Gmail | connected | Already in our workflow. |
| — | **Anti-slop design check** (Gesso, MIT) | skill installed | `npx -y @gessobuild/anti-slop check <html files>` then `fix <file> --write`. 73 checks for UI that reads as generated. |

## Not installed, and why
| # | Add-on | Why not (yet) |
|---|---|---|
| 26, 27, 17 | GPT Image, Nano Banana, Higgsfield | AI image and video generation. Our posts must never carry the AI label. Blender, free stock and HTML instead. |
| 28 | ElevenLabs | AI voice, paid plan, account needed. Our sound rule is real recordings. If we ever need a voiceover, a real voice first. |
| 18, 20, 21 | Perplexity, Firecrawl, Apify | Need accounts and API keys (Firecrawl and Apify have free tiers). Zayn signs up if he wants them; we already have WebSearch and WebFetch. |
| 02 | gstack (MIT) | A full dev setup (needs Bun and its own browser binary). Cloned for reference: its `design-review`, `qa` and `plan-design-review` checklists are worth reading for web and app builds. |
| 05 | Vercel | Free account needed (Zayn) to put client sites live. Recommended once we ship our own site. |
| 07 | Codex | OpenAI account. A separate agent reviewer covers second opinions. |
| 08 | Claude HUD | A terminal status bar; our sessions run in the app, so it shows nothing. |
| 31, 36, 37, 38 | Granola, Google Calendar, Slack, Zapier | Connectors on Zayn's account. Connect them only when there's a real use (Calendar for client calls is the likely first). |
| 39 | caveman (Apache) | Cuts replies short to save tokens. Our messages to Zayn must stay clear, full plain English, so it stays off. |
| 42 | Ollama | Runs local models on a Mac. It belongs on Zayn's own computer, not this workspace. |

## The anti-slop gate (runs in every job, before preflight)
1. **Writing** (captions, slides, emails, case studies, site copy): draft, then run `python3 slopbeth/scripts/deslop_lint.py caption.txt --format json` and fix every hit. Then read it once against `stop-slop/SKILL.md` and the humanizer rules. Check that no meaning changed with `slopbeth/scripts/preservation_check.py original.txt rewrite.txt`.
2. **Design** (every HTML page, UI screen, slide or story built in HTML): `npx -y @gessobuild/anti-slop check <file>`, `fix --write` for safe fixes, and hand-fix the rest. Render again and check at 100% (the auto-fix can remove borders that were doing work).
3. **Image**: no AI imagery; GIMP edits stay subtle (`brand/tools/gimp/README.md`).
4. **What we report to Zayn**: slopgent rules. Say what actually ran and what was verified, lead with the result, no "should work now".
5. Never use tools built to fool AI detectors (token perturbation and similar). The goal is better work, not hiding.

## Infographics (Zayn asked for a lean infographic skill)
- **Installed: editorial-infographics** (aosoficial/agent-infographic-skill, MIT). Every graphic does one job (explain, prove, compare, map or humanize), with one takeaway readable in 5 seconds, real evidence only (each claim marked verified, inference or unknown) and structure chosen before style. Build in HTML or SVG in our type and colours, then run the anti-slop gate and preflight.
- Skipped: AAAAAAAJ high-density infographics (dense, the opposite of lean) and Mnilax JSON-to-SVG (needs Bun; its idea of a JSON spec with palette, type and layout presets is worth copying for repeatable series).

## From charliehills.ai/free-resources
- **Installed: security-audit** (cloudflare/security-audit-skill, MIT). A six-phase audit of an app's code by isolated agents: recon and a coverage ledger, hunting, a fresh verifier trying to disprove every finding, then a report sorted into confirmed, needs-validation and rejected. Run it on every website, app and AI agent we build before handover. It takes about an hour on a small app. Test a lead only with the owner's yes. It doesn't replace a professional for apps that handle payments or personal data. It's a strong selling point for us ("security-checked builds").
- **Installed: prompt-master** (nidhinjs, MIT). Turns a rough sentence into a finished prompt for a named tool, asking at most 3 questions, and leaves placeholders instead of inventing stats. Use it when writing briefs for Blender or HyperFrames scenes, agent system prompts for client AI agents, and research prompts.
- **Charlie's own 104 skills** (charliehills.ai/skills) are free zips, but download only after signing up for his newsletter. We don't create accounts, so Zayn downloads them and attaches the zips. The ones worth having for us: remove-ai-design-slop, graphic-designer, video-check, brand-setup (install first), opening-hook, call-to-action, every-format, product-demo, apple-style, motion-effects with brand-intake, answer-first, push-check, exposure-audit. Install with `unzip -o <slug>.zip -d ~/.claude/skills/`.
- **Guides worth reading** (the full text needs the same sign-up): Make Claude your Graphic Designer (one folder holding house rules, brand, 5 liked graphics and 2 design skills, with winners fed back in; we already work this way through `brand/refs`), Block AI training on your website (2 robots.txt lines, for our site and client sites), Forever Components (791 animated web components; copying needs a free account at 3 a day and the licence isn't stated, so treat them as reference, never shipped code, until it's clear).

## Impeccable and Taste (installed live, newest versions)
- **impeccable** 4.8 (pbakaus, Apache-2.0): design, critique, audit, polish and animate any frontend. Run the detector with `~/.claude/skills/impeccable/scripts/impeccable detect <html files>` (telemetry turned off). Its verbs are shape, audit, critique, polish, distill, quieter, typeset, layout, harden and adapt. The first run on our services carousel caught two real contrast fails (the spam tag at 4.0:1, the chat placeholder at 3.7:1); both are fixed.
- **taste-skill** 2.5 (Leonxlnx, MIT; the skill is named design-taste-frontend): the anti-slop frontend skill for company sites. Plain copy, one system, one section per screen, real photos and real product UI, quiet micro-interactions, and a browser checker in its scripts/. Use it on every website build.
- Our reference copies in brand/tools/impeccable and brand/tools/taste-skill are updated to the same versions.
- Note: Impeccable flags our Bone #ECEAE4 base as the "default cream" AI surface. Bone is a deliberate studio colour (measured from .raw's bone and greige), so it stays. Keep checking that each post's world isn't Bone by reflex.

## SkillOpt (microsoft/SkillOpt, MIT; NeurIPS 2026 spotlight)
- **What it is:** it trains a skill file like a model. It scores real runs, proposes small add, delete or replace edits, and keeps an edit only if it beats a held-out score. Its **SkillOpt-Sleep** mode reads past Claude Code sessions (read only), mines the recurring tasks, replays them and stages a better SKILL.md or CLAUDE.md. Nothing changes until you `adopt` it, and the live files are backed up first.
- **Installed:** `pip install -e` from the repo, plus the `skillopt-sleep` skill. Run it with `SKILLOPT_SLEEP_REPO=<repo> bash plugins/claude-code/scripts/sleep.sh dry-run|run|adopt --project <dir> --backend mock`.
- **Tested:** a mock dry run (no model calls, no cost) worked end to end: harvest, then mine, then the gate. This workspace has only 1 session to learn from, so the gate correctly made no change.
- **Making it useful:** run it where our history builds up (Zayn's computer, or a long-lived session) with `--backend claude`. That uses plan usage on every replay, so run it weekly and keep `--edit-budget` small. Point `--target-skill-path` at one of our skills (e.g. may11leven-preflight) and pass our house rules with `--preferences`. Always review the baseline-to-candidate score and the diff before adopting. Never adopt edits that weaken our rules.
