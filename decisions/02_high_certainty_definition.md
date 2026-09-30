# D2: What does "a high degree of certainty" mean?

**Status:** DECIDED · **Evidence:** `results.json` → `grid[*].p_funded`, `history`, `sensitivity.contribution_2028`, `sensitivity.y0`

## Question
The case asks us to "define what [we] consider a high degree of certainty, explain how [we] evaluated that level of certainty, and identify the assumptions supporting [our] recommendation."

## Options
1. **A probability only**, e.g. "90% chance of success," the common financial-planning convention.
2. **A mechanism only**, e.g. "funded by Treasuries held to maturity."
3. **Both:** a mechanism, plus a probability standard tested in several independent ways.

## Evidence
- **Planning convention:** advisors often target 80–90% probability of success. Kitces shows that this makes sense *only when the client can adjust*: a 90% figure "overstates" risk if spending can be cut later. **Laura cannot adjust.** The payments are fixed and outside money is ruled out, so the planning convention is the wrong benchmark.
- **Institutional convention for promises that can't be adjusted:**
  - Insurers under Solvency II must hold enough capital to survive "all but the most extreme risks that occur less than once every 200 years" (99.5% one-year VaR).
  - Pension plans near their end state use cash-flow matching to remove market risk entirely (Western Asset).
- **Our model for Strategy A:**
  - Funded in **100%** of paths in all 9 scenario × stock-bond regime combinations (bear/base/bull × three correlation regimes).
  - Funded in **93/93** historical windows (1928–2025), with at least $102k to spare.
  - Still 100% funded if the 2028 $150k is halved or never arrives.
  - Still 100% funded at starting yields of 4.0–5.5%.
- **Why the model can't be the whole answer:** Monte Carlo results are only as good as their assumptions; Advisor Perspectives and Income Lab both caution against treating them as facts. Certainty that rests on a *contract* (a bond that repays a known amount on a known date) is sturdier than certainty that rests on a *forecast*.

## Debate
- **Advocate (option 3):** Give judges a number *and* explain why it isn't just a number.
- **Opponent:** "100%" sounds naïve; no model can promise that. Say 95% and move on.
- **Advocate:** We don't claim 100% about markets. We claim the payments no longer depend on markets, because they are matched by US Treasuries held to maturity. The residual risks are listed below, and they are small and named.
- **Judge:** Option 3. The mechanism wins the argument, and the 99.5% standard gives judges a recognisable benchmark. Require the residual-risk list.

## Decision
**"High degree of certainty" means both of the following:**
1. **Mechanism:** every $50k payment is matched in amount and timing by US Treasury securities held to maturity, bought in 2027–28. After that, stock or bond market movements cannot change whether a payment is made.
2. **Standard:** the strategy must fund all ten payments in ≥ 99.5% of simulated outcomes (the 1-in-200 standard insurers use) in *every* scenario we test, *and* in every historical 6-year sequence since 1928, *and* if the 2028 contribution is late or smaller.

**Residual risks** (state these honestly in the IPS):
- US government default.
- Small timing mismatch: bonds maturing Nov/Dec pay January payments, covered by holding T-bills for about 1–2 months.
- Reinvestment of coupons from coupon-paying bonds: small, and handled by buying slightly less face value in the shortest rungs.
- Execution: prices on the actual Jan-2027 purchase date will differ from today's.

## What would change our mind
If Wharton's Final Report instructions (9 Nov) define certainty differently, we adopt their definition and keep ours as supporting evidence.

## Plain English for Laura
"High certainty" means your yearly $50k doesn't depend on the stock market at all. Each payment is already sitting in a US government bond that matures just before it's due. The only way a payment is missed is if the US government defaults.

**Sources:**
- [Kitces: Monte Carlo for one-time vs ongoing plans](https://www.kitces.com/blog/monte-carlo-one-time-vs-ongoing-retirement-planning-probability-of-success-guardrails/)
- [Skadden: Solvency II standard formula (99.5%)](https://www.skadden.com/insights/publications/2024/06/the-standard-formula-a-guide-to-solvency-ii-chapter-8)
- [Western Asset: Cash-flow matching](https://www.westernasset.com/us/en/research/blog/the-final-phase-of-ldi-cash-flow-matching-2023-02-23.cfm)
- [Advisor Perspectives: The dangers of Monte Carlo simulations](https://www.advisorperspectives.com/articles/2023/01/10/the-dangers-of-monte-carlo-simulations)
