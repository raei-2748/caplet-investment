# D3: Quant Modeler working file (simulation model, confidence statements, the 2031 range, stress scenarios)

Agent D3, insight_v1 run, Phase D. Written 2026-09-28. This is AI-generated research for Team Caplet. It holds numbers,
evidence, checklists and "what a strong sentence must contain" specifications. It holds **no text to submit**: the six
students decide and write every deliverable in their own words and record this AI use in the Final Report's Works
Cited (Wharton AI policy, brief section 14). Laura appears only through the case and her public professional record.

**Scope.** Nine Phase C survivors: M034, M243, M039, M060, M028, M238, M053, M055, M059. They are worked in deadline
order:
- tier 1 = WInS now / Trading Notes, 23 Oct;
- tier 2 = IPS, 6 Nov;
- tier 3 = Final Report, 4 Dec.

The extra mandate is the v2 model, `research/insight_v1/scripts/strategy_mc_v2.py`. Its full results are in
`research/insight_v1/phase_D/D3_model_v2_results.md`.

**Scripts** (run from the repo root with `.venv/bin/python <script>`; each docstring lists inputs and status labels):

| Script | Topic |
|---|---|
| `strategy_mc_v2.py` | model v2 and switches (a)-(g) |
| `D3_control_and_equity.py` | M034 |
| `D3_funded_status_log.py` | M028 |
| `D3_barbell.py` | M238 |
| `D3_lock_frontier.py` | M243 |
| `D3_range_rules.py` | M039, M060 |
| `D3_joint_tail.py` | M053 |
| `D3_ratchet.py` | M055 |
| `D3_history_stress.py` | M059 |
| `D3_data_snapshot.py` | data snapshots in `scripts/data/D3/` |

All scripts are under `research/insight_v1/scripts/`.

**Labels:**
- VRF = VERIFIED-REPO-FILE.
- VP = VERIFIED-PRIMARY (read on the primary page or file, with its date).
- MODEL = an ASSUMPTION-based model output. It is not a forecast.
- ASSUMPTION = a modelling choice.

Model numbers are rounded to $1k unless the table says otherwise.

**Terms used:**
- **Surplus:** the money left in 2033 after the ten payments are bought. It is the facility-plus-flexibility money.
- **Sleeve:** the invested money outside the payment ladder.
- **Floor:** the part of the sleeve moved into a 2-year Treasury in 2031, so it is certain by 2033.
- **p5/p50/p95:** 5 in 100 simulated futures end below p5; p50 is the median.
- **Riskless control:** the same money put in Treasuries maturing just before 2033, with no stocks at all.

---

## Summary: top findings, ranked by impact on reaching the semifinals and on making the plan unmistakably Laura's

1. **The case's hardest sentence can be answered with a certainty instead of a model percentage (M039, M060).**
   - The case asks for confidence that the 2033 contribution "will fall within that range" (p.3 L117-118, VRF).
   - The bottom can be bought: the 2031 floor. The top can be a cap Laura sets herself, because the case says Laura
     "must decide how much" (p.3 L101, VRF). With both, "within the range" holds in 100% of modelled futures and in
     every fat-tail, low-return and historical test. The only exception is a U.S. default.
   - The model is then needed for one number only: the chance of reaching the top (about 1 in 5 for a top at the 80th
     percentile).
   - Without the cap, an "80% confident" statement lands within the range 62-93% of the time, depending on which model
     or history is used.
   - Pair the cap with a share rule, "give up to about 90% of the post-reserve money". This keeps flexibility of
     $15k/$21k/$30k (p5/p50/p95, central case). The case warns against committing everything (p.3 L102-103, VRF).
   - Lock share: 80-90% of the 2031 sleeve. The median barely moves ($209k at 50% to $206k at 100%). 100% collapses the
     range into "one exact amount", which the case says Laura does not want (L115-116, VRF).
2. **Against the money Laura could lock for certain, stocks in the sleeve buy range, not a bigger expected facility
   (M034).**
   - The riskless control is about $204k by 2033, with no fee (MODEL).
   - 60% sleeve equity adds about $3k at the median under JPM. It adds about $6k if sleeve bonds earn forward yields.
     It loses about $4k under Vanguard's midpoint, and about $2k after a 0.5% advisory fee on the sleeve.
   - The plan ends below the control in 43-54% of futures.
   - What equity buys is spread: on the same simulated path, p95 +$70k against p5 -$46k.
   - The Investment Policy Statement (IPS) must justify equity as upside for the residency and flexibility, not as
     higher expected growth.
   - WInS-now: fix the sleeve equity share (40-60% are all defensible) before the growth-fund (VT) order. WInS trade
     notes cannot be edited, and the note will record the share.
3. **The honest reason to lock all ten payments is that the certainty is bought, not forecast, and it is cheap (M243).**
   - With the 2028 deposit present, 70-95% locks also never fail: in 200,000 model futures and in 93 historical
     windows.
   - A full lock gives up only $0.6-3.3k of median facility money under JPM, and nothing under Vanguard or lower 2033
     rates.
   - But a 90% lock fails in 13% of futures, and an 80% lock in 26%, if the deposit from a self-employed author does
     not come.
   - The IPS must not say "anything less fails".
   - The team should also say what it has been overstating: in about 30% of rate paths the real ladder costs more than
     $300k in January 2027, and the first ~$7k of the 2033 payment then waits for the 2028 deposit.
4. **The joint tail is small, and it is better stated in dollars than as a probability (M053).**
   - Rates must first fall more than 19bp before January (about 30% of rate paths). Even then, the payments go short
     only if the 2028 deposit is almost entirely missing.
   - When they do go short, the unfunded part of the 2033 payment averages $9k (p95 $24k; $31k at a 100bp fall).
   - A deposit of $25k covers even a 100bp fall.
   - The IPS needs one clause: the first use of the 2028 deposit is completing the ladder.
   - "Longest payments first" cuts the price risk of the top-up about threefold compared with "nearest first".
5. **The WInS hedge demonstrably tracks the promise (M028).**
   - In 2026, an IEF/TLH hedge valued from its actual holdings stayed within ±0.42% of the value of Laura's ten
     payments in 95% of six-week windows. That is about ±$830 on the $198k WInS hedge.
   - Over the same windows the payments' value itself swung by up to ±2-3% (MODEL; VP inputs).
   - A five-number weekly log gives one checkable fact for a Trading Note reflection. The WInS-now to-do is small.
6. **Reject the barbell (M238).**
   - The barbell means locking part of the growth money in January 2028 and holding the rest 100% in stocks.
   - The 50% barbell matches the plan only by keeping half the facility money in stocks until 2033.
   - In 2031 it can promise a bought bottom of only about $101k (the plan: about $165k).
   - A 2031-32 crash after the announcement costs it about $34k of median (the plan: $8k).
   - Larger barbells are just lower-equity points on the same frontier.
   - Do not use "it mirrors her floor-first leap": D13 bars that trait.
7. **History check (M059).**
   - A 2008-type year after the 2031 lock trims the facility money by about 5%.
   - The same crashes before the lock cut it by 19-29%: 2022, 2008, 2000-02 and 1973-74. A 1929-31 replay cuts it by
     48%.
   - All ten payments stay bought in every case.
   - The bell-curve model understates crash years: a -30% year happens in 0.3% of model years against 3.1% of S&P
     years. But its 10th percentile matches history's.
   - Show one named historical row next to the model's p5 in the Final Report.
8. **No ratchet (M055).**
   - Locking the floor in thirds (2029-31) raises the bad case (p5 +$9k) but costs $17k at p95.
   - A plain ~42% equity sleeve reaches the same p5 within $2k of median.
   - A second IPS rule is not earned.
9. **The v2 model tells the team where to spend words.** See `D3_model_v2_results.md`.
   - What matters: the 2028 deposit, fees charged on the ladder (a 1% fee on everything costs about $32k of median),
     and which house's return forecast is used.
   - What barely matters: fat tails; holding the WInS funds (VT/VGSH-like) instead of the model's assets.
   - Central case: 2033 surplus $152k/$204k/$277k (p5/p50/p95), against the verified $159k/$207k/$273k.

---

## Tier 1: WInS now and the Trading Notes (23 Oct)

### M034. Judge the sleeve against Laura's riskless control, not a stock index
**The question (Phase C):** should every sleeve recommendation be judged against the whole surplus locked in Treasuries
(about $204k in 2033), given that 60% equity gives a median of about $207-210k but a p5 of about $159k? And would an
all-Treasury rival beat us on simplicity?

**One-sentence answer:** Yes. Against the roughly $204k Laura could lock without any fee, 60% sleeve equity adds only
about +$3k at the median under JPM (from -$4k to +$6k across the tested assumptions, and -$2k after a 0.5% sleeve fee).
The plan ends below the control in 43-54% of futures. So the equity buys a wider facility range, not a bigger expected
facility, and it must be justified and benchmarked that way.

**Numbers** (`D3_control_and_equity.py`; MODEL unless labelled):

*The riskless control.* Two Treasury zeros maturing 1 January 2033 (F-012; F-106 method; VRF curve):
- the 2027 leftover: $7,736 × 1.3512 = $10,453;
- the 2028 deposit: $150,000 × 1.2903 = $193,544 on today's forwards;
- total **$203,997**.

The 2028 part cannot be locked until the money arrives. With a yearly rate move of sd 0.71pp (F-014), the control is
**$193k/$204k/$215k** (p5/p50/p95).

*Sleeve equity weight against the control* (verified inputs; 80% floor locked in 2031):

| Sleeve equity | 2033 surplus p5/p50/p95 | Median lift over control | Lift on the same path, p5 / p95 | P(plan < control) |
|---|---|---|---|---|
| 0% | $177k/$195k/$215k | -$9.3k | -$31k / +$14k | 75% |
| 20% | $177k/$199k/$225k | -$4.5k | -$29k / +$23k | 61% |
| 40% | $170k/$204k/$247k | -$0.5k | -$36k / +$44k | 51% |
| 50% | $164k/$205k/$260k | +$1.4k | -$41k / +$57k | 48% |
| **60% (current)** | **$159k/$207k/$273k** | **+$3.3k** | **-$46k / +$70k** | **46%** |
| 70% | $154k/$209k/$287k | +$5.0k | -$51k / +$84k | 45% |
| 100% | $137k/$214k/$332k | +$9.7k | -$68k / +$128k | 43% |

The median lift of 60% equity under other assumptions:

| Assumption set | Median lift of 60% equity | P(plan < control) |
|---|---|---|
| Central case (STRIPS ladder, rate risk, AC World + short government bonds, fund fees) | +$3.3k | 45% |
| Sleeve bonds at the forward-implied 4.9% | +$5.7k | 43% |
| Vanguard midpoint 5.2% (VP range 4.2-6.2%) | -$3.9k | 54% |
| 0.5% advisory fee on the sleeve (the control pays none) | -$1.7k | 51% |

- Moving from 40% to 60% equity: p5 -$8-10k, median +$1.5-3.9k, p95 +$22-26k, across the four sets.
- Whole-portfolio equity on 1 January 2028 (sleeve equity 40/50/60/70%): 13.6% / 17.0% / 20.4% / 23.8%.
  ASSUMPTION: medians; ladder at its forward value of $306,077 (F-106).
- WInS option (ii) at a 66% hedge: VT/VGSH = 13.2/19.8% at 40% sleeve equity, 16.5/16.5% at 50%, 19.8/13.2% at 60%.

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| The case asks for "an appropriate balance between pursuing growth and protecting the capital required for her goals" | case p.2 L71-74 | VRF |
| Laura "has been willing to take thoughtful risks" | case p.2 L69-71 | VRF |
| JPM: U.S. large cap 6.70/7.94/16.47; AC World 7.00/8.28/16.78; intermediate Treasuries 4.00; short govt/credit 4.00/4.01/1.63 | JPM LTCMA 2026 matrix p.2 | VRF |
| JPM's bond assumption (4.0%) sits about 1pp below today's yields (IEF YTM 5.17%) | F-317, F-203 | VRF/VP |
| Vanguard: U.S. equities 10-year expected return 4.2%-6.2% (run of 30 June 2026) | https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html (accessed 2026-09-28) | VP |
| Her résumé lists "A/B testing" as a product-management skill (so a control-vs-plan comparison is a frame she uses professionally) | D13a B9b-Q02, https://lauragao.com/s/Laura-Gao-Resume.pdf | VP (D13a); use at most once, in the Final Report only |

**Mis-posed parts:**
- The premise number is right: $204.0k.
- The phrase "the whole surplus locked" is not: the 2028 money cannot be locked today. The control therefore carries
  about ±$11k of 2028 rate risk.
- The "all-Treasury rival" is the riskless control itself: median $204k (-$3k against the 60% plan) and p5 $193k
  (+$34k). Keeping the sleeve but holding 0% equity is worse than both (median $195k) because JPM's 4.0% bond
  assumption sits below the ~5.1% that locking earns. The rival's facility amount is known in 2028.
- On simplicity alone it would win. It loses on the case's "pursuing growth" and on giving co-sponsors a range. Name it
  in the Final Report's "alternatives considered".

**Implication:**
- *Decision (WInS-now):* the team fixes the sleeve equity share before the VT order.
  - The evidence does not force a move from 60%.
  - 50% ("half of the free money") costs $2k of median and $13k of p95 and gains $5k at p5.
  - The WInS growth note must state the share in the team's words. Notes are permanent (S3 ticket; A4).
- *Sentence (IPS):* the "why any stocks" sentence must contain:
  1. the sure alternative exists;
  2. what equity adds (upside for the facility and flexibility);
  3. what it costs (a lower bad case);
  4. that the payments never depend on it.
- *Number (Final Report):* one chart. A flat line for the riskless control (~$204k) over the plan's p5-p95 fan,
  labelled "lift over the control".
- *Fee note:* if the fictional firm charges a fee, say what it is charged on. A fee on the sleeve alone (0.5%) erases
  the median lift. A fee on the ladder costs about $11k of median per 0.5% (model v2 (c)).

**Tier** 1. **Confidence:** high on the direction; medium on each dollar figure. **Changes current strategy:** no.
The structure stays; the justification and the benchmark change. **Criterion:** Portfolio Analysis ("reasonable
assumptions and projections … under varying market outcomes", R-S26).

**What this teaches:** a risky choice should always be compared with the best sure thing you could have had instead,
not with a market index.

### M028. A weekly funded-status log for the WInS hedge
**The question:** should the team log, from the first WInS trade, the value of Laura's ten payments on that day's curve,
the ladder cost, the funded ratio and the WInS hedge value, so a Trading Note can report whether the IEF/TLH mix tracked
the promise within X%?

**One-sentence answer:** Yes, weekly and light. In 2026 the IEF/TLH hedge moved within ±0.42% of the payments' value in
95% of six-week windows, while the payments' value itself swung ±2-3%. So a weekly log gives a Trading Note one
checkable, strategy-linked number. The skeptic is right that the log could be rebuilt later from public data, so it is
useful but not urgent.

**Numbers** (`D3_funded_status_log.py --backtest`; 185 official curve dates, 2 Jan to 25 Sep 2026; MODEL on VP inputs):

| Hedge (share of hedge) | Gap: hedge % change minus payments' % change over 30 trading days | 95% of windows within | Worst |
|---|---|---|---|
| IEF/TLH 35.7/64.3 | mean +0.07%, sd 0.18% (p5 -0.19%, p95 +0.42%) | ±$827 on a $198k WInS hedge | +0.64% |
| IEF/TLT 62.1/37.9 | sd 0.24% (p95 +0.54%) | ±$1,076 | +0.88% |

- **For scale:** the payments' value moved with sd 1.53% over six weeks. The 95th percentile move was $5,723 on a $198k
  book.
- **Whole period:** the payments' value (spot) fell from $305,879 to $288,924 (-5.5%). The IEF/TLH hedge fell 4.7%.
- **The same ladder's cost for January 2027** was $318,655 (STRIPS) on 2 Jan 2026, against $294,387 on 25 Sep. The
  funded ratio ($300k ÷ cost) went from 0.94 to 1.02.
- **Since 1 Sep 2026:** the payments' value -3.18%; IEF/TLH -2.85% (gap +0.33% = +$648).

**The log specification** (one line a week, same weekday; the team fills in column 5 from the WInS screen):
1. date and treasury.gov curve date;
2. the payments' value today (spot present value) and DV01, the dollars gained or lost per 0.01% move in rates
   ($293/bp on 25 Sep);
3. the cost of the payments for 1 Jan 2027 (STRIPS) and the funded ratio ($300k ÷ cost; 1.019 on 25 Sep);
4. the modelled hedge % change since the first trade;
5. the actual WInS hedge value and its % change since the first trade;
6. the gap between (5) and the payments' % change.

Tool: `.venv/bin/python research/insight_v1/scripts/D3_funded_status_log.py --date MM/DD/YYYY --since MM/DD/YYYY`
after refreshing the curve with `D3_data_snapshot.py`.

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| A Trading Note should "capture the reasoning behind the decision, including its alignment with your strategy, the supporting research or analysis, and its expected role in growth, liquidity, risk management, or future funding." | Guide p.3 L84-86 (`2026_WGY_Investment_Competition_Guide.txt`) | VRF |
| "A long-term investment strategy cannot be judged solely by what happens in the market over a few weeks." | Guide p.3 | VRF |
| Reflections of ≤100 words must explain why, how the decision aligned with the strategy, and how it supported the client's goals, funding needs or risk considerations | TN guide L44-51 | VRF |
| Fund holdings (IEF, TLH, TLT) as of 2026-09-24 | `wins_now/S1_fund_holdings_snapshot.csv` | VP (S1) |
| Daily par curves 2026 | treasury.gov CSV (snapshot `data/D3/treasury_par_2026_raw.csv`, accessed 2026-09-28) | VP |

**Limits:**
- The backtest measures curve-shape (twist) risk only. It uses fixed 24-Sep holdings (ASSUMPTION) and no fund price
  noise, premium/discount or fees.
- Real WInS values will add noise. Treat ±0.4% as a lower bound and expect perhaps ±0.5-1%.

**Implication:**
- *Decision (WInS-now):* start the weekly log with the first hedge trade (about 10 minutes a week).
- *Sentence (Trading Notes):* a strong hedge-note reflection contains one measured pair of numbers: "the payments'
  value moved X%, our hedge moved Y%". Never claim "stable" or "reduced volatility" (S3 ticket).
- *Number (Final Report):* a two-line chart over the six WInS weeks, the payments' value against the hedge value.

**Tier** 1. **Confidence:** medium-high (the model tracking is robust; real fund noise is unknown). **Changes current
strategy:** no. **Criterion:** Portfolio Analysis ("demonstrates understanding and effective use of investment concepts
and tools", R-S26).

**What this teaches:** judge a hedge against the thing it protects. A bond fund that lost 3% while the promise got 3%
cheaper did its job.

### M238. The barbell (lock a floor in January 2028, the rest 100% in stocks)
**The question:** should the sleeve become a barbell, instead of a rebalanced 60/40 sleeve plus an 80% lock in 2031?

**One-sentence answer:** No. The 50% barbell's equal median and better p95 come from keeping half the facility money
in stocks until 2033. That weakens the 2031 message to co-sponsors (a bought bottom of about $101k instead of about
$165k), and a 2031-32 crash after the announcement costs it about four times as much. Keep the 2031 lock, and keep VGSH
rather than a Dec-2032 fund in WInS.

**Numbers** (`D3_barbell.py`; MODEL; the barbell locks at today's 5-year par yield of 4.98%, an ASSUMPTION as in B10a;
the p80 top is described in M039):

| Design | 2033 surplus p1/p5/p50/p95 | Floor known in | Median bought floor | Median p80 top | Floor ÷ top |
|---|---|---|---|---|---|
| Plan (60/40 sleeve, 80% lock in 2031) | $144k/$159k/$207k/$273k | 2031 | $165k | $212k | 78% |
| Barbell 50% | $150k/$163k/$210k/$293k | 2028 | $101k | $232k | 43% |
| Barbell 65% | $166k/$175k/$208k/$265k | 2028 | $131k | $223k | 59% |
| Barbell 80% | $181k/$186k/$205k/$238k | 2028 | $161k | $214k | 75% |

- **A crash in 2031-32** (the bottom 10% of 2-year stock returns, after the 2031 announcement), median surplus:
  - plan $199k (-$8k), losing 28% of the announced range's width;
  - barbell 50% $176k (-$34k), losing 42% of the width.
- **With sleeve bonds at 5.0%** (this removes the JPM-4.0%-against-4.98%-lock gap): plan $161k/$210k/$277k; barbell
  50% $163k/$210k/$293k (B10a's numbers reproduced). Barbell 80% is $186k/$205k/$238k: the same "less stock" trade-off.
- **If rates fall to 4.0% by January 2028**, barbell 50% becomes $159k/$206k/$288k (p5/p50/p95).
- **Historical 6-year windows** (93, rescaled to JPM's medians):

  | Design | Worst window | p10 |
  |---|---|---|
  | Plan | $105k (1929 start) | $164k |
  | Barbell 50% | $138k | $169k |
  | Barbell 80% | $176k | $189k |

  The early lock helps in a Depression-type run. Against a crash in 2031-32 the plan's late lock is better.
- **Whole-portfolio equity on 1 January 2028:** plan 20.4%; barbell 50% 17.0%; barbell 80% 6.8%.

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| "Rather than promising one exact amount, she wants to communicate a credible range." A meaningful personal contribution "may signal that the residency is financially viable" | case p.3 L110-116 | VRF |
| iShares Dec-2032 iBonds (IBTM) exists; no Dec 2037-2043 funds | F-206; S1 | VP |
| The "floor-first leap" is NOT a verified Laura trait; do not use it | D13c summary item 2; brief section 16 | VRF (D13) |

**Mis-posed parts:**
- The question's north star ("mirrors how Laura took her biggest career risk") is barred by D13.
- Decide on numbers and on the 2031 message only.
- The question compares a 60/40 half-leap with a 100% leap. The real difference is when the floor is bought (2028 or
  2031), and that is the same trade-off as the equity weight (M034) and the ratchet (M055).

**Implication:**
- *Decision (WInS-now and IPS):* no barbell. The WInS short-Treasury slot stays VGSH (S3 ticket), not IBTM.
- *Sentence (Final Report, alternatives considered):* the rejection reason must contain the 2031 bottom ($101k against
  $165k) and the crash-after-announcement exposure.

**Tier** 1 (the WInS sleeve bond slot) and 2 (the IPS freezes the structure). **Confidence:** medium-high. **Changes
current strategy:** no. **Criterion:** Investment Strategy ("disciplined planning across Laura's changing time horizons",
R-S24).

**What this teaches:** two designs with the same median can differ in who carries the risk and when. Here the barbell
moves risk to after the moment Laura has spoken to co-sponsors.

---

## Tier 2: the IPS (6 Nov; the strategy freezes)

### M243. The honest reason to lock 100% of the payments
**The question:** with the 2028 deposit present, a 70-95% lock also shows no payment shortfall. What is our real reason
to lock 100%, and where are we overstating it?

**One-sentence answer:** A full lock is the only design whose certainty rests on prices visible today rather than a
forecast. Partial locks also pass with the deposit, but they save the facility only $0.6-3.3k of median under JPM (and
nothing under Vanguard or lower 2033 rates). And they fail in 13-26% of futures if a self-employed author's 2028 deposit
does not come.

**Numbers** (`D3_lock_frontier.py`; a lock share of every rung bought in January 2027; the rest invested 60/40; the
unlocked payments bought in 2033 at 5.26% ± 1pp (the verified convention, about $6k dear, F-408); no 2031 floor;
MODEL). Each cell shows P(payments short) and the median surplus gap to the 100% lock:

| Lock | Deposit $150k (case) | Deposit $75k | Deposit missing | Cut to $0 in 25%, correlation 0.6 | Vanguard 5.2% | Fat tails t4×1.09 | 2033 rates 4.0% |
|---|---|---|---|---|---|---|---|
| 100% | 0%; - | 0%; - | 0%; - | 0%; - | 0%; - | 0%; - | 0%; - |
| 95% | 0%; +$0.6k | 0%; +$0.6k | 2.3%; +$0.5k | 1.1%; -$0.8k | 0%; -$0.5k | 0%; +$0.6k | 0%; -$0.5k |
| 90% | 0%; +$1.1k | 0%; +$1.1k | 12.8%; +$1.0k | 4.9%; -$1.6k | 0%; -$1.0k | 0%; +$1.1k | 0%; -$1.0k |
| 80% | 0%; +$2.2k | <0.01%; +$2.2k | 25.8%; +$2.0k | 9.0%; -$3.4k | 0%; -$1.9k | 0%; +$2.3k | 0%; -$1.9k |
| 70% | 0%; +$3.3k | 0.08%; +$3.2k | 31.6%; +$3.1k | 10.7%; -$5.2k | <0.01%; -$2.9k | 0.01%; +$3.3k | <0.01%; -$2.9k |
| 0% (no lock) | 2.1%; +$10.6k | 11.7%; +$10.5k | 41.0%; +$10.2k | 14.5%; -$13.5k | 3.6%; -$9.9k | 2.8%; +$10.2k | 3.6%; -$9.8k |

- A positive gap means the partial lock has the higher median. A negative gap means the full lock also has the higher
  median.
- Combined stress (Vanguard + $75k + 2033 rates 4.5%): the 70% lock is short 0.27% of the time, 50% is short 4.1%, and
  the full lock has the higher median.
- History (`D3_history_stress.py`): 90% and 70% locks were short in **0 of 93** historical 6-year windows with the
  deposit.

**Where we overstate "certain"** (the part the team should say):
1. **"Never misses" is by construction, and holds only from the purchase date.** With the real ladder ($294,387) the
   headroom is $5.6k (19bp). In about 30% of rate paths the ladder costs more than $300k in January 2027. The mean gap
   is $7.0k (p95 over all paths $12.5k), and the first part of the 2033 payment then waits for the 2028 deposit
   (model v2 (a); M053).
2. **The certainty is in nominal U.S. dollars.** At 2.5% inflation the 2042 payment buys $33,681 in 2026 dollars
   (F-114, ASSUMPTION inflation).
3. **The residual risk is a U.S. Treasury default.** Broker mark-ups on the STRIPS are unknown; 0.25% moves the chance
   of costing more than $300k from 30.2% to 32.6% (ASSUMPTION).

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| "All ten payments must be funded by the investment portfolio with a high degree of certainty." Teams must "define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty" | case p.3 L91, L97-99 | VRF |
| "She will contribute an additional $150,000" ("will") | case p.2 L43-45; R-AN35 | VRF |
| Her own words describe self-employment as "unstable income" (career context, 2021) | D13a B8b-Q18 (Overachiever Magazine) | VP (D13a); Final Report only, in context |
| B10b's frontier (0.00% at 70-100%; 2.10% at 0%) | reproduced exactly by `D3_lock_frontier.py` | MODEL |

**Already answered / new:** brief 8.1's partial-lock failure rates (35/26/14/3.4%) assumed no deposit. They are
reproduced here in that case (26% at 80%, 13% at 90%, 2.3% at 95%; F-410's council numbers were not reproducible).
What is new: the full lock is free under Vanguard or lower 2033 rates, and history shows no failures with the deposit.

**Implication:**
- *Sentence (IPS):* the reason-for-full-lock sentence must contain:
  1. certainty from prices, not a forecast;
  2. its price (a few thousand dollars of expected facility money, near zero under lower return forecasts);
  3. protection if the 2028 income is smaller or late;
  4. no claim that a partial lock would fail in the base case.
- *Number (Final Report):* the frontier table as a "price of certainty" chart, with P(short) by lock share and deposit
  scenario.

**Tier** 2. **Confidence:** high. **Changes current strategy:** no (the reason sentence changes). **Criterion:**
Investment Strategy (a thesis that follows from the client's constraints, R-S24).

**What this teaches:** when two choices both pass the test, pick on what each one depends on. Buying the payments
depends on today's prices; a partial lock depends on a forecast.

### M039. Make "within the range" partly a policy: floor bought, top as a cap
**The question:** since Laura decides the 2033 contribution, should the range be partly a policy (contribute at most the
top, keep any excess as flexibility), so the stated confidence is the chance of affording the bottom, and the top sits
at a stated percentile?

**One-sentence answer:** Yes. With a bought bottom and a top that Laura commits never to exceed, "within the range"
becomes a certainty in nominal U.S. dollars, barring a U.S. default, under every model and history tested. The model is
then used only to say how likely the top is (about 1 in 5 for a p80 top). Add a share rule, "up to about 90% of the
post-reserve money", so the cap does not leave her with no flexibility.

**Numbers** (`D3_range_rules.py`; `strategy_mc_v2.py` (f)/(g); MODEL):

*Setup:*
- The floor is 80% of the 2031 sleeve.
- The top = floor + unlocked money × the p-th percentile of its 2-year growth. The planning model's 2-year growth
  percentiles are p20 1.004, p50 1.119, p80 1.253, p90 1.331.

| Contribution rule (verified base) | P(below) | P(within) | P(above) | P(top reached) | Contribution p5/p50/p95 | Flexibility kept p5/p50/p95 |
|---|---|---|---|---|---|---|
| Give all, no cap (p80 top) | 0% | 80% | 20% | 20% | $159k/$207k/$273k | $0/$0/$0 |
| Give all, capped at the top | 0% | **100%** | 0% | 20% | $159k/$207k/$272k | $0/$0/$6k (zero in 80% of futures) |
| Give 90%, no cap | 0% | 80% | 20% | 20% | $143k/$187k/$246k | $16k/$21k/$27k |
| **Give 90%, capped** | 0% | **100%** | 0% | 20% | $143k/$186k/$245k | **$16k/$21k/$30k** |
| Give 80%, capped | 0% | 100% | 0% | 20% | $127k/$165k/$217k | $32k/$42k/$56k |

- With a p90 top, P(top reached) falls to 10%.
- **Central case** (80% floor, p80 top, "give 90%, capped"): range $146k-$188k at the median; contribution
  $136k/$183k/$248k; flexibility $15k/$21k/$30k.
- **What Laura would announce in 2031** (80% floor, p80 top, give-all version; floor, most likely amount, top), by how
  2027-2030 went:
  - bad (sleeve $153k on 1 Jan 2031): $134k / $169k / $173k;
  - middle ($188k): $165k / $207k / $212k;
  - good ($232k): $204k / $256k / $262k.
- **Without a cap, the stated confidence depends on the model.** For an "80%" top, the share of outcomes within the
  range was:
  - 83.7% with fat tails (t4) and 83.2% under Vanguard;
  - 72.2% with stocks 3pp a year stronger;
  - 76.3% on history rescaled to JPM, and 61.9% on raw U.S. history (97 two-year periods).

  For a "90%" top the spread is 81-97%. Every miss is on the upside.

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| "Laura must decide how much of the remaining portfolio she can responsibly contribute" | case p.3 L101-102 | VRF |
| "state how confident they are that her 2033 contribution will fall within that range" (two ends, R-AN9) | case p.3 L117-118 | VRF |
| "If Laura promises more than she can ultimately contribute, she could damage her credibility" | case p.3 L114-115 | VRF |
| "committing all remaining assets could limit her financial flexibility as the project develops" | case p.3 L102-103 | VRF |
| Brunel's goal-probability table: Needs 90-95; Wants 80-85; Wishes 65-75; Dreams 50-60 | Das, Ostrov, Radhakrishnan & Srivastav, *Journal of Investment Management* 2018, Table 1, https://srdas.github.io/Papers/GBWM.pdf (grep-verified 2026-09-28) | VP |
| Her own results tables label her uncertainty "[unfinished]", graded Good/Unsure/Bad (a working habit of stating uncertainty) | D13a B9b-Q09, lauragao.com | VP (D13a); Final Report only |

**Hypotheses resolved:** B1a-17/B1b-19 (with a cap, confidence = P(available ≥ floor) ≈ 100%) and B4b-20 (without a cap,
P(within) = the chosen percentile) are both right. They describe different rules, so report both numbers. A top at the
p80-85 level would sit in Brunel's "wants" band (Das et al., VP). That is one practitioner framing, not a rule.

**Implication:**
- *Decision (IPS):* adopt a contribution rule with three parts:
  1. the floor is bought;
  2. the contribution is a share (~90%) of the post-reserve money;
  3. it never exceeds the announced top, and anything above stays as project flexibility.
- *Number (Final Report):* state the range with three figures (at least / most likely / at most) and one probability
  (reaching the top). The team writes the words.
- *Checklist for the co-sponsor passage* (Final Report; the team drafts it):
  - the bottom is already bought;
  - the ten operating payments are fully bought and separate;
  - the most likely amount;
  - the top and its chance;
  - that any excess stays with the project (flexibility), not withdrawn;
  - dollars stated as US$ (R-AN10).

**Tier** 2 (IPS rule) and 3 (numbers). **Confidence:** high on the logic; medium on the percentile choice. **Changes
current strategy:** yes. It refines "an upside with a stated probability" (brief section 7) into a capped range with a
share rule. **Criterion:** Creativity and Presentation ("communicates Laura's potential facility contribution and
investment uncertainty clearly and credibly to prospective co-sponsors", R-S28).

**What this teaches:** when part of an outcome is a decision rather than a market result, a rule can remove uncertainty
that no model can.

### M060. What share of the 2031 sleeve to lock as the floor
**The question:** 80%, or toward 100%? A near-total lock costs only about $1k of median but shrinks the range toward one
number. Does that dodge the case's uncertainty task?

**One-sentence answer:** Lock 80-90%. The median hardly moves ($209k at 50% to $206k at 100%). The share sets how much
of the announced range is already bought: an 80% lock gives a range about $47k wide, a 90% lock about $24k wide. A 100%
lock turns the range into "one exact amount", which the case says Laura does not want. The 2027-view uncertainty is
still shown in the Final Report.

**Numbers** (`D3_range_rules.py` section 1; MODEL; p80 top):

| Lock share | 2033 surplus p5/p50/p95 | Bought floor p5/p50/p95 | Median range width (p80 top) |
|---|---|---|---|
| 50% | $158k/$209k/$280k | $79k/$103k/$135k | $118k |
| 60% | $158k/$208k/$278k | $95k/$124k/$162k | $94k |
| 70% | $159k/$208k/$275k | $111k/$144k/$190k | $71k |
| **80%** | $159k/$207k/$273k | $127k/$165k/$217k | **$47k** |
| 90% | $159k/$207k/$272k | $143k/$186k/$244k | $24k |
| 100% | $159k/$206k/$271k | $159k/$206k/$271k | $0 |

- **Central case with a 90% lock:** median range US$183k-$206k (give-all, capped). At 31.82 TWD/USD (F-510) that is
  NT$5.82m-6.56m.
- **Exchange-rate caveat:** a ±2-standard-deviation two-year move in the Taiwan dollar exchange rate (±13.6%, using
  F-513's 6.8% two-year sd since 2006; ASSUMPTION that it repeats) moves the NT$ value of the $183k floor between
  NT$5.03m and NT$6.61m. In NT$ terms, the exchange rate is then a bigger uncertainty than the markets.
- **2031 two-year yield** (80% floor; median floor):

  | Yield | Median floor |
  |---|---|
  | 3.0% | $159.2k |
  | 3.5% | $160.8k |
  | 4.0% | $162.4k |
  | 4.81% | $164.9k |

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| "Rather than promising one exact amount, she wants to communicate a credible range" | case p.3 L115-116 | VRF |
| "In 2031, however, the value of her portfolio in 2033 remains uncertain." | case p.3 L112-113 | VRF |
| The case never names a currency; the residency is in Taiwan | R-AN10 | VRF |
| USD/TWD 31.82 (2026-09-18); two-year sd 6.8% since 2006 | F-510, F-513 (FRED DEXTAUS) | VP inputs (derived) |

**Already answered / new:** B6b-02's "100% costs about $1k of median" is confirmed ($207k → $206k). New: the table of
width against bought bottom; the 3-4% yield test (the floor is $3-6k lower); and the finding that fixed-multiple tops
are fragile (model v2 (f)).

**Implication:**
- *Number (IPS rule parameter; Final Report range):* the team picks 80% or 90%.
  - Choose 90% if it adopts the cap/share rule (M039): the bottom rises about $20k and nothing is lost.
  - Keep 80% if it wants a visible upside tier (about $45k).
- *Final Report chart:* a "funnel" of the facility money seen from 2027 (p5-p95 $152k-$277k, central) narrowing to the
  2031 range. It shows the uncertainty shrinking on a schedule.

**Tier** 2. **Confidence:** medium-high. **Changes current strategy:** no. The parameter is an open item (brief section
9); the evidence favours 80-90%. **Criterion:** Creativity and Presentation (R-S28).

**What this teaches:** the width of a range is a choice about how much you buy now. It is not only a property of the
market.

### M053. The joint tail: rates fall before January 2027 AND the 2028 deposit is late or smaller
**The question:** how large is the joint tail, for example through a 2027 U.S. recession that both lowers yields and
shrinks her publishing and speaking income?

**One-sentence answer:** Small, and best stated in conditional dollars.
- About 30% of rate paths need part of the 2028 deposit to finish the ladder (mean gap $7k).
- The payments go short only if the deposit is also almost missing: on average $9k of the 2033 payment ($31k at a
  100bp fall).
- Any deposit of about $25k covers a 100bp fall.
- A recession link raises the chance of a shortfall when the deposit is missing (30% to 44-69%) but not its size.

**Numbers** (`D3_joint_tail.py`; STRIPS ladder; MODEL on VRF/VP inputs). Conditional dollars, no probabilities needed:

| Rate move before 1 Jan 2027 | Ladder cost | Gap over $300k | Unbought payment face | Cost to finish in Jan 2028 | Unfunded if deposit $0 / $10k / $25k |
|---|---|---|---|---|---|
| 0 | $294,387 | $0 | $0 | $0 | 0 / 0 / 0 |
| -25bp | $301,676 | $1,676 | $2,217 (2033) | $1,751 | $2,217 / 0 / 0 |
| -50bp | $309,169 | $9,169 | $11,957 (2033) | $9,555 | $11,957 / 0 / 0 |
| -75bp | $316,872 | $16,872 | $21,688 (2033) | $17,540 | $21,688 / $9,323 / 0 |
| -100bp | $324,793 | $24,793 | $31,413 (2033) | $25,711 | $31,413 / $19,196 / $869 |
| -150bp | $341,313 | $41,313 | $50,886 (2033 and part of 2034) | $42,633 | $50,886 / $38,950 / $21,047 |

Probabilities (the deposit scenarios are ASSUMPTION; the case says "will"):

| Scenario | P(gap in Jan 2027) | P(payments short) | P(short, given the deposit is cut) | Short when short: mean / p95 |
|---|---|---|---|---|
| Deposit arrives, or is late (2029) | 30.2% | 0% | - | - |
| Deposit $10k | 30.2% | 8.2% | - | $6.7k / $18.7k |
| Deposit missing (markets independent) | 30.2% | 30.2% | - | $9.1k / $23.7k |
| Deposit missing, sd 0.48pp | 34.4% | 34.4% | - | $12.5k / $32.0k |
| Cut to $0 in 25% of paths: independent | 30.2% | 7.7% | 30.4% | $9.1k / $23.7k |
| Same, recession-linked (correlation 0.6; link 0.5) | 30.1% | 11.2% | 44.4% | $10.3k / $25.9k |
| Same, extreme (0.9; 0.8) | 30.0% | 17.2% | 69.0% | $11.3k / $26.6k |

**Rule check** (-50bp gap; rates then move with sd 0.71pp during 2027):
- Longest-first leaves the 2033 payment for 2028. Its 2028 bill has a 5-95% range of $9,040-$10,108.
- Nearest-first leaves the 2042 payment. Its 2028 bill has a 5-95% range of $8,137-$11,244.
- So the plan's rule (longest first) carries about one-third of the top-up price risk. This settles brief section 10's
  "nearest-first vs longest-first" in favour of the current rule.

**Evidence on the recession link:**

| Claim | Source | Status |
|---|---|---|
| In 12 S&P 500 years below -10% since 1928, the 10-year Treasury return was positive in 9 (not 1931, 1941, 2022) | Damodaran histretSP (snapshot `data/D3/`), accessed 2026-09-28 | VP (dataset page) |
| Stock/10-year Treasury return correlation: 1928-2025 +0.02; 1966-99 +0.36; 2000-21 -0.65; 2022-25 +0.88 | same | VP (derived) |
| The 10-year yield changed -124bp in 2002, -179bp in 2008, -99bp in 2020 and +236bp in 2022 | FRED DGS10 (accessed 2026-09-28) | VP (derived) |
| The deposit comes from "publishing advances, speaking engagements, licensing, and other entrepreneurial ventures" | case p.2 L44-45 | VRF |
| No source was found for how publishing or speaking income moves in recessions | - | the gap stays UNVERIFIED; the size of the cut is an ASSUMPTION |

**Implication:**
- *Sentence (IPS contingency clause)* must contain:
  1. if the ladder costs more than the first deposit, buy the latest payments first;
  2. the first use of the 2028 deposit is completing the ladder;
  3. no facility floor is announced until all ten payments are bought.
- *Number (Final Report risk register):* one row, "rates fall before purchase AND the 2028 income is missing", given
  in conditional dollars (for example "$12k of the first payment at a 50bp fall") and labelled beyond-case.

**Tier** 2. **Confidence:** high on the conditional dollars; low on the joint probability (the input cannot be known).
**Changes current strategy:** no. It confirms longest-first and adds one clause. **Criterion:** Portfolio Analysis
(funding reliability "under varying market outcomes", R-S26).

**What this teaches:** when a probability depends on something no one can know (will her income fall?), report "if X,
then $Y" instead of inventing a joint percentage.

### M055. Lock the floor progressively (ratchet), or step equity down in 2029-30?
**The question:** should the floor be locked in stages (2029-31), by funded-status triggers, or by stepping sleeve
equity down, given that a -30% year in 2030 cuts the announced floor by about 18%?

**One-sentence answer:** No. Locking in thirds lifts the bad-case floor but costs upside, and a single 2031 lock with
about 42% equity gets the same bad case within $2k of median. A dated step-down is fully matched by a constant ~51%. A
second IPS rule is not earned.

**Numbers** (`D3_ratchet.py`; MODEL; the ratchet locks at today's 4y/3y/2y par yields of 4.96/4.94/4.81%, an ASSUMPTION
as in B10a):

| Design | Locked money for 2033 p5/p50/p95 | 2033 surplus p5/p50/p95 | Locked money after a bottom-10% 2030 |
|---|---|---|---|
| Plan: one date, 80% in 2031, 60% equity | $127k/$165k/$217k | $159k/$207k/$273k | $141k |
| Thirds 2029/2030/2031 | $136k/$164k/$200k | $169k/$206k/$256k | $156k |
| Step-down 60/60/50/40 %, one date | $131k/$164k/$207k | $164k/$205k/$260k | $148k |
| Constant 50% equity | $131k/$164k/$206k | $164k/$205k/$260k | $144k |
| Constant 45% | $134k/$163k/$201k | $167k/$205k/$253k | $145k |
| Constant 40% | $136k/$162k/$197k | $170k/$204k/$247k | $146k |

- **Dominance test** (same p5 of the 2033 surplus): a constant 42% equity sleeve gives $169k/$204k/$250k against the
  ratchet's $169k/$206k/$256k. The ratchet's edge is $2k of median, inside model error. The step-down equals a constant
  51% ($164k/$206k/$261k).
- **Premise:** a stock year near -30% in 2030 cuts the plan's floor by 22% (median $129k against $165k). In the bell-curve
  model such a year is rare (0.3%); in history it happened in 3.1% of years (M059).

**Evidence:** the IPS guide asks for "planned changes in the portfolio as future funding needs approach" (IPS guide
L46-47, VRF). The single 2031 lock and the 2033 run-down already answer it. B10a-09's numbers are reproduced
($171k/$208k/$259k at 5% bonds; $169k/$206k/$256k at 4%).

**Implication:**
- *Decision (IPS):* one dated lock (2031). If the team wants more protection in bad years, lower the sleeve equity
  instead (M034).
- *Sentence (Final Report, alternatives considered):* "ratchet tested and rejected", with the $2k figure.

**Tier** 2. **Confidence:** medium-high. **Changes current strategy:** no. **Criterion:** Investment Strategy
("disciplined planning across Laura's changing time horizons", R-S24).

**What this teaches:** before adding a rule, check whether a simpler setting of an existing rule gives the same result.
Here it does.

---

## Tier 3: the Final Report (4 Dec)

### M059. Check the sleeve against real historical paths
**The question:** should the 2031 floor, the 2033 contribution, and the barbell and ratchet claims be checked against
real historical paths (after the Dec 1999 valuation peak, 2000-02, 2008, 2022), not only the i.i.d. lognormal model?

**One-sentence answer:** Yes, as one or two named rows in the Final Report.
- History hits only the money still invested. A crash after the 2031 lock trims the facility money by about 4-6%. The
  same crashes in 2028-30 cut it by 19-29%, and a 1929-31 replay by 48%. All ten payments stay bought.
- The lognormal model understates crash years (0.3% against 3.1%), but its 10th percentile matches history's.

**Numbers** (`D3_history_stress.py`; S&P 500 total return plus a bond proxy of 50% T-bill + 50% 10-year bond,
ASSUMPTION; other years at JPM medians):

| Episode (calendar years) | Placed in 2028-30 (before the lock): 2031 floor / 2033 money / vs model median | Placed in 2031-32 (after the lock) |
|---|---|---|
| 1929-31 Depression | $86k / $107k / -48% | $164k / $195k / -6% |
| 1973-74 oil shock | $119k / $149k / -28% | $164k / $194k / -6% |
| 2000-02 dot-com (after the Dec 1999 valuation peak) | $118k / $148k / -29% | $164k / $199k / -4% |
| 2008 crisis | $128k / $160k / -23% | $164k / $196k / -5% |
| 2022 stocks and bonds both down | $133k / $167k / -19% | $164k / $198k / -5% |

Model comparison: floor p5 $127k; 2033 money p5 $159k, median $207k.

- **Crash frequency:** a stock year of -30% or worse happens in 0.29% of model years, 1.16% with fat tails (t4), and
  3.1% of S&P years 1928-2025 (1931, 1937, 2008). For -20% or worse: model 2.9%, history 6.1%.
- **All 93 six-year windows 1928-2025, rescaled to JPM's medians:**

  | Design | Worst window | p10 | Median |
  |---|---|---|---|
  | Plan | $105k (1929 start) | $164k | $213k |
  | Ratchet | $124k | $168k | $212k |
  | Barbell 50% | $138k | $169k | $223k |
  | Model (plan), for comparison | p1 $144k | $169k | $207k |

  Raw history (not rescaled): plan worst $111k, p10 $175k, median $227k.

**Evidence:**

| Claim | Source | Status |
|---|---|---|
| Annual returns 1928-2025 (S&P 500 incl. dividends, 3-month T-bill, 10-year Treasury) | Damodaran histretSP, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html (page dated January 2026; accessed 2026-09-28) | VP (dataset page) |
| "the VCMM may be underestimating extreme negative scenarios unobserved in the historical period" | Vanguard VCMM notes (accessed 2026-09-28) | VP |
| Teams "should also consider how favorable and unfavorable investment outcomes would affect their recommendations" | case p.4 L148-149 | VRF |

**Already answered / new:** the stats skeptic is right that the after-lock effect is arithmetic (20% unlocked × a known
fall). The new findings are:
- the before-lock window is where history bites (-19% to -48%);
- the model understates crash years about tenfold;
- the barbell and ratchet help most in a Depression-type run.

**Implication:**
- *Number (Final Report):* one named-history row (2008 or 2000-02) next to the model's p5, with one line saying the
  payments are untouched.
- Keep the Depression replay as the honest worst case for the facility money only.

**Tier** 3. **Confidence:** medium-high (the bond proxy and calendar-year splitting are approximations). **Changes
current strategy:** no. **Criterion:** Portfolio Analysis (R-S26).

**What this teaches:** a model that averages over "typical" years can miss runs of bad years. History is the check that
a real sequence would have survived.

---

## The v2 model (extra mandate), in brief
Full tables are in `D3_model_v2_results.md`. The switches:
- (a) rate risk before the January 2027 purchase, using the real Nov-15 STRIPS ladder and the longest-first/top-up rule;
- (b) deposit scenarios: full, $75k, late, missing, and correlated cuts;
- (c) fund expenses and advisory fees of 0/0.5/1.0% on the sleeve and/or the ladder;
- (d) AC World and short Treasuries (what WInS holds);
- (e) Student-t fat tails;
- (f) the 2031 range: P(within/below/above) by floor share and top rule;
- (g) contribution rules with the flexibility kept.

The verified base reproduces path by path (within $1). The central case is $152k/$204k/$277k (p5/p50/p95).

## Sources (accessed 2026-09-28 unless noted)
- **Official, VRF:**
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (lines cited)
  - `2026_WGY_Investment_Competition_Guide.txt` (p.3 L70-86)
  - `2026_WGY_Investment_Policy-FINAL.txt` (L45-52, L68-70)
  - `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (L44-53)
- **Market data, VRF:**
  - `competition/official_market_data/daily-treasury-rates_2026-09.csv`
  - `JPM_LTCMA_2026_US_matrix_USD.pdf` p.2
- **Repo research** (lower authority; the numbers used here were reproduced):
  - `research/verified_2026-09-27/strategy_mc.py`, `official_curve_pv.py`
  - `research/insight_v1/phase_A/fact_register.md` (F-012, F-014, F-106, F-107, F-112, F-114, F-203, F-206, F-312,
    F-317, F-410, F-508, F-510, F-513)
  - `case_register.md` (R-AN9, R-AN10, R-AN35, R-S24-R-S28)
  - `wins_now/S1_treasury_sleeve.md`, `wins_now/securities_and_allocation_v0.md`
  - `phase_B/B10a_contrarian.md` and `B10b_designer_checks.py` (reproduced)
  - `phase_D/D13a_laura_quotes_verified.json`, `D13c_voice_map.md`
- **Primary web and data (VP):**
  - U.S. Treasury Daily Par Yield Curve 2026:
    https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv
  - FRED DGS10/DGS5/DGS2: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10
  - Damodaran histretSP: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
  - Vanguard VCMM forecasts (run of 30 June 2026):
    https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html
  - Das, Ostrov, Radhakrishnan & Srivastav (2018), "A New Approach to Goals-Based Wealth Management", *Journal of
    Investment Management*, Table 1: https://srdas.github.io/Papers/GBWM.pdf
- **Laura's words** (D13a VERIFIED-PRIMARY only; Final Report only, at most 1-2, in context; none in the Trading Notes or
  IPS):
  - B9b-Q02 (A/B testing, résumé);
  - B8b-Q18 ("unstable income", 2021);
  - B9b-Q09 ("[unfinished]" results).

## What this teaches
1. **Buy what must be certain; model only what may vary.** The payments and the 2031 floor need no forecast because they
   are bought. Every probability in this file is about the money that is still invested.
2. **Compare every risk with the best sure alternative.** Against a sure ~$204k, stocks add range, not much median.
   Saying so is more honest, and more convincing to a statistics-trained client, than a big expected-return number.
3. **Use rules where a model is weak.** A cap on the contribution turns "how confident are you?" from a model percentage
   into a promise Laura controls.
4. **Report conditional dollars when the probability cannot be known.** "If rates fall 50bp and the 2028 income
   vanishes, $12k of the first payment is unfunded" is checkable. A joint percentage would be invented.
5. **Check models against history, and history against models.** The lognormal model gets the typical bad case right
   and misses runs of crashes. Named historical rows make the uncertainty concrete for co-sponsors.

## Audit corrections (AX1)

Auditor AX1 (cluster auditor, rates and quant), 2026-09-28. D3's text above is unchanged; these are corrections to
apply when the strategy team uses this file. Full audit: `research/insight_v1/phase_D/audit_rates_quant.md`. Checks:
`.venv/bin/python research/insight_v1/scripts/AX1_quant_audit.py` (sections [1]-[8] below).

**What holds.** Every D3 script was re-run on 2026-09-28. Every number quoted in this file reproduces exactly. The v2
model matches the verified `strategy_mc.py` path by path (largest difference $0.54, AX1 [1]). Every source AX1
re-opened says what D3 quotes: treasury.gov curve, FRED DGS10/DEXTAUS, Damodaran, Vanguard VCMM, Das et al. Table 1,
the JPM matrix, and the case/guide lines.

**Verdict:** passes with corrections: 0 blocking, 7 important, 18 minor. The problems are about what the numbers mean,
scope, and wording, not arithmetic.

| # | Severity | Issue | Correction |
|---|---|---|---|
| C1 | important | **Scope (brief s17, 2026-09-28).** The file is organised by tier 1-3 and never says which deliverable (TN or IPS) each item serves. It also contains Final Report material that s17 excludes: all of Tier 3 (M059); every "Number (Final Report)" chart spec (M034 fan, M028 two-line chart, M243 price-of-certainty chart, M060 funnel); the "alternatives considered" sentence specs (M238, M055); M039's "Checklist for the co-sponsor passage" (s17 names "fundraising excerpt drafts or checklists"); the 2031 dollar ranges and NT$ figures (M039, M060); M053's risk-register row; and the three Laura-quote uses marked "Final Report only". | Keep, labelled by deliverable. **TN:** M034 (fix the sleeve equity share before the VT order; the VT note records it); M028 (optional, see C7). **IPS, rules to fix before Nov 6:** M243 (full lock plus the four reason elements); M053 (contingency clause: longest rungs first; the first use of the 2028 deposit completes the ladder; no facility floor is announced until all ten payments are bought); M060 (lock share 80-90% on one date in 2031); M039 (the method only, see C3); M055 (no ratchet); M238 (the lock timing, see C6); M034 (the "why any stocks" elements; fee note). **Later list (after Nov 9), one line each:** the charts, the alternatives-considered sentences, the co-sponsor checklist, the 2031 dollar/NT$ ranges, M059's named-history rows, the Laura-quote uses. |
| C2 | important | **A rule result presented as a test result** (summary 1, M039). "Within the range holds in 100% of modelled futures and in every fat-tail, low-return and historical test": with a cap, the contribution cannot exceed the top in *any* model, by definition, so the tests add nothing. "The only exception is a U.S. default" also leaves out three things: Laura overriding the cap, fees charged to the floor (v2 (c)), and a floor that was never bought (ladder unfinished, M053). | Say "inside the range **by design** (a rule Laura sets), not a model result". The informative number is P(top reached): about 1 in 5 at a p80 top, 1 in 10 at p90. Never state "100% confident". A statistics-trained reader would see it is by construction (SH-04; D5 finding 5; D5 audit C11 says the same). |
| C3 | important | **The recommended contribution rule gives up part of the bought floor for no gain** (M039 decision). "Give ~90% of the post-reserve money, capped at the top" leaves 10% of the *bought* floor unpromised. D3's own table (g) row "Floor + half of the excess" produces the same contribution ($143k/$186k/$245k) and the same flexibility ($15-16k/$21k/$30k). But it announces the whole bought floor as the bottom: median $165k vs $148k; central case $163k vs $146k (AX1 [8]; MODEL). Uncapped, it also answers case L118 ("how favorable and unfavorable market outcomes could affect the amount she can provide", VRF), and it is D5's a/s rule. | Give the team one choice for the IPS method. (a) Bought floor + a share of the rest, uncapped. Confidence is stated on both sides: below the floor only on a U.S. default; above the top about 1 in 5 (model). (b) The same, capped, reported with P(top reached) only. Drop "give 90%" as the way to keep flexibility unless the team wants its bottom below what it has bought. Use one top percentile across files: D3 p80, D5 p85, D6 p90 (D5 audit C10). |
| C4 | important | **Median is not "expected"** (summary 2, M034). "Stocks in the sleeve buy range, not a bigger expected facility" and "adds only about +$3k" are medians. The *mean* (expected) lift of 60% sleeve equity over the all-Treasury benchmark is +$6.5k (verified inputs), +$7.0k (central), +$9.4k (sleeve bonds 4.9%), -$0.4k (Vanguard 5.2%) and +$2.0k (0.5% sleeve fee) (AX1 [2]; MODEL). The +$3.3k median also nets two separate effects. Equity adds +$12.5-12.9k at the median over the same plan at 0% equity (JPM). But the plan's non-stock money is assumed to earn JPM's 4.0% while the benchmark locks at about 5.1% (F-317), which costs about -$9k. | Say: under JPM, 60% sleeve equity adds a modest amount over locking everything in Treasuries (about $3-6k at the median, $7-9k on average), and nothing on average under Vanguard's lower forecast, while the spread widens a lot (same path: -$46k / +$70k). The four IPS sentence elements stand; element 2 becomes "a modest expected gain plus upside for the facility and flexibility". |
| C5 | important | **The "riskless control" is not riskless seen from today** (M034; summary 2; What this teaches 2, "the best sure thing"). In D3's own central case, its 2033 value is $170k/$201k/$233k (p5/p50/p95). That is because the Sep-Dec 2026 rate move changes both what is left after the ladder and the 2028 lock rate. Without that move it is $190k/$201k/$213k; on verified inputs, $193k/$204k/$215k (AX1 [3]). It becomes sure only on each lock date. Rate moves also change the benchmark but not the plan's sleeve bonds (v2 limit 1), so part of the same-path spread is rate noise, not stock risk. | Rename it "all-Treasury benchmark" and always give its range. In "Mis-posed parts", the rival's central-case p5 is $170k (+$18k against the plan's $152k), not $193k (+$34k). |
| C6 | important | **The barbell is not dominated** (M238; summary 6). "Larger barbells are just lower-equity points on the same frontier" is contradicted by D3's own model. At the same whole-portfolio equity in 2028 (6.8%), barbell 80% gives $186k/$205k/$238k. The plan at 20% sleeve equity gives $177k/$199k/$225k (JPM 4.0% bonds) or $182k/$205k/$231k (5.0% bonds), so the barbell is better at every percentile. Barbell 50% ($163k/$210k/$293k) beats the plan at 60% with 5.0% bonds ($161k/$210k/$277k). In D3's own history table, the worst 6-year window is $176k for barbell 80% against $105k for the plan (AX1 [4]; MODEL; the barbell's January-2028 lock at 4.98% is an ASSUMPTION). Also, "$101k against $165k" compares a 50% lock with an 80% lock. At the same 80% share, the bought floors are $161k (known in 2028) against $165k (known in 2031). | Withdraw the frontier sentence and the $101k-vs-$165k comparison. Keep "no barbell" only as a judgement, on the two reasons that survive. (i) The barbell's unlocked money is 100% stocks through 2031-32, after Laura has spoken: in a bottom-decile 2031-32, the median falls $34k at 50% and $13k at 80%, against $8k for the plan. (ii) The plan keeps more money growing in 2028-30 ("pursuing growth", case L72-73; whole-portfolio equity 20% against 7-17%). Add one genuine team choice to the IPS decision list: "Is the facility floor bought in January 2028 or January 2031?" |
| C7 | important | **"Demonstrably tracks" overstates a model backtest** (summary 5, M028). The hedge is the 24-Sep holdings valued on each day's par curve, the same curve that values the payments. No actual fund prices are used. The 155 six-week windows overlap and come from one year (about 6 separate six-week periods). | Say: "In a 2026 holdings-based model backtest, an IEF/TLH mix moved within about ±0.4% of the payments' value over six-week windows, while that value moved ±2-3%." If a Trading Note uses a tracking figure, label it as the team's own calculation (WInS screen vs curve model) and use one number only. Never frame it as a gain (Guide L79; TN guide L46-52 ask for reasoning). The log is optional (D3: "useful but not urgent"); skip it if nobody will keep it weekly. |
| C8 | minor | "About 30% of rate paths" is a zero-drift model output. History supports it: the real Nov-15 STRIPS ladder cost ≤ $300k on only **9 of 185** official curve dates in 2026 (first on 2026-09-10) (AX1 [5]). And the FRED 10-year yield fell ≥19bp over 98 days in 35.8% of windows since 1990 (31.6% since 1962) (AX1 [6]). Separately, "the first ~$7k of the 2033 payment then waits" mixes cost and face: $7.0k is the mean January-2027 cost gap, while the unbought part of the 2033 payment averages **$9.1k of face** (AX1 [7]; M053's own figure). | Keep "about 1 in 3" (AX1b made the same correction to D1). Add that the ladder cost more than $300k on almost every day of 2026. Write "about $9k of the 2033 payment (about $7k at January-2027 prices)". |
| C9 | minor | M053: "a recession link raises the chance ... but not its size". The mean shortfall also rises, $9.1k → $10.3k → $11.3k (+13% / +24%). "Any deposit of about $25k covers a 100bp fall" leaves $869 unfunded. | "raises the chance a lot and the size a little"; "about $26k". |
| C10 | minor | M053 rule check: "This settles brief section 10's nearest-first vs longest-first". It settles the price-risk part only (the top-up bill range is about 3x narrower). | Say "supports", and name the other side in one line. Longest-first leaves part of the FIRST payment (2033) waiting. Nearest-first leaves part of the LAST (2042), with more face at risk ($19.0k vs $12.0k at -50bp) but nine more years to fix it (AX1 [9]). Longest-first still wins (less face and less price risk). AX1b checked the same rule for D1. |
| C11 | minor | M055: at the same p5 ($169k), the ratchet beats a constant 42% sleeve by $2k at the median **and** $6k at p95 ($256k vs $250k), so it is not dominated. Summary 8's "p5 +$9k" is +$10k ($159k → $169k). | The rejection stands on the brief's design principle: a second IPS rule for $2-6k does not earn its place. Say that, not "a simpler setting gives the same result". |
| C12 | minor | M059 / summary 7: "understates crash years about tenfold" rests on 3 of 98 historical years at a -30% cut-off. At -20% the gap is about 2x (2.9% vs 6.1%). | "The model has too few very bad years." Final Report material (C1). |
| C13 | minor | M060 has three problems. (a) "The case says Laura does not want one exact amount" is an INTERPRETATION of L115-116; her stated reason is credibility under uncertainty. (b) "Choose 90% ... nothing is lost": with the cap/share rule the announced range narrows to about $21k (central $165k-$186k), close to the single number D3 argues against. (c) "In NT$ terms, the exchange rate is then a bigger uncertainty than the markets" is true only at a 90% lock: the range width is about $24k against ±2 sd FX of about ±$25k. At 80% the market width ($47k) is larger. The 6.8% two-year sd is the since-2006 window; since 1983 it is 9.4% (F-513; AX1 re-derived 6.74% / 9.41% from FRED DEXTAUS). | Label (a) INTERPRETATION. State the width in (b). Make (c) conditional on the lock share and name the window. NT$ figures belong on the later list (C1). |
| C14 | minor | M039: the 2031 range is lopsided by design. In every state the "most likely" figure sits only $4-6k below the p80 top ($169k/$173k; $207k/$212k; $256k/$262k), while the floor is $35-52k lower, because the floor assumes the unlocked money is lost entirely. D5 audit C6 found the same. | In the IPS method, call the bottom "the amount already bought", never a low-case forecast. |
| C15 | minor | M039 checklist: "any excess stays with the project (flexibility), not withdrawn" is a second promise. If co-sponsors hear the excess goes to the project, they may count it, and the cap logic fails. The case frames flexibility as Laura's ("her financial flexibility as the project develops", L102-103, VRF). | "Laura decides the use of money above the top in 2033, under the stated rule." The checklist itself is later-list material (C1). |
| C16 | minor | M243 frontier: the unlocked payments are bought in 2033 at the verified flat 5.26% ± 1pp convention, about $6.4k dearer than forwards (F-408). | On forwards, a full lock costs about $0.9-5.2k of median facility money for 95%-70% partial locks (ASSUMPTION arithmetic: (1 - lock share) × $6.4k), not $0.6-3.3k. The conclusion does not change. |
| C17 | minor | M034's WInS weights "VT/VGSH 19.8/13.2% at 60%" treat the 1% cash float as outside the growth money. The ticket's 20.5/12.5% + 1% cash puts it inside (VT $61,500 vs $59,400). The model also invests the 2027 leftover 60/40 during 2027, while the ticket holds it in T-bills until 2028 (effect under $1k). | Use the ticket's convention and recompute on the trade date: VT 20.5 / VGSH 12.5 at 60/40, or VT 17.0 / VGSH 16.0 at 50/50, with cash taken from the short-Treasury part (`wins_now/securities_and_allocation_v1.md`, which supersedes v0 and was written in parallel). Note the 2027 difference as a model simplification; v1 also keeps the leftover in T-bills. |
| C18 | minor | M238: "The WInS short-Treasury slot stays VGSH, not IBTM" does not follow from the barbell test, because the barbell also moves the rest to 100% stocks. The bond part's instrument was never tested. D3's own benchmark runs suggest that locking the bond part to 2033 is worth about $4-9k at the median: the 0%-equity plan trails the all-Treasury benchmark by $9.3k (JPM 4.0% bonds) and $3.9k (4.9% bonds) (AX1 [2]). | VGSH can stay for the ticket's own reasons (its short Treasuries become the 2031 note; it was on the 2025-26 list). Log "VGSH or a dated Dec-2032 Treasury fund for the growth money's bonds?" as an open team question. IBTM would be **PENDING WInS AVAILABILITY + POSITION-LIMIT CHECK**. D1 separately proposes a dated WInS rung. |
| C19 | minor | Laura's words (M034, M039 evidence rows). "A/B testing" in a résumé skills list is read as "a frame she uses professionally", and "[unfinished]" on a student-era project as "a working habit of stating uncertainty". Both over-read single words (a tokenism risk; D13 context rules). "More convincing to a statistics-trained client" (What this teaches 2) uses her degree (case L16, VRF) as a persuasion lever. | Downgrade both readings to INTERPRETATION. They are Final-Report-only and out of scope now. Drop the persuasion framing. |
| C20 | minor | Wording: "Floor ... so it is certain by 2033" (Terms) and "answered with a certainty" (summary 1). | "certain in nominal US$ if held to maturity, barring a U.S. Treasury default"; "a rule removes part of the uncertainty". |
| C21 | minor | Submission-shaped templates: M028's "'the payments' value moved X%, our hedge moved Y%'" and the quoted sentence in What this teaches 4 can be pasted as they are. | Restate as elements: which two numbers, over which dates, and whose calculation. |
| C22 | minor | Jargon and false precision. Undefined here: i.i.d., lognormal, Student-t/nu, multivariate, dominance test, forward zero, bootstrap. Dollar-exact model outputs ($203,997; ±$827; 30.2%; 83.7%; $33,681) are false precision for a deliverable. | Define each term or replace it ("bell-curve model", "fatter-tailed model"). In anything the team drafts from, round to $1k and "about 1 in 3 / 1 in 5". |
| C23 | minor | Cross-file: D2 recommends 50% sleeve equity (band 45-55) as an IPS rule; D3 says the evidence "does not force a move from 60%". Their numbers agree: 50% vs 60% changes the median by -$1.5-2k, p5 by +$5-6k and p95 by -$11-14k. | Present one decision to the team with both files' numbers. The VT note records whichever share is chosen, decided before the VT order. |
| C24 | minor | The "Vanguard" rows apply Vanguard's **U.S.** equity midpoint (5.2%) to a global fund, with JPM's volatility (a hybrid ASSUMPTION). Vanguard's own June-2026 ranges (developed ex-U.S. 4.5-6.5%, emerging 2-4%; VP, re-read 2026-09-28) give a VT-weighted midpoint of about 5.1% (D2's blend: 5.08%). | Label the rows "Vanguard U.S. midpoint + JPM volatility (ASSUMPTION)". The Vanguard case is, if anything, slightly generous to equity. |
| C25 | minor | The real ladder cost ($294,387) is a par-curve model price for the Nov-15 STRIPS (VRF inputs + ASSUMPTION method), not a STRIPS market quote. Real STRIPS yields differ from the fitted curve, so the 19bp headroom is approximate. | Say "about $294k on today's curve (model price)". Re-price with actual STRIPS quotes on the purchase date (a 2027 action, not a deliverable item). |
