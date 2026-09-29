# M2 model card: rate paths to January 2027

WS4, 30 Sep 2026 (Sydney). AI-generated research (Claude Code) for Team Caplet; MODEL outputs, not deliverable text.
Scale: **Laura's plan** (Nov-15 STRIPS basis, numbers.yaml headline basis). Curve: Treasury par curve of 28 Sep 2026.
Spec `rab/models/M2_SPEC.md` (headline rule committed before any estimator ran, 88e7f4a). Code `rab/models/m2_rate_paths.py`,
figures `m2_figures.py`, outputs `rab/results/M2/`. Runs in about 5 s, seed 20260930. Proposed numbers:
`rab/results/M2/m2_proposed_numbers.yaml` (WS1 is the only writer; nothing is in numbers.yaml yet).

## Answer

**Chance the ten payments cost more than $300,000 on 1 Jan 2027: about 1 in 3** (32.7%, the median of five methods;
they give 27-33%, so quote "roughly 25-35%"). If there is a shortfall it is typically about $10,000; in 1 path in 20 it
is about $18,000 or more; the chance that a whole payment waits is under 0.3%. It is paid from the 2028 deposit
(the longest payments are bought first, so only part of the 2033 payment waits).

| Estimator (no view on rate direction) | P | Spread of rates to Jan (sd) |
|---|---|---|
| E1 History of 95-day curve moves since 1963, rescaled to today's volatility | 33% (90% range 30-37%) | 56bp |
| E2 History when the 10-year yield was 4.0-6.5% | 27% (22-33%) | 39bp |
| E3 Vasicek (AR(1), statsmodels) on the ladder's yield, 1962+, bias-corrected | 33% | 51bp |
| E4 Three-factor curve model (PCA + VAR(1), statsmodels), 1990+ | 32% | 45bp |
| E5 Options market: MOVE 101.8 on 28 Sep, calibrated to the ladder | 33% | 51bp |

## Reconciliation with "about 1 in 3" (insight_v1) and 24.2% (D1 rerun, `ref.H6`)

All three insight_v1 figures reproduce from their own files: D1 [6] 30.5% (25 Sep) and 24.2% (28 Sep); AX1b [C]
27.6 / 31.1 / 28.5% (26bp falls since 1962 / 1990 / 2000); strategy_mc_v2 (a) 30.1% analytic (30.2% printed).
The waterfall (figure 2): 30.5% on 25 Sep -> **24%** when yields rose by 28 Sep (room grew from 19bp to 26bp) ->
**27%** when the price on 1 Jan is set by "yields unchanged" instead of "forward rates come true" (the bonds are three
months older and roll down the curve, so the ladder costs $293,401, not $292,418; the room is 23bp, not 26bp) ->
**33%** when volatility comes from today's markets and long history instead of 2026's calm average (71bp a year;
today's recent-days estimate is 81bp, the options market about 101bp, the 1962-2026 average 101bp).
So "1 in 3" survives, but for new reasons; 24.2% should not be quoted. On the 25 Sep curve M2 gives 38%.

## What this teaches (plain English)

1. The risk is about how jumpy rates are over one quarter, not where they are heading. Five different ways of
   measuring jumpiness all land near 1 in 3.
2. Nobody can say where "normal" rates are: a textbook Vasicek model fitted from 1962 says 6.2%, from 1990 3.9%, from
   2000 3.3% (figure 4). After correcting its known bias, the fitted pull back to "normal" is almost zero over three
   months (a half-life of centuries on 1962-2026 data; a unit-root test cannot reject "no pull", p = 0.42). So the
   headline takes no view on direction.
3. The shortfall, if it comes, is small and lands on the stock fund, not on the payments - as long as the 2028
   deposit arrives. Fifteen months of history (to 1 Jan 2028): the stock fund is typically about $41,000, under
   $20,000 in about 1 path in 6, and nothing at all in 1-5% of paths (figure 5; `laura.stock_fund_2028_usd.strips` is
   $40,736 on today's forwards).

## Re-checked WS4 references (28 Sep curve, forward convention as D1/E6)

- H13 (rates fall before Jan 2027): -50bp: stock fund $23-25k; -100bp: $4-9k; -150bp: no fund and the floor repays
  $131-140k instead of $150k (range = 5-year yield unchanged or also lower). E6's 25 Sep values were $20-23k / $1-7k /
  $127-137k: slightly better now because yields are higher.
- H14 (no 2028 deposit at all): $9,281 (-50bp) / $28,753 (-100bp) of the 2033 payment unfunded. Reproduced exactly.

## Assumptions, data, limits, failure modes

- Data: Treasury par curves 1990-2026 and FRED constant-maturity yields 1962-1989 (16,170 days; FRED equals Treasury
  on the 9,190 shared days); MOVE from Yahoo (secondary source). One reference curve (28 Sep); re-run Friday with
  `--curve-date`. MODEL prices, no STRIPS dealer mark-up (a mark-up raises the odds).
- E1 assumes today's volatility lasts three months, and window scaling fattens the tails (sd 56bp, robust sd 48bp).
  E2 mixes calm (1960s, 2000s) and stormy periods at similar yields and comes out lowest. E3 uses the 1962-2026
  average volatility, including 1979-1982. E4's mean reversion is not bias-corrected (it drifts the 10-year yield
  down 2bp; its no-reversion twin gives 31%). E5 uses a one-month option volatility for a three-month horizon while
  MOVE had just jumped from about 78 to 102 in a week; with MOVE's 63-day average (76) E5 gives 27%.
- Failure mode: if the calm of mid-2026 returns, the odds are nearer 1 in 4 (27% with 2026's volatility and yields
  unchanged). If volatility stays at September's level, nearer 1 in 3. Either way this is a quarter-by-quarter
  number: re-run it before quoting it after Friday.
- Not modelled: the WInS book (bought in the competition at WInS prices, so it has no January 2027 purchase);
  Laura's real plan under the strict "for BOTH contributions" reading, which would use coupon Treasuries and iBond
  ETFs instead of STRIPS (their odds are not computed here; see `reinvest.*` for their extra coupon risk).

## Triage (contradiction rule; nothing is applied to the IPS or the Sheet)

- **note-in-Final-Report**: "about 1 in 3 (MODEL, 28 Sep 2026 curve)" with its basis; never in a WInS note.
  The IPS draft does not quote the odds (inventory F2), so no IPS change.
- **fix-before-6-Nov (RAB files only, WS0; no IPS change)**: `rab/assumptions.md` C2 and `rab/premortem.md` PM-32 quote 24.2% as the model figure;
  replace with `laura.rates.gap_odds_2027` once WS1 adds it; retire `ref.H5`, mark `ref.H6` reproduced.
- **ignore**: the 4 Jan vs 1 Jan purchase date (E1: 33.7% vs 33.2%; median of five in the blind rebuild: 33.1% vs
  32.7%). Corrected at Gate B: this line used to compare E1 on 4 Jan with the five-method median on 1 Jan.

**Gate B (30 Sep 2026): PASS.** The blind rebuild from `M2_SPEC.md` matches every headline key (decision keys within
0.005pp, deterministic figures to the cent); see `rab/gates/gate_B_ws4.md`. Monte Carlo noise in the headline is about
0.15pp (noise-free median 32.6%), so quote "about 1 in 3", never a decimal.
