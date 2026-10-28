# FICTION (the room, the simulated readers) + real work. LR-05: who pays for the blind fifth?

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), Laura's Room, Wed 28 Oct 2026, 15:10 run
(Sydney), round 1 beat 6 (`../../loop/rounds/2026-10-28.md`). Not for submission. Simulated readers are tests built only
from the case, never quotes. Script `LR-05_who_pays_the_blind_fifth.py` (appends one block to the Lab's L-11 run,
unchanged), results `LR-05_results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths, seed
20261016 | L-11's model | MODEL.** Self-check: the script reproduces L-11's bottom misses exactly (A 0.81% / 1.39% /
19.9%, C6 2.15% / 3.27% / 29.8%, S0 / S1 / S6).

**For a judge, first.** The Lab found a cure for the coupon gap with two halves: pay the four-fifths already showing in
January 2033, and cover the last fifth with a $7,500 Treasury holding bought with the 2028 deposit (challenger A),
or with a $7,500 cushion set aside in January 2033 (champion C6). The Lab tested both *without* the 2031 mark Keel
adopted yesterday (LR-04: the bottom is quoted net of the gap already visible). Put the mark into both, and let it
carry the cushion too, and C6 wins on every measure a co-sponsor cares about: the same bottom label, never broken in
200,000 paths, cut in about one path in six by about $2,000, for a quarter of A's cost to the signal. The rule
underneath is a clearing house's: **the defaulter pays first.** Laura's own spare money stands behind her own
promise; the co-sponsors' number is touched only where hers runs out, and they are told in 2031, not surprised in 2033.

**Against the newest draft, V28 (main, 28 Oct; `../../ips_rewrite/drafts/D8/ips.txt`).** Two lines meet this run. (1) "So the bottom is the floor she owns, rounded down" has no 2031 mark, and "the one thing that can still trim the gift" is C6 unmarked: the coupon gap can still take the gift below the bottom after it is named (2.2% / 3.3% / 30% of paths, S0 / S1 / S6). With the mark carrying the cushion, the gap trims the bottom once, in 2031, and never the gift after it. (2) "that is what Laura's half, sellable any day, is for" (the building) beside "from leftover cash and Laura's half first" (the cushion) is the double booking; one clause fixes it. Caveat: the 2031 lock (the promised half into Treasuries) is not in L-11's model; the Genius Lab's R10 ran the lock with the cushion (99.25% inside the range).

## 1. The test (MODEL; $7,500 in every arm; mark = 2031 view of the gap, rounded up to $5k)
"Mark carries the cushion" (MC) cuts the 2031 bottom by max(gap seen in 2031 + $7,500 - 2027 leftover - Laura's half
in 2031, 0). Co-sponsor money lost uses LR-04's elasticity (List & Lucking-Reiley seed study, E = 0.94; 0.5 in
brackets): a heroic transfer from a mail campaign to institutions, so read the ranking, not the decimals.

| S0 independent | Payments short >$1k | Bottom label (p50) | Paths cut / mean cut | Below the quoted bottom | Top reached | Gift p50 | Laura's half sold | Co-sponsor money lost |
|---|---|---|---|---|---|---|---|---|
| A (L-11 D2, no mark) | 0.00% | $135k | 100% / $8.8k | 0.81% | 77% | $157k | 34% | 6.0% (3.2%) |
| A + mark | 0.00% | $135k | 100% / $9.7k | 0 of 200,000 | 77% | $157k | 34% | 6.6% (3.6%) |
| C6 (L-11 D1, no mark) | 0.07% | $145k | 0% | 2.15% | 73% | $165k | 71% | 0 |
| C6 + LR-04 mark (gap only) | 0.07% | $145k | 8% / $0.8k | 0.08% | 73% | $165k | 71% | 0.6% (0.3%) |
| **C6 + mark carries the cushion** | **0.07%** | **$145k** | **17% / $2.0k** | **0 of 200,000** | 73% | $165k | 71% | **1.4% (0.8%)** |
| C6, stocks never pay (Laura's half kept out) | 0.07% | $130k | 71% / $9.8k | 0 of 200,000 | 39% | $162k | 0% | 6.9% (3.8%) |

| Same, the other two worlds | S1 rho 0.5: below bottom / cost | S6 yields -2pt for good: below bottom / cost | Payments short >$1k (S1 / S6) |
|---|---|---|---|
| A + mark | 5 of 200,000 / 6.7% | 13 of 200,000 / 11.8% | 0.00% / 0.01% |
| **C6 + mark carries the cushion** | **10 of 200,000 / 1.6%** | **29 of 200,000 / 8.8%** | 0.07% / 0.09% |
| C6, stocks never pay | 0 / 6.9% | 2 of 200,000 / 14.6% | 0.07% / 0.09% |

**What it says.**
1. **The mark does the work the holding was bought for.** Unmarked, A's bottom breaks in 1 path in 125 and C6's in 1
   in 47; marked, both are 0-29 in 200,000. Yesterday's mark was the cure for the bottom; today it covers the cushion too.
2. **A buys certainty for the payments that the co-sponsors pay for in every path.** Its ~$9-10k comes off the bottom in 100%
   of paths, though Laura's own spare money (the 2027 leftover and her half) could have carried the cushion in about
   five paths in six (LR-04's "initial margin taxes the signal in every path", again). C6 + mark charges the bottom
   only in the ~17% of paths where her spare money can't, and says so in 2031.
3. **The payments difference is real but tiny:** 0.07-0.09% short by over $1k against 0.00-0.01%. Both are far inside
   any "high degree of certainty" (case :91).
4. **Purity costs A's price.** Keeping Laura's stocks out of the cheques entirely (locked TNA reflection 3 read
   strictly) costs the co-sponsors 6.9% (S6 14.6%) and halves the chance of the top. Someone has to pay for the gap:
   Laura's spare money, or the bottom. There is no third payer, because the cheques can't be the one.
5. **Honest weakness of the winner.** Laura's half is sold once, in January 2033, in 71% of paths (S6 87%), median
   $7,500: the cushion. Unused, it comes back to her after the tenth cheque. But D6 calls her half "the project's
   second cheque" (for building-cost inflation), so the cushion is its first call, and the IPS must say so in one
   clause or a judge will catch the double booking.

## 2. Beat 6: the Lab's four challengers, read three ways (SIMULATED readers, built only from the case)
| Challenger | Co-sponsor (foundation programme officer) | Competition judge, case open | Practitioner, from the find's field | Call |
|---|---|---|---|---|
| **A** coupon holding, 2 Jan 2028, before the floor | "So the number for my board paper is $10k lower in every world, to protect a cheque you'd have covered anyway?" | Clean on :91 (payments 0.00%) and the central idea, but answers :117-120 by shrinking the range rather than by sizing the reserve | Clearing-house risk officer (RBA Bulletin, Dec 2017: margin is "a 'defaulter-pays' resource; it is not mutualised"): A posts the margin out of the pool that should come last | **SHARPEN**: keep its insight (the blind fifth is real and bounded), drop its funding |
| **C6 + mark carries the cushion** | "The bottom moves only in 2031, only if Laura's own spare money can't cover her own cheques, and never after. I can book that." | Answers :94-97 literally (the reserve is sized "at the beginning of 2033, before making the first operating payment") and :119-120 literally (the 2031 range is quoted net of everything the reserve might still need) | Same officer: defaulter's margin first, the mutual fund last, and the waterfall written down before anyone defaults | **PASS**, to tonight's head-to-head as C6's amended form |
| **B** a check before every cheque | Indifferent: nothing in it touches the 2031 figure | Breaks locked reflection 3 (stocks sold at a payment deadline in 24% of paths) | Stage manager (CCSU handbook): the fix goes in "before the next performance"; cheque ten has none | **KILL** for the IPS; FR habit only (as the Lab) |
| **C** Redington immunisation of the residual | "Half the deposit in 30-year bonds to save $7,500?" | Fails Portfolio Analysis' "reasonable": a hedge bigger than the risk (43-50% of the 2028 deposit) | Pension actuary: immunisation matches the whole liability, not a rounding error of it | **KILL** for the IPS; FR: priced and turned down |
| **D** thin-coupon twins + a smaller holding | Invisible to her | A nice dedication detail ("effective use of investment concepts"), but a WInS listing is unseen | Bond desk: same yield, lower coupon, less to reinvest; the only cure bought in 2027 itself | **PARK** (FR) until the Trading Desk prices the twins (Sat 31 Oct) |

## 3. Case-requirement check on the survivor (C6 + mark carries the cushion)
| Case line | Asked | Answered? | Sentence that would fix any gap (AI DRAFT (Claude, 28 Oct 2026); Caplet rewrites) |
|---|---|---|---|
| :94-97 reserve size, composition, how it changes | Size at Jan 2033 | Yes: the ten holdings as bought, plus the visible gap and $7,500 in a WInS-listed short Treasury fund (Trading Desk, 28 Oct: not "bills"); one holding redeemed each December | "In January 2033 the reserve is the ten holdings plus whatever the coupons have fallen short by, and $7,500 more." |
| :97-99 define certainty, how evaluated | Payments short | Yes: under 1 in 1,000 by over $1k in three worlds (MODEL) | none |
| :101-103 flexibility | Not all remaining assets | Partly: the cushion is the first call on her half; unused, it comes back to her | "Her half pays the cushion first; whatever the coupons don't need comes back to her." |
| :113-120 range, confidence, protect the payments | Range that protects | Yes, structurally: the 2031 bottom already nets the reserve's possible need, so the range can't eat a cheque | "In 2031 the bottom is what Laura owns, less anything her cheques might still need that her own spare money can't cover. After that it doesn't move." |

**Line it could change:** D6's slot 7 ("in January 2033 the reserve changes once ...") and the 2031 range sentence.
**North stars and criteria:** star 4 (a clearing house's default waterfall, applied rather than named) and star 3 (the
answer to "a smaller promise kept or a bigger one missed" is "neither: a bigger promise, kept"); Investment Strategy,
Client Knowledge (:94-97, :117-120), Portfolio Analysis.

**Plain-English lesson.** When a risk has to land on someone, decide the order before it happens: the person whose
promise it is pays first, and everyone else is told, in advance, exactly when they might be asked.
