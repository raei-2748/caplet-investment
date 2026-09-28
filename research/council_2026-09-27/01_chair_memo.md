# Council Chair Decision Memo — Team Caplet (brainstorming input, not submission text)

**Date:** 2026-09-27 · **Chair's recomputation script:** `/tmp/claude-0/-home-user-caplet-investment/8c147b18-bf89-5749-b72d-4751bfb03bef/scratchpad/council/chair/settle.py`

> **Wharton AI policy.** Everything below is analysis for you to argue over, recompute yourselves and rewrite in your own words. Do not paste any phrase from this memo into a deliverable. That includes the council's slogans.

## 1. Recommended architecture

**Recommended: a rule-based policy engine (architecture B), stated in plain language.**

1. **Lock the promise with Treasuries as soon as money arrives.** The ten fixed $50k payments are matched with Treasury zero-coupon bonds (or defined-maturity Treasury funds), each maturing just before its 1 January payment date. The hedge ratio rule is: hedge = min(100%, assets ÷ Treasury-priced liability), and it only ratchets up. At today's yields the rule means locking about 100% in January 2027.
2. **Measure risk on the surplus, not on total assets.** Laura's appetite for "thoughtful risk" is spent only on money the promise does not need.
3. **Funding waterfall.** The 2027 deposit buys the ladder, starting with the nearest maturity and working outward. Any cost above $300k is covered first from the 2028 deposit. Only the remainder goes to growth.
4. **2031 rule.** Laura's co-sponsor range is a rule the team applies to the growth sleeve's value in 2031 (see §5). It is not a forecast made today.

**Why it fits Laura.**
- The case demands "a high degree of certainty". Under this design that becomes a matter of arithmetic, not a model output.
- Her income is lumpy. If the 2028 $150k is late, partial or missing, only the facility shrinks; the operating commitment is unaffected.
- She is a statistics graduate who began by fighting misinformation. She gets a certainty standard that does not depend on a model, and every probability comes with its model stated.

**Runner-up A: static lock plus a growth sleeve with no formal rules.** This is simpler to explain. Prefer it if the team judges that B's rules are too much for a 500-word IPS. Its weakness is that it reads as "safe bucket plus growth bucket", which is what most teams will submit.

**Runner-up (b): a calendar-based partial lock with a funded-ratio trigger.** Prefer it only if the team deliberately wants to keep some exposure to rates falling before 2031 as an expression of Laura's risk-taking side. In practice the council found that it converges to full locking, and there is no statistical reason to wait unless you hold a view on rates.

**Rejected: architecture C (the original plan of ~75% equity with a glide path and buying the reserve later).**
- Across the four council models, it fails to fund all ten payments in 3.3–9.3% of paths.
- If the 2028 deposit never arrives, it fails in 40–60% of paths.
- Both results are incompatible with "high degree of certainty".

## 2. Resolving the flagged contradictions

**(1) Lock-in timing. Decision: lock all ten maturities early. Do not roll 2037–42 in short bonds.**
- Payments due 2037–42 are worth about $154k today.
- If they are left short and rates fall, the extra cost is about $20k per −100bp and about $43k per −200bp (Actuary; confirmed by the CIO within $1k).
- Locking in 2027 is consistent with "reserve set aside at start of 2033". The ladder is economically locked from 2027 and formally designated as the reserve in 2033. The IPS needs one sentence that says so.

**(2) Risk budget. Decision: "~75% equity" applies to the growth sleeve only.**
- With a growth sleeve at 50–70% equity, whole-portfolio equity is only about 17–23% after 2028 (for example 0.7×150/450 = 23.3%).
- In the CIO's model, moving the sleeve from 40% to 100% equity adds only +$4–10k to the median 2033 facility sleeve but costs −$26–29k at the 5th percentile. The Quant found +$2k. Extra equity mostly widens the range; it adds little to the median.
- **Unresolved:** the sleeve's equity weight. The CIO revised to 50–60%; the Quant says 70%. This is your decision.

**(3) Rate assumption. Decision: retire both the flat 4% and "10y 5.1%".**
- Price each payment off one bootstrapped zero curve, taken from one verified Treasury table on one date.
- My recomputation (annual-coupon bootstrap, DF(0)=1 anchored, curve flat below 2y — all ASSUMPTIONS):
  - Zero rates for the 2033–2042 payment dates: 5.04% rising to 5.38%.
  - **Ladder cost at 1/1/2027: $295.3k** on the forward (no-arbitrage) basis, and $295.9k if the curve is unchanged.
- The spread across the council was $293.3k–$297.7k. The $297.7k treats par yields as zero rates, and the Actuary's $296.7k came from a DF(0) bug. Both should be retired. The remaining $293–296k gap is bootstrap convention.
- **Settled figure: "about $295k (±$3k by method), repriced on purchase day".**
- Headroom inside $300k: rates falling roughly 15–20bp before January uses it up (DV01 ≈ $297/bp). A fall of −100bp would push the cost to about $326k, which the waterfall then covers.

## 3. Key numbers

The figures are the Chair's recomputation unless noted. **Every yield comes from a search snippet; no primary page was reachable. Verify all of them.**

| Item | Value | Source / assumption | As of |
|---|---|---|---|
| Par yields 2/5/7/10/20/30y | 4.81/4.99/5.06/5.17/5.45/5.48% | Advisor Perspectives, Forbes, primerates snippets (5y/7y/20y may be 9/23) | 2026-09-25 |
| Zero rates for 2033–42 payments | 5.04–5.38% | Bootstrap of the par yields above; method is an ASSUMPTION | same |
| Ladder cost at 1/1/2027 | ≈$295k (range $293–296k) | Forward-consistent computation | same |
| Ladder cost at 1/1/2027 if rates −100bp | ≈$326k | Parallel shift of the zero curve | same |
| DV01 / modified duration | ≈$290–297 per bp / ≈10 | Council range | same |
| Implied reserve value on 1/1/2031 / 1/1/2033 if locked now | $357–358k / $396–397k | Forward curve | same |
| Reserve cost in 2033 if bought then at flat 5/4/3% | $405k / $422k / $439k | Annuity-due arithmetic | — |
| 2y Treasury factor over 2 years | ×1.0985 | 1.0481² | 2026-09-25 |
| 10y TIPS real yield / breakeven | 2.85% / 2.28% (auction 2.653% on 9/17) | tipswatch/ecmsource snippets; **conflicting** | 2026-09-25 |
| US large-cap expected return | 6.7% | JPM 2026 LTCMA (Oct 2025 vintage, set when yields were lower) | 2025-10 |
| Vanguard US equity range | 3.5–5.5% / 3.9–5.9% / 4.2–6.2% | **Three versions cited; unresolved** | 2025-12 |
| Equity volatility | 16% | ASSUMPTION | — |
| USD/TWD | 31.79 (9/24), 31.73 (9/26) | tradingeconomics, pluang snippets | 2026-09 |
| Taiwan CPI / policy rate | 2.4% y/y (Aug) / 2.0% | CEIC, finimize snippets | 2026-09 |
| Real value of $50k at 2% inflation | $43.5k in 2033 / $36.4k in 2042 | ASSUMED 2% | — |
| Team note's "$626k" | Implies a flat 5.99% return | Solved 300(1+r)⁶+150(1+r)⁵=626 | — |
| No-lock shortfall probability | 3.3–9.3% | Model-dependent; the spread is driven by rate-drift assumptions | — |
| Median 2033 facility sleeve (locked design) | $194–212k | Four models; quote as a range | — |

## 4. "High degree of certainty"

**Proposed definition** (Actuary, adopted by all four members):

1. **Market-consistent funding.** Assets are at least the value of the ten payments discounted on the Treasury zero curve, not at an assumed return.
2. **Cash-flow matching.** Each payment is matched by a Treasury cash flow maturing on or before its date and held to maturity.
3. **Stated residual risks.** The only risks left are US Treasury default and operational error. Say "certain in nominal USD, barring US Treasury default". Do not say "100%".

**How to evaluate it:**
- Report the funded ratio (assets ÷ Treasury-priced liability) at each checkpoint.
- Show that a model-based "95%" is fragile: the same no-lock strategy scores roughly 91–97% funded across four models.
- If you want a numeric tolerance, the Solvency II "99.5%" analogy is currently **unsourced**. Fetch a source for it or drop it.
- Give probabilities to two significant figures at most, and name the model behind each one.

## 5. The 2031 co-sponsor range rule

The reserve is already locked by 2031 and never forms part of the range. Let **S** be the growth sleeve's value on 1/1/2031, **a** the share you choose to lock, **z₂** the 2-year Treasury rate on that day, and **c** the payout share of the invested remainder.

- **Floor F = a · S · (1+z₂)².** It is bought in a Treasury maturing before 2033, so it is already paid for.
- **Upper figure U = F + c · (1−a) · S · g₉₀,** where g₉₀ is the model's 90th-percentile two-year growth factor. The model must be stated.
- **Communicated:** "at least F; up to U with about 90% model confidence."

Floor examples at today's 2y rate (×1.0985):

| S | a = 0.6 | a = 0.8 | a = 1.0 |
|---|---|---|---|
| $100k | $66k | $88k | $110k |
| $189k (Quant median) | $125k | $166k | $208k |

**How it protects the floor:** the floor is bought, not forecast. If the 2028 money never arrives, S is roughly zero, so F is roughly zero and the rule automatically says "aspiration only".

**Why a matters:** the stretch half is risky. With 16% volatility and a 5.5% arithmetic mean return, two-year equity loses money 36% of the time (32% if 5.5% is the geometric mean). State which one you mean.

The council rejected the Quant's alternative floor of "0.96·S at 95% confidence" as the headline, because it depends on the model.

## 6. WInS implementation, Sept 28 – Nov 6

**Unknown until you check the platform:** the approved list, starting capital, trade limits and sector minimum. The "6 sectors" claim is unverified. Check all of these before the first trade.

**Choose one framing now** and use it in the Trading Notes, the IPS and the Final Report:
- **(i)** WInS mirrors the post-2028 steady state, roughly 65% hedge / 35% growth (council preference); or
- **(ii)** WInS mirrors the 2027 state, which is about 99% bonds.

**Portfolio roles and instrument types:**
- **Liability hedge (~65%).** Defined-maturity Treasury ETFs dated in the 2030s, if approved. The iShares iBonds Dec 2033–2035 funds exist; eligibility and later vintages are unverified. Otherwise use long or intermediate Treasury or zero-coupon Treasury funds blended to a duration of about 10. TIPS are not the core hedge, because the liability is fixed nominal.
- **Floor proxy.** Short Treasury or T-bill funds, standing in for the 2031 two-year Treasury.
- **Growth (~35%).** Broad US plus developed ex-US equity. Meet any sector rule inside this sleeve so that the rule does not drive the allocation. Avoid theme bets.

**Three Trading Notes by Oct 23:**
1. **The ladder or duration-matching purchase.** Log the trade-day yield against the lock rule.
2. **The first growth-sleeve purchase.** Justify it as surplus-only risk.
3. **A discipline trade.** Either a rebalance back to target bands, or the floor-proxy position illustrating the 2031 rule.

Each note should name which part of the plan the trade serves. Say explicitly that a mark-to-market loss on long Treasuries does not matter to a hold-to-maturity liability.

**Rebalancing rule (suggestion; you set the numbers):**
- Review weekly.
- Rebalance when a sleeve drifts more than ±5 percentage points from target.
- Never sell hedge assets to buy equity.
- Record every deviation in a decision log.

## 7. What makes this distinctive, and what to avoid

**Distinctive:**
- A certainty standard that does not rely on a model.
- The ladder is self-liquidating, so the reserve's composition does not need active management.
- All risk sits in the surplus, and the team says openly that extra equity "buys range, not median".
- The 2031 range is a rule to be applied then, not a forecast made now.
- Cover what the debate under-covered: Taiwan cost inflation, TWD exposure (the 2-year forward implies about 5% fewer TWD per USD), and one reasoned sentence on how much flexibility to keep after the facility contribution.

**Avoid:**
- Jargon in the IPS: DV01, Vasicek, bootstrapping, defeasance, LDI.
- More than one rounded number in the IPS. The instructions say calculations are not expected.
- The words "guaranteed" or "100%" without qualifiers.
- Deliverables that contradict each other.
- The Actuary's curve bug. Anchor DF(0)=1 in any code you reuse.
- Pasting AI slogans into any deliverable.

## 8. Decisions only the students can make

- Architecture B vs. A vs. (b).
- WInS framing (i) or (ii).
- Growth-sleeve equity weight: 50%, 60% or 70%.
- The 2031 parameters a and c, and whether the range is quoted in USD only or also as a TWD reference.
- Whether to state a numeric shortfall tolerance.
- Which single equity source to use.
- Rebalancing bands.
- Which three trades become Trading Notes.
- The wording of the pitch, the IPS and the co-sponsor communication.

**Research tasks (unranked; assign among yourselves):**
- Verify one Treasury par curve on a single date from treasury.gov or H.15, and re-bootstrap it.
- Confirm the WInS rules: approved list, capital, limits, sectors.
- Check which defined-maturity Treasury ETFs exist, their vintages and whether they are approved.
- Fetch one primary equity capital-market assumption (Vanguard or JPM) with its date.
- Research Taiwan inflation, USD/TWD and the facility-currency question.
- Keep the decision log and draft the Articulation narrative; recompute the key Python figures independently.

## 9. Open questions and sources

**Open:**
- The true curve on the purchase date.
- TIPS: 2.653% vs. 2.85%.
- The Vanguard figure.
- The 2y TWD rate (the policy rate was used as a proxy).
- TWD volatility (5–7% is unsourced).
- A source for Solvency II 99.5%.
- Equity–bond correlation.
- Whether the case expects the reserve to be designated in 2033 or merely funded by then.
- The instructions for the Final Report (due Nov 9).

**Sources** (search snippets, accessed 2026-09-27; primary pages blocked):
- https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026
- https://www.forbes.com/advisor/investing/treasury-rates/
- https://primerates.com/primerate/treasury-yield-curve/
- https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026 (verify here)
- https://www.federalreserve.gov/releases/h15/
- https://tipswatch.com/2026/09/17/10-year-tips-reopening-gets-real-yield-of-2-653-highest-in-nearly-18-years/
- https://ecmsource.com/tips-breakevens-fall-hot-cpi-real-yields-september-2026/
- https://tipsyield.com/real-yields
- https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/tmt/30-years-of-foresight-the-2026-ltcmas-in-focus
- https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/2026-outlook-economic-upside-stock-market-downside.html
- https://www.morningstar.com/markets/experts-forecast-stock-bond-returns-2026-edition
- https://www.schwab.com/learn/story/schwabs-long-term-capital-market-expectations
- https://tradingeconomics.com/taiwan/currency
- https://pluang.com/en/tools/currency-converter/usd-twd
- https://www.ceicdata.com/en/indicator/taiwan/consumer-price-index-cpi-growth
- https://finimize.com/content/taiwans-central-bank-edged-up-its-2026-inflation-view
- https://www.ishares.com/us/products/337745/ishares-ibonds-dec-2034-term-treasury-etf
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=295075 (List & Lucking-Reiley 2002)

**Council scripts:** `.../scratchpad/council/{actuary,cio,client,quant,chair}/`