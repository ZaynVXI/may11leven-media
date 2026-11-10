#!/usr/bin/env bash
for c in "python3 -c 'import bpy'" "gimp-console --version" "which gmic" "ffmpeg -version" "sox --version" "tesseract --version" "python3 -c 'import faster_whisper'" "which graphify" "node -v" "gh --version"; do
  if eval "$c" >/dev/null 2>&1; then echo "OK      $c"; else echo "MISSING $c"; fi; done
