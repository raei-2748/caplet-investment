# R5 facts check (R3 Fact-Checker, Fri 6 Nov 2026, Sydney)

Counts (strict `textcheck.py`): **pitch 50 / 50, IPS 499 / 500: pass** (no room to add a word without a cut).
Fixed since R4: "minimum facility contribution" (pitch and P3); "can rise and fall with the economy"; "one holding is
redeemed before each January"; the 2032 fund's two jobs ("more of the late-2032 fund that pays her first January",
which matches the IBTM note).

## Must fix

| # | R5 words | Verdict | Fix |
|---|---|---|---|
| 1 | P1: "American public pensions … have spent two decades taking on more risk to keep up with it" | **The span is UNVERIFIED; the mechanism is verified.** The Andonov, Bauer & Cremers abstract (*RFS* 30(8), 2017, 2555-2595, read on ideas.repec.org tonight) says US public funds' discount-rate rule "gives them incentives to invest more in risky assets" and that they "act on their regulatory incentives", but it gives no span of years. This agrees with R6 Library's flag | Drop the span: "… whose accounting rules let them do exactly that, take on more risk to keep up with it." (−3 words, which also buys room) |

## Should fix (small overclaim)

| # | R5 words | Verdict | Fix |
|---|---|---|---|
| 2 | Pitch and P1: "she buys the Treasuries that pay it **that day** / that same day", listing "her ten … operating payments in 2027" | **Not always true for 2027.** P2 admits the 2028 deposit may finish the ladder, and on the 4 Nov close it would ($300,608 v $300,000, FACTS N1). So the 2027 commitment isn't always fully bought that day | Pitch: "as soon as the money arrives" in place of "that day", or keep "that day" and accept the small gap (P2 discloses it). IPS P1 the same. The Writer's call; flagged, not a stop |

## Checked, pass

| # | Claim | Verdict |
|---|---|---|
| 3 | P2: "Each holding pays out at its end date whatever markets do" | **Pass.** It claims timing, not a fixed amount, so the funds' NAV payout isn't contradicted. Don't turn it into "pays exactly" |
| 4 | P2/P6: "R for redemption, the day a bond is repaid"; "one holding is redeemed before each January" | **Pass with a note.** The bonds inside the funds are redeemed; the funds themselves *terminate* about 15 Dec and pay out their net assets (R6 Library, S18). The first sentence is exact. The second is loose for 2033-37 but true for 2038-42, which is acceptable flair (Book 5). If a word is spare: "one holding pays out before each January" |
| 5 | P1: "her shares only ever hold money nobody else is counting on" | True by design (the kept half is "promised to no one"; VT reflection: "not standing between Laura and a payment deadline") |
| 6 | P3: shares get "roughly the interest it will earn" | True (about $32k of interest vs VT p50 $30.9k, FACTS N4/N8) |
| 7 | P3: "Laura's own income can rise and fall with the economy"; the deposit "can dry up" | Case-true with "can" |
| 8 | P4: bottom = "that extra in the 2032 fund, rounded down"; top = half her shares moved before naming | Matches the FINAL design and the IBTM/VT notes |
| 9 | P5: the weakness; "as if every waiting dollar earned nothing"; "she names a lower range" | True and consistent with the locked notes |
| 10 | P6: "by 2033 nothing a resident or a co-sponsor is relying on depends on a share price" | True by design; never "guaranteed" |
| 11 | P1: "the price of Treasuries that will pay it on its date" | Loose (they pay *by* its date); optional "by" |
| 12 | Never-say sweep | Clean: no ticker, printed range, STRIPS, TIPS, CPPI, immunise, duration-matched, floor, guaranteed, risk-free |

**For the Final Report bank:** the same abstract also says "The increased risk-taking by U.S. public funds is
negatively related to their performance." The higher assumed return bought more risk and worse results, which is the
evidence behind P1's rule.

**Gate verdict (facts):** pass once fix 1 is in (it saves words). Fix 2 is the Writer's call.
