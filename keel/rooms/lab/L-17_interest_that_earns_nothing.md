# L-17: interest that earns nothing (the Genius Lab, Tue 3 Nov 2026, round 7 beat 5; huddle H-023)

(Keel is a simulated team, AI-written.) AI-generated (Claude Code). MODEL. Not for submission.

**For a judge, first.** The ladder's one weak point is the interest it has to reinvest. Our IPS prices that gap once,
in 2031, "at that day's yields, plus a cushion", but the model behind our cheque figures quietly looks again in 2033.
Kai's rule needs no second look and no cushion to size: on the day Laura names her range, set aside what the ladder
would be short if every dollar it pays from then on sat idle until its cheque, in Treasuries that mature before each
January. The only rate nobody has to forecast is zero. In 200,000 model futures the honest version of that rule pays
every cheque in full whenever the money exists and never takes from the gift once the range is named; it costs the
average gift about $670 and empties the stocks Laura keeps more often (28 futures in 100, against 19). Public bond
escrows are sized the same way: "sufficient, without reinvestment".

**Request answered:** the Window (H-021, Tue 3 Nov): run Kai's lock beside A0f and W0f; report cheques paid in full,
kept half all gone, gift mean, top reached, S0 and S6. Done, plus S9, three variants and Kai's two roast arms.

## 1. Hypothesis (Felix's C1, one sentence that can be wrong)
Kai's lock, bought on naming day and never revisited, pays every cheque at least as often as A0f (cushion plus the
January 2033 look), without emptying Laura's kept stocks, lowering the range or cutting the gift mean by more than a
few hundred dollars more often than W0f (V54 as written).

## 2. Kai's roast (sealed before the test; `../../huddles/2026-11-03_interest-that-earns-nothing/posts/r2_kai.md`)
"W-08c sizes each rung's face at `PAY / db`. The model sizes it at `PAY / (dbase * gapf_base)`: smaller, because it
banks on bill interest between a bond's maturity and its January cheque ... Honest lock: about $14,000, not $11,201."
Side knife: "The model grows every pre-2031 coupon at its landing-day yield all the way to maturity. That's a STRIPS,
and STRIPS are banned." And: "the test is half circular: yields are floored at 0.25%". Sealed: as W-08c sized it, base
~99.5% of futures pay every cheque, ~0.4% short over $1,000; ~1.5% if yields fall. The test added his two arms (KW, K0).

## 3. Test
`L-17_interest_that_earns_nothing/run.py` reuses the Window's W-08 chain unchanged (A0f and W0f are asserted equal to
`../window/W-08_results.json`) and appends one block. Curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA
global equities 7.5% | 200,000 paths, seed 20261016 | rho 0.5 unless S0 | ~30 s per world. Results: `results.json`.
- **K, Kai's lock:** each rung's gap if every coupon paid after 1 Jan 2031 earns 0%, and the wait between a bond's
  maturity and its January earns 0%; coupons paid before naming day keep what they earned (the model reinvests each
  coupon at its day's yield to the rung's maturity, so that money no longer rides on future rates). The 2027 leftover
  pays the earliest gaps first. Bought on naming day in par Treasuries maturing before each January, their own coupons
  also held at 0% (cost = gap / (1 + y x years)). Paid from the stocks Laura keeps, then from the range's money that
  day (the range lowered by what her stocks couldn't cover, as W0f). No second look; scored on the realised gap.
- **KK, strictest:** coupons paid before naming day also stop earning on naming day.
- **Kz:** K priced as zero-coupon Treasuries (STRIPS, banned on the WInS-only basis): what the 0% coupon rule costs.
- **KW, WInS-true** (Kai's side knife, round 2): the model reinvests each coupon to its rung's maturity as if in a
  zero-coupon bond, which only STRIPS do. On WInS a coupon reinvested before naming day sits in a coupon bond, so its
  own coupons after naming day also earn 0% here: compounding to naming day, simple interest after.
- **K0, Kai's sealed bet:** the lock as W-08c sized it (each bond sized to pay $50,000 at maturity, so no bill wait),
  applied to the model's real ladder, which counts on bill interest while a bond waits for its January.
- Wrong if: K pays every cheque less often than A0f, or empties her kept stocks, lowers the range or costs the gift
  mean much more than W0f.

## 4. Results (MODEL)
| World | Arm | Every cheque in full | Short over $1,000 | Kept stocks all gone | Range lowered on naming day | Gift pays a cheque after naming | Top reached | Gift mean | Laura's 2042 mean | Naming-day set-aside p50 / p95 / p99 |
|---|---|---|---|---|---|---|---|---|---|---|
| base | A0f (cushion + Jan 2033 look) | 99.87% | 0.02% | 19.0% | 16.9% | 8.1% | 97.84% | $159,956 | $49,270 | $7,500 / $25,226 / $33,197, + the 2033 top-up |
| base | W0f (V54 as written) | 96.01% | 2.44% | 17.5% | 16.9% | 0% | 99.29% | $159,980 | $49,678 | the same, no top-up |
| base | **K, Kai's lock** | **100.00%** | **0%** | **23.0%** | **22.0%** | **0%** | **99.29%** | **$159,767** | **$49,892** | **$9,032 / $23,773 / $30,027** |
| base | KK strictest | 100.00% | 0% | 68.5% | 67.2% | 0% | 99.52% | $152,886 | $48,883 | $25,163 / $34,459 / $38,475 |
| base | **KW, WInS-true lock** (Kai's side knife) | **100.00%** | **0%** | **28.1%** | **26.9%** | **0%** | **99.33%** | **$159,286** | **$48,722** | **$11,635 / $24,893 / $30,781** |
| base | K0, Kai as W-08c sized it (his sealed bet) | 95.16% | 3.30% | 16.3% | 15.5% | 0% | 99.13% | $160,532 | $51,149 | $6,176 / $20,429 / $26,448 |
| yields 2 pts lower for good | A0f | 99.85% | 0.02% | 65.4% | 62.9% | 24.1% | 95.86% | $141,771 | $23,725 | $19,177 / $39,397 / $43,327, + top-up |
| yields 2 pts lower for good | W0f | 94.39% | 3.27% | 63.6% | 62.9% | 0% | 99.55% | $141,826 | $24,038 | the same |
| yields 2 pts lower for good | **K** | **100.00%** | **0%** | **69.9%** | **68.9%** | **0%** | **99.54%** | **$142,211** | **$24,675** | **$20,149 / $35,822 / $39,658** |
| yields 2 pts lower for good | **KW** | **100.00%** | **0%** | **72.8%** | **71.9%** | **0%** | **99.57%** | **$141,580** | **$24,914** | **$21,225 / $36,098 / $39,787** |
| yields 2 pts lower for good | K0 | 79.90% | 15.63% | 62.9% | 61.8% | 0% | 99.52% | $144,580 | $23,490 | $16,943 / $32,174 / $35,889 |
| yields 1 pt lower before the build, 2028 deposit halved | A0f | 98.60% | 1.22% | 86.1% | 83.5% | 22.6% | 95.80% | $37,464 | $13,409 | $7,500 / $26,705 / $32,241 |
| same (S9) | W0f | 95.84% | 2.69% | 85.6% | 83.5% | 0% | 99.85% | $37,530 | $13,402 | the same |
| same (S9) | **K** | **98.71%** | **1.15%** | **82.1%** | **80.4%** | **0%** | **99.82%** | **$37,451** | **$16,239** | **$11,471 / $23,717 / $28,606** |
| same (S9) | **KW** | **98.71%** | **1.15%** | **90.3%** | **89.1%** | **0%** | **99.80%** | **$35,983** | **$17,639** | **$13,158 / $24,437 / $29,192** |
| same (S9) | K0 | 90.93% | 6.20% | 73.0% | 70.8% | 0% | 99.87% | $39,616 | $14,362 | $8,974 / $20,688 / $25,338 |

- **K's only shorts (S9, 1.29%) are futures where the money isn't there:** the lock can't be fully bought in 2.2% of
  them, and a rung was never bought in 2027-28; with the lock fully bought, no cheque is ever short (0 of 200,000 in
  every world). It is a bound, not a forecast: the model floors yields at 0.25%, so anything above zero is a bonus.
- **What the honest lock (KW) costs:** about $670 of the base gift mean (A0f $159,956, KW $159,286; K alone $190), and
  Laura's kept stocks run out more often (28.1% v 19.0% of base futures; 72.8% v 65.4% if yields fall); the range is
  lowered on naming day more often (26.9% v 16.9%). What it gives back: the gift is never taken for a cheque after the
  range is named (A0f takes about $1,800 from it in 8% of base futures and 24% if yields fall); the top is reached
  99.3% v 97.8%; what the cheques never needed (the lock plus the 2027 leftover, less the realised gap: about $18,000
  at the median under KW) goes back to Laura as the rungs pay, so her 2042 mean is within $550 of A0f's ($48,722 v
  $49,270) and $1,189 above it if yields fall. If yields fall for good, KW costs the gift only $191 against A0f.
- **The shape of the cost:** K costs more than "that day's gap plus $7,500" on an ordinary day ($9,032 v $7,500 at the
  median) and less in a bad one ($23,773 v $25,226 at the 95th percentile), because a fixed cushion is the same size
  whatever happened, while the zero-rate gap grows with how much interest is still to come.
- **KK, the strictest reading, is too dear:** it empties her kept stocks in 69% of base futures and costs about $7,000
  of the gift mean. So the rule must say *the interest still to come*, not *all of it*: interest already reinvested
  in bonds that mature with each rung no longer depends on future rates.
- **Kz v K:** holding the lock's own coupons at 0% costs about $700 at the median. Cheap enough to keep the strict rule.

**CORD (Kai's W-08c number; Kai found it in his own roast, round 2):** on the model's own sizing the lock costs **$14,282** on the 22 Oct curve with no rate
moves, not $11,201. W-08c sized each bond to pay $50,000 at its maturity; the model's ladder (`ips_numbers.py` s3)
sizes the Feb-2037 bond (for January 2038) and the May-2038 bond (for January 2039) to earn bill interest during the
10 and 7 months they wait, so the zero-rate gap on those two rungs is $3,108 and $3,158, not $1,379 and $1,917. The
wait is a second, smaller reinvestment exposure the IPS doesn't name; the lock covers it. Left out (K0), it matters:
as W-08c sized it, the lock pays every cheque in only 95.16% of base futures and 79.90% if yields fall, worse than V54
as written.

**Felix's C4 (deterministic, 22 Oct curve, the model's sizing):** of the $500,000 the ladder pays, the bonds' face
values are $317,155 (63.4%), their coupons $135,890 (27.2%), interest on that interest $42,610 (8.5%) and bill
interest while bonds wait for January $4,345 (0.9%). The coupons are fixed; only the last two, about a tenth, depend
on future yields. On naming day the part still riding on yields to come is $19,945 nominal (4.0%).

**Felix's C3:** top reached 99.27-99.87% under every lock and W0f in every world, 95.8-97.8% under A0f. MODEL.

## 5. Verdict (Jun, round 3; the builder, Felix, did not judge; `../../huddles/2026-11-03_interest-that-earns-nothing/posts/r3_jun.md`)
- **Felix's hypothesis is wrong, and C1 is adopted anyway.** KW passes the cheque and top tests (0% short over $1,000
  v A0f's 0.02%; top 99.33% v 97.84%) and fails the price tests (kept stocks emptied 28.1% v W0f's 17.5%; range lowered
  on naming day 26.9% v 16.9%; gift mean $670 under A0f, $1,481 in S9). Jun: "your tests priced it and the price is
  fair."
- **C1: ADOPT, KW as the rule** (IPS as a rule, no figure; Final Report the table and the escrow source). Why: W0f
  misses a cheque by over $1,000 in 1 base future in 41; A0f gets to 99.87% only by paying cheques out of a gift
  co-sponsors have already heard, in 8.1% of base futures and 24.1% if yields fall, "which is what P6 is there to rule
  out". KW, once bought, never misses a cheque and never touches a named range. K needs STRIPS; KK empties her stocks
  in 68.5% of futures; K0 fails.
- **C2 (bond first): BIN.** P5 already goes floor first; the trip is "option", which C2 keeps (a Writing Room word).
- **C3 (every chance with its amount): BIN for the IPS, Final Report.** Once named, the top is bonds; "almost always"
  could only cite the model (Book 11). The confidence goes beside its amount in the co-sponsor draft.
- **C4 (the missing step): Final Report only.** The number worth keeping is not 36.6% but that about a tenth of the
  cheques rides on future yields, and 4.0% on naming day.
- **Kai's bets:** the roast won ($14,282 honest lock, +$3,081, the STRIPS knife worth $2,603 at the median); the seal
  lost (K0 pays every cheque in 95.16% of base futures, not ~99.5%, worse than V54 as written; 15.63% short over
  $1,000 if yields fall, not ~1.5%).
- **What would worry an actuary (Jun):** "0 of 200,000" is true by construction (yields floored at 0.25%, the lock
  assumes zero); the real evidence is K0, where one leg nobody zeroed (0.9% of the cheques) cut 100% to 95.16%. What
  else is unzeroed? One known: the model pays the five fund rungs (2033-37) at par, and the iBond funds pay out net
  asset value. Final Report.
- **The count copy (Jun):** the Lab's "as if that interest earned nothing more" reads as KK to a literal reader and
  misses the wait for January. Jun's, same count (497 strict): "we price that gap as if money paid later sat idle".

## 6. For the IPS and the Final Report
- **IPS (offer, `../../ips_rewrite/inbox/2026-11-03_genius-lab.md`):** P8 "at that day's yields, plus a cushion" ->
  "as if money paid later sat idle" (497 strict, no figure). P9 stays word for word: no second look to name, which
  road A would need. The Writing Room owns the words and tests them on strangers (16:20).
- **Final Report:** the rule, the escrow precedent (`../../huddles/2026-11-03_interest-that-earns-nothing/research/lab_chair.md`),
  this table's KW and A0f rows, the price (her flexibility), K0 as the lesson (the leg nobody zeroed), what the $500,000
  is made of, and the par-v-NAV limit of the model.
