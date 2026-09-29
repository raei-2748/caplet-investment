# M5 spec: century backtest of Root-and-Branch, and the cost-of-certainty history

WS3, 2026-09-30 (Sydney). AI-generated research specification (Claude Code) for Team Caplet; no deliverable text.
Implementation-independent: a builder who reads only this file and the inputs in section 1 must reproduce every M5
number within the tolerances in section 6. The reference code is `rab/models/m5_backtest.py` (a blind builder must
not read it). Strategy is not reopened (RUN_PLAN s0): this model tests the adopted design, it does not redesign it.

## 0. Questions

1. **Cost of certainty.** What would Laura's ten $50,000 payments have cost on every Treasury curve the data allow
   (1871-2026), priced exactly like the Gate A headline (`laura.ladder.cost_today_strips`)? Where does 28 Sep 2026 sit?
2. **Backtest.** If Laura's two deposits had arrived in year Y and Y+1 (instead of 2027 and 2028), with that era's
   yields for the ladder and the floor and that era's stock returns for the branch, what would the plan have
   delivered? Every start year Y the data allow.

## 1. Inputs (paths relative to the worktree root)

| Id | File | Content |
|---|---|---|
| H1 | `rab/data/treasury_par_1990_1999/*.csv`, `rab/data/treasury_par_2000_2026/*.csv` | Daily Treasury par curve 1990-2026 (same files as M1 G) |
| H2 | `rab/data/history/daily_curves_1962_1989.csv` | FRED constant-maturity yields (DGS*) every day 1962-1989 with both 1 Yr and 10 Yr present, in the par-file column layout (percent) |
| H3 | `rab/data/history/shiller_monthly.csv` | Shiller monthly `GS10` (long rate, percent) 1871-2026 |
| H4 | `rab/data/history/soy_curves.csv` | Par yields on the first trading day of each year 1871-2026; `basis` = `treasury_par` (1990-), `fred_cmt` (1962-1989), `flat_shiller_gs10` (1871-1961: only the 10 Yr column, = Shiller January GS10) |
| H5 | `rab/data/history/annual_history.csv` | Calendar-year returns 1871-2025: `world_eq`, `us_eq`, `us_bill`, `cpi_infl` (sources in `build_history.py` docstring) |
| N  | `rab/numbers.yaml` | `laura.ladder.cost_today_strips`, `laura.ladder.cost_2027_strips`, `laura.floor_cost_2028`, `laura.stock_fund_2028_usd.strips`, `market.par_curve`, `history.*` (reproduction targets) |

All returns are decimals for the calendar year (row t = growth from the start of year t to the start of t+1).

## 2. Curve (identical to M1_METHOD.md A1, the "D1 method")

Tenor map: 1 Mo = 1/12, 2 Mo = 2/12, 3 Mo = 0.25, 6 Mo = 0.5, 1 Yr = 1, 2 Yr = 2, 3 Yr = 3, 5 Yr = 5, 7 Yr = 7,
10 Yr = 10, 20 Yr = 20, 30 Yr = 30; blank tenors skipped; other columns ignored. Par grid t_j = 0.5j, j = 1..60,
linear interpolation of (tenor, yield/100), flat outside; bootstrap DF_j = (1 - (p_j/2) sum_{i<j} DF_i) / (1 + p_j/2);
DF(t) = exp of the linear interpolation of (0, 0), (t_j, ln DF_j), flat ln DF beyond 30 years. Year fraction =
calendar days / 365.25. A curve with only the 10 Yr column (1871-1961) is therefore a flat par curve at GS10.

## 3. Part A: cost-of-certainty series

A1. Curve dates: every row of H1 (1990-01-02 .. 2026-09-28); every row of H2 (1962-1989); the first month of H3 rows
1871-01 .. 1961-12 (monthly; the curve date is the 1st of the month; flat par curve at that month's GS10).
A2. For curve date d, with D = 2026-09-28 and P_k = 15 Nov of 2032..2041 (k = 1..10):
`V0(d) = sum_k 50,000 x DF_d(d + (P_k - D))` (the calendar-day offset P_k - D is kept, "same time to maturity").
This is M1 G's spot value on the Nov-15 basis; on d = D it equals `laura.ladder.cost_today_strips`.
A3. Outputs: `rab/results/M5/cost_of_certainty_series.csv` (date, V0, basis), `..._by_year.csv` (per calendar year:
min, median, max, basis). Headlines: (i) reproduction of M1 G on the H1 days: V0(D), the 2020 median, 2020 max and date,
the last date before D with V0 <= V0(D); (ii) extended: the lowest and highest V0 since 1871 and since 1962 and their
dates; the share of monthly observations (first curve date of each month) since 1871 with V0 <= V0(D); the same share
with V0 <= 300,000; the share of calendar years 1871-2026 whose median V0 (over all curve dates of that year) is below
V0(D). Sensitivity: the month share again after dividing every pre-1962 V0 by (1 + e), e = the A4(a) median and 95th
percentile error (removes the flat-curve bias).
A4. Approximation checks (reported, never used to adjust): (a) flat vs full curve: on the first curve date of every
month 1962-2026 compute V0 with the full curve and with only its 10 Yr yield; report the median and the 5th/95th
percentiles of flat/full - 1 by decade. (b) FRED vs Treasury file: on the first date of every month 1990-2026,
V0 from the FRED DGS values of that date (`rab/data/fred/`) vs V0 from H1; report the largest absolute difference.
A5. Figure `fig_cost_of_certainty.png`: V0 over time (monthly first-date values), lines at $300,000 and at V0(D),
the pre-1962 part drawn dashed and labelled "flat curve at the 10-year rate", annotations for D and for the 2020 peak.

## 4. Part B: start-year backtest

Start years Y = 1872 .. 2020 (149 windows; 1872 is the first year with every input, 2020 the last whose 2033-analog
curve, Y+6, exists). Year labels: Y plays 2027, Y+1 plays 2028, Y+4 plays 2031, Y+6 plays 2033.

B1. **Ladder cost on the deposit day.** Curve c_Y = H4 row Y. tau_k = (15 Nov of (2031+k) - 1 Jan 2027) / 365.25,
k = 1..10. Rung cost R_k = 50,000 x DF_Y(tau_k); C_Y = sum_k R_k.
B2. **2027 purchase, longest first.** Money M = 300,000. For k = 10 down to 1: buy fraction
f_k = min(1, M_remaining / R_k) of rung k; M_remaining -= f_k R_k. Leftover L = M_remaining (0 if any f_k < 1).
Unbought fraction u_k = 1 - f_k. Leftover rate r1: the 1 Yr yield of c_Y / 100 if present, else `us_bill` of year Y;
leftover value on 1 Jan Y+1 = L (1 + r1).
B3. **2028 deposit completes the ladder.** Curve c_{Y+1} = H4 row Y+1; tau'_k = (15 Nov of (2031+k) - 1 Jan 2028) / 365.25.
Top-up T = sum_k u_k x 50,000 x DF_{Y+1}(tau'_k). Growth money G = L (1 + r1) + 150,000 - T.
If G < 0: payments short by S = -G (1 Jan Y+1 dollars), F = 0, fund = 0 (every output below is then 0). Else S = 0.
B4. **Floor** (E6 / M1 F convention): y5 = 5-year par yield of c_{Y+1} / 100 (linear interpolation over the tenors present;
flat curve -> GS10). Floor cost Cf = 150,000 / (1 + y5)^5. If G >= Cf: floor face F = 150,000 and fund0 = G - Cf. Else
F = G (1 + y5)^5 and fund0 = 0. **IPS-wording variant** (inventory F4): face F' = 150,000 - T (floor repays the whole
remainder of the deposit after the top-up), fund0' = G - F' / (1 + y5)^5 (if negative: F' = G (1 + y5)^5, fund0' = 0).
The two differ only when T > 0.
B5. **Branch.** fund0 bought on 1 Jan Y+1 in the equity series e (base: `world_eq`; variant: `us_eq`), never traded:
fund31 = fund0 x prod_{t=Y+1}^{Y+3} (1 + e_t); fund33 = fund0 x prod_{t=Y+1}^{Y+5} (1 + e_t).
B6. **2031 range and 2033 gift.** bottom = F; top = F + fund31 / 2; gift = F + min(fund33, fund31) / 2;
kept = fund33 - min(fund33, fund31) / 2; total T33 = F + fund33; top_reached = (fund33 >= fund31).
B7. **Real terms.** Deflator from 1 Jan Y to 1 Jan Y+6: I = prod_{t=Y}^{Y+5} (1 + cpi_infl_t). Real gift = gift / I,
real T33 = T33 / I (start-of-Y dollars, i.e. "2027 dollars").
B8. **Three views** (every output is produced for each):
- `hist`: B1-B7 as written (history's yields and history's returns).
- `today_yields`: C, T and the floor from today's curve instead: C = `laura.ladder.cost_2027_strips` (292,418.11),
  L = 7,581.89, r1 = 0.0459, T = 0, y5 = 0.0506 (numbers.yaml `market.par_curve`); history's returns as in B5.
  Check: fund0 = 40,736 (`laura.stock_fund_2028_usd.strips`) and Cf = 117,194 (`laura.floor_cost_2028`), to $1.
- `today_yields_rescaled`: as `today_yields`, with every return series rescaled so its mean log return over 1872-2025
  equals ln(1.07) (JPM 2026 LTCMA AC World 7.00% compound): e'_t = exp(ln(1 + e_t) - mean + ln 1.07) - 1
  (E6 [5] convention; comparison with insight_v1 H9, which used 1928-2025 and the 25 Sep curve).
B9. **Outputs.** `rab/results/M5/backtest_by_start_year.csv`: one row per (view, fund series, Y) with every quantity
above plus the curve bases of Y and Y+1. `backtest_summary.csv`: per view and fund series: worst / p10 / median /
p90 / best of gift, T33, real gift, real T33 (with the start year of the worst), share of windows with top reached,
number of windows with S > 0 and the largest S, number with T > 0 and the largest T, and the IPS-variant worst gift.
Era table (hist view, world_eq): 1872-1913, 1914-1945, 1946-1981, 1982-2020: median ladder cost, median gift, worst gift.
B10. **Figures.** `fig_m5_ladder_cost_by_start_year.png` (C_Y with lines at $300,000 and $450,000);
`fig_m5_gift_by_start_year.png` (hist view, world_eq: floor F as bars, gift as bars on top, T33 as a line; the
windows with a top-up marked).

## 5. Conventions and assumptions (state them wherever the numbers are used)

- Scale-free: deposits and payments keep today's dollar amounts in every era (the plan is proportional, so only
  yields and returns matter). No fees, taxes or commissions. STRIPS-like zero-coupon rungs (M1 A5): no coupon
  reinvestment (the WInS book's coupon risk is M1 E's topic). MODEL prices, no dealer mark-up.
- Pre-1962 curves are flat at the long rate (checked in A4); pre-1928 U.S. returns are JST's; `world_eq` uses today's
  62% U.S. weight in every year (it beat actual VT by about 1pp a year in 2009-2025; build_checks.txt).
- Annual steps: returns are calendar-year; the 2031 range uses the fund's 1 Jan Y+4 value.

## 6. Tolerances (Gate B)

Deterministic model: per-window values to $1; summary statistics to $100; shares to 0.5pp; dates identical.
Part A: V0 to $1 on the H1 days (must equal M1 G: `history.cost_2020_median` 458,828, `history.cost_max` 470,249 on
2020-08-04, `history.cheapest_since` 2002-05-28), extended-series statistics to $100.

## 7. Changelog

- **2026-09-30, Gate B (`rab/gates/gate_B_ws3.md`)**. These are clarifications only; no method or number changed.
  - A3(ii): "lowest and highest V0 since 1871" can be read over month-start observations or over every curve date.
    Both builds report both readings. Month starts: $111,249 (1 Oct 1981) and $468,154 (3 Aug 2020). Every curve
    date: $110,214 (30 Sep 1981) and $470,249 (4 Aug 2020). Quote the every-curve-date figure as "the cheapest day".
  - H1: the 11 Oct 2010 row of the Treasury file has every tenor blank. Both builds drop it.
  - The insight_v1 H9 reconciliation (U.S. stocks, starts 1928-2020, rescaled over 1928-2025, today's yields) is a
    reference-build extra, not part of this spec. Gate B recomputed it separately and it matches to the cent.
