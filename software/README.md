# May11Leven software list

Everything the studio uses, in one place. After a fresh workspace, run `bash setup.sh` from the repo root (it reads this list) and check with `bash software/check.sh`.

## Installed in the workspace (free)
| Tool | What we use it for | How to install | Check |
|---|---|---|---|
| Blender (bpy 5.3) | All 3D: products, packaging, merch, devices, scenes | `pip install --break-system-packages bpy` (~400 MB, a few minutes) | `python3 -c "import bpy"` |
| GIMP 2.10 + gimp-plugin-registry | Photo finishing, retouch (`brand/tools/gimp/gimp.py`) | `apt-get install -y gimp gimp-plugin-registry` | `gimp-console --version` |
| G'MIC | Filters, speck clean-up | `apt-get install -y gmic gimp-gmic` | `which gmic` |
| ffmpeg | Video cuts, frame sheets, encoding | `apt-get install -y ffmpeg` | `ffmpeg -version` |
| SoX + pyloudnorm + soxr + soundfile | Sound mix, -14 LUFS loudness | `apt-get install -y sox`; `pip install pyloudnorm soxr soundfile` | `sox --version` |
| faster-whisper | Transcribing videos (model download needs HF access or the GitHub bridge) | `pip install faster-whisper` | `python3 -c "import faster_whisper"` |
| Tesseract OCR + pyspellchecker | Preflight text and spelling check | `apt-get install -y tesseract-ocr`; `pip install pyspellchecker` | `tesseract --version` |
| Playwright + Chromium | Rendering HTML to images and video, browser QA | Pre-installed (do not reinstall) | `node -e "require('playwright')"` |
| graphify | Code maps | `pip install graphifyy` | `which graphify` |
| Node 22 + npx | Remotion, HyperFrames, awwwards/jury scripts, skills CLI | Pre-installed | `node -v` |
| Remotion | React to video | `npm i remotion @remotion/cli react react-dom` in `brand/code/remotion-starter` | render test |
| GitHub CLI (gh) | Repo, PRs (REST via `gh api`) | Pre-installed | `gh --version` |
| Fonts | Inter Tight, Instrument Serif, Plex Mono, Hanken Grotesk, Archivo | In `brand/fonts/` | — |

## Connected apps (through Claude)
| App | Use | Account |
|---|---|---|
| Figma (Education plan) | Design system, mockups, merch boards, handover | yusufzaynali@my.uopeople.edu, "yusufzaynali's team". Apple iOS 26 kit licence accepted |
| Metricool | Scheduling, analytics | blog 7782767 |
| Gmail | Drafts and urgent alerts only | studio account |
| Google Drive, Notion | Documents | — |
| Adobe for creativity | Photoshop-grade edits (ask before paid credits) | — |
| Canva | Exports only, never AI images | — |
| Mobbin | App screen references (free browsing) | — |
| Lovable, Framer, Webflow | Site builds when chosen for a project | — |

## Not used (and why)
- Photoshop: paid. GIMP and the Adobe connector cover it.
- AI image, video and voice generators (GPT Image, Nano Banana, Higgsfield, Kling, ElevenLabs): would get our posts the AI label.

## Installed or reviewed 24 Nov (all inspected before install; licences checked)
| Tool | Status | Why |
|---|---|---|
| CLI-Anything (HKUDS, Apache-2.0) | Installed: GIMP, LibreOffice, Inkscape, Audacity and Blender harnesses (`cli-anything-gimp` etc.); skills vendored in `brand/tools/cli-anything/` | Agent-usable commands for our desktop tools. The Blender harness needs the Blender app; our pipeline uses `bpy`, so keep using that. |
| agent-skills (Addy Osmani, MIT) | Vendored in `brand/tools/agent-skills/` (skills only, no hooks) | 24 engineering skills: spec, plan, TDD, security, accessibility, shipping. The accessibility audit uses pinned `@axe-core/cli` and `pa11y` through npx. |
| Kokoro TTS (kokoro-onnx, Apache-2.0 model) | Installed; model in `~/.cache/kokoro/` | Voiceovers from built-in voices (bf_emma, bm_george). No cloning, no consent issue. |
| Voicebox (MIT), VoiceStudio (AGPL-3.0) | Not installed here | Desktop apps for voice cloning. Run on Zayn's computer when linked. Clone only Zayn's own voice, or someone who gave clear written consent. AGPL: don't ship it inside client products. |
| Open Generative AI (MIT) | Not installed | AI image and video front end, sold as "no content filters", built on a paid API (MuAPI). Conflicts with our no-AI-imagery rule. |
| Lummi, Luma | Not installed | AI-generated images and video. Ideas only. |
| Seed skill (investor "closer") | Not installed | It emails investors and follows up on its own, which breaks "never contact anyone without approval". We're not raising money. |
| OmniRoute (300 free AI providers) | Not installed | It sends our work and data to unknown providers to get around usage limits. That's a security risk and may break providers' terms. |
| Ponytail, graphify | Already installed | Token savings come from these plus scheduling ahead. |
