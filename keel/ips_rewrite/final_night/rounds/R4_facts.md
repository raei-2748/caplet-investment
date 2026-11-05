# R4 facts check (R3 Fact-Checker, Thu 5 Nov 2026, 23:55 Sydney)

Counts (strict `textcheck.py`): **pitch 50 / 50, IPS 497 / 500: pass.**
Fixed since R3: the $300,000 ladder now carries the 2028 top-up ("if rates leave it short, her 2028 deposit finishes
it"). The pitch no longer says her first $300,000 buys every payment.

## Still must fix (carried from R3_facts.md, all wording-only, all still in R4)

| # | R4 words | Why it's wrong | Fix |
|---|---|---|---|
| 1 | P2: "A Treasury held to maturity repays what it promised whatever markets do" | Five of the ten holdings are funds, which pay net asset value, not a promised sum (TNA reflection 2: "as opposed to a promise of par") | "A Treasury **bond** held to maturity …" (+1 word) |
| 2 | P6: "each January one holding is redeemed" | They redeem in Dec, Feb, May or Nov, before the January | "each year one holding is redeemed before its January" (+2) or "each year one holding is redeemed" (0) |
| 3 | P3: "Laura's fortunes already ride on the economy" | The case never ties her income to markets. The next sentence's "can dry up" is the supportable version | "because Laura's income can already rise and fall with the economy" or drop the clause |
| 4 | P3: "sets the smallest facility contribution she could make"; pitch: "buys her smallest facility contribution" | The smallest she could make is nothing. The fund's payout isn't fixed (IBTM note; MODEL p50 about $146k) | "sets her minimum facility contribution" (IBTM note: "a minimum figure"). Pitch: "buys her minimum facility contribution" (0 words) |

## New in R4: checked

| # | Claim | Verdict | Note |
|---|---|---|---|
| 5 | P6: "by 2033, nothing a resident or a co-sponsor is relying on depends on a share price" | **True by design.** Payments sit in Treasuries; both ends of the range are in Treasuries before naming; the kept half of her shares is "promised to no one". This sentence is the plan's truest strong claim | Keep. Don't upgrade it to "guaranteed": funds pay NAV, and the harsh-world lock is 98.71% (FACTS N6) |
| 6 | P1: "American public pensions, whose accounting rules let them do exactly that, have spent two decades taking on more risk" | **Plausible and sourced off-page:** GASB 67/68 lets US public plans discount funded liabilities at expected return. Andonov, Bauer & Cremers (2017, *RFS*) find they took more risk as rates fell (sample about 1990-2012) | Final Report cite. "accounting rules" is right |
| 7 | P2: "A patient investor can wait out a bad decade. A January cannot." | Rhetoric, not a factual claim. Fine | — |
| 8 | P1: "the price of Treasuries that will pay it on its date" | Loose: they pay *before* its date (up to 10.5 months early for 2038) | Optional: "by its date" |
| 9 | P4: "Its top adds half of what her shares are then worth … moves into Treasuries before she names" | Matches the FINAL design and the VT note ("a rise before 2031 lifts the top") | — |
| 10 | P5: the weakness: waiting interest "earns less than we planned"; "as if every waiting dollar earned nothing" | True (also covers the Feb-2037/May-2038 principal waiting). Consistent with the locked notes | — |
| 11 | Pitch: "Treasuries maturing before each January pay her ten $50,000 operating payments" | True, and no longer tied to the first $300,000 alone | — |
| 12 | Two-jobs point (R3 #15) | Unchanged: P2's ladder includes the 2033 holding, and P3's 2028 deposit buys "a Treasury fund maturing in late 2032". In WInS both are IBTM. Not false, but Archivist (V4) should rule | — |
| 13 | Never-say sweep | Clean: no ticker, printed range, STRIPS, TIPS, CPPI, immunise, duration-matched, floor, guaranteed, risk-free | — |

**Gate verdict (facts):** R4 passes once fixes 1-4 are in. They cost +3 words at most, which still fits (≤500).
