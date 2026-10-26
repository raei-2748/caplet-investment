# FICTION. Team Keel: the ideas ledger

> Every investment concept someone brings to the team gets a row: who brought it, the argument, the verdict for
> Laura's case and why. Kai keeps it (he brings most of them, from his reading pile); Tess checks the wording.
> The Portfolio Analysis criterion asks for "understanding and effective use of investment concepts and tools"
> (`competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md:53`). A rejected idea, with its reason, is evidence of that too.
> Verdicts: **ADOPTED**, **ADAPTED** (used in a changed form), **REJECTED**, **PARKED** (waits for evidence or a later deliverable).

| # | Concept | Brought by | Ep | For it | Against it | Verdict for Laura | Why, in one line |
|---|---|---|---|---|---|---|---|
| I-01 | The yield curve, bootstrapped into discount factors | Jun | 1 | Prices each payment at its own date's rate | Needs a fresh curve every day | ADOPTED | Ten payments on ten dates need ten prices, not one average rate |
| I-02 | Duration matching (immunisation) with bond index funds (IEF + TLT) | Jun | 3 | Simple, two tickers, matches the payments' interest-rate sensitivity | Index funds never mature, so the match drifts and must be rebalanced | REJECTED | Laura needs cash on ten dates, not a matching sensitivity today |
| I-03 | Cash-flow matching: one bond or term fund per payment | Kai | 3 | Each payment has an owned asset that turns into cash just before it is due | WInS lists no Treasury maturing 15 Feb 2031 to 15 Feb 2036 | ADAPTED | Bonds where they exist; term Treasury funds (iBonds) for the gap |
| I-04 | Bid-ask spreads and limit orders | Jun | 4 | After-hours quotes can be far from fair value | Limit orders may not fill | ADOPTED | Trade in U.S. hours, with limits, and check each bond's yield against the curve |
| I-05 | Modern portfolio theory (Markowitz 1952): choose the mix on the efficient frontier | Kai | 6 | The standard way to balance return and risk; diversification is free | Optimises asset return and variance; Laura's problem is dated payments, not variance | REJECTED as the method; diversification kept | The payments come first; MPT can only describe the sail, not the plan |
| I-06 | Liability-driven investing: hedge the promises first, then take risk with the surplus | Felix (found it in a pension report Kai lent him) | 6 | Exactly Laura's shape: fixed payments, then a surplus | Jargon a co-sponsor will not know | ADAPTED | The idea is the plan; the name never goes in a deliverable ("keel and sail" instead) |
| I-07 | Sequence-of-returns risk | Kai | 9 | A bad year just before money is needed does the most damage | Not relevant if the payments never depend on stocks | ADOPTED | The reason the sail never funds a payment |
| I-08 | Global diversification over home bias (one world fund) | Kai | 11 | Thousands of companies, many countries, one low fee | U.S. funds are more familiar | ADOPTED | Laura's growth should not depend on one country |
| I-09 | A Taiwan fund for the sail ("she's moving there") | Amara | 11 | Emotional fit with the residency | Her career, her project and her move are already tied to Taiwan; more Taiwan concentrates the risk | REJECTED | Don't add risk that is correlated with her own life (human capital) |
| I-10 | The Sharpe ratio as the target | Kai | 12 | One number for return per unit of risk | Says nothing about whether the payments are met | REJECTED | Our test is "paid in full", not "efficient" |
| I-11 | Two buckets (mental accounting) | Amara | 14 | Laura and co-sponsors understand "the promise money" and "the building money" at once | Economists call bucketing a bias | ADOPTED for explaining, not for deciding | The buckets are real here because the cash flows are dated |
| I-12 | Kelly criterion for the sail | Kai | 16 | Maximises long-run growth | Needs known odds; full Kelly is ruinous with estimation error | REJECTED (in nine minutes) | Kai's own verdict: "I just wanted to say Kelly in a meeting" |
| I-13 | Dollar-cost averaging the 2028 money into stocks | Kai | 17 | Less regret if markets fall right after January 2028 | On average lump sum invested earlier does better; adds rules to explain | PARKED to the sail vote (25 Oct) | Amara's point about regret is real; Jun wants numbers first |
| I-14 | History windows as well as models | Jun | 19 | History has crashes in it; smooth models do not. First test: the ladder priced on every 2026 curve cost more than $300k on 173 of 198 days | History is one path | ADOPTED | Every MODEL number gets a check against real history before it is quoted |
| I-15 | A glide path for the operating reserve (2033-42) | Jun | 20 | Standard for target-date funds | The ladder already runs down: one rung paid each year, nothing sold | REJECTED | The reserve's composition changes by maturity, not by selling |
| I-16 | Barbell: very safe bonds plus very risky stocks, nothing in between | Kai | 22 | Matches keel + sail | It is what the plan already is; the label adds nothing | REJECTED as a label | "We don't need a new word for our own plan" (Tess) |
| I-17 | Currency risk (USD against TWD) | Amara | 23 | The facility's costs will be in Taiwan dollars | No derivatives allowed; facility cost estimates are out of scope | PARKED for the Final Report | State it as an assumption about facility costs |
| I-18 | Inflation: nominal payments, real building costs | Amara | 25 | The case asks for it | No TIPS allowed | ADOPTED as an assumption | Payments are nominal (case :90); inflation goes in the Final Report's assumptions (:147) |
| I-19 | Coupon reinvestment risk | Kai | 26 | Real Treasuries pay coupons before 2033 | Small next to the ladder | ADOPTED | Named as the one remaining risk in the certainty definition |

## Kai's reading pile (what he has actually read, by Sydney date)
- 28 Sep: the WInS FAQ and Session Rules (all of it, for once).
- 30 Sep: a pension fund's liability-matching explainer; Markowitz's 1952 paper "Portfolio Selection" (Journal of
  Finance), the first three pages, and then a textbook chapter on it.
- 5 Oct: chapters on sequence risk from a retirement-planning textbook.
- 8 Oct: a textbook chapter on human capital (why a portfolio should not double the risks in your own life).
- 9 Oct: the Sharpe ratio, between customers at the shop.
- 13 Oct: Kelly's 1956 paper "A New Interpretation of Information Rate" (he says he read it; Jun says he read the
  abstract).
- 19 Oct: barbell portfolios.
- 21 Oct: the J.P. Morgan 2026 Long-Term Capital Market Assumptions (the USD matrix).
| I-20 | One dial: the cost moves about $289 per 0.01% in the 10-year (DV01) | Jun | 27 | Lab L-01: worst miss $652 over 20 closes | Curves twist (Kai's roast) | ADOPTED for explaining | One number a judge can hold; numbers stay out of the IPS |
| I-21 | Defence in depth: back-ups must be independent | Felix (from Kai's pile) | 27 | Nuclear safety's oldest rule; explains why order alone is not enough | Our layers share one cause (falling yields) | ADOPTED as a test, not a label | Where the analogy breaks names the one layer that doesn't fall with yields: a Treasury buffer |
| I-22 | Freeze list: every rule the Final Report will use must already be a sentence in the IPS | Felix | 28 | IPS file :68-70, :73-76; case :96-104, :117-120, :146-148 | No line requires a review rule (Kai); it is Felix's reading | ADOPTED as a check before each IPS version | Found the one missing rule (review) in Keel's own v1 |
| I-23 | One sheet, one edition: every number said aloud carries its curve date and forecast edition | Tess (Rooftop), Jun | 29 | Four of five fixes in a week were Keel's own dates; buffer on 7.0%, sail on 7.5% | "Half a point changes nothing" (Kai) | ADOPTED | Splits the vote: the rule doesn't depend on the edition, the size does |
| I-24 | A buffer is a lower quote with a name: test any safety layer against its plain twin | Kai | 30 | Courtroom C-01: $10k buffer and a $10k lower quote both give 0.11% below the quoted bottom | Jun: the buffer leaves Laura $8.3k in her worst years | ADOPTED (margin); buffer moved to "who owns the slack" | The payments are covered either way once the floor is last |
