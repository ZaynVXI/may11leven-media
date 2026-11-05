# Sound tools and Everything Claude Code (from the two reels Zayn sent)

## Sound: real recordings, placed on the frame
The lesson from both sound tools: **a premium film never uses code-synthesized sound.** Every cue is a real recording (or a CC0 UI cue), placed on the exact frame the picture moves, at a measured level, with one licensed music bed. Our earlier reels used a numpy-synthesized bed and blips; from now on we use real sounds.

| Tool | Where | Use |
|---|---|---|
| Openverse API | https://api.openverse.org/v1/ (free, no key) | 5M+ audio files. Search `/v1/audio/?q=...&license=cc0,by&category=sound_effect|music`. The workspace can't reach it directly, so send searches and downloads through the GitHub fetch bridge (`fetch/urls.txt`). Keep only CC0 or CC BY (credit BY in the caption or alt text). No NC, no ND, no SA. |
| real-sfx (Clipwing, MIT; sounds CC0) | `brand/tools/real-sfx` | Finds every moment in a motion video that needs a sound and places it on the frame (`find_moments.py`, `from_cues.py`, `mix.py`, `critique.py`, `levels.py`). Ships 78 CC0 UI cues (send, receive, press, success, purchase…) in `vendor/node_modules/uisfx`. Keeps music and voice and outputs a separate WAV. |
| earshot (MIT) | `brand/tools/earshot`, `pip install -e` (CLI `earshot`) | "Ears for agents": timeline, sheet (annotated spectrogram), critique against professional launch films, realness check, loudness. The `real-sound` skill inside is the full soundtrack process. The AI tagging commands need torch, which can't be installed here (pytorch.org is blocked), so we use the measurement commands. |

### Our sound rules (from these tools)
1. **Cue list from the picture:** every sound sits on a frame we compute from the timeline (message lands, tap, payment, reveal).
2. **One real music bed** (CC0 or CC BY, instrumental), with a drop or swell on the hero moment and a tail into silence.
3. **UI moments** get uisfx CC0 cues or real recorded foley (a real phone tap, real paper). **Everything else** gets real recordings.
4. **Never double:** no synth under the real sounds.
5. **Measure, don't guess:** about -14 LUFS for Instagram, true peak at or below -1.5 dBTP. Check the mix with `earshot timeline` or `sheet`, and real-sfx's `critique.py` and `levels.py`.
6. **Credit** CC BY sounds and music in the caption or alt text. CC0 needs no credit, but keep it in `audio/CREDITS.md`.

## Everything Claude Code (ECC, MIT)
Vendored to `brand/tools/everything-claude-code` (skills, agents, commands; 314 skills). We did **not** run its installer, because it rewires the harness (hooks, settings). We use its skills as references when a job needs them:
- **Design and UI:** frontend-design-direction, design-system, frontend-a11y, accessibility, liquid-glass-design (to know the trend, not to use it), ui-demo, frontend-slides, loop-design-check
- **Motion and video:** motion-foundations, motion-patterns, motion-advanced, video-editing, remotion-video-creation, manim-video, tasteforge-video, blender-motion-state-inspection
- **Brand and marketing:** brand-discovery, brand-voice, content-engine, marketing-campaign, market-research, seo, social-publisher
- **Engineering for client builds:** api-design, frontend-patterns, dashboard-builder, swiftui-patterns, nuxt4-patterns

Read the matching `skills/<name>/SKILL.md` in step 1 of the workflow, take what fits our minimal style, and ignore the rest.
