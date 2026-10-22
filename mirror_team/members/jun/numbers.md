# FICTION. Jun's numbers sheet

Every number Keel uses: value, date, inputs, and how to re-run it. MODEL = computed, not a fact.
Rule since Episode 2: no number goes into a draft unless it is on this sheet.

| Number | Value | Basis | How | Added |
|---|---|---|---|---|
| Cost of the ten $50k payments (2033-42), valued 1 Jan 2027 | $293,928 (MODEL) | Treasury par curve, 21 Oct 2026 close | `scripts/ladder_pv.py` | 22 Oct |
| Headroom under the $300k deposit | $6,072, about 21bp (MODEL) | same | same; DV01 $291/bp | 22 Oct |
| Deadline gap, TNA | Fri 23 Oct 5 p.m. ET = Sat 24 Oct 08:00 Sydney (15 h) | Python `zoneinfo` | conversion | 23 Oct |
| Deadline gap, IPS | Fri 6 Nov 5 p.m. ET = Sat 7 Nov 09:00 Sydney (16 h, after US clocks change 1 Nov) | Python `zoneinfo` | conversion | 23 Oct |
| Last U.S. fill on 6 Nov | 4 p.m. ET = Sat 7 Nov 08:00 Sydney | Python `zoneinfo` | conversion | 23 Oct |
| Final Report instructions | Mon 9 Nov 9 a.m. ET = Tue 10 Nov 01:00 Sydney | Python `zoneinfo` | conversion | 23 Oct |
| Ladder cost re-run 23 Oct | $293,928, headroom $6,072 = 21bp (MODEL), unchanged: no newer curve row could be loaded on 23 Oct, so the 21 Oct close stands | Treasury par curve, 21 Oct 2026 | `scripts/ladder_pv.py` | 23 Oct |
| 2028 money for the sail | $156,347 (MODEL) | $150,000 + $6,072 leftover held 1 yr at 1y par 4.52% | `scripts/sail_mc.py` | 23 Oct |
| Sail on 1 Jan 2033, 0% stocks (all in a Treasury maturing near 1 Jan 2033) | $200k, fixed (MODEL) | 5y par 4.95% (21 Oct), coupons reinvested at 4.95% (x1.277); $198k if reinvested 2pt lower | `scripts/sail_mc.py` | 23 Oct |
| Sail, 25% stocks: p5/p25/p50/p75/p95; floor | $181k/$193k/$205k/$219k/$246k; floor $150k (MODEL) | JPM 2026 LTCMA AC World Equity 7.00% compound, 16.78% vol (data 30 Sep 2025), lognormal, 200k paths, buy and hold | same | 23 Oct |
| Sail, 50% stocks | $162k/$187k/$209k/$238k/$293k; floor $100k (MODEL) | same | same | 23 Oct |
| Sail, 75% stocks | $143k/$180k/$214k/$257k/$339k; floor $50k (MODEL) | same | same | 23 Oct |
| Sail, 100% stocks | $124k/$174k/$219k/$277k/$386k; floor $0 (MODEL) | same | same | 23 Oct |
| Chance any stock mix ends below the 0% option | 39% (MODEL), the same for every mix: it is the chance stocks grow less than the 4.95%/yr bond over 2028-32 | same | same | 23 Oct |
| Stocks -40% over 2028-31, then +7% in 2032 | 0%/25%/50%/75%/100%: $200k/$175k/$150k/$125k/$100k (MODEL) | deterministic stress | same | 23 Oct |
| Joint bad case: yields -100bp by 1 Jan 2027 + 5y at 3.95% in 2028 + stocks -40% | 0%/25%/50%/75%/100%: $151k/$133k/$116k/$98k/$80k (MODEL); payments still covered, gap $25.6k paid from 2028 money first | same + ladder repriced at -100bp ($324,703) | same | 23 Oct |
| 2028 deposit only $75k | sail floor $104k at 0% stocks, $78k at 25% (MODEL) | same | same | 23 Oct |
| 2028 deposit $0 | sail about $8k; if the ladder was short in 2027, the 2033 payment is short by the gap (MODEL) | same | same | 23 Oct |
| Chance the ladder costs more than $300k on 1 Jan 2027 | about 30% (10 weeks of moves, 40bp sd); about 40% over a full year (90bp sd) (MODEL) | parallel normal yield shift, 90bp/yr vol = assumption, UNVERIFIED | `scripts/sail_mc.py` | 23 Oct |
| Gap if short | mean $7.8k, p95 $13.8k, p99 $22.4k (10 weeks); -25/-50/-100bp: $1.3k/$8.9k/$24.7k (MODEL) | same | same | 23 Oct |
| Cost of the gap to the sail | about $1.33 in 2033 per $1 of 2027 gap (1y at 4.52%, then 5y at 4.95%); mean gap = about $10k less sail (MODEL) | same | same | 23 Oct |

Curve used (21 Oct 2026, home.treasury.gov par yields): 1y 4.52, 2y 4.81, 3y 4.89, 5y 4.95, 7y 5.03, 10y 5.13,
20y 5.47, 30y 5.42.

Not yet on the sheet (so not usable): any 2031 range, any facility contribution. The sail table above is MODEL
and compares mixes; it is not the team's chosen size (Nora decides by 1 Nov). No historical-window check yet.
