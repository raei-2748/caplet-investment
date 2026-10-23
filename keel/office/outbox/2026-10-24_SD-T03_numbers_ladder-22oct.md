# The 22 Oct close took Laura's ladder to about $300,000: the 2027 leftover is gone on every basis
AI-generated research by the Keel Office (Claude Code). Not for submission. Cite in Works Cited.
Work order: SD-T03 | Asked by: self-directed (board card T03) | Desk(s): Numbers (Jun; ladder-pricer, numbers-auditor) | Date: Sat 24 Oct 2026 (Sydney)

## Answer
- **Yields fell hard on the 22 Oct U.S. close** (10-year 5.13% -> 4.96%, 20-year 5.47% -> 5.32%, 30-year 5.42% ->
  5.29%), and the cost on 1 Jan 2027 of Laura's ten $50,000 payments rose about $4,900 in one day. MODEL, 22 Oct curve:
  | Basis | Script | Cost | Headroom under $300,000 |
  |---|---|---|---|
  | Payment dates (1 Jan 2033-42), bootstrapped (the verified 27 Sep method) | `keel/scripts/ladder_history.py` | **$298,861** | **$1,139 (4bp)**; 21 Oct: $6,072 (21bp) |
  | Holdings (bond maturity dates), zero-rate view | `keel/library/ips_numbers_2026-10/ips_numbers.py` | $300,224 | **-$224** |
  | Holdings, forward to 1 Jan 2027 | `keel/library/range_2031/range_2031.py` | $302,139 | **-$2,139 (-7bp)** |
- **Chance the ladder costs more than $300k on 1 Jan 2027: 47%** (was 35% on 15 Oct; `ips_numbers.py`, rates 1.0
  point a year). The range model says the 2028 deposit must top up the ladder in **57%** of paths (90bp a year), top-up
  p95 $22,033. In other words, the January-gap rule is no longer a corner case; it is the expected case.
- **Knock-on (MODEL, 22 Oct):** the "2027 leftover", the first link of the draft's shortfall order (Tab 15, last
  paragraph), is about zero. The 2031 quoted bottom drops from $145,000 to **$140,000** (range model, all three equity
  models); top p50 $165,000 (p5-p95 $141k-$187k); the gift lands at or above the bottom in ~100% of paths and reaches the
  top in 76% (lognormal). Coupon-reinvestment shortfall unchanged (p95 $25,111). Payments needing more than every
  backup: 9.0% (15 Oct: 7.1%).

## Evidence
- Curve: `keel/library/assistant_review_2026-10/checks/tsy_202610_22oct.csv` (treasury.gov daily par curve, rows
  10/21 and 10/22/2026; committed 23 Oct). A fresh download failed tonight (treasury.gov refused by the network
  proxy), so 22 Oct is the newest close on file.
- Runs tonight: `ladder_history.py` as committed; `ips_numbers.py` and `range_2031.py` with only the curve file and
  date changed (results kept outside the repo; committed `results.json` and `range_2031_results.csv` still hold the
  15/16 Oct runs their README files describe).
- Check (numbers-auditor): the one-line rule from Lab L-01 (cost moves $289 per 0.01% in the 10-year) predicts
  $298,841 for 22 Oct from the 21 Oct cost; the full repricing gives $298,861 (miss $20).

## Limits
- MODEL throughout. The three bases differ by up to $3,278 on the same curve because they place the cash flows on
  different dates; no figure from this table belongs in the IPS (R7: "framework, not calculations").
- One day is one day: on 19 Oct the headroom was $7,007. The point is not the level; it is that a single ordinary
  17bp move erases it.
- `range_2031.py` could not run its "history" equity model since the repo restructure (wrong path to
  `archive/rab/`); fixed tonight (one line), output unchanged for the other two models.

## For the team
- **Vote set B (Tue 27 Oct):** D3 (what fills the January gap, and in what order) and D1 (coupon risk) now decide
  real money in about half the paths, not a footnote. Options memo: `2026-10-24_SD-T04_strategy_vote-set-B-options.md`.
- **IPS authors (draft due Sat 31 Oct):** cut "about $292,000" from the pitch (stale by ~$7-10k on every basis), and
  do not write that the 2027 deposit alone buys all ten payments. The rule ("any gap is the first use of the 2028
  deposit") is what holds; the number does not.
- Owner: whole team (vote), IPS authors (draft). Jun reprices on each new close he can reach.

AI use: Claude Code re-ran the team's existing ladder, IPS-number and range scripts on the 22 Oct 2026 Treasury curve (Keel Office, SD-T03, 24 Oct 2026).
