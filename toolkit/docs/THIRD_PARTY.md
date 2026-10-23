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

## 2. Reference Repositories Forensic Metadata (V2.1)

| Repository | Exact Commit SHA | Inspected Date | License | Competition Verified | Role in Caplet |
|---|---|---|---|---|---|
| **TauricResearch/TradingAgents** | `2d17df8da1536c121e4d7395ac5a5dcec9e96d6f` | 2026-09-19 | Apache-2.0 | General FinTech | ADAPT: State graph, deterministic checkpointing, multi-round debate |
| **AI4Finance-Foundation/FinRobot** | `6d6ccd32c1b8b1904dc656cf06897438aba3daec` | 2026-09-19 | Apache-2.0 | General FinTech | ADAPT: Specialist agent library, compute-vs-reasoning boundaries |
| **virattt/ai-hedge-fund** | `154a8b2f46dca0f40764d814e4e747b0ad71f4c4` | 2026-09-19 | MIT | General FinTech | ADAPT: First-class `CapletMandate` independent of tickers |
| **gavin-ho1/wharton-investment-comp** | `ac08d15fce77d06064bf8dd7303a6bf04c3ec2f0` | 2026-09-19 | MIT | Yes (Hotchkiss Top 50 Semifinalist 2025-26) | ADAPT: Correlation clustering, deterministic report exhibits |
| **aaravp6/All-Wharton-Investment-Competition** | `9b6a93bb79a4a33298e057bd96be92b149d0cbee` | 2026-09-19 | NONE (Unlicensed) | Yes (Amity 2nd Global 2022-23) | LEARN_ONLY: Client liability survival simulation concept |
| **davidliu-2008/wharton-investment-competition25-26** | `89526f3e284d84c64b2d799739290c9148d42b6d` | 2026-09-19 | NONE (Unlicensed) | Yes (Semifinalist 2025-26) | LEARN_ONLY: Barbell defensive/offensive sleeve concept |

---

## 3. Compliance and Originality Declaration

- **No Code Plagiarism**: No proprietary strategy code, heuristic factor weights, or competition narratives from previous competitors have been copied or reproduced.
- **Unlicensed Repositories Protected**: Code from `aaravp6/All-Wharton-Investment-Competition` and `davidliu-2008/wharton-investment-competition25-26` is strictly classified as `LEARN_ONLY` due to the absence of an open-source license. Zero lines of code have been imported from them.
- **Original Architecture**: All data schemas, valuation models, risk metrics, decision ledgers, and CLI commands were designed and coded specifically for `wharton-ic`.
- **License Compatibility**: All open-source packages and architectural inspirations comply with their respective MIT, Apache-2.0, and BSD licenses.

