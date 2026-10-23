# `model/`: Laura Gao cash-flow and risk model

One small, tested model that produces every number in `decisions/`. It uses only numpy and pyyaml (matplotlib for charts) and is separate from `src/wharton_ic` on purpose.

```bash
# from the repo root
python -m model.laura.run          # ~5 s: writes outputs/laura/results.json, tables.md, charts
python -m pytest model/tests -q    # 14 tests
```

To change an assumption, edit `model/laura/assumptions.yaml` and re-run. Every assumption there is sourced or marked `TEAM_ASSUMPTION` / `TEAM_DECISION`.

## What it does (plain English)

1. **Prices the promise.** It works out what the ten $50k payments (2033–2042) cost at any interest rate. The cost is the price of a Treasury "ladder": one bond maturing on each payment date.
2. **Simulates 2027–2033.** It runs 20,000 paths of interest rates (mean-reverting around 4.2%) and stock returns (fat-tailed). Bond returns are consistent with the simulated rates, so the reserve's cost moves with rates exactly as it would in real life.
3. **Tests four strategies:**
   - **A:** lock the whole ladder in 2027.
   - **B:** hedge 50% rising to 100% by 2031.
   - **C60 / C80:** a 60/40 or 80/20 portfolio, buying the ladder in 2033.
4. **Replays history.** It applies every actual 6-year stretch since 1928 (93 windows: the 1929 crash, 1970s stagflation, dot-com, 2008, 2022) to today's starting yields.
5. **Tests the 2031 promise to co-sponsors.** In 2031 part of the surplus is moved into Treasuries maturing in 2033. The model then checks how often the announced range holds.
6. **Runs sensitivities:**
   - the Jan-2027 starting yield
   - the growth-sleeve equity share
   - the flexibility buffer
   - the $150k 2028 contribution arriving late, smaller, or never
   - Taiwan dollar exchange-rate moves
   - inflation (US and Taiwan)

## Key modelling simplifications (state these in the IPS)

- **Flat yield curve:** the 6–15 year curve is represented by a single yield. Today's curve is fairly flat across those maturities (7Y 5.05%, 10Y 5.11%). A real ladder built from coupon Treasuries has small reinvestment risk on the coupons, which the model ignores.
- **Equity sleeve:** modelled as one diversified global equity asset. The team's actual stock picks are the *implementation* of that sleeve.
- **Annual time steps:** there are no intra-year trades, taxes or fees. Taxes are out of scope per the case; fees would lower returns by roughly 0.1–0.3% a year.
- **Historical replays are US data:** S&P 500 and the 10Y Treasury (Damodaran, 1928–2025).
- **The 2031 range uses the team's base-case assumptions** (as it would in reality). It is then tested against bear and historical outcomes it was not calibrated on.

## Files

| File | Purpose |
|---|---|
| `laura/assumptions.yaml` | All inputs with sources |
| `laura/engine.py` | Liability valuation, market simulation, historical replay, strategies, 2031 rule |
| `laura/run.py` | Runs everything; writes results, tables, charts |
| `laura/data/us_history_1928_2025.csv` | Damodaran annual returns and yields, with source header |
| `tests/test_laura.py` | PV vs hand calculation, beginning-of-year timing, hedge immunity, reproducibility, history, 2031 rule |
