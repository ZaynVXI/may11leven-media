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
