# M7 spec: stress scenarios for Root-and-Branch, and the real value of the $50,000 payments

WS3, 2026-09-30 (Sydney). AI-generated research specification (Claude Code) for Team Caplet; no deliverable text.
Implementation-independent; reference code `rab/models/m7_stress.py` (not to be read by a blind builder).
Strategy is not reopened: scenarios test the adopted rules; findings are triaged, never applied.

## 0. Questions

1. What happens to the payments, the 2031 range and the 2033 gift if 2027-2032 look like the 1970s, Japan's 1990s,
   2022, 2008, the Great Depression, or a U.S. credit downgrade?
2. What will ten fixed $50,000 payments be worth in real terms (purchasing power) under sourced inflation paths?

## 1. Inputs

`rab/numbers.yaml` (`market.par_curve` = 28 Sep 2026 par curve, `laura.ladder.cost_2027_strips`,
`laura.stock_fund_2028_usd.strips`), `rab/data/history/annual_history.csv` (`world_eq`, `jpn_eq`, `jpn_ltrate`,
`jpn_cpi_infl`, `cpi_infl`), `soy_curves.csv` (10 Yr on the first trading day of each year), `market_inflation_2026-09.csv`
(T10YIE, EXPINF10YR), `jpm_ltcma_2026_usd.csv` (U.S. Inflation 2.50%), `rab/data/fred/DGS10.csv` and
`rab/data/history/raw/yf_GSPC_daily.csv` (downgrade windows).

## 2. Scenario engine (one deterministic path per scenario)

A scenario = shift before the ladder purchase `dpre` (percentage points, parallel on every par yield), yearly parallel
par changes `dy_t` and world-fund returns `e_t` for t = 0..5 (years 2027..2032, change during the year), and inflation
`pi_t` for t = 0..14 (2027..2041). Cumulative shift at 1 Jan (2027+t): s_t = dpre + sum_{u<t} dy_u (s_0 = dpre).
Curve at any 1 Jan T (T = 2027..2033) = the 28 Sep 2026 par curve shifted by s_{T-2027} (M1 A1 step 5, bootstrap
after the shift), used as a forward curve: DF_T(d) = DF(d)/DF(T). Consequences:
- Ladder cost on 1 Jan 2027: C = sum_k 50,000 DF_{2027}(P_k), P_k = 15 Nov 2032..2041 (= M1 A3 V_A at shift dpre;
  base 292,418.11).
- Longest-first purchase with 300,000; leftover L grows for one year at r1 = 4.59% + dpre (today's 1-year par plus
  the shift, annual compounding); unbought
  fractions u_k priced at 1 Jan 2028 on the s_1 curve: T = sum u_k 50,000 DF_{2028}(P_k). G = L (1 + r1) + 150,000 - T.
- Floor (E6 / M1 F convention): y5 = 5.06% + s_1; cost 150,000 / (1 + y5)^5; F and fund0 as M5 B4 (fund0 = G - cost if
  G >= cost, else F = G (1 + y5)^5 and fund0 = 0). Base: fund0 = 40,736.
- Fund: fund31 = fund0 (1+e_1)(1+e_2)(1+e_3); fund33 = fund31 (1+e_4)(1+e_5). bottom, top, gift, kept, T33 as M5 B6.
- Payments funded in full iff G >= 0.
- Real terms: deflator to 1 Jan 2033 = prod_{t=0..5} (1 + pi_t); real gift = gift / deflator ("1 Jan 2027 dollars").
  Real value of payment k (paid 1 Jan 2032+k): 50,000 / prod_{t=0}^{4+k} (1 + pi_t).
Context rivals on the same path (M6 definitions, bond fund return b_t = (5.06% + s_t) - 5 dy_t, duration 5):
All-Treasury (R1: T33 = G (1 + y5)^5), 60/40 whole portfolio (R2: reserve bought 1 Jan 2033 on the s_6 curve), CPPI m = 3
(R5: floor_t on the s_t curve).

## 3. Scenarios (analog year A0 plays 2027; t-th year plays A0 + t)

| Id | Scenario | dpre | dy_t, e_t (t = 0..5) | pi_t (t = 0..14) |
|---|---|---|---|---|
| S0 | Base | 0 | dy = 0; e = 7.00% (JPM AC World compound) | 2.34% (T10YIE, 28 Sep 2026) |
| S1 | 1970s stagflation | 0 | A0 = 1973: dy = 10 Yr(1 Jan A0+t+1) - 10 Yr(1 Jan A0+t) from `soy_curves.csv`; e = `world_eq` A0+t | `cpi_infl` 1973..1987 |
| S2 | Japan's lost decade | 0 | A0 = 1990: dy = (`jpn_ltrate` A0+t+1 - A0+t)/100; e = `jpn_eq` A0+t (yen, as the world fund) | `jpn_cpi_infl` 1990..2004 |
| S2b | Japan, rates fall first | -1.00 | as S2 | as S2 |
| S3 | 2022 in 2028 | 0 | base, except t = 1: dy = 10 Yr(2023) - 10 Yr(2022), e = `world_eq` 2022 | `cpi_infl` 2021..2025, then 2.34% |
| S3b | 2022 in 2027 | 0 | base, except t = 0 as above | as S3 |
| S4a | Downgrade, 2011-style | measured | base | 2.34% |
| S4b | Downgrade, 2023-style | measured | base | 2.34% |
| S4c | Downgrade, 2025-style | measured | base | 2.34% |
| S4d | Downgrade plus buyers' strike (hypothetical) | +1.00 | base, except e_1 = -20% | 2.34% |
| S5 | Great Depression | 0 | A0 = 1928: dy from `soy_curves.csv` (flat-curve era); e = `world_eq` A0+t | `cpi_infl` 1928..1942 |
| S6 | 2008 in 2028 | 0 | base, except t = 1: dy = 10 Yr(2009) - 10 Yr(2008), e = `world_eq` 2008 | 2.34% |
| S7 | Great Inflation | 0 | A0 = 1966: as S1 with 1966 | `cpi_infl` 1966..1980 |

Downgrade "measured" = change in FRED DGS10 from the last close before the announcement to 20 trading days later:
S&P 5 Aug 2011, Fitch 1 Aug 2023, Moody's 16 May 2025 (announcement dates; S&P 500 moves over the same windows reported
from Yahoo, secondary).

**Thresholds.** On the S0 path with dpre = -x (the fall persists to Jan 2028; dy = 0), solve by bisection for the x at
which (a) C = 300,000 (top-up starts), (b) fund0 reaches 0 (the floor is still 150,000), (c) G = 0 (a payment unfunded).

## 4. Real value of the payments (inflation paths)

Paths for 2027..2041: breakeven 2.34% (T10YIE); Cleveland Fed 10-year expected inflation (EXPINF10YR, latest);
JPM 2026 LTCMA U.S. inflation 2.50%; Fed target 2.00%; S1, S2, S3, S5, S7 paths; and the historical distribution:
every 15-year U.S. window of `cpi_infl` starting 1872..2011 (p5 / p50 / p95 of each payment's real value).
Report each payment's real value (1 Jan 2027 dollars), the ten-payment total, and the 2033 and 2042 values.
Reproduce insight_v1 H19 (`ref.H19.real_value_50k`) exactly with its convention (2.5%, 7 and 16 years from 2026) and
note the sourced input (JPM 2.50%).

## 5. Outputs

`rab/results/M7/stress_table.csv` (scenario x all engine quantities, rivals), `real_value_paths.csv`,
`real_value_history_distribution.csv`, `downgrade_events.csv`, `fig_m7_stress.png`, `fig_m7_real_value.png`,
`M7_results.json`, `M7_report.txt`.

## 6. Tolerances (Gate B)

Deterministic: every value to $1; dates and event moves identical (1bp).

## 7. Assumptions to state

Parallel shifts of today's curve (no twists); analog returns are annual and in each market's own currency (Japan in
yen); the world fund in S1/S5/S7 is the VT-like proxy (M5); no fees; the ladder is held to maturity, so price moves
after 1 Jan 2027 change only its market value, never the payments.

## 8. Changelog

- **2026-09-30, Gate B (`rab/gates/gate_B_ws3.md`)**. These are clarifications only; no number changed.
  - S2 erratum: "(`jpn_ltrate` A0+t+1 - A0+t)/100" should read `jpn_ltrate`(A0+t+1) - `jpn_ltrate`(A0+t), in
    percentage points. `jpn_ltrate` is already in percent, like the 10 Yr column used in S1. Both builds used
    percentage points. The literal reading (blind row `S2_lit`, a shift of about -0.01pp, gift $163,194) is not used.
  - Downgrade base: all three announcements came after the U.S. close, so "the last close before the announcement"
    is that day's close (both builds). Using the previous day's close instead gives 2011 -32bp, 2023 +23bp and
    2025 -4bp (blind `downgrade_events.csv`, `alt_prior_close_change_pp`).
