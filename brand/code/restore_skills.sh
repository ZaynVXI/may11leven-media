#!/usr/bin/env bash
# Copy vendored everyday skills into ~/.claude/skills for this session.
# Skips names the account already provides. Run from the repo root.
set -euo pipefail
dst="$HOME/.claude/skills"; mkdir -p "$dst"
skip=" frontend-design docx pdf pptx xlsx skill-creator web-artifacts-builder "
for root in brand/tools/anthropic-skills brand/tools/jakub-skills brand/tools/shadcn-skills brand/tools/claude-42; do
  for d in "$root"/*/; do
    n=$(basename "$d"); [ -f "$d/SKILL.md" ] || continue
    case "$skip" in *" $n "*) continue;; esac
    [ -e "$dst/$n" ] && continue
    cp -r "$d" "$dst/$n"
  done
done
echo "skills in $dst: $(ls "$dst" | wc -l)"
