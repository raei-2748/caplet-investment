# R71 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

I re-ran `keel/scripts/ladder_pv.py` on the 23 Oct close: $297,636, which is 66.1% of $450,000 (63% at +0.5pt, 70% at -0.5pt).

| Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|
| "all owed by the US government, which issues the dollars it owes" | HALF-TRUE | pack:79-82; 02c:240 (T7) | The US government owes every bond, whether held directly or inside a fund. A fund share isn't a government debt: it pays what its bonds and cash are worth. Issuing dollars rules out running short of dollars, not a political default |
| "each kept until its redemption" | STRAINS | pack:78 ("plan of liquidation") | For the five funds, "redemption" means the fund closes in December and pays out its net assets |
| "funds of Treasuries maturing in one year" | STRAINS | pack:55 | Each fund's Treasuries all mature in one calendar year (2032-36). As written it can read as one-year bills |
| "a second debt, so it is matched the same way" | STRAINS | archive.md:95 (A27); case:114-116 | The top's money goes into Treasuries that pay out before 2033 (the date is what "same way" needs). It is a ceiling she may undershoot (P6), not a fixed debt |
| "She contributes the top, or less if the building needs less, which is why it's a range" | STRAINS | case:112-118; 02c:46-47 (VT note: "promised minimum") | The case wants a range because her 2033 value is uncertain. Here, owning both ends removes that uncertainty, so the width is what the shares fetched before naming. "Less" must never read as below the bottom she promised |
| "reserve ... empties one redemption at a time" | STRAINS | case:94-97; 02c:242 (T9) | It shrinks by one payment each January. A redemption only moves money into waiting, and two bonds pay out 10.5 and 7.5 months early |
| IPS "That day" v pitch "Before she names" | TRUE, but they differ | 02c:249 (T16) | Both should say the half is sold before she speaks |
| "Barring a US default and with both deposits ... not a payment" | TRUE (MODEL, conditional) | archive.md:101 (A33: 0 of 600,000), :84 (A16); models/README.md:35, :38 | It rests on the 2031 cover, and on no rate collapse before the build worse than any on record. At 2020's lows the ten cost $469k, more than both deposits |
| "figures she already owns, so no later fall can cost her credibility" | TRUE (conditional) | range README:41-45; archive.md:83 (A15) | It holds because the bottom sits under the fund's unfixed payout. "Owns" means the bought fund, not a fixed sum |
| "starts a little under it" | TRUE | 02c:248 (T15) | P4's draw on the stake can push the bottom further under |
| "about two thirds of her $450,000" | TRUE | re-run; 00_GROUND_TRUTH.md:86-95 | "Current" means 23 Oct, the last close on file |
| "heavily borrowed company ... far harder" | TRUE (inference) | FR_IDEAS.md:36 (1.6-2x) | It holds for any mix with more in shares than the leftover (a 60/40). "Far" means about twice |
| "balanced mix ... probably richer by 2042" | TRUE (MODEL) | models/README.md:73, :78-81 | The model ran on an older design: re-run it before the Final Report quotes anything |
| "anything else she holds ... sold any day" | TRUE | 02c:89; archive.md:87 (A19) | It can be small: kept shares are gone by 2033 in about 28 futures in 100 (A33, MODEL) |

**True as written, no change needed:** fixed in dollars, portfolio only, a debt (case:90-92). Ten holdings, five funds and five bonds (snapshot:22-31; T8). First $300,000 buys all it can, 2028 tops up (IBTR note, 02c:57-58; T3). Fixed payout traded for liquidity (refl. 2, 02c:43; C6). Facility gets the leftover (case:101-102). Extra stake in the same 2032 fund, sized to the deposit's remainder (IBTM note; commitment 5; range README:23). The stake costs less, and the difference goes to a world fund (README:23-24; T13-T14). A slump "could" shrink giving (IDEA_BANK.md:243). Reinvestment risk (T10; commitment 12; pack:81-84). The 2031 cover, dated, in Treasuries, sized at zero earnings (A19, A33). "No payment depends on how shares do", the true form (02c:268). Pitch: "buys the Treasuries that repay it", "her 2028 deposit buys the bottom" (what is left after any top-up).

No clash with C1-C12 (no rebalancing, TIPS, "to the dollar", fixed $150,000, "just before" or crossed coupons).

## What the record or the case needs that R71 lacks
1. **Where waiting money sits.** It goes in a short-term Treasury fund (Note 1, May-2038 note; commitment 11, A13).
2. **The reserve's size, in words** (case:95-96): the ten holdings plus the 2031 cover.
3. **Inflation hits the building, not the payments** (case:146-147; refl. 1).
4. **Living costs sit outside the portfolio, and nothing flows in or out before 2033** (case:61-65). That is why every holding can be held to its end.
5. **The good-market path** (case:118-119; VT note): a rise before naming lifts the top.
6. **The cost in flexibility.** What she keeps can be thin (models/README.md:78-81).
7. **A replacement rule** (A4). The fund's Board can extend or end a fund (pack:86-87).
8. **Where the 2027 leftover goes** (range README:24).
