# Testing every social idea before it posts (founder-skill)

Zayn's order: install the founder skill and use it to test every project or post idea for our social media before posting.

- **Skills:** `brand/tools/founder-skill/skills/founder-*` (MIT, Jake Schincariol). Eleven skills: board, consumer, competitors, pricing, offer, CFO, marketing, brand, ops, launch, plan.
- **Per post:** run `founder-consumer --quick` (20 simulated buyers) on the idea. The customer profile is our target client (owners and marketing leads of growing businesses in East Africa first, then the Gulf and the rest; see `brand/idea-tests/customer.json`). The pitch is exactly what they'd see: cover, the first slide line, the caption's first 125 characters and the offer. Keep the results in `brand/idea-tests/<post-slug>/`.
- **Per campaign, new offer or new service:** also run `founder-board` (Offers, Monopoly and Product lenses) and `founder-offer`. Run `founder-pricing` and `founder-cfo` before announcing any price.
- **Passing a post:** the panel must name what it would do (save, share, comment 11, DM) and why. Every stop reason is either fixed in the post or accepted on purpose. Record the change in the test folder.
- **Warning from the skill's own creator:** "AI buyers are too polite." The panel is a first filter, not proof. Real proof is the post's analytics (saves, shares, profile visits, comment 11) in the weekly report; feed them back into the next customer profile.
