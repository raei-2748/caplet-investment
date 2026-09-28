# D3 model v2 results: what each new switch changes

Agent D3 (Quant Modeler), insight_v1 run, Phase D. Written 2026-09-28. This is AI-generated research for Team Caplet:
numbers, tables and checklists. None of it is text to submit. The team decides and writes every deliverable in its own
words, and records this AI use in the Final Report's Works Cited.

- **Model:** `research/insight_v1/scripts/strategy_mc_v2.py`. It extends the verified
  `research/verified_2026-09-27/strategy_mc.py`.
- **Run it** (from the repo root, about 25 seconds): `.venv/bin/python research/insight_v1/scripts/strategy_mc_v2.py`
- **Data snapshots** (`research/insight_v1/scripts/data/D3/`): written by `D3_data_snapshot.py`.
- **Question scripts:** `D3_control_and_equity.py`, `D3_lock_frontier.py`, `D3_range_rules.py`,
  `D3_funded_status_log.py`, `D3_barbell.py`, `D3_joint_tail.py`, `D3_ratchet.py`, `D3_history_stress.py`.
- **Status labels:**
  - **MODEL** means an ASSUMPTION-based model output, not a forecast.
  - **VRF** means VERIFIED-REPO-FILE.
  - **VP** means VERIFIED-PRIMARY.

## Summary (read this first)

1. **The verified base still reproduces, path by path.** With every switch off, v2 matches the verified script within
   $1 per path. The 2033 surplus (the money left after the payments are bought) is p5/p25/p50/p75/p95 =
   $159k/$186k/$207k/$232k/$273k. The 2031 floor is $127k/$165k/$217k, and growth-first misses 3.2% of the time.
   These are the same numbers as F-401/F-402.
2. **The D3 central case is a little lower and a little wider than the verified base.** The central case turns on:
   - the real Nov-15 STRIPS ladder ($294,387);
   - rate moves between today and the January 2027 purchase;
   - what WInS actually holds (AC World equity plus short government bonds);
   - fund expense ratios.

   It gives a 2033 surplus of **$152k/$204k/$277k** (p5/p50/p95) and a 2031 floor of **$121k/$163k/$220k** (MODEL).
   Against the verified base, p5 falls by $7k and the median by $3k.
3. **The payments are never short in any tested case where the 2028 deposit arrives.** This includes a $75k deposit
   and a deposit one year late.
   - The ladder costs more than $300,000 in January 2027 in about **30%** of rate paths. The mean gap is $7k and the
     p95 gap is $12.5k (MODEL; VP inputs).
   - Any deposit of about $43k or more fills the gap, even after a 150bp fall in rates (about a 4-standard-deviation
     move at 2026 volatility).
   - Only a missing or near-zero deposit leaves part of the 2033 payment unfunded: $9k on average when it happens,
     $24k at p95.
4. **Robust numbers:**
   - Payments fully bought whenever the deposit arrives.
   - P(contribution below the bought floor) = 0.
   - A median facility amount of about $200-210k in every asset, fat-tail and rate switch.
   - Fat tails move p1/p5/p95 by less than about $7k.
   - Switching the model to what WInS holds moves the median by about +$1k.
5. **Assumption-driven numbers:**
   - Anything that depends on the 2028 deposit. A $75k deposit cuts the median by $98k.
   - Advisory fees charged on the ladder: about -$11k of median per 0.5% a year.
   - Which forecasting firm's return assumptions are used. Vanguard's midpoint gives about -$6k of median.
   - The pre-purchase rate move: P(ladder costs more than $300k) is 24-34%.
   - The stated confidence of the range's top. An "80%" top lands 72-84% within the range across the model variants,
     and 62% on raw U.S. history. With a cap rule it is 100% by design.
6. **Three new facts the team should know:**
   - **A fee on the ladder is a claim on the promise money.** Charging 1% a year on everything costs about $32k of
     median surplus. If the deposit is missing, the fees cannot be paid from the leftover money in 100% of paths.
   - **The model understates crash years.** It gives a -30% stock year in 0.3% of years; S&P history shows 3.1% (1931,
     1937, 2008). Even so, its 10th percentile matches history's.
   - **Choosing the top of the range as a fixed multiple of the floor (for example 1.25x) is fragile.** It lands within
     the range 0%, 44% or 100% of the time depending on the floor share. Set the top from the unlocked money's own risk
     instead.

## 1. The model in one paragraph (plain English)

The model simulates 200,000 possible futures, each a set of yearly returns for stocks and bonds drawn from
J.P. Morgan's published long-term assumptions. In each future:
- Laura's $300,000 first buys ten zero-coupon Treasury bonds (Treasury bonds sold at a discount that pay one fixed
  amount on one date), one for each $50,000 operating payment in 2033-2042.
- The leftover (the "sleeve"), plus the $150,000 she adds in 2028, is invested in a stock/bond mix.
- In 2031 most of the sleeve moves into a 2-year Treasury note. That is the "floor" she can promise co-sponsors.
- In 2033 the floor plus the rest is the money for the facility and for flexibility.

Version 2 adds switches for what version 1 assumed away: rates moving before the January 2027 purchase, a smaller,
late or missing 2028 deposit, fees, WInS-like funds, fat-tailed returns, rules for the 2031 range, and rules for the
2033 contribution. Every switch is off by default, so the default run is the verified model.

Terms:
- **p5/p50/p95**: 5 in 100 futures end below the p5 number; p50 is the median, the middle outcome.
- **Fat tails**: extreme years happen more often than a bell curve says.
- **Common random numbers**: every run uses the same random futures, so a difference between two runs is caused by
  the switch, not by luck.

## 2. Reproduction check (VRF inputs; MODEL outputs)

| Quantity | Verified script | v2, all switches off |
|---|---|---|
| Ladder cost at 2027-01-01, exact Jan-1 dates | $292,264 | $292,264 (computed: $292,263.85) |
| 2033 surplus p5/p25/p50/p75/p95 | $159k/$186k/$207k/$232k/$273k | identical (largest path difference $0.54) |
| 2031 floor p5/p50/p95 | $127k/$165k/$217k | identical |
| Growth-first miss rate; $75k; $0 deposit | 3.2%; 13.7%; 40.8% | identical (exactly) |
| Equity 50/60/70% | $164k/$205k/$260k; $159k/$207k/$273k; $154k/$209k/$287k | identical |

The Nov-15 STRIPS ladder recomputes to **$294,387**, the same as S1.
The forward zero rate from 2027 to 2033 recomputes to 5.08% (F-012).

## 3. What each switch changes (one at a time, against the verified base; MODEL)

Changes are in $k of the 2033 surplus. The last column is the chance that part of a payment is unbought.

| Switch | Label | Δp5 | Δp50 | Δp95 | P(payments short) |
|---|---|---|---|---|---|
| (a) Real Nov-15 STRIPS ladder, no rate move | VRF + method | -2.3 | -3.0 | -3.9 | 0% |
| (a) Rates move before purchase, sd 37bp (2026 volatility) | VP inputs / ASSUMPTION | -4.8 | -0.6 | +5.1 | 0% |
| (a) Both (the central-case setting) | | -7.1 | -3.6 | +1.2 | 0% |
| (a) Both, sd 48bp (98-day moves since 1990) | | -10.3 | -3.8 | +4.6 | 0% |
| (b) Deposit $75k | ASSUMPTION scenario | -75.5 | -98.3 | -129.6 | 0% |
| (b) Deposit late (arrives January 2029) | ASSUMPTION scenario | -1.0 | -11.0 | -26.8 | 0% |
| (b) Deposit missing | ASSUMPTION scenario | -151.3 | -196.6 | -258.6 | 0% without (a); 30% with (a) |
| (b) Deposit cut to $0 in 25% of paths, correlation 0.6 with 2027 stocks | ASSUMPTION | -150.6 | -13.9 | -6.5 | 0% without (a); 7.6% with (a) |
| (c) Fund expenses 0.048% (60% VT 0.06% + 40% VGSH 0.03%) | VP | -0.3 | -0.3 | -0.4 | 0% |
| (c) Plus a 0.5% advisory fee on the sleeve | ASSUMPTION | -4.3 | -5.3 | -6.6 | 0% |
| (c) Plus a 1.0% advisory fee on the sleeve | ASSUMPTION | -8.3 | -10.2 | -12.8 | 0% |
| (c) Plus 0.5% on the sleeve and the ladder | ASSUMPTION | -14.6 | -16.6 | -19.1 | 0% |
| (c) Plus 1.0% on the sleeve and the ladder | ASSUMPTION | -28.6 | -32.4 | -37.3 | 0% |
| (d) JPM AC World equity instead of U.S. large cap | VRF | +0.3 | +1.3 | +3.0 | 0% |
| (d) AC World plus JPM short government/credit (the WInS mix) | VRF | -0.1 | +1.1 | +3.1 | 0% |
| (d) AC World plus short Treasuries at 3.5% | ASSUMPTION | -1.2 | -0.2 | +1.4 | 0% |
| (d) AC World plus short Treasuries at 4.9% (forward-implied) | ASSUMPTION | +1.9 | +3.6 | +6.2 | 0% |
| (d) Vanguard-midpoint U.S. equity return, 5.2% | VP range 4.2-6.2% | -4.7 | -6.0 | -7.8 | 0% |
| (e) Student-t, nu=4, same variance | ASSUMPTION | +2.0 | -0.5 | -3.0 | 0% |
| (e) Student-t, nu=4, scaled to the same 5% bad year | ASSUMPTION | -1.2 | -0.3 | +4.3 | 0% |
| 2031 2-year yield 3.0% instead of 4.81% | ASSUMPTION | -4.4 | -5.7 | -7.4 | 0% |

**Reading the table.** The deposit dwarfs everything else. Fees on the ladder come next, then the choice of forecasting
firm and the 2031 yield. Fat tails and the choice of funds barely matter over six years. The central case (row 3 of the
table, plus (d) WInS mix and fund expenses) is $152k/$204k/$277k.

## 4. Switch by switch

### (a) Rate risk between today and the January 2027 purchase
**Rule modelled:**
- If the ladder costs more than $300,000, buy the longest payments first with the $300,000.
- Buy the rest in January 2028 from the deposit, at January-2028 prices.

**Rates:** parallel moves with zero drift from today's forward prices (ASSUMPTION). The standard deviation is 0.37pp
to January 2027: 71bp a year (F-014; recomputed from FRED DGS10 as 70.6bp) times √0.27. The sensitivity run uses
0.48pp, the standard deviation of 98-day moves in the 10-year yield since 1990 (FRED DGS10, VP inputs, derived). After
the purchase, yields move with a standard deviation of 0.71pp a year; that only affects top-up prices.

| Ladder | Pre-purchase sd | P(cost > $300k) | Mean gap if > 0 | p95 gap | P(short), deposit arrives | 2033 surplus p5/p50/p95 |
|---|---|---|---|---|---|---|
| Exact dates ($292,264) | 0 | 0% | - | - | 0% | $159k/$207k/$273k |
| Exact | 0.37pp | 23.8% | $6,579 | $10,446 | 0% | $154k/$207k/$278k |
| Exact | 0.48pp | 29.2% | $9,195 | $16,095 | 0% | $151k/$206k/$282k |
| STRIPS ($294,387) | 0 | 0% | - | - | 0% | $157k/$204k/$269k |
| **STRIPS** | **0.37pp** | **30.2%** | **$7,022** | **$12,458** | **0%** | **$152k/$204k/$275k** |
| STRIPS | 0.48pp | 34.4% | $9,690 | $18,070 | 0% | $149k/$203k/$278k |
| STRIPS plus a 0.25% broker mark-up (ASSUMPTION, unsourced) | 0.37pp | 32.6% | | | 0% | $151k/$203k/$273k |

**Cost of the STRIPS ladder by rate move before purchase** (VRF curve; same bootstrap method):

| Move | Ladder cost |
|---|---|
| +25bp | $287,297 |
| 0 | $294,387 |
| -19bp | $299,908 (the breakeven) |
| -25bp | $301,676 |
| -50bp | $309,169 |
| -75bp | $316,872 |
| -100bp | $324,793 |
| -150bp | $341,313 |

**Reading.** The 24% in F-112 was for the exact-date ladder. With the real ladder the headroom is 19bp, not 27bp, so
about 3 rate paths in 10 need part of the 2028 deposit before the promise is complete.

### (b) 2028 deposit scenarios
Lock-early runs use the STRIPS ladder with the pre-purchase sd at 0.37pp. The growth-first ("G") runs use the verified
convention.

| Scenario | L: P(payments short) | L: mean short if short | L: 2033 surplus p5/p50/p95 | G: miss |
|---|---|---|---|---|
| Full $150k, 2028 (case) | 0% | - | $152k/$204k/$275k | 3.2% |
| $75k, 2028 | 0% | - | $73k/$105k/$149k | 13.7% |
| Late: $150k in 2029 | 0% | - | $150k/$193k/$249k | 2.9% |
| Missing | 30.2% | $9,114 of payment face | $0k/$8k/$33k | 40.8% |
| Cut to $75k in 25% of paths, correlation 0.6 with 2027 stocks | 0% | - | $87k/$189k/$268k | 7.0% |
| Cut to $0 in 25% of paths, correlation 0.6 | 7.6% | $9,043 | $0k/$189k/$268k | 15.4% |
| Same, plus 2026 rates linked to a coming 2027 recession (link 0.5) | 11.2% | $10,327 | $0k/$191k/$271k | 15.4% |
| Extreme: correlation 0.9, link 0.8 | 17.2% | $11,327 | $0k/$194k/$274k | 16.9% |

**Correlation sensitivity** (deposit cut to $0 in 25% of paths):

| Correlation with 2027 stocks | 0.0 | 0.3 | 0.6 | 0.9 |
|---|---|---|---|---|
| G's miss rate | 12.6% | 14.1% | 15.4% | 16.9% |
| L's shortfall (a (b)-only effect) | 7.6% at every correlation | | | |

L does not respond to this correlation alone. It responds only when the rate fall before January 2027 is also linked
to the 2027 downturn (the "link" rows above).

**Reading.**
- The correlation is an ASSUMPTION. History gives a range: the stock/10-year-Treasury return correlation was +0.36 in
  1966-99, -0.65 in 2000-21 and +0.88 in 2022-25 (Damodaran annual data, VP; `D3_joint_tail.py`).
- The case says the deposit "will" arrive (R-AN35), so every deposit row is a beyond-case stress. Label it that way.

### (c) Fees
- Fund expenses are VP (issuer pages via the S3 ticket). Advisory fees are ASSUMPTION scenarios: the case names no fee
  and the firm is fictional.
- Fees on the ladder are paid out of the sleeve. A buy-and-hold zero-coupon ladder pays no income to cover a fee.

| Fund expense | Advisory fee | Charged on | Surplus p5/p50/p95 | Change in median |
|---|---|---|---|---|
| 0 | 0 | - | $159k/$207k/$273k | - |
| 0.048% | 0 | - | $159k/$207k/$273k | -$0.3k |
| 0.048% | 0.5% | sleeve | $155k/$202k/$267k | -$5.3k |
| 0.048% | 1.0% | sleeve | $151k/$197k/$261k | -$10.2k |
| 0.048% | 0.5% | sleeve + ladder | $145k/$191k/$254k | -$16.6k |
| 0.048% | 1.0% | sleeve + ladder | $131k/$175k/$236k | -$32.4k |

- With the deposit arriving, fees never dent the bought 2031 floor (0% of paths).
- **Stress:** 1% on everything with the deposit missing. The fees exceed the leftover money in 100% of paths, by $12.2k
  on average. They would have to come out of the payments' money.
- The riskless control (Treasuries Laura could buy herself) pays no fee and has a median of **$204k**. A 0.5% sleeve
  fee takes away the whole median gain from equity (see M034 in `D3_quant.md`).

### (d) Assets: what the sleeve holds
All rows are VRF JPM rows unless labelled.

| Equity | Sleeve bonds | Surplus p5/p50/p95 | 2031 floor p5/p50/p95 |
|---|---|---|---|
| U.S. large cap 6.70% | Intermediate Treasuries 4.00% (verified) | $159k/$207k/$273k | $127k/$165k/$217k |
| AC World 7.00% | Intermediate Treasuries | $159k/$209k/$276k | $127k/$166k/$219k |
| AC World | Short government/credit 4.00%, vol 1.63% (closest JPM row to VGSH) | $159k/$208k/$276k | $127k/$166k/$219k |
| AC World | Short Treasuries 3.5% (ASSUMPTION) | $158k/$207k/$275k | $126k/$165k/$218k |
| AC World | Short Treasuries 4.9%, forward-implied (ASSUMPTION) | $161k/$211k/$279k | $128k/$167k/$221k |
| Vanguard midpoint 5.2% (VP) | Intermediate Treasuries | $155k/$201k/$265k | $124k/$161k/$211k |

- AC World correlations: 0.00 with intermediate Treasuries and 0.21 with short government/credit.
- U.S. large cap vs short government/credit: 0.16. All from the JPM matrix, p.2 (VRF).
- Vanguard source: U.S. equities "declined from a range of 4.9%–6.9% to a range of 4.2%–6.2%" (VCMM run of 30 June
  2026; corporate.vanguard.com; VP, re-read 2026-09-28).

**Reading.** Moving the model to what WInS holds (VT-like and VGSH-like funds) changes the median by about +$1k. This
closes S3's red-team finding 10: the effect is below model noise.

### (e) Fat tails: Student-t robustness
Setup:
- Multivariate t: stocks and bonds share the same extreme years.
- The median log return is unchanged. The draws are clipped at 8 standard deviations so the mean stays finite.
- The last row is scaled so its 5% bad year matches the bell-curve model's.

| Tails | One-year stock p1/p5 | Simulated arithmetic mean | 2033 surplus p1/p5/p50/p95 | Floor p5 |
|---|---|---|---|---|
| Normal (verified) | -25.1% / -16.9% | 7.94% | $144k/$159k/$207k/$273k | $127k |
| t, nu=6 | -27.8% / -16.2% | 7.95% | $142k/$160k/$207k/$273k | $128k |
| t, nu=4 | -28.8% / -15.2% | 7.92% | $141k/$161k/$207k/$270k | $129k |
| t, nu=3 | -28.4% / -13.2% | 7.83% | $142k/$164k/$207k/$265k | $131k |
| t, nu=4, x1.09 | -31.4% / -17.0% | 8.14% | $137k/$158k/$207k/$278k | $126k |

**Reading.** Fat tails that are random from year to year change the 2033 outcome by only a few $k:
- six years of returns average out;
- only the sleeve is at risk;
- the payments are already bought.

What they do NOT capture is a run of bad years, and history shows such runs. For that test see
`D3_history_stress.py` (M059 in `D3_quant.md`). Vanguard's own notes warn that its model "may be underestimating extreme
negative scenarios unobserved in the historical period" (VP, 2026-09-28).

### (f) The 2031 co-sponsor range
**Setup:**
- Laura buys a floor with share *a* of the sleeve on 1 January 2031.
- The top is set in 2031 as: floor + unlocked money × the p-th percentile of its 2-year growth under the planning
  model.
- The table assumes the contribution is the whole post-reserve surplus. Cap and share rules are in (g).

| Floor share | Top rule | Median floor | Median top | Median width | P(within) | P(below) | P(above) |
|---|---|---|---|---|---|---|---|
| 60% | p80 | $124k | $218k | $94k | 80% | 0% | 20% |
| 70% | p80 | $144k | $215k | $71k | 80% | 0% | 20% |
| **80%** | **p80** | **$165k** | **$212k** | **$47k** | **80%** | **0%** | **20%** |
| 80% | p90 | $165k | $215k | $50k | 90% | 0% | 10% |
| 90% | p80 | $186k | $209k | $24k | 80% | 0% | 20% |
| 100% | any | $206k | $206k | $0 | 100% | 0% | 0% |

Two top rules to avoid:
- **"Top = the unlocked money keeps its 2031 value"** is within the range only 19% of the time, because that money
  usually grows.
- **"Top = 1.25 × floor"** is within 0% of the time at a 60-70% floor share, 44% at 80% and 100% at 90%. A top set as a
  fixed multiple of the floor is not tied to the money that is still at risk.

**Is the stated confidence model-proof?** The range is set with the planning model (80% floor, no cap). The outcomes
come from:

| Outcome model | P(within), p80 top | P(within), p90 top |
|---|---|---|
| Same model | 80.0% | 90.0% |
| t, nu=4 | 83.7% | 92.1% |
| t, nu=4 x1.09 | 81.7% | 90.5% |
| Vanguard midpoint | 83.2% | 92.0% |
| Stocks 1.7pp a year weaker | 83.8% | 92.4% |
| Stocks 3pp a year stronger | 72.2% | 84.8% |
| 0.5% fee on the ladder | 92.6% | 96.8% |
| History 1928-2025, raw (97 two-year periods; S&P 500 + bond proxy) | 61.9% | 81.4% |
| History, rescaled to JPM's medians | 76.3% | 90.7% |

- P(below the floor) = **0** in every row. The floor is bought.
- When the stated confidence is wrong, it is wrong on the upside: outcomes land above the top, which is good news for
  co-sponsors.

**2031 two-year yield** (M060 caveat), median floor at 80%:

| Yield | Median floor | Change vs 4.81% |
|---|---|---|
| 3.0% | $159.2k | -$5.7k |
| 3.5% | $160.8k | |
| 4.0% | $162.4k | -$2.5k |
| 4.81% | $164.9k | - |

### (g) The 2033 contribution rule and the flexibility kept
Setting: 80% floor, top at p80, verified base.

| Rule | Contribution p5/p50/p95 | Flexibility kept p5/p50/p95 | Median flexibility share | P(flexibility = 0) | P(within range) |
|---|---|---|---|---|---|
| Give everything | $159k/$207k/$273k | $0/$0/$0 | 0% | 100% | 80% |
| Give everything, capped at the top | $159k/$207k/$272k | $0/$0/$6k | 0% | 80% | 100% |
| Give 90% of the surplus | $143k/$187k/$246k | $16k/$21k/$27k | 10% | 0% | 80% |
| Give 80% of the surplus | $127k/$166k/$219k | $32k/$41k/$55k | 20% | 0% | 80% |
| **Give 90%, capped** | **$143k/$186k/$245k** | **$16k/$21k/$30k** | 10% | 0% | **100%** |
| Give 80%, capped | $127k/$165k/$217k | $32k/$42k/$56k | 20% | 0% | 100% |
| Floor + half of the excess above it | $143k/$186k/$245k | $15k/$21k/$30k | 10% | 0% | 80% |

**The same rules in the central case** (`D3_range_rules.py` section 6):

| Floor share | Top | Rule | Median floor | Median top | P(within) | P(top reached) | Contribution p5/p50/p95 | Flexibility p5/p50/p95 |
|---|---|---|---|---|---|---|---|---|
| 80% | p80 | give 90%, capped | $146k | $188k | 100% | 20% | $136k/$183k/$248k | $15k/$21k/$30k |
| 90% | p80 | give 90%, capped | $165k | $186k | 100% | 20% | $137k/$183k/$248k | $15k/$21k/$28k |
| 90% | p80 | give everything, capped | $183k | $206k | 100% | 20% | $152k/$204k/$275k | $0/$0/$3k |

**Purchasing power** (median, "give 80%" rule): $166k nominal in 2033.
- In 2026 U.S. dollars at JPM's 2.5% inflation (F-312), that is **$140k**.
- Deflated by the Taiwan construction-cost trend of 3.54% a year (F-508, 2021-2026 average), that is **$130k**.

This is ASSUMPTION arithmetic. The case asks teams to explain inflation's effect on projections and facility costs.

## 5. Robust vs assumption-driven (what can be said with confidence)

| Number or claim | Robust? | What drives it | How to present it |
|---|---|---|---|
| All ten payments bought in January 2027 at a known price | **Robust** (market prices, VRF) | U.S. Treasury credit only | "bought, not forecast" |
| The payments are complete once any deposit ≥ ~$43k arrives | **Robust** across rate paths (the gap is $41k at -150bp, a 4-standard-deviation move; finishing it in January 2028 costs about $43k) | How far rates fall before January | Give the conditional dollar table (M053) |
| P(ladder costs more than $300k in January 2027) ≈ 30% (24-34%) | Assumption-driven (rate volatility) | Rates in Sep-Dec 2026 | "about 1 in 3 rate paths"; re-check on the purchase date |
| P(contribution below the bought floor) = 0 | **Robust** (bought) | U.S. credit; no ladder fees charged to the floor | State it as certainty in nominal U.S. dollars |
| Median facility money ≈ $200-210k | **Fairly robust** ($197-211k across the (a), (d), (e) and 2031-yield switches) | Mostly bond yields, not stocks | "most likely about $200k" |
| p5 of the facility money ≈ $150-160k | Model-dependent (history's worst 6-year window: $105k) | 2027-2030 stock returns | Show one named historical row next to it (M059) |
| p95 ≈ $270-280k | Model-dependent | Equity return assumption | Label as model |
| "80% / 90% confident the contribution lands in the range" | **Assumption-driven** (62-93% across models and history) | The top percentile and the return model | Round it ("about 8 / 9 in 10"), or use a cap so within = 100% and state only the chance of reaching the top |
| Anything involving the 2028 deposit being cut | Assumption-driven, beyond the case | An unknowable probability | Conditional dollars, not joint probabilities |
| Fee effects | Arithmetic, robust given the fee | The fee the firm charges | Say what the fee is charged on |

## 6. What v2 still assumes away (known limits)

1. **Sleeve bond returns are independent of the modelled rate moves.** The shifts only price the ladder, top-ups and
   locks. JPM's 4.0% intermediate-Treasury return is also about 1pp below today's yields (F-317); the forward-implied
   switch in (d) tests this.
2. **Returns are the same distribution every year.** There is no momentum, no valuation regime and no mean reversion.
   History (M059) is the check.
3. **Only parallel moves of the whole curve before purchase.** A twist would change the ladder cost somewhat
   differently. The rungs sit between 6 and 15 years, so the error is small.
4. **The 2031 two-year yield is fixed** (sensitivity 3-4.81%). **The 2028 barbell lock rate is fixed** at 4.98%
   (sensitivity 4.0%).
5. **No fund price noise, bid/ask spread or premium/discount.** STRIPS broker mark-ups are unknown (0.25% tested).
6. **Money is in nominal U.S. dollars.** Taxes are out of scope (case). Taiwan-dollar exchange-rate risk is not in the
   model; F-513 gives a 2-year standard deviation of 6.8% since 2006.
7. **The historical bond proxy** (50% T-bill + 50% 10-year bond) is an ASSUMPTION.

## 7. Reproduce
From the repo root:

1. `.venv/bin/python research/insight_v1/scripts/D3_data_snapshot.py --offline` (re-parses the saved data)
2. `.venv/bin/python research/insight_v1/scripts/strategy_mc_v2.py` (the tables in sections 2-4)
3. The question scripts listed at the top (sections (f) and (g) detail: `D3_range_rules.py`)

- Seed 20260927, 200,000 paths.
- New random streams: `SeedSequence([20260927, k])` for k = 1 (rates), 2 (deposit), 3 (fat-tail mixing).

## Sources (accessed 2026-09-28 unless noted)
- Repo, VRF:
  - `competition/official_market_data/daily-treasury-rates_2026-09.csv` (row 09/25/2026)
  - `competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` p.2 (rows and correlations above)
  - `research/verified_2026-09-27/strategy_mc.py`, `official_curve_pv.py`
  - `research/insight_v1/wins_now/S1_treasury_sleeve.md` (STRIPS dates and costs)
  - `research/insight_v1/wins_now/securities_and_allocation_v0.md` (expense ratios)
  - `research/insight_v1/phase_A/fact_register.md` (F-012, F-014, F-106, F-112, F-312, F-317, F-508, F-513)
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
- U.S. Treasury Daily Par Yield Curve 2026 (VP):
  https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
- FRED DGS2 / DGS5 / DGS10 (VP): https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
- Damodaran, "Historical Returns on Stocks, Bonds and Bills: 1928-2024" (page dated January 2026, rows to 2025; VP
  dataset page): https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
- Vanguard, "Vanguard Capital Markets Model forecasts" (VCMM run of 30 June 2026; VP):
  https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html

## What this teaches
- **A model is a machine for asking "what if", not for predicting.** The most useful output here is the tornado table
  in section 3. It shows which assumptions matter (the deposit, fees, the return forecast) and which do not (fat
  tails, the exact fund). That tells the team where to spend its words.
- **A number you have already bought needs no model.** The payments and the 2031 floor are certain in dollars because
  they are purchased. Everything the model says is about the money that is still invested.
- **An honest range is set from the money still at risk.** A rule of thumb like "1.25 × the floor" is not.
