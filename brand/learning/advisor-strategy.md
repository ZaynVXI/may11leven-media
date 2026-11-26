---
name: advisor-strategy
description: How May11Leven splits work between Opus, Sonnet and Haiku (Anthropic's advisor strategy), so usage lasts longer without lowering quality. Read before any long job, scheduled task or agent build.
---

# The advisor strategy (Opus thinks, Sonnet builds, Haiku runs errands)

Source: Anthropic, "The advisor strategy: Give agents an intelligence boost" (claude.com/blog/the-advisor-strategy), plus a creator reel Zayn sent explaining it for Claude Code. No frames from the reel are saved (it shows a face).

## What Anthropic says
- **The pairing:** Opus is the advisor. Sonnet or Haiku is the executor and runs the whole task: it calls the tools, reads the results and works towards the answer.
- **When Opus steps in:** when the executor hits a decision it can't solve, it asks Opus. Opus reads the shared context and sends back a plan, a correction or a stop, and the executor carries on.
- **Results quoted (their evals):**
  - Sonnet with an Opus advisor: +2.7 points on SWE-bench Multilingual, about 12% cheaper per task than Sonnet alone.
  - Haiku with an Opus advisor: 41.2% on BrowseComp, against 19.7% for Haiku alone.
- **API:** the advisor tool is a server-side tool (beta header `advisor-tool-2026-03-01`). Anthropic's advice is to test on our own work: Sonnet alone, Sonnet with an Opus advisor, and Opus alone.

## The three roles in our studio
| Role | Model | Our jobs |
|---|---|---|
| **Advisor** | Opus | Brief and idea, moodboard and steal list, art direction, judgement calls, the final preflight and critique, anything sent to Zayn or a client |
| **Main builder** | Sonnet | HTML screens, Figma assembly, Blender scripts, reel assembly, caption drafts, repo edits, research write-ups |
| **Sub-agents** | Haiku | Web searches and link checks, frame sheets and transcripts, file sweeps, manifest and licence checks, data pulls (Metricool, Buffer reads), restoring skills |

## Rules
1. **Opus decides; Sonnet and Haiku do.** Opus writes the plan with clear acceptance checks. The builders don't change the idea.
2. **Escalate at decision points, not on every step:**
   - before the first pixel
   - when a check fails twice
   - when something can't be undone (publishing, deleting, spending)
   - before anything ships
3. **Taste stays with Opus.** The final look at 100%, the Motto comparison and the go or no-go are never handed off.
4. **Give Haiku narrow jobs** with one clear output (a list, a file, yes or no) and no design choices.
5. **Measure it.** If a task gets worse with this split, move that task back to Opus and log it in `brand/practice/log.md`.

## How to switch it on, by surface
- **Claude Code (terminal), as shown in the reel:**
  - Run the session on Sonnet as the main model, then type `/advisor opus`. Claude Code then consults Opus when it needs to.
  - Not tested here: this workspace isn't Claude Code in a terminal.
- **This Claude app session:** the main model stays as chosen. Use the Agent tool with `model: "haiku"` for errands and `model: "sonnet"` for builds. Opus keeps planning and review.
- **Scheduled tasks:** a task's model can be set to Sonnet, with Opus used through a sub-agent for the judgement steps. Change a task's model only after Zayn says yes.
- **Client agents we build (AI agents service):** Sonnet or Haiku as the executor, plus the advisor tool with Opus. This is a selling point: near-Opus quality at a lower running cost. Show the eval comparison in the proposal.
