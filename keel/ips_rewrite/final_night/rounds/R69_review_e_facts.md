# R69 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

Keys: REC = `harvest/02c_library_models_record.md`; ARC = `keel/rooms/archive.md`; CSP = `casestudy_pack.md`; CASE = client profile; WN = `wins_notes.csv`; COMP = `COMPETITION.md`.

| Claim | Verdict | Evidence | True version must convey |
|---|---|---|---|
| "keeps every sum ... in Treasuries before anyone counts on it" | TRUE (design) | Payments bought 2027-28 (COMP:177-185); range and set-aside before naming (ARC:101) | |
| "fixed in dollars ... only from her portfolio"; "ten Treasury holdings ... kept until its redemption" | TRUE | CASE:88-92; snapshot:22-31; ARC:43, :79 | |
| "first $300,000 buys all it can, and the 2028 deposit buys the rest" | HALF-TRUE | `ladder_pv.py`, 23 Oct: $2,364 spare (REC:236); IBTR note: "is enough" (REC:56-58); REC:91 | The 2028 deposit buys whatever the first couldn't, if anything |
| "Five are funds ... since no Treasury she may buy matures in those years" | FALSE (2036) | None listed "between 15 Feb 2031 and 15 Feb 2036" (WN:18): the 15-Feb-2036 bond is listed (CSP:3), in IBTR's year. Reflection 2: "Some years" (ARC:43) | No listed Treasury matures in four of those years; in 2036 only a February bond, ~10.5 months early |
| "balanced mix ... richer by 2042"; "about two thirds of her $450,000"; "heavily borrowed company ... swing far harder" | TRUE | 60/40 leaves $229k-285k v ours $31k-56k (MODEL, `keel/models/README.md:73`); 66.1% (`00_GROUND_TRUTH.md:87`); own CALC: ~$152k left bears a 60/40's swings, ~32%/yr v 16.8% for shares | |
| "extra stake in the fund behind the 2033 payment ... payout isn't fixed ... starts a little under it" | TRUE | IBTM note (REC:36-38); REC:86, :248; ARC:73, :98 | |
| "costs less than it pays out ... still get that sum back" | TRUE, loosely | REC:246; VT 10,048 stocks (CSP:322) | Back roughly, less anything the 2031 set-aside takes from the stake |
| "keeps the bottom clear of any share slump that could also shrink co-sponsors' giving and her earnings" | STRAINS | Para 4: the stake pays what the shares can't, so a slump can lower it; A31 (ARC:99); lowered in 27 futures in 100 (MODEL, ARC:101) | The stake holds no shares; a slump can still lower the bottom via the set-aside |
| "Its interest and early repayment wait in a short-term Treasury fund" | HALF-TRUE | True of the bonds (REC:27-28, :59-61). Each fund's final-year cash waits inside it (CSP:81, :114). A lock on interest alone paid every cheque in 97.02% / 82.18% of futures (base / yields 2pt lower) (MODEL, ARC:101; `inbox/2026-11-04_library.md:19-25`) | Zero earnings on every dollar waiting for a payment, the funds' own cash included |
| "priced as if that money earns today's rates" | HALF-TRUE | Curve pricing implies forwards ~5.0-5.9% (CALC) v 4.11-4.22% for 1-3 month bills (`daily-treasury-rates_2026-10-23.csv:2`) | Today's long-bond yields, above what a short fund pays now |
| "rates can fall to nothing for years"; "assumes it earns nothing ... sells up to half ... stake pays the rest"; "other half sets the top ... A rise ... lifts the top" | TRUE (design) | 0-0.25% 2008-15 and 2020 (`04a_LECTURES_damodaran_shiller.md:162`); dated, into Treasuries (REC:89; ARC:87); VT note (REC:45-47); ARC:86, :95 | |
| "Barring a US default and with both deposits made, falling markets and rates land on the range, not the payments" | HALF-TRUE | 0 of 200,000 worse off only if the set-aside counts the funds' cash (ARC:101); deposit halved 98.71% (ARC:88) | Holds only with all waiting cash in the set-aside |
| "She contributes the top, or less if the building ... needs less, which buildings seldom do" | STRAINS | Funds pay NAV (ARC:43); 80%+ of US arts buildings overran (`04b_WIDE_RESEARCH.md:215-217`); facility cost undetermined (CASE:164-167) | Top at or under its Treasuries' payout; buildings usually overrun; no implied budget |
| "everything beyond her contribution stays out of every promise and can be sold any day" | STRAINS | The reserve is beyond it, and promised; kept shares gone by 2033 in ~28 futures in 100 (MODEL, ARC:101) | Beyond the reserve and contribution; may be nothing |
| "operating reserve ... only on paper"; "final redemption meets the final payment in 2042" | TRUE | COMP:177-178, :189; REC:75-77; CASE:92-93 | Last redemption 15 Nov 2041 |
| Pitch: "owns every figure she commits to before she says it aloud" | STRAINS | Five pay NAV, not par (REC:39-43, :65-71, :85) | Holdings bought to pay each figure before she names it |
| Pitch: "Ten Treasury holdings repay ..."; "both its ends are in Treasuries ... her 2028 deposit and half its shares" | TRUE (design) | ARC:79; `keel/pm/REQUESTS.md:69`; COMP:183-186 | |

## What the locked record needs that R69 lacks
1. The funds' "not fixed" payout for 2034-37 (IBTO, IBTP, IBTQ notes; reflection 2): said only of the 2033 stake (ARC:82).
2. The set-aside counting the funds' own cash (A33's 4 Nov repair, ARC:101): reopened.
3. The set-aside's price (A33 rule 3): her kept shares can be used up, not only the range lowered.
4. "If needed" on the 2028 top-up (REC:91).
5. Reflection 2's trade, a fixed payout for liquidity (`what_october_allows.md:37`): the true reason for funds; mends the 2036 error.

Case asks still open: how certainty was evaluated (CASE:97-99); inflation on facility costs (CASE:146-148).
