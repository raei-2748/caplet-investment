# Q20: A pooled book or Keel's margin for the ten payments (Final Report part 3a)

**Date.** Tue 10 Nov 2026 (Sydney). Web sources read that day (Parallel web_search and web_fetch, Firecrawl), unless a
row says otherwise. Notes for the Final Report store, not report prose. Every figure is MODEL: re-derived on the
register's engine (`../../numbers/engine.py`, `plan.py`, 6 Nov 2026 curve) by `../../numbers/pooled.py`; results in
`../../numbers/results_pooled.json`. The IPS, the Trading Notes and the WInS book are frozen: a clash is a risk to
record, never a change to the strategy.

**Why this card.** Scorecard target 2 (`../../SCORECARD.md`): the bond-desk judge marked 3a down because "certainty
still depends on rates under Keel's call" and proposed a pooled book (`../panel/2026-11-09_judge_bond_desk.md`,
weakness 1, section 3 items 6-11). NUMBERS section 2 carries the candidate, unchecked against CANON.

**Claims tested.**
1. "A pooled book (every coupon pays the next payment due) that still buys all ten rungs in January 2027 is consistent
   with every frozen word." The lead's prior: it clashes with CANON A12, A17 and A18 unless every rung is held at
   least at its own design-A size, so each rung's own coupons still fund it at forward rates and pooling is only a
   backstop.
2. "A pooled book with every rung at least its design-A size at forward rates pays all ten even if interest earns
   nothing, for about $9,486 more than Keel's call ($332,922 against $323,436, NUMBERS 2)." Plus three variants: floors
   at Keel's call's rung sizes; floors in the frozen WInS book's rung shape; floors at 25%, 50% and 75%.
3. "If Keel's call stays, the 6% of history windows where the ten fall short (worst $12,117, start Jul 2007) are paid
   by X."
4. "The certainty definition a fixed-income professional would sign is 'every payment paid even if no coupon earns a
   cent'."

**Problem class.** Defeasance sufficiency: does a fixed schedule of assets pay a fixed schedule of liabilities, and
under which reinvestment assumption? The prior art is the municipal escrow verifier, defeasance accounting, pension
dedication (Leibowitz) and insurers' asset adequacy testing (NY Regulation 126). The design question is an operating
rule for coupons (the IPS never states one) plus a sizing standard for the January 2028 completion.

**Method (MODEL).** Same curve, ten instruments, reinvestment worlds (forwards; falls of 1, 2, 3 points for good;
zero; 585 history windows of the 1-year Treasury yield, Jan 1962 to Sep 2010) and gift model (`plan.run`, margin =
design cost less $302,287) as NUMBERS 1-4. Three operating rules:
- *own* (design A, Keel's call, the Trading Notes' wording): each rung's coupons are reinvested in Treasuries maturing
  before its own payment; surplus carries forward.
- *pooled* (design B): every flow is held only to the next payment due; surplus carries forward.
- *hybrid*: the ten rungs run *own*, plus a backstop of extra face in the same ten Treasuries run *pooled*.
Sizing at 0% is a linear programme (at 0% all ten are paid if and only if the cash arrived by each 1 January covers
the payments due by then). Solved by the engine's heuristic (`size_matched`, which made NUMBERS 2) and by exact vertex
enumeration (10 variables, 20 constraints): the two agree to the dollar for every floor tested, so NUMBERS 2's figures
are true minima. NY Regulation 126 scenarios are applied to today's spot curve ("level"), not to forwards, with and
without the regulation's floor (5-year rate not below 50% of its start).

**Sources read (APA 7; S-numbers used in the table).**
- S1 Moody's Investors Service. (2020, July 15). *Rating methodology: Pre-refunded and escrow-backed transactions*.
  https://ratings.moodys.com/api/rmc-documents/68216 (excerpts; the PDF is watermarked "OUTDATED METHODOLOGY")
- S2 City of Austin, Texas. (2024). *Escrow agreement: Water and wastewater system revenue refunding and improvement
  bonds, Series 2024* (ss. 3.03, 4.02). https://services.austintexas.gov/edims/document.cfm?id=427345
- S3 City of Austin, Texas. (2026). *Council meeting backup: August 27, 2026, file ID 26-2278: Escrow agreement* (ss.
  4.02-4.03; the heading the PDF prints, REFERENCES_APA 11 Nov). https://services.austintexas.gov/edims/document.cfm?id=479581
- S4 City of Kyle, Texas. (2024). *Resolution No. 1586: Providing for debt defeasance for FY 2024-2025*.
  https://www.cityofkyle.gov/media/0recfy0t/resolution_-_providing_for_debt_defeasance_for_fy_2024-2025.pdf
- S5 Trustees of the California State University. (2022, June 9). *Voluntary notice: Posting of escrow agreement,
  systemwide revenue bonds* (with the verification report of April 6, 2021). Municipal Securities Rulemaking Board,
  EMMA. https://emma.msrb.org/P21580535-P21220057-.pdf
- S6 City of Vero Beach, Florida. (2018). *Escrow deposit agreement: Electric refunding revenue bonds, Series 2003A*.
  https://www.covb.org/DocumentCenter/View/1657/8B-3
- S7 City of St. Clair Shores, Michigan. (2021). *Security report 557* [Bond resolution filing]. Michigan Department
  of Treasury. https://treas-secure.state.mi.us/DocumentSearch/Home/downloaddoc?doccd=SECURITY557&dyr=2021&luid=2994&sqn=1
- S8 Governmental Accounting Standards Board. (1987). *Statement No. 7: Advance refundings resulting in defeasance of
  debt* (para. 4 and fn. 2; based on FASB Statement No. 76). https://storage.gasb.org/GASBS-07.pdf
- S9 Governmental Accounting Standards Board. (2017). *Statement No. 86: Certain debt extinguishment issues*.
  https://storage.gasb.org/gasbs86.pdf
- S10 Leibowitz, M. L. (1986). The dedicated bond portfolio in pension funds, Part I: Motivations and basics.
  *Financial Analysts Journal, 42*(1), 68-75. https://doi.org/10.2469/faj.v42.n1.68 (abstract page, CFA Institute RPC)
- S11 Leibowitz, M. L. (1986). The dedicated bond portfolio in pension funds, Part II: Immunization, horizon matching
  and contingent procedures. *Financial Analysts Journal, 42*(2), 47ff. https://doi.org/10.2469/faj.v42.n2.47
  (abstract page; end page not shown)
- S12 Ryan, R. J. (2013). *The evolution of asset/liability management*. Research Foundation of CFA Institute
  (Literature Review 8(2)). https://rpc.cfainstitute.org/sites/default/files/-/media/documents/book/rf-lit-review/2013/rflr-v8-n2-1-pdf.pdf
  (quotes Fabozzi, F. J. (2005). Dedicated bond portfolios. In *The handbook of fixed income securities* (7th ed.,
  pp. 1103-1117). McGraw-Hill.)
- S13 CFA Institute. (2017). *Overview of fixed-income portfolio management* [Curriculum reading, Wiley excerpt, ISBN
  978-1-946442-91-8]. https://catalogimages.wiley.com/images/db/pdf/9781946442918.excerpt.pdf
- S14 Jhawar, V. (2015, February 26; page as read 10 Nov 2026). *Portfolio immunization vs. cash flow matching: What's the
  difference?* Investopedia.
  https://www.investopedia.com/articles/investing/022615/portfolio-immunization-vs-cash-flow-matching.asp
- S15 N.Y. Comp. Codes R. & Regs. tit. 11, § 95.10(d) (Regulation 126: required interest scenarios).
  https://www.law.cornell.edu/regulations/new-york/11-NYCRR-95.10
- S16 New York State Department of Financial Services. (2026, August). *Special considerations relating to December
  31, 2026 reserves and other solvency issues* (items 4 and 5). https://ko.dfs.ny.gov/system/files/documents/2026/08/spec_con_2026.pdf
- S17 National Association of Insurance Commissioners. (2025). *Actuarial Guideline LV: Application of the Valuation
  Manual for testing the adequacy of reserves related to certain life reinsurance treaties* (Appendix 1, New York 7).
  https://content.naic.org/sites/default/files/inline-files/AG%2055%28adopted%29_1.pdf
- S18 American Academy of Actuaries. (2024). *Asset adequacy analysis* [Practice note].
  https://actuary.org/wp-content/uploads/2025/03/Life-PracticeNote-2017AATUpdate.pdf (search excerpts)
- S19 Kocherlakota, R., Rosenbloom, E. S., & Shiu, E. S. W. (1988). Algorithms for cash-flow matching. *Transactions
  of the Society of Actuaries, 40*(1), 477-484. (Citation confirmed in the SOA index, vols. 36-40,
  https://www.soa.org/globalassets/assets/library/indexes/index-to-the-transactions-of-the-soa/1984-1988/january/TSAIndex36-40.pdf;
  the paper itself was not reachable)
- S20 Society of Actuaries. (2002). Defining asset-liability management (ch. 2). In *Asset-liability integration*
  (Monograph M-FI02-1). https://www.soa.org/globalassets/assets/library/monographs/finance/asset-liability-integration/2002/january/m-fi02-1-02.pdf
- S21 U.S. Securities and Exchange Commission, Office of Chief Counsel. (1993, June 24). *T. Rowe Price Tax-Free
  Funds* [No-action letter]. https://www.sec.gov/divisions/investment/noaction/1993/troweprice062493.pdf
- Repo: FINAL IPS (`../../FINAL_IPS_as_submitted.txt`, lines as `cat -n`); TNA (`../../../drafts/writing_room_2026-11-03/tna_as_submitted.txt`);
  WN (`../../../../caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`); `../../CANON.md`;
  `../../NUMBERS.md`; `../HARVEST_BRIEF.md`; cards Q16, Q17; the engine files above.

## (a) Ideas

| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pooling creates no money: at 0% a pooled book holds exactly the same cash as an own-rung book of the same units; it only lets early coupons pay early payments. The fix for reinvestment risk is the sizing standard, not the pooling | pooled.py; engine.py designs A and B | REINVEST, LADDER | KNOWN | Says in one line why "pool the coupons" and "be certain" are two different decisions | none | VERIFIED: engine re-run (MODEL) | no | `numbers/pooled.py` deliver(), lp_min_cost() |
| 2 | Keel's call's own units, run pooled without re-sizing, get worse: any shortfall in 9.4% of windows (6.0% run own-rung), 1-in-20 $5,089 ($1,225), NY Reg 126 pop-down with the floor $1,088 short ($0); the $22,192 short at 0% moves to 2041 ($5,127) and 2042 ($17,065) | pooled.py, design KEEL_run_pooled | REINVEST, LADDER | NICHE | Kills "just pool the coupons" as a free improvement | One coupon rule, one curve | VERIFIED: engine re-run (MODEL) | no | results_pooled.json designs.KEEL_run_pooled |
| 3 | P100 (pooled, every rung at least its plain size, sized at 0%) costs $332,922, $9,487 more than Keel's call: rungs 2033-2040 at plain size, the 2041 bond 61% and the 2042 bond 67% bigger; the exact LP confirms it is the minimum | NUMBERS 2; pooled.py P100_engine, P100_lp | CERTAINTY, LADDER, COMPLETE2028 | NICHE | The register's figure stands as arithmetic | Run pooled, its bonds' coupons pay earlier payments (row 5) | VERIFIED: engine and exact LP agree (MODEL) | risk: CANON A17, HARVEST_BRIEF (row 5) | results_pooled.json designs.P100_lp |
| 4 | The lead's reading of P100 fails: its holdings run with each rung's own coupons reinvested in its own rung and only the extra pooled are $22,650 short at 0% (2036 $2,263 to 2040 $5,501), more than Keel's call ($22,192). P100 pays at 0% only if every coupon is pooled | pooled.py P100_holdings_run_as_hybrid | REINVEST, CERTAINTY | NICHE | Separates the operating rule (who gets each coupon) from the floor on rung sizes | none | VERIFIED: engine re-run (MODEL) | yes: as an own-rung book it does not pay at 0%; as a pooled book it strains A17 | results_pooled.json P100_holdings_run_as_hybrid |
| 5 | In P100 run pooled, each 2034-2040 payment gets only 58-76% from its own Treasury (principal plus that year's coupons) at forward rates, and up to $49,813 of the 2033 payment can come from the 2038-2042 bonds' coupons; the Nov-2039 bond's own cash reaching the 2040 payment is $28,741 (57%) | pooled.py canon_tests; CANON A12, A17; HARVEST_BRIEF l.37-39 | LADDER, REINVEST | NICHE | The test a strict judge would run on "rests on a dedicated instrument" | Money in a pooled book is fungible, so "which bond paid" is partly bookkeeping | VERIFIED: engine re-run (MODEL) | risk: WN l.18 "its fixed coupons and principal cover most of it" survives only through the principal; it is exactly HARVEST_BRIEF's flagged "later bonds' interest paying earlier payments" | results_pooled.json canon_tests |
| 6 | Hybrid H_plain: the ten at their plain sizes run own-rung (each rung's reinvested coupons fund the rest, as the WInS notes say), plus a backstop of extra face in the same Treasuries (IBTQ +$331, IBTR +$3,991, the five T-bonds +$5,458 to +$7,152 face) whose coupons and principal wait in the short-term Treasury ETF for the next payment due; sized so all ten are paid at 0%: $335,771, $12,335 over Keel's call (backstop $33,484) | pooled.py H_plain (exact LP for the backstop) | CERTAINTY, LADDER, COMPLETE2028, REINVEST | NICHE | The ten exactly as Caplet described them, plus a reserve whose interest is never counted on | $2,849 dearer than P100; the stated range rounds $5,000 lower (row 12) | VERIFIED: engine re-run (MODEL) | no: keeps IPS l.11, l.13, TNA l.13, l.15, WN l.18, l.24 literally | results_pooled.json designs.H_plain |
| 7 | Design A sized for 0% (each rung's own coupons and principal pay $50,000 with no interest on interest): $337,836, $14,400 over Keel's call and $2,065 over H_plain | NUMBERS 2; pooled.py A_zero | CERTAINTY, LADDER | KNOWN | The simplest sentence: "each Treasury is big enough to pay its year with no help from interest" | WN l.18's "reinvested coupons fund the rest" becomes a rest of zero | VERIFIED: engine re-run (MODEL) | no | results_pooled.json designs.A_zero |
| 8 | Floors at Keel's call's rung sizes, pooled and sized at 0%: $335,498 (+$12,062; the 2042 bond 47% bigger); the hybrid on Keel's sizes: $337,000 (+$13,564). Keel's minus-3 sizing over-buys the early rungs, whose cash is least useful at 0% | pooled.py Pkeel_lp, H_keel | CERTAINTY, COMPLETE2028 | NICHE | Starting from Keel's call costs more than starting from the plain ladder | none | VERIFIED: engine re-run (MODEL) | as rows 5 (pooled) and 6 (hybrid) | results_pooled.json |
| 9 | The frozen WInS book's rung shape (NUMBERS 8g cost shares; IBTM rung lot 1,142 shares): as floors scaled to $302,287, pooled at 0%: $333,017 (+$9,582, almost P100, because the shape is close to the plain ladder); the shape alone scaled up until it pays at 0%: $339,467 (+$16,032), run pooled or own-rung alike (the 2041-2042 rungs bind) | pooled.py Pshape_floor_lp, Pshape_pure, Ashape_pure; NUMBERS 8g; Q17 row 26 | LADDER, COMPLETE2028 | NICHE | Keeping the book's look costs up to $6,500 more than the cheapest certain design | WInS shares were bought at Oct prices; rescaled on the 6 Nov curve | VERIFIED: engine re-run (MODEL) | no | results_pooled.json |
| 10 | Floors at 25%, 50%, 75%: $320,707 (-$2,729), $322,352 (-$1,084), $325,569 (+$2,133). They beat Keel's call only by shrinking early rungs: the 2033 payment's own Treasury supplies 25% (P25) or 50% (P50), and the 2034-2036 payments 37-43% (P50); the rest is later bonds' coupons | NUMBERS 2; pooled.py P25/P50/P75 | LADDER, CERTAINTY | NICHE | Shows where the panel's "about the same cost" came from | none | VERIFIED: engine and LP agree (MODEL) | yes: TNA l.13 (IBTM "supports her first $50,000 payment") holds only weakly; A12 "rests on a dedicated instrument" fails in substance for 2033-2036 | results_pooled.json canon checks |
| 11 | Design B with no floor ($319,687) buys no 2033 or 2034 rung | NUMBERS 2; pooled.py B_zero_lp | LADDER | KNOWN | The bond desk's original number | none | VERIFIED (MODEL) | yes: IPS l.13 "buy 10 Treasuries"; TNA l.13 | results_pooled.json |
| 12 | What certainty costs the gift (central, per-end deductions 4.1% and 2.5%, $5k rounding): Keel's call floor $115,929, range $110,000-$130,000, kept half $23,986; P100 $106,779, $100,000-$120,000, $22,092; H_plain $104,031, $95,000-$115,000, $21,524; design A at 0% $102,040, $95,000-$115,000, $21,112. At $1,000 rounding: $111k-$133k, $102k-$122k, $99k-$119k, $97k-$117k. H_plain's floor is $244 short of the $104,275 that would state $100,000 | pooled.py gift(); plan.run | COSPONSOR, FLOOR, CEILING, HALFKEPT | NICHE | The honest price tag: about $10,000-$15,000 off the stated range for "paid even if no coupon earns a cent" | $5k rounding magnifies a $2,748 floor gap into $5,000 at each end | VERIFIED: engine re-run (MODEL) | no | results_pooled.json designs.*.gift |
| 13 | The floor still takes "most" of the 2028 deposit in every certain design: 61.3% (Keel's call), 56.5% (P100), 55.0% (H_plain), 54.0% (design A at 0%) | pooled.py gift(); IPS l.15 | FLOOR, COMPLETE2028 | NICHE | IPS l.15 "Most of the 2028 deposit will fund a Treasury fund" survives | Margin to the word "most" narrows from 11 to 5 points | VERIFIED (MODEL) | no | results_pooled.json |
| 14 | The certainty is bought, not spent: if rates follow today's forwards the ten overflow by $21,110 (Keel's call), $30,636 (P100), $33,461 (H_plain), $35,485 (design A at 0%), all in 1 Jan 2027 money, and the overflow is Laura's | pooled.py overflow | CERTAINTY, RESERVE2033 | KNOWN | "The extra only costs you anything in the world it is bought for" | Comes back from 2033 to 2042, after the gift | VERIFIED (MODEL) | no | results_pooled.json overflow_value_jan2027 |
| 15 | House model (200,000 paths), floor p5/p50/p95: Keel's call $93k/$116k/$140k; P100 $84k/$107k/$131k; H_plain $81k/$104k/$128k; kept half: $12k/$24k/$47k against $11k/$21k/$42k (H_plain) | pooled.py house; plan.house | FLOOR, HALFKEPT | KNOWN | The cost of certainty in the spread of outcomes, not only the centre | House model draws stocks and rates independently (NUMBERS 7) | VERIFIED (MODEL) | no | results_pooled.json house_gift_p5_p50_p95 |
| 16 | Keel's call falls short in 35 of 585 windows: one start (Nov 2000, $31, the 2042 payment only), then every start from Feb 2006 to Nov 2008, 34 in a row: one rate era. 287 of 5,850 payments are short (4.9%); 20 windows have all ten short; each short payment is $23 to $2,015 (at most 4.0% of a payment); worst Jul 2007, $12,117 ($391 in 2033 rising to $2,015 in 2041) | pooled.py claim3; NUMBERS 2 | REINVEST, CERTAINTY | NICHE | "Paid in full in every rate era since 1962 except the one that began in 2006-2008", with the size | 585 overlapping windows are about three independent periods (panel item 7) | VERIFIED: engine re-run (MODEL) | yes: IPS l.11 and TNA l.7 "near-ironclad" fail in those windows | results_pooled.json claim3_keel_shortfall_windows |
| 17 | Nothing in Treasuries is left to pay it: earlier rungs' surplus is already counted (design A carries it forward); the floor and the moved half are promised ("the bottom will remain constant", IPS l.15) and a rate move is no reason to change (IPS l.17; CANON A34: evaluate, never add a trigger); outside money is banned (case; IPS l.11 "anybody else's money"). Only the kept half (VT) is unpromised | IPS l.11, l.15, l.17; CANON A4, A34 | HALFKEPT, CERTAINTY, TWOREASONS | NICHE | X = the kept half of VT: in those windows a payment depends on a share price | The kept half's stated purpose is overruns, the Taiwan dollar and co-sponsors (IPS l.15), not payments | VERIFIED (frozen texts) | yes: IPS l.11 fails in 6.0% of windows, for up to 4% of a payment; IPS l.19 "ours is to take none" too | CANON A4, A34; IPS |
| 18 | The kept half in the same history (Shiller US stocks with dividends, the same months; $33,515 of VT bought Jan 2028, half kept from 2031): $16,673 to $118,039 at the short dates, at least 27.8 times each payment's shortfall. It covers every one, but only because those starts map 2033-2042 onto 2013-2023, a strong stock decade; the house model's 1-in-20 kept half on 1 Jan 2033 is $12,150, about the worst total shortfall | pooled.py claim3; plan.py Shiller data; NUMBERS 8f | HALFKEPT, CERTAINTY | NICHE | "Shares would have paid it, this time" is luck of alignment, not design | Three short dates use stock months after Jun 2023 (dividend held flat, flagged); rates and stocks from one history only here | VERIFIED: engine re-run (MODEL) | yes, as row 17 | results_pooled.json windows[].kept_half_at_short_dates |
| 19 | A 2031 check would see it: holding each window's rates at their Jan 2031 level, all 35 windows already show a shortfall in Jan 2031 ($261 to $14,949; at or above the final figure in 32 of 35). The canon lets Caplet evaluate, not act (A34), so the warning has nowhere to go but the kept half | pooled.py claim3; CANON A34; Q15 card | PROCESS, MOVE2031, CERTAINTY | NICHE | Monitoring (3e) could name it, but under Keel's call it would be a warning without a remedy | Projection rule is Keel's (rates held flat from 2031) | VERIFIED (MODEL) | risk: a remedy would be a new trigger (A34) | results_pooled.json projected_short_at_2031... |
| 20 | The escrow verifier's test: escrow cash flows "sufficient, without further reinvestment, to pay the debt service due on the transaction in full and on time", with maturities "on or prior to" each payment date; a real verification report states it will "assume that all cash balances are not reinvested". Escrows pool every security's cash against one schedule | S1 Moody's (2020); S5 CSU (2021 report) | CERTAINTY, LADDER | NICHE | The professional's words for IPS l.11: "paid even if no coupon earns a cent" | Escrows are irrevocable, legally defeased and built from made-to-measure SLGS; Laura buys WInS-listed Treasuries | VERIFIED (Moody's PDF and EMMA PDF excerpts) | no | ratings.moodys.com 68216; emma.msrb.org P21580535 |
| 21 | Idle escrow cash is reinvested in SLGS "with an interest rate equal to zero percent (0%)", or held "uninvested", in agreements from 2021 to 2026; sufficiency is certified "without reinvestment" by a CPA before any substitution | S2, S3 City of Austin; S4 City of Kyle | CERTAINTY | NICHE | 0% is the market's own convention, not a Keel invention | In Laura's plan the waiting money sits in a short-term Treasury ETF (CANON A15); 0% is only the sizing test | VERIFIED (agreement PDFs) | no | austintexas.gov 427345, 479581; cityofkyle.gov |
| 22 | Older wordings of the same test: principal "without consideration of any interest thereon or reinvestment of such maturing principal" (2018); obligations whose principal and interest, "without reinvestment, come due at times and in amounts sufficient" (2021); "sufficient without reinvestment" (SEC staff letter, 1993) | S6 Vero Beach; S7 St. Clair Shores; S21 SEC | CERTAINTY | NICHE | Thirty years of the same standard | none | VERIFIED (PDF excerpts) | no | covb.org; michigan.gov; sec.gov |
| 23 | Accounting defeasance (GASB 7, based on FASB 76; carried into GASB 86): assets "essentially risk-free as to the amount, timing, and collection of interest and principal", whose cash flows "approximately coincide, as to timing and amount" with the debt service; callable bonds do not qualify because "there is no assurance that the reinvested funds would provide the yields necessary" | S8, S9 GASB | CERTAINTY, LADDER | NICHE | Reliance on reinvestment yields is the named disqualifier | A government accounting rule, not an investment standard | VERIFIED (GASB PDFs, excerpts) | no | storage.gasb.org GASBS-07, gasbs86 |
| 24 | Pension dedication: the objective is often to "assure fulfillment even under totally passive management", which Leibowitz defines as "no reinvestment"; reinvesting at positive rates "can lower pension fund costs without substantially increasing risk or complexity" | S10 Leibowitz (1986a) | CERTAINTY, REINVEST | KNOWN | Both standards are professional: zero (strict) and a conservative positive rate (cheaper). Keel's call is the second; H_plain the first | Abstract only | VERIFIED (CFA RPC abstract) | no | rpc.cfainstitute.org FAJ v42 n1 |
| 25 | Textbooks: "Cash matching or prefunding these liabilities leads to the elimination of interest-rate risk and the defeasance of the liability" (Fabozzi's handbook, quoted by Ryan); cash flow matching "essentially has no underlying assumptions" but timing mismatches result "in some reinvestment risk" (CFA); early funds "must be reinvested at a conservative short-term rate" (Investopedia) | S12 Ryan (2013); S13 CFA (2017); S14 Jhawar (2015), Investopedia | LADDER, REINVEST | TEXTBOOK | Names the residual in Laura's ladder correctly: coupons arrive years before the payments | Fabozzi read through Ryan's quotation only | VERIFIED (PDF excerpts; Fabozzi via S12) | no (TNA l.5 names reinvestment-rate risk) | rpc.cfainstitute.org; catalogimages.wiley.com; investopedia.com |
| 26 | Actuaries "commonly assume" cash flow matching uses "zero-coupon risk-free government bonds", and a well-built matched book is "the ultimate buy and hold strategy" | S20 SOA (2002) | LADDER | NICHE | With STRIPS banned by Wharton, a no-reinvestment standard is bought with extra coupon bonds: about $12,000-$15,000 here | none | VERIFIED (SOA PDF excerpt) | no | soa.org m-fi02-1-02.pdf |
| 27 | NY Regulation 126 requires at least seven scenarios, among them "level with no deviation" and "an immediate decrease of three percent and then level"; rates "need not be reduced beyond" a 5-year yield of "50 percent of its initial level". On the engine: Keel's call passes all seven with that floor (without it, pop-down $5,337 short, down-then-up $49); the plain ladder fails even "level" ($5,678) because level means today's spot rates, below the forwards it was sized on; every 0% design passes all seven | S15 11 NYCRR 95.10(d); S17 NAIC AG LV App. 1; pooled.py NY7 | CERTAINTY, REINVEST | NICHE | Keel's call meets the insurer's standard; the ladder as written does not | Insurers test whole blocks with lapses and calls; Laura's ten are fixed | VERIFIED (Cornell LII; NAIC PDF) and MODEL | no | law.cornell.edu; content.naic.org |
| 28 | New York's 2026 letter makes the original falling scenarios sensitivity tests only; the required ones are milder (gradual down 0.40 a year, down then up 0.80, pop-down 2.50 points when rates are at least 5.0%) with floors at "the beginning rate less one half the 5-year Treasury rate"; actuaries note some New York 7 scenarios "may be considered beyond moderately adverse" | S16 NY DFS (2026); S18 AAA | CERTAINTY | NICHE | The insurer's norm is adequacy under moderately adverse scenarios, not zero | Life reserves, not a dated escrow | VERIFIED (DFS PDF; AAA excerpt) | no | dfs.ny.gov spec_con_2026; actuary.org |
| 29 | Kocherlakota, Rosenbloom and Shiu set cash-flow matching up as a linear programme (the method used here) | S19 | PROCESS | NICHE | Lets the report say the backstop is the cheapest one, by a published method | Paper not read; its reinvestment assumption unknown | UNVERIFIED (content); citation confirmed | no | SOA TSA index vols 36-40 |
| 30 | Every design here, Keel's call included, reads IPS l.13's "complete it with the 2028 deposit" as a completion standard, not only the $2,287 by which the ten exceed $300,000: the January 2028 completion is $24,475 (Keel's call), $34,383 (P100), $37,358 (H_plain), $39,515 (design A at 0%) | pooled.py gift(); NUMBERS 2; CANON intro (the top-up is the IPS's planned adjustment) | COMPLETE2028 | NICHE | One rule, one standard, decided in January 2028, never a trigger | The larger the standard, the larger the stretch of "complete" | VERIFIED (MODEL) | risk: a strict reader sees a margin, not a completion (same for Keel's call) | results_pooled.json |
| 31 | The Moody's methodology quoted in Q17 and here is the 15 Jul 2020 edition, now watermarked "OUTDATED METHODOLOGY"; the current edition was not read | S1 | PROCESS | NICHE | Cite it as the 2020 edition or replace it with the escrow agreements (rows 21-22) | none | CONFLICTING (Q17 S12 cites it as current) | no | ratings.moodys.com 68216 |

## (b) Cards: the strongest ideas

**1. The escrow verifier's test is Caplet's own promise in a professional's words (rows 20-24).**
- What is it? Municipal escrows, defeasance accounting and strict pension dedication all certify that a fixed
  schedule is paid by Treasuries "without further reinvestment", with idle cash at "zero percent".
- Did it work? Yes: it is how pre-refunded bonds keep top ratings, written into escrow agreements from 2018 to 2026.
- How is Laura's case like it? Ten fixed dollar payments, funded in advance with Treasuries, certain "barring a US
  default" (IPS l.11): a structural promise (CANON A4), not a probability.
- How is it not? No trustee, no legal defeasance, no made-to-measure SLGS; WInS-listed bonds pay coupons years early.
- What Caplet takes: the test a fixed-income reader trusts most, in seven words: "paid even if no coupon earns a cent".

**2. Pooling only works if every coupon is pooled (rows 1-5).**
- What is it? P100 ($332,922) pays at 0% only when each bond's coupons pay the next payment due; run with each rung's
  coupons kept for its own payment, the same holdings are $22,650 short at 0%.
- Did it work? As arithmetic, yes (engine and exact LP agree); as a reading of the frozen words, only partly.
- How is Laura's case like it? Escrows pool, so P100 is the textbook escrow form.
- How is it not? Caplet's notes describe each bond funding its own payment: "its fixed coupons and principal cover
  most of it; reinvested coupons fund the rest" (WN l.18). In P100 that bond's own cash is 57% of its payment, and
  up to $49,813 of the 2033 payment can come from the 2038-2042 bonds.
- What Caplet takes: the lead's prior is half right. A floor on rung sizes is not enough; the operating rule decides
  consistency.

**3. The ten as written, plus a backstop whose interest is never counted on (rows 6, 12-14).**
- What is it? H_plain: each rung exactly as the Trading Notes describe, plus extra face in IBTR and the five T-bonds,
  bought with the 2028 deposit, whose coupons and principal wait in a short-term Treasury ETF for the next payment due.
- Did it work? All ten paid at 0%, at every fall for good, in all 585 windows and all seven NY scenarios; $335,771.
- How is Laura's case like it? It is the 2028 completion the IPS already names, sized to the escrow standard instead
  of Keel's minus-3 standard.
- How is it not? It costs $12,335 more than Keel's call and moves the stated range from $110k-$130k to $95k-$115k.
- What Caplet takes: the cheapest design that makes IPS l.11 true at 0% and keeps every quoted line literally.

**4. Keel's call's 6% is one era, and only shares could pay it (rows 16-19).**
- What is it? 35 of 585 windows short, 34 of them starting Feb 2006 to Nov 2008; up to $2,015 on one payment and
  $12,117 in all.
- Did it work? In that history the kept half would have covered it 27.8 times over, because 2013-2023 was a strong
  stock decade.
- How is Laura's case like it? IPS l.11 promises no payment depends on a share price; in those windows one would.
- How is it not? The amounts are small (at most 4% of a payment) and a 2031 check would see them coming.
- What Caplet takes: if Keel's call stays, 3a must say in numbers that the residual falls on the kept half, and that
  the canon allows no rule to move it (A34).

**5. Keel's call already meets the insurer's standard; the ladder as written does not (rows 27-28).**
- What is it? NY Regulation 126's seven scenarios, applied to today's curve.
- Did it work? Keel's call passes all seven with the regulation's floor; the plain ladder fails even "level"
  ($5,678 short), because "level" means today's spot rates, below the forwards it was priced on.
- How is Laura's case like it? An adequacy test of fixed outflows against bond cash flows under falling rates.
- How is it not? Insurers test "moderately adverse" conditions for a going concern; Laura's promise is structural.
- What Caplet takes: two honest standards exist. Keel's call is "adequate under moderately adverse rates"; the
  zero standard is "certain barring default", which is what the IPS says.

**6. What certainty costs and what comes back (rows 12-15).**
- What is it? Each dollar added to the 2028 completion is a dollar less for the floor and the VT purchase.
- Did it work? Central: P100 costs the gift $9,150 of floor and $1,894 of kept half against Keel's call; H_plain
  $11,898 and $2,462. If forwards hold, $30,636 (P100) or $33,461 (H_plain) flows back from 2033 to 2042.
- How is Laura's case like it? Payments are "fixed and non-negotiable" (IPS l.11); the facility is the flexible part.
- How is it not? The stated range is what co-sponsors hear; $5,000 rounding makes the step look bigger than it is.
- What Caplet takes: the price of the zero standard is about $10,000-$15,000 off the stated range, paid back in full
  unless rates fall.

## (c) Verdicts

| Claim | Verdict | Why, in one line |
|---|---|---|
| 1 | CHANGE | No fully pooled book keeps every frozen word: run pooled, each bond's coupons pay earlier payments (P100: own Treasury 58-76% of each 2034-2040 payment; up to $49,813 of 2033 from the 2038-2042 bonds), which strains WN l.18 and is HARVEST_BRIEF's flagged contradiction; floors below the plain size (P25, P50) also break TNA l.13 and A12 in substance. The prior is half right: the floor at design-A size is necessary but not sufficient. What keeps every line is the operating rule (own-rung base, pooled backstop: H_plain). In the other direction, a zero-sufficient book fits IPS l.11, l.19, TNA l.7 ("near-ironclad") and l.15's "(not merely a forecast)" better than Keel's call does. |
| 2 | CHANGE (arithmetic KEEP) | $332,922 and +$9,487 re-derived, and the exact LP shows the engine's sizing is the true minimum. But that cost holds only if every coupon is pooled; the same holdings run as the prior describes are $22,650 short at 0%. The prior's design costs $335,771 (+$12,335). Variants: floors at Keel's sizes $335,498 (+$12,062); WInS shape as floors $333,017 (+$9,582), pure shape $339,467 (+$16,032); 25/50/75% floors $320,707 / $322,352 / $325,569. The panel's "the gift's bottom barely moves" is wrong: $10,000 (P100) to $15,000 (H_plain) off the stated bottom. |
| 3 | KEEP the size; X named | X = the kept half of VT, the only unpromised money; the floor and moved half are promised (IPS l.15), a rate move is no reason to change (l.17, A34), outside money is banned (case, l.11). So in 35 of 585 windows (6.0%; 287 of 5,850 payments, $23-$2,015 each) a payment would depend on a share price, and IPS l.11 fails there. The kept half covered every case in this history, by luck of a strong 2013-2023 market. |
| 4 | CHANGE (precision) | "Paid even if no coupon earns a cent" is the escrow verifier's and the defeasance accountant's test, and the strict form of pension dedication; it matches Caplet's structural definition (IPS l.11, CANON A4). It is not the only professional norm: insurers sign adequacy under moderately adverse scenarios (NY Reg 126), which Keel's call meets, and pension practice often reinvests at a conservative positive rate. Say "the test a municipal escrow verifier applies", not "the definition professionals sign". |

**Design table (MODEL; 6 Nov 2026 curve; 1 Jan 2027 value; history = 585 windows, 1962-2010 starts).**

| Design | Cost | vs Keel's call | Rungs bought | Short at 0% | Short if rates fall 1 / 2 / 3 pt for good | History: windows short / 1-in-20 / worst (start) | NY Reg 126 pop-down 3 pt: with floor / without | Floor payout | Stated range ($5k) | Kept half 1 Jan 2033 | Back to Laura at forwards | CANON lines kept or broken |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A as written (forwards) | $302,287 | -$21,149 | 10 | $54,595 | $12,172 / $23,509 / $34,083 | 55.6% / $34,555 / $45,266 (Jul 2007) | $31,823 / $39,013 (level $5,678) | $136,328 | $130k-$155k | $28,206 | $0 | Breaks l.11 in most tests |
| **Keel's call** (A, minus 3 pt) | **$323,436** | 0 | 10 | $22,192 | 0 / 0 / 0 | 6.0% / $1,225 / $12,117 (Jul 2007) | $0 / $5,337 | $115,929 | $110k-$130k | $23,986 | $21,110 | Keeps A12, A17, A18, l.13, TNA l.13; l.11 and l.19 fail in 6.0% of windows and at 0%; strains TNA l.15 "(not merely a forecast)" |
| Keel's units run pooled | $323,436 | 0 | 10 | $22,192 | 0 / 0 / 0 | 9.4% / $5,089 / $12,900 (Jul 2007) | $1,088 / $9,026 | $115,929 | $110k-$130k | $23,986 | $21,110 | Worse than Keel's call on every test; strains A17 |
| B, no floor | $319,687 | -$3,748 | 8 | 0 | 0 | 0% | 0 / 0 | $119,545 | $110k-$135k | $24,734 | $17,599 | Breaks IPS l.13 (ten), TNA l.13 |
| P25 | $320,707 | -$2,729 | 10 | 0 | 0 | 0% | 0 / 0 | $118,561 | $110k-$135k | $24,530 | $18,628 | Breaks A12 in substance (2033 own 25%); TNA l.13 weak |
| P50 | $322,352 | -$1,084 | 10 | 0 | 0 | 0% | 0 / 0 | $116,975 | $110k-$130k | $24,202 | $20,288 | As P25 (2033 own 50%, 2034-36 37-43%) |
| P75 | $325,569 | +$2,133 | 10 | 0 | 0 | 0% | 0 / 0 | $113,872 | $105k-$130k | $23,560 | $23,468 | Strains A12 (2034-38 own 49-65%), A17 |
| **P100** (pooled, plain floors) | **$332,922** | +$9,487 | 10 | 0 | 0 | 0% | 0 / 0 | $106,779 | $100k-$120k | $22,092 | $30,636 | Keeps l.11, l.13, l.19, TNA l.7, l.13; strains A17 (Nov-2039 bond 57% of its payment), HARVEST flag |
| Pooled, Keel's floors | $335,498 | +$12,062 | 10 | 0 | 0 | 0% | 0 / 0 | $104,295 | $100k-$120k | $21,578 | $33,172 | As P100 |
| Pooled, WInS-shape floors | $333,017 | +$9,582 | 10 | 0 | 0 | 0% | 0 / 0 | $106,688 | $100k-$120k | $22,073 | $30,733 | As P100 |
| WInS shape scaled up | $339,467 | +$16,032 | 10 | 0 | 0 | 0% | 0 / 0 | $100,466 | $95k-$115k | $20,786 | $37,092 | Keeps all lines; dearest |
| **H_plain** (ten as written + pooled backstop) | **$335,771** | +$12,335 | 10 | 0 | 0 | 0% | 0 / 0 | $104,031 | $95k-$115k ($99k-$119k at $1k) | $21,524 | $33,461 | Keeps every quoted line literally: l.11, l.13, l.15 ("most" 55.0%), l.19, TNA l.7, l.13, l.15, WN l.18, l.24 |
| H on Keel's sizes | $337,000 | +$13,564 | 10 | 0 | 0 | 0% | 0 / 0 | $102,847 | $95k-$115k | $21,279 | $34,666 | As H_plain, dearer |
| A sized for 0% | $337,836 | +$14,400 | 10 | 0 | 0 | 0% | 0 / 0 | $102,040 | $95k-$115k | $21,112 | $35,485 | Keeps all; WN l.18's "rest" becomes zero |

Rung sizes (units: fund dollars or bond face) for the three finalists:

| Pays | Instrument | Keel's call | P100 | H_plain (own-rung base + backstop) |
|---|---|---|---|---|
| 2033 | IBTM | $39,200 | $37,908 | $37,908 + $0 |
| 2034 | IBTO | $37,570 | $36,065 | $36,065 + $0 |
| 2035 | IBTP | $36,014 | $34,300 | $34,300 + $0 |
| 2036 | IBTQ | $34,529 | $32,588 | $32,588 + $331 |
| 2037 | IBTR | $33,145 | $30,922 | $30,922 + $3,991 |
| 2038 | 4.750% Feb 2037 | $31,527 | $28,930 | $28,930 + $5,458 |
| 2039 | 4.500% May 2038 | $31,087 | $28,483 | $28,483 + $5,856 |
| 2040 | 4.375% Nov 2039 | $30,096 | $27,536 | $27,536 + $6,013 |
| 2041 | 4.250% Nov 2040 | $29,346 | $42,855 | $26,550 + $7,127 |
| 2042 | 3.125% Nov 2041 | $31,937 | $48,485 | $29,021 + $7,152 |

**Recommendation.** Adopt the hybrid (H_plain) as the January 2028 completion standard: the ten exactly as the Trading
Notes describe them (each rung's reinvested coupons fund its own payment at today's forward rates), plus a backstop of
extra face in IBTR and the five T-bonds whose coupons and principal wait in a short-term Treasury ETF for the next
payment due, sized so that all ten are paid even if no coupon ever earns a cent. One-line reason: it is the cheapest
design that makes IPS l.11 true under the escrow verifier's test while keeping every quoted line of the IPS, the TNA
and the WInS notes literally. Numbers: $335,771 (+$12,335 over Keel's call); short $0 at 0%, at every fall for good, in
0 of 585 windows and in all seven NY scenarios; stated range $95,000-$115,000 (Keel's call $110,000-$130,000), kept half
$21,524 ($23,986); $33,461 back to Laura if forwards hold. If Caplet accepts that later bonds' coupons pay earlier
payments, P100 does the same job for $2,849 less ($332,922; range $100,000-$120,000). If Caplet will not pay for
certainty, keep Keel's call and write the residual into 3a with its numbers: 35 of 585 windows, one era, up to 4% of a
payment, payable only from the kept half (shares).

Before any of these replaces Keel's call: re-run NUMBERS sections 2, 4, 5, 8a, 8c, 8f and 8h on it, change the
register first, and log the call in `../../../pm/ASK_HUMANS.md` (the stated range moves, which Caplet hears in 3c).

## (d) Gaps
- The current Moody's methodology for pre-refunded and escrow-backed bonds, and any S&P or Fitch equivalent, were not
  read; the 2020 edition is marked outdated (row 31). The escrow agreements (rows 21-22) carry the standard on their own.
- Kocherlakota, Rosenbloom and Shiu (1988) was not reachable; nothing in the card rests on its content.
- No joint history of rates and stocks from a deep-recession start other than the 2006-2008 era: the kept half's
  cover in row 18 rests on one lucky alignment. The joint stress the panel asks for (weakness 4) is still to build.
- The backstop is sized on the engine's fund coupons (par yields, above IBTM's real 3.50%), which the register calls
  conservative; real bond lots ($1,000 face) and the funds' actual distributions would move the backstop by a few
  hundred dollars, enough to cross the $5,000 rounding line at $104,275 of floor.
- Whether WInS lists a short-term Treasury ETF for the waiting money is still UNVERIFIED (CANON A15); the report should
  name the type, not a ticker.
- The 2031 range rule (per-end deductions, rounding step) is still open in NUMBERS 4; at $1,000 rounding the gap
  between Keel's call and H_plain is $12,000 at the bottom ($111k against $99k), not $15,000.
- NUMBERS sections 2, 4, 5, 8a, 8c, 8f and 8h have not been re-run on any new design; this card changes no register
  figure.
