# FICTION. Jun's numbers sheet

Every number Keel uses: value, date, inputs, and how to re-run it. MODEL = computed, not a fact.
Rule since Episode 2: no number goes into a draft unless it is on this sheet.

| Number | Value | Basis | How | Added |
|---|---|---|---|---|
| Cost of the ten $50k payments (2033-42), valued 1 Jan 2027, **payment-date basis** (each $50k discounted from 1 Jan of its year) | $293,928 (MODEL) | Treasury par curve, 21 Oct 2026 close | `scripts/ladder_pv.py` | 22 Oct |
| Headroom under the $300k deposit | $6,072, about 21bp (MODEL) | same | same; DV01 $291/bp | 22 Oct |
| Deadline gap, TNA | Fri 23 Oct 5 p.m. ET = Sat 24 Oct 08:00 Sydney (15 h) | Python `zoneinfo` | conversion | 23 Oct |
| Deadline gap, IPS | Fri 6 Nov 5 p.m. ET = Sat 7 Nov 09:00 Sydney (16 h, after US clocks change 1 Nov) | Python `zoneinfo` | conversion | 23 Oct |
| Last U.S. fill on 6 Nov | 4 p.m. ET = Sat 7 Nov 08:00 Sydney | Python `zoneinfo` | conversion | 23 Oct |
| Final Report instructions | Mon 9 Nov 9 a.m. ET = Tue 10 Nov 01:00 Sydney | Python `zoneinfo` | conversion | 23 Oct |

Curve used (21 Oct 2026, home.treasury.gov par yields): 1y 4.52, 2y 4.81, 3y 4.89, 5y 4.95, 7y 5.03, 10y 5.13,
20y 5.47, 30y 5.42.

**Basis matters.** Bonds that mature before 1 January cost more to hold than the payment dates alone suggest. A
*holdings basis* (each $50k discounted from the date the bond actually matures) gives a higher cost; checking this
is an open job for Jun. Never quote a ladder cost without saying which basis.

Not yet on the sheet (so not usable): any 2031 range, any facility contribution, the size of the sail.
