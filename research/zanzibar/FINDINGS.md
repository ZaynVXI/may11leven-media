# Zanzibar hotel websites on a phone: findings (study 01)

## Method
- **Sample:** every hotel, guest house, hostel or apartment on Unguja that OpenStreetMap lists with its own website: **107 sites**. It's a public, reproducible list; we didn't pick the sites.
- **Excluded:** chains (Iberostar, Diamonds, Sunrise, SBH), a museum, a beach club, watersports, aggregator pages and an Airbnb link. Also excluded: 12 sites that showed a bot check or maintenance page. We never tried to get past a bot check.
- **Measured:** the homepage only, opened as a guest on a mid-range phone would (Playwright, Moto G4 profile), plus Google Lighthouse 12 (mobile, simulated slow 4G), one run per site. Detection of booking links, WhatsApp, prices and mobile money is automated, and screenshots were checked by eye.
- **Final set: 51 independent places to stay with a working website.**
- **Limits:** one run per site, so times vary between runs. Homepage only. OpenStreetMap lags reality. Booking detection is a heuristic. We publish totals only and never name a business.

## Findings
| | Result |
|---|---|
| Listed websites that are dead (domain gone) or taken over by spam after the domain lapsed | **21 of 107 (20%)**: 18 dead, 3 now showing gambling or video spam |
| Median time until the main content appears on a mid-range phone (LCP, median of 3 runs, n=50) | **9.2 s** |
| Slower than Google's 4 s "poor" line | **84%** |
| Over 10 s | **46%** |
| "Good" (2.5 s or less) | **8%** |
| Lighthouse performance 90+ | **10%** |
| Median homepage weight | **5.2 MB**; 50% are over 5 MB |
| Booking buttons that send the guest to another site | **35%** |
| Give any reason to book direct (perk, best-rate promise) | **8%** |
| Show any price on the homepage | **18%** |
| Mention M-Pesa or any mobile money | **0%** |
| Link to Instagram | **78%** |
| Offer WhatsApp somewhere on the page | **59%** |
| Accessibility score under 90 | **62%** |

## The story in one line
Guests find Zanzibar's small hotels on Instagram and maps, then meet a website that takes over 9 seconds to show anything, doesn't show a price, and sends them somewhere else to book. One in five listed websites is already dead.

## Before publishing
- [x] Re-ran Lighthouse three times per site; the speed figures are medians of 3 runs (150 runs; one site failed every run, so n=50).
- [ ] Cold review by a separate agent (high-stakes claim).
- [ ] Keep it to totals only, with the method shown in full.
