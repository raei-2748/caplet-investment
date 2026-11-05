# R39 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

`ladder_pv.py` re-run, 23 Oct close: $297,636, headroom $2,364 (8bp). "02c" = `harvest/02c_library_models_record.md`; "arch" = `keel/rooms/archive.md`; P1-P6 = paragraphs.

| Claim | Verdict | Evidence | What a true version must convey |
|---|---|---|---|
| "every amount Laura commits to is held in Treasuries before anyone relies on it" (and pitch) | TRUE (design) | 02c:244-249; range README:41-45 | Only with the 2031 cover; five "Treasuries" are funds whose payout isn't fixed |
| "cannot count on co-sponsors" | HALF-TRUE | case L91-92 | A case rule against all outside money, not a judgment on co-sponsors |
| "her first $300,000 buys one Treasury holding for each payment" | HALF-TRUE; clashes with P3 | GT:86-95; 02c:236, 260, 91 (#10) | A one-close fit (8bp): all ten only if prices allow; P1 and P3 must tell one story |
| "redeemed in the year before it falls due" | TRUE | snapshot:22-31; 02c:242 (T9) | Right as is; never "just before" |
| "their interest makes up the rest of the $500,000" | HALF-TRUE | 02c:62-63, 75-77, 243 | Interest, below-face bonds rising to face, and what waiting interest earns (uncertain until the 2031 cover) |
| "A balanced mix ... would probably leave her richer by 2042" | TRUE (MODEL) | `keel/models/README.md:73, 78-80` (60/40 leaves $229k-$285k v $31k-$56k) | Says it is our modelled result |
| Gearing: payments "take most of her money"; slice "would swing harder than the share market" | TRUE (CALC) | payments ~$298k of ~$444k (2027 money); a 60/40 slice swings ~1.8x shares | "Thin" = about a third, at about triple weight |
| "Matching ... removes that gearing" | HALF-TRUE | 02c:93, 239; arch:84, :102 | Removes it for prices; waiting money (and a yield fall before January 2027) still lands on the facility |
| "no payment rests on a share price or on selling a bond before it matures" | TRUE, with P5 | arch:101 (A33: 0 of 600,000 worse off; 0.94% if the 2028 deposit halves) | Keep the cover beside it; assumes the 2028 deposit arrives |
| 2028: "first buys any holding the first $300,000 couldn't afford" | TRUE; strains with P1 | 02c:56-58, 65-67 (IBTR, IBTO "top up") | A conditional top-up of whatever is missing |
| Extra holding's payout "rounded down ... is the bottom" | HALF-TRUE | 02c:248 (T15); arch:73 (A5 "less any gap") | Unless the shares can't cover the waiting-money gap (P5's own rule) |
| "if every share were lost, the extra holding alone would repay about what she put into both" | STRAINS | arch:101 (shares wiped: cover from the floor, median $12,688-$21,627, MODEL) | True of the payout; the nameable bottom falls by the cover |
| "A top left in shares could prove out of reach, while a rise above it would only add to what she keeps" | STRAINS | range README:59-63 | First half true (top reached ~3 in 4); the move gives up that half's 2031-33 rise, which would have been hers |
| "Money that arrives before its payment, mostly interest, earns short-term rates" | STRAINS | CALC, five WInS bonds (snapshot:27-31): principal ~65% of early dollars, interest ~90% of dollar-years; 02c:26-28, 59-61, 92 | Interest waits longest; two bonds' principal waits 10.5 and 7.5 months; the home is a short-term Treasury fund |
| "the other half ... first buys enough Treasuries ... as if the waiting money earned nothing" | HALF-TRUE (undated) | 02c:89; arch:87 (A19); V57 `FINAL/ips.txt:13` dated it | In 2031, before she names the range; never after 2033 |
| "the range comes down, top first, so no payment ever waits on shares" | TRUE for payments | arch:87, :101 (tested order: off the bottom) | Payments unaffected (every pocket is Treasuries); range figures need a re-run on top-first |
| "Barring a US default, her contribution will land in the range" | HALF-TRUE | casestudy:79, 86-87 (no predetermined amount; Board may extend or terminate); arch:79 (A11) | Both ends owned before naming; a US default or a fund paying below its rounded-down estimate could break it |
| "the tenth redemption pays the last in 2042" | HALF-TRUE | 02c:75-77 (Nov-2041 note); CALC: face + last coupon ≈ 61% of the payment | Redeemed 15 Nov 2041; with the interest saved for it, it pays January 2042 |
| Pitch: "Her first $300,000 buys Treasuries for her ten ... payments" | HALF-TRUE | 02c:237 (T4); arch:79 | Saved only by the next sentence's "if needed" |
| Pitch: "puts only its interest into shares" | STRAINS | 02c:246 (T13) | "Its" reads as the deposit's interest: shares get a sum about equal to what the bottom's Treasuries will earn by 2032 |
| Also TRUE: "near-ironclad"; "thoughtful risks all her career"; "spoken for"; "extra holding in the fund behind the 2033 payment"; "about the interest it will earn by 2032"; P4; inflation clause; flexibility sentence; reserve sentence; pitch top-up and bottom | TRUE | 02c:30-31, 84, 86, 235-236, 244, 246, 251; arch:70, 95-98; case L59-60, L69-71, L94-103 | Flexibility may be empty in about a quarter of futures (MODEL); the case says "could" |

## What the locked record needs that R39 lacks
- The cover's date, "before she names the range" (A19; commitment #8).
- The waiting place named as a short-term Treasury fund, with the early principal (Note 1; #11; arch:81).
- Five payments sit in funds paying NAV, for liquidity (refl. 2; `what_october_allows.md:37`). P3 covers one.
- Payments are nominal, so inflation cannot raise them (refl. 1; #6).
- Holdings replaced only if unavailable (#2; arch:72).
- The favourable path: a rise before 2031 lifts the top (VT note; case L118-119). Implied only.
- Case asks open: how certainty was evaluated (L97-99); assumptions (L146-148); living costs outside the portfolio (L61-65); "meaningful" (L110-112); the $150,000 (L43-45).
