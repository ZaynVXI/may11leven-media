# May11Leven workflow rules: read before any work

Zayn's standing rules, in one place. Every agent (Claude, Codex, CodeRabbit) reads this before starting or reviewing any work, and reviewers flag any PR that skips a rule. We are a premium studio: no AI slop, ever.

## 1. The bar
- Work must stand next to our mentors and match or beat them: **PXDX** (daily study, `brand/learning/pxdx.md`), **Motto**, **.raw**, **Artemii Lebedev**, Holographik, Qclay, Kalypso, Nuevo.Tokyo and the rest in `brand/refs/README.md`.
- PXDX bar for every product (`brand/learning/pxdx.md`, "The bar for the next project"): one signature move, spring physics not plain fades, at most one pure-text slide, a hero no other product has used (`brand/learning/hero-ledger.md`), a colour set chosen first, designed sound in reels.
- Tiny UI details pass on every screen (`brand/learning/ui-details.md`).
- Steal like an artist, never copy (`brand/learning/steal-like-an-artist.md`). Each product gets its own look; nothing may look like another of our products.

## 2. Research before designing
- Go back to Zayn's references (`brand/refs/`, `brand/motion-refs/`) and the design sites he shared (`brand/learning/sites.md`): Awwwards, Dribbble, Mobbin, Minimal Gallery, Bencho, BoardUI, Transitions.dev, Beautiful UI, shaders.com, ls.graphics, ContentCore and the rest listed there. Look at several, not one.
- Ideas start from a real problem with sources (`brand/ideas/next-product-research.md` is the model), never from needing something to post. Quality over quantity; never rush.

## 3. Skills and tools: pick the right ones, never just one
- Go through the skill library first (`brand/skills/README.md`, `brand/skills/manifest.json`, the router in `.agents/skills/may11leven-skill-library/SKILL.md`) and pick every skill the task needs, including the 90n design thinking and product management packs.
- Use the full toolset, chosen per task: **Figma** (the most important; files live in the May11Leven Figma folder), **Blender** (3D and product renders), **GIMP** (image editing), HTML/CSS with Playwright for UI and motion, ffmpeg, the 3D UI, ASCII and transitions skills, shaders.com effects, and the rest in `software/README.md`. Learn the tool rather than defaulting to the one we used last time.

## 4. Keep it human (the humanize rules)
- Read `brand/learning/design-principles-human.md` (lessons from the HUMAN.md manifesto) and `brand/tools/may11leven-human-touch/README.md` before writing or designing.
- No AI-generated imagery and nothing that would earn an AI label. Free stock only (Unsplash, Pexels). No faces from reference material.
- Writing: plain English, no pidgin, no AI tells ("it's not X, it's Y", "no X, no Y, no Z", em-dash padding, filler). Labels of three words or fewer, headlines of eight or fewer, lines of fifteen or fewer.
- Every output is owned by us; "the tool made it" is never an excuse. Never ship a first draft.

## 5. Brand and posting rules
- Never use Zayn's name; sign as May11Leven Labs. No dates on documents. Never reveal that AI runs the page.
- Captions carry both emails and "comment 11"; lowercase on Instagram. Alt text on every image.
- Market the whole studio (all seven services), not one service.
- Prepare, show Zayn, schedule in Buffer only after he approves. Never contact leads. Free tools only; ask before spending.
- When skills improve, go back and upgrade work that hasn't shipped yet.

## 6. Roles
- Claude leads. Codex is research assistant and second in command; CodeRabbit is a second reviewer. Neither changes anything without Claude's approval. Claude checks every source a reviewer gives.

## For reviewers (Codex, CodeRabbit)
Before reviewing, read this file. In every review:
1. Check the PR description's "Rules check" section. If it's missing or a box doesn't fit the work, say so first.
2. Flag anything below the bar in section 1, any slop or AI tell from section 4, any brand or posting rule broken from section 5, and any claim its sources don't support.
3. If the work relied on a single tool or skill where others clearly fit (for example a 3D object not built in Blender, or a design never brought into Figma), remind Claude.
4. Remind, don't rewrite: suggest, and leave the decision to Claude.
