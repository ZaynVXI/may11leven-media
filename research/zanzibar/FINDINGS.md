# Zanzibar hotel websites on a phone: findings (study 01, reviewed)

May11Leven Labs is a design studio that builds websites for hotels, so we have an interest in this topic. That's why the method is published in full and only totals are reported. No business is named, and the per-site data stays private.

## Method
- **Sample:** every hotel, guest house, hostel or apartment on Unguja that OpenStreetMap lists with its own website: **107 listings** (query in `overpass.py`).
- **Dead links:** every domain that failed was rechecked on two DNS resolvers (1.1.1.1 and 8.8.8.8) and looked up in WHOIS.
- **Excluded from the website checks:**
  - international chains (Iberostar, Meliá, Hilton, Hyatt, Golden Tulip, Diamonds, Sunrise, SBH, TUI)
  - places that aren't accommodation (a museum, a beach club)
  - aggregator and Airbnb pages
  - pages behind a bot check or showing a maintenance or "not available" notice (we never tried to get past a bot check)
  - a group website that two listings both point to, counted once
- **Final set:** **51 independent places to stay with a working website** ("independent" here means not part of an international chain).
- **Homepage checks:** the homepage opened as a guest would see it on a mid-range Android phone (Playwright). Every price and "book direct" match was then checked by eye from the saved text.
- **Speed:** Google Lighthouse 12, mobile profile (simulated mid-range phone on slow 4G), **3 runs per site, median used**. These are lab estimates, not measurements from real guests. A few sites varied more than 2× between runs; no headline figure depends on them.
- **Limits:**
  - Homepage only.
  - OpenStreetMap lags reality.
  - The accessibility figure is Lighthouse's automated subset, not a full audit.

## Findings
| | Result | n |
|---|---|---|
| Listed hotel websites that are gone (domain no longer registered or resolving) or taken over after lapsing (now gambling, pirated video or a "for sale" page) | **18 (17%), about 1 in 6** | 107 |
| Further listed links that lead to an error (certificate warning, redirect loop, 404/500) | **13 (12%)** | 107 |
| Median time until the **main image or headline** appears (LCP) | **9.6 s** (the first thing appears at a median of 3.5 s) | 49 |
| Slower than Google's 4 s "poor" mark for LCP | **86%** | 49 |
| Main content takes over 10 s | **47%** | 49 |
| Rated "good" (2.5 s or less) | **6%** | 49 |
| Lighthouse performance score 90+ | **8%** | 49 |
| Homepage heavier than 3 MB | **76%** (median 4.8 MB) | 49 |
| "Book" button leaves the hotel's website for a booking page on a different web address | **51%** (23 to a booking-engine page, 3 to Booking.com or Airbnb) | 51 |
| No booking button on the homepage at all | **18%** | 51 |
| Show a room price on the homepage | **16%** (8, checked by eye) | 51 |
| Give a real reason to book direct (a discount or perk) | **4%** (2, checked by eye) | 51 |
| Mention M-Pesa or any mobile money on the homepage | **0%** | 51 |
| Visible WhatsApp button or link | **27%** | 51 |
| Link to Instagram | **78%** | 51 |
| Lighthouse accessibility score under 90 | **61%** | 49 |

## The story (wording checked against the data)
On a mid-range phone, the median small-hotel website in Zanzibar takes about 9.6 seconds (lab estimate) before its main image or headline appears. 86% are slower than Google's "poor" line. Most don't show a price, only 2 in 51 give guests a reason to book direct, and half send guests to a different web address to finish booking. About 1 in 6 hotel websites listed on the map is gone or taken over.

## Review
An independent review recomputed every number and listed 10 fixes. All 10 are applied here. The per-site review notes are kept privately because they name businesses.
