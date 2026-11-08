# Case map: everything the Final Report must answer, and the research behind each (Sun 8 Nov 2026)

Book 15: "Every single part of our Final Report MUST be underpinned by a breathtaking level of research and
analysis." This page lists every requirement the case and Wharton place on the report, the questions (Q1-Q14 in
`README.md`) and store tags (`research/INSIGHT_STORE.md`) that feed it, and the analysis still open. Wharton's Final
Report instructions (Tue 10 Nov, 01:00 Sydney) will be added as section E the day they arrive. This is a planning
page, not report text. The IPS this page uses is the one in the "Past Submissions" tab of Caplet's FINAL REPORT doc,
checked word for word against `FINAL_IPS_as_submitted.txt` on 8 Nov.

## A. What the case requires (Client Case Study, `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`)

| # | Requirement (case words) | Questions | Tags | Open analysis |
|---|---|---|---|---|
| A1 | The operating reserve: "recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made" | Q2, Q3, Q7, Q9 | LADDER, RESERVE2033, REINVEST | Its size in 2033 on the FINAL design and the 6 Nov curve; what it holds (T-bonds and iBond ETFs, rung by rung); how it runs down with no rebalancing; what the residency needs from it, seen from its side (Q9) |
| A2 | "Define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" | Q2, Q8 | CERTAINTY, REINVEST | Caplet's definition is structural ("barring a US default, none ... will depend on a share price, or on anybody else's money"). Test it four ways: structure, models across four kinds of market, history, and what engineers and insurers mean by certainty (Q8). Two honest limits to reconcile: iBond ETFs pay their net asset value, not par (TNA note 2; iShares says IBTM "does not seek to return any predetermined amount at maturity"); and interest received before it is needed must be reinvested (TNA note 1's 10.5-month gap) |
| A3 | Facility contribution: "recommend and justify the extent to which Laura can responsibly contribute, based on their investment strategy, projected portfolio outcomes, assumptions, and understanding of her goals" | Q3, Q5, Q6, Q9 | FLOOR, CEILING, HALFKEPT | The bottom (the 2032 Treasury fund's payout) and the top (plus the promised half of VT, moved into Treasuries before 2031), with numbers on the FINAL design; why that is "responsible" |
| A4 | "Committing all remaining assets could limit her financial flexibility as the project develops" | Q5, Q9, Q10 | HALFKEPT, RESIDENCY, INFLATION_TWD | Is half right? Test 30%, 50%, 70%; what overruns, a stronger Taiwan dollar and a co-sponsor shortfall could each cost (reference classes, Q5 and Q10) |
| A5 | The 2031 range: "recommend the dollar range Laura should communicate and state how confident they are that her 2033 contribution will fall within that range" | Q4, Q6, Q11 | COSPONSOR, MOVE2031 | How the 2031 move shapes the range: once the promised half is in Treasuries, both ends are owned; what confidence that supports, and what still moves between 2031 and 2033 (the iBond payout, nothing else?). How to say "how sure" so people hear it right (Kent, Gigerenzer, fan charts) |
| A6 | "Explain how favorable and unfavorable market outcomes could affect the amount she can provide" | Q3, Q6 | CEILING, COSPONSOR | Good and bad markets before 2031 move only the top; after the move, nothing moves it. Show with history (1929, 1973-74, 2000-02, 2008, 2020, 2022) and the four model worlds |
| A7 | "The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment" | Q2, Q3 | CERTAINTY, FLOOR | The range is drawn only from money outside the ladder; show that no outcome of the range can touch a payment |
| A8 | "Draft part of Laura's fundraising materials describing this potential contribution for prospective co-sponsors" | Q4, Q11, Q12 | FUNDRAISING, COSPONSOR, LAURA | What good case-for-support writing does; what a founder's committed money signals; how to state a range and its confidence in a donor document; Laura's own voice and values (public sources only) |
| A9 | Strategy must: support the commitment with high certainty; determine a responsible facility contribution; address how uncertainty affects both; communicate the contribution clearly and credibly; preserve flexibility | all | all | The report's spine: one argument (EXPECTATIONS 2.9) |
| A10 | Assumptions on "investment performance, the timing of cash flows, outside funding, the effect of inflation on portfolio projections and facility costs, and the financial flexibility Laura should preserve"; favourable and unfavourable outcomes | Q6, Q10, Q12 | CEILING, INFLATION_TWD, REINVEST | One assumptions table, every figure sourced. Return: the TNA's 7.5% is J.P. Morgan's 2027 estimate for global equities (press release 19 Oct 2026, "increasing from 7.0%"; settled 27 Oct, `../office/outbox/2026-10-27_noticeboard_7-5-is-world-stocks.md`); the 2026 edition's 7.50% for EAFE is a coincidence of editions. Test about 4% to 10% around it. Inflation: US CPI against Taiwan CPI and Taiwan's construction cost index. Outside funding: none for the payments, by design |
| A11 | "Evaluates how that strategy was implemented" (the WInS portfolio) | Q13 | PROCESS | What the WInS book shows (IBTM, the T-bond ladder, VT 8.6%), what it could not show (no 2028 deposit, no Treasuries for some years), the trades of 7-8 Oct, what the Trading Notes tested. WInS gains never enter Laura's projections |
| A12 | Projections start from $300,000 in 2027 and $150,000 in 2028 with "reasonable return assumptions consistent with their strategy" | Q6 | all numbers | One engine, one curve (6 Nov close), Caplet's design as written |
| A13 | Out of scope: the facility's cost, a construction budget, the funding gap, a business plan, taxes, Taiwan's legal rules | Q9, Q10 | RESIDENCY, INFLATION_TWD | Research on residencies and Taiwan informs flexibility and the co-sponsor text; it never estimates the building's cost |

## B. What Wharton's five criteria ask of the report (`../WHARTON_WORD.md` section 1)

| Criterion | What it rewards | Where the research comes from |
|---|---|---|
| Investment Strategy | A clear, creative thesis; planning across changing horizons and cash needs; diversification; consistency with the IPS | Q1-Q7; the lineage of each plan part (EXPECTATIONS 2.4) |
| Client Knowledge and Objectives | Tailored to Laura's circumstances, priorities, risk and residency goals; earns her confidence | Q1, Q9, Q10, Q12 |
| Portfolio Analysis | Concepts and tools used well; quantitative and qualitative together; reasonable assumptions; funding reliability, facility contribution and flexibility under varying markets | Q2-Q8; the numbers engine |
| Articulation of Competition Experience | Teamwork, communication, learning; research and decision process; growth and response to challenges | Q13; Caplet's own sentences (asked for by Sun 22 Nov); real events only |
| Creativity and Presentation | A compelling, organised narrative in an authentic team voice; data used well; original thinking; the co-sponsor communication clear and credible | Q11, Q14; voice studies 1-3 |

## C. Open analysis found while gathering the old research (to settle before Thu 26 Nov)

1. **Reinvestment under Caplet's design: the largest open question.** A ladder of coupon bonds costing about
   $300,000 delivers $50,000 a year only if its coupons are reinvested: a T-bond bought for about $30,000 reaches
   $50,000 in 2038 only with ten years of coupons reinvested on the way. So the payments depend on future Treasury
   rates as well as on default, and Caplet's FINAL has no rule for a shortfall (TNA note 1 names the risk). Wharton
   bars revising the strategy, so the report can measure, explain and implement within the IPS's words, but cannot add
   a new rule. Work to do: (a) size the risk on the 6 Nov curve under the FINAL design (old-design figure: about $21,000
   if yields fall 2 points for good); (b) test the implementation the IPS's words allow: a cash-flow-matched ladder in
   Leibowitz's sense, where each later bond's coupons pay the earlier payments as they fall due, leaves only the
   2027-2032 coupons to reinvest. Keel's harvest brief flagged "later coupons paying earlier payments" as a clash; that
   was too strict, because the FINAL only says each Treasury matures "just before it's needed" and TNA note 2 says each
   payment "rests on a dedicated instrument", which stays true. Decide on Mon 16 with the numbers, log the call in
   `pm/ASK_HUMANS.md`, and show Caplet the reasoning in the 28 Nov draft; (c) the case's own order helps: the operating
   reserve is set aside in 2033 before the facility contribution, and Caplet's choice to fill the ladder with the 2028
   deposit's first dollars shows the same priority. (d) Lineage: Fisher and Weil, Redington, Leibowitz's dedicated
   portfolios, municipal escrows "sufficient without reinvestment", Damodaran's two conditions for a riskless asset.
2. **"Pay what they say" against "net asset value, not par".** The FINAL says the Treasuries "pay what they say" and
   the bottom is promised "without doubt"; TNA note 2 says the iBond payout is a net asset value. The report must state
   the bottom in a way that is true for an iBond ETF (for example, rounded down from its expected payout) and say why
   the gap is small.
3. **The ladder's cost now.** On the 6 Nov close the ten payments cost $301,544 on 1 Jan 2027 (MODEL), so the 2028
   deposit's first dollars finish the ladder, exactly as the FINAL says. Old research that says "under $300,000" or
   "the 2028 deposit never funds payments" is out of date.
4. **The 7.5% figure** (A10): settled. J.P. Morgan, 2027 Long-Term Capital Market Assumptions, press release 19 Oct
   2026: "Global equities are projected to return 7.5% (USD), increasing from 7.0%." The matrix itself (compound or
   arithmetic) sits behind a login, so the report says "J.P. Morgan's estimate for global shares" and never "compound".
5. **The 2031 move:** into which Treasury, when, and what the 2031 range then is. After the move both ends are owned;
   is the communicated range then floor to floor-plus-promised-half, with near-certain confidence, and what is the
   honest residual risk?
6. **A missed or smaller 2028 deposit** (one of the two reasons to change): what exactly changes, in order.
7. **Caplet's own use of the half kept back.** The FINAL keeps half the shares for overruns, a stronger Taiwan dollar
   and a co-sponsor falling short. Keel's old research argued against earmarking that half for the building, so the
   store has almost nothing in support of Caplet's choice. Q5 must research it fairly (contingency practice in capital
   projects, P50/P90 budgets, reference classes) and the report follows the FINAL.
8. **Benchmarks for the facility contribution.** An all-Treasury plan leaves about $191,000 for the facility on the 4
   Nov curve (MODEL, `ips_rewrite/final_night/IDEA_LIST_MATHS.md`); the report should show what VT adds over that and
   what it risks, re-run on the 6 Nov curve.
9. **Wording traps in the locked texts.** TNA reflection 1 says "duration-matching" (a ladder matched payment by
   payment is also matched in duration, so this is true, but the report should call the ladder cash-flow matched);
   "pay what they say" against NAV (item 2); no fixed $150,000 minimum (TNA note 2: the payout "is not fixed").
10. **Writers' income in recessions:** the career argument opens the IPS and has almost no sources in the store
   (Q1, Q12).

## D. Coverage today (from the store's first pass)

Thin: Taiwan and the Taiwan dollar, the residency itself, the fundraising text, Laura's working life, how the team
learned, how the report presents itself (Q8-Q14 start from little). Dense: certainty, the ladder, co-sponsors and the
shares.
