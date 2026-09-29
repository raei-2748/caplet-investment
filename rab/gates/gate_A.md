# Gate A (data): PASS

WS0, 30 Sep 2026 (Sydney). AI-generated gate record (Claude Code) for Team Caplet; no deliverable text.
Test (RUN_PLAN s3): ladder priced twice and agreeing to $1; curve and prices dated and sourced; `numbers.yaml` locked.

## Result

| Check | Result |
|---|---|
| Curve dated and sourced | U.S. Treasury Daily Par Yield Curve, row 28 Sep 2026, `rab/data/treasury_par_2000_2026/2026.csv` (URL, sha256, fetch time in `rab/data/MANIFEST.md`) |
| Prices dated and sourced | `rab/data/wins/wins_prices_2026-09-28.csv` (`close_0928`); WInS names and bond units marked UNVERIFIED where not seen in WInS |
| Ladder priced twice, agree to $1 | 4 builders (primary, blind 1, blind 2, third stdlib pricer): **max difference $0.00** |
| Book priced twice, agree to $1 | same 4 builders: **max difference $0.00** |
| `numbers.yaml` locked | 70 entries, status LOCKED, `gate_a` block; sha256 in `rab/numbers.lock` |
| Fallback to insight_v1 figures | not needed; nothing FLAGGED |

| Quantity (28 Sep 2026 curve, MODEL) | Primary | Blind 1 | Blind 2 | Third |
|---|---|---|---|---|
| Ten payments, Nov-15 STRIPS basis (**headline**) | $289,119.20 | $289,119.20 | $289,119.20 | $289,119.20 |
| Ten payments, exact 1 Jan basis (secondary, not buyable) | $287,016.47 | $287,016.47 | $287,016.47 | $287,016.47 |
| `Portfolio` tab book at 28 Sep closes, incl. $200 commission | $294,764.50 | $294,764.50 | $294,764.50 | $294,764.50 |

Primary vs blind 1 on everything else both built: 65 numbers and 8 dates identical. Third check: 38 checks, 0 failures
(largest $0.0037, cent rounding). The first-round $2,102.73 "gap" was two builders reporting different bases; see
`rab/verification/gateA_reconciliation.md`. The spec now fixes the headline basis (M1_METHOD.md A6, B6).

## Key locked numbers (quote the `quote_as` strings in `rab/numbers.yaml`)

- Ten $50k payments cost **about $289,000** today (`laura.ladder.cost_today_strips`), **about $292,000** on 1 Jan 2027
  (`laura.ladder.cost_2027_strips`); headroom under $300k $7,582, gone after a 26.2bp fall.
- WInS book: **about $294,800** including commission, cash left $5,235.50 (`wins.portfolio.cost_close_0928`).
- History: 2020 median $458,828 ("about $460,000"); cheapest since May 2002 (`history.*`).

## Lock mechanics

`build_numbers.py --lock` writes a fixed lock stamp instead of the run time, so a re-run reproduces the file byte for
byte (checked twice: same sha256). This fixes reconciliation finding 1 (hash changed on every rebuild). The
`numbers:` body is identical to the DRAFT (sha256 1bc2d194...); only the header changed.
Verify: `shasum -a 256 rab/numbers.yaml` against `rab/numbers.lock`, or re-run with `--lock`.

## Carried forward (strategy unchanged; triage from WS1)

- fix-before-6-Nov: T 4.500% May-2038 accrued recorded 0.530, should be about 1.663 (Sheet input, ~$215).
- fix-before-6-Nov: IPS wording "needs no rebalancing"; coupon reinvestment (`reinvest.*`) must be caveated.
- Friday: re-fetch curve and prices, re-run M1; if any headline moves, WS0 re-locks with a changelog line.
- Stale WInS prices (4.5% Feb-2036, 4.375% Feb-2038) flagged -111bp / -92bp; not in the book.
