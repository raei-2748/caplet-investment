| Key | Primary | Blind | Diff | Tol | Verdict |
|---|---|---|---|---|---|
| `laura.rates.gap_odds_2027` (D) | 32.66% | 32.66% | +0.00pp | 2pp | MATCH |
| `gap_odds_range_min` (D) | 26.67% | 26.67% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E2 90% bootstrap low | 21.57% | 21.85% | +0.28pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;E2 90% bootstrap high | 33.16% | 32.73% | -0.43pp | 2pp | WITHIN TOL |
| `gap_odds_range_max` (D) | 33.16% | 33.16% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E1 90% bootstrap low | 29.83% | 29.83% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E1 90% bootstrap high | 36.66% | 36.66% | +0.00pp | 2pp | MATCH |
| `E3_vasicek_1962` (D) | 32.69% | 32.69% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E3 plug-in (OLS) | 31.65% | 31.65% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E3 plug-in (bias-corrected) | 32.73% | 32.73% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E3 share of draws at phi = 1 | 49.35% | 49.35% | +0.00pp | 2pp | MATCH |
| `E4_pca_var_1990` (D) | 32.21% | 32.20% | -0.00pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;E4 PCA share 1 | 78.26% | 78.26% | +0.00pp | 0.5pt | MATCH |
| &nbsp;&nbsp;E4 PCA share 2 | 12.36% | 12.36% | -0.00pp | 0.5pt | MATCH |
| &nbsp;&nbsp;E4 PCA share 3 | 5.05% | 5.05% | +0.00pp | 0.5pt | MATCH |
| &nbsp;&nbsp;E4 without mean reversion | 30.89% | 31.02% | +0.14pp | 2pp | WITHIN TOL |
| `E5_move_calibrated` (D) | 32.66% | 32.66% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;MOVE on 28 Sep | 101.8 | 101.8 | +0 | exact | MATCH |
| &nbsp;&nbsp;rho = median RV / MOVE | 0.9895 | 0.9895 | +1.05e-14 | 2% | MATCH |
| &nbsp;&nbsp;E5 with MOVE 63-day average | 27.43% | 27.43% | +0.00pp | 2pp | MATCH |
| `cost_2027_yields_unchanged` (D) | $293,401.14 | $293,401.14 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;Cost_FWD(R) (numbers.yaml $292,418.11) (D) | $292,418.11 | $292,418.11 | +0.00 | $1 | MATCH |
| `breakeven_fall_bp_yields_unchanged` (D) | 22.776bp | 22.776bp | -0.0000bp | 0.01bp | MATCH |
| &nbsp;&nbsp;FWD break-even (numbers.yaml 26.2bp) (D) | 26.196bp | 26.196bp | -0.0000bp | 0.01bp | MATCH |
| `recon_R1_insight_v1_25sep` | 30.52% | 30.23% | -0.29pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;R1, blind same convention as primary | 30.52% | 30.52% | +0.00pp | 2pp | MATCH |
| `recon_R2_D1_28sep` | 24.21% | 23.84% | -0.37pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;R2, blind same convention as primary | 24.21% | 24.21% | +0.00pp | 2pp | MATCH |
| `recon_R5_no_view_centre_2026_vol` | 27.16% | 26.83% | -0.34pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;R5, blind same convention as primary | 27.16% | 27.16% | +0.00pp | 2pp | MATCH |
| `recon_AX1b_26bp_since1962` | 27.55% | 27.83% | +0.28pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;AX1b 26bp since 1990 | 31.06% | 31.37% | +0.31pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;AX1b 26bp since 2000 | 28.54% | 28.85% | +0.30pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;AX1b 19bp since 1962 | 31.80% | 32.17% | +0.37pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;AX1b 19bp since 1990 | 36.11% | 36.53% | +0.42pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;AX1b 19bp since 2000 | 34.04% | 34.47% | +0.42pp | 2pp | WITHIN TOL |
| `m2_on_25sep_curve` | 37.90% | 37.90% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;25 Sep E1 | 38.21% | 38.21% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;25 Sep E2 | 31.62% | 31.62% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;25 Sep E3 | 37.90% | 37.90% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;25 Sep E4 | 38.19% | 38.07% | -0.12pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;25 Sep E5 | 37.04% | 37.04% | +0.00pp | 2pp | MATCH |
| `gap_if_any_typical` (D) | $10,010 | $10,010 | +0 | min(2%, $500) = $200 | MATCH |
| &nbsp;&nbsp;median gap p95 (D) | $18,213 | $18,213 | +0 | min(2%, $500) = $364 | MATCH |
| &nbsp;&nbsp;E4 mean gap given a gap | $8,802 | $8,771 | -32 | min(2%, $500) = $176 | WITHIN TOL |
| &nbsp;&nbsp;E4 gap p95 | $16,022 | $15,955 | -67 | min(2%, $500) = $320 | WITHIN TOL |
| &nbsp;&nbsp;E4 cost p50 | $294,051 | $293,959 | -91 | min(2%, $500) = $500 | WITHIN TOL |
| `P_whole_payment_waits_max` (D) | 0.27% | 0.27% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;2028 fund median H-FHS (D) | $37,908 | $37,908 | +0 | min(2%, $500) = $500 | MATCH |
| `stock_fund_2028_median` (D) | $40,968 | $40,968 | +0 | min(2%, $500) = $500 | MATCH |
| &nbsp;&nbsp;2028 fund median H-RAW (D) | $41,366 | $41,366 | -0 | min(2%, $500) = $500 | MATCH |
| &nbsp;&nbsp;2028 fund p5 H-FHS | $1,410 | $1,410 | -0 | min(2%, $500) = $28 | MATCH |
| &nbsp;&nbsp;2028 fund p5 H-LVL | $10,339 | $10,339 | +0 | min(2%, $500) = $207 | MATCH |
| &nbsp;&nbsp;2028 fund p5 H-RAW | $1,596 | $1,596 | -0 | min(2%, $500) = $32 | MATCH |
| &nbsp;&nbsp;2028 fund base, FWD (numbers.yaml $40,736) (D) | $40,736.19 | $40,736.19 | -0.00 | $1 | MATCH |
| &nbsp;&nbsp;2028 floor base (numbers.yaml $117,194) (D) | $117,193.70 | $117,193.70 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;2028 fund base, RW | $39,708.05 | $39,708.05 | +0.00 | $1 | MATCH |
| `P_stock_fund_below_20k_2028` (D) | 16.84% | 16.84% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(fund < $20k) H-FHS | 20.04% | 20.04% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(no fund) H-FHS | 4.20% | 4.20% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(top-up) H-FHS | 33.40% | 33.40% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(fund < $20k) H-LVL | 12.33% | 12.33% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(no fund) H-LVL | 0.76% | 0.76% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(top-up) H-LVL | 27.20% | 27.20% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(fund < $20k) H-RAW | 16.84% | 16.84% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(no fund) H-RAW | 4.52% | 4.52% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;P(top-up) H-RAW | 29.84% | 29.84% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;H13 fund -50bp, 5y unchanged (D) | $25,418.61 | $25,418.61 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 fund -50bp, 5y also lower (D) | $22,589.62 | $22,589.62 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 top-up Jan 2028 -50bp | $7,387.68 | $7,387.68 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 fund -100bp, 5y unchanged (D) | $9,366.06 | $9,366.06 | +0.00 | $1 | MATCH |
| `H13_fund_minus100bp_low` (D) | $3,625.72 | $3,625.72 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 top-up Jan 2028 -100bp | $23,440.24 | $23,440.24 | -0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 fund -150bp, 5y unchanged (D) | $0.00 | $0.00 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 floor face -150bp, 5y unchanged (D) | $140,469.49 | $140,469.49 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 fund -150bp, 5y also lower (D) | $0.00 | $0.00 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 floor face -150bp, 5y also lower (D) | $130,723.97 | $130,723.97 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H13 top-up Jan 2028 -150bp | $40,252.40 | $40,252.40 | +0.00 | $1 | MATCH |
| `H14_unfunded_2033_minus50bp` (D) | $9,281.45 | $9,281.45 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;H14 -100bp (D) | $28,752.60 | $28,752.60 | -0.00 | $1 | MATCH |
| `vasicek_theta_1962_vs_2000` | 6.190% | 6.190% | -0.00bp | 5bp | MATCH |
| &nbsp;&nbsp;Vasicek kappa_bc 1962+ | 0.0007 | 0.0007 | +2.24e-13 | 0.02/yr | MATCH |
| &nbsp;&nbsp;ADF p-value 1962+ | 42.01% | 42.01% | -0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;Vasicek theta 1990+ | 3.905% | 3.905% | -0.00bp | 5bp | MATCH |
| &nbsp;&nbsp;Vasicek kappa_bc 1990+ | 0.0484 | 0.0484 | +8.39e-14 | 0.02/yr | MATCH |
| &nbsp;&nbsp;ADF p-value 1990+ | 19.16% | 19.16% | -0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;Vasicek theta 2000+ | 3.295% | 3.295% | -0.00bp | 5bp | MATCH |
| &nbsp;&nbsp;Vasicek kappa_bc 2000+ | 0.1763 | 0.1763 | +1.12e-13 | 0.02/yr | MATCH |
| &nbsp;&nbsp;ADF p-value 2000+ | 16.09% | 16.09% | +0.00pp | 2pp | MATCH |
| `ewma_vol_today` | 81.21 | 81.21 | -7.11e-13 | 2% | MATCH |
| &nbsp;&nbsp;1962-2026 vol (E3 residual sd), bp/yr | 101.1 | 101.1 | -3.41e-13 | 2% | MATCH |
| &nbsp;&nbsp;E5 horizon sd sigma_h, bp | 50.77 | 50.77 | +5.4e-13 | 2% | MATCH |
| &nbsp;&nbsp;E1, purchase Mon 4 Jan 2027 | 33.72% | 33.72% | +0.00pp | 2pp | MATCH |
| `sensitivity_purchase_4jan2027_median` | 33.07% | 33.08% | +0.01pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;4 Jan median, primary at strict n_h = 64 | 32.95% | 33.08% | +0.13pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;4 Jan E2 (n_h = 65) | 27.24% | 27.24% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;4 Jan E3 (n_h = 65) | 33.15% | 33.15% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;4 Jan E4 (n_h = 65) | 32.71% | 32.68% | -0.03pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;4 Jan E5 (n_h = 65) | 33.07% | 33.08% | +0.01pp | 2pp | WITHIN TOL |
| &nbsp;&nbsp;4 Jan Cost_RW(R) | $293,536.88 | $293,536.88 | -0.00 | $1 | MATCH |
| &nbsp;&nbsp;4 Jan RW break-even | 22.321bp | 22.321bp | -0.0000bp | 0.01bp | MATCH |
| `pv_today_R_usd` (D) | $289,119.20 | $289,119.20 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;2033 rung cost at R, 1 Jan 2027, yields unchanged | $37,166.35 | $37,166.35 | +0.00 | $1 | MATCH |
| &nbsp;&nbsp;ladder yield today | 5.3289% | 5.3289% | +0.0000bp | 0.01bp | MATCH |
| &nbsp;&nbsp;d ladder yield / d parallel shift | 1.008 | 1.008 | +5.33e-13 | 2% | MATCH |
| &nbsp;&nbsp;median P(gap > $10k) | 13.37% | 13.37% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;R3 strategy_mc_v2 (a), 25 Sep, analytic | 30.09% | 30.09% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;R3' same on 28 Sep | 23.95% | 23.95% | +0.00pp | 2pp | MATCH |
| &nbsp;&nbsp;E1 windows (95-day) | 15,855 | 15,855 | +0 | exact | MATCH |
| &nbsp;&nbsp;E1 non-overlapping windows | 247 | 247 | +0 | exact | MATCH |
| &nbsp;&nbsp;E2 windows (10y 4.0-6.5%) | 5,661 | 5,661 | +0 | exact | MATCH |
| &nbsp;&nbsp;15-month windows | 15,605 | 15,605 | +0 | exact | MATCH |
| &nbsp;&nbsp;2028 mean top-up if any H-FHS | $11,155 | $11,155 | -0 | min(2%, $500) = $223 | MATCH |
| &nbsp;&nbsp;2028 mean top-up if any H-LVL | $8,423 | $8,423 | +0 | min(2%, $500) = $168 | MATCH |
| &nbsp;&nbsp;2028 mean top-up if any H-RAW | $13,431 | $13,431 | +0 | min(2%, $500) = $269 | MATCH |
