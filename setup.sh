#!/usr/bin/env bash
# Rebuild the May11Leven workspace tools after a fresh container (idempotent).
set -eo pipefail
pip install -q --break-system-packages bpy faster-whisper pyspellchecker soxr pyloudnorm soundfile graphifyy 2>&1 | tail -1
apt-get install -y -q ffmpeg sox tesseract-ocr >/dev/null 2>&1 || true
command -v gimp-console >/dev/null || (apt-get update -q >/dev/null; apt-get install -y -q gimp gimp-plugin-registry gmic gimp-gmic >/dev/null 2>&1 || true)
# restore our installed skills
mkdir -p ~/.claude/skills
for d in brand/tools/claude-42/*/; do [ -f "$d/SKILL.md" ] && cp -r "$d" ~/.claude/skills/; done
for d in brand/tools/founder-skill/skills/*/ brand/tools/juliobsz-skills/awwwards brand/tools/juliobsz-skills/jury brand/tools/impeccable; do [ -d "$d" ] && cp -r "$d" ~/.claude/skills/; done
[ -d brand/tools/taste-skill ] && cp -r brand/tools/taste-skill/* ~/.claude/skills/ 2>/dev/null || true
echo "setup done"
bash software/check.sh
