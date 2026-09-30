# M3 SPEC: the Branch, 2028-2033 (three return models)

WS2, written 2026-09-30 (Sydney) before any M3 code was run. Implementation-independent: a blind builder needs only
this file and the raw inputs in section 1. AI-generated research (Claude Code) for Team Caplet; no deliverable text.

**Question.** Under the adopted Root-and-Branch rule, what range will Laura announce in January 2031, where in that
range will the January-2033 gift land, and how much does the answer depend on the model of stock returns?

## 1. Inputs (paths relative to the worktree root)

| Symbol | Value | Source |
|---|---|---|
| B0 | 40,736.193940603116 USD: stock fund bought 2 Jan 2028 (Laura's plan) | `rab/numbers.yaml` `laura.stock_fund_2028_usd.strips` (= `rab/models/out/m1_results.json` F.nov15.fund_usd); Nov-15 STRIPS basis (the Gate A headline basis) |
| F | 150,000 USD: floor face, repaid by late 2032 | case p.2 (2028 deposit) and IPS rule; `laura.floor_cost_2028` (cost 117,194 at the 5-year par 5.06%) |
| mu_L | ln(1.0700) = 0.0676586: median (compound) annual log return | J.P. Morgan 2026 LTCMA, AC World Equity, compound 7.00% (`competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf` p.2, data as of 30 Sep 2025; main checkout) |
| sig_L | sqrt(2 ln(1.0828/1.0700)) = 0.1542182: sd of annual log return | same page, arithmetic 8.28% (lognormal fit exactly as insight_v1 `D6_behavioural_numbers.lp`) |
| Shiller monthly | nominal total returns Jan 1871 .. Dec 2025 (1,860 months) | `rab/data/ws2_returns/shiller_monthly.csv` column `r_nominal`, rows `1871-01` .. `2025-12` (built from `raw/shiller_ie_data.xls` by `build_returns.py`; manifest `rab/data/ws2_returns/MANIFEST.csv`) |
| Shiller annual | January-to-January nominal log returns 1871 .. 2025 (155 years) | `rab/data/ws2_returns/shiller_annual.csv` column `log_r_nominal` |

Seed: 20260930. Paths: N = 200,000 per model.

## 2. Timeline and the rule (Laura's plan, nominal U.S. dollars)

- t = 0: 2 January 2028 (treated as 1 January). The fund B0 is bought; the floor is bought.
- Annual log returns x_1 .. x_5 for 2028, 2029, 2030, 2031, 2032.
- B3 = B0 exp(x_1 + x_2 + x_3): the fund on 1 January 2031, the day the range is announced.
- B5 = B3 exp(x_4 + x_5): the fund on 1 January 2033.
- Share promised s = 1/2 (the adopted D6 default; M4 varies it).
- **Range announced in 2031:** bottom = F; top U = F + s B3.
- **Gift in 2033:** G = F + s min(B5, B3) (the cap). Kept money K = B5 - s min(B5, B3). Total T = F + B5 = G + K.
- **Position in the range** p = (G - F) / (U - F) = min(B5 / B3, 1).
- The floor pays F exactly (M3 assumes it; M4 models the floor's delivery). No fees (M8 varies them).

For the monthly bootstrap, x_k is the sum of months 12(k-1)+1 .. 12k of the path.

## 3. Return models

All four headline models have the same centre: median compound return 7.00% a year (JPM AC World). They differ in
shape (tails, serial dependence) and in parameter uncertainty.

**L (reference, insight_v1 E6 method).** x_k i.i.d. Normal(mu_L, sig_L^2). Kept only to reconcile with insight_v1
(H8) on the 28 Sep basis; not one of the three decision models.

**T (fat-tailed parametric).** x_k i.i.d. = mu_L + c t_nu, nu = 4, truncated: a draw with |x_k - mu_L| > 5 sig_L is
discarded and redrawn. The scale c is set so that the truncated distribution's standard deviation equals sig_L exactly:
c = 0.1162464 (about 0.754 sig_L; 0.268% of raw draws are discarded). Same median and same sd as L; fatter tails.
(Truncation keeps the expected fund value finite: an untruncated Student-t on log returns has no finite mean.)

**BOOT (Shiller stationary block bootstrap).** Monthly log returns y_i = ln(1 + r_nominal_i), i = 1..n, n = 1,860.
Re-centred: y'_i = y_i - mean(y) + mu_L / 12 (so the bootstrap's expected annual log return is mu_L; shape and
volatility stay historical). Stationary bootstrap (Politis and Romano 1994) with mean block length 24 months: month 1
of a path is y'_J with J uniform on 1..n; each later month either continues to the next index (probability 23/24;
index n is followed by index 1) or jumps to a new uniform index (probability 1/24). 60 months per path.
Sensitivity variants (reported, not headline): BOOT-raw (no re-centring: history's own mean), BOOT-b1 (mean block
1 month = i.i.d. months), BOOT-b60 (mean block 60 months).

**BAYES (pymc, uncertain mean).** Two parts.
1. History fit (the shape): annual log returns z_j (Shiller annual, 1871-2025, n = 155) ~ StudentT(nu, m_h, sigma).
   Priors: m_h ~ Normal(0.08, 0.05); sigma ~ HalfNormal(0.30); nu = 2 + nu', nu' ~ Gamma(shape 2, rate 0.1)
   (the Juarez and Steel 2010 prior, shifted so the variance exists). NUTS: 4 chains, 1,000 tuning + 1,000 draws each,
   target_accept 0.9. Convergence required: r_hat <= 1.01 and bulk ESS >= 400 for m_h, sigma, nu; otherwise stop.
2. Forward mean (the uncertain centre): mu_f ~ Normal(ln 1.07, 0.015^2), independent of the history fit. History sets
   how bumpy stocks are; published forecasts set the centre (US history's own mean, about 9%, is not used as a
   forecast, WS5 ref [15] Anarkulova et al. 2022); sd 1.5 points spans the Vanguard-like VT blend 5.08% (insight_v1
   `D2_equity_premium.py`, Vanguard VCMM run of 30 Jun 2026) at about 1.3 sd below and 9% at 1.3 sd above.
3. Predictive path: draw a posterior sample j uniformly from the 4,000 (with replacement) and mu_f; then x_k =
   mu_f + sigma_j t_{nu_j} for k = 1..5, a draw with |x_k - mu_f| > 5 sigma_j sqrt(nu_j / (nu_j - 2)) being redrawn.
Sensitivity variant BAYES-hist: mu_f = m_h,j (the forward centre learned from US history).

## 4. Outputs (`rab/results/M3/`)

1. `summary.csv`: one row per model (L, T, BOOT, BAYES, and the variants), columns: B3 and U (2031 top), G (2033
   gift), K (kept), T (total) at p5, p10, p25, p50, p75, p90, p95 and the mean; P(top reached) = P(B5 >= B3);
   P(upper half) = P(B5 / B3 >= 0.5); median position p; P(B3 < B0) (fund below cost when she speaks); P(G >= F)
   (must be 1); the realised annual log-return mean and sd of the simulated paths (check).
2. `range_confidence.csv`: the statements Laura can make, per model: bottom (certain by construction if the
   conditions in section 5 hold); top median and 90% interval (as seen today); P(top reached); P(upper half).
3. `conditional_top.csv` (BOOT only, the only model with serial dependence): P(top reached) given B3 below vs above
   its median.
4. `bayes_posterior.csv`: posterior mean, sd, 5% and 95% of m_h, sigma, nu, with r_hat and ESS.
5. `reconcile_E6.csv`: L on this basis next to insight_v1 E6 [1]-[2] (25 Sep basis, B0 = 40,400, seed 20260927):
   gift, kept, total p5/p50/p95, median top, P(top reached).
6. Figures (PNG, colour-blind-safe palette, direct labels): `fig_M3_top2031.png` (distribution of the 2031 top per
   model), `fig_M3_gift2033.png` (2033 gift per model, showing the cap), `fig_M3_where_in_range.png` (at the top /
   upper half / lower half, per model).
7. `numbers_proposed.yaml`: the headline figures in the `rab/numbers.yaml` schema, for WS0/WS1 to review. WS2 does not
   write `rab/numbers.yaml` (PM-35).

## 5. The confidence statement (fixed wording, PM-25)

"The 2033 gift falls inside the 2031 range: **certain by construction if** (a) the floor holding pays its face value,
(b) the 2028 deposit arrived in full (known before 2031), (c) the gift is capped at the announced top, and (d) no
fee is ever taken from the floor." Model outputs add only where in the range the gift lands. M4 quantifies (a).

## 6. Tolerances (Gate B blind rebuild)

Range ends (bottom, top percentiles, gift percentiles): within 2%. Probabilities: within 2 points. For L, the
analytic values must hold within Monte Carlo error: median top = F + s B0 e^{3 mu_L} = 174,952; P(top reached) =
Phi(sqrt(2) mu_L / sig_L) = 73.3%. BAYES posterior means within 10% of each other (MCMC noise).

## 7. References (DOIs checked on Crossref, 30 Sep 2026)

- Politis, D. N., & Romano, J. P. (1994). The stationary bootstrap. JASA 89(428), 1303-1313. doi:10.1080/01621459.1994.10476870
- Juarez, M. A., & Steel, M. F. J. (2010). Model-based clustering of non-Gaussian panel data based on skew-t
  distributions. JBES 28(1), 52-66. doi:10.1198/jbes.2009.07145 (source of the Gamma(2, 0.1) prior on nu)
- Pastor, L., & Stambaugh, R. F. (2012). Are stocks really less volatile in the long run? J. Finance 67(2), 431-478.
  doi:10.1111/j.1540-6261.2012.01722.x (why an uncertain mean matters for multi-year horizons)
- Shiller, R. J. ie_data.xls, "U.S. Stock Markets 1871-Present and CAPE Ratio", shillerdata.com (fetched 30 Sep 2026 AEST).
- WS5 ref [15]: Anarkulova, Cederburg & O'Doherty (2022), JFE 143(1), 409-433 (`rab/literature/references.md`, rab/ws5).

## 8. Gate B clarifications (30 Sep 2026; sections 1-7 unchanged)

- C1. Section 4.5 (E6 reconciliation). insight_v1 E6's own fund is B0 = 7,736 x 1.045 + 150,000 - 150,000 / 1.0498^5
  = $40,442.6 (the "40,400" above is that figure rounded). E6's draws are `numpy.random.default_rng(20260927)
  .standard_normal((200000, 6))`, columns 1-5 = 2028-2032 (`D6_behavioural_numbers.py` `draws`). The primary build used
  B0 = $40,443 on its own seed-20260930 paths; the blind build used B0 = $40,400 on its own stream. Both land within
  $0.4k of E6. The Gate B check (`rab/verification/gateB_ws2/`) feeds E6's exact draws through both rule codes and
  reproduces every printed H8 figure.
- C2. BAYES-hist takes its forward centre from the posterior sample, so two separate MCMC runs give slightly different
  BAYES-hist paths: the posterior means of m_h were 0.0952 and 0.0946. BAYES, the decision model, does not depend on
  m_h. It is not a bug, and BAYES-hist is a sensitivity variant only.
