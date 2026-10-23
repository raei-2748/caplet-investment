# IPS edit ledger: every fix-before-6-Nov item in one place, with a word budget

Completeness critic (WS7), 30 Sep 2026 (Sydney). AI-generated (Claude Code) for Team Caplet. **The team writes the
IPS**; this ledger lists what each edit must achieve, not the words. Written because Gate D (`rab/redteam/triage.md`
D6) found the edits spread over nine files and about 40-50 words of changes against 17 spare. Nothing here edits the
IPS Google Doc. Basis: the read-only snapshot of 30 Sep (`rab/trades/data/ips_doc_text_2026-09-30.txt`, headed
"EXEMPLAR ONLY"): pitch 49 of 50 words, body 483 of 500 by whitespace count (W3 `ws3.ips.word_count_30sep`; Google
Docs may count differently: recount in the Doc). Word changes are estimates from each source memo.

## Edits (ranked: the case's primary requirement first)

| # | IPS sentence (30 Sep) | What the edit must achieve | Words | Source | Decide by |
|---|---|---|---|---|---|
| L1 | "By high certainty we mean that each payment is matched by a dated Treasury ETF or bond maturing just before it, so that once bought it depends essentially on the US government." (32) | Treasuries maturing *before* each payment, held to maturity; the government owes most of each payment, the rest depends on reinvesting coupons | 0 (swap) | `D_certainty_definition.md`; notes.md s7; triage D5 | 20 Oct |
| L2 | "This cash-flow matching, unlike immunization, needs no rebalancing." (8) | Replace with the coupon policy: once a year, each holding's income buys Treasuries for the same payment (stress rules 1-2) | about +8 net of the 8 removed: 0 to +8 | `D_stress_bad_year.md`; Gate A carried forward; assumptions C3 | 26 Oct |
| L3 | "The other half remains with Laura as a cushion if costs rise or co-sponsors fall short." (16) | Name the order of use: a payment shortfall first (coupons earn less), then costs or co-sponsor gaps. Never "her own money" | +3 | `D6_cap_share.md`, `D_stress_bad_year.md` rule 3; triage D1-D2 | 26 Oct (with D6) |
| L4 | none (new clause) | Costs: who pays them (the stock fund, not the floor) | about +10 | `D_ips_three_assumptions.md` | 26 Oct |
| L5 | "Part of the remainder buys Treasuries maturing in late 2032 that, with coupons reinvested, repay the whole remainder as Laura's facility floor." (22) | (a) which pocket absorbs a pre-2028 fall in yields (the floor definition); (b) "during 2032, through a dated 2032 Treasury fund" | +5 to +12 (UNVERIFIED estimate) | notes.md s7 rows 3 and 6; `refresh_tickets.py --floor-rule` | 14 Oct |
| L6 | "We do not recommend it, because Laura will quote the floor to co-sponsors in 2031." (15) | Laura quotes the floor *rounded down* (keeps "cannot fall outside" true) | +2 | `D_range_confidence_2031.md` | 26 Oct |
| L7 | "At September 2026 yields the ten payments cost less than $300,000." (11) | Date the claim to one day and re-check it on the final curve (false on 9 of 20 September sessions on the 1 Jan 2027 basis) | +1 | triage D14 | 6 Nov |
| L8 | Pitch: "...and her contribution cannot fall outside it." (pitch 49 of 50) | Soften to a claim that holds on the buyable ladder (e.g. "is built to stay inside it") | pitch +1 (50 of 50) | triage D4 | 6 Nov |
| L9 | "Our WInS portfolio shows the allocation after both deposits, scaled down." (11) | Only if the 1 Oct vote picks Book L: say the WInS book is the 2027 deposit | 0 to +4 | `D7_wins_book.md` | 1 Oct vote |
| L10 | none | Optional: name the January 2028 five-year yield as the second assumption | about +8 | `D_ips_three_assumptions.md` | if words allow |

**Needed:** L1-L7 add about +21 to +36 body words (sum of the estimates above; triage D6 put the total at 40-50 with
the optional items). L9 adds up to 4 if Book L wins; L10 about 8. **Spare:** 17.

## Candidate cuts (each moves a fact to the Final Report; the team chooses)

| Cut | Words saved | Trade-off |
|---|---|---|
| "We tested this on every Treasury curve since 2000." | 9 | Suggested in triage D6; the test is Final Report evidence |
| "We call our liability-driven approach Root-and-Branch." (the pitch already names it) | 6 | Loses the name's link to "liability-driven"; keep "liability-driven" elsewhere if cut |
| ", when they would have cost about $460,000," | 7 | Loses the vivid comparison; keep it in the Final Report |
| "This policy governs the portfolio ... she plans to open in 2033." shortened to the two deposits and the goal | about 8 | The opening restates the case; judges read it once |

With all four cuts (about 30 words) there are about 47 words to spend: enough for L1-L7 even at the high estimate,
and about 1 word short if L9 and L10 are added too. Without cuts nothing fits: even the low estimate needs about 4 words more than the 17 spare. **Recount in the Google Doc after each change**; the Doc's count is the one that matters.

## Not IPS edits (kept out on purpose)

Numbers, projections, the 2031 range, the reserve size and the co-sponsor text belong in the Final Report (IPS
Instruction; `rab/decisions/D_ips_three_assumptions.md`). Individual securities stay out of the IPS.
