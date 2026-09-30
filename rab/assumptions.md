# Key assumptions check: Root-and-Branch and the WInS book

WS0, 2026-09-30 (Sydney). Every load-bearing assumption, with a rating and the evidence behind it. AI-generated
planning material for Team Caplet; no deliverable text. Companion to `rab/premortem.md` (PM-xx ids).

**Errata, 30 Sep 2026 (Gate D, WS7-fixer).** The rows below were written before the Gate A lock and the later
memos. Where a row and this block disagree, this block wins; quote only `rab/numbers*.yaml` `quote_as` strings.
- **C2:** the model chance of a gap on 1 Jan 2027 is **about 1 in 3** (`ws4.gap_odds_2027` 0.3266, WS4 reconciled
  five methods). The 24.2% figure is superseded.
- **C3:** the Book L reinvestment figures are the locked `reinvest.bookL_delivered` (MODEL): about $503,000 at
  own yields, $479,000 two points lower, $466,000 at 2%, $447,000 at 0%, $507,000 at curve forwards. The example
  IPS wording "coupons reinvested in Treasury bills" contradicts adopted stress rule 2 (`D_stress_bad_year.md`:
  coupons buy a Treasury for the same payment, not bills; bills leave about twice the exposure after 2031, WS7
  kac-3, UNVERIFIED). Use "coupons reinvested in Treasuries for the same payment".
- **C9:** **Solid (STRIPS basis; reproduced).** WS1 reproduced all three claims: 2020 median $458,828
  (`history.cost_2020_median`), every daily curve since 2000 (6,688 days, `history.days_priced_since_2000`), and
  the cheapest since 28 May 2002 (`history.cheapest_since`).
- **E3:** **Caveated.** Under the adopted rule 3 (`D_stress_bad_year.md`, D6 decision 2, not yet ratified), a coupon
  shortfall is paid first from the half of the stock fund Laura keeps, so a small part of the payments can depend on
  equities (D6 says it "qualifies E3").
- **W3:** the locked Portfolio book costs $294,764.50 with $200 commission and leaves $5,235.50
  (`wins.portfolio.cost_close_0928`); a parallel fall of 27.6bp uses the cash up (`wins.portfolio.cash_margin`).
- **R14:** the Week-One email and Trading Details page are now read on Thursday 1 Oct, before the vote
  (`rab/trades/friday_checklist.md`). The rating stays Unsupported until they are read.
- **W1/W2:** the two-sided comparison for the 1 Oct vote is `rab/decisions/D7_wins_book.md`.

**Ratings.**
- **Solid:** primary evidence, unlikely to be wrong.
- **Caveated:** true, but only within limits that outputs must state.
- **Unsupported:** no evidence found; nobody asserts it until it is verified.

**Triage** applies where an assumption strains the IPS (RUN_PLAN s0). It is one of: fix-before-6-Nov /
note-in-Final-Report / ignore. The strategy itself is never changed. "IPS" means the IPS Google Doc
`1qtEuzXq_QYdQ9VJlusPY9km2l80E1hkk8FPR0iw71-w` as read on 30 Sep. It is headed "EXEMPLAR ONLY. NOT FOR SUBMISSION"
and the team writes its own.

**Evidence keys:**
- *Case* = `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` (page numbers).
- *Guide*, *TN guide*, *IPS guide* = the official PDFs in the same folder.
- *FAQ* = https://wghsinvcomp.smapply.us/res/p/faqs/ (fetched 30 Sep 2026).
- *Sheet* = `1EHCJxbFI0UOzNOpOWvDfzNqbK45qWuopZcL7HNN3VPM`, tabs named (read 30 Sep).
- *D1* = `research/insight_v1/verification/ladder_2026-09-28/D1_rerun_output_2026-09-28.txt`.
- *[n]* = output section of `rab/premortem_checks.py`: a WS0 rough check, not a headline number.

---

## 1. Laura and the case

| # | Assumption | Rating | Evidence and limits |
|---|---|---|---|
| L1 | $300,000 arrives at the start of 2027 and $150,000 at the start of 2028; nothing else goes in or out before 2033 | Solid | Case p2. A missing or late 2028 deposit is not in the case. It is a stress test only (D1 [8]: with a 100bp rally and no deposit, $28,753 of the 2033 payment is unfunded). |
| L2 | Ten fixed nominal $50,000 payments, one at the start of each year 2033-2042, not inflation-adjusted | Solid | Case p3. |
| L3 | The payments must be funded "with a high degree of certainty", with no outside money | Solid | Case p3. What counts as "high" is ours to define and defend (L4). |
| L4 | High certainty = each payment backed by a dated Treasury holding that ends before it (the IPS definition) | Caveated | The case asks teams to "define" high certainty and "explain how they evaluated" it (p3). The definition holds for principal. It leans on reinvesting coupons (C3) and on U.S. credit (C4). The evaluation still has to be shown: cost against budget, rate paths, reinvestment stress. |
| L5 | The operating reserve in 2033 is simply the ladder bought in 2027, shrinking as holdings pay out | Solid | Case p3 asks for the reserve's size, initial composition and how it changes. The ladder answers all three. Its 2033 market value is the "size". |
| L6 | No living-cost or liquidity needs before 2033 | Solid | Case p2. |
| L7 | Laura's tolerance is below average for the payments and above average for facility money above the floor | Caveated | Our inference from case p2 ("willing to take thoughtful risks", "appropriate balance") and p3 (credibility with co-sponsors). Reasonable, but state it as the team's reading. |
| L8 | No preset facility amount; flexibility matters; no contingency fund needs to be sized | Solid | Case p3. |
| L9 | A floor-based range is what co-sponsors will find credible | Caveated | The case supports the direction: overpromising damages credibility, so give a range (p3). No evidence on how co-sponsors weigh a floor against a wider range. |
| L10 | Amounts are U.S. dollars | Caveated | The case writes "$" and never names a currency (insight_v1 M130). The facility costs are in Taiwan, so the contribution carries NT$ risk, left unhedged because derivatives are excluded under the safe rule reading (R1). Triage: **note-in-Final-Report**. |
| L11 | Taxes, Taiwan legal setup and facility cost are out of scope | Solid | Case p4. |
| L12 | WInS gains and losses stay out of Laura's projections | Solid | Guide p4; FAQ ("not applied to the client's long-term portfolio projections"). |
| L13 | The case pull quote can be used as Laura's words | Unsupported | insight_v1 D13a: not verifiable as hers. No Laura quotes in notes. |

## 2. Rule readings

| # | Assumption | Rating | Evidence and limits |
|---|---|---|---|
| R1 | **"Investments permitted (for BOTH contributions)"** (FAQ) limits Laura's real plan, not just WInS, to: stocks priced $5 or more, ETFs available on WInS, and government/Treasury bonds available on WInS; no derivatives | Caveated | The heading is on the live FAQ (30 Sep). Reading (a): "both contributions" means Laura's 2027 and 2028 money, so the real plan is limited too. Reading (b): recycled text. insight_v1 cited the FAQ's "10 weeks of trading" as a leftover, but the competition runs about 10 weeks (28 Sep to 4 Dec), so that evidence is weak and reading (a) is the more natural one. Root-and-Branch complies under both readings *only if* its real instruments are WInS-listed: iBonds ETFs, WInS Treasuries, VT, SGOV for cash. Under (a) the plan cannot use STRIPS (not seen on the WInS list; UNVERIFIED), NT$ forwards, annuities or TIPS bonds not on WInS. The main cost of (a) is coupon reinvestment risk (C3). Adopt (a). Triage: **note-in-Final-Report** (state the reading). An optional Contact Us question is for the team to send (RUN_PLAN s9). |
| R2 | Trading ends and the book freezes on 6 Nov 2026 at 4pm ET (Sat 7 Nov, 8am AEDT) | Solid | Session Rules (tab `WInS Notes`); Guide. |
| R3 | $300,000 cash; 0% interest on cash; no fractional shares; minimum buy price $3 (Session Rules) against $5 (FAQ, for stocks) | Solid | Tab `WInS Notes`; FAQ. Use the stricter $5. Every planned ETF is above $20. |
| R4 | Commission $25 per stock or ETF trade and $10 per Treasury trade, charged only when a trade clears | Solid | FAQ; tab `WInS Notes`. |
| R5 | At most 200 trades; open and cancelled orders do not count | Solid | Tab `WInS Notes`. |
| R6 | Order size limit | Caveated | The Guide says at most 2x daily volume. The WInS Portfolio FAQ says at most half of the security's market volume, with larger orders waiting (tab `WInS Notes`). Apply the stricter. Planned sizes are 0.6-3.0% of 20-day median volume [3]. The binding risk is timing at the open (PM-05). |
| R7 | Position limits: 200% per ETF, 100% per bond and for all bonds | Solid | Session Rules, seen 29 Sep. |
| R8 | Bonds are U.S. Treasuries only | Solid | Session Rules. The FAQ says "any exchange", and the WInS bond page shows UK/DE/FR/NL. Use the stricter rule. |
| R9 | The note box takes 300 characters | Solid | maxlength seen 29 Sep. Whether a saved note can be edited is **unsupported** (not seen). A note can be added later from Order History (tab `WInS Notes`). |
| R10 | WInS offers limit orders | Unsupported | Not seen. A Friday checklist item (RUN_PLAN s7, s8). |
| R11 | A bond quantity is entered as face value in dollars, in lots of $1,000 | Unsupported | Assumed by the Trade Log header and Book L. Never seen in Preview. PM-02 stop rule. |
| R12 | Bond fills use a price set once a day | Caveated | FAQ: prices "updated once daily at U.S. market open". Tab `WInS Notes`: "Bonds fill at end-of-day prices". Two prices were stale on 29 Sep. Yield-check every bond before ordering (PM-04). |
| R13 | No day trading; mistakes are not "fixed" the same day | Solid | Session Rules; FAQ ("run with it"). |
| R14 | A one-day buy-and-hold book meets the "required trading activity and portfolio management guidelines" | Unsupported | FAQ, 30 Sep: the requirement exists but is undefined. The Week-One email is unread. Triage: resolve **before Friday's trades** (PM-10). This is not an IPS contradiction. |
| R15 | TN Analysis: 3 notes from executed trades, quoted exactly, reflections of 100 words or fewer; the holdings need not still be held | Solid | TN guide. |
| R16 | The strategy locks at the IPS; the Final Report evaluates implementation and may not redesign | Solid | IPS guide p2. |
| R17 | AI work must be cited and not submitted as the students' own | Solid | Wharton AI policy (insight_v1 R-W46/R-W49, VP). This applies to exemplar notes (PM-13). |
| R18 | All three deliverables are scored | Caveated | SMApply says all three "are evaluated". The Rules page names the IPS and Final Report for Top-50 selection (insight_v1 R-AN41). Treat all three as scored. |

## 3. Yields and the ladder (the root)

| # | Assumption | Rating | Evidence and limits |
|---|---|---|---|
| C1 | The ten payments cost about $289k today and about $292k forward to 1 Jan 2027, on the 28 Sep par curve | Solid as a model; caveated as a price | Two independent zero-coupon pricings agree within $204, and the gap is explained by day count plus the short-end nodes (commit 84e7010, `reconcile.py`). Book L at WInS prices: $292,226 including rounding (tab `Book L`). These are model values for zero-coupon bonds, not the cost of the instruments actually bought (C3). They are not the January purchase price either. Quote as "about $290k" (PM-24). |
| C2 | The deposit covers the ladder in January 2027 | Caveated | Headroom is about 26-27bp of yields. Model chance of a gap on 1 Jan 2027: 24.2% (D1 [6]: zero drift, lognormal, 2026 realised volatility 7.17% a year, thin tails). Older text says "about 1 in 3" (PM-32; WS4 reconciles). The design handles a gap: longest payments first, then the 2028 deposit completes the rest (D1 [3]). The cost of a gap falls on the floor and the growth fund, not on the payments. |
| C3 | **Dated holdings need "no rebalancing" and, once bought, depend only on the U.S. government** (IPS: "This cash-flow matching, unlike immunization, needs no rebalancing") | **Caveated: material** | True for principal. False for coupons. The instruments available in WInS (and, under R1, in the real plan) are coupon Treasuries and iBond ETFs paying monthly income, and their value to each payment date assumes the income is reinvested near today's yields. WS0 rough check on Book L [2] (assumptions: iBonds as 4% bullets, flat rates). The ten holdings deliver about $505k if reinvested at their own yields (about 5.1-5.4%). About $483k if every reinvestment is 2pp lower. About $470k at 2%. About $453k at 0%. The target is $500k. insight_v1's "~$5k" (F-113) counted coupons only to 2033. Triage: **fix-before-6-Nov** (IPS wording, team's decision: e.g. "held to maturity, with coupons reinvested in Treasury bills") and **note-in-Final-Report** (M1's proper cash-flow schedule and the cost of a buffer). No strategy change. |
| C4 | U.S. Treasuries are the default-free anchor | Caveated | The market standard. But the U.S. is rated below AAA by all three agencies (Moody's Aa1, May 2025: insight_v1 SNIP, not re-checked), and debt-limit episodes recur. Say "backed by the U.S. government", never "risk-free" (PM-28). |
| C5 | iBond ETFs end on schedule and pay out about their net asset value | Caveated | iShares: an iBond ETF "does not seek to return any predetermined amount" (insight_v1 open_questions s3). Expense 0.07%; IBTR had about $34m in assets (insight_v1 S1). The small risks are an early closure or tracking drift. Hold to the end date, and never state "repays $X". |
| C6 | Each holding ends shortly before its payment | Caveated | iBonds end about 15 Dec, a couple of weeks before 1 Jan. The Treasury rungs end 15 Feb 2037 (about 10.5 months before the 2038 payment), 15 May 2038 (about 7.5 months early) and 15 Nov 2039-2041 (about 7 weeks early) (tab `Book L`). The gap sits in cash or bills; in WInS, cash earns 0%. The IPS's "just before" is loose for the 2037/2038 bonds. Triage: ignore (or one clause in the Final Report). |
| C7 | No WInS Treasury matures between Feb 2031 and Feb 2036, so iBonds carry 2033-2037 and the floor | Solid | WInS bond drop-down, 29 Sep (tab `WInS Notes`). |
| C8 | WInS bond prices are within about 25bp of curve yields, except the two stale ones | Caveated | Seen 29 Sep. Re-check on Friday (PM-04). |
| C9 | "About $460,000 at 2020 yields", "tested on every Treasury curve since 2000", "cheapest since 2002" | **Unsupported** | No committed script or output in either checkout (grep, 30 Sep). D1 [4] points the same way: only a 428bp parallel fall (10-year 0.89%) pushes the ladder past the whole 2028 deposit. WS1/WS3 must reproduce each claim from treasury.gov or FRED history. Triage: **fix-before-6-Nov** if not reproduced (IPS wording). UNVERIFIED everywhere until then. |
| C10 | If the deposit is short, buy the latest payments first | Solid | D1 [3]: when the gap waits a year and rates fall another 100bp, longest-first adds 5% to the gap's cost against 15% for nearest-first. IPS: "latest payments first". |
| C11 | The 2028 floor costs about the remaining deposit discounted at the January 2028 five-year yield | Caveated | The five-year rate is held at 4.98% (insight_v1, ASM). At 4.0% the growth fund is about $35k, not $40k (insight_v1 E4 [4], ASM). The floor equals whatever is left of the deposit after completing the ladder (IPS), so it is not always $150k. Outputs must define the floor that way. |
| C12 | The floor, held in IBTM, repays "the whole remainder" | Caveated | The size comes from a yield, and IBTM's end value is not predetermined (C5). Suggest announcing the floor rounded down (PM-25). Triage: **note-in-Final-Report**. |

## 4. The branch (equity) and the range

| # | Assumption | Rating | Evidence and limits |
|---|---|---|---|
| E1 | VT is expected to return about 7% a year over the long run | Caveated | JPM 2026 LTCMA, AC World: 7.00% compound, 16.78% volatility (data to 30 Sep 2025; `competition/official_market_data/`). That is one house view, a year old; the 2027 edition is due about October 2026. insight_v1 also used a Vanguard-like 5.08% (ASM). It moves only the top of the range, never the payments. |
| E2 | "Equities should outperform Treasuries over five years" (IPS) | Caveated | That is an expectation, not a reliable result. Past five-year windows where stocks trailed Treasuries exist (WS3/M5 to show which, with data). Triage: note-in-Final-Report; changing "should" to "are expected to" in the IPS is optional. |
| E3 | Payments never depend on equities | Solid, given C3 | By design: stocks are bought only with money left after the ladder and the floor. |
| E4 | Half of the fund goes to the gift and half is kept | Caveated | A judgement (insight_v1 D6 default "one half"), not derived. The D6 memo tests it (WS2). Any other share is a decision to ratify, never applied (PM-26). |
| E5 | The 2033 gift "cannot fall outside" the 2031 range | Solid by construction, under conditions | The bottom holds if the floor pays (C5, C12) and the 2028 deposit arrived (known before 2031). The top holds because the gift is capped. State the confidence with those conditions, plus where in the range the gift is likely to land (PM-25). |
| E6 | One global fund (VT) is the right branch | Caveated | Listed in WInS, with a 20-day median volume of about 2.0m shares [3]. VT against the alternatives is WS3's memo. |
| E7 | Nothing is traded between 2028 and 2033 | Solid (design); caveated (behaviour) | The IPS holds the fund to 2033. The risk is that Laura sells in a crash. A bad-year clause belongs in the IPS (insight_v1 E6 R6). |
| E8 | Inflation leaves the payments unchanged but raises facility costs | Solid / caveated | The payments are fixed nominal (case p3). Taiwan construction costs rose about 3.5% a year since 2021 and 6.53% year on year (repo CLAUDE.md, verified 27 Sep). The real value of the $50k payments falls; that belongs in the Final Report. |

## 5. The WInS book

| # | Assumption | Rating | Evidence and limits |
|---|---|---|---|
| W1 | The current book is the Sheet `Portfolio` tab: Laura's plan on 2 Jan 2028, scaled to $300k | Caveated | The tab says "Provisional until the team votes on 1 Oct 2026". D7 (Portfolio vs Book L) is open. Build for both (PM-09). |
| W2 | Judges will understand the scaling (VT and the floor on day one, although the 2028 money never reaches WInS) | Caveated | No rule covers it. The IPS has one sentence ("shows the allocation after both deposits, scaled down"). Notes must match it (PM-15, PM-17). |
| W3 | The planned units fit inside $300k | Caveated | At 28 Sep prices: $294,569 spent including commissions, $5,431 cash [1]. A yield fall of about 28bp uses the cash up unless units are re-sized (PM-03). |
| W4 | Planned orders are small relative to market volume | Solid (size); caveated (timing) | 0.6-3.0% of 20-day median volume, from yfinance with `auto_adjust=False`, 30 Sep [3]. See R6 on timing. |
| W5 | Tickers resolve to the intended funds | Caveated | IBTN = INSCORP Inc in WInS (seen). Longbridge has no IBTN.US record, so only WInS's own order screen confirms a name (PM-01). |
| W6 | Sheet prices are consistent between tabs | Caveated | Portfolio-tab bond prices are clean plus accrued; Book L shows them separately (the differences equal Book L's accrued column exactly). Ticket builders must not count accrued twice (PM-03). |
| W7 | IBTM carries two jobs: the 2033 payment and the floor | Solid | Portfolio tab: 32.5% = the ladder rung plus the 24.3% floor. Any note on IBTM must reflect both jobs, or give the split. |
| W8 | The frozen WInS book is what the Final Report evaluates as "implementation" | Solid | IPS guide p2; Guide p4. |

---

## What must be stated in outputs (the short list)

1. The reinvestment caveat on "dated holdings" (C3), with M1's numbers.
2. The rule reading adopted for "for BOTH contributions" and what it excludes (R1).
3. The 2031 confidence as "certain by construction if...", with the conditions (E5, C12).
4. The history claims only once reproduced (C9).
5. The January-2027 gap chance as one reconciled, dated number (C2).
6. Every UNVERIFIED WInS mechanic on the Friday checklist (R9-R12, R14).
