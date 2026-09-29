# M6 spec: rivals on the same metrics, and the branch-fund choice (pre-registered switch rule)

WS3, 2026-09-30 (Sydney). AI-generated research specification (Claude Code) for Team Caplet; no deliverable text.
Implementation-independent; the reference code `rab/models/m6_rivals.py` must not be read by a blind builder.
The switch rule in section 5 was written before any M6 number was computed and is not changed after.
Strategy is not reopened (RUN_PLAN s0): rivals are yardsticks; any finding against the IPS is triaged, not applied.

## 0. Questions

A. How do the rivals a judge will think of (all-bond, 60/40, a glide path, CPPI, a TIPS ladder) compare with the adopted
   plan (REC = Root-and-Branch) on the **same** metrics, in history and under one set of forward assumptions?
B. Should the branch fund be something other than VT (VTI+VXUS, U.S. only, a small/value tilt, gold/REIT added)?

## 1. Inputs

`rab/data/history/annual_history.csv`, `soy_curves.csv` (M5 inputs, same meaning), `jpm_ltcma_2026_usd.csv`,
`jpm_ltcma_2026_corr.csv` (J.P. Morgan 2026 LTCMA, U.S. dollar, data as of 30 Sep 2025, repo PDF page 2),
`market_inflation_2026-09.csv` (FRED breakevens and TIPS real yields), `rab/numbers.yaml` (`market.par_curve`,
`laura.ladder.cost_2027_strips`, `laura.floor_cost_2028`, `laura.stock_fund_2028_usd.strips`).
Curve method, tau conventions, `C_Y`, rung costs, leftover rate r1 and floor cost convention: M5_SPEC.md sections 2 and B1-B4.

## 2. Common frame (every rival)

Deposits 300,000 on 1 Jan Y (2027) and 150,000 on 1 Jan Y+1 (2028). Ten payments of 50,000 on 1 Jan Y+6 .. Y+15,
each met by a zero-coupon Treasury maturing 15 Nov of the year before (M1 A5). On 1 Jan Y+6 (2033) the operating
reserve is set aside: a rival that already holds the ladder uses it; any other rival buys it then at
`reserve33 = 50,000 + sum_{k=2..10} 50,000 x DF_{Y+6}(tau33_k)`, tau33_k = (15 Nov of (2031+k) - 1 Jan 2033)/365.25
(the 2033 payment itself is due that day).

**Metrics (the same for all):**
- `unfunded`: share of windows / paths where the money on 1 Jan Y+6 cannot buy the reserve (a payment is short), and
  the largest shortfall.
- `T33`: money for the facility and flexibility on 1 Jan Y+6 = all assets minus the reserve (ladder rivals: all
  non-ladder assets). Reported worst / p10 / median (history) and p5 / p50 / p95 (MC). Negative = unfunded.
- `certain31`: what can be promised in 2031 with certainty by construction = face value of Treasuries already held
  that mature by 1 Jan Y+6 and are not needed for the payments (0 for rivals that hold no such Treasuries).
- `gift`: the adopted announcement rule applied to each rival: bottom = certain31; uncertain part U31 =
  max(0, surplus31 - PV31(bottom)) where surplus31 = assets on 1 Jan Y+4 minus the value of whatever still has to fund
  the payments (the reserve at 1 Jan Y+4 prices for rivals without a ladder: 50,000 x sum_k DF_{Y+4}(tau31_k),
  tau31_k = (15 Nov of (2031+k) - 1 Jan 2031)/365.25; 0 for ladder rivals); top = bottom + U31/2;
  gift = bottom + min(max(U33, 0), U31)/2 where U33 = T33 - bottom; if T33 < bottom, gift = max(T33, 0).
  For REC this is exactly M5 B6.
- `real_T33` (history only): T33 / prod_{t=Y}^{Y+5}(1 + cpi_infl_t).
- `trades`: number of trades 2027-2033 implied by the rule (section 3), counted, not simulated.

## 3. Rivals

Bond sleeve ("Treasury fund") return b_t: history = 0.5 `us_bill` + 0.5 `us_bond10` (the D3/E6 proxy);
MC = JPM U.S. Intermediate Treasuries with its compound return reset to today's 5-year par yield (section 4).
Equity e_t: history `world_eq`; MC AC World. Rebalancing = back to target weights every 1 Jan.

| Id | Rival | Rule |
|---|---|---|
| REC | Root-and-Branch (adopted) | M5 B1-B6 (floor face 150,000; VT fund never traded) |
| R1 | All-Treasury ("all-bond") | REC's 2027 ladder and 2028 top-up; all of G buys the 5-year floor: face G (1+y5)^5. certain31 = that face |
| R2 | 60/40, whole portfolio | 300,000 on 1 Jan Y and 150,000 on 1 Jan Y+1 in 60% e / 40% b, rebalanced yearly; reserve bought on 1 Jan Y+6 |
| R3 | Ladder + 60/40 growth money | REC's 2027 ladder and top-up; G in 60/40 rebalanced yearly to Y+6; no floor (certain31 = 0) |
| R4 | Glide path, whole portfolio | equity share 65, 60, 50, 40, 30, 20% on 1 Jan Y..Y+5 (insight_v1 E7 firm A), rest b; reserve bought on 1 Jan Y+6 |
| R4b | Growth-first, whole portfolio | equity 75, 75, 75, 75, 60, 40% (insight_v1 E7 firm B, `strategy_mc.py` default); MC also with a 2028 deposit of 75,000 and 0 (re-verifies ref H16: share of paths where the money cannot buy the reserve) |
| R5 | CPPI, whole portfolio | floor_t = 50,000 x sum_k DF_t(tau_k(t)) + 150,000 x DF_t((1 Jan 2033 - 1 Jan (2027+t'))/365.25) on the curve of year t (t' = t - Y), future deposits not counted. Each 1 Jan t = Y..Y+5 (after any deposit): cushion C = A - floor_t; stocks E = min(A, m max(C, 0)); the rest S = A - E in zeros with the floor's cash flows (pro rata). A_{t+1} = E (1 + e_t) + S x floor^{same flows}_{t+1} / floor_t. m = 3 (base) and 5. Promised bottom = 150,000; certain31 = 0 (a CPPI floor can be broken by a jump) |
| R6 | TIPS ladder | 2027: rungs of TIPS sized to pay 50,000 if inflation equals today's breakeven b_k, same cost as REC's ladder (assumption: no inflation-risk or liquidity premium); nominal paid at payment k = 50,000 x max(1, I_k) / (1 + b_k)^{n_k}, I_k = CPI growth from 1 Jan Y to 1 Jan (Y+5+k), n_k = years from 1 Jan 2027 to 1 Jan (2032+k). 2028: as REC. A payment is short when paid < 50,000; the gap is met from kept money |

For R5 the floor's own-cash-flow growth is floor_{t+1}/floor_t with both valued on their year's curve (the zeros held).
R6 breakeven b_k (annual): b(n) = (1 + y_nom(n)) / (1 + r_real(n)) - 1 with y_nom = today's par yield at n years
(linear in the par curve) and r_real = FRED DFII5/7/10/20/30 (25 Sep 2026) interpolated linearly in n (flat below 5y).
Trades: REC 13 (10 rungs, T-bill, floor, VT); R1 12; R2 2 + 2 + 2x5 + 10 = 24; R3 10 + 1 + 2 + 2x4 = 21; R4, R4b 24;
R5 up to 12 a year x 6 = 72; R6 as REC (13).

## 4. The two lenses

**History lens.** Start years Y = 1872..2020 (M5 windows), history's yields and returns, as M5 `hist` (every rival,
its curves on 1 Jan Y .. Y+6 from `soy_curves.csv`). R6 is scored only on delivery: today's TIPS ladder (today's
breakevens) under each historical inflation path, Y = 1872..2011 (needs CPI to Y+14); its T33 equals REC's by
construction (same cost, same 2028 step).

**MC lens (JPM 2026 LTCMA).** 200,000 paths, 6 annual steps (2027..2032), seed 20260930, numpy default_rng.
Each asset i: log return ~ Normal(mu_i, s_i^2), mu_i = ln(1 + compound_i), s_i = sqrt(2 ln((1 + arith_i)/(1 + compound_i)))
(E6/D6 `lp` fit); correlations = JPM matrix entries applied to the normal shocks (nearest positive-definite matrix by
eigenvalue clipping at 1e-8 and rescaling to unit diagonal, if needed). Assets: AC World, U.S. Large Cap, EAFE,
Emerging Markets Equity, U.S. Small Cap, U.S. Equity Value Factor, U.S. REITs, Gold, U.S. Intermediate Treasuries,
U.S. Inflation. Overrides (ASSUMPTION, market-consistent, as E6 did with 5.00% on the 25 Sep curve): Intermediate
Treasuries compound = 5.06% (today's 5-year par), arithmetic = 5.06% + (4.06% - 4.00%).
Rates in the MC lens: yield change in year t = -(b_t - 0.0506) / 5 (duration 5); cumulative change dy(t) shifts every
continuously compounded zero rate of today's curve rolled forward (DF_fwd(date, tau) x exp(-dy x tau)). Used for:
REC/R1/R3 floor rate y5 = max(0.001, 0.0506 + dy(1)) (floor at 1 Jan 2028, annual compounding as M5 B4); R2/R4 reserve33 and
surplus31; R5 floor_t. REC ladder = `laura.ladder.cost_2027_strips` (no rate risk before 2027: that is WS4's M2).
Leftover rate 0.0459. R6 inflation: AR(1) on annual CPI, pi_t = mu + phi (pi_{t-1} - mu) + eps_t, eps ~ Normal(0, s^2) independent of the
asset shocks (its own stream: default_rng(20260936), one standard normal per path per year, years in order); phi and s from OLS of `cpi_infl`_t on `cpi_infl`_{t-1}, t = 1953..2025 (s = residual sd with 2 degrees of
freedom removed); mu = the 10-year breakeven (T10YIE, 28 Sep 2026); pi_0 = CPI Aug 2026 / CPI Aug 2025 - 1 (FRED
CPIAUCNS); pi_2027 .. pi_2041 simulated (15 years).

## 5. Branch-fund alternatives (Part B) and the pre-registered switch rule

REC with everything fixed except the fund (E6 convention: fund0 = `laura.stock_fund_2028_usd.strips` = 40,736,
floor 150,000 at y5 = 5.06%). Bought 1 Jan 2028, **buy-and-hold, never rebalanced**:

| Id | Fund | MC weights (JPM) | History weights |
|---|---|---|---|
| A0 | VT (baseline) | 100% AC World | 100% `world_eq` |
| A1 | VTI + VXUS 62/38 | 62% U.S. LC + 28.5% EAFE + 9.5% EM | 62% `us_mkt_kf` + 38% (`world_eq` - 0.62 `us_eq`)/0.38 |
| A2 | U.S. only (VTI) | 100% U.S. LC | 100% `us_mkt_kf` |
| A3 | VT + small/value tilt | 70% AC World + 15% U.S. Small + 15% U.S. Value Factor | 70% `world_eq` + 30% `us_smallval` |
| A4 | VT + gold/REIT | 80% AC World + 10% Gold + 10% U.S. REITs | 80% `world_eq` + 10% `gold` + 10% `housing` (home prices: REIT history unavailable, flagged) |

History windows Y = 1928..2020 (93; all series exist), today's yields (M5 `today_yields`). ETF lens: actual fund total
returns (`*_etf` columns; A3 skipped: no small-value ETF series here; A4 = 80% VT + 10% GLD + 10% VNQ; A1 = 62% VTI +
38% VXUS), 5-year windows Y+1..Y+5 inside 2012..2025 (Y = 2011..2020, 10 windows; VXUS has no 2011 return).
Metrics: gift p5/p50/p95, spread90 = p95 - p5, P(top reached), median range width (fund31 / 2), T33 p5/p50.
History: gift worst / p10 / median / p90, spread80 = p90 - p10.

**Switch rule (pre-registered).** Replace VT by alternative A only if all hold:
1. Benefit (MC lens): gift p5(A) >= gift p5(A0) + 2,000, **or** spread90(A) <= 0.90 x spread90(A0).
2. Same direction in history: for the p5 test, history p10(A) >= p10(A0) + 1,000; for the spread test,
   spread80(A) <= 0.95 x spread80(A0).
3. Median not cut: MC median gift(A) >= median(A0) - 500 **and** history median(A) >= median(A0) - 1,000.
4. One sentence: a plain, true reason fits in one sentence, and WInS can hold it (each extra fund is one more $25 trade
   and one more thing to explain; listing and the $3 minimum price are checked by WS6).
Otherwise VT stays. The rule is applied mechanically; its output is recorded in `fund_choice_decision.csv`.
Section 7 applies to the rule's output too: a SWITCH counts only if the MC tests give the same answer on other seeds
(checked on 20 seeds, `fund_robustness` in the results); a result that flips with the seed is reported as not robust.

## 6. Outputs

`rab/results/M6/`: `rivals_history.csv` (per rival and window), `rivals_summary.csv` (both lenses, all metrics),
`fund_alternatives.csv`, `fund_choice_decision.csv`, `fig_m6_rivals.png` (T33 bad/typical/good and unfunded share, both
lenses), `fig_m6_fund_choice.png`, `M6_results.json`, `M6_report.txt`.

## 7. Tolerances (Gate B)

History: per-window values to $1, summaries to $100. MC: percentiles within 2% (the gate's range tolerance),
probabilities within 2pp, with any seed; decisions of the switch rule identical.

## 8. Assumptions to state wherever used

No fees, taxes or commissions (except as trade counts). i.i.d. annual lognormal returns in the MC lens (no fat tails;
WS2's M3 has them). The JPM equity assumptions are dated 30 Sep 2025. The bond proxy is an intermediate fund, not the
WInS book. The TIPS ladder cost is assumed equal to the nominal ladder's. REIT history before 2009 is not available here.

## 9. Changelog

- **2026-09-30, Gate B (`rab/gates/gate_B_ws3.md`)**. These are clarifications only. The switch rule in s5 is unchanged.
  - R5 "floor broken" means T33 < 150,000 on 1 Jan 2033, i.e. the $150,000 promise is missed. MC: 1.99% (reference)
    against 1.96% (blind). A negative cushion at some 1 Jan 2028-32 is a different, secondary statistic (blind 1.60%).
    In the history lens the promise is missed in 94 (m = 3) and 106 (m = 5) of 149 windows. The reference summary
    had read 1 because of a counting bug, fixed at Gate B. At history's yields REC's own floor is below $150,000 in
    91 of 149 windows, so only the MC lens separates the two.
  - R6 `unfunded` = at least one of the ten payments is paid below $50,000.
  - s5/s7 robustness: the spec did not fix the other seeds. The reference build used 20261930-20261949 and the blind
    build used 20260930-20260949. With the noise removed, A4's spread90 ratio is 0.8991 in both builds (100 seeds x
    200,000 paths). The s7 outcome therefore depends on the path count: at 200,000 paths A4 passes on about 80-85% of
    seeds, so it is "not robust". A future rerun should keep 200,000 paths and 20 seeds, or report the noise-free
    ratio next to the seed count.
  - `fund_choice_decision.csv` now records the rule's final output (`final`, after s7), next to the base-seed test
    (`decision_seed_20260930`).
