# R3 facts check (R3 Fact-Checker, Thu 5 Nov 2026, 23:45 Sydney)

Checked against `../FACTS.md` (sections 2-4), the locked TNA and trade notes, and the 4 Nov treasury.gov close.
Counts (`office/tools/textcheck.py`, strict): **pitch 55 (limit 50), IPS 576 (limit 500): both fail the gate.**

## Must fix (false, or on the never-say list)

| # | Claim (R3 words) | Verdict | Source | Fix needed |
|---|---|---|---|---|
| 1 | IPS P2: "A Treasury held to maturity repays what it promised whatever markets do" | **False as written.** Only a *bond* promises an amount. Five of the ten holdings are funds that pay their net asset value ("as opposed to a promise of par") | FACTS s4 row "pays exactly"; TNA reflection 2; IBTM/IBTO notes | "A Treasury **bond** held to maturity …". The funds can't carry the sentence. |
| 2 | IPS P6: "Each January after that, one holding is redeemed" | **False timing.** They end in Dec, Feb, May or Nov, always *before* the January | FACTS s4 "maturing in January"; WInS snapshot | "Each year one holding is redeemed before its January …" |
| 3 | IPS P3: "Laura's fortunes already ride on the economy" | **Overclaim the case doesn't support.** The case never ties her income to markets; "can" is the most we can say (the next sentence does say "can dry up", correctly) | FACTS s4 "her income rides on"; Archive C5 | Drop the clause, or "her income can rise and fall with the economy". |
| 4 | IPS P3 "the smallest facility contribution she could make"; pitch "buys her smallest facility contribution" | **False.** The smallest she *could* make is nothing. The fund also pays NAV, not a fixed sum, and a top-up shrinks it (p50 about $146k, not $150k) | FACTS N4; Archive C12; IBTM note "the final payout is not fixed" | "the least she plans to contribute" / "her minimum facility contribution" (the IBTM note's own words: "a floor … a minimum figure"; avoid "floor", I83). |
| 5 | Pitch: "Her first $300,000 buys ten Treasury holdings" (flat, no top-up) | **Not true today.** On the 4 Nov close the ten payments cost $300,608 (payment-date basis), $608 over; $303,916 on the holdings-forward basis. It holds on the WInS book's prices, not on today's curve | FACTS N1, N2; IBTR note | The IPS pairs it with the 2028 top-up, so P2-P3 pass. The pitch needs the same hedge, or "buys the ladder for her ten payments, which her 2028 deposit tops up if rates fall". |

## Check, then keep

| # | Claim | Verdict | Source / note |
|---|---|---|---|
| 6 | IPS P1: US public pensions, "whose rules let them do exactly this, have spent two decades taking on more risk" | **Plausible, but the source isn't in FACTS.** The finding is Andonov, Bauer & Cremers (2017, *Review of Financial Studies*, "Pension Fund Asset Allocation and Liability Discount Rates": GASB lets US public plans discount at expected return, and they took more risk as rates fell). Their sample is about 1990-2012, so "two decades" is fair | Add the cite to `FINAL_REPORT_BANK.md`. Leave it uncited in the IPS (Wharton: no citations). R6's `READING_BEYOND.md` should confirm. |
| 7 | IPS P4: "Companies raise dividends only to levels they expect to keep … a cut costs more trust than the rise ever earned" | **True** (Lintner 1956; Brav, Graham, Harvey & Michaely 2005 survey: managers avoid cuts and raise only when they can sustain the rise). "only" is a fair human generalisation | Final Report cite. |
| 8 | IPS P2: "R for redemption, the bond market's word for the day a bond is repaid" | **True** for the five T-bonds. The five funds are *liquidated* when their bonds mature, so "one holding is redeemed" is loose for 2033-37. Acceptable flair (Book 5) | Optional: "the day its bonds are repaid". |
| 9 | IPS P3: shares get "roughly the interest that fund will earn" | **True.** The 2032 fund costs about $114k in Jan 2028 to pay about $146k: ~$32k of interest. VT bought in Jan 2028 is modelled at p50 $30.9k. The sheet weights agree (8.7% v 24.3%) | FACTS N4, N8, s2a |
| 10 | IPS P3: VT "is the one place the plan is allowed to be wrong" | **Matches** VT reflection ("where we allow ourselves to be wrong") | TNA reflection 3 |
| 11 | IPS P3: deposit "from book advances, speaking fees and licensing, which can dry up …"; residency money from "grants, program fees and co-sponsors" | **Case-true** with "can" | case 2028 deposit; FACTS s1 |
| 12 | IPS P2: "Cash only looks safer … a bet that interest rates won't fall" | **True** (reinvestment risk on fixed dollars). Fine as the alternative refused. Don't let it imply waiting money sits in "cash": the locked notes say "a short-term Treasury ETF" | FACTS s4 "T-bills/cash" |
| 13 | IPS P5: the weakness is interest earning less "while it waits for its January"; "price the gap as if every waiting dollar earned nothing" | **True.** Also covers the Feb-2037 and May-2038 principal waiting 10.5 and 7.5 months (named in the locked notes). The rule pays in full in 100% of base paths and 98.71% in a harsh one (22 Oct curve), so never "guaranteed" | FACTS N6; Feb-2037 and May-2038 notes |
| 14 | IPS P4: bottom "rounded down, which she has owned since 2028"; "both ends are already bought" | **True under the plan.** The bottom is set on naming day after the top-up rule, so "lower range" in P5 is consistent. No range is printed (correct: Wharton says it goes in the Final Report) | FACTS N5; WHARTON_WORD s2 |
| 15 | IPS P6: "the facility contribution is paid from the 2032 fund and the shares she moved" | **True, but** the same 2032 fund also pays the 2033 operating payment (IBTM "does two jobs", TNA note 2). Not a contradiction, but P2 implies the 2033 holding is part of the $300,000 ladder while P3 makes the 2032 fund a 2028 purchase. In WInS both are IBTM | Archivist (V4) to confirm. A clause like "the same 2032 fund that pays her first January" would close it. |
| 16 | Pitch: "money leaves shares on the day someone starts counting on it" | **Fine as a principle.** Her first $300,000 and the 2028 minimum never sit in shares, so it is true only of the top half. Don't let a rewrite say her $300,000 "left" shares | Archive A32 |
| 17 | No ticker, range, confidence level, STRIPS, TIPS, CPPI, "immunise", "duration-matched", "floor", "guaranteed", "risk-free" anywhere | **Clean** | FACTS s4 |

## For the Writer
Fixes 1-4 are wording only and cost no words. Fix 5 matters for the pitch. Everything else is sourced or case-true.
