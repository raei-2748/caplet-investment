# IPS v3.1: Keel's answer to the outside review (Gemini, pasted by Ray, 24 Oct 2026)
**AI DRAFT (Claude, 24 Oct 2026).** Suggestions only; the IPS Report doc was not touched. Caplet rewrites and decides.
(Keel is a simulated team, AI-written.) Counts by `keel/office/tools/textcheck.py`: **pitch 37 strict, IPS 489 strict**
(484 by spaces), 0 overclaim words. 489 passes the 500 limit but sits above Keel's own 470 cushion (R7); the cut
menu is at the bottom.

## Verdict per point
| # | Reviewer's point | Verdict | Why (checked against) |
|---|---|---|---|
| 1 | Two en dashes: replace for the SMApply form | **Reject as a gate** | A web form takes Unicode; the official rules set words, not characters. Ray's own voice uses spaced en dashes. Swap them only if Caplet prefers |
| 2 | Pre-2033 hold rule was cut | **Accept** | Real gap; the locked TNA line "Every year the bonds sit untouched is a good year" needs it. Restored as a trading rule that also covers replacing a delisted holding (the clash that got it cut) |
| 3 | Laura's background has gone | **Modify** | A biography line was cut on purpose as generic (criterion map F3). Her statistics degree comes back only if the name does real work, as Pre-Registered does |
| 4 | Nothing on a stock crash 2028-33 | **Accept** | True, and it is the "how does she feel in a bad year" question. Now P4 says it in one line |
| 5 | 2027 leftover in ~2/3 of paths | **Reject (stale)** | That is the 15 Oct curve. On the 22 Oct close the ladder costs $298.9k-$302.1k, P(cost > $300k) 47%, and waiting cash shaves the rest (MODEL, `keel/office/outbox/2026-10-24_SD-T03_numbers_ladder-22oct.md`; L-05 rung 2). The leftover is about zero; Caplet's vote D3 (Tue 27 Oct) decides whether to name it |
| 6 | Bound "lowers the floor, not a payment" | **Reject** | To pass the $150k deposit the ladder must cost over $450k: a ~4-5 point fall in yields before January (MODEL). "First" would invite the question it answers |
| 7 | Bond coupons can't buy $1,000 bond lots | **Accept (modified)** | Right: WInS bonds trade in $1,000 face units (`competition/COMPETITION.md`:86). But "coupons just wait in a short-term ETF" would quietly change the model, which reinvests at each holding's own yield (`ips_numbers.py`:136). So: coupons wait in the ETF, then buy more of the holding that paid them |
| 8 | P4 "never gives more than she quoted" is backwards | **Accept (modified)** | Fair: co-sponsors fear less, not more. New P4 line: a stock fall after 2031 moves the gift toward the floor she already owns; any rise stays with Laura. Avoids "never below" (IBTM pays a NAV) |
| 9 | Choppy short sentences in P1 and P5 | **Reject** | Deliberate: the long-then-short rhythm is Ray's own essay voice (`keel/VOICE.md`); minimal-edit rule |
| 10 | Pitch: "co-sponsors may fund the building without paying to run it" isn't in the case | **Accept** | Checked: the case lets co-sponsors give "operating support beyond Laura's commitment" (case p.3). What it forbids is relying on them for *her* ten payments. New pitch grounded in that rule |
| 11 | The name must match the Final Report | **Agree** | Noted for the Final Report plan; the TNA carries no name, so any of the three packages fits |

## Full text (v3 + accepted fixes)
**Pitch (37 strict; room for a name and a closing image)**

Laura's ten $50,000 operating payments cannot lean on co-sponsors, so [NAME] buys them first, in Treasuries held to maturity. More Treasuries back a minimum facility contribution. Above that minimum, a global index fund grows her gift.

**IPS (489 strict)**

This policy governs Laura Gao's $450,000 for her 2033 Taiwan residency. Its first objective is to fund ten $50,000 operating payments, each January of 2033-42, with high certainty from this money alone. We match each payment with a Treasury bond or defined-maturity Treasury ETF maturing before it. Each payment's cash comes from a maturity, not a sale. By high certainty we mean every payment is owned in Treasuries by 2028. No stock has to rise. Only reinvested coupons and the ETF payouts can leave one short. The second objective is a facility contribution with a floor Laura can quote to co-sponsors and growth above it.

With her living costs met elsewhere and no withdrawals due before 2033, Laura's ability to bear risk beyond the payments is high. Her tolerance for a missed payment is low – the artists would bear the loss.

[NAME] buys every payment before a single share. Laura's 2028 deposit depends on publishing and speaking income, so the 2027 deposit goes entirely to the payments, latest first. Any gap left in January is the first use of the 2028 deposit, so a rate fall before we buy lowers the floor, not a payment. From the 2028 remainder, just enough goes into a 2032 Treasury ETF to grow back to the full remainder; that sum is Laura's facility floor. The rest buys a global index fund of thousands of companies. The payments rely on one issuer by design – no dollar asset is safer.

In 2031 Laura tells co-sponsors a range from the floor, quoted at the 2032 ETF's projected payout rounded down, to the floor plus half the fund's value then. In 2033 the same rule sets her contribution, capped at that top. A stock fall after 2031 moves the gift toward the floor she already owns; any rise stays with Laura.

Moving floor money into stocks would raise the expected gift. This is the obvious trade. But it could break a number Laura has quoted, so we refuse. A lasting fall in yields hurts twice: the payment Treasuries cost more in January, and their coupons earn less afterwards. Before the 2033 gift, we price any gap the ladder will leave at that day's yields and set it aside from the half Laura keeps, then the contribution above the floor. Inflation or a stronger Taiwan dollar raises costs in Taiwan; the rest of her half covers overruns first, then her own plans.

Until 2033 we trade only to invest the 2028 deposit or to swap a delisted holding for an earlier Treasury. Coupons and early maturities wait in a short-term Treasury ETF; coupons then buy more of the holding that paid them. Each January we review the plan with Laura. In 2033 the payment Treasuries become the operating reserve, renamed rather than rebuilt: five Treasury ETFs for 2033-37, then five bonds for 2038-42. Our WInS portfolio shows this allocation, scaled down.
## If Caplet wants back under 470 (whole ideas, not squeezes)
- "Each payment's cash comes from a maturity, not a sale." (-10): the new trading rule now carries the idea, but the
  outsider judge's favourite line goes with it.
- "This is the obvious trade." (-5): costs some voice.
- "quoted at the 2032 ETF's projected payout rounded down," (-9): the Final Report can carry the quoting method.
Any two of these take it to 470-475.
