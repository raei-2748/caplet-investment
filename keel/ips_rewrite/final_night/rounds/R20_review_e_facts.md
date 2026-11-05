# R20 review (e): facts and the locked record

AI-generated (Claude, 5 Nov). GT = `00_GROUND_TRUTH.md`; 02c = `harvest/02c_library_models_record.md`;
OA = `rooms/archive_checks/2026-11-05_what_october_allows.md`; AR = `rooms/archive.md`; CS =
`library/assistant_review_2026-10/oct20/casestudy/casestudy_pack.md`. `ladder_pv.py` on the 23 Oct CSV: $297,636, headroom $2,364 (8bp), as GT:93-94.

| # | Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|---|
| 1 | All ten mature "in the year before the January it pays for"; pitch "before each January" | TRUE | snapshot:22-31; OA:69 | Never "just before" (02c:272) |
| 2 | "named for those ten redemptions" | HALF-TRUE | Five funds "terminate ... distribute remaining net assets" (CS:78); refl. 2 "net asset value, as opposed to a promise of par" (GT:68-69) | Five bonds redeem at face; five funds wind up and pay what they hold |
| 3 | 60/40 makes the leftover "swing harder than the share market"; "as a company ... borrows" | TRUE | 1 Jan 2028: payments $311.3k, deposits $463.8k, leftover $152.5k; 60% shares = $278k = 1.83x leftover; shares -30% → leftover -55%, before rate mismatch. True whenever payments exceed 40% of the money (here 67%). Analogy = Modigliani-Miller II | Fine |
| 4 | "near-ironclad: no payment depends on a share price, a forecast or a sale before maturity" | HALF-TRUE | Refl. 1's word (GT:63-64). Until 2031 the gap's cover is unbought, then comes from shares with no back-up; kept shares fell short in ~27 of 100 modelled futures (AR:101; 02c:244-245) | From naming day nothing rides on shares or forecasts; before it, the gap has a source and a back-up |
| 5 | "one borrower ... a second would only add a second way to miss" | HALF-TRUE | Credit all US (CS:3). Five payments also rest on a fund's value and board (CS:86; OA:57). "only": another borrower also pays more | One credit by choice; extra yield is the price of a second risk |
| 6 | 2028 deposit "buys any holding the first $300,000 couldn't afford, if bond prices rose" | HALF-TRUE | IBTR note "top up the ladder" (GT:75-76); 22 Oct holdings bases already over $300k (02c:236) | It tops up whatever part of the ten fell short |
| 7 | IBTM "behind the first payment, whose Treasuries all mature in late 2032" | FALSE (second half) | First half true (snapshot:22). Notes mature 31 Jan-30 Nov 2032, ~53% by 30 Jun; cash by ~15 Dec (CS:21, :82, :114); same slip ruled FALSE for IBTR (`oct21_tna/factcheck.md:108`) | A fund of 2032 Treasuries paying out around mid-December 2032 |
| 8 | "rounded down because a fund's payout isn't fixed"; "about that fund's interest"; pitch's "small slice" | TRUE | IBTM note (GT:66-67); 02c:246, :248 | Fine |
| 9 | Waiting to 2031 leaves the bottom "at the mercy of shares in the same years that co-sponsors give less" | HALF-TRUE, not in case | Case links markets only to "the amount she can provide" (:118-119); "can" is the limit (C5, OA:36, :68). True only if waiting money sits in shares | Hedge it, or use credibility (:114-115) |
| 10 | 2031: half to Treasuries = top; cover "from the other half" | STRAINS | Not C2 (OA:33; allowed form 02c:89). But the cover isn't dated, and the top is fixed before the cover is funded, so a short other half fails "must also protect" (case :119-120). The VT note's "only" and refl. 3 (GT:70-72) need a back-up | Cover first, before naming; what kept shares can't cover comes out of the range before naming (A31, AR:99) |
| 11 | "afterwards shares move neither end" | TRUE | Both ends owned (02c:249) | With item 10's back-up, a bad market plus low rates can lower the bottom too, pre-naming |
| 12 | "Barring a US default, her contribution will land in the range" | HALF-TRUE | Also: a fund paying under the rounding (OA:41, :43; CS:185); its board moving the end date (CS:86); her 2033 choice | Both ends owned before naming; else only a fund paying well under expectation |
| 13 | "sellable on any trading day ... the only part that can grow with building costs in Taiwan" | HALF-TRUE | Funds are daily-liquid too (GT:69); "a building cushion, not inflation insurance" (02c:251); US v Taiwan dollars | Can grow; no promise it keeps pace |
| 14 | Reserve = "the ten holdings and the money set aside" | HALF-TRUE | By 1 Jan 2033 IBTM has wound up; saved interest sits in the short-term fund (GT:61-62) | Everything waiting for a payment |
| 15 | "each January's $50,000 comes from the holding redeemed before it"; Nov-2041 "pays the last" | HALF-TRUE (dates TRUE) | Coupons "fund the rest" / "part of each" (02c:62-64, :75-77). Nov-2041 face pays ~59%, its coupons ~$20k (MODEL) | "rests on" (02c:300): holding plus its saved interest, plus set-aside if rates fell |
| 16 | Weak point: "the interest its holdings pay" | HALF-TRUE | Note 1's "proceeds": Feb-37 / May-38 principal waits 10.5 / 7.5 months (GT:61-62); funds' final-year cash (CS:83); AR:101 | Every waiting dollar, principal included |
| 17 | "buys every amount ... before she commits"; "only money nobody has been promised goes into shares" | HALF-TRUE | Gap's cover bought in 2031 from shares; shares "fund the lock" (AR:101) | Shares are the gap's first call |
| P | "because co-sponsors can't fund them" | HALF-TRUE | Case :85-86 allows "operating support beyond Laura's commitment"; :91-92 "may not rely on" | She can't count on them |

## Missing from R20 that the locked record needs
1. **A back-up for the 2031 cover** (item 10): without it item 4 fails in about a quarter of modelled futures. The main fix.
2. **Every waiting dollar**, the principal Note 1 names (item 16).
3. **Saved interest in the reserve** (item 14).
4. **Payment funds pay value, not par** (refl. 2; 02c:85). R20 says it only of the bottom.
5. Watch A32 (AR:100): the frozen book holds VT and extra IBTM bought from $300,000; Keel's call is the Final Report.
