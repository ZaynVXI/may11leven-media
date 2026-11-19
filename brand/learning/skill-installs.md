---
name: skill-installs
description: How we vet and install outside skills and tools, and what was installed or declined and why. Read before installing anything new.
---

# Installing outside skills and tools

**Protocol:** clone into a scratch folder, read the README, licence and every script; then run NVIDIA SkillSpector (`skillspector scan <dir> --no-llm -f json -o report.json`) and read the HIGH and CRITICAL findings yourself (most are test fixtures). Install the skill files only; skip lifecycle hooks, webhooks and auto-updaters unless needed. Public repo rule: vendor only what the licence lets us redistribute.

## Installed
- **NVIDIA SkillSpector** (Apache-2.0), `uv tool install --python 3.13 git+https://github.com/NVIDIA/skillspector.git`. The scanner for every future install.
- **Ponytail** (MIT): the core skill (shorter code, tests on risky logic), vendored in brand/tools/ponytail. Hooks and webhook not installed.
- **Lemo-Opuscar** (code MIT, docs CC BY-NC 4.0 with a permission to use them for our own and client films): 99 code-made film styles. Installed locally only, not vendored (its docs may not be redistributed in our public repo). On first use it downloads its library to ~/lemo-opuscar; point its renderer at the pre-installed Chromium instead of installing another. Never use its TTS narration or any AI voice in our posts; our films stay silent or use licensed sound.
- Earlier tonight: stageshow, UI UX Pro Max, Taste Skill, Floorplan, 90n design thinking and PM packs.

## Declined (and why)
- **FreeLLMAPI**: a server that stacks free tiers from 87 AI providers. Using it needs accounts and API keys at each provider (we never create accounts), a server on Zayn's machine, and it routes our prompts through many third parties. We already work in Claude, so it adds risk and no quality.
- **Agent Reach**: makes agents read X, Reddit, YouTube and Xiaohongshu by using the owner's login cookies, scrapers and proxies. That means handing over session cookies and getting around platform limits, which breaks our rules (never type or store credentials, never bypass bot checks) and the platforms' terms. For studying PXDX on Instagram we use the built-in browser on Zayn's computer, signed in by him, read-only.
