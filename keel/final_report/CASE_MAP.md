# Case map: everything the Final Report must answer, and the research behind each (Sun 8 Nov 2026)

Book 15: "Every single part of our Final Report MUST be underpinned by a breathtaking level of research and
analysis." This page lists every requirement the case and Wharton place on the report, the questions (Q1-Q14 in
`README.md`) and store tags (`research/INSIGHT_STORE.md`) that feed it, and the analysis still open. Wharton's Final
Report instructions arrived on Mon 9 Nov and are section E. This is a planning
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
| Articulation of Competition Experience | Teamwork, communication, learning; research and decision process; growth and response to challenges | Q13; the team's real, dated record in `research/EXPERIENCE_RECORD.md`, told vividly; a scenario that helps is told as an illustration |
| Creativity and Presentation | A compelling, organised narrative in an authentic team voice; data used well; original thinking; the co-sponsor communication clear and credible | Q11, Q14; voice studies 1-3 |

## C. Open analysis found while gathering the old research (to settle before Thu 26 Nov)

1. **Reinvestment under Caplet's design: the largest open question.** *Settled Mon 9 Nov (`NUMBERS.md` section 2): the ladder as written falls short in 56% of historical rate stretches; Keel's call sizes the 2028 completion so all ten are paid even 3 points below today's forward rates (margin $21,149); the matched ladder halves the risk but buys only eight in January, against the IPS. Logged in `../pm/ASK_HUMANS.md`.* A ladder of coupon bonds costing about
   $300,000 delivers $50,000 a year only if its coupons are reinvested: a T-bond bought for about $30,000 reaches
   $50,000 in 2038 only with ten years of coupons reinvested on the way. So the payments depend on future Treasury
   rates as well as on default, and Caplet's FINAL has no rule for a shortfall (TNA note 1 names the risk). Wharton
   bars revising the strategy, so the report can measure, explain and implement within the IPS's words, but cannot add
   a new rule. Work to do: (a) size the risk on the 6 Nov curve under the FINAL design (old-design figures: about $21,000
   short if yields fall 2 points for good; and in Keel's two runs closest to the plan as written, with no margin for
   interest waiting to be reinvested, all ten payments were paid in full in only about 76% and 75% of base futures,
   the misses a few thousand dollars each; `research/harvest/H8_lab_window_plans.md`); (b) test the implementation the IPS's words allow: a cash-flow-matched ladder in
   Leibowitz's sense, where each later bond's coupons pay the earlier payments as they fall due, leaves only the
   2027-2032 coupons to reinvest. Keel's harvest brief flagged "later coupons paying earlier payments" as a clash; that
   was too strict, because the FINAL only says each Treasury matures "just before it's needed" and TNA note 2 says each
   payment "rests on a dedicated instrument", which stays true. Decide on Mon 16 with the numbers, log the call in
   `pm/ASK_HUMANS.md`, and show Caplet the reasoning in the 28 Nov draft; (c) the case's own order helps: the operating
   reserve is set aside in 2033 before the facility contribution, and Caplet's choice to fill the ladder with the 2028
   deposit's first dollars shows the same priority. (d) Lineage: Fisher and Weil, Redington, Leibowitz's dedicated
   portfolios, municipal escrows "sufficient without reinvestment", Damodaran's two conditions for a riskless asset.
2. **"Pay what they say" against "net asset value, not par".** *Settled Mon 9 Nov (`NUMBERS.md` section 3): each fund's payout can move by up to about 2% (its final months in cash); the floor's by up to 4.1%; the stated bottom is the modelled payout less 4.1%, rounded down to $5,000.* The FINAL says the Treasuries "pay what they say" and
   the bottom is promised "without doubt"; TNA note 2 says the iBond payout is a net asset value. The report must state
   the bottom in a way that is true for an iBond ETF (for example, rounded down from its expected payout) and say why
   the gap is small.
3. **The ladder's cost now.** *Settled Mon 9 Nov (`NUMBERS.md` section 1): $301,544 curve, $302,287 with the funds' fees.* On the 6 Nov close the ten payments cost $301,544 on 1 Jan 2027 (MODEL), so the 2028
   deposit's first dollars finish the ladder, exactly as the FINAL says. Old research that says "under $300,000" or
   "the 2028 deposit never funds payments" is out of date.
4. **The 7.5% figure** (A10): settled. J.P. Morgan, 2027 Long-Term Capital Market Assumptions, press release 19 Oct
   2026: "Global equities are projected to return 7.5% (USD), increasing from 7.0%." The matrix itself (compound or
   arithmetic) sits behind a login, so the report says "J.P. Morgan's estimate for global shares" and never "compound".
5. **The 2031 move:** *Settled Mon 9 Nov (`NUMBERS.md` section 4): after the move both ends are Treasuries maturing late 2032, so the stated range holds barring a default; the uncertainty is which range she can announce (top about $111,000 to $170,000 from today, 1 in 20 each side).* into which Treasury, when, and what the 2031 range then is. After the move both ends are owned;
   is the communicated range then floor to floor-plus-promised-half, with near-certain confidence, and what is the
   honest residual risk?
6. **A missed or smaller 2028 deposit** *Settled Mon 9 Nov (`NUMBERS.md` section 5): the payments are safe unless the deposit falls by more than about 98% (77% after a 1-point fall in yields first); a missed deposit leaves the 2033 payment about $3,000 short (longest rungs bought first) and no gift.* (one of the two reasons to change): what exactly changes, in order.
7. **Caplet's own use of the half kept back.** The FINAL keeps half the shares for overruns, a stronger Taiwan dollar
   and a co-sponsor falling short. Keel's old research argued against earmarking that half for the building, so the
   store has almost nothing in support of Caplet's choice. Q5 must research it fairly (contingency practice in capital
   projects, P50/P90 budgets, reference classes) and the report follows the FINAL.
8. **Benchmarks for the facility contribution.** *Settled Mon 9 Nov (`NUMBERS.md` section 4): all-Treasury $158,157 certain with Keel's margin; the FINAL's top is below it in 98% of paths because half of VT is kept back; counting the kept half, the FINAL leaves more in 63%.* An all-Treasury plan leaves about $191,000 for the facility on the 4
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

## E. What Wharton's Final Report instructions require (filed Mon 9 Nov; verbatim in `WHARTON_NORTH_STAR.md` section 0)

The instructions fix the report's shape. They rank above sections A-D where the two differ. Planning notes only.

**The shape and the budget.** Title page (1 page, Caplet's logistics), **Section 2 Portfolio Implementation** (2-3
pages), **Section 3 Integrated Recommendation and Reflection** (6-8 pages, the Team Reflection at its end), then a
separate References page (APA). 9-12 pages in all without References; 12-point Times New Roman, double-spaced, 1-inch
margins, page numbers bottom left, a PDF of 5 MB or less, no links the reader is meant to open; tables and graphics may
be single-spaced. A double-spaced page holds about 280-300 words, so a full-length report is about 2,700-2,900 words of
prose plus the holdings table and two or three exhibits: roughly 700 words for Section 2 and 2,000 for Section 3. The
store holds 1,771 ideas; perhaps sixty will be used. Keel's first page budget, for the skeleton (Day 3) to refine:

| Part | Pages | What it must do (Wharton's words in quotes) | Feeds from |
|---|---|---|---|
| 2. Portfolio Implementation | 3 | The table of every holding at cost on $300,000 (NUMBERS 8g); "how the portfolio's construction and allocation reflect your strategy"; "how diversification and risk considerations influenced your decisions"; "the intended roles of the most important holdings"; "how effectively the portfolio aligns with your IPS and Laura's financial goals" | A11; CANON; Q13 |
| 3a. The ten-year commitment and the operating reserve | 1.5 | "how your strategy supports the ten-year operating commitment"; "recommend an appropriate operating reserve" (case A1: size, initial composition, how it changes; A2: what high certainty means) | A1, A2, A7; NUMBERS 1-3, 8a, 8b, the reserve (NUMBERS 9) |
| 3b. The facility contribution and flexibility | 1.25 | "a responsible facility contribution while preserving financial flexibility" | A3, A4; NUMBERS 4, 5, 8c, 8f |
| 3c. The 2031 range and its confidence | 1.25 | "a credible dollar range"; "the level of confidence associated with that range and the factors that could affect it" | A5, A6; NUMBERS 4, 8e |
| 3d. Words for co-sponsors | 0.75 | "language Laura could use when communicating with prospective co-sponsors" | A8; Q4, Q11 cards |
| 3e. Assumptions, limits and what to watch | 1.25 | "important assumptions, uncertainties, and limitations"; "what Laura or her asset management team should monitor as 2031 and 2033 approach and how changing conditions could affect your recommendations" | A10, A12, A13; NUMBERS 7, 8d; CANON |
| 3f. Team Reflection | 1.5 | "how your team's research, collaboration, disagreements, decision-making, and learning influenced its final recommendation"; "the overall competition experience"; not the Trading Notes' analysis again | EXPERIENCE_RECORD; the blind ranking |

**New or sharper than before.**
1. **The holdings table** is a minimum requirement ("actual holdings"). Built tonight at cost (NUMBERS 8g); the WInS
   identifiers of four bonds come from Caplet's final export.
2. **Monitoring "as 2031 and 2033 approach"** is now required in its own right. It must agree with the IPS's "only 2
   possible reasons we would change our plan": Laura watches many things, and only a missed deposit or a Treasury default
   changes the plan. Everything else watched (yields in January 2028, VT before the 2031 move, the Taiwan dollar and
   building costs, co-sponsor budgets, each iBond fund's payout against par) changes a number, never a payment.
3. **Liquidity needs** are named in Client Knowledge: each payment's money is in hand when it falls due (a rung
   matures just before each payment), and the kept half is a daily-traded fund.
4. **"WInS gains and losses are not treated as evidence of the quality of the strategy."** The report never cites the
   WInS return (+1.85% on 23 Oct) as evidence.
5. **"Without repeating the content of your IPS or Trading Notes Analysis."** The report applies the IPS and evaluates
   it; it does not restate the letter. The Team Reflection may tell an event that a trade note recorded, but not its
   analysis; the blind re-rank on Mon 16 Nov scores against the instructions' own Articulation wording (now with
   "disagreement" and "uncertainty") and marks events that would repeat the Trading Notes.
6. **"The strategy established in your IPS should remain consistent ... not an opportunity to create a new strategy or
   revise the IPS."** Ray's coherence order (I99) is now Wharton's rule. Keel's calls that size what the IPS left open
   (the reinvestment margin, the floor and VT split) are applications of the IPS, and the report says so.
7. **Permitted investments apply to all long-term modelling.** Checked Mon 9 Nov: the numbers engine models only the
   frozen book's instruments (IBTM-IBTR, the five T-bonds, VT; IBTM again for the floor and the 2031 move). Figures from
   older scripts built on STRIPS or idealised zero-coupon bonds stay void (NUMBERS section 6).
8. **Exhibits are welcome** ("graphics should support the narrative"), but the page budget allows two or three beside
   the holdings table.
9. **APA references** on a separate page: every source carded from now on records the author, year, title and
   publisher it needs.

**Not expected** (Wharton): the facility's total cost, the funding gap, a construction budget or business plan,
Laura's taxes, the residency's legal or regulatory requirements. Unchanged from A13.
