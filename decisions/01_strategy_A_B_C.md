# D1: Which overall strategy: lock early (A), staged hedge (B), or build in 2033 (C)?

**Status:** DECIDED: Strategy A, "Lock, then grow" · **Evidence:** `outputs/laura/tables.md`, `outputs/laura/results.json` (`grid`, `history`, `sensitivity.y0`, `sensitivity.contribution_2028`) · Charts 01, 02, 03, 05

## Question
How should Laura's $450k be run between 2027 and 2033? It must fund ten fixed $50k payments (2033–2042) "with a high degree of certainty" and leave as much as responsibly possible for the facility.

## Options
| | Description |
|---|---|
| **A: Lock early** | In Jan 2027, use the $300k to buy a Treasury ladder: one maturity per payment, held to maturity. If it costs more than $300k, top it up from the 2028 $150k. All other money goes to an 80/20 growth sleeve. |
| **B: Staged hedge** | Hedge 50% in 2027, rising to 100% by 2031. Lock 100% early if assets reach 125% of the reserve cost. The unhedged money sits in the growth sleeve. |
| **C60 / C80: Build in 2033** | Run a 60/40 or 80/20 portfolio until 2033, then buy the ladder. This is the "conventional advisor" approach and matches how the case frames the 2033 set-aside. |

## Evidence (model, 20,000 paths per cell; history = 93 real 6-year windows 1928–2025)
| Base case | P(10 payments funded) | Facility p10 | p50 | p90 |
|---|---|---|---|---|
| A: Lock early | **100.00%** | $118k | $167k | $230k |
| B: Staged hedge | 99.98% | $110k | $167k | $240k |
| C60 | 97.16% | $58k | $182k | $329k |
| C80 | 93.12% | $26k | $187k | $392k |

- **Bear case + inflation regime:** A stays at 100% funded (p50 $152k). C80 falls to 86.6% (p50 $133k), with an average shortfall of about $70k when it fails.
- **Historical replay** (actual S&P 500 returns and 10Y yield changes applied to today's yields): A funds 93/93 windows, worst surplus +$102k (1928). C60 funds 92/93. C80 funds 90/93, worst −$102k (the 1929 crash).
- **Rate timing:** Jan-2027 yields are unknown. If the starting yield is 4.0%, the ladder costs $333k. A still funds 100% by using $33k of the 2028 money; its median facility falls to $125k (C60: $161k). At 5.5% the ladder costs $288k and A's median rises to $180k.
- **If the 2028 $150k never arrives:** A still funds 100%; B 56%; C60 60%. See D8.
- **Why A costs so little:** with Treasuries yielding ~5%, the ladder already earns close to what a balanced portfolio is expected to earn. J.P. Morgan's 2026 long-term forecasts: 60/40 = 6.4%, intermediate Treasuries = 4.0%, US large cap = 6.7%. Vanguard expects 4.2–6.2% a year for US equities over 10 years. The extra return from taking risk before 2033 is small, but the damage it can do to the promise is large.

## Debate (3 rounds)
**Round 1**
- **Advocate (A):** The case's first requirement is non-negotiable and has no outside backstop. Pension funds with a fixed promise and enough money to cover it do exactly this: they hedge the promise and invest the surplus (Russell Investments, 2026; Western Asset on cash-flow matching). Yields near 5% make the hedge the cheapest it has been since 2007. A is the only option with zero failures in simulation, in history, and under the missing-contribution stress.
- **Opponent (for C/B):** Laura is an entrepreneur who "takes thoughtful risks." C80 has a median $20k higher and a p90 $160k higher. Locking everything in 2027 looks timid, and judges may read "we bought bonds" as no strategy at all. The case also *says* the reserve is set aside in 2033.

**Round 2**
- **Advocate:** The +$20k median comes with a 1-in-15 chance (base case) to 1-in-7 chance (bear case) of failing a promise Laura cannot renegotiate. A still takes risk, but only with money that is *not* promised: the whole $150k second contribution plus any surplus. The case says she *formally* sets aside the reserve in 2033; it doesn't forbid buying the bonds earlier. We'd be buying in 2027 exactly the assets she will hold in 2033.
- **Opponent:** Then take B. It keeps 50% of the upside flexibility and still reaches 99.98%.

**Round 3**
- **Advocate:** B's extra upside is tiny: +$10k at p90 and the same median. It loses $8k at p10 and falls to 56% funded if the 2028 money never comes. B also needs trigger rules that judges will call over-engineered. A is simpler, stronger on every downside measure, and easier for Laura to understand.
- **Opponent (final):** A depends on Jan-2027 yields. If rates fall sharply before then, the logic weakens.
- **Advocate:** Agreed. We state that as the rule that would change our mind (below).

**Judge (sceptical Aberdeen PM; scored on the five Wharton criteria)**
- **Investment Strategy:** A. Clear thesis, disciplined, consistent across time horizons.
- **Client Knowledge:** A. It separates what Laura *must* do from what she *hopes* to do, which matches her own words: "balance between pursuing growth and protecting the capital required."
- **Portfolio Analysis:** A. It is backed by simulation, history and sensitivity, and C's attraction is quantified rather than ignored.
- **Creativity:** A, provided the team tells the "two cheques" story.
- **Verdict: A.** Keep B as the documented fallback if yields are below ~4% in Jan 2027.

## Strongest counter-argument
Most of Laura's money sits in bonds until 2033, so the facility depends mainly on one $150k cheque. If equities boom (bull case), C80's median facility is $233k against A's $181k. We are deliberately accepting that lower upside in exchange for certainty.

## Decision
**Strategy A, "Lock, then grow."**
1. **Jan 2027:** buy the Treasury ladder for all ten payments (≈ $298k at today's yields). Any remainder goes to the growth sleeve.
2. **Jan 2028:** top up the ladder if it wasn't fully bought, then invest the rest of the $150k in the growth sleeve (80/20, see D4).
3. **2031:** apply the announce-then-protect rule (D6).
4. **2033:** formally designate the ladder as the operating reserve and contribute 80% of the surplus to the facility (D5).

## What would change our mind
- **Jan-2027 yields below ~4.0%** (ladder costs > $333k): switch to B, hedging about 70% and rising to 100% by 2031. The model shows B with a 70%→100% schedule gives 100% funded with a similar median.
- **Laura saying the facility matters more to her than certainty** on the operating payments. This contradicts the case, but we would ask.
- **Evidence that the 2028 contribution will be much larger than $150k** would make C-style risk more affordable.

## Plain English for Laura (3 sentences)
Your first $300k buys US government bonds that pay out exactly $50k at the start of each year from 2033 to 2042, so the residency's running costs are locked in no matter what markets do. Your second $150k, plus anything left over, is invested for growth and becomes your contribution to the building. Taking more risk with the whole portfolio would only add about $20k on a typical outcome, while creating a real chance of breaking the one promise you can't renegotiate.

**Sources:**
- [Russell Investments: Pension surplus investing (Jul 2026)](https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html)
- [Western Asset: Cash-flow matching](https://www.westernasset.com/us/en/research/blog/the-final-phase-of-ldi-cash-flow-matching-2023-02-23.cfm)
- [J.P. Morgan 2026 LTCMA press release](https://am.jpmorgan.com/us/en/asset-management/institutional/about-us/media/press-releases/jp-morgan-releases-2026-long-term-capital-market-assumptions/)
- [Vanguard return forecasts (30 Jun 2026)](https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html)
- [US Treasury par yield curve, 23 Sep 2026](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202609)
- [Damodaran historical returns 1928–2025](https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls)
