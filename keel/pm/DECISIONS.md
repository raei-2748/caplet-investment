# Decision queue (decisions waiting for a Caplet vote)

Keel prepares the options; Caplet votes. When a vote is taken, record it (with any dissent) in
`caplet/decisions/LOG.md` and move the row to "Decided" below with a link. Keel's own fictional decisions stay in
`keel/tea_room.md`. Vote dates Sydney.

## Waiting for a vote
| ID | Decision | Options (short) | Options memo | Vote by | Who votes |
|---|---|---|---|---|---|
| D1 | Coupon reinvestment risk, now two votes (26 Oct): D1a floor last in the order (yes/no); D1b quote margin below the floor (none / margin / $10k buffer) | Keel leans D1a yes, D1b margin | [ballot v2](../office/outbox/2026-10-26_SD-T12b_noticeboard_vote-set-B-ballot-v2.md); Courtroom C-01 | Tue 27 Oct | Whole team |
| D2 | What "high degree of certainty" means (standard and words) | Mechanism only (bonds held to maturity, matched) / mechanism + modelled standard / plus a named residual-risk list | [T04a](../office/outbox/2026-10-24_SD-T04_strategy_vote-set-B-options.md); `caplet/decisions/02_high_certainty_definition.md` | Tue 27 Oct | Whole team |
| D3 | Shortfall order if the ladder costs more than $300k, and where the 2027 leftover sits | 2028 deposit first, longest rungs first / leftover in cash or a short Treasury ETF vs in VT | [T04b](../office/outbox/2026-10-24_SD-T04_strategy_vote-set-B-options.md); R1 | Tue 27 Oct | Whole team |
| D4 | Floor definition and the 2031 valuation date | Floor = IBTM value rounded down / a fixed dollar figure; value on 1 Jan 2031 vs the announcement date | [T04b](../office/outbox/2026-10-24_SD-T04_strategy_vote-set-B-options.md); `keel/library/range_2031/README.md` | Tue 27 Oct | Whole team |
| D5 | Jobs for the half Laura keeps; meaning of "responsible" and "flexibility" | Overrun buffer first / ventures first / split | [T04c](../office/outbox/2026-10-24_SD-T04_strategy_vote-set-B-options.md); `caplet/decisions/05_facility_contribution.md` | Tue 27 Oct | Whole team |
| D6 | Does WInS still show Laura's allocation at the lock (any order needed?) | Hold as is / small fix by Thu 5 Nov 08:00 | [T04c](../office/outbox/2026-10-24_SD-T04_strategy_vote-set-B-options.md); WO-0005 (hold) | Tue 27 Oct | Whole team; Ray places |
| D7 | Adopt this project office and the autonomous loop (scheduled routines) | Adopt / adopt with changes / not now | This pull request | Sun 25 Oct (retro) | Ray, then the team |

Vote set A (word list, name, "promise", 16 Oct North Star memo) was set for Sun 18 Oct; Keel has no record of the
result. A student should log it in `caplet/decisions/LOG.md` or re-queue it here.

## Decided
| ID | Decision | Result | Date | Record |
|---|---|---|---|---|
