# Red Team Review: "Lock, then grow" (Strategy A)

Three hostile readers review the strategy in `decisions/`. Each weakness comes with a fix; the top 10 are ranked by how much they could cost us with judges.

---

## (a) Aberdeen portfolio manager (professional judge)
> "Competent, but I've seen 'buy a bond ladder' before. Convince me you *decided* this rather than defaulted to it. And why am I reading about stock picks in a bond portfolio?"

- Will test whether the team understands **why** the ladder is cheap now: yields ~5%, the highest 10Y since late 2023. Will ask what the team would do at 3%.
- Will probe **model risk**: a flat yield curve, a single-factor rate model, US-only history, and equity returns chosen by the team.
- Will check **consistency**: does the WInS account look like the IPS? Do the Trading Notes cite the IPS rules?
- Will like: clean separation of promise and aspiration; 93/93 historical windows; the 2031 lock rule; honest residual risks.

## (b) Laura Gao (the client)
> "I'm an entrepreneur. You've put two-thirds of my money in bonds for six years. What's my building actually going to get? And what happens to the residency when $50k buys less in 2040?"

- The median facility contribution of **$167k** ($144k in 2027 dollars) may feel small against her ambitions. She will want to see the upside she is giving up (C80: median $187k, p90 $392k) and to make that choice herself.
- The $50k nominal payments lose ~23% of their purchasing power by 2042 at 2.5% inflation. That isn't our requirement, but she will notice.
- She will want the plan explained without jargon. "Liability-driven," "funded ratio" and "hedge ratio" must be translated.

## (c) Prospective co-sponsor (2031)
> "You say 'at least $113k, probably $153–174k'. How do I know that minimum is real? What stops her using it for something else?"

- Wants proof the committed minimum is *set aside*: separately held Treasuries maturing Dec 2032, not a forecast.
- Wants to know what happens if the facility costs more than planned. Is Laura's 20% buffer available to the project?
- Would respond better to a **written commitment letter** from Laura than to a range in a slide deck.

---

## Top 10 weaknesses and fixes
| # | Weakness | Who raises it | Fix (owner: team) |
|---|---|---|---|
| 1 | "It's just buying bonds; where's the strategy?" (Creativity, Investment Strategy criteria) | Aberdeen PM | Frame as a **decision under a rule**: at yields ≥ ~4% we lock early; below that we'd use a staged hedge (B). Show chart 02 (certainty vs facility) as the decision picture, and tell the "two cheques" story: the first buys certainty, the second builds the dream. |
| 2 | Contradicts the case wording "at the beginning of 2033, Laura will set aside…" | Aberdeen PM | Say it explicitly: Laura *designates* the reserve in 2033 as the case says; we recommend *buying its assets* in 2027 because they are the same assets and are cheaper now. Cite pension practice (Russell 2026; Western Asset). |
| 3 | Everything depends on Jan-2027 yields | Aberdeen PM | Show the y0 sensitivity table: A stays 100% funded from 4.0% to 5.5%; only the facility changes ($125k–$180k median). State the fallback rule (D1). |
| 4 | Model risk (flat curve, one-factor rates, t-tails, US history, our return assumptions) | Aberdeen PM | Put a "What the model can't tell you" box in the Final Report. The *operating-payment* conclusion rests on the bond mechanism, not the model; only the *facility* numbers depend on assumptions, and we show bear/base/bull for those. |
| 5 | Stock picks look disconnected from a bond-heavy plan | Aberdeen PM | Every Trading Note must state the sleeve (growth equity core / conviction / Treasury), the D4 filter it passed, and its weight vs the IPS target. Never trade "because it went up." |
| 6 | Facility contribution may look underwhelming | Laura | Present an **options menu** to Laura (A / B / C80) with our recommendation, so the choice is hers (Client Knowledge criterion). Show the cost of each extra $10k of expected facility in "chance of breaking the promise." |
| 7 | Inflation erodes the $50k payments (real value in 2042 ≈ $34k in 2027 money) | Laura | One paragraph: this sits outside the case's fixed-dollar requirement, but it is flagged for Laura's planning. The flexibility buffer and future business income can top up operations; a TIPS ladder was considered and rejected for the *stated* promise (D3). |
| 8 | Currency: costs in TWD, money in USD | Laura, co-sponsor | Quote the historical USD/TWD range (−11% to +26% over 6 years since 2000). The 20% buffer covers a 15% adverse move. Optionally give the conviction sleeve some Taiwan exposure (D4). |
| 9 | Committed minimum isn't legally binding | Co-sponsor | Recommend a short commitment letter plus a separately titled account holding the 2032 Treasuries. Mention it in the co-sponsor talking points. |
| 10 | Jargon and over-engineering (the repo's council/governance layers) | All | The Final Report uses the plain-English boxes from each D-memo. The software goes in one appendix line, not in the narrative. Judges warned that "overly technical" is not better. |

## Also check
- **AI policy:** every memo here is AI-assisted analysis. Students must write all submitted prose themselves and log AI use (`docs/AI_USE.md` §5). Numbers are fine to use; sentences are not.
- **Unverified facts:** WInS cash and ETF eligibility (Q1–Q3); the iBonds ticker list (D3); longer-dated iBonds launches. Don't state these as fact until checked.
- **Rounding consistency:** use the same figures everywhere. $298k lock cost; $167k median facility (p10 $118k, p90 $230k); $113k / $153–174k for 2031.

## Consistency check across the three deliverables
| Element | Trading Notes (23 Oct) | IPS (6 Nov) | Final Report (4 Dec) |
|---|---|---|---|
| Two-sleeve structure (reserve / growth) | Each trade labelled by sleeve | Formal allocation + ranges | Evaluates it |
| Certainty definition (D2) | — | Stated | Tested with final model run |
| Growth sleeve 80/20, core + 8–12 names (D4) | Trades implement it | Ranges and filters | Performance vs role, not vs index |
| Rebalancing rule (drift > 5 pts from 80/20 → rebalance) | Show one instance if it happens | Stated | Reflected on |
| 2031 lock-70% rule (D6) | — | Stated as policy | Co-sponsor range + draft materials |
| Facility 80% / buffer 20% (D5) | — | Stated | Projected with scenarios |
| Model limitations | — | Brief | Box |

**Sources:**
- [Russell Investments 2026](https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html)
- [Western Asset](https://www.westernasset.com/us/en/research/blog/the-final-phase-of-ldi-cash-flow-matching-2023-02-23.cfm)
- [Wharton: judging and advice](https://globalyouth.wharton.upenn.edu/developing-strategy/)
- [2024 finale (behavioural finance advice)](https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/)
