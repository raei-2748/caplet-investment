# M2 spec: rate paths to January 2027 (and January 2028)

WS4, 2026-09-30 (Sydney). AI-generated research specification (Claude Code) for Team Caplet; no deliverable text.

**Purpose.** An exact, implementation-independent recipe. A blind builder who reads only this file and the raw inputs
in section 1 must reproduce every M2 probability to within 2 percentage points and every dollar figure to within $500
(Gate B). No results are printed here on purpose. The reference implementation is `rab/models/m2_rate_paths.py`; a
blind builder must not read it. Strategy is not reopened (RUN_PLAN s0).

**Question.** Laura's $300,000 arrives on 1 January 2027 and buys the ten dated holdings (numbers.yaml headline
basis: zero-coupon ladder maturing 15 November of the year before each $50,000 payment). On the 28 Sep 2026 curve that
ladder costs $292,418 on 1 Jan 2027 (`laura.ladder.cost_2027_strips`). **What is the chance it costs more than
$300,000 on the purchase day?** And, secondarily, what do rate moves to January 2028 (when the $150,000 deposit buys
the floor and the stock fund) do to the money left for the stock fund? Reconcile with insight_v1's "about 1 in 3".

**Pre-registered headline rule (written before any estimator was run).** The headline probability is the **median
of the five estimators E1-E5** in section 5, each on the "no-view" pricing convention RW (section 3). It is quoted as
"about 1 in N", N = the integer nearest to 1 / P. The range quoted with it is the minimum and maximum of E1-E5.
Everything else (the D1 reproduction, forward-convention variants, raw history, other samples) is a sensitivity or
a reconciliation row, never the headline. Reason for a median of five: the answer depends mostly on how volatile
rates will be for three months, which no single method can know; five methods that take volatility and curve shape
from different places (long history rescaled to today, history at similar yield levels, a fitted one-factor rate
model, a fitted three-factor curve model, and the options market) bracket it, and the median is robust to one of
them being off.

---

## 1. Inputs (paths relative to the worktree root)

| Id | File | What it is |
|---|---|---|
| I1 | `rab/data/treasury_par_2000_2026/<year>.csv`, `rab/data/treasury_par_1990_1999/<year>.csv` | U.S. Treasury Daily Par Yield Curve, 2 Jan 1990 - 28 Sep 2026, percent (semiannual bond-equivalent). Rows are in reverse date order in some files; sort by date |
| I2 | `rab/data/fred/DGS1MO.csv, DGS3MO, DGS6MO, DGS1, DGS2, DGS3, DGS5, DGS7, DGS10, DGS20, DGS30` | FRED constant-maturity yields (same concept as I1), used **only for dates before 2 Jan 1990**. "." or blank = missing |
| I3 | `rab/data/m2/MOVE_yahoo_daily.csv` | ICE BofA MOVE index, daily close, 12 Nov 2002 - 29 Sep 2026, Yahoo Finance `^MOVE` (secondary source; ICE owns the index). Column `Close` |
| I4 | `rab/numbers.yaml` (LOCKED, sha256 in `rab/numbers.lock`) | Cross-checks only: `laura.ladder.cost_2027_strips` ($292,418.11), `laura.ladder.breakeven_fall_bp_strips` (26.2), `laura.stock_fund_2028_usd.strips` ($40,736), `laura.floor_cost_2028` ($117,194), `ref.H6.gap_odds_28sep`, `ref.H13`, `ref.H14` |
| I5 | `research/insight_v1/scripts/data/D3/treasury_par_2026_raw.csv`, `research/insight_v1/scripts/data/D3/fred_DGS10.csv` | insight_v1's own inputs, used only to reproduce its 25 Sep figures in the reconciliation (section 7) |

## 2. Dates and constants

- Reference date **D = 2026-09-28** (the locked curve; the row `09/28/2026` of I1 is the reference curve **R**).
  The code takes `--curve-date` so it can be re-run on Friday's curve; every date below moves with D.
- Purchase date **A = 2027-01-01** (the deposit date; the valuation date of the locked forward cost). Horizon
  h = A - D = **95 calendar days**. Business-day horizon n_h = number of weekdays strictly after D and strictly
  before A, excluding U.S. bond-market holidays on which Treasury publishes no curve (in 2026: 12 Oct, 11 Nov,
  26 Nov, 25 Dec). For D = 28 Sep 2026, **n_h = 64**. (Sensitivity: purchase on Mon 4 Jan 2027, h = 98, n_h = 65.)
- Second-deposit date **B = 2028-01-01**; h2 = B - D = 460 calendar days.
- Payment dates (Nov-15 basis): P_Y = 15 Nov (Y - 1) for Y = 2033, ..., 2042; $50,000 each. Deposits $300,000 (A),
  $150,000 (B). Seed **20260930**.

## 3. Curve, cost and the two pricing conventions

**3.1 Curve (M1 "D1 method", unchanged).** From a par vector (tenor -> percent) and a valuation date v: tenors in
years 1 Mo = 1/12, 2 Mo = 2/12, 3 Mo = 0.25, 6 Mo = 0.5, 1 Yr = 1, 2 Yr = 2, 3 Yr = 3, 5 Yr = 5, 7 Yr = 7, 10 Yr = 10,
20 Yr = 20, 30 Yr = 30 ("1.5 Month" and "4 Mo" are not used; blanks skipped). Par grid t_j = 0.5j, j = 1..60, by
linear interpolation of the available (tenor, par/100) points, flat outside. Bootstrap DF_1 = 1/(1 + p_1/2),
DF_j = (1 - (p_j/2) sum_{i<j} DF_i)/(1 + p_j/2). DF(d) = exp(L(tau)), tau = (d - v) days / 365.25, L = linear
interpolation of (0, 0), (t_j, ln DF_j), flat beyond 30y. Implementations must match M1's `Curve` to 1e-10.

**3.2 Ladder cost functions** for a par vector c:
- **RW ("yields unchanged", no view; PRIMARY):** the curve on the purchase day is c, valued at A:
  Cost_RW(c) = sum_Y 50,000 x DF_{c,v=A}(P_Y).
- **FWD ("forward rates come true"; the basis of the locked 26.2bp headroom and of insight_v1 D1):** c is today's curve
  shocked today and carried at its own short rate: Cost_FWD(c) = [sum_Y 50,000 x DF_{c,v=D}(P_Y)] / DF_{c,v=D}(A).
- Cost_FWD(R) must equal $292,418.11 (I4). Cost_RW(R) is the "yields unchanged" cost; it is higher when the curve
  slopes up, because on 1 Jan 2027 each bond is three months shorter and rolls down to a lower yield.
- Gap = Cost - 300,000. **The event is Gap > 0.** Break-even parallel fall b*_conv: the parallel shift b (bp, added
  to every par tenor of R) with Cost_conv(R + b) = 300,000; report -b* (a positive number of bp) to 0.01bp.
- A scenario is a change vector Delta at the 12 tenors of R; the scenario curve is c = R + Delta (percent).
  A parallel shift b adds b to all 12 tenors.

**3.3 Ladder yield (the one-number summary of the curve used by E1, E3, E5).** For any date d with a par curve,
V(d) = sum_Y 50,000 x DF_{d,v=d}(d + (P_Y - D)) (same time to maturity as on D). The ladder yield y(d) (percent) solves
V(d) = sum_Y 50,000 x (1 + y/200)^(-2 tau_Y), tau_Y = (P_Y - D)/365.25 (solve to 1e-10). Daily changes
dy_t = y(t) - y(t-1) between consecutive panel dates, in bp. Report the ratio d y(R + b)/d b at b = 0 (expected ~1).

## 4. The daily curve panel (1962-2026)

- From 2 Jan 1990 to D: I1 rows (tenors as in 3.1).
- Before 2 Jan 1990: I2, mapped DGS1MO -> 1 Mo, DGS3MO -> 3 Mo, DGS6MO -> 6 Mo, DGS1 -> 1 Yr, DGS2 -> 2 Yr, DGS3 -> 3 Yr,
  DGS5 -> 5 Yr, DGS7 -> 7 Yr, DGS10 -> 10 Yr, DGS20 -> 20 Yr, DGS30 -> 30 Yr, on the union of their dates.
- Keep a date only if 1 Yr, 5 Yr and 10 Yr are all present.
- **par_d(t)**: the linear interpolation of date d's available tenors at t (flat outside) - the same rule as 3.1.
  Change vectors between two dates are always taken at the 12 tenors of R using par_d(t).
- Check (report): on the 1990-2026 overlap, max |FRED DGS10 - I1 10 Yr| over common dates.

**EWMA volatility (used by E1 and the 15-month section).** On the panel's daily ladder-yield changes dy_t (bp):
sigma2_t = 0.97 x sigma2_{t-1} + 0.03 x dy_t^2, initialised at t = 60 with the mean of dy_1^2 ... dy_60^2 (zero-mean
variance). sigma_t = sqrt(sigma2_t) includes the change into t. sigma_D is today's value. Report annualised x sqrt(252).

**Windows.** A window starts on a panel date s with at least 250 earlier daily changes and s + h <= D. Its end e(s) is
the last panel date on or before s + h (calendar days). Delta_s = par_{e(s)} - par_s at the 12 tenors (percent).
Windows overlap (one per start date).

## 5. The five headline estimators (all RW convention, Nov-15 basis, horizon A)

Each estimator produces a sample of scenario curves c = R + Delta (equal weights); P = share with Cost_RW(c) > 300,000.

**E1. History rescaled to today's volatility (filtered historical simulation), 1962+.** All windows. Scale:
k_s = sigma_D / sigma_s; Delta'_s = k_s x Delta_s (all tenors by the same factor). Demean: subtract the mean of
Delta' over all windows, tenor by tenor ("no view on direction").

**E2. History at similar yield levels, 1962+.** Windows whose 10 Yr par at s is between 4.00% and 6.50% inclusive
(today 5.24%). No scaling. Demean over these windows, tenor by tenor.

**E3. One-factor Vasicek (AR(1)) on the ladder yield, 1962+, fitted with statsmodels.**
1. Fit y_t = c + phi y_{t-1} + e_t by OLS on the whole panel series y (one step = one panel date; statsmodels
   `AutoReg(y, lags=1, trend="c")`). Keep c_hat, phi_hat, residual sd s_e (ddof = number of parameters, i.e.
   statsmodels `sigma2`), the 2x2 parameter covariance, n = number of observations used.
2. Small-sample bias correction (Kendall 1954; Marriott and Pope 1954): phi_bc = min(1, phi_hat + (1 + 3 phi_hat)/n);
   theta = c_hat / (1 - phi_hat) (the long-run level, kept); c_bc = theta (1 - phi_bc).
3. Vasicek reading (report): kappa = -ln(phi) x 252 per year, half-life = ln 2 / kappa years, sigma = s_e x sqrt(252)
   (bp/yr, the instantaneous volatility to first order), theta.
4. Predictive sample with parameter uncertainty: M = 100,000 draws of (c, phi) ~ Normal((c_bc, phi_bc), covariance
   from step 1); where phi >= 1 set phi = 1 and c = 0 (random walk). For each draw, the n_h-step change of y is
   Normal(mean m, variance v): m = (c - (1 - phi) y_D) x (1 - phi^n_h)/(1 - phi) (this equals
   (theta_k - y_D)(1 - phi^n_h) with theta_k = c/(1 - phi), written so it stays finite as phi -> 1; m = 0 if phi = 1),
   v = s_e^2 (1 - phi^(2 n_h))/(1 - phi^2) (v = n_h s_e^2 if phi = 1). Draw one change per parameter draw.
   The scenario is a **parallel shift** of R by that change.
5. Also report (not headline): plug-in P at (c_hat, phi_hat) and at (c_bc, phi_bc); the same fit on the 1990+ and
   2000+ sub-panels (theta, kappa, half-life, plug-in P); and the ADF unit-root test (statsmodels `adfuller`,
   regression "c", autolag "AIC") p-value for each sample.

**E4. Three-factor curve model: principal components + VAR(1), 1990+, fitted with statsmodels.**
1. Panel 2 Jan 1990 - D; K = 10 fixed tenors {0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30} years, Y_t(k) = par_t(k).
2. PCA: eigenvectors of the sample covariance (ddof = 1) of the daily changes dY_t; loadings L = the 3 largest (K x 3).
   Report the variance share of each. Scores F_t = (Y_t - mean Y) L. Residual U_t = (Y_t - mean Y) - F_t L'.
3. statsmodels `VAR(F).fit(1, trend="c")`. n_h-step forecast mean mu = forecast from F_D; covariance S = the
   n_h-step forecast MSE (`forecast_cov`).
4. Draws (N = 100,000): F_h ~ Normal(mu, S); residual change dU ~ Normal(0, n_h x Cov(dU_t)) (sample covariance,
   ddof = 1, of the daily residual changes). Delta at the K tenors = (F_h - F_D) L' + dU. Delta at the 12 tenors of R
   by linear interpolation on K (flat below 0.25y).
5. Also report (not headline): the random-walk version, F_h - F_D ~ Normal(0, n_h x Cov(dF_t)), plus dU as above.

**E5. The options market's volatility (MOVE), calibrated to the ladder.**
1. MOVE_s = I3 `Close` on s (else the last earlier close). For every window start s with MOVE_s available:
   realised volatility RV_s = sqrt(252 x mean of dy_t^2 over the panel dates t in (s, e(s)]) (bp/yr).
2. rho = median over those windows of RV_s / MOVE_s (report quartiles).
3. sigma_h = rho x MOVE_D x sqrt(n_h / 252) bp; MOVE_D = close on D. Draws N = 100,000 of a parallel shift
   b ~ Normal(0, sigma_h^2).
4. Also report (not headline): rho = 1 (MOVE as is), and rho at its quartiles.

**Seeds.** One numpy `default_rng` per stochastic step, seeded `[20260930, k]` with k = 3 (E3), 4 (E4), 44 (E4-RW),
5 (E5), 9 (bootstrap). Monte Carlo noise (~0.15pp) is inside the Gate B tolerance.

**Headline.** P = median(E1..E5), quoted as above. Tag: laura_plan, MODEL, curve date D, valuation date A,
Nov-15 STRIPS basis.

## 6. Outputs per estimator (and for every reported variant)

P(Gap > 0); P(Gap > $5,000); P(Gap > $10,000); P(Gap > cost of the 2033 rung, i.e. at least one whole payment waits);
mean Gap given Gap > 0; Gap at the 90th, 95th and 99th percentiles (0 if below); Cost at the 5th/50th/95th
percentiles; number of scenarios (for E1/E2 also the number of non-overlapping windows, floor(count / n_h)).
For E1 and E2 a 90% interval for P from a moving-block bootstrap over window start order: 1,000 replicates,
block length n_h windows, ceil(count/n_h) blocks per replicate, Delta held as computed (no re-demeaning).
Also the same P for E1, E2 and E5 under the FWD convention (sensitivity only).

## 7. Reconciliation with insight_v1 (every row reproduced, not copied)

| Row | Method | Must reproduce |
|---|---|---|
| R1 | D1 [6] on the 25 Sep curve (I5): zero-drift lognormal around Cost_FWD, sigma = realised 2026 volatility of daily log Cost_FWD over I5's 2026 rows (ddof 1, x sqrt 252), t = (A - 25 Sep)/365.25 | 30.5% |
| R2 | Same on D (2026 rows of I1 up to D) | 24.2% (`ref.H6.gap_odds_28sep`) |
| R3 | strategy_mc_v2 (a): parallel shift Normal(0, 0.37pp), FWD, 25 Sep; and on D | 30.2% on 25 Sep |
| R4 | AX1b [C]: share of 68-trading-day windows in which FRED DGS10 fell by at least X bp, since 1962 / 1990 / 2000, X = 19 (25 Sep headroom) and 26 (28 Sep); with I5's DGS10 | 26bp: 27.6% / 31.1% / 28.5% |
| R5 | R2 but RW centre: P(Cost > 300,000) = 1 - Phi(ln(300,000 / Cost_RW(R)) / (sigma sqrt t)), same sigma and t as R2 | new |
| R6 | Headline (median E1-E5) | new |

Waterfall (report): "1 in 3" (R1, 25 Sep) -> R2 (curve moved to 28 Sep: headroom 19 -> 26bp) -> R5 (no-view centre
instead of forward rates) -> R6 (volatility and curve shape from the five estimators instead of 2026's average).

## 8. Fifteen-month section (secondary; rate moves to 1 Jan 2028)

For every window start s with s + h2 <= D (same burn-in): e1 = last panel date <= s + h, e2 = last panel date <= s + h2;
Delta1 = par_{e1} - par_s, Delta2 = par_{e2} - par_s (12 tenors). Variants: **H-FHS** (both scaled by k_s = sigma_D /
sigma_s, then each demeaned over all windows), **H-LVL** (10 Yr at s in [4.00, 6.50]%, each demeaned over those
windows), **H-RAW** (all windows, no scaling, no demeaning). For each window, with c1 = R + Delta1 (1 Jan 2027) and
c2 = R + Delta2 (1 Jan 2028), RW convention on both dates:
1. Cost_1 = Cost_RW(c1). If Cost_1 <= 300,000: leftover = 300,000 - Cost_1, grown to B at (1 + y1(c1)), y1 = the
   1 Yr par of c1 (annual compounding, E6 convention); top-up T = 0.
2. If Cost_1 > 300,000: longest first - buy whole rungs 2042, 2041, ... at c1 prices (rung cost 50,000 x
   DF_{c1,v=A}(P_Y)) while money lasts, then the fraction of the next rung the rest buys. The unbought fractions f_Y
   are bought on B: T = sum_Y f_Y x 50,000 x DF_{c2,v=B}(P_Y). Leftover 0.
3. Money on B: G = 150,000 + leftover x (1 + y1(c1)) - T. Floor cost F = 150,000 / (1 + y5(c2))^5, y5 = the 5 Yr par
   of c2 (annual compounding, E6 / M1 F convention). Stock fund S = max(0, G - F); floor face = 150,000 if G >= F,
   else G x (1 + y5)^5.
Outputs per variant: S at p5/p50/p95; P(S < $20,000); P(S = 0); P(T > 0); mean T given T > 0; F at p5/p50/p95.
Check: with Delta1 = Delta2 = 0 and the FWD convention in step 1 (leftover = 300,000 - Cost_FWD(R)), S must equal
$40,736 (`laura.stock_fund_2028_usd.strips`) and F $117,194 (`laura.floor_cost_2028`); report the RW base too.

**Re-check of the WS4-owned references (28 Sep curve, FWD convention as D1/E6).**
- H13 (E6 [8]): parallel falls b = -50, -100, -150bp before A. Gap(b) = Cost_FWD(R + b) - 300,000; top-up on B =
  max(Gap, 0) x DF_{R+b,v=D}(A) / DF_{R+b,v=D}(B); leftover 0 if Gap > 0. Five-year yield on B: (i) R's 5 Yr,
  (ii) R's 5 Yr + b. Floor, fund and floor face as in step 3.
- H14 (D1 [8]): no 2028 deposit: unfunded part of the 2033 payment = Gap / (rung cost of 2033 at A, FWD) x 50,000
  for b = -50, -100bp. Must reproduce $9,281 / $28,753.

## 9. Tolerances (Gate B)

Probabilities within 2 percentage points; dollar quantiles and means within $500; Vasicek theta within 5bp, kappa
within 0.02/yr; PCA variance shares within 0.5 point. Deterministic checks (Cost_FWD(R), break-evens, H13, H14,
the $40,736 base) to $1. A difference is explained, never averaged.

## 10. Known limits (state them wherever the numbers are used)

The event is for Laura's real ladder on the Nov-15 STRIPS basis, MODEL prices (no dealer mark-up), one purchase
day. History assumes the future resembles some mix of the past; E1 assumes today's volatility lasts three months;
E3/E4 fit daily data whose mean reversion is weak and biased (E3 corrects the AR(1) bias, E4 does not); E5 relies
on a secondary source for MOVE and on a stable MOVE-to-ladder ratio. None of this forecasts the direction of rates:
the headline takes no view on direction by construction.
