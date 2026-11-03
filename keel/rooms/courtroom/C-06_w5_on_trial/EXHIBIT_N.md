# C-06 exhibit N: the five fund rungs as funds, not bonds (the Courtroom, Tue 3 Nov 2026; huddle H-026)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code), the chair's test. MODEL. Not for submission.
Script `exhibit_N_funds_at_nav.py`; results `exhibit_N_results.json`. Asked by Jun's "what would worry an actuary"
(L-17 s5) and the Courtroom's open to-do ("does 'pays exactly what it promises' stretch to the fund rungs?").

**For a judge, first.** Half of Laura's ladder (the cheques for 2033-37) is five iBond funds, not five bonds. Our model
treats each as a bond that pays its face on 15 December. A real fund holds Treasuries that mature all through its last
year, and the cash then sits waiting for the December close, earning bill rates; it also charges 0.07% a year. Put
that in, and the lock the Lab adopted today stops being airtight: in the world the IPS worries about (rates fall and
stay low), about 1 future in 6 misses a cheque, by about $2,000. Sizing the lock the way W5's own words read, counting
the bonds *inside* the funds as "later bond payments" that sit idle, closes it again, for about $3,500 more on naming
day, all of it paid by the stocks Laura keeps and most of it back to her as the rungs pay.

## What was added (one leg the model never saw)
Per fund rung and path: `face x sum over 12 maturity dates of (1/12) x (coupon - bill rate) x (years from that maturity
to 15 Dec)`, plus `face x 0.07% x its life`. Coupon = the model's own rung (its yield when bought in January 2027).
Maturities spread evenly through the final year (ASSUMPTION: the index allows 1 Jan-15 Dec; real weights not read).
The floor (IBTM again, bought 2 Jan 2028) gets the same leg, against the gift. Sources: iShares, "During the final year
of the fund's life, the underlying bonds will mature and the proceeds will be held in cash equivalents until the
liquidation of the fund"; "the Funds do not seek to return any predetermined amount" (`../../../ips_rewrite/research/R04_fact_checks.md`
row 8, product page archived 30 Sep 2026); expense ratio 0.07 (archived product pages, `archive/rab/data/ishares/`).

## Results (MODEL: V54's design via L-13 -> L-14 -> L-16 -> W-08 -> L-17; 22 Oct 2026 curve; J.P. Morgan 2027 LTCMA global equities 7.5%; 200,000 paths, seed 20261016)
| World | Arm | Every cheque in full | Short over $1,000 | Short p50 / p90 when short | Lock cost p50 | Kept stocks all gone | Gift mean | Top reached |
|---|---|---|---|---|---|---|---|---|
| base | KW, as the Lab ran it (check: identical to L-17) | 100.00% | 0% | - | $11,635 | 28.1% | $159,286 | 99.33% |
| base | **KW-N, funds at net asset value** | **97.02%** | **1.88%** | $1,372 / $2,489 | $11,635 | 28.1% | $159,183 | 91.55% |
| base | KW-N0, bills at 0% after maturity (bound) | 96.69% | 2.14% | $1,421 / $2,641 | $11,635 | 28.1% | $158,926 | 72.81% |
| base | **KWN, lock sized as the words read (+ fee)** | **100.00%** | 0% | - | $15,189 | 38.8% | $157,689 | 92.46% |
| base | KWN-w, words only (fee not priced) | 100.00% | 0% | - | $14,416 | 36.5% | $158,053 | 92.24% |
| yields 2 pts lower for good | KW | 100.00% | 0% | - | $21,225 | 72.8% | $141,580 | 99.57% |
| yields 2 pts lower for good | **KW-N** | **82.18%** | **13.96%** | $2,160 / $3,093 | $21,225 | 72.8% | $141,527 | 94.27% |
| yields 2 pts lower for good | **KWN** | **100.00%** | 0% | - | $25,126 | 79.5% | $138,341 | 94.47% |
| yields 2 pts lower for good | KWN-w | 100.00% | 0% | - | $24,279 | 78.2% | $139,045 | 94.50% |
| S9 (yields 1 pt lower before the build, 2028 deposit halved) | KW | 98.71% | 1.15% | $5,716 / $17,019 | $13,158 | 90.3% | $35,983 | 99.80% |
| S9 | KW-N | 91.97% | 5.77% | $1,703 / $6,531 | $13,158 | 90.3% | $35,980 | 99.00% |
| S9 | KWN | 98.27% | 1.55% | $5,977 / $17,534 | $16,687 | 96.2% | $32,544 | 98.67% |

- **The leg's size** (base): $1,446 at the median with the model's own bill rates (p5 -$1,584, p95 $4,046), of which the
  fee is $949; $4,501 at the median if bills paid nothing (p95 $4,791, max $5,261). If yields fall 2 points for good:
  $2,890 at the median. Per rung at 0% bills, about $860-$930 each.
- **What KWN costs over KW:** $3,559 more on naming day at the median (p95 $4,144; $3,901 if yields fall), paid from the
  stocks Laura keeps (all gone 38.8% v 28.1% of base futures); gift mean -$1,597 (-$3,239 if yields fall); most of it
  comes back to her as the rungs pay (unused lock back to Laura, median $21,326 v $16,981 under KW-N).
- **The fee doesn't decide it:** KWN-w, which zeroes only the funds' waiting cash and ignores the fee, still pays every
  cheque in the base and low-yield worlds, because a 0% assumption is far below what bills pay in almost every path.
- **S9 stays below 100% under every lock**: its shorts are futures where the money to buy the lock or a rung was never
  there (L-17); KWN is a little worse than KW there (98.27% v 98.71%) because a bigger lock is fully bought less often.
- **The floor and the range:** the bottom is never broken in any arm or world (its rule rounds down after a $3,700
  margin; the floor's own leg is $922 at the median, $3,509 at 0% bills). The **top** is reached less often once the
  floor is a fund (91.6% v 99.3% base), always by small amounts, because the top adds the floor at its face.

## What it means (the chair's reading; the bench rules)
1. "Every cheque in full, 0 of 200,000" holds only for the model's par bonds. With the funds as funds, the lock as the
   model sized it misses in 3% of base futures and 18% if yields fall and stay low. A real leg, unzeroed, like K0's.
2. W5's words can be read to cover it: the bonds inside the funds also make "later bond payments". The lock the words
   describe, sized on the funds' holdings, restores every cheque in the base and low-yield worlds. So the fix is in how
   the lock is sized (Final Report: name the funds' holdings, the waiting cash and the fee), and in whether the IPS
   words make a judge see that the funds are inside the rule.
3. Limits: an even maturity spread is assumed; distributions are monthly in the funds and semi-annual here; the date the
   fund pays out after its close isn't stated by iShares; the model floors yields at 0.25%.
