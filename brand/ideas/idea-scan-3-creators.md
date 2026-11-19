---
name: idea-scan-3-creators
description: Product ideas for photographers and creators (moodboards, location scouting, shoot planning, creative direction), researched and scored, plus the weekly release rhythm for ideas. Read before planning a creator-facing product or the weekly content calendar.
---

# Ideas for photographers and creators

Research only. The founder's brief: "products that help photographers or creators come up with moodboards, scout locations, plan a shoot or creative direction. Think outside the box. If people are crazy about one, we can make it our own real product."

## What's already out there (it's crowded)
Shoot planning tools are plentiful worldwide. A 2026 roundup lists Storyflow (moodboard, shot list, schedule and call sheet on one canvas, $7.99–39 a month), Milanote ($9.99 a month), StudioBinder ($42–85 a month), PhotoPills (sun and moon planning, about $11 once), plus Notion, Miro, Canva and photography CRMs like HoneyBook and Studio Ninja (Storyflow blog; note it's Storyflow's own comparison). Most cover one or two lanes; Storyflow and Notion cover all four (moodboard, shot list, schedule, call sheet) by that comparison, which Storyflow wrote about its own market. We haven't checked Africa-focused platforms such as StreetCreator, so "nothing is built for African creators" is a hypothesis, not a finding. Either way, another general moodboard app isn't worth building; the opening, if there is one, is local.

## The local gaps we found
- **The light is short near the equator.** Our own calculation (solar geometry, no refraction): the evening window with the sun 0–6° above the horizon lasts about 24–26 minutes in Nairobi, Kigali and Lagos all year, against 36–48 minutes in Vienna and 39–55 in London. Equatorial shoots have to be planned to the minute. Global tools show the times but don't plan the shoot around them.
- **The rules are unclear and changing.** Nairobi's County Finance Act 2026 brought new filming charges. Reports don't even agree on the figures: Techweez lists KES 5,000 a day for a professional photo shoot and KES 5,000 for a music video and calls the measure proposed; Citizen Digital, the same day, lists KES 8,000 per local commercial shoot, KES 10,000 for a music video and KES 40,000 a year for content studios, and quotes the governor saying the charges target commercial productions, not ordinary content creators. The Kenya Film Classification Board has its own charges, and whether county and board fees both apply is unclear (Techweez, Citizen, Aug 2026). Codex reports the County Assembly lists the Act as assented on 31 July 2026; we couldn't open that page to confirm. The confusion itself is the problem: nobody gives creators a plain, current answer per city.
- **Contracts can be the barrier, not reach.** The Africa Creator Economy Report 2026 found that for Nigerian Instagram creators aged 25–35, the hurdle is "navigating the legal and contractual infrastructure"; we have no equivalent evidence yet for other markets. Kenya has 89,001 creators with more than 1,000 followers or subscribers, by the report's count (TechCabal on ACER 2026). A Kenyan creator interviewed in the report describes waiting up to 90 days for brand payments (per CodeRabbit's reading of the report; not yet checked by us).
- **Consent at shoots.** Model releases and consent for people in the frame are the same problem as Nod (see next-product-research.md); a creator tool can reuse Nod's consent engine.

## Four ideas
### 1. Scout: a shoot planner built for African cities
- **What it is.** Location cards for a city: the exact light window for the date (computed, short near the equator), what fees and permits apply to that kind of shoot in that city (with sources and "unclear" when it is), access and safety notes, and cost. Then brief → moodboard → shot list → call sheet, shared on WhatsApp, with model release and consent from Nod built in.
- **Who pays.** Working photographers and videographers, small production teams, brands planning shoots. Free location cards as the hook; paid planning.
- **Services:** app, website, brand, AI automation (light and permit lookups), AI agent (drafts the shoot plan), social content. Six of seven.
- **Risk:** location and permit data take work to keep current; Storyflow and others could add light planning.

### 2. Colour from a place: a reference library of African light, places and palettes
- **What it is.** Moodboards today lean on Pinterest and Western references. A curated, properly licensed library of light, textures, colours and places from African cities, each with a palette and the time it was shot.
- **Cheap test first:** it's already our proposed content series ("Colour from a place"). If people save and send those posts, that's the demand signal to build the library. If not, it stays a series.
- **Risk:** licensing every image properly; thin evidence of demand today (a hypothesis).

### 3. Brief: a creative-direction agent for brands hiring creatives
- **What it is.** A brand uploads its guidelines once; for every shoot, the agent drafts a brief, moodboard, shot list and do-and-don't list that stay on brand, and the creator gets a clear page instead of a WhatsApp voice note.
- **Why us.** It extends our brand identity service: every brand system we design can ship with its own shoot brief generator.
- **Risk:** AI drafts must be checked by a person; brands may see it as a feature of a brand guideline, not a product (which is fine for us).

### 4. Fair: a rate and usage-rights kit for African creatives
- **What it is.** A rate calculator (day rate, usage, licence period, territory) and plain-English contract and usage-rights templates reviewed by a lawyer, sent as a page the client signs.
- **Why.** The ACER 2026 finding for Nigerian Instagram creators aged 25–35: contracts and legal infrastructure are the barrier. Other markets are untested.
- **Risk:** must never be legal advice; needs a lawyer partner per country.

### Scores (same six criteria as earlier rounds, 1–5)
| Idea | Reach | Evidence | Our edge | Services | Working tool | Fresh | **Total /30** |
|---|---|---|---|---|---|---|---|
| **Scout** | 4 | 4 | 5 | 5 | 3 | 4 | **25** |
| Brief | 4 | 3 | 5 | 4 | 3 | 4 | 23 |
| Colour from a place | 3 | 2 | 5 | 4 | 4 | 5 | 23 |
| Fair | 4 | 4 | 2 | 3 | 3 | 4 | 20 |

"Our edge" for Scout and Colour from a place counts the founder's own photography and our design work; that creators would trust a tool because of it is a hypothesis (Codex review). At 3 instead of 5, Scout drops to 23, level with Brief and Colour from a place. Scout's "Fresh" is 4, not 5, until Africa-focused platforms such as StreetCreator are checked. Scores are judgement, not customer evidence; none of these has been tested with real creators yet.

### Think-outside-the-box notes
- The light window is the hook nobody uses: "Nairobi gives you 25 minutes. Plan them." That's a post, a product feature and a free tool in one.
- Scout and Nod could share a consent engine; whether building one makes the other cheaper is a hypothesis until both are specified (CodeRabbit review).
- Colour from a place can be content first and product later, which matches the weekly rhythm below.

## Reviewer suggestions not yet researched
- **Creator payment tracker** (CodeRabbit): agreed milestones, invoices and overdue brand payments, given reports of 90-day waits. Compare with Fair in creator interviews.
- **Gulf creator permits** (Codex): the UAE requires individuals promoting on social media to hold an advertiser permit; a permit-and-renewal workflow for creators could be a Gulf entry point. Not yet verified by us.

## How ideas go out: one a week
The founder's rule: never ship all ideas at once. One product idea a week; the other days market our other services.

| Day | What goes out |
|---|---|
| Product day (one a week) | The week's product idea: PXDX-structure carousel with loops |
| Two days | Sendable explainers for a service: the law or money behind it, ending in a real first-look offer |
| One day | Studio and process: how we built something, the tools, the details |
| One day | LinkedIn: a professional document or case for one service |
| Stories | Daily, quality only, pointing at the week's posts |

**Proposed order of product ideas** (each only when its post is built to the bar, never rushed): Term (already scheduled) → Nod (after the paper test, if owners respond) → Scout → Encore → Receipt → Colour from a place as a series. Ally runs as a service offer, not a product post. If one idea gets a strong response (saves, sends, DMs asking to use it), we consider building it as our own real product.

## Sources
- Storyflow, best photoshoot planning tools 2026 (vendor comparison): https://storyflow.so/blog/best-photoshoot-planning-tools-2026
- Techweez, Nairobi County Finance Act and photography (Aug 2026): https://techweez.com/2026/08/24/nairobi-county-finance-act-photography-licensing/
- Citizen Digital, Nairobi film charges clarified (Aug 2026): https://citizen.digital/article/sakaja-clarifies-film-charges-says-finance-act-does-not-target-ordinary-content-creators-n388893
- TechCabal, Africa Creator Economy Report 2026 (Feb 2026): https://techcabal.com/2026/02/05/africa-creator-economy-report/
- Light window: our own calculation from standard solar geometry (sun elevation 0–6°, no atmospheric refraction), at the equinox and both solstices.
