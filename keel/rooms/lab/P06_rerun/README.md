# P06: the four tail figures at J.P. Morgan's 2027 7.5% (old 7.0% beside them)
(Keel is a simulated team, AI-written.) AI-generated research, not for submission. Genius Lab, Sun 25 Oct 2026 (Sydney).
Card P06 (Noticeboard, `../../../pm/BOARD.md`); request from the Noticeboard in `../../../pm/REQUESTS.md`.

**Basis.** 22 Oct 2026 treasury.gov par curve (`keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv`),
16.78% equity vol, same seeds for both editions, so the only change is the stock return: 2026 LTCMA AC World 7.00%
compound -> 2027 LTCMA global equity 7.5% (report p. 8, Library LC-02; the 2027 matrix is behind a login, so
"compound" is inferred). Runner: `p06_run.py` (patches each script in memory; no model file edited). Raw: `p06_results.json`.
All MODEL.

| Figure in the vote copy | Script | 7.0% (2026 ed.) | 7.5% (2027 ed.) | Say on Tuesday's sheet |
|---|---|---|---|---|
| Coupon-reinvestment gap not covered by leftover + Laura's half | `ips_numbers.py` via L-02 patches | 8.96% | 8.67% | **about 9 in 100** (unchanged) |
| Same, with a $10k buffer from the 2028 deposit | same | 2.85% | 2.73% | **about 3 in 100** (unchanged) |
| Same, with a $15k buffer | same | 1.29% | 1.23% | about 1 in 100 (unchanged) |
| Gift lands below the 2031 top (fund lower in 2033 than 2031) | `L-07_lunch_line/r2.py` | 28.8% | 27.5% | **about 28%** (was 29%) |
| Quoted 2031 bottom, p50 | `range_2031.py` | $140,000 | $140,000 | **$140,000** (unchanged) |
| Quoted 2031 top, p50 | `range_2031.py` | $165,000 | $165,000 | $165,000 (unchanged) |
| P(gift reaches the quoted top) | `range_2031.py`, lognormal | 76% | 77% | about 3 in 4 (unchanged) |

**numbers-auditor check (done).** (1) The 7.0% run reproduces the committed figures exactly (8.96% and 2.85% =
`../L-02_results_22oct.json`; 28.8% = L-07 rung 2), so the runner changes nothing but the return. (2) Size by hand:
half a point more a year for three years lifts the 2031 fund by (1.075/1.07)^3 = 1.014; the model's median fund in
2031 goes $39,524 -> $40,080 (x1.014). On a ~$40k fund that is ~$560, half of it in the range: too small to move a
rounded figure. (3) The bottom is the 2032 Treasury ETF's payout, which owns no stock, so it cannot move with the
stock return. It doesn't.

**Verdict.** The edition switch moves one rounded number (29% -> 28%). Tuesday's sheet can sit on the 2027 edition
with no other change; Archive A1 holds. What *does* move the figures is the curve (15 Oct -> 22 Oct took the bottom
from $145k to $140k), so date the curve, not the return, when a number is read aloud.
