# Q17: Judging the implementation (Final Report Section 2, Portfolio Implementation)

Mon 9 Nov 2026 (Sydney). Notes for the Final Report store, not report prose.

**Wharton's ask (`../../WHARTON_NORTH_STAR.md` s.0):** Section 2 must "evaluate how effectively it implemented the
investment strategy established in your IPS": construction and allocation, diversification and risk, the roles of the
most important holdings, alignment with the IPS and Laura's goals; a holdings table at the original $300,000; WInS
gains are never evidence. The IPS and the Trading Notes Analysis are frozen; nothing here proposes a change.

**Claims tested**
1. The right way to judge this implementation is how professionals judge a dedicated (cash-flow-matched) portfolio
   against its policy: does each liability have an asset maturing before it, at what cost, with what residual risks?
2. The WInS book is Laura's whole plan in miniature, not her January 2027 purchase.
3. Implementation costs and frictions were small and chosen.
4. What the book could not show, and honest limits (which belong in Section 2, which in Section 3).
5. Diversification means different things in different parts of the book.

**Problem class.** An attestation problem, not a performance problem: verifying that a schedule of assets covers a
schedule of fixed liabilities (the municipal escrow verifier's and the insurance actuary's question), plus an
execution-cost problem for the build (implementation shortfall). Return-based tools (tracking error to an index,
Sharpe ratio, performance attribution) answer a different question and do not fit.

**Verdicts**
| Claim | Verdict | Why, in one line |
|---|---|---|
| 1 | CHANGE | Keep the dedicated-portfolio frame, but name the exact professional yardstick: the escrow verifier's two tests (Treasuries maturing on or before each payment; sufficient "without further reinvestment", Moody's 2020) plus rate scenarios as in NY Regulation 126, and Perold's implementation shortfall for the build. The book passes the date test 10 of 10; without reinvestment the instruments deliver 89.1% of the $500,000 as bought (NUMBERS 2), so "at what cost, with what residual risks" must be answered with the IPS's 2028 completion. Kill tracking error to an index, Sharpe ratio and attribution for Section 2. |
| 2 | KEEP, one precision | Verified: plan "(ii)R" = Laura's position after both deposits scaled by 300/450. At cost: ladder 65.3%, floor stand-in 24.3%, VT 8.84%, cash 1.61%; times 1.5 these add to $450,000. Rung coverage is 65.6-70.4% of a full rung (whole ladder 68.0%), not "67-72%": the 2040 rung sits slightly under scale because bonds trade in $1,000 lots. |
| 3 | CHANGE | True of execution: $200 commissions (0.07%), bonds bought within 9 basis points of the Treasury curve, ETF spreads 0.01-0.05%, 11 of 200 trades. But accrued interest is not a cost, and the frictions that matter for a bond ladder were not chosen: the yield level on purchase day (a $37,625 swing in the ladder's cost through 2026) and the instruments WInS allows (coupons to reinvest, NAV payouts). In WInS the timing was luck; for Laura the IPS's completion rule is the answer. |
| 4 | KEEP | Split given below: Section 2 says what the book shows and cannot show; Section 3 sizes the residual risks and the 2028 completion. |
| 5 | KEEP | Hedging part: one issuer by design, spread across ten dates; growth part: VT's breadth (10,185 stocks, index in over 47 countries); whole-wealth level: the bonds counterweight her career (IPS l.9). EDHEC's "diversification, hedging, insurance" gives the vocabulary. |

**Claim 4: where each limit goes**
| Limit | Section 2 (what the book shows or cannot show) | Section 3 (size, consequence, monitoring) |
|---|---|---|
| WInS cannot hold the 2028 deposit | Yes: explain the 300/450 scale once, with the table note | No |
| No WInS Treasury maturing Feb 2031-Feb 2036 | Yes: why five rungs are iBond ETFs (one line per instrument type) | No (the story belongs in the Team Reflection) |
| iBond ETFs pay net asset value, not par | One clause in the holdings' roles | Yes: up to about 2% per rung; the floor deduction of 4.1% (NUMBERS 3) in the confidence statement |
| Coupons must be reinvested | Yes: the honest measure (hedge ratio 78%; 89.1% without reinvestment) | Yes: the completion standard and its cost ($21,149, NUMBERS 2), and what to monitor |
| Ladder cost $301,544 at the freeze, above $300,000 | One line: the book was priced on 7 Oct ($288,510 for the full ten); WInS timing is not Laura's purchase date | Yes: the completion rule in January 2028 (NUMBERS 1, 5) |
| WInS cash earns 0%; Laura's waiting money sits in a short-term Treasury ETF | Table note | Assumption list |
| The 2031 move and the kept half | No (the book cannot show dates) | Yes |

**Inconsistencies flagged (for the owners of NUMBERS and CANON; none changes the strategy)**
- I1. CLAUDE.md and `keel/scripts/holdings_ladder.py` say the WInS positions hold "67-72% of each full rung". This
  card, on the register's engine at the 23 Oct curve, finds 65.6-70.4% (bonds on NUMBERS 1's 6 Nov faces: 65.4-70.2%).
  The Nov-2039 bond (2040 payment) is below the two-thirds scale: 18 units held, about 18.3 needed.
- I2. CANON C12 glosses the ladder as "Matched payment by payment, which also matches duration". NUMBERS 1 gives
  instrument duration 7.76 years against 9.94 for the payments ($234 against $300 per basis point). CANON should drop
  "which also matches duration"; the TNA's "duration-matching" (l.7) is explained as cash-flow matching.
- I3. NUMBERS 8g lumps $1,309.42 as "commissions and the interest accrued". It splits as $200 commissions plus
  $1,109.42 accrued interest. WInS's 15 Aug coupon date on the May-2038 bond (COMPETITION.md l.116) undercharged
  accrued interest by about $225.
- I4. CANON Table E and the snapshot give market-value weights (IBTM 32.5%, VT 8.6%); NUMBERS 8g gives cost weights
  (IBTM 32.50%, VT 8.84%). The Section 2 table uses 8g only and the text must not mix bases.
- I5. VT is 8.84% of the frozen book but 7.45% of the $450,000 in the plan with Keel's margin (NUMBERS 4: $33,515).
  The book was built before the margin (decided 9 Nov); Section 2 must not claim the frozen weights equal the plan
  with the margin.
- I6. CANON D17 keeps IBTO "among the first rungs completed in any top-up" (WN l.20); NUMBERS 1 says the part left
  unbought in January 2027 is the 2033 rung (IBTM). They agree only if read "earliest rungs first: IBTM, then IBTO";
  say it that way once.
- I7. `competition/COMPETITION.md` s.7 still describes an old design (floor "sized to return about $150k"; shortfall
  covered "first from the 2027 leftover, then Laura's half"). Void per NUMBERS 6 and CANON; never quote.

**Arithmetic behind this card (MODEL where marked; not yet in NUMBERS, so the register must adopt any figure before
the report uses it)**
- Holdings at cost: snapshot quantity times price paid, $295,176.79 (matches NUMBERS 8g). $300,000 less that, less
  WInS cash $3,513.79, leaves $1,309.42; less 6 x $25 + 5 x $10 = $200 leaves $1,109.42 of accrued interest.
- Accrued interest check: standard Treasury accrual (actual/actual, `indep_pricer.accrued`) on the five bonds,
  counted to 6 Oct with the May-2038 bond's last coupon set to 15 Aug as WInS shows it: $1,113.48 (correct dates:
  $1,338.48). The same method to 22 Oct gives $1,288.59 against WInS's $1,285.99 on 23 Oct.
- Bond prices against the curve: yield of each fill price (clean plus accrued, settlement 7 Oct) against the yield of
  the same bond priced on the treasury.gov par curve of 6 Oct and of 7 Oct (`daily-treasury-rates_2026-10.csv`,
  bootstrapped as in `indep_pricer.py`).
- Coverage: the register's engine (`numbers/engine.py`, design A, own-rung sizing at forward rates) re-run on the
  23 Oct curve with valuation date 23 Oct; it reproduces NUMBERS 8b's $297,636 (payments) and $298,367 (instruments)
  exactly. Fund rungs: shares x 23 Oct price, carried forward to 1 Jan 2027, over the full rung's fund dollars
  (IBTM rung lot 1,142 shares, team record). Bond rungs: WInS face over the full rung's face.

**Sources read (APA elements; web pages read Mon 9 Nov 2026 unless marked)**
- S1 Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *The Journal of Portfolio
  Management, 14*(3), 4-9. https://doi.org/10.3905/jpm.1988.409150. Reprinted in P. L. Bernstein & F. J. Fabozzi
  (Eds.), *Streetwise* (pp. 106-111). Princeton University Press, 1998. Citation read on hbs.edu (faculty item 2083)
  and pm-research.com; wording from the reprint's excerpts on degruyterbrill.com (full text paywalled).
- S2 Russell Investments. (2014, September). *Transition management explained* [Brochure].
  https://russellinvestments.com/-/media/files/nz/insights/transition-management-explained.pdf; US edition (2026):
  https://russellinvestments.com/-/media/files/us/insights/institutions/implementation/transition-management-explained.pdf
- S3 Meketa Investment Group. (2026, March). *Transition management update*.
  https://meketa.com/wp-content/uploads/2026/03/MEKETA_Transition-Management-Update.pdf
- S4 Financial Conduct Authority. (2014, February). *Transition management review* (Thematic Review TR14/1).
  https://www.fca.org.uk/publication/thematic-reviews/tr14-01.pdf
- S5 Leibowitz, M. L. (1986). The dedicated bond portfolio in pension funds, Part I: Motivations and basics.
  *Financial Analysts Journal, 42*(1), 68-75. https://doi.org/10.2469/faj.v42.n1.68 (abstract page, CFA RPC)
- S6 Leibowitz, M. L. (1986). The dedicated bond portfolio in pension funds, Part II: Immunization, horizon matching
  and contingent procedures. *Financial Analysts Journal, 42*(2). https://doi.org/10.2469/faj.v42.n2.47 (abstract page)
- S7 Symmetric cash matching. (1990). *Financial Analysts Journal, 46*(5). https://doi.org/10.2469/faj.v46.n5.46
  (abstract page; author not shown on the page read)
- S8 Ryan, R. J. (2013). *The evolution of asset/liability management (a summary)*. Research Foundation of CFA
  Institute. https://rpc.cfainstitute.org/sites/default/files/-/media/documents/book/rf-lit-review/2013/rflr-v8-n2-1-sum.pdf
- S9 Leibowitz, M. L. (1987). *A new perspective on asset allocation*. Research Foundation of the Institute of
  Chartered Financial Analysts. https://rpc.cfainstitute.org/sites/default/files/-/media/documents/book/rf-publication/1987/rf-v1987-n1-4469-pdf.pdf
- S10 Government Finance Officers Association. (2019, March 8). *Refunding municipal bonds* [Best practice].
  https://www.gfoa.org/materials/refunding-municipal-bonds
- S11 National Association of Bond Lawyers. (2023). *Verification agent*; *Verification report* [Bond basics].
  https://www.nabl.org/bond-basics/verification-agent; https://www.nabl.org/bond-basics/verification-report
- S12 Moody's Investors Service. (2020, July 15). *Rating methodology: Pre-refunded and escrow-backed transactions*.
  https://ratings.moodys.com/api/rmc-documents/68216 (excerpts)
- S13 City of Austin. (2024). *Escrow agreement, public improvement and refunding bonds, Series 2024* (s.4.02); and
  *Water and wastewater system revenue refunding bonds, Series 2024* (s.3.03).
  https://services.austintexas.gov/edims/document.cfm?id=434512; id=427345
- S14 Actuarial Standards Board. (2021). *Actuarial Standard of Practice No. 22: Statements of actuarial opinion
  based on asset adequacy analysis for life insurance, annuity, or health insurance reserves and other liabilities*
  (Doc. No. 203). http://www.actuarialstandardsboard.org/wp-content/uploads/2021/11/asop022_203.pdf
- S15 N.Y. Comp. Codes R. & Regs. tit. 11, § 95.10(d) (Regulation 126, required interest scenarios).
  https://www.law.cornell.edu/regulations/new-york/11-NYCRR-95.10
- S16 Vanguard. (2022). *Revisiting pension asset allocation*.
  https://workplace.vanguard.com/content/dam/inst/iig-transformation/insights/pdf/revisiting-pension-asset-allocation.PDF
- S17 BofA Securities. (2025). *Next-generation liability-driven investing*.
  https://business.bofa.com/content/dam/flagship/workplace-benefits/id20_0905/documents/00-63-1983NSB.pdf
- S18 CFA Institute. (2026). *Liability-driven and index-based strategies* [Refresher reading summary].
  https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/liability-driven-index-based-strategies
- S19 The Pensions Regulator. (n.d.). *Liability hedging* [Help file].
  https://helpfiles.thepensionsregulator.gov.uk/members/dbliabilityhedgingamend
- S20 Abaris Holding Limited Pension Scheme. (2023, October). *Statement of investment principles*.
  https://www.mypension.com/media/3pkpjklt/abaris-db-section-statement-of-investment-principles.pdf
- S21 CFA Institute. (2010). *Elements of an investment policy statement for institutional investors*.
  https://doi.org/10.2469/ccb.v2010.n13.1 (PDF on rpc.cfainstitute.org)
- S22 Maginn, J. L., Tuttle, D. L., McLeavey, D. W., & Pinto, J. E. (2018). *The portfolio management process and
  the investment policy statement* [Refresher reading]. CFA Institute.
  https://www.cfainstitute.org/sites/default/files/-/media/documents/article/refresher-readings-free/rr-2018-l2v6r47.pdf
- S23 CFA Institute. (2025). *Overview of fixed-income portfolio management* [Refresher reading summary].
  https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2025/overview-fixed-income-portfolio-management;
  2017 reading excerpt: https://catalogimages.wiley.com/images/db/pdf/9781946442918.excerpt.pdf
- S24 EDHEC-Risk Institute (now EDHEC Climate Institute). (n.d.). *How factor investing can help liability-driven
  investors*; *Multi-asset products and solutions*. https://climateinstitute.edhec.edu/how-factor-investing-can-help-liability-driven-investors;
  https://climateinstitute.edhec.edu/multi-asset-products-and-solutions
- S25 Martellini, L., & Milhau, V. (2021). *Diversification and insurance: Which should come first?* EDHEC-Risk
  Institute. https://climateinstitute.edhec.edu/diversification-and-insurance-which-should-come-first
- S26 PwC. (2026, October 7). *Loans and investments guide*, 3.4 Accounting for debt securities [Viewpoint].
  https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/loans_and_investment/loans_and_investment_US/chapter_3_accounting__1_US/34_accounting_for_de_US.html
- S27 Certain personal injury liability assignments, 26 U.S.C. § 130 (2024).
  https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIII-sec130.htm
- S28 Markowitz, H. (1952). Portfolio selection. *The Journal of Finance, 7*(1), 77-91.
  https://doi.org/10.1111/j.1540-6261.1952.tb01525.x (JSTOR copy read)
- S29 Vanguard. (2026). *Vanguard Total World Stock ETF (VT)* [Fact sheet as of September 30, 2026; product page].
  https://fund-docs.vanguard.com/F3141.pdf; https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etf
- S30 BlackRock. (2026). *iShares iBonds Dec 2032 Term Treasury ETF (IBTM)* [Product page, data as of October 27,
  2026]. https://www.ishares.com/us/products/328944/ishares-ibonds-dec-2032-term-treasury-etf
- S31 U.S. Department of the Treasury. (2026). *Daily Treasury par yield curve rates* [CSV, October 2026; 23 Oct;
  6 Nov]. Repo copies in `competition/official_market_data/`.
- Repo sources: SNAP = `competition/wins/2026-10-23_snapshot.md`; NUMBERS = `keel/final_report/NUMBERS.md`; CANON =
  `keel/final_report/CANON.md`; team sheet = `caplet/google_drive/sheets/portfolio_and_trading_notes/`.

## Proposed evaluation measures (notes)

| Measure | Value | Source | Why a judge would care |
|---|---|---|---|
| Payments with a dedicated Treasury holding that ends on or before them | 10 of 10. Gaps: 17 days for the five iBond ETFs (end "on or about" 15 Dec), 47 days for the Nov-2039/40/41 bonds, 231 days (May-2038), 320 days (Feb-2037) | SNAP l.22-31; CANON B8; S30 | It is the escrow verifier's first test (S12: maturities "on or prior to" each payment date) and the IPS's own words ("each maturing just before it's needed") |
| Promised money held in shares | $0. Treasuries $268,652.18 = 89.55% of the $300,000 at cost (iBond ETFs 61.28%, bonds 28.27%); VT 8.84%, standing only for money not yet promised; cash 1.61% | NUMBERS 8g; IPS l.11 | Direct evidence that the IPS's central rule held in the build: alignment with the IPS, which Wharton names |
| Fidelity to the plan at two-thirds scale | Each rung 65.6-70.4% of a full $50,000 rung (target 66.7%); whole ladder 68.0%; IBTM split 1,142 rung and 3,361 floor shares; floor 73.3% of floor plus VT | This card (MODEL, register engine at 23 Oct curve; for NUMBERS to adopt); trading_notes.csv l.63; NUMBERS 0 | Construction and allocation judged against Caplet's own policy portfolio (S21), not an index; it also shows the one small flaw (2040 rung, lot rounding) |
| Cost of carrying out the build | $200 commissions (0.07% of $300,000); five bonds bought 2.6-8.8 basis points from the Treasury curve, all inside the team's 25-basis-point rule, together $56-$192 below curve value; ETF median spreads 0.01-0.05% (about $47 for half the spread); 11 of 200 trades, none after 8 Oct | SNAP; COMPETITION s.4; this card; S29, S30 | Perold's implementation shortfall (S1): almost nothing was lost between the decision and the book; the discipline (limit orders, yield check, hold rule) shows |
| What the ladder delivers under the strictest test | Without any reinvestment: $445,405 of $500,000 (89.1%); per rung 84.7% (2041) to 96.6% (2033); rate hedge ratio $234 / $300 per basis point = 78%. With Keel's margin from the 2028 deposit: all ten paid in 94% of 16-year windows since 1962 | NUMBERS 1, 2, 8a | The honest limit, in a professional's units. It shows where "pay what they say" is weakest and how the IPS's completion rule closes it, without redesign |

## The card

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Implementation shortfall: the real portfolio's result minus a "paper" portfolio bought instantly at decision prices at no cost; two parts, "execution cost" and "opportunity cost" | S1 Perold (1988) | PROCESS | KNOWN | Section 2 can treat the IPS's ten rungs, floor and VT at decision prices as the paper book and the WInS fills as the real one | Built for active stock trading over days; for a six-year hold the opportunity cost is the yield level on purchase day, and Laura's purchase day is January 2027, not the WInS dates | VERIFIED: citation (hbs.edu, pm-research DOI record); wording from the reprint's excerpts; full text not read | no | hbs.edu faculty item 2083; degruyterbrill.com doi 10.1515/9781400829408-014 (read 9 Nov 2026) |
| 2 | Implementation shortfall is the "generally accepted industry standard for measuring the cost of a transition" (T-Standard, Russell, 2003): brokerage, spread, impact and opportunity cost against the new portfolio "built on the day before ... at zero cost" | S2 Russell (2014; 2026 US ed.); S3 Meketa (2026) | PROCESS | KNOWN | The WInS build was a transition from $300,000 cash to a target book in 11 trades; Section 2 can report it the way a transition report does | Transitions run over days with a clean start price; the team's tickets were set on 28 Sep prices and refreshed before 6-7 Oct, so the "day before" baseline is loose | VERIFIED (Russell glossary; Meketa) | no | russellinvestments.com NZ PDF glossary, US PDF 2026; meketa.com 2026-03 (read 9 Nov 2026) |
| 3 | "For bonds, interest rate volatility typically represents the biggest part of implementation shortfall" | S2 Russell (2014, p.20) | PROCESS, LADDER | NICHE | The full ladder's cost moved $37,625 through 2026 ($287,938 on 5 Oct to $325,563 on 27 Feb, NUMBERS 8b): 12.5% of $300,000 and 188 times the $200 of commissions. The yield level, not execution, sets the cost | The 7-8 Oct fills landed within $572 of the year's cheapest close: luck, as NUMBERS 8b says, and not Laura's purchase date | VERIFIED (Russell); figures NUMBERS 8b | Risk: telling the fill timing as skill or gain breaches Wharton's "Do not focus on portfolio performance" | russellinvestments.com NZ PDF p.20; NUMBERS 8b |
| 4 | Best practice is a pre-trade estimate and a post-trade report that explains differences; the FCA calls pre- and post-implementation reports "an important element" of transparency | S2 Russell; S4 FCA (2014) | PROCESS | KNOWN | The team's order tickets (2 Oct) carried, per order, an expected cost, a do-not-pay-above price and a cash-after check; the fills are the post-trade side (IBTM planned 4,486 shares, filled 4,503) | Tickets were re-sized on later prices by plan, so planned and filled quantities differ for a known reason, not slippage | VERIFIED (FCA TR14/1 p.9; Russell stages); team tickets in repo | no | fca.org.uk TR14/1; rb_tickets.csv l.9-20 |
| 5 | Cash matching ("dedication") gives coupons and principal that match a liability schedule; often the aim is to "assure fulfillment even under totally passive management", that is, "no reinvestment"; a least-risk asset for nominal-dollar liabilities | S5 Leibowitz (1986a) | LADDER, CERTAINTY | KNOWN | The professional name for Caplet's ladder; the yardstick is coverage of each payment, not return | Leibowitz's strict standard is no reinvestment; as bought, 3-15% of each payment is interest on interest (NUMBERS 8a) | VERIFIED (CFA RPC abstract) | Risk: IPS "pay what they say" holds for the cash flows, not the reinvested part (CANON C2, C17); explain, never retract | rpc.cfainstitute.org FAJ 1986 v42 n1 (read 9 Nov 2026) |
| 6 | Immunization (duration matching) "requires portfolio changes over time"; cash matching "utilizes cash flows on or before a liability date to meet each liability" and needs none | S6 Leibowitz (1986b); S7 FAJ (1990) | LADDER | TEXTBOOK | Names Caplet's ladder correctly: cash-flow matched, held to the end, never rebalanced (IPS l.13) | The TNA calls it "duration-matching"; NUMBERS 1 shows the durations differ (7.76 against 9.94 years) | VERIFIED (CFA RPC abstracts) | Yes, wording: TNA l.7 "duration-matching" (CANON C12; I2) | rpc.cfainstitute.org FAJ 1986 v42 n2; FAJ 1990 v46 n5 |
| 7 | Municipal escrow verification: a CPA "verification agent" independently confirms that escrow investments "will be sufficient to fund the debt service payments" up to each redemption date | S10 GFOA (2019); S11 NABL (2023) | CERTAINTY, LADDER | NICHE | The closest real twin of Laura's ten payments: a fixed schedule paid in advance with Treasuries; Section 2 can apply the verifier's test to the book | Escrows choose any Treasury (often SLGS made to measure); Laura is limited to WInS-listed instruments | VERIFIED (GFOA best practice; NABL glossary) | no | gfoa.org/materials/refunding-municipal-bonds; nabl.org bond-basics (read 9 Nov 2026) |
| 8 | Moody's two tests: escrow cash flows "sufficient, without further reinvestment, to pay the debt service ... in full and on time"; securities with "scheduled maturities on or prior to dates on which any debt service payment ... becomes due" | S12 Moody's (2020) | CERTAINTY, LADDER | NICHE | Date test: 10 of 10 pass. Sufficiency without reinvestment: $445,405 of $500,000 (89.1%) as bought; 95.6% with Keel's margin (NUMBERS 2) | By this standard the ladder as bought is not escrow-grade; it relies on reinvesting coupons at forward rates (NUMBERS 8a break-even 5.12%) | VERIFIED (Moody's methodology excerpts, 15 Jul 2020) | Risk: IPS "immune to markets", TNA "near-ironclad guarantee"; the true meanings are CANON C1, C13 | ratings.moodys.com/api/rmc-documents/68216 |
| 9 | Escrow agreements reinvest spare cash only in SLGS "with an interest rate equal to zero percent (0%)" and state sufficiency "without further reinvestment" | S13 City of Austin (2024) | CERTAINTY | NICHE | NUMBERS 2's "interest earns nothing" test is the market's own conservative convention, so the report can call it the strictest case with a real precedent | Escrows are legally irrevocable and deliberately over-funded; Laura's plan is not a legal defeasance | VERIFIED (agreement PDFs) | no | services.austintexas.gov id 434512 s.4.02; id 427345 s.3.03 |
| 10 | A certain match needs zero-coupon bonds; before Treasury STRIPS (1985) coupon-bond dedication could not be a guaranteed match "because of reinvestment risk" | S8 Ryan (2013) | LADDER, CERTAINTY | NICHE | Wharton's ban on individual STRIPS puts Caplet where dedication stood before 1985: the reinvestment risk is the price of the rules, not a design slip | Zeros would still leave the gap between maturity and payment; iBond ETFs add NAV risk that zeros would not | VERIFIED (Research Foundation summary PDF) | no (TNA l.5 already names reinvestment-rate risk) | rpc.cfainstitute.org rflr-v8-n2-1-sum.pdf |
| 11 | Dedication's listed advantages: predictable cash flows when held to maturity; reduced market, reinvestment, inflation, default and liquidity risk; asset flows matched to liability flows; 100% bonds; passive, low fees | S8 Ryan (2013) | LADDER | TEXTBOOK | A checklist Section 2 can tick: held, matched, all Treasuries, 0.07% fund fee, no trade after 8 Oct | "Reinvestment risk reduced" is true only with zeros or no-reinvestment sizing (row 8) | VERIFIED | no | rpc.cfainstitute.org rf-lit-review 2013 PDF |
| 12 | Cash flow testing: "The projection and comparison of the timing and amount of cash flows under one or more scenarios in order to evaluate cash flow risks" | S14 ASB (2021) | CERTAINTY, PROCESS | NICHE | NUMBERS 2's tests (falls of 1-3 points, 0%, 585 history windows) are a cash flow test in the actuary's sense; one line in Section 2 | Insurers test many uncertain liabilities; Laura's ten are fixed, so the test is simpler | VERIFIED (ASOP 22 definitions 2.4-2.5) | no | actuarialstandardsboard.org ASOP 22 (read 9 Nov 2026) |
| 13 | New York Regulation 126 requires seven rate scenarios, including "an immediate decrease of three percent and then level" and "uniformly decreasing over 10 years at a half percent (0.5%) per year" | S15 11 NYCRR 95.10(d) | CERTAINTY | NICHE | Keel's margin is sized for rates 3 points lower for good (NUMBERS 2), the regulator's scenario (vii); with it that scenario's shortfall is $0 | The rule also tests rises and floors falls at half the starting 5-year yield; Laura's ladder is hurt only by falls | VERIFIED (Cornell LII text) | Risk: the margin is a recommendation for the 2028 completion, not in the frozen book (row 28, I5) | law.cornell.edu 11-NYCRR-95.10 |
| 14 | LDI interest-rate hedge ratio = dollar duration of hedging assets divided by dollar duration of liabilities ("the portion of liability risk due to fluctuating interest rates that is expected to be offset") | S16 Vanguard (2022); S17 BofA (2025); S18 CFA (2026) | LADDER | KNOWN | Caplet's ladder: $234 / $300 per basis point = 78% (NUMBERS 1), while cash-flow coverage at forward rates is 100%; the 22% is coupons arriving early | Hedge ratio measures value sensitivity today; Laura needs cash on dates; report both | VERIFIED (three sources) | Yes: TNA l.7 "duration-matching" is not literally true at 78%; CANON C12 gloss conflicts with NUMBERS 1 (I2) | workplace.vanguard.com PDF; business.bofa.com 00-63-1983NSB.pdf; cfainstitute.org 2026 reading |
| 15 | UK pension schemes report PV01 (value change for a 0.01% move in rates) and set hedge ranges, e.g. PV01 85-130% of liability exposure in one scheme's statement of investment principles | S19 TPR (n.d.); S20 Abaris (2023) | LADDER | NICHE | Shows professionals manage hedging as a measured ratio with a band; Caplet's band is implicit (complete in January 2028) | Leveraged LDI (the 2022 gilt stress) is unlike Laura's unleveraged ladder; borrow the measure only | VERIFIED | no | helpfiles.thepensionsregulator.gov.uk; mypension.com Abaris SIP |
| 16 | The IPS "serves as a strategic guide in the planning and implementation of an investment program"; define "a policy portfolio to serve as a basis for performance and risk assessments" | S21 CFA Institute (2010) | PROCESS | KNOWN | Section 2's benchmark is Caplet's own policy portfolio (ten rungs, floor, VT), which is exactly Wharton's "alignment with your IPS" | CFA pairs the policy portfolio with an index per asset class; for a liability-matched book the benchmark is the liability (rows 18-19) | VERIFIED (CFA PDF) | no | rpc.cfainstitute.org position paper PDF (read 9 Nov 2026) |
| 17 | Performance evaluation assesses "progress toward the achievement of investment objectives as well as ... portfolio management skill" | S22 Maginn et al. (2018) | PROCESS | TEXTBOOK | For Laura the objective is payments covered and a floor bought; skill over six WInS weeks cannot be measured and Wharton bars WInS gains as evidence | none | VERIFIED (CFA refresher PDF s.5.3.2) | no | cfainstitute.org rr-2018-l2v6r47.pdf |
| 18 | Liability-based mandates (cash flow or duration matching) differ from total return mandates, which "are generally structured to either track or outperform a benchmark" | S23 CFA Institute (2017; 2025) | PROCESS, LADDER | KNOWN | Tracking error and active return belong to total-return mandates; the ladder and floor are liability-based, so KILL tracking error to an index in Section 2 | VT alone tracks an index (FTSE Global All Cap); its tracking is Vanguard's job, not a test of Caplet | VERIFIED (CFA reading pages) | no | cfainstitute.org 2025 refresher summary; Wiley 2017 excerpt |
| 19 | "In the presence of liabilities, to minimize risk means to minimize the tracking error with respect to liabilities" | S24 EDHEC (n.d.) | LADDER, CERTAINTY | NICHE | The only tracking error that fits is against Laura's ten payments, which the coverage and hedge-ratio measures already report | Academic frame with continuous rebalancing, which Caplet never does | VERIFIED (EDHEC page) | no | climateinstitute.edhec.edu how-factor-investing-can-help-liability-driven-investors |
| 20 | The Sharpe ratio belongs to the performance-seeking portfolio ("the portfolio that achieves the highest Sharpe ratio"), not to a hedge; and six WInS weeks are no sample | S24 EDHEC (n.d.); WHARTON_NORTH_STAR s.4 | PROCESS | KNOWN | KILL Sharpe and attribution for the book; if VT's risk and return are discussed, use J.P. Morgan's 7.5% and 17.88% (NUMBERS 0), never WInS returns | none | VERIFIED (EDHEC multi-asset page; Wharton text in repo) | Risk: quoting WInS +1.85% as evidence breaches Wharton | climateinstitute.edhec.edu multi-asset-products-and-solutions; WHARTON_NORTH_STAR.md s.4 |
| 21 | Held-to-maturity accounting: debt held to collect contractual cash flows is carried at amortized cost; "it would not be appropriate ... to recognize interim fluctuations in fair value ... since those fluctuations will not be realized by the investor" | S26 PwC (2026) | LADDER, CERTAINTY | KNOWN | Supports showing the ladder at cost (Wharton's "amount allocated") and the TNA's "ignore price noise" | iBond ETFs are funds, not debt securities, and would not qualify as held-to-maturity; the analogy is to the principle only | VERIFIED (PwC Viewpoint 3.4.1) | no (TNA l.15) | viewpoint.pwc.com loans and investments 3.4.1 |
| 22 | US tax law lets "any obligation of the United States" fund fixed periodic payments if its payment periods are "reasonably related" to them and each asset payment "does not exceed the periodic payment to which it relates" | S27 26 U.S.C. 130(d) | LADDER, CERTAINTY | NICHE | Congress's own test for funding a schedule of fixed payments with Treasuries is one dated asset per payment; Laura's ladder meets the timing part | A tax rule for structured settlements, not an investment standard; T-bond rungs pay coupons years early, which 130(d) would not count as matched | VERIFIED (govinfo, 2024 ed.) | no | govinfo.gov USCODE-2024 title 26 sec 130 |
| 23 | Surplus view: "a fund with a zero surplus should be able to fulfill exactly its associated liabilities through ... a dedicated bond portfolio at current market interest rates" | S9 Leibowitz (1987) | LADDER | KNOWN | Laura's surplus on 6 Nov: $300,000 less $301,544 on the payment basis, less $302,287 on the instruments (NUMBERS 1): a small deficit that the IPS's 2028 completion closes | A pension's surplus moves daily; Laura's ladder is bought once, on one day in January 2027 | VERIFIED (Research Foundation PDF) | no (IPS l.13 completion rule) | rpc.cfainstitute.org rf-v1987-n1-4469-pdf.pdf |
| 24 | The WInS book is plan "(ii)R": Laura's position after both deposits scaled by 300/450. At cost: ladder $195,886.53 (65.3%), floor stand-in $72,765.65 (24.3%), VT $26,524.61 (8.84%), cash $4,823.21 (1.61%); times 1.5: $293,830, $109,148, $39,787, $7,235 = $450,000 | Team record; NUMBERS 8g; this card | LADDER, FLOOR, CEILING | NICHE | Explain once in Section 2: the table is the plan in miniature, not Laura's January 2027 purchase, which is all ladder | WInS cannot show dates: the plan buys the ladder in 2027 and the floor and VT in 2028 | VERIFIED (arithmetic on SNAP prices; team record "ladder about 66%, floor about 25%, stocks about 9%") | Risk: reading the table as the January 2027 purchase contradicts IPS l.13 "your entire first deposit" (CANON D3) | caplet/google_drive/notes_and_discussions.md l.307-308; SNAP l.22-32 |
| 25 | The team rejected "Book L" (WInS shows only the first $300,000, all bonds, no VT) so that the book would show the whole strategy | Team record | PROCESS | NICHE | A real implementation choice about what the simulator should demonstrate; one line in Section 2 or the Reflection | Wharton's example table is a $300,000 book; one sentence stops a judge reading VT as bought with the first deposit | VERIFIED (team record) | no | caplet/google_drive/notes_and_discussions.md l.305-309 |
| 26 | Each holding's job ("Pays for"): IBTM 2033 rung plus floor stand-in; IBTO-IBTR 2034-2037; T-bonds Feb-2037 to Nov-2041 for 2038-2042; VT growth. IBTM = 1,142 rung shares + 3,361 floor shares; floor 73.3% of floor plus VT at cost | SNAP l.22-32; trading_notes.csv l.63; NUMBERS 0 | LADDER, FLOOR, CEILING | KNOWN | Wharton's "intended roles of the most important holdings": one line each; IBTM's two lots are the key story | One WInS position cannot show two purchase dates or which shares are which (CANON Table E) | VERIFIED | no (TNA l.13 "two jobs") | SNAP; caplet/google_drive/sheets/portfolio_and_trading_notes/trading_notes.csv l.63 |
| 27 | Coverage per payment (WInS position over a full $50,000 rung, 23 Oct curve): iBond rungs 2033-2037 67.6-67.7%; 2038 69.3%; 2039 70.4%; 2040 65.6%; 2041 68.0%; 2042 69.1%; whole ladder 68.0% against 66.7%. Scaled by 1.5 it pays $510,396 for $500,000; nine payments at or above $50,000, the 2040 one $49,165 ($835 short) because bonds come in $1,000 lots | This card (register engine re-run at 23 Oct; reproduces NUMBERS 8b) | LADDER | NICHE | Honest construction evidence: a little above scale on average, one rung slightly under from lot rounding | Not yet in NUMBERS; on NUMBERS 1's 6 Nov faces the bond ratios are 65.4-70.2% | MODEL (this card) | Inconsistency I1: "67-72%" in CLAUDE.md is high at the low end; use "about 66-70%" once adopted | method under "Arithmetic behind this card" |
| 28 | What the book cannot show: the 2028 deposit and the ladder's completion; Keel's reinvestment margin (decided 9 Nov, after the freeze); the short-term Treasury ETF for waiting money; the 2031 move; purchase dates. VT is 8.84% of the book but 7.45% of $450,000 in the plan with the margin | CANON Table E; NUMBERS 2, 4 | LADDER, FLOOR, CEILING | KNOWN | Section 2 says the book shows the plan as traded; the margin is how the 2028 completion is carried out (Section 3) | none | VERIFIED (repo) | Risk: implying the frozen weights already include the margin (I5) | CANON Table E; NUMBERS 2, 4 |
| 29 | Each holding ends before its payment: 17 days early for the five iBond ETFs ("on or about" 15 Dec), 47 days for three bonds, 231 days (May-2038) and 320 days (Feb-2037); none after | CANON B8; S30 | LADDER | KNOWN | The verifier's date test (row 8): 10 of 10 | "On or about" lets a fund's end date move slightly | VERIFIED | Wording: IPS "just before" against TNA's "10.5-month gap" (CANON D6) | CANON B8; ishares.com IBTM (read 9 Nov 2026) |
| 30 | WInS's pie chart labels the iBond ETFs "Long Equities" (61.6% at market; 61.28% at cost) although they hold Treasuries | COMPETITION.md s.4; NUMBERS 8g | OTHER | NICHE | One table note; the asset-type column says "ETF (Treasury)" | none | VERIFIED (team record) | no | competition/COMPETITION.md l.117 |
| 31 | Commissions: 6 ETF trades at $25 + 5 bond trades at $10 = $200, 0.067% of $300,000; 11 of 200 trades; no trade after 8 Oct; nothing sold; the cash reconciliation shows no charge for the four cancelled orders | COMPETITION s.4; SNAP l.15, l.71; this card | PROCESS | TEXTBOOK | "Small and chosen" is fair for execution: the hold rule was kept and nothing was rebalanced | none | VERIFIED (arithmetic on the WInS export) | no | SNAP; COMPETITION.md s.4 |
| 32 | Accrued interest: $1,109.42 was paid as accrued interest at purchase. It is not a cost: it is the earned part of the next coupon, paid back in full on that coupon date. Standard accrual to 6 Oct with WInS's 15 Aug date on the May-2038 bond gives $1,113.48 (correct dates $1,338.48, so WInS undercharged about $225); WInS's 23 Oct figure ($1,285.99) matches the same method to 22 Oct ($1,288.59) | This card; SNAP check 3; COMPETITION s.4 | PROCESS | NICHE | The table note can say the cash line includes the accrued interest and commissions (NUMBERS 8g) without calling accrued interest a loss | The $225 is a simulator artifact; Laura's real purchase pays standard accrual | MODEL arithmetic (this card), within ETF price rounding | Partly resolves SNAP check 3; still quote no WInS accrued figure in the report (CANON E; I3) | SNAP l.10-12, l.67-68; COMPETITION.md l.116 |
| 33 | Bond fills against the Treasury curve: yields 5.25-5.60%, between 2.6 and 8.8 basis points from the curve on the 6 and 7 Oct closes, all inside the team's 25-basis-point rule; together the five cost $56 (7 Oct curve) to $192 (6 Oct curve) less than curve value. The 28 Sep ticket checks were 1.9-15.3 basis points | This card (S31 curve); trading_notes.csv l.73, 88, 102, 115, 129 | LADDER, PROCESS | NICHE | Evidence the yield-check rule worked: the ladder cost what the Treasury market said, not a trading accident | The par curve is built from on-the-run issues; older bonds normally sit a few basis points off it | MODEL (this card) on VERIFIED inputs | no | competition/official_market_data/daily-treasury-rates_2026-10.csv; SNAP l.27-31 |
| 34 | The yield-check rule changed instruments: the 4.5% Feb-2036 bond (stale price on 29 Sep) lost to IBTR for the 2037 payment, although the bond offered 92% fixed cash against 88% and no fee or NAV risk for about $1,400 more upfront; the stale 4.375% Feb-2038 bond was not used | rb_tickets.csv l.10, l.18; trading_notes.csv l.7-15; EXPERIENCE_RECORD s.1 | PROCESS, LADDER | NICHE | "Whichever works best for each year" (IPS l.13) in action: one rung was a real choice (CANON D13) | On certainty alone the bond was better for that rung; say so plainly | VERIFIED (team record) | Risk: IPS "pay what they say" fits the bond better than IBTR (CANON D5) | rb_tickets.csv; trading_notes.csv l.7-15 |
| 35 | ETF trading costs: IBTM 30-day median bid/ask 0.05%, premium 0.03% (27 Oct); VT 30-day bid/ask 0.01% (6 Nov). Half the spread is about $46 on the $183,851 of iBond ETFs and about $1 on VT. After hours on 19 Oct Nasdaq showed IBTM bid $19.16 and ask $24.31 (about 10% over the last price), which is why the team used limit orders in market hours | S30; S29; casestudy_pack.md R9; COMPETITION s.4 | PROCESS | KNOWN | Section 2: execution cost about $250 in all (0.08%), and the control that kept it there | Fill-day premiums to NAV (6-8 Oct) not read at source; half-spread is an estimate | VERIFIED issuer pages; estimate this card | no | ishares.com IBTM; advisors.vanguard.com VT; keel/library/assistant_review_2026-10/oct20/casestudy/casestudy_pack.md l.231 |
| 36 | The implementation cost of the WInS-only rule: the ten instruments cost $743 more than the payment-date ideal at forward rates ($302,287 against $301,544, including $1,098 of iBond fees), but fall $54,595 short if coupons earn nothing | NUMBERS 1, 2, 3 | LADDER, CERTAINTY | NICHE | The real cost of implementing with what WInS lists is reinvestment exposure, not commissions; this is where Section 2 hands over to Section 3 | none | VERIFIED (register) | Same risk as row 8 | NUMBERS 1-3 |
| 37 | Markowitz: security returns "are too intercorrelated. Diversification cannot eliminate all variance"; mean-variance implies "the 'right kind' of diversification for the 'right reason'" | S28 Markowitz (1952) | CEILING | TEXTBOOK | VT removes company risk, not market risk; the market fall that remains is why only unpromised money is in VT | Mean-variance looks at one portfolio's returns and ignores liabilities | VERIFIED (JSTOR copy) | no (TNA l.23 "diversified across countries and sectors") | Markowitz 1952 PDF (JSTOR copy, read 9 Nov 2026) |
| 38 | Three forms of risk management: diversification builds a performance-seeking portfolio; hedging builds a liability-hedging portfolio; insurance allocates between them | S25 Martellini & Milhau (2021) | LADDER, CEILING, FLOOR | NICHE | Diversification means different things by part: the ladder and floor hedge (one issuer, ten dates); VT diversifies; the floor plus the half moved in 2031 is a static form of insurance | EDHEC's insurance is dynamic; Caplet's is static and must not be called CPPI (COMPETITION s.7) | VERIFIED (EDHEC page) | no | climateinstitute.edhec.edu diversification-and-insurance-which-should-come-first |
| 39 | VT's breadth at the source: 10,185 stocks (30 Sep 2026); its index has "approximately 8,000 holdings in over 47 countries"; developed 89.98%, emerging 10.02%; foreign holdings 37.37%; 0.06% fee; technology 34.2%; top ten about 23.5% | S29 Vanguard (2026) | CEILING | KNOWN | One trade buys the world: the diversification measure for the growth part | Cap-weighted: a third in one sector, nearly a quarter in ten names; in a world recession all markets fall together, the IPS's own point | VERIFIED (Vanguard product page, fact sheet, investment profile) | no (TNA "about 10,000 stocks"; CANON B13) | advisors.vanguard.com VT; fund-docs.vanguard.com/F3141.pdf |
| 40 | In the hedging part one issuer is the point: 89.55% of the book at cost in US Treasury obligations ($268,652.18; IBTM itself 99.45% Treasuries); other issuers would add default risk against fixed dollar payments; the ten rungs spread the book across dates, not credits | NUMBERS 8g; CANON C7; S8 Ryan (2013) | LADDER, CERTAINTY | KNOWN | Answers "appropriate diversification" for the bond part in one sentence | The single-credit exposure is real and named by the IPS itself ("barring a US default") | VERIFIED | no (IPS l.11) | NUMBERS 8g; CANON C7 |

## Best five for the report

1. **The escrow verifier's two tests (rows 7-9, 29).** A judge sees that a professional standard exists for exactly
   Laura's problem and that the team applied it to itself: Treasuries ending on or before every payment, 10 of 10;
   sufficient without reinvestment, 89.1% as bought, closed by the IPS's own 2028 completion. Honest and exact.
2. **Implementation shortfall, split the way a bond desk would (rows 1-3, 31-35).** Execution cost about $250 (0.08%),
   bonds bought within 9 basis points of the curve, against a $37,625 swing in the ladder's price through 2026. For
   bonds, rates dominate cost; so Laura is protected by the completion rule, not by trading skill, which also keeps
   WInS timing out of the evidence as Wharton asks.
3. **The STRIPS history (rows 10, 36).** A certain match needs zero-coupon bonds; the rules forbid them, which puts
   the team where dedication stood before 1985. The reinvestment risk is the price of the rules ($743 at forward
   rates, up to $54,595 if coupons earn nothing), named rather than hidden.
4. **The plan in miniature, measured rung by rung (rows 24-27).** Two-thirds scale, 68.0% of the full ladder, one
   rung $835 short from $1,000 lots. Construction judged against Caplet's own policy portfolio, flaw included.
5. **Hedge ratio 78% against cash-flow coverage 100% (row 14).** Explains the TNA's "duration-matching" in a way a
   fixed-income reader respects: matched by cash on dates, not by duration, and the 22% gap is the coupons.

## Gaps

- The final WInS export after the freeze is not in the repo: final values, the five bonds' WInS identifiers (532281 is
  probably May-2038, NUMBERS 8g) and whether the November iBond distributions were credited.
- Fill-day ETF premiums or discounts to NAV (6-8 Oct) were not read at the iShares premium history; row 35 is an
  estimate from 27 Oct and 6 Nov issuer figures.
- Perold (1988) full text not read (paywalled); quotes come from the 1998 reprint's excerpts.
- No AICPA attestation standard for escrow verification was read; the "without reinvestment" and 0% conventions rest
  on Moody's methodology and escrow agreements.
- Whether WInS lists a short-term Treasury ETF for waiting money remains UNVERIFIED (CANON A15).
- Rows 27, 32, 33 and the half-spread in row 35 are this card's arithmetic: NUMBERS must adopt or reject them before
  any report use. Inconsistencies I1-I7 are for the owners of NUMBERS and CANON.
- FLOOR and CEILING are thin here by design (Section 3 material); the floor lot's payout and the 2031 range live in
  NUMBERS 3-4.
