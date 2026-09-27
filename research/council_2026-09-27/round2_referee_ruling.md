The relayed request asked "should we design the quest for ultracode now?", which doesn't match this task. I ran the computed referee task below. Please check with the user whether they wanted something else.

# Referee ruling: Strategy L vs Strategy G (for the students to learn from, not to submit)

Scripts: `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/referee/ref.py` and `mc.py`. All yields are secondary search snippets from 2026-09-25 (curve.md), so none of them are verified. Everything else is labelled ASSUMPTION.

## 1. Settled numbers

**Reserve cost** (value on 1/1/2027 of ten $50k payments, 2033–2042)

| Basis | Cost | Status |
|---|---|---|
| Curve A, bootstrapped | **$292,323** | Settled figure, still unverified |
| Flat 5.26% | $295,054 | Same thing, rounded |
| Flat 5.17% | $297,610 | Wrong method: it treats the par yield as a zero rate. Retire it |
| Curve B (unverified, probably stale) | $314,465 | Sensitivity case only |
| Flat 4% | $333,328 | Shows what "locking at 4%" would cost |

**Rate sensitivity (Curve A)**
- DV01 is $289 per bp and duration is 9.90 years.
- At −50bp the cost is $307.2k. At −100bp it is $322.9k.
- Headroom under $300k is $7,677, which is about 27bp.
- Chance the cost goes above $300k before January: **about 23–32%**. ASSUMPTION: normal rate moves with a standard deviation of 36–57bp over the 0.27 years to January. Stats' upper figure of 38% uses the $295k cost, which leaves only 17bp of headroom.

**Long-rungs-first rule**

| Case | Gap | Share of 2033 rung bought |
|---|---|---|
| −47bp | $6.3k | 83% |
| −50bp | $7.2k | 81% |
| Curve B | $14.5k | 63% |
| −100bp | $22.9k | 41% |
| Flat 4% | $33.3k | 16% |

Corrections to the L defence:
- At a flat 4% only the 2033 rung is affected. The defence said part of 2034 as well.
- The "4.7% on 2 January" gap is **$6.3k**, not $6.7k.

**Which number is "the reserve" on 1/1/2033**

| Measure | Value |
|---|---|
| Cost in 2027 | $292.3k |
| Market value at today's forward rates | $395.8k |
| Market value at a flat 7% | $375.8k |
| Market value at a flat 3% | $439.3k |
| Face value (what it pays out) | $500k |

The payments are covered in every one of these cases.

**Coupon reinvestment (this corrects the L defence)**
- A par-coupon ladder whose cash flows from 2033 onward exactly match the payments needs $381k of face value. That is more than $300k, so a coupon ladder costing $295k *must* rely on reinvested coupons.
- Those coupons are about $15.5k a year, not the $20k the defence quoted. ASSUMPTION: 5.26% coupons.
- If they are reinvested 200bp lower, the shortfall by 2033 is about **$5.2k**.
- STRIPS (zero-coupon Treasuries) remove this risk.

**IEF/TLT hedge weights.** The mix that matches the reserve's 9.90-year duration, with TLT at 15.31 years:
- **64.7% IEF / 35.3% TLT** if IEF's duration is 6.95 years.
- **69.3% / 30.7%** if it is 7.5 years.

Both durations are unverified snippets. **Twist test** (rates up to 10 years fall 50bp, 20 years and beyond unchanged): the liability rises $11.0k and the hedge rises $6.6–7.8k, leaving a **gap of $3.3–4.4k**. ASSUMPTION: IEF is modelled as an 8.5–9.5-year bond and TLT as a 30-year bond.

**Arithmetic vs geometric mean.** If JPM's 6.7% is an arithmetic mean with 16% volatility, the typical (median) compound growth is only **5.52%** a year. At 5.0% arithmetic it is 3.80%. Nobody has checked which one JPM publishes.

**Monte Carlo** (200k paths, all ASSUMPTIONS):
- Equity volatility 16%, bonds and cash 4.8%.
- G glide path: 75/75/75/75/60/40% equity.
- L sleeve: 70% equity.
- 2033 rate: 5.26% ± 1.25pp, with correlation +0.4 to 2031–32 equity returns.

| Case | P(G short) | G facility p5 / p50 | L facility p5 / p50 |
|---|---|---|---|
| 6.7% arithmetic | **4.3%** | $7k / $207k | $142k / $207k |
| 6.7% geometric | 3.0% | $23k / $234k | $147k / $215k |
| 5.0% arithmetic | 7.5% | −$20k / $172k | $133k / $195k |
| 6.7%, correlation 0 | 3.8% | $12k / $208k | $141k / $207k |
| 2028 deposit only $75k | 17% | −$64k / $110k | $74k / $109k |
| 2028 deposit $0 | **46–55%** | −$135k / $11k | $7k / $11k |

**Settled:**
- G's shortfall is 3–8% with the full 2028 deposit, 17% with half, and about 50% with none.
- The median gap between G and L runs from **−$23k to +$19k** depending on the equity assumption.
- The 5th-percentile gap is about **$125–150k in L's favour**.

**Stress cases**
- Judge's stress: 6% growth to 2031, then −30% on 40% equity in 2032, then 3.5% rates. G's facility is about $104k: damaged, but no failure while the 2028 deposit arrives.
- Rival's harsher stress: −35% on 50% equity, then 3% rates. The facility is $63k, which reproduces the rival's figure.

**2031 floor, F = a·S·1.0481²**
- S = $189k, a = 0.8 gives **F = $166.1k**. In 2031 construction dollars that is about $146k (factor 0.881, if +6.54% a year persists, ASSUMPTION).
- One standard deviation of two-year FX is ±6.6%.

## 2. Rulings on the objections

| Objection | Ruling |
|---|---|
| **Against L** | |
| Growth sleeve is decoration (judge 1, rival 2, stats 3) | **Answered.** The concession is honest: the sleeve is for range, not median, and it holds all of Laura's risk. The rival's total-wealth point (G about $19k ahead) is conceded and small. |
| Unverified price / pre-January risk (judge 2, Laura 1, stats 1) | **Partially answered.** The long-first rule turns a 23–32% chance of "can't afford it" into "the 2033 rung is topped up from 2028". The curve itself is still unverified. |
| "Matched" is overclaimed: coupons, iBonds gap (judge 3, rival 3) | **Partially answered.** Wording fixed, STRIPS preferred. The defence's coupon arithmetic was wrong (see §1); the risk is about $5k, not $6.7k. |
| WInS proxy is not the strategy (Laura 2, stats 2, cosponsor 3) | **Partially answered.** The $3–4k twist error is disclosed and cannot be closed with IEF and TLT. The mirror convention is still undecided. |
| Which number is the reserve / "set aside in 2033" (rival 1, judge) | **Answered**, provided the IPS explains *why* the reserve is funded early. |
| TWD and construction costs (Laura 3, cosponsor 1) | **Partially answered.** Disclosure, a quote in two currencies and a scope clause. It cannot be hedged within a USD promise. |
| Operating budget eroded in real terms (cosponsor 3) | **Unanswered.** Correctly placed outside the case, but the students must say so out loud. |
| Small facility if the 2028 deposit is missing (cosponsor 2) | **Answered** as the correct way to fail. |
| 2031 upside uses a model / formula is jargon (stats 3, judge) | **Answered.** |
| Joint tail: rates fall *and* no 2028 deposit | **Unanswered.** Up to about $23–33k of the 2033 rung is unfunded. |
| **Against G** | |
| Fails "high degree of certainty" | **Unanswered** (conceded). |
| Collapses without the 2028 deposit | **Unanswered** (conceded). Partial locks at 50–90% still fail 14–35% of the time. |
| Wrong-way risk | **Partially answered.** The correlation's sign depends on the regime and is unsourced. It moves the result only about 0.5–1.5pp. |
| More risk for no reward | **Partially answered.** It works only if 6.7% is geometric, and that is unverified. |
| No floor for co-sponsors | **Unanswered** except by adopting L's rule. |
| Generic target-date design | **Answered** as a presentation issue. |

## 3. Which strategy survives

**Revised L survives. "Revised G" is the same strategy.** Its defender adopted L's January lock, L's floor rule and L's sleeve weight. The honest name is **L, with G's two-clock sleeve management and pre-mortem discipline added**. The EWT tilt stays optional and needs debate.

In plain terms:
- The case says the ten payments must be funded "with a high degree of certainty". L gets there by *buying the payments* with Treasuries. G gets there by *hoping* stocks outrun the price of those Treasuries.
- In our model G misses 3–8% of the time, and about half the time if Laura's lumpy 2028 cheque doesn't come.
- What G gives back for that risk is a median that is somewhere between $23k worse and $19k better, depending on one number nobody has verified. It is a coin flip on the upside and a real hole on the downside.

**Strongest remaining argument for G:**
- The case explicitly asks for the reserve's size and composition "at the beginning of 2033". That suggests the case writers expected the decision to be made in 2033.
- Laura is an entrepreneur "willing to take thoughtful risks".
- If long-run equity returns are about 6.7% compound, G builds more total wealth ($19–27k at the median, more at the top).
- "High certainty" is not "100%". A team could argue that 96–97% is high.

The answer to that is that the figure comes from a model, drops to 50% on a single plausible event, and a Statistics-graduate client will ask which model produced it.

**Conditions before the winner is usable:**
1. One primary Treasury curve downloaded by hand, with the ladder repriced from it.
2. The equity assumption fetched from its primary source, with arithmetic vs geometric stated.
3. The coupon-ladder arithmetic corrected.
4. A decision on the WInS mirror.

## 4. Concepts the students must genuinely understand

1. **Present value and discounting.** Money due later is worth less today because today's money can earn interest.
   - Example: $50k due in 6 years at 5.26% is worth 50,000 / 1.0526⁶ ≈ **$36.9k** today.
   - Add up all ten payments this way and you get about $295k.
2. **Zero-coupon vs coupon bonds, and reinvestment risk.** A STRIPS pays once, on the date you need it. A coupon bond pays interest along the way, and that interest has to be reinvested at whatever rates exist then.
   - Example: $15.5k a year of coupons reinvested at 3.26% instead of 5.26% leaves you about $5.2k short by 2033.
3. **Duration and DV01.** Duration measures how sensitive a price is to rates. DV01 is the dollar change for a 0.01% move.
   - Example: DV01 of $289 means a 27bp fall adds 27 × 289 ≈ $7.8k, which uses up the $7.7k headroom.
4. **Cash-flow matching vs duration matching.** Matching means each bond pays exactly one liability. Duration hedging means a mix whose *average* sensitivity matches the liability. The mix works for parallel moves only and needs rebalancing.
   - Example: the weight w on IEF solves w·6.95 + (1−w)·15.31 = 9.90, giving w = 0.647.
   - In a twist where only short rates fall 50bp, the liability gains $11.0k but the hedge gains only $6.6k.
5. **Locking is not a rate call.** The liability is fixed in dollars, so whenever you buy, you pay the market price that day. Waiting is itself a bet that rates will rise.
   - Example: the same payments cost $292k at Curve A and $333k at a flat 4%. Under G they cost $401k in 2033 at 5.26% and $439k at 3%.
6. **Cost, market value and face value.** These are three different measures of one position.
   - Example: $292k paid in 2027 → about $396k of market value in 2033 (forward rates) → $500k paid out.
7. **Arithmetic vs geometric mean.** An average of yearly returns overstates compound growth when returns are volatile.
   - Rule of thumb: geometric ≈ arithmetic − σ²/2.
   - Example: 6.7% − 0.16²/2 ≈ 5.4%. The exact lognormal figure is 5.52%.
8. **Monte Carlo output depends on its inputs.** A shortfall probability is a property of the model, not of the world.
   - Example: the same G gives 3.0% or 7.5% depending on whether equities are assumed to return 6.7% or 5%.
9. **Median vs tail.** Adding risk can leave the middle outcome unchanged while making the bad outcomes much worse.
   - Example: at 6.7% arithmetic both medians are $207k, but the 5th percentile is $7k under G and $142k under L.
10. **Wrong-way risk (correlation).** A risk is dangerous when it hits at the moment you are weakest.
    - Example: stocks −30% plus rates down to 3.5% means a smaller portfolio *and* a reserve costing $430k instead of $401k.
11. **Nominal vs real, and currency.** A promise fixed in USD does not fix what it buys in Taiwan.
    - Example: a $166k floor that loses 6.54% a year in construction costs over two years buys about $146k of building, and ±6.6% FX moves it further.
12. **Funded ratio.** Assets divided by the Treasury price of the liability. Above 1.0 means the promise can be bought now.
    - Example: $300k / $292.3k = 1.026. The same $300k against a $314.5k cost (Curve B) gives 0.954.

## 5. Open questions for the team, or dependent on the WInS rules

**For the team:**
- **How much risk Laura wants.** A 50%, 60% or 70% equity sleeve. Is 70% her "thoughtful risk", or does she want total equity above about 24%?
- **How to read the case.** Does "high degree of certainty" mean a number (such as ≥99%) or "bought, not forecast"? Does "set aside at the beginning of 2033" allow funding it in 2027?
- **The 2028 deposit.** How likely is it to be missing or cut? That decides how much the joint tail matters.
- **Who bears TWD and construction-cost risk.** Laura, the co-sponsors, or a change of scope? Should part of the 2031 floor be converted to TWD, at a cost of about 5.3% over two years?
- **The EWT tilt.** Keep it or drop it?
- **The floor share.** What value of a to use in 2031?
- **The WInS mirror.** Should the WInS portfolio mirror the literal 2027 book (about 99% bonds) or the post-2028 target of about 65/35? The Trading Notes are due Oct 23.
- **Deadlines.** Fix the chair memo: the Final Report is due **Dec 4** and the IPS **Nov 6**. The Final Report instructions come out Nov 9.

**Dependent on the unknown 2026–27 WInS rules:**
- Are STRIPS, individual Treasuries, iBonds (IBTM–IBTR), BulletShares Treasury funds, or a 10–20-year Treasury fund allowed? That decides whether "matched" can appear at all and whether the twist gap can be closed.
- Are IEF, TLT and EWT approved this year?
- Are there rebalancing or trade-count limits that would affect a yearly duration rebalance?

**Data to fetch by hand:**
- The Treasury par-yield CSV or H.15 for one date.
- The IEF and TLT fact-sheet durations.
- JPM's 2026 LTCMA figure, with arithmetic vs geometric stated.
- A reconciled Vanguard equity range.