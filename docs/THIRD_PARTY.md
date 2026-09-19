# Third-Party Dependencies and Provenance Attribution

This document records the provenance, licensing, and attribution of external libraries and conceptual designs utilized in `wharton-ic`.

---

## 1. Direct Software Dependencies

| Package | Version Range | License | Role in System | Attribution |
|---|---|---|---|---|
| **skfolio** | `^1.2.8` | BSD-3-Clause | Core quantitative portfolio optimization (MeanRisk, Max Sharpe, Min Vol, CVaR, Risk Budgeting, HRP). | [skfolio/skfolio](https://github.com/skfolio/skfolio) (Hugo Delatte et al.) |
| **pydantic** | `^2.10.0` | MIT | Strict data validation, schema enforcement, and JSON serialization. | [pydantic/pydantic](https://github.com/pydantic/pydantic) |
| **typer** | `^0.12.0` | MIT | Command-line interface framework for student and analyst interactions. | [tiangolo/typer](https://github.com/tiangolo/typer) |
| **cvxpy** | `^1.6.0` | Apache-2.0 | Convex optimization solvers for portfolio constraints. | [cvxpy/cvxpy](https://github.com/cvxpy/cvxpy) |
| **pandas** | `^2.2.0` | BSD-3-Clause | Time series, financial dataframes, and tabular operations. | [pandas-dev/pandas](https://github.com/pandas-dev/pandas) |
| **numpy** | `^1.26.0` | BSD-3-Clause | Vectorized numerical operations and linear algebra. | [numpy/numpy](https://github.com/numpy/numpy) |
| **scipy** | `^1.12.0` | BSD-3-Clause | Scientific computing, optimization, statistical distributions. | [scipy/scipy](https://github.com/scipy/scipy) |
| **statsmodels** | `^0.14.0` | BSD-3-Clause | Econometric regressions, factor models, rolling OLS. | [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) |
| **duckdb** | `^1.1.0` | MIT | Embedded analytical database for point-in-time SQL queries. | [duckdb/duckdb](https://github.com/duckdb/duckdb) |
| **pyarrow** | `^15.0.0` | Apache-2.0 | Parquet file format persistence for price and fundamental caches. | [apache/arrow](https://github.com/apache/arrow) |
| **pyyaml** | `^6.0.0` | MIT | Declarative YAML configuration parsing. | [yaml/pyyaml](https://github.com/yaml/pyyaml) |
| **matplotlib** | `^3.8.0` | PSF / BSD | Generation of publication-quality figures and charts for Report Pack. | [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib) |
| **yfinance** | `^0.2.40` | Apache-2.0 | Free fallback provider for historical market prices and dividends. | [ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) |
| **pytest** | `^8.0.0` | MIT | Comprehensive testing framework (unit, leakage, integration, regression). | [pytest-dev/pytest](https://github.com/pytest-dev/pytest) |

---

## 2. Conceptual Provenance and Intellectual Lineage

The design of `wharton-ic` draws conceptual inspiration from multiple institutional frameworks while maintaining 100% original, clean-room implementation:

1. **Declarative Pipeline Configuration & Report Outputs**:
   - *Inspiration*: `gavin-ho1/wharton-investment-comp` (Hotchkiss School - Bullish Bearcats, MIT License).
   - *Attribution*: The concept of separating pipeline stages into a declarative YAML configuration file and exporting automated final report tables was inspired by the Hotchkiss workflow.
   - *Distinction*: `wharton-ic` completely reimagines the backend with point-in-time stores, out-of-sample walk-forward backtests, client-mandate constraints, and deterministic DCF engines.

2. **Adversarial Multi-Agent Financial Council**:
   - *Inspiration*: `TauricResearch/TradingAgents` (Apache-2.0 License) and `AI4Finance-Foundation/FinRobot` (Apache-2.0 License).
   - *Attribution*: The division of labor into independent analytical roles (Fundamental, Quant, Valuation, Macro) followed by an adversarial Bull vs. Bear debate and Risk Officer review.
   - *Distinction*: In `wharton-ic`, language models are strictly forbidden from performing financial arithmetic. All numerical calculations are executed by deterministic Python engines and provided as frozen inputs to the council.

3. **Mandate Abstraction**:
   - *Inspiration*: `virattt/ai-hedge-fund` (MIT License).
   - *Attribution*: Structuring the investment strategy as a client mandate with explicit constraints.
   - *Distinction*: `wharton-ic` adapts the mandate specifically to Wharton High School Investment Competition rules (client case study, ethics/impact values, risk tolerance, investment horizon, and approved universe constraints).

4. **Convex Portfolio Optimization**:
   - *Implementation*: Direct integration of `skfolio` (BSD-3-Clause).
   - *Distinction*: `wharton-ic` wraps `skfolio` estimators with Wharton-specific constraint management, tracking error budgets, benchmark comparisons, and explainable decision logs.

---

## 3. Compliance and Originality Declaration

- **No Code Plagiarism**: No proprietary strategy code, heuristic factor weights, or competition narratives from previous competitors have been copied or reproduced.
- **Original Architecture**: All data schemas, valuation models, risk metrics, decision ledgers, and CLI commands were designed and coded specifically for `wharton-ic`.
- **License Compatibility**: All open-source packages and architectural inspirations comply with their respective MIT, Apache-2.0, and BSD licenses.
