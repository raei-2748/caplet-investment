# FICTION (the room) + real work (the test). L-09: the dedicated ladder in 200,000 rate paths (WO-R1)

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Mon 26 Oct
2026, 13:40 Sydney. Script `../../ips_rewrite/lab/R01_mc.py`, results `../../ips_rewrite/lab/R01_mc_results.json`.
All numbers MODEL, 15 Oct 2026 par curve (par yields as zero rates), the 200,000 paths and seed of
`../../library/ips_numbers_2026-10/ips_numbers.py` (1.00pp/yr parallel walk, yields floored at 0.25%).

**Hypothesis.** Sizing the ladder from 2042 backwards, so every coupon is counted toward a named payment (R01 "B3",
every holding kept at >= $10k face), cuts the coupon-reinvestment tail (p95, p99) by at least a third across the
200,000 paths, not only in R01's one "fall 2 points and stay" line, for under $2,000 more.

**Kai's roast (written before the run).** "You'll pay to fix a risk that only bites if rates fall for good. And six
years of coupons before 2033 still sit in cash, so you've moved the leak, not plugged it. Bet: the tail barely moves
once rates wander instead of falling in a straight line."

**Test.** Both ladders bought 1 Jan 2027 at the 15 Oct curve; only coupon handling differs. A = today's rule (each
rung's coupons reinvested in itself, then cash to its payment date; same formula as the number sheet). B3 = one short
Treasury pot takes every coupon and maturity and pays $50,000 each 1 January. Wrong if B3's p95 is more than two thirds
of A's. Audit: A reproduces R01 exactly (fall 1/2/3 points: $11,062 / $21,385 / $31,030) and the number sheet's p95
within $364 ($25,112 vs $25,476, which also lets the purchase price wander); B3's monthly engine lands within $600 of
R01's annual one ($9,616 vs $10,027 at -2 points).

**Result (MODEL).**

| | Today's ladder (A) | Dedicated (B3) |
|---|---|---|
| Cost on 1 Jan 2027 (R01 basis; compare the gap, not the level) | $297,457 | $298,943 (+$1,486) |
| Shortfall, rates fall 2 points for good | $21,385 | $9,616 |
| Shortfall across 200,000 paths: chance over $1k / p50 / p95 / p99 | 47% / $0 / $25,112 / $32,429 | 47% / $292 / $14,832 / $17,584 |
| Largest gap in any one year, p95 | (rung by rung) | $7,923 (the 2033 payment) |
| Duration / chance cost tops $300k by 1 Jan (iBond coupons fixed at 15 Oct yields) | 7.7 yrs / 41% | 8.6 yrs / 47% |

- **The tail halves (p95 -41%, p99 -46%).** The hypothesis holds; it is not an artefact of the straight-line fall.
- **The gain is the sizing, not the pot.** Run A's holdings through B3's pot and the p95 gets worse ($41,957): pooling
  coupons only helps when the holdings are sized for it.
- **Kai is right about where the risk now lives.** The $85,025 of coupons paid before 2033 waits in short Treasuries
  and pays most of 2033-35 (the first three holdings shrink to $10k face). That pot is the residual risk, and it is
  bounded: B3's worst single-year gap tops out at $7,923 because rates can't fall below the 0.25% floor.
- **Price.** $1,486 more, a longer ladder (DV01 $258 vs $228 per 0.01%), and six points more chance that the 2028
  deposit has to top the ladder up. In 9% of paths B3 ends up shorter than A (rates fall early, then rise).

**WInS book (what "showing it" would take).** At fill prices and the book's scale (0.658 of Laura's plan): sell about
$18k of IBTM's ladder part, $17k IBTO, $16k IBTP, $2k IBTQ; buy $6k IBTR and $7k-12k of each T-bond. About $52k each
way (17% of the book), ten trades, roughly $175 commission, before Fri 6 Nov ET (Sat 7 Nov 09:00 Sydney), across the
iBond ex-date (Mon 2 Nov). Position limits and the 2x-volume rule for IBTO/IBTP are unchecked. Only Ray trades; Keel's
default is **no trades**: the IPS can state dedication as how Laura's real money is sized on 1 Jan 2027, with WInS a
scale model that holds the same ten securities. Whether that reads as a contradiction is the Courtroom's call (WO-R2).

**Where the coupons go, one line (Library request).** Today each holding swallows its own coupons until it matures;
dedicated, the long bonds' coupons are the early years' money. False anywhere? Only if read as "nothing waits": the
coupons before 2033 do wait, in short Treasuries, and that is the risk left.

**Cold panel on the explaining line (C&P; one Sonnet 5.5 subagent as three judges, no Keel context).** S1 "We spend the
interest instead of reinvesting it…" understood by all three, but "instead of reinvesting" overstates (the $85k waits).
S2 "Every coupon is a dose, not a leak…" most memorable (4-5) but all three flag it as AI ("not a leak" template) and
"every… pays the early years" as false: **BIN** the dose/leak line. S3 "size from 2042 backwards" reads most human,
benefit missing; say "payment", never "bill" (reads as T-bill). Merged keeper, true on the model: *"We size the ladder
from 2042 backwards, so every coupon pays a named payment and a fall in rates has less to spoil."* The capsule stays
off this sentence; the motif can carry the schedule elsewhere.

**Verdict: ADOPT as a strategy option for the rewrite** (pending WO-R2 and a Caplet choice). Kai half-won: the leak
moved, not plugged, but moving it halves the tail.
