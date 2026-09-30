# M8 SPEC: which assumptions move the 2031 range (tornado + Sobol)

WS2, written 2026-09-30 (Sydney) before any M8 code was run. Implementation-independent. AI-generated research
(Claude Code) for Team Caplet; no deliverable text.

**Question.** The 2031 range is [floor, floor + half the stock fund]. Which assumptions move it most, so that the IPS
states them? Market luck is kept separate from assumptions.

## 1. The model (one path, Laura's plan, nominal U.S. dollars)

Curve: the 28 Sep 2026 par curve (`rab/data/treasury_par_2000_2026/2026.csv`, row 09/28/2026) with the D1 curve method
of `rab/models/M1_METHOD.md` A1 (a parallel shift of d basis points is added to every par yield, A1 step 5). On the
curve shifted by d, with the ten $50,000 payments on the Nov-15 basis (A2):
V0(d) = value on 28 Sep 2026; V_A(d) = V0(d) / DF_d(1 Jan 2027); V_28(d) = V0(d) / DF_d(1 Jan 2028);
ladder value on 1 January of year y: LV_y(d) = V0(d) / DF_d(1 Jan y), y = 2028..2032.
(Check: V_A(0) = 292,418.11, `laura.ladder.cost_2027_strips`.)

Rates: y1 = 0.0459 + d/10,000 (1-year par + d; the 2027 leftover earns it); y5 = max(0.001, 0.0506 + d/10,000 + e/100)
(the 5-year par on 2 Jan 2028: today's 5.06% plus the shift before 1 Jan 2027 plus e, the change during 2027, in points).

Second deposit (IPS wording, flag F4 in `rab/inventory.md`: the floor repays "the whole remainder"):
- No gap (V_A <= 300,000): leftover = 300,000 - V_A; F = 150,000; B0 = leftover (1 + y1) + 150,000 - 150,000 / (1 + y5)^5.
- Gap (V_A > 300,000): top-up T = (V_A - 300,000) V_28 / V_A (the unbought part, grown along the curve to Jan 2028);
  remainder R = max(0, 150,000 - T); F = R; B0 = R - R / (1 + y5)^5.
(Check: d = 0, e = 0 gives B0 = 40,736.19, `laura.stock_fund_2028_usd.strips`.)

Stock fund: annual log return in year y = ln(1 + mu_c) + sd_log z_y, z_y = the standardised quantile of the return
shock u_y: Phi^{-1}(u_y) if inv_nu = 0, else t^{-1}_{nu}(u_y) sqrt((nu - 2) / nu) with nu = 1 / inv_nu; z clipped to
[-5, 5]. Fees: at the start of each year y = 2028..2032, fee_y = fee x (LV_y(d) + FV_y + B), paid from the fund
(the IPS cost principle), B <- max(B - fee_y, 0) exp(return_y); FV_y = (F / (1 + y5)^5) (1 + y5)^(y - 2028) is the
floor's value. B3 = B after 2030; B5 = B after 2032. Share s = 1/2.

Outputs of one path: **Y1 = the top of the 2031 range, U = F + s B3**; the bottom F; **Y2 = the 2033 gift,
G = min(phi F + s min(B5, B3), U)** (phi = floor delivery ratio, M4 section 2).

## 2. Inputs (independent)

| Input | Distribution for Sobol | Base | Tornado low / high | Why this range |
|---|---|---|---|---|
| X1 mu_c: stock fund's compound expected return | Uniform[0.0408, 0.0800] | 0.0700 | 0.0408 / 0.0800 | Vanguard-like VT low end 4.08% (insight_v1 D2, VCMM 30 Jun 2026) to JPM AC World 7.00% plus 1 point (US history is higher still, but not a forecast) |
| X2 sd_log: sd of annual log return | Uniform[0.12, 0.20] | 0.154218 (JPM) | 0.12 / 0.20 | Shiller annual 1871-2025 0.170, Damodaran 1928-2025 0.189 (`rab/data/ws2_returns/build_report.txt`); calm decades lower |
| X3 inv_nu: tail heaviness (1/nu) | Uniform[0, 1/3] | 0 (normal) | 0 / 1/3 (nu = 3) | from thin tails to very fat tails |
| X4 d: curve shift 28 Sep 2026 -> 1 Jan 2027 (bp) | empirical: 95-calendar-day changes of the 10-year CMT (FRED DGS10), every business day from 2 Jan 1990 with an end value; u -> empirical quantile | 0 | 2.5th / 97.5th percentile | the actual history of 3-month moves |
| X5 e: 5-year yield change during 2027 (points) | empirical: 365-day changes of the 5-year CMT (FRED DGS5), same window | 0 | 2.5th / 97.5th percentile | the actual history of 1-year moves |
| X6 fee: yearly cost on all assets, paid from the fund | Uniform[0, 0.010] | 0 | 0 / 0.010 | none to a full advisory fee |
| X7 phi: floor delivery ratio (Y2 only) | Uniform[0.9755, 1.0] | 1.0 | 0.9755 / 1.0 | M4 section 2 (r = 0 to full reinvestment) |
| u1..u5: market luck 2028..2032 | Uniform(0, 1) each | median | - | not an assumption |

Empirical quantile: numpy percentile with linear interpolation at 100u. FRED files: `rab/data/fred/DGS10.csv`,
`rab/data/fred/DGS5.csv`.

## 3. Analyses (`rab/results/M8/`)

1. **Tornado** (`tornado.csv`, `fig_M8_tornado.png`): each of X1..X7 set to its low and its high value, all others at
   base; over 200,000 common luck paths (u1..u5, seed 20260930) report the median and the 5th percentile of Y1 and the
   median of Y2. Sort by the swing of the median Y1. Two reference bars, labelled as not assumptions: the decision
   lever s = 1/3 vs 2/3, and the return-model choice (range of the median 2031 top across M3's L, T, BOOT, BAYES).
2. **Sobol A, luck included** (`sobol_A_top2031.csv`, `sobol_A_gift2033.csv`): SALib Sobol sampling (Saltelli scheme,
   calc_second_order = False), N = 2^14, seed 20260930. Y1 over (X1..X6, u1..u3); Y2 over (X1..X7, u1..u5). First-order
   S1 and total ST with 95% bootstrap intervals. Answers: how much of the uncertainty is luck, how much assumptions.
3. **Sobol B, assumptions only** (`sobol_B.csv`, `fig_M8_sobol.png`): the median and the 5th percentile of Y1 over a
   fixed set of 4,000 luck paths (seed 20260930), as functions of X1..X6; N = 2^12. Answers: which assumptions move the
   typical and the bad-case 2031 top.
4. **The three assumptions the IPS must state** (pre-registered rule): the three inputs with the largest ST in Sobol B
   for the median Y1; cross-checked against the p5 ranking and the tornado. Disagreements are reported, not resolved
   by hand.
5. `floor_reading.csv`: the floor F and fund B0 under the IPS reading ("whole remainder") and the insight_v1 E6
   reading ($150,000 face kept, fund absorbs the top-up) for d = 0, -50, -100 bp (e = 0).
6. `input_ranges.csv`: the realised low/high of X4 and X5 from the data.

## 4. Tolerances (Gate B)

Base checks exact (V_A(0), B0). Tornado medians within 1%. Sobol ST within 0.05 or the published 95% interval; the
top-3 list identical.

## 5. References (DOIs checked on Crossref, 30 Sep 2026)

- Sobol', I. M. (2001). Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates.
  Math. Comput. Simul. 55(1-3), 271-280. doi:10.1016/S0378-4754(00)00270-6
- Saltelli, A., Annoni, P., Azzini, I., Campolongo, F., Ratto, M., & Tarantola, S. (2010). Variance based sensitivity
  analysis of model output. Comput. Phys. Commun. 181(2), 259-270. doi:10.1016/j.cpc.2009.09.018
- Herman, J., & Usher, W. (2017). SALib: An open-source Python library for sensitivity analysis. JOSS 2(9), 97.
  doi:10.21105/joss.00097

## 6. Gate B clarifications (30 Sep 2026; sections 1-5 unchanged)

- C1. "How much is luck" can be summarised two ways from the same Sobol A indices. The sum of S1 over u1..u3 is 0.17
  for the 2031 top; the sum of ST is 0.22. Both builds give identical values under each definition. The blind build
  quoted S1 and the primary ST. Quote "about a fifth" and name the index used.
