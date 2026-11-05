# Free fonts: where to find them, and how we check them

Our rule is free fonts only, picked for taste and accessibility at the same time. Always read a font's licence on its own page before using it for client work.

## Libraries (free for commercial use unless noted)
| Library | What it's good for | Licence |
|---|---|---|
| Google Fonts / Fontsource (npm `@fontsource/<name>`) | the biggest open catalogue, easy to install here through npm | OFL / Apache |
| Fontshare (Indian Type Foundry) | premium-feeling grotesks and serifs (Satoshi, General Sans, Clash, Switzer, Erode, Gambetta) | ITF Free Font Licence: free for personal and commercial use; don't resell or redistribute the files |
| Velvetyne | experimental display faces, libre culture | OFL |
| Collletttivo | Italian collective, refined display and text faces | OFL / open; check each font |
| Open Foundry | curated open-source fonts with type specimens | open; check each font |
| Uncut.wtf | curated free fonts, contemporary grotesks | varies; check each font |
| The League of Moveable Type | classic open faces | OFL |
| Free Faces Gallery | curated free fonts with clear licence notes | varies |
| Use & Modify (Raphaël Bastide) | handpicked libre fonts | OFL / libre |
| Noto (Google) | every script: Ge'ez, Arabic, Tifinagh, N'Ko, Vai, Adlam | OFL |
| Braille Institute | Atkinson Hyperlegible (Next, Mono) for low-vision readers | OFL |

Not free for commercial use: Pangram Pangram (free for personal use only), most "free trial" fonts from foundries, and anything on dafont-style sites without a clear licence. PP Neue Montreal (Motto) is paid.

## Accessibility rules for type
1. **Can people tell I, l and 1 apart?** This matters for us more than most: our name is "May11Leven" and our emails are "may11leven.labs" and "hello@may11levenlabs.com". In a font where l and 1 look alike, people misread the email.
   - Emails, codes, prices and phone numbers must use a face where l and 1 are clearly different: Atkinson Hyperlegible Next, Hanken Grotesk, Public Sans, Geist, Schibsted Grotesk, or IBM Plex Mono for labels.
   - Never set our emails in Instrument Serif or Cormorant: their l and 1 look alike.
   - On the web, Inter (and Inter Tight) can switch features on: `font-feature-settings: "cv05", "cv08"` gives a tailed l and a serifed I.
2. **Large x-height, open shapes.** Aim for an x-height of about 0.5 of the em or more for body text. Light weights only at display sizes.
3. **Sizes and contrast:** follow accessibility.md (4.5:1 for body text, 3:1 at 48 px and up; at least 20 px on posts, 24 px on reels, 16 px for web body).
4. **Language: English by default.** Zayn: we design in English, and only use an African language when a job truly needs it (a client's name or place with special letters, a bilingual Arabic brand for the Gulf). When that happens, check the font covers it:
   **The languages our clients may write in.** Many target markets write Latin letters that common fonts lack:
   - Yoruba (ẹ ọ ṣ plus tone marks) and Igbo (ị ọ ụ ṅ) for Nigeria
   - Hausa (ɓ ɗ ƙ ƴ) for Nigeria, Niger and Ghana
   - Akan, Ewe, Lingala and Wolof (ɛ ɔ ŋ ɖ ʋ ɣ) for Ghana, DRC and Senegal
   - Amharic (Ge'ez script) for Ethiopia
   - Arabic for North Africa and the Gulf
   - Naira ₦ and Cedi ₵ signs

   Missing glyphs show up as empty boxes ("tofu"), which breaks the brand and excludes readers. Run the lab only when a job actually includes these letters.
5. **Dyslexia:** no special "dyslexia font" has strong evidence behind it. What helps is clear letter shapes, generous spacing (line height 1.5 for body text), left-aligned text, short lines (60–75 characters) and no long italics or all-caps paragraphs.

## Our font lab
`brand/tools/fonts-lab/lab.py` tests installed Fontsource fonts for two things:
- **Glyph coverage:** the language sets above.
- **Confusable letters:** how much I/l/1, O/0 and rn/m overlap. 1.0 means they are identical, lower is clearer.

Results (2026 run, 400 weight, from Fontsource subsets) are in `report.md`. Highlights:
- **Full African Latin coverage (Yoruba, Igbo, Hausa, Akan, ₦ ₵):** Noto Sans, Inter Tight, Questrial (extended by Google for African languages), Onest (missing ₦ and ₵).
- **Clearest l and 1:** Hanken Grotesk, Public Sans, Atkinson Hyperlegible Next, Geist, Schibsted Grotesk.
- **Clearest I and l:** Atkinson Hyperlegible Next and Schibsted Grotesk. In Host Grotesk, Instrument Sans, Inter Tight, Figtree, DM Sans and Manrope, I and l are identical.
- **Arabic:** IBM Plex Sans Arabic, and Readex Pro (Lexend's Arabic sister, which also covers Yoruba and Igbo).
- **Ge'ez:** Noto Sans Ethiopic.
- **Weak on African languages:** Atkinson Hyperlegible Next, Host Grotesk, Instrument Sans, DM Sans and Figtree (no Igbo or Hausa).
- Caveat: Fontsource splits fonts into subsets, so a full font file can have more glyphs than this shows. Check the full font before ruling it out.

## Pairings that pass (taste and access)
- **Studio voice:** Hanken Grotesk or Geist for sentences and emails, Instrument Serif for one italic accent word (never emails or codes), IBM Plex Mono for labels.
- **West Africa client:** Inter Tight or Noto Sans (full coverage), with Fraunces or Newsreader for an editorial line.
- **Gulf or North Africa client (bilingual):** Readex Pro plus Lexend (they share proportions), or IBM Plex Sans Arabic plus IBM Plex Sans.
- **Ethiopia:** Noto Sans Ethiopic plus Noto Sans.
- **Signage and wayfinding (hotels, clinics):** Atkinson Hyperlegible Next.
