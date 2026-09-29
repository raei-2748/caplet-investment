# Research Brief: Laura Gao Case, Professional Practice & WInS

*Knox team — Wharton Global High School Investment Competition 2026–27. Compiled 24 Sep 2026.*

---

## 1. Bottom line

1. **Judges reward reasoning, not returns.** Wharton says WInS standings "have little to do with the final outcome." The five published criteria are Investment Strategy, Client Knowledge, Portfolio Analysis, Competition Experience, and Creativity & Presentation.
2. **Professionals would treat Laura as a liability-driven case.** Pension funds, endowments and goals-based wealth managers all use the same design for a client like her: first *hedge the promise* (the $500k operating commitment), then invest the *surplus* for growth (the facility contribution).
3. **Current yields make this unusually cheap.** The 10-yr Treasury is ~5.1%, the highest since late 2023. At ~5.2%, locking in all ten $50k payments would cost about **$297k at the start of 2027**, almost exactly Laura's first contribution. Deciding whether to lock early, in stages, or in 2033 is the core strategic choice.
4. **"High degree of certainty" needs a number and a mechanism.** Planners use 80–90% success rates for goals that can be adjusted. Laura's commitment cannot be adjusted, and pension practice suggests near-100% via cash-flow matching. We should state both a probability and a mechanism.
5. **The 2031 range is a signalling problem.** Fundraising research shows a credible lead gift raises later giving. Laura should promise a conservative floor and then *protect* it after announcing it.
6. **Deadline we were missing:** a **Trading Notes Analysis is due 23 October** (5pm ET). It is not in our `config/wharton_public_2026_27.yaml`.

---

## 2. WInS and the competition: what is verified

| Item | Finding | Confidence |
|---|---|---|
| Timeline | First trading day 28 Sep; roster 9 Oct; **Trading Notes Analysis 23 Oct**; IPS 6 Nov; Final Report + school docs 4 Dec; Final Report instructions released 9 Nov; Global Finale 29–30 Apr 2027. No extensions. | Official (SMApply, Aralia) |
| Performance | "Your team's standings on WInS have little to do with the final outcome." | Official FAQ |
| Top-50 selection | Based on the IPS and Final Report (plus school verification). | Official |
| Rubric (5 categories) | **Investment Strategy** (clear thesis, disciplined planning across time horizons, diversification, IPS consistency) · **Client Knowledge** (tailored, builds confidence) · **Portfolio Analysis** (quant + qual, reasonable assumptions) · **Competition Experience** (teamwork, reflection) · **Creativity & Presentation** (narrative, data use, original thinking) | Official (SMApply deliverables page) |
| Trading Notes purpose | "Demonstrate how your team's investment decisions reflected the strategy it developed." | Official |
| Virtual cash | **$500,000 in 2025–26** (up from $100k). A China-based site (wghs.org.cn) lists $100k for 2026–27. Our `competition.yaml` says $100k. | **Unverified. Check WInS.** |
| Eligible assets | The wghs.org.cn page says "stocks from the approved list only," with Treasuries/TIPS "recommended but not traded on WInS." Wharton's own strategy page implies stocks only. | **Unverified. Check the Box trading-requirements doc.** |
| Judges | Wharton students + professionals from Aberdeen Investments. Past finals judged by practitioners. | Official |
| Scale | 6,300+ teams registered, 2,300 final reports from 79 countries in 2025–26. | Official |

**What past judges said:**
- 2025 (Ladi Ayoola client): the winner (Deerfield) combined SWOT, sentiment analysis and portfolio optimisation with a "human-centred" link to the client's values. A judge said: "What distinguished managers was clear thoughtfulness and reasoning behind all the decisions." The client praised teams for "making the investment plans not just about the numbers."
- 2024 (Hilary Ash): judges noted the efficient frontier, correlations and ML used by finalists. Their advice was to consider **behavioural finance** (the client's emotions in downturns) and the client's **total financial picture**.
- 2023 (Peter Wang Hjemdahl): the winner (TJHSST) used ESG as a "critical pillar." That case included recurring $5–10k annual grants from Year 5, the closest past analogue to Laura's case.
- Wharton's guidance: "developing a strategy and sticking with it… is the best approach." Avoid over-trading and panic selling. A vague strategy is not competitive.

**Implication for us:** if WInS is stocks-only, the Treasury reserve cannot be traded. The WInS account then represents the **growth part** only, and the IPS must say so explicitly. The reserve can then be shown on paper as a Treasury ladder (the case asks for its "size and initial asset composition," not trades). If bond ETFs are allowed, we can hold iBonds in WInS to show it.

---

## 3. How professionals handle a client like Laura

### 3.1 The frameworks

| Framework | Who uses it | How it maps to Laura |
|---|---|---|
| **Liability-driven investing (LDI) / surplus investing** | Corporate pensions, insurers | Split assets into a *liability-hedging portfolio* and a *return-seeking portfolio*. Russell Investments (Jul 2026): "any surplus strategy should begin by preserving benefit security through a robust liability hedge," after which surplus can be run "with a more total-return mindset." |
| **Cash-flow matching (dedicated portfolio)** | Pensions near the end of their life, endowment spending | A bond ladder whose coupons and maturities pay each obligation. No rebalancing, no forced selling. It has become affordable again because yields are high (Western Asset). |
| **Goals-based wealth management / risk buckets** | Private banks (Merrill, Fidelity, TD) | Chhabra's *Beyond Markowitz* uses three buckets. **Personal/safety** (Laura's operating reserve), **market** (diversified growth that funds the facility), and **aspirational** (upside: the facility beyond the floor). Brunel's goals-based wealth management ranks goals as needs, wants and wishes, each with its own required confidence. |
| **Bucket / time-segmentation strategies** | Retirement planners | Near-term spending sits in cash or bonds, long-term money in equities (Morningstar compares these approaches). |
| **Funded-status glide paths** | Pensions | Risk falls as funded status rises (for example, 70% return-seeking when underfunded down to ~20% at 110% funded). This maps to Laura: the more the growth part outperforms, the more of it we lock in. |

### 3.2 Current market: why timing matters

US Treasury par curve, 23 Sep 2026: 1Y 4.49%, 2Y 4.85%, 5Y 4.99%, **7Y 5.05%, 10Y 5.11%**, 20Y 5.45%, 30Y 5.40%. TIPS real yields, 22 Sep: 7Y 2.56%, 10Y 2.63%. Implied inflation is therefore ~2.5%.

Cost of the $500k commitment (ten $50k payments, starts of 2033–2042):

| Flat yield | Needed at start of **2027** | Needed at start of **2033** |
|---|---|---|
| 4.5% | $318k | $413k |
| 5.0% | $303k | $405k |
| 5.2% | $297k | $402k |
| 5.5% | $288k | $398k |
| 3.0% (if rates fall) | — | $439k |
| 0% | — | $500k |

**The key trade-off:** hedging the whole commitment early would use essentially all of the 2027 $300k, leaving only the 2028 $150k plus later gains for the facility. Waiting until 2033 leaves more money growing, but risks both an equity crash *and* lower rates, which raise the reserve's cost at the moment it is bought.

**Implementation tools professionals use:**
- **Individual Treasury notes/bonds held to maturity**, one per year 2033–2042. This is the cleanest option: no credit risk, and fixed nominal payments are matched by nominal Treasuries. **TIPS are not needed for the reserve**, because the payments are *not* inflation-adjusted.
- **iShares iBonds term Treasury ETFs**, which mature and pay out their NAV in the named year. The line-up currently runs to **Dec 2036 (IBTR)** and includes IBTO 2033, IBTP 2034 and IBTQ 2035, so they cover roughly the first four payments. Later years need individual bonds or a duration-matched long Treasury position.
- STRIPS are a textbook fit but are listed as prohibited on the wghs.org.cn rules page, so avoid naming them as the main tool.
- Pensions sometimes add investment-grade credit for extra yield (Cambridge Associates). For a "high certainty" mandate, Treasuries are more defensible.

### 3.3 Defining "a high degree of certainty"

- Planners commonly target **~80–90% probability of success**. Kitces shows that such figures overstate risk only when the client *can adjust* (guardrails). **Laura cannot adjust**: payments are fixed and outside funding is banned. The benchmark should therefore be close to pension-style full hedging.
- A defensible definition could have two layers:
  1. **Mechanism:** the reserve is a Treasury ladder held to maturity, so there is no market or reinvestment risk after 2033 (only US government default risk).
  2. **Probability:** before 2033, the chance the portfolio is worth less than the cost of the reserve is **≤ 2.5–5%** under stated assumptions, stress-tested with historical crises (2008, 2022) and not just normally distributed simulations. Advisor Perspectives and Income Lab both criticise over-reliance on Monte Carlo.
- Report results as **dollar guardrails**, as Kitces recommends. For example: "If the portfolio falls below $X in 2031, we increase the hedge to 100% and cut the facility range to $Y."

### 3.4 Communicating with co-sponsors (2031)

- **The evidence supports a credible lead gift.** List & Lucking-Reiley (2002, university capital campaign field experiment): raising seed money from 10% to 67% of the goal increased later contributions nearly sixfold. Vesterlund (2003) and Andreoni (1998) model early and leadership gifts as *signals of quality*. Krasteva & Saboury (2021) show seed money works best as a signal when early donors have limited information, which describes co-sponsors of a new Taiwanese residency.
- **Credibility is asymmetric.** Falling short of a promise costs more than beating it. Professionals therefore state a **floor they can guarantee plus a stretch amount**, not a symmetric range.
- **Suggested approach:** in 2031, announce a range whose floor is the facility amount we can protect (for example, the 10th–25th percentile of the simulated 2033 surplus), then **move that floor into short Treasuries or iBonds maturing in 2033**. The floor is then locked in, and only the upside stays exposed to markets. This follows the pension "lock in gains as funded status rises" logic.
- The case also asks for **draft fundraising text**. Keep it plain and honest: a floor, a likely amount, and what drives the upside.

### 3.5 Creative-entrepreneur clients

- Wealth managers who work with creatives stress **irregular income** (advances, royalties, speaking fees), which calls for large cash buffers and diversified revenue. Laura's living costs are outside the portfolio, but her **2028 $150k contribution comes from "publishing advances, speaking engagements, licensing."** Although the case says she "will contribute," a strong report can stress-test a delay or a smaller amount.
- **Human-capital concentration:** Laura's income depends on publishing, education and media. Professionals avoid adding portfolio risk in the same direction, for example by being overweight publishing or media stocks, though a values-aligned theme is still fine in moderation.
- Values: identity, belonging, education, community, Asian-American voice, Taiwan. Past winners linked holdings to the client's values without letting values override the financial logic.

### 3.6 Inflation and currency (the case asks for assumptions on these)

- **Reserve:** payments are fixed nominal USD, so inflation does not raise the reserve's cost. Inflation lowers the real value of each $50k, which is Laura's problem and not a funding risk, but it is worth one sentence in the report.
- **Facility:** costs are in Taiwan. Taiwan CPI was +2.20% y/y in May 2026, and the central bank forecasts 1.80% CPI for 2026. Real-estate and construction costs can run higher. The facility contribution should be shown in both nominal and 2027 dollars.
- **Currency:** the facility will be paid for in **TWD**. A USD→TWD move changes how much residency the contribution buys. This is worth a short paragraph, even though the case does not require a hedge.

---

## 4. Strategic options for our IPS

| Option | Description | Pros | Cons |
|---|---|---|---|
| **A. Lock early** | Build the full Treasury ladder in 2027 (~$297k at ~5.2%); everything else goes to growth | Near-100% certainty from day one; simple story; uses today's high yields | Leaves ~$150k plus growth for the facility; heavily bond-weighted, so less to show in WInS |
| **B. Staged hedge with triggers** | Hedge ~50–60% in 2027, raise to 100% by 2031–33, faster if funded status improves (pension glide path) | Balances certainty and growth; strong "disciplined framework" story for judges | More complex; must define trigger rules clearly |
| **C. Buy at 2033** | Balanced growth portfolio until 2033, then buy the ladder | Highest median facility contribution | Exposed to both equity and rate risk (~8–14% chance of falling short in our earlier simulation); weakest on "high certainty" |

**Working recommendation:** Option B, with Option A's numbers as the "certainty floor" benchmark. It gives the clearest story across all three deliverables. The Trading Notes can show the growth part being built; the IPS can set out the hedge ratio, triggers and definition of certainty; and the Final Report can give the 2031 range, the floor-locking rule and the co-sponsor text.

---

## 5. Open items to check this week

1. WInS starting cash and eligible securities (read the Box trading-requirements document on SMApply).
2. Add the **23 Oct Trading Notes Analysis** deadline to `config/wharton_public_2026_27.yaml`.
3. Download the approved securities list into `competition/official/2026_27/`.
4. Replace the demo `client_mandate.yaml` with Laura's actual mandate.
5. Decide as a team between options A, B and C before the IPS draft.

---

## Sources

**Competition**
- [Wharton Global Youth: Investment Competition](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/)
- [General Rules & Roles](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/)
- [FAQ](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/)
- [SMApply: Deliverables & evaluation criteria](https://wghsinvcomp.smapply.us/res/p/deliverables/)
- [Developing a Strategy](https://globalyouth.wharton.upenn.edu/developing-strategy/)
- [Top 50 2026 teams / $500k virtual cash](https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/)
- [Archive of past clients & winners](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/)
- [2025 champion: BAM Investing (Deerfield)](https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/)
- [2024 finale: Spark Investments](https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/)
- [2023 finale: DMV's Finest](https://globalyouth.wharton.upenn.edu/news/the-2023-investment-competition-global-finale-ends-in-sweet-victory-for-dmvs-finest/)
- [2026 global champions](https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/)
- [Case study 2022–23 (Peter Wang Hjemdahl)](https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2022-2023/)
- [Aralia: 2026–27 guide](https://www.aralia.com/helpful-information/guide-to-the-wharton-global-high-school-investment-competition/)
- [wghs.org.cn rules (unofficial, unverified)](https://en.wghs.org.cn/rules)

**Professional practice**
- [Russell Investments: Pension surplus investing (Jul 2026)](https://russellinvestments.com/content/ri/us/en/insights/russell-research/2026/07/pension-surplus-investing-value-overfunding.html)
- [Western Asset: The final phase of LDI, cash-flow matching](https://www.westernasset.com/us/en/research/blog/the-final-phase-of-ldi-cash-flow-matching-2023-02-23.cfm)
- [Cambridge Associates: Constructing a liability hedging portfolio](https://www.cambridgeassociates.com/insight/liability-hedging-portfolio/)
- [CFA Institute: Liability-driven and index-based strategies](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2025/liability-driven-index-based-strategies)
- [Wikipedia: Dedicated portfolio theory](https://en.wikipedia.org/wiki/Dedicated_portfolio_theory)
- [Chhabra: Beyond Markowitz (SSRN)](https://www.ssrn.com/abstract=925138)
- [Brunel: Goals-Based Wealth Management](https://www.perlego.com/book/999615/goalsbased-wealth-management-an-integrated-and-practical-approach-to-changing-the-structure-of-wealth-advisory-practices-pdf)
- [Morningstar: Bucket strategies comparison](https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/blt2da7af775da0d57e/65aacbb9c7bb160246a29912/Bucket_Strategies_Comparison_(3)_(1).pdf)
- [BlackRock: Pension glide paths](https://www.blackrock.com/institutions/en-ca/insights/thought-leadership/pensions-perspectives)
- [Kitces: Monte Carlo for one-time vs ongoing plans](https://www.kitces.com/blog/monte-carlo-one-time-vs-ongoing-retirement-planning-probability-of-success-guardrails/)
- [Advisor Perspectives: The dangers of Monte Carlo simulations](https://www.advisorperspectives.com/articles/2023/01/10/the-dangers-of-monte-carlo-simulations)
- [Income Lab: Why probability of success is wrong](https://incomelaboratory.com/why-probability-of-success-is-wrong/)
- [iShares: Build better bond ladders with iBonds](https://www.ishares.com/us/strategies/bond-etfs/build-better-bond-ladders)
- [iShares iBonds Dec 2033 Term Treasury ETF (IBTO)](https://www.ishares.com/us/products/332291/ishares-ibonds-dec-2033-term-treasury-etf)
- [iShares iBonds Dec 2036 Term Treasury ETF (IBTR)](https://www.ishares.com/us/products/350028/ishares-ibonds-dec-2036-term-treasury-etf)
- [Krasteva & Saboury (2021): Signalling value of seed money](https://ideas.repec.org/a/eee/pubeco/v203y2021ics0047272721001377.html)
- [Andreoni: Leadership giving in charitable fund-raising](https://ideas.repec.org/a/bla/jpbect/v8y2006i1p1-22.html)
- [Wealthspire: Financial planning for creatives](https://www.wealthspire.com/blog/the-art-of-financial-planning-for-artists-entertainers-and-creatives/)

**Market data**
- [US Treasury: Daily par yield curve (Sep 2026)](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202609)
- [US Treasury: Daily real yield curve (Sep 2026)](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value_month=202609)
- [CNBC: 10-yr yield highest since Nov 2023 (2 Sep 2026)](https://www.cnbc.com/2026/09/02/bond-yields-treasurys-inflation.html)
- [DGBAS: Taiwan price indices, May 2026](https://eng.dgbas.gov.tw/News_Content.aspx?n=4438&s=236327)
- [CBC Taiwan: Inflation outlook 2026](https://www.cbc.gov.tw/en/dl-227016-0dddfe3fc61a43c1bc631de9adcef2fc.html)
