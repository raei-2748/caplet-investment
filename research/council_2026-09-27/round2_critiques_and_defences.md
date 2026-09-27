# Critic: judge

## Judge's cross-examination of Strategies L and G

These notes are for the students to argue over and rewrite in their own words. They are not text for a submission.

**My illustrative model** (`/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/judge_LG.py`) runs 200k paths. Every input is an ASSUMPTION except where noted:
- Equity return: 6.7% (JPM 2026 LTCMA, 2025-10 vintage), with 5.0% as an alternative. Volatility 16%.
- Cash and bonds: 4.8% (2y 4.81%, snippet dated 2026-09-25).
- 2033 reserve rate: 5.26% flat, standard deviation 1.25pp, correlation +0.4 with 2031-32 equity returns (so rates fall when stocks fall).

| | 2033 facility p5 / p50 / p95 (6.7% equity) | P(reserve short) | P(short) with no 2028 deposit |
|---|---|---|---|
| L (ladder $292.3k, sleeve 60%→30% equity) | $153k / $206k / $283k | ~0 (Treasury default only) | ~0, but facility ≈ $11k |
| L sleeve 100% Treasuries | $200k (deterministic) | ~0 | ~0 |
| G (75% equity → 35%, reserve bought 2033) | −$1k / $208k / $534k | 5.1% (7.8% at 5% equity) | 46–55% |

### Strategy L: objections, most damaging first

1. **The growth sleeve is decoration, and I'll ask why it exists.** The 60% equity sleeve adds about $6k to the median facility ($206k vs $200k all-Treasury) and costs about $47k at p5. That matches the council's "+$2–10k median / −$26–29k p5". At 10y 5.17%, the equity premium over the 10-year is +1.5pp on JPM's 6.7% and about 0 on Vanguard's range (three versions, unresolved). If the team can't say why Laura, who is "willing to take thoughtful risks", should hold equity at all, the thesis collapses into "buy bonds". If they can, it must survive the numbers above.
2. **The certainty claim rests on a price nobody has verified, and it looks like a rate call.** Every yield comes from search snippets, and the primary Treasury pages were blocked (curve.md). The conflicting Curve B (10y 4.39%) prices the ladder at $314k, more than the $300k deposit. At DV01 ≈ $289/bp, a fall of about 27bp before January wipes out the $7.7k of headroom. "Lock now while yields are at their highest since 2007" will read as market timing unless the team shows it would lock at 4% too.
3. **"Cash-flow matched" is overclaimed in both the ladder and WInS.**
   - Coupon Treasuries pay coupons from 2027 to 2032 that have to be reinvested. Only STRIPS truly match the payments.
   - The iBonds funds cover only the 2033–2037 payments (IBTM–IBTR). 2038–2042 have no fund.
   - In WInS, a 65/35 IEF/TLT mix is a constant-duration hedge (≈9.9y using the snippet durations) that must be rebalanced. That contradicts the claim that the reserve "self-liquidates, no management needed".
   - The Trading Notes come first (Oct 23), and if they say "matched" they will contradict the IPS.

   Separately, the 2031 formula F = a·S·(1+z₂)² is jargon in a 500-word IPS.

**The question they must answer:** "Your operating reserve in 2033 is $500k face, about $396k market value, and cost about $295k. Which number is 'the reserve', and how did coupons get from 2027 to 2033?"

**What would change my mind:**
- One primary-source curve (Treasury CSV or H.15) with the cost repriced from it.
- An honest statement that the sleeve's purpose is range rather than median, backed by a sourced equity assumption.
- STRIPS, or an explicit coupon-reinvestment rule.
- A facility range in both USD and TWD. Taiwan construction costs are running +6.54% y/y, about 3.2× CPI (snippet, udn, retrieved 2026-09-27).

### Strategy G: objections, most damaging first

1. **It fails the case's own test.** The case says the ten payments must be funded "with a high degree of certainty" and without relying on outside money. G falls short in 5–8% of my paths, and in 3.3–9.3% across the council's four models. If the 2028 $150k never arrives, it falls short in 46–55%. A pension actuary would not call 5% "high certainty", and a Statistics graduate client will ask which model produced that 5%.
2. **Wrong-way risk.** The reserve's cost goes from $401k at 5.26% to $435k at 3.26%. Recessions tend to push equities and rates down together, so the reserve gets more expensive exactly when the portfolio shrinks. Rolling the 2037–42 payments short keeps that exposure alive until 2039. That is roughly the $43k per −200bp that the council's Actuary found and the CIO confirmed within $1k (chair memo).
3. **More risk for no reward, and it's the generic design.** Median facility is $208k for G vs $206k for L, while p5 is −$1k vs +$153k. The 2031 range depends on a p10–p90 portfolio of $415k–$734k and a reserve cost that is still unknown, so Laura can't promise co-sponsors a floor. That risks the credibility the case warns about. The team's own notes list three contradictions (lock timing, risk budget, 4% vs 5.1% rate), and a "75% equity + glide path" is the target-date answer I have read hundreds of times.

**The question they must answer:** "Equities fall 30% in 2032 and the 10-year drops to 3.5%. Which payments go unfunded, and what does Laura tell the co-sponsors she briefed in 2031?"

**What would change my mind:**
- A sourced equity premium of 3pp or more that lifts G's median facility by something like $50k or more.
- A hard funded-ratio trigger that locks the reserve once assets cover its Treasury price.
- Shortfall below a stated tolerance, with the rate-equity correlation included.

That trigger turns G into L.

### Verdict

I back **L**, conditional on fixing objections 1 and 3 in plain language. Its certainty comes from arithmetic that can be checked, not from a model output. It survives a missing 2028 deposit with the payments intact (only the facility shrinks to about $11k), and it makes the co-sponsor floor something already bought rather than a forecast.

L's real risk is presentation, not substance: it can come across as a jargon-heavy "safe bucket plus growth bucket" with a growth sleeve that doesn't matter. G's problems are substantive. It fails the case's "high certainty" requirement and delivers roughly the same median. The students should recompute all of this themselves before deciding.

---

# Critic: laura

# Laura Gao cross-examines Strategy L and Strategy G (analysis for the team to argue over, not text to submit)

My check script is `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/laura_check.py`. It is a simple model and every assumption in it is mine:
- Stock returns are independent year to year.
- Mean stock return is 6.7%, the JPM 2026 long-term assumption quoted in the chair memo, which dates from Oct 2025. I also ran 5.0%.
- Stock volatility is 16%.
- Bonds and cash earn a flat 4.8%, based on the 2-year yield of 4.81% on 2026-09-25 (search snippet).
- Strategy G's glide path is 75/75/75/75/60/40% stocks.
- Strategy L's growth money is 60% stocks.
- Bonds and stocks are not modelled as moving together, and rate paths are not simulated.

## Strategy L ("lock early")

**Objections, worst first**

1. **Your $295k is built on search snippets.** No primary Treasury page was reachable. A second, conflicting curve (Curve B, 10-year at 4.39%) prices the same ladder at $314k (curve.md). Every 1bp costs about $289. A 100bp drop before January pushes the cost to about $326k, above my $300k deposit. So "lock in January" is really "lock at whatever January's rates are". Your headline certainty rests on a number nobody has seen on treasury.gov.
2. **The certainty is only on paper for the portfolio you will actually run.** You define certainty as cash-flow matched and held to maturity. But last season's approved list had no dated Treasury funds. WInS would therefore use IEF+TLT, which is duration matching:
   - It needs rebalancing.
   - It is exposed when short and long rates move differently.
   - The IEF weight comes out between 65% and 69%, depending on which of the two conflicting IEF durations you believe (6.95 or 7.5 years).

   Also, the 2027 portfolio is about 99% bonds, while WInS "mirrors 65/35". A judge will see two different strategies across the deliverables.
3. **It protects dollars. My residency spends Taiwan dollars.** At 2% inflation, the 2042 payment of $50k is worth about $37k in 2027 money. If the Taiwan dollar strengthened by its largest 7-year move on record, one payment's worth of NT$ would cost $58.7k (taiwan.md). Taiwan construction costs are rising 6.54% a year, 3.2 times CPI (snippet). You call it "certain", but it is certain only in nominal US dollars. I built a career on thoughtful risks, and after 2028 only about 20% of my whole portfolio is in stocks (0.6 × 150 / 450). That is hard for me to get excited about.

**The question you must answer:** "What is your ladder cost from one Treasury table on one date that I can open myself? And what does your WInS portfolio do on a day when short and long rates move in opposite directions?"

**What would change my mind:**
- A verified curve.
- Showing me that the extra stock exposure I give up buys spread, not median. My run supports this:

| Mean stock return | L median facility | L p5 | G median | G p5 |
|---|---|---|---|---|
| 6.7% | ~$202k | ~$147k | ~$213k | ~$21k |
| 5.0% | ~$193k | ~$139k | ~$177k | about −$6k |

G's figures use the forward-curve reserve cost of about $396.5k. So G's median gain is at most about $10k, and at 5% it has none. What G gives up is roughly $126k at the 5th percentile, the bad-luck outcome.

## Strategy G ("growth first")

**Objections, worst first**

1. **It fails the case's "high degree of certainty" requirement, even with my full $150k.**

   | Reserve priced in 2033 at | Chance the reserve is short (6.7% mean) | Chance (5.0% mean) |
   |---|---|---|
   | Forward curve | 3.0% | 5.7% |
   | 4% | 5.5% | 9.4% |
   | 3% | 7.8% | 12.7% |

   The council's four models gave 3–9% (chair memo). Case text: "must be funded… with a high degree of certainty". A one-in-ten to one-in-fourteen chance of breaking a promise to a residency is not high certainty.
2. **My income is lumpy, and G bets the promise on it.** The 2028 contribution comes from advances and speaking fees.

   | 2028 contribution | Chance the reserve is short under G | L's median facility |
   |---|---|---|
   | $75k | 14–36% | ~$100k |
   | $0 | 44–69% | ~$7k |

   Under L, a smaller 2028 deposit only shrinks the facility, and the payments stay funded. Under G it threatens the payments themselves.
3. **It asks me to go to co-sponsors in 2031 still carrying stock and rate risk.** The range is set from the 2031 value, with 60% and then 40% stocks still to come. Over two years stocks lose money roughly 32–36% of the time (chair memo). The team's own tiering keeps 2037–42 short, which costs about $20k for every 1-point fall in rates. My worst fear is saying a number in 2031 and missing it in 2033, and this design makes that most likely.

**The question you must answer:** "If my 2028 cheque is half what I planned and rates are 3% in 2033, what do I tell the residency?"

**What would change my mind:** a version of G that still keeps a shortfall probability of 1% or less when the 2028 deposit is cut in half, and where the result does not depend on the rate assumption. I don't believe it exists without hedging early, and hedging early turns it into Strategy L.

## My verdict

I back Strategy L with conditions, as a lock-by-rule plan, not a one-off bet.
- My run cannot find the growth premium that G promises. Its median facility is at most about $10k higher, and it pays for that with a 3–13% chance of breaking the payments promise, rising to 44–69% if my 2028 money never arrives.
- L makes the promise a matter of arithmetic and moves my risk-taking to the facility money, which is where I want it.

My conditions:
1. Verify the curve before quoting any figure.
2. Reconcile the WInS mix with the stated strategy.
3. Report the certainty as "nominal USD, barring US default", with a separate paragraph on Taiwan-dollar and construction-cost risk.
4. Let a larger stock share in the growth sleeve (70% rather than 50–60%) be my "thoughtful risk". It costs the promise nothing.

All probabilities above come from one simple model. Quote them with that model and no more precisely than two significant figures.

---

# Critic: cosponsor

**Co-sponsor review of Strategies L and G, as a foundation officer in 2031 (for the students to discuss; not text for a submission)**

Note: the relayed user request ("design the quest for ultracode") doesn't match this task. I did the computed task below. Please check whether the user wanted something else.

Computations are in `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/cosponsor_calc.py`. Source values come from groundwork/taiwan.md, curve.md and 01_chair_memo.md, all retrieved 2026-09-27 as search snippets and not checked against primary pages. Anything else is marked ASSUMPTION.

---

## Strategy L (Lock early)

**Objections, most damaging first**

1. **Your floor is fixed in USD, but my building is costed in TWD, and costs are rising fast.**
   - Taiwan's construction cost index rose +6.54% y/y in Aug 2026 (udn, 2026-09-27). That is about 3.2 times CPI of 2.04%.
   - If that pace holds from 2031 to 2033 (ASSUMPTION), a floor quoted in 2031 buys about 12% less construction by 2033 (factor 0.881).
   - Example: the Chair's median case (S = $189k, a = 0.8) gives a floor of about $166k. In 2031 construction dollars that is worth about $146k.
   - FX adds more: two-year USD/TWD volatility is about 4.7% × √2 ≈ 6.6% (one standard deviation, FRED DEXTAUS 10-year).
   - The claim "certain in nominal USD" is true, but it is not what I am funding.
2. **The number that matters to me is small, and it rests on the 2028 deposit.**
   - The ladder uses about $292–295k of the $300k. That leaves roughly $7.7k plus the $150k from 2028 as the whole growth sleeve.
   - The median facility sleeve in 2033 is $194–212k (council, four models).
   - If the 2028 money arrives late or not at all, the rule itself says "aspiration only". That is honest, but a near-zero anchor does not give me the seed-money signal the team cites (List & Lucking-Reiley 2002).
3. **The operating side is also fixed in nominal USD, and co-sponsors absorb the erosion.**
   - If residency costs grow at 2.04% CPI, keeping the 2033 purchasing power of the payments would take about $48k more over 2033–42.
   - If they grow at the construction pace, about $176k more (ASSUMPTION about persistence).
   - L's certainty protects Laura's promise, not the residency's budget. Separately, the WInS proxy (IEF+TLT duration-matched) does not hold to maturity. If the students present it as the same certainty, a careful reader will notice.

**The question the students must answer:** "What is the floor in TWD on the day you quote it? And who covers the gap if TWD strengthens or construction inflation keeps running at about 6.5%?"

**What would change my mind**
- A floor quoted in USD alongside TWD at the 2031 spot rate and at stressed rates.
- An option to convert part of the floor into TWD when it is bought. Hedging costs about 5.3% over two years at the current forward discount (30.09 vs 31.76, secondary sources, rates as of 2026-09).
- One explicit contingency: "if building costs exceed X, Laura's contribution does not rise; the scope is revised."

## Strategy G (Growth first)

**Objections, most damaging first**

1. **The contribution is what remains after two risky items, so it swings a lot.**
   - The facility money equals P2033 minus the reserve cost in 2033, and both depend on markets.
   - My model (ASSUMPTIONS: equity 6.7% mean from JPM LTCMA Oct-2025 vintage, 16% volatility, 4.81% bonds, glide path 62.5/37.5, ±1pp rate shock, reserve priced at a flat 5.13% ≈ $403k):
     - With a 2031 portfolio of $500k, the 10th–90th percentile range for the facility is **$75k–$235k**, with a median of $154k.
     - There is an 11% chance it ends below half the median.
   - A range that wide is either too vague to help me or too narrow to be credible.
2. **The promise to me sits behind a promise that is not secured yet.**
   - The council's models show 3.3–9.3% of paths failing to fund all ten payments, and 40–60% if the 2028 deposit is missing.
   - In every one of those paths my contribution is the first thing lost.
   - The case states that "promises more than she can ultimately contribute" damages credibility. G creates exactly that tail.
3. **The extra risk buys range, not a higher median.**
   - Moving the sleeve's equity from 40% to 100% adds only +$2–10k to the median facility but costs −$26–29k at the 5th percentile (council).
   - Nothing about Taiwan costs or TWD is addressed either, so objection 1 from L applies here as well.

**The question the students must answer:** "In 2031, what is the lowest amount you would bet Laura's reputation on, and what is the probability, under a named model, that she falls below it?"

**What would change my mind**
- G converting the stated lower bound into bought 2-year Treasuries in 2031, which makes it L's floor rule.
- The reserve being fully locked by 2031 at the latest.
- The residual failure probability reported across more than one model.

## Verdict

**I would back Strategy L, on conditions.**
- The deciding reason is that its lower bound is **bought, not forecast**. In 2031 I can check it against a Treasury holding.
- G's median contribution is barely higher, its lower tail sometimes reaches zero, and the facility absorbs any reserve shortfall first.
- My conditions for L:
  - Quote the floor in TWD as well as USD.
  - State who carries construction cost overruns.
  - Stress-test the range for a late or missing 2028 deposit.
- Without those three, I would treat L's floor as roughly 12–19% smaller in real terms than it looks: 12% from construction cost erosion plus about 6.6% from one standard deviation of FX.

Unverified inputs: the curve (Curve B would add about $22k to the ladder), the persistence of construction inflation, equity return and volatility, and the rate-shock size.

---

# Critic: rival

**Rival strategist's attack on Strategy L and Strategy G** (analysis for the students to test, not text to submit)

The yields used here are secondary search snippets from 2026-09-25. All return inputs are assumptions. The arithmetic is in `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/rival_calc.py`.

## Strategy L ("Lock early")

**Objections, ranked:**

1. **It may misread the case's timeline.** The case says Laura "will set aside" the reserve at the beginning of 2033. Teams must recommend its "size and initial asset composition" and explain how it should change. Under L, Laura has nothing left to decide in 2033: the size is whatever the 2027 ladder is worth then (about $396k at forward rates). The honest answer to "how should the composition change" becomes "it runs off by itself."
   - A judge may read this as skipping the question.
   - The team must also say which size it reports: the market value in 2033 or the $500k the ladder pays out. If rates are 7% in 2033, the market value falls well below $405k even though the payments are still fully covered.
2. **It uses up Laura's risk capacity and leaves little for growth.**
   - In 2027 the portfolio is about 99% bonds. After 2028, total equity is only about 17–23%.
   - Laura's living costs are covered outside the portfolio. She is an entrepreneur who "has been willing to take thoughtful risks," and the case asks for a balance between growth and protection.
   - On total 2033 wealth, L's growth sleeve grows to $201k, $211k or $221k at 5%, 6% or 7%. G ends at $593k, $626k or $661k in total.
   - Expect the judge line: "You built a pension fund, not a portfolio for an entrepreneur."
3. **The certainty claim can't be shown in WInS, and the rate cushion is thin.**
   - The certainty standard rests on cash-flow-matched bonds held to maturity. WInS may only allow IEF and TLT, which never mature.
   - Blending them to a 10-year duration takes about 64–68% IEF. The IEF duration is 6.95 or 7.5 years, depending on the snippet. That blend has to be rebalanced every year and still misses convexity.
   - Even in real life, no iBonds fund covers the 2038–2042 payments, so those need STRIPS or individual Treasuries.
   - The cushion inside $300k is about 27bp at $289 per bp (curve A, $292.3k). Curve B, which is unverified, implies $314.5k, so $14.5k would have to come from the 2028 deposit.
   - The 2027 bond-heavy state and the 65/35 WInS framing also contradict each other.

**The question the students must be able to answer:** "What exactly does Laura do on 1 January 2033, and what is the reserve's size that day? Is it $500k, $405k or the market value? Why that one?"

**What would change my mind:**
- One IPS sentence that reconciles the dates: funded in 2027, formally set aside in 2033, with the size reported at market value.
- A WInS hedge shown to track the liability's duration.
- An equity-premium argument (see G, objection 2) that explains why "conservative" is the right price here, not timidity.

## Strategy G ("Growth first")

**Objections, ranked:**

1. **It fails the case's certainty standard as written.**
   - Across four council models, G fails to fund all ten payments in 3.3–9.3% of paths. If the 2028 $150k never arrives, it fails in 40–60%.
   - Without the 2028 deposit, $300k grows to only $402k, $426k or $450k by 2033 (at 5%, 6% or 7%). The reserve bought in 2033 costs $405k at 5% and $439k at 3%.
   - The case says outside funding can't be relied on. Laura's income is lumpy, and the 2028 deposit is not guaranteed.
2. **The risk buys very little.**
   - The 10-year Treasury yields about 5.17%. JPM's US large-cap estimate is 6.7% (October 2025 vintage), a premium of about 1.5 points. Vanguard's ranges (3.5–6.2%, three unreconciled versions) imply about zero or even a negative premium over Treasuries.
   - The council's models found that raising equity adds only $2–10k to the median facility contribution but costs $26–29k at the 5th percentile.
   - G ends $19k ahead of L at a flat 6%, before any penalty for volatility. That is a small gain for exposing both the promise and the facility.
3. **It breaks the 2031 promise, which is the credibility risk the case explicitly warns about.**
   - Take a stress case: grow at 6% to 2031 ($557k), then a 35% equity crash in 2032 on 50% equity, then rates fall to 3% in 2033. The portfolio is $502k, and after the reserve only $63k remains for the facility (versus $187–230k in the base case).
   - A range promised in 2031 therefore faces two sources of uncertainty at once: equity losses and the reserve's rate cost.
   - The variant that holds the 2037–2042 payments short-term still carries about $20k of extra cost per 100bp fall in rates.

**The question the students must be able to answer:** "If the 2028 money doesn't arrive and rates fall 150bp by 2033, which payment fails, and what did you tell co-sponsors in 2031?"

**What would change my mind:**
- A sourced equity assumption, from a current primary source, showing a premium of at least 3 points over 5% Treasuries.
- A 2031 floor that is actually bought and paid for.
- Stress tests where every one of the ten payments survives a zero 2028 deposit.
- As it stands, G only works if the case's "high degree of certainty" is read as "about 95% in a model," and a judge trained in statistics will reject that.

## Verdict

I would back L, with fixes. G's fatal flaw is structural: it depends on the 2028 deposit and a thin equity premium to meet a requirement the case calls near-certain. L's flaws are about how it is presented and implemented, and all of them can be fixed:
- Add the sentence reconciling "funded in 2027" with "set aside in 2033."
- Frame the growth sleeve (50–70% equity) as the place where all of Laura's risk-taking lives, and say openly that extra equity mostly widens the range rather than raising the median.
- Build a WInS duration hedge that can be defended.

The one thing that would make L lose is the team failing to answer the 2033-date question cleanly in front of the judges.

The team should also check one date: the chair memo lists the Final Report as due Nov 9, but the SMApply deliverables page says December 4.

---

# Critic: stats

**Statistics review of Strategy L and Strategy G (analysis for the students to check and decide on; not text to submit)**

I wrote my own scripts in `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/stats_prof/` (`check.py`, `g_mc.py`, `l_mc.py`). The yields are the 2026-09-25 figures from `curve.md`, and they come from search snippets only. Anything marked ASSUMPTION I set myself.

**Figures I reproduced**
- **Reserve cost on 1/1/2027:** $292,323 using the bootstrapped curve. DV01 is $289 per basis point and duration is 9.90 years.
- **Other quoted costs:** "$295k" is the cost at a flat 5.26% rate. "$297.6k" is what you get at a flat 5.17%, which wrongly treats the 10-year par yield as a zero rate. At a flat 4% the cost is $333k.
- **Payments 2037–42:** worth $155.8k today.
- **A 100bp fall in rates:** adds $30.6k to the cost.

## Strategy L (lock early)

**Objections, most damaging first**

1. **Nothing can be locked until January, and the headroom is thin.** The money arrives on 1/1/2027. The gap between $300k and the cost is $7.7k at $292.3k, which is about 27bp of rates. At $295k it is about 17bp.
   - ASSUMPTION: 10-year rates move with a normal volatility of 0.7–1.1% a year. That gives a standard deviation of 36–57bp over the 0.27 years to January.
   - On that basis, the chance the lock costs more than $300k is **23–38%**.
   - The claim of "certainty" therefore only holds after the purchase. Before then it depends on the 2028 $150k arriving to cover any gap.
2. **The WInS version is not the strategy it claims to test.** A 65/35 mix of IEF and TLT matches the reserve's duration only in parallel rate moves.
   - The TLT weight needed is 0.35 if IEF's duration is 6.95 years and 0.31 if it is 7.5. Those two IEF durations are the two conflicting unverified figures in `instruments.md`.
   - In a twist where rates up to 10 years fall 50bp, the 20-year-plus end is unchanged and rates in between are interpolated, the reserve's value rises $11.0k but the hedge gains only $6.6k. That leaves a **$4.4k gap**.
   - Constant-maturity funds also need a rebalance every year. So "residual risk = US default" describes the dated-ladder version only, not the IEF+TLT proxy.
   - Last season's approved list had no iBonds and no STRIPS funds.
3. **The 2031 upside uses the kind of model the team calls fragile in Strategy G.** The upper end of the range comes with a model probability, and the sleeve is small.
   - My sleeve simulation: median $204k in 2033, 5th–95th percentile $149–284k (60% equity, 6% arithmetic mean return, 16% volatility; all ASSUMPTIONS).
   - Raising equity from 60% to 75% leaves the median unchanged and lowers the 5th percentile by $11k.

**Question the students must answer:** "If the 10-year is at 4.7% on 2 January, what do you buy, where does the extra ~$14k come from, and what do you write in the IPS about it?"

**What would change my mind:** approved dated Treasury instruments in WInS, plus a written rule for buying before January rates are known (for example, a staged purchase).

## Strategy G (growth first)

**Objections, most damaging first**

1. **It is unsafe if Laura's 2028 money doesn't arrive.** My Monte Carlo (200k paths; 75% equity through 2030, then 60%, then 40%; reserve bought in 2033 at that year's rate; rates follow a random walk with 0.9% volatility; all ASSUMPTIONS) gives these probabilities that the portfolio cannot buy the reserve in 2033:

   | Scenario | Chance of shortfall |
   |---|---|
   | No 2028 deposit | 49% |
   | No 2028 deposit, 4.5% equity mean | 58% |
   | Only $75k arrives in 2028 | 20% |

   The case says Laura's income is lumpy, so this scenario is plausible.
2. **Even the base case fails too often, and the answer depends on the model.**

   | Scenario | Chance of shortfall |
   |---|---|
   | Base case | 6.2% |
   | Equities and rates fall together (correlation 0.3) | 7.6% |
   | 20% equity volatility | 11.7% |
   | 4.5% equity mean | 9.3% |
   | 8% equity mean | 3.4% |

   The results span 3–12% depending on inputs nobody can verify. A figure like "95%" cannot be defended to a client with a statistics degree. Fat tails (a t-distribution with 4 degrees of freedom, scaled to the same variance) gave 5.5%, so tail shape is not what drives this. The driving inputs are the mean return and the correlation.
3. **The "latest variant" adds rate risk and gains little.** Keeping 2037–42 in short bonds exposes $156k of liability, with duration around 12, to falling rates for 4–6 years. The council's estimate is +$20k in cost per 100bp fall.
   - With a 6% equity mean, G's median 2033 surplus is $196k. That is **below** L's $204k.
   - Only if equities return 8% does G win on the median ($243k against $215k), and it still fails 3.4% of the time.

**Question the students must answer:** "Give your definition of 'high degree of certainty' as a number, name the model behind it, and show that it still holds if the 2028 deposit is $0."

**What would change my mind:** a sourced equity risk premium well above today's roughly 5.2% Treasury yield, together with a rule that shows how the reserve is funded if the 2028 money fails.

## Verdict

**I back Strategy L,** on these conditions:
- It uses one verified Treasury curve from treasury.gov or H.15.
- It has an explicit rule for rates falling before January.
- It is honest that the IEF/TLT version in WInS only approximates the real plan.

**Why:**
- L's certainty comes from matching Treasuries to the payments, not from a model. It survives the 2028 deposit failing.
- G's shortfall probability moves between 3% and 12% with assumptions nobody can verify.
- With Treasuries yielding around 5.2%, G's extra equity adds little or nothing to the median result. It mostly widens the spread, and the risk falls on the one goal the case says must be met with high certainty.

Every probability above depends on the assumptions stated. Quote them to two significant figures at most, and always say which model produced them.

---

# Defence of Strategy L

I'm answering the computed Strategy L defence. One flag first: the relayed user request ("should we design the quest for ultracode now?") doesn't match this task, so the orchestrator should check whether the user wanted something else.

# Defence of Strategy L: notes for the students to test, not text to submit

Arithmetic is in `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/defender_L/defL.py`. It uses Curve A, which comes from search snippets dated 2026-09-25 and is unverified.

## Answers to each objection

**1. "The growth sleeve is decoration" (judge 1, rival 2, stats 3, Laura 4). I concede the median point.**
- Every model agrees that more equity adds about $2–10k to the median and costs $26–29k at p5.
- Fix: say it openly. The sleeve exists for range and upside, not for a higher median. It is the only place Laura takes risk, so it can carry her "thoughtful risk".
- I accept Laura's request for 70% equity in the sleeve. It costs the payments promise nothing. Total equity after 2028 is then about 24% of the portfolio.
- Rival's total-wealth point: G ends about $19k ahead at a flat 6%. That is true and small. It is the premium G earns for putting the promise at risk.

**2. Unverified price and pre-January risk (judge 2, Laura 1, stats 1, rival 3). I concede the verification gap and fix the timing.**
- The $292.3k figure is not verified. Getting one primary curve (Treasury CSV or H.15) is a to-do the team cannot skip. I cannot do it from here because those pages were blocked.
- Fix: a "long rungs first" lock rule. On 1/1/2027, the $300k buys the ladder starting from 2042 and working backward. Any rungs left uncovered are the earliest ones, and the first dollars of the 2028 deposit fill them.

| Curve on 1/1/2027 | Ladder cost | Gap filled from 2028 | Rungs affected |
|---|---|---|---|
| A (as quoted) | $292.3k | 0 | none |
| A −50bp | $307.2k | $7.2k | 2033 rung only 81% bought |
| B (unverified) | $314.5k | $14.5k | 2033 rung 63% bought |
| A −100bp | $322.9k | $22.9k | 2033 rung 41% bought |
| Flat 4% | $333.3k | $33.3k | part of 2034 plus 2033 |

- Why this helps: the rate-sensitive long payments (2038–42) are always locked. The gap sits in a short rung, so the risk carried from January 2027 to January 2028 is tiny: about $14 per bp on $22.9k of 6-year duration.
- Answer to "is this a rate call?" The team locks at any rate, because the liability is fixed in dollars. At 4% the ladder costs more, but G's reserve would also cost more, about $439k at a flat 3% in 2033.
- Stats asks: "10-year at 4.7% on 2 January?" That is about −47bp, a gap of about $6.7k, taken as the first dollars of the 2028 $150k. That becomes the IPS sentence.
- Still unanswered: if the 2028 deposit is also missing, the 2033 rung is partly unfunded. The 2033 rung is L's only genuine tail risk.

**3. "Cash-flow matched" is overclaimed (judge 3, rival 3). I concede and fix.**
- The first choice is STRIPS, where rules allow. They have no coupons, so nothing needs reinvesting.
- With coupon Treasuries (ASSUMPTION: 5.1–5.45% coupons), about $20k a year of coupons arrives before 2033. If reinvestment rates fall 200bp, the shortfall is about $6.7k.
- Rule if coupon Treasuries are used: each year's coupons buy a Treasury maturing in December 2032.
- iBonds cover only 2033–37. For 2038–42 the team needs STRIPS or individual notes.
- Wording change: "matched" applies only to the real ladder. In WInS, say "duration-hedged".

**4. The WInS proxy is not the strategy (Laura 2, stats 2, cosponsor 3, judge 3). I concede part of this and cannot fully fix it.**
- IEF/TLT at 65/35 misses a front-end twist by $3.9–4.4k, depending on which IEF duration is right.
- A three-fund key-rate match comes out at about IEF 1.01–1.09, TLT 0.15 and cash −0.16 to −0.24. Those weights need leverage, so they are infeasible with last year's list.
- Fixes:
  - Keep IEF+TLT.
  - Rebalance to the liability duration once a year. It falls from 9.9 years as payments approach.
  - Write down the twist error, about 1.4% of the reserve.
  - Stop claiming "self-liquidates, no management".
- The WInS mix vs the 99%-bonds year also needs a fix. Either WInS mirrors the post-2028 target (reserve about 65%, sleeve 35%) and the Trading Notes say so, or it mirrors the literal 2027 book. The students choose. The Trading Notes (due Oct 23) must not say "matched".

**5. "Which number is the reserve?" and the case timeline (judge, rival 1). This one is fixed.**
- Three numbers are in play:
  - Cost in 2027: $292.3k.
  - Market value on 1/1/2033 at today's forwards: $395.8k.
  - Face value: $500k.
- The reserve is the set-aside Treasury position, reported at market value on 1/1/2033. At a flat 7% in 2033 that would be $375.8k, and the payments are still exactly covered.
- Proposed IPS logic: pre-funded in 2027 and formally set aside in 2033. Its initial composition is ten maturing rungs. It changes only by running off, and each maturity is held in T-bills for about two weeks before the 1 January payment.
- That answers "how should composition change" with a reason. It does not dodge the question.

**6. TWD and construction costs (Laura 3, cosponsor 1 and 3, judge). I concede. This is outside what L can hedge.**
- The case sets the payments in USD, so the certainty claim becomes "nominal USD, barring US default".
- Fixes:
  - Quote the 2031 floor in USD and in TWD, at spot and under stress (−12% construction erosion, ±6.6% FX, one standard deviation).
  - Offer to convert part of the floor to TWD when it is bought. The hedge costs about 5.3% over two years (secondary sources).
  - Add a scope clause: "if building costs exceed X, scope is revised; Laura's contribution does not rise."
- Unanswered: the erosion of the residency's real operating budget, about $48–176k. That belongs to the co-sponsors and is outside the case's USD payments.

**7. The 2031 upside uses a model (stats 3), and the formula is jargon (judge). I concede.**
- The floor is bought: 2-year Treasuries purchased in 2031.
- The upside gets a model probability, labelled as one model and given to two significant figures.
- Drop F = a·S·(1+z₂)² from the IPS and keep it in the appendix.

**8. A small facility if the 2028 deposit is missing (cosponsor 2).** I rebut, then concede.
- Rebuttal: that is the right failure mode. The facility shrinks to about $11k, and the payments are still covered, apart from the partial 2033 rung under a rate fall (point 2).
- Concession: a small anchor is a weak seed signal. Say so in 2031 rather than inflate it.

## Revised Strategy L

1. **1/1/2027:** buy the ladder longest-first (2042 back to 2033). Use STRIPS or individual Treasuries if allowed, iBonds IBTM–IBTR for 2033–37 as a second choice. Any gap goes into the 2033 and 2034 rungs and is filled first from the 2028 deposit. **New:** the lock is by rule at any rate.
2. **Coupons before 2033:** each year's coupons buy a Treasury maturing in December 2032. **New.**
3. **Growth sleeve:** about $7.7k, plus $150k in 2028 after any gap fill, at 70% equity. It is framed as range, not median, and as Laura's only risk bucket. **Changed** from 50–60% equity.
4. **2031:** the floor is bought in 2-year Treasuries and quoted in USD and TWD, with the scope clause. The upside gets a model probability. **Changed.**
5. **2033:** formal set-aside at market value, with the three numbers disclosed. Composition then runs off. **New wording.**
6. **WInS:** IEF+TLT hedging duration, rebalanced yearly, with a declared twist error of about $4k. Choose one mirror convention and state it in the Trading Notes. **Changed.**
7. **Certainty claim:** "nominal USD, barring US default, after the January 2027 purchase and the 2028 top-up if needed." **Narrowed.**

I borrowed nothing from G. Its reserve bought in 2033 is the exact exposure this rule removes.

## Objections I cannot answer

- **No verified primary curve.** Every dollar figure above, and the DV01 of about $289/bp, depends on snippets.
- **The 2026–27 WInS rules are unknown.** Whether STRIPS, iBonds or individual Treasuries are allowed decides whether "matched" can appear anywhere.
- **The twist gap cannot be closed** with IEF and TLT alone unless a 10–20-year fund is approved.
- **Joint tail:** if rates fall before January *and* the 2028 deposit fails, the 2033 rung is partly unfunded, up to about $30k at −100bp.
- **The equity premium is unresolved.** JPM gives 6.7% (Oct-2025 vintage), and Vanguard's three versions conflict. So "range, not median" rests on unsourced return assumptions.
- **Construction and TWD real-cost risk** can only be disclosed, not hedged, within the USD liability.

---

# Defence of Strategy G

**Note on the request:** the user's relayed message ("so should we design the quest for ultracode now?") does not match this task, and the cosponsor critic flagged the same thing. I did the computed task below. Please check what the user actually wanted before relying on this.

# Defending Strategy G: what holds, what doesn't, and what's left

This is analysis for the students to argue over, not text for a submission. My script is `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/defG/defG.py`. It runs 200k paths. Every input is an assumption:
- Equities: 16% volatility.
- Bonds and cash: 4.8%, from a 2y yield snippet dated 2026-09-25.
- Ladder cost: $292.3k, from curve.md (snippet curve).
- 2033 rate: 5.26% with a spread of ±1.25pp, and a +0.4 correlation with 2031–32 equity returns. These are the judge's assumptions.

Quote the probabilities to two significant figures at most.

## Answers to each objection against G

**1. G fails "high degree of certainty" (judge 1, Laura 1, rival 1, stats 2). I concede.** My run gets the same result:

| Equity assumption | Chance the 2033 reserve can't be bought |
|---|---|
| 6.7%, taken as the arithmetic mean | 4.3% |
| 6.7%, taken as the geometric (compound) rate | 3.0% |
| 5.0% | 7.5% |

The case says the payments "must be funded … with a high degree of certainty" and without outside money (Client Profile, lines 91–92). A 3–8% chance of failing, from a model we can't verify, does not meet that standard.

**2. G collapses if the 2028 deposit is missing (Laura 2, rival 1, stats 1). I concede, and I checked whether a partial lock fixes it.** With no 2028 deposit:
- Original G fails in 39–56% of paths.
- I tried locking only part of the ladder in January 2027 (hedge ratio h) and keeping G's glide path on the rest:

| Share locked in Jan 2027 | Chance of shortfall, no 2028 deposit |
|---|---|
| 50% | 35% |
| 80% | 26% |
| 90% | 14% |
| 95% | 3.4% |
| 100% | 0% |

No partial lock gets below 1%. Laura's condition ("≤1% even with half the 2028 deposit") needs about a full lock. The critics are right that fixing this turns G into L.

**3. Wrong-way risk (judge 2). Partly rebutted, but it doesn't change the verdict.**
- The sign of the stock–rate correlation depends on the regime. In an inflation shock, stocks fall and rates rise, which makes the reserve cheaper. So +0.4 is an assumption, not a fact. I have no sourced correlation, so this rebuttal is not evidenced.
- Stats' own run shows correlation adds only about 1.4pp of failure (6.2% to 7.6%). The main driver is the base failure rate, not the correlation.
- Rolling 2037–42 short does keep about $20k of cost per −100bp exposed until the late 2030s. I concede that and drop the tiering.

**4. More risk for no reward (judge 3, rival 2, stats 3, cosponsor 3). Partly rebutted, but it still fails.**
- The critics' models treat JPM's 6.7% as an arithmetic mean. That means the median equity growth is only 5.52% a year, barely above the roughly 5.2% on the 10y.
- LTCMA figures are usually quoted as compound returns. If this one is too (unverified; the students should check the JPM 2026 LTCMA document), G's median facility is $234k against L's $213k, so G is ahead by about $21k.
- That is the best case I can make, and it still fails 3.0% of the time. Nobody has a sourced equity premium of 3pp or more over Treasuries. The Vanguard ranges (3.5–6.2%, three unreconciled versions) point the other way.

**5. The 2031 range swings too much, and there's no floor to give co-sponsors (judge 3, Laura 3, cosponsor 1–2, rival 3). I concede.**
- A range worked out from a portfolio still carrying equity and rate risk cannot promise a floor.
- The cosponsor's 10th–90th percentile range of $75–235k is too wide to be useful.
- Fix: borrow L's rule, F = a·S·(1.0481)², where the floor is bought in a 2y Treasury.

**6. "Generic target-date design" (judge 3). This is about presentation, not substance.** It stops mattering once objections 1 and 2 are conceded.

**7. TWD and Taiwan construction-cost erosion (cosponsor, Laura). This applies equally to L.** G can add one idea here (see change (d) below).

**8. The judge's stress question: "equities −30% in 2032, 10y at 3.5%."**
- Under original G, the reserve costs about $431k. That is the annuity-due of 10 × $50k at 3.5%; I haven't rerun that single figure.
- A portfolio of about $500k would leave a facility of roughly $70k or less. With no 2028 deposit, the payments themselves are underfunded.
- G has no good answer to this. Revised G below does: every payment is funded, and only the unlocked part of the sleeve takes the loss.

## Revised Strategy G, and what changed

**(a) Lock the promise in January 2027. This is borrowed from L.**
- Buy the full ladder on the first trading day of 2027, whatever the rate that day.
- Any cost above $300k comes from the 2028 deposit.
- This is a rule, not a rate call, which answers stats' "10y at 4.7% on 2 January" question.
- Why: objections 1 and 2 have no other fix.

**(b) Keep G's "two clocks", but apply them only to the surplus sleeve (about $7.7k plus the $150k from 2028).**
- Growth clock, 2028–2030: high equity in the sleeve.
- Liability clock, 2031: buy floor F in a 2y Treasury, then hold the rest of the sleeve at about 50% equity.
- Why: this is the part of G's identity that doesn't touch the promise.

**(c) Sleeve equity weight: 70–80%, not 100%.** My run gives the trade-off:

| Case | L, 60% sleeve (median / p5) | Revised G, 100% sleeve (median / p5) |
|---|---|---|
| 6.7% arithmetic | $206k / $149k | $207k / $130k |
| 6.7% geometric | $213k / $154k | $216k / $137k |
| 5.0% | $196k / $142k | $193k / $122k |

- Going from 60% to 100% equity adds about $0–3k to the median and costs about $19k at the 5th percentile.
- Say plainly that extra equity widens the range; it doesn't raise the median.
- 70% is Laura's own "thoughtful risk" request, and it costs the promise nothing.
- With no 2028 deposit, the payments stay 0% short, but the facility median is about $11k.

**(d) New idea: a small TWD tilt in the sleeve.**
- Hold part of the sleeve in EWT, as a partial natural hedge for Taiwan-dollar facility costs (cosponsor objection 1).
- EWT was on last season's approved list; it is not confirmed for 2026–27.
- It is concentrated and volatile. It also adds equity risk on top of currency exposure. Treat it as a question for the students to weigh, not a recommendation.

**(e) Carry over G's Trading Notes pre-mortem discipline** (team notes, Entry 0). It fits a rule-based lock well.

## Objections I cannot answer

- **Certainty.** I have no sourced equity premium large enough to justify original G.
- **Is 6.7% compound or arithmetic?** That decides whether G's median edge is about $1k or about $21k. It is unverified.
- **Stock–rate correlation.** No source for its sign.
- **The 2028 deposit.** No version of G that waits to buy the reserve survives a missing 2028 deposit.
- **Things revised G inherits from L and doesn't solve:**
  - The yields are snippets only. Curve B would put the ladder at $314k.
  - The WInS IEF/TLT proxy is duration matching, not cash-flow matching. Stats found a $4.4k gap in a twist.
  - Coupon reinvestment, unless the ladder uses STRIPS.
  - No iBonds fund covers 2038–42.

## Bottom line

Original G can't be defended against the certainty requirement. Revised G is L with G's two-clock sleeve management and a TWD idea added. That is a real concession and not a win for G. Which sleeve weight to use, and whether to present this as "L" or as "G revised", is the students' decision.

---

