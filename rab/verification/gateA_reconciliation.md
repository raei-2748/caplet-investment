# Gate A reconciliation: M1 primary vs blind rebuild

WS1-reconciler, 30 Sep 2026 (Sydney). This is an AI-generated verification (Claude Code) for Team Caplet. It contains no deliverable text.
Curve: U.S. Treasury Daily Par Yield Curve, row 09/28/2026 (`rab/data/treasury_par_2000_2026/2026.csv`, source URL and
sha256 in `rab/data/MANIFEST.md`). Valuation and settlement date: 28 Sep 2026. All figures are MODEL prices.

## Verdict

**Both pricers produce the same numbers.** The two builders reported a $2,102.73 gap in the ten-payment value, but it
did not come from the data, the conventions or a code bug. Each builder put a *different basis* into the one-number
field `pv_ten_payments_usd`. Both builders computed both bases, and on each basis they agree to the cent. A third
minimal pricer, using the standard library only, agrees with both. The Gate A agreement test (to $1) is met.

| | Primary (`m1_ladder.py`) | Blind (`blind_pricer.py`) |
|---|---|---|
| Put in `pv_ten_payments_usd` | exact basis, payments on 1 Jan 2033-2042: **$287,016.47** | Nov-15 basis, STRIPS maturities 15 Nov 2032-2041: **$289,119.20** |
| Its own exact-basis value | $287,016.47 | $287,016.47 |
| Its own Nov-15-basis value | $289,119.20 | $289,119.20 |

$289,119.20 - $287,016.47 = **$2,102.73**. This is the reported gap, to the cent. The Nov-15 value is higher because each
$50,000 is discounted for 47 fewer days (15 Nov to 1 Jan).

**Classification: spec ambiguity plus a reporting slip. It is not a data, convention or code error.**
- Spec: A3 in `M1_METHOD.md` said "For each basis" and never named a headline. So a builder filling a single field had
  to choose one basis.
- Reporting slip: the primary's own `numbers.yaml` already marks the Nov-15 spot value as the headline
  (`laura.ladder.cost_today_strips`, note "HEADLINE for 'what the ten payments cost today'"). Its summary still
  quoted the exact basis instead.

## Which basis is the headline, and why

**The headline is the Nov-15 basis: $289,119.20 on 28 Sep 2026, or $292,418.11 on 1 Jan 2027 against the $300,000 deposit.**

1. Laura's real ladder is zero-coupon STRIPS maturing 15 November (spec A5). No Treasury, STRIPS or WInS security
   matures on 1 January. The exact-date figure is therefore the *value of the payments*, not a price anyone can
   pay, and it is always a little lower.
2. The IPS figure "about $289k" is this basis. Evidence: insight_v1 H3 = $289,119, and the independent ChatGPT
   check was briefed on "$50,000, maturing 15 November of each year 2032 through 2041"
   (`research/insight_v1/verification/ladder_2026-09-28/README.md`, commit 84e7010, 29 Sep 2026).
3. Section G history ("about $460,000 at 2020 yields"; 2020 median $458,828) is quoted on the same basis in
   `numbers.yaml`.

Strategy impact: none. The IPS already uses this basis, so there is no contradiction to triage.

## Evidence: three implementations

The third pricer (`rab/verification/gateA_third_check.py`) was written from the spec alone. It uses the Python
standard library only and imports neither of the other two. It uses bisection where both others use `scipy.brentq`.
It recomputes A3 (both bases), B1 (the `Portfolio` tab at `close_0928`) and the C yield gaps. It then compares every
figure with both other results and with `numbers.yaml`. Result: **38 checks, 0 failures; the largest dollar difference is
$0.0037**. That difference is cent rounding in `numbers.yaml` and the headline block; between the raw results the
difference is $0.00.

| Quantity | Third | Primary | Blind |
|---|---|---|---|
| Nov-15 basis, value 28 Sep 2026 (**headline**) | $289,119.20 | $289,119.20 | $289,119.20 |
| Nov-15 basis, value 1 Jan 2027 | $292,418.11 | $292,418.11 | $292,418.11 |
| Nov-15 basis, headroom under $300,000 | $7,581.89 | $7,581.89 | $7,581.89 |
| Nov-15 basis, break-even parallel fall | 26.20bp | 26.20bp | 26.20bp |
| Nov-15 basis, value 1 Jan 2028 | $306,524.65 | $306,524.65 | $306,524.65 |
| Exact basis, value 28 Sep 2026 | $287,016.47 | $287,016.47 | $287,016.47 |
| Exact basis, value 1 Jan 2027 | $290,291.38 | $290,291.38 | $290,291.38 |
| Exact basis, headroom / break-even | $9,708.62 / 33.22bp | $9,708.62 / 33.22bp | $9,708.62 / 33.22bp |
| Exact basis, value 1 Jan 2028 | $304,295.32 | $304,295.32 | $304,295.32 |
| `Portfolio` tab cost, `close_0928`, incl. $200 commissions | $294,764.50 | $294,764.50 | $294,764.50 |
| Cash left | $5,235.50 | $5,235.50 | $5,235.50 |
| Each of the 11 holdings' cost | same to the cent | same | same |
| C gaps, 7 bonds (5 in book, 2 stale) | -15.27 ... -92.11bp | same (diff < 1e-9bp) | same |

The C gaps compared in full are -15.27, -14.39, -6.61, -5.14 and -1.89bp for the five bonds in the book, all inside
the 25bp limit. The two stale prices, T 4.500% Feb-2036 and T 4.375% Feb-2038, are -110.93 and -92.11bp; both are
flagged by all three builders.

The same script also compares primary vs blind on everything else both of them built: A4 band (4 variants x 2 bases x
spot and forward), the other price sets and Book L, both C gap measures, F shares, and the G medians, minima, maxima,
shares and deposit check. That is **65 numbers and 8 dates, all identical**, with a largest difference of 0.

**Independence caveat (pre-mortem PM-8).** The primary and blind codes share no files. They do share an author model,
and 14 of about 400 lines are identical idioms (for example the same `brentq(f, -0.05, 0.5, xtol=1e-12)` yield
solver). That is why their C yields match to every digit. The third pricer avoids those idioms (standard library,
bisection, hand-written interpolation and dates) and still agrees. The agreement comes from the spec, not from
shared code.

## Fixes made (strategy unchanged)

1. **Spec** (`rab/models/M1_METHOD.md`):
   - New **A6**: the headline is the Nov-15 basis; the exact basis is always reported beside it, labelled "not
     buyable"; `pv_ten_payments_usd` = Nov-15 spot.
   - New **B6**: the headline book cost is the `Portfolio` tab at `close_0928`, commissions included; Book L costs
     already include their $175.
   - **G**: a V0 share and a V_A share of days may never be quoted under each other's names.
   - **F**: a note that F keeps E6's exact basis as a comparison.
   - A like-with-like rule under Tolerances, and a Changelog.
   - No formula changed.
2. **Primary code** (`rab/models/m1_ladder.py`): a new `headline()` writes a `headline` block into `m1_results.json`
   (right after `meta`) and adds an `[A6 HEADLINE]` line to `m1_report.txt`. No reader has to pick a basis again.
   Re-run check: `m1_results.json` is identical outside the new block, both CSVs are byte-identical, and the report
   differs only by the new line.
3. **Third pricer**: `rab/verification/gateA_third_check.py`, with its output in `gateA_third_check.json`. It exits
   non-zero on any failure, so it can be re-run as a gate check.

`numbers.yaml` did not need a change: it already had the right headline and every value agrees. I re-ran
`build_numbers.py` and got identical content. Then I restored the committed file, so the sha256 stays
`1bc2d19410900a0a3298b62aacbd4bd15ce203c1338e5dd34ca757006ae17f57`.

## Other findings from the comparison (triage per RUN_PLAN s0)

| # | Finding | Evidence | Class |
|---|---|---|---|
| 1 | **The lock hash cannot be checked by re-running.** `build_numbers.py` stamps `generated_et` / `generated_sydney`, so every re-run changes the sha256 even when no number moves. On 30 Sep a re-run gave 9839544d... instead of 1bc2d194...; only those two lines differed. | `git diff` of the re-run | Gate A process (WS0): lock by hashing the committed file; to verify later, compare with those two lines stripped |
| 2 | The primary's summary said "Cost was at or below $300k on 11.1% of days since 2000". That is the **V0** share ("$300,000 in hand that day would have bought all ten"). The spec's G statistic is the **V_A** share, 9.8%, which is what the blind builder quoted. Both are in `numbers.yaml` (`history.share_days_le_300k`), and its `quote_as` is correctly worded for V0. | G.nov15 in both results | note-in-Final-Report (name which one is quoted) |
| 3 | The primary's summary said "Book L at 28 Sep closes: $292,580.89 plus $175 commission". That $292,580.89 already *includes* the $175 (securities $292,405.89). `numbers.yaml` says "including", which is correct. | B.bookL.close_0928 | ignore (summary wording only) |
| 4 | The `Portfolio` tab's bond labels (-8/+6/+13/+14/+15bp) are not the spec's C gaps. The primary found they match a check that treats the clean price as the full price; the blind builder did not test that and reported "not reproduced". The two are consistent, and all three builders agree every in-book bond passes. | C in both results | note-in-Final-Report (wording), as WS1 already said |

## Result to carry forward (from the corrected primary)

- Curve: 28 Sep 2026, U.S. Treasury Daily Par Yield Curve.
- **Ten payments: $289,119.20 today; $292,418.11 on 1 Jan 2027; $7,581.89 headroom; 26.20bp break-even fall**
  (Nov-15 STRIPS basis).
- Exact-date liability value: $287,016.47 (secondary, not buyable).
- **WInS book (`Portfolio` tab, 28 Sep closes): $294,764.50 including $200 commissions; cash left $5,235.50.**
- Source: `rab/models/out/m1_results.json` → `headline`, and `numbers.yaml` → `laura.ladder.cost_today_strips`,
  `wins.portfolio.cost_close_0928`.

Re-run (from the worktree root, about 3 seconds in total):

    /Users/ray/Research/rab-ws/.venv/bin/python rab/models/m1_ladder.py
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateA_third_check.py   # exit 0 = agree
