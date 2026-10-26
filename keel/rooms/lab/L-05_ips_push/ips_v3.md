# IPS v3: pitch + IPS (Writing Room: Tess cuts, Amara drafts)

**AI DRAFT (Claude, 24 Oct 2026).** A suggestion only. Keel is a simulated team, and nothing here touches the IPS Report doc. Caplet rewrites every line in its own words and logs the AI use for the Works Cited.
Base text: "Full text" in `/mnt/project-files/ips/IPS_edits_v2_2026-10-24.md` (pitch 47, IPS 494). Applied: Courtroom C1, C2 and C3 with their exact amended words; the name and all roots/branch/secure wording taken out (team leader's decision), with [NAME] standing in until the vote on Mon 26 Oct; the Writing Room's hard fixes (K4 dates, "bond" -> "holding"). No new facts or numbers.

## (a) Full text

**Pitch (45 strict)**

Laura's co-sponsors may fund the building without paying to run it, so [NAME] pays for the running first. Treasuries held to maturity cover ten $50,000 payments, and more Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift.

**IPS (471 strict)**

This policy governs Laura Gao's $450,000 for the Taiwan creative residency she opens in 2033. Its first objective is to fund ten $50,000 operating payments, each January from 2033 through 2042, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. Each payment's cash comes from a maturity, not a sale. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a facility contribution with a floor Laura can quote to co-sponsors and growth above it.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

[NAME] buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that sum is Laura's facility floor. The rest buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range from the floor, quoted at the 2032 ETF's projected payout rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top, so she never gives more than she quoted.

Moving floor money into stocks would raise the expected gift. This is the obvious trade. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hurts twice: the payment Treasuries cost more in January, and their coupons earn less afterwards. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Coupons are reinvested in the holding that paid them; early maturities wait in a short-term Treasury ETF. Each January we review the plan with Laura, replacing any holding that becomes unavailable with a Treasury maturing earlier. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42. Our WInS portfolio shows this allocation, scaled down.

**After the Writing Room (Nora, 24 Oct evening):** two lines rewritten the way the Room's own section (e) said a
person would say them: C1 split into three short sentences, and K2 now says what falls on whom ("A lasting fall in
yields hurts twice: ..."). Recount with `textcheck.py`: **pitch 45, IPS 471 strict** (467 by spaces), 0 overclaim
words, 2 en dashes. The table below describes the Room's version (469).

## (b) Change table
Paragraph totals are exact (`textcheck.py` strict count, per paragraph). Per-change figures are approximate where one change moves text between paragraphs.

| Para | Old -> new | Why | Words |
|---|---|---|---|
| Pitch | "so Root & Branch funds the running costs first. Its roots, matched Treasuries, cover ... Its branch, a global index fund, grows her gift" -> "so [NAME] pays for the running first. Treasuries held to maturity cover ... Above that minimum, a global index fund grows her gift." | Name and roots/branch out. "Held to maturity" sets up the IPS's maturity-not-sale line | 47 -> 45 |
| P1 | "..., so each payment depends mainly on the US government paying its debts." -> **C1 exact**: "By high certainty we mean each payment is owned in Treasuries by 2028, needing no stock return; only coupon reinvestment and ETF payouts can leave it short." | Courtroom C1 (amended). Answers the official ask to "define high certainty" | +14 |
| P1 | "Each payment's cash comes from a maturity, not a sale." moved up from P6, straight after the matching sentence | Keeps the outsider judge's one clear line and puts it where it explains the matching. It is a short sentence after a long one | +10 (from P6) |
| P1 | "a floor Laura can promise co-sponsors" -> "a floor Laura can quote to co-sponsors" | Optional item flagged in v2. Takes "promise" out of the plan's own words (the case says a range "rather than promising"), and "quote" matches P4. Revert if vote set A keeps "promise" | +1 |
| P1 | total | | 85 -> 111 (+26) |
| P2 | Cut "Because her 2028 deposit depends on publishing and speaking income, the 2027 deposit goes entirely to the payments." (moved to P3 and merged); "low, since the artists" -> "low – the artists" | Repeated idea: P3 already said the 2027 deposit funds the payments. The client fact (income source) survives in P3 | 55 -> 36 (-19) |
| P3 | "Root & Branch secures the roots (the payments and a facility floor) before investing in the branch." -> "[NAME] buys every payment before a single share." | Name and roots/secure out; "secures" was also an overclaim word. A short punch opens the paragraph | -8 |
| P3 | P2's income sentence + "The 2027 deposit funds the latest payments first, since their cost moves most with interest rates." -> "Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first." | Two sentences said "2027 money goes to the payments". One now carries the client reason and the order. The rate-sensitivity reason goes (Amara's cut C5: a judge already believes it) | about -15 across P2/P3 |
| P3 | "Any gap left in January is the first use of the 2028 deposit." + **C2 exact**: ", so a rate fall before we buy lowers the floor, not a payment." | Courtroom C2 (amended) | +13 |
| P3 | "The rest forms the branch, a global index fund of thousands of companies. The roots rely on one issuer by design, since no dollar asset is safer." -> "The rest buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer." | Branch/roots out. **One-issuer and diversification kept** (required): one issuer for the payments, thousands of companies for the growth | -5 |
| P3 | total | | 97 -> 103 (+6) |
| P4 | Cut "A range built to hold protects her credibility better than a narrower one she might miss." | Repeated idea: credibility was said three times (this line, "never gives more than she quoted", and P5's refusal). The refusal in P5 keeps it as a decision | -16 |
| P4 | "In 2033 she contributes the floor plus half the fund's value, capped at that top" -> "In 2033 the same rule sets her contribution, capped at that top" | The formula was spelled out twice in two sentences | -3 |
| P4 | total | | 68 -> 49 (-19) |
| P5 | "Moving floor money into stocks would raise the expected gift; we refuse, because it could break a number Laura has quoted." -> "Moving floor money into stocks would raise the expected gift. This is the obvious trade. But it could break a number Laura has quoted, so we refuse." | Voice pass: the concessive turn, then a three-word close. Same claim, no softening | +6 |
| P5 | K5 moved here from P6, placed straight after K2: "Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor." | K2 names the second hit and K5 handles it. Next to each other they read as cause and rule, and the old P5 line on what "the half Laura keeps backs" no longer repeats it | +31 (from P6) |
| P5 | "Inflation or a stronger Taiwan dollar raises costs in Taiwan. The half Laura keeps backs the payments first, then cost overruns, then her own plans." -> "Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans." | The "payments first" step is now K5. Same order of use, one idea fewer | -5 |
| P5 | total | | 66 -> 100 (+34) |
| P6 | Cut "Until 2033 the portfolio is held without trading beyond investing the 2028 deposit." | The idea is already carried by maturity-not-sale and the annual review. It also sat badly with "replacing any holding" one sentence later | -13 |
| P6 | "Coupons are reinvested in the bond that paid them" -> "... in the holding that paid them" | Hard fix: half the ladder is ETFs | 0 |
| P6 | K4 + **C3 exact**: "In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42." | Courtroom C3 (+4). Hard fix for the dates: the payment years, because IBTM closes in Dec 2032 (-3) | +1 |
| P6 | Maturity line and K5 moved out (see P1, P5) | | -41 |
| P6 | total | | 123 -> 70 (-53) |
| **IPS** | | | **494 -> 469 (-25)** |

Kept as required: the one-issuer choice, diversification, where early cash waits, the annual review, the WInS mirror, the reserve's make-up, inflation/FX, and "Each payment's cash comes from a maturity, not a sale."

## (c) textcheck.py counts (`python3 keel/office/tools/textcheck.py <file> --limit N`)
| Text | By spaces | Strict | Characters | Limit | Result | Non-ASCII | Overclaim |
|---|---|---|---|---|---|---|---|
| Pitch | 44 | **45** | 275 | 50 (aim 45-48) | PASS, margin 5 | 0 | 0 |
| IPS | 465 | **469** | 2,693 | 500 (target 470) | PASS, margin 31 (1 under target) | 2 (both en dashes, deliberate: P2, P3) | 0 |

Notes on the counts:
- [NAME] counts as one word. A two-word name adds 1 to the pitch and 1 to the IPS; a three-word name adds 2 to each.
- The two en dashes are the only non-ASCII characters. If Caplet wants plain ASCII for the form, use a colon in P2 and P3 instead (no change to the strict count).
- A scan for root, branch, secur*, em dash, "?", Furthermore and Moreover finds nothing.
- If Caplet takes option A (the inflation-rate sentence) on Tuesday, it now fits under 500 with no further cut.

## (d) Voice notes (how Ray's essay voice differs from typical AI prose; described, not quoted)
1. **Long sentence, then a very short one.** A broad, multi-clause sentence is followed by two or three blunt, short ones that each make one point. AI prose keeps every sentence at about the same middling length. *Applied:* "[NAME] buys every payment before a single share.", "This is the obvious trade.", "so we refuse."
2. **Concede first, then turn on "But".** He grants the other side's comfort or appeal in a sentence that starts with a demonstrative, then opens the next sentence (or paragraph) with "But". AI hedges both sides at once. *Applied:* P5, on moving floor money into stocks.
3. **Beats the objection with a distinction, not a pile of evidence.** He separates two things the objection runs together. *Applied, lightly:* the paragraph leans on C2's floor-versus-payment split and C3's renamed-versus-rebuilt. Both are the Courtroom's words, kept as written.
4. **Spaced en dashes carry the asides.** They hold the qualifications in the middle of a sentence, never em dashes. *Applied:* two of them (P2, P3), each one turning the sentence.
5. **One plain definition before the argument.** He says in a sentence what a term will mean and then uses it without fuss. *Applied:* C1 sits at the front of the IPS.
6. **Hedges are rare and single.** He commits to a verdict, and when he qualifies he uses one word, once. *Applied:* no hedges added and no confident claim softened. "No dollar asset is safer" and "never gives more than she quoted" stay flat.
7. **Wit sits in headings and the odd dry phrase, not in the body.** He uses puns on familiar sayings for section titles, and the body stays straight. *Partly applied:* "the obvious trade" is the one dry double meaning. A form IPS has no headings, so the pun habit is left for the Final Report (and perhaps the name).
8. **British spelling and a slightly formal register** without stiffness. *Applied by default:* the text contains no US-only spellings. It never tries for the formal register, because Ahaan's plainer base wins there.

## (e) Two lines that still sound like AI
1. "By high certainty we mean each payment is owned in Treasuries by 2028, needing no stock return; only coupon reinvestment and ETF payouts can leave it short." This reads like a machine because a trailing participle ("needing ...") and a semicolon pack a definition and its exception into one balanced unit. Students split that into two sentences. It is the Courtroom's exact wording, so it was left alone. A human version: "By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short."
2. "One yield sets both the ladder's January price and what its coupons earn later, so a lasting fall works twice." The neat "both X and Y ... works twice" symmetry is the kind of compressed aphorism models produce. "Works twice" is also abstract, because it never says what falls on whom. The ladder is also unnamed until this point (inherited from v2). It is the plan's one real insight, so it stays. Caplet should say it the way they would explain it to each other out loud.
