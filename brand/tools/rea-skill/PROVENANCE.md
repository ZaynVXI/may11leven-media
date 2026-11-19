# REA (Reverse Engineer Anything)

- Source: https://github.com/morluto/rea (MIT). Skill copied from .agents/skills/reverse-engineer-anything; CLI is the npm package rea-agents, pinned to 6.9.0 (no install scripts).
- Restore: copy reverse-engineer-anything/ into ~/.claude/skills/, then `npm install -g rea-agents@6.9.0 --ignore-scripts`.
- Our use: study how great websites build their interactions (for example `rea analyze-web-bundle` or `capture-browser-scenario` on a studio's public site), then build our own version. Learning only: never copy code or assets, never analyse anything behind a login, never break a site's terms, and never install paid engines without Zayn.
