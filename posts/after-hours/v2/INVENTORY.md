# After hours v2: full carousel (concept)

8 slides, PXDX structure (brand/learning/prototype-posts.md, Rosie case study), our own style:
1. Hero loop `s1-hero.mp4` (8 s, seamless): the Kusi House chat on a phone held at dusk. Cover still `s1-cover.jpg` (no labels, no headline).
2. Manifesto `s2.jpg`: what it does, then the assistant's first line in grey, the sail mark and the message pill.
3. Split `s3.jpg`: the guest's question at 21:47 over the night roof; the quote card and a "Quote sent" pill below.
4. Full screen `s4.jpg`: the hold screen with real states (raised M-Pesa tab, nested pay button, free cot, 20% hold).
5. Loop `s5-pay.mp4` (7.2 s, seamless): pay pill opens into the M-Pesa prompt, the ring fills, it turns to a tone-on-tone "Booked" card, folds into a chip, back to the pill. Cover `s5-cover.jpg`.
6. Chat `s6.jpg`: it knows the house (cot, late flight), ends on the booked chip.
7. Summary `s7.jpg`: $364 in deposits, 10 answered / 3 booked / 1 for you, the wedding enquiry left for a person.
8. Offer `s8.jpg`: every service, comment 11, email.

- Details pass (brand/learning/ui-details.md): nested radii (card 22/p16 -> image 6; card 36/p24 -> 12; track 22/p4 -> tile 18), equal gaps around nested buttons, raised selection, tone-on-tone status chips with ringed dots, ringed online dot, colour-tinted shadows (sea under guest bubbles, green under booked), one icon stroke.
- Hero photo: Unsplash, David Monje (UjFMiozp51E), free licence, night-graded by us; the screen is replaced with our UI by perspective warp (corners measured at 4x zoom, curved right edge widened so no original screen shows). No AI imagery, no faces.
- Interior photo: Pexels, Keegan Checks (39836716). Roof at night: Pexels 11025138, graded.
- Data checks: $220 x 4 = $880; 20% = $176; rest $704; deposits $176 + $132 + $56 = $364.
- QA: preflight.py pass (spelling warnings are proper nouns and OCR only). Every frame checked at 100%; hero edges zoomed at 4x.
- Build: phone.html + hero.py (hero), pay.html + loop.py (loop), slides.html + shot.py (stills).
