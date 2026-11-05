# R61 review (e): facts and the locked record
AI-generated review (Claude, 6 Nov 2026). Not submission text.

`keel/scripts/ladder_pv.py` re-run on the 23 Oct close: ladder $297,636 (66.1% of $450,000); a $150,000 Dec-2032 payout costs $117,641 in Jan 2028 (parallel shifts, MODEL). Notes = `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md`; 02c = `harvest/02c_library_models_record.md`; A33 = `keel/rooms/archive_checks/A33_results.json` (S0, C06 design).

| Claim | Verdict | Evidence | A true version must convey |
|---|---|---|---|
| P1 payments fixed, portfolio-only; ten holdings, each redeemed the year before its payment; figures held in Treasuries | TRUE | case L90-92; snapshot :22-31 | – |
| P2 balanced mix "probably" richer by 2042; leverage swing | TRUE (MODEL) | `keel/models/README.md:73`, `:78` | – |
| P2 "about two thirds of her $450,000" | TRUE | re-run; GROUND_TRUTH:87 | "Today's" = 23 Oct, last close on file |
| P3 bought Jan 2027; gap first claim on 2028 deposit | TRUE | notes:15; 02c:91 | – |
| P3 funds hold one year's Treasuries, pay out that December; some years have no listed Treasury | TRUE | casestudy_pack:19, :55; COMPETITION.md:93-96 (real plan WInS-only), :112 | Keep "listed": real Treasuries mature in 2032-35 (casestudy_pack:186) |
| P4 "enough ... to repay the whole deposit" | STRAINS | P3's top-up; range_2031/README:47-50, :54-58; 02c:270 | Holds only while the top-up is small: near a one-point fall before January 2027 nothing is left for shares, and beyond it the bottom shrinks (re-run). Say "what is left", or the order: shares shrink first, then the bottom |
| P4 bottom = extra payout, rounded down; co-sponsors, earnings "could shrink" | TRUE (hedged) | archive.md:73; 02c:248; what_october_allows:36, :52 | Bottom is net of cover the kept half can't pay |
| P4 "the bottom barely moves in a slump before 2031" | HALF-TRUE | A33: floor pays part of the cover in 26.9% of futures; shares halved, bottom lower by median $7,471 (p95 $20,661) | A slump can't touch the fund behind the bottom, but if it leaves her kept shares short of the cover, the bottom drops by the difference. P5 says so; P4 contradicts it |
| P4 "losing every share would still return almost all the deposit" | HALF-TRUE | A33 wiped: cover then comes from the floor, median $12,688, p95 $25,353; $21,627 if yields fall 2pt | No payment suffers (02c:245); the fund repays the deposit less the cover. "Most", not "almost all", in bad-rate futures |
| P5 "each holding's repayment months before its January" | FALSE | notes:22 ("about two weeks before"); P3's own "that December"; casestudy_pack:137-138; notes:18 ("47 days"); only notes:16-17 are months; 02c:242 | Before each January, from about two weeks (funds) to 10.5 months. True of waiting money: the funds' bonds mature through their last year and sit in cash (casestudy_pack:20, :81-84) |
| P5 low rates could leave payments short; cover dated, from shares, into Treasuries, zero-earnings sizing; top = bottom + other half's proceeds | TRUE | notes:14, :16, :18, :23-24; archive.md:87, :95, :101; 02c:243-244 | – |
| P5 "the range she names is smaller" | HALF-TRUE | archive.md:87 ("comes off the bottom") | Both ends fall; the width doesn't. "Smaller" reads as narrower |
| P5 "barring a US default and with both deposits made, no payment waits on shares, interest rates or an early sale" | TRUE (MODEL), two gaps | A33 S0/S1/S6 all paid; S9 (deposit halved) 1.3% short; casestudy_pack:228 (fund board may move the end date) | "Made in full"; the funds' payouts aren't fixed and their end date isn't Laura's, so the replacement rule (archive.md:72) is an assumption too |
| P6 she chooses where in 2033 | TRUE | case L101-103, L164 | Shares set the ceiling, she sets the gift (VT note's "gift", notes:14) |
| P6 "including shares she can sell any day" | HALF-TRUE | A33 26.9%; 02c:244 | What the cover leaves of her kept half stays hers, sometimes nothing. No withdrawals before 2033 (case L63-65) |
| P7 reserve = everything held plus cover, no trade; one holding a year; tenth redemption plus its own interest | TRUE | snapshot :22-31; notes:24; 02c:82 | – |
| Pitch "promise only money already in Treasuries" | HALF-TRUE | 02c:243; notes:18 | True of the range; payments lean on reinvested interest until the 2031 cover |
| Pitch "Her first $300,000 buys Treasuries for her ten ... payments" | HALF-TRUE | 02c:236, :260; notes:15 | As far as it reaches; the 2028 deposit tops up if needed |
| Pitch "Most of her 2028 deposit sets the bottom"; "half her shares become Treasuries for its top" | TRUE | re-run 78%; 02c:246 | – |

## What the locked record needs that R61 lacks
1. Five notes and reflection 2: the funds' payout is not fixed (02c:85). R61 implies it only for the bottom. Reflection 2's liquidity reason is unused.
2. How certainty was evaluated (case L97-99; 02c:160-162): no test stated.
3. Inflation (case L146-147; reflection 1; 02c:87): absent.
4. Reserve size in words (case L96): composition only.
5. Basis of confidence in the range (case L117-118): implied, never stated.
6. Living costs outside the portfolio, no flows before 2033 (case L61-65): absent.
7. Replacement rule if a fund closes or moves its date (archive.md:72; casestudy_pack:228).
8. WInS book scaled (archive.md:100): Final Report job, but the frozen book shows VT and an oversized IBTM against P3's "first $300,000".
