# Architectural Benchmark: `wharton-ic` vs. Previous Wharton Competitor Systems

This document benchmarks the software and quantitative infrastructure of `wharton-ic` against publicly available codebases from past Wharton Global High School Investment Competition finalists and semifinalists.

> [!IMPORTANT]
> **Benchmarking Disclaimer**:
> This document evaluates *infrastructure, data integrity, mathematical rigor, and governance*. It does not assert that our investment strategy or simulated stock returns are superior, as market outcomes depend on unpredictable macroeconomic regimes. Our objective is to prove that `wharton-ic` provides a vastly more rigorous, reproducible, and defensible institutional platform for student analysts.

---

## 1. Feature Matrix & Infrastructure Comparison

| Dimension | Amity 2nd Global (`aaravp6`) | Hotchkiss Semifinalist (`gavin-ho1`) | David Liu Semifinalist (`davidliu-2008`) | Adam Mawani (`TradingAlgorithms`) | Iraj Shroff (`Blast-Strategy`) | **`wharton-ic` (Our System)** |
|---|---|---|---|---|---|---|
| **Software Architecture** | Ad-hoc scripts; committed 25k venv files | Modular YAML scripts | Flat standalone scripts | Monolithic ML scripts | Standalone Black-Litterman script | **Production `src/` Python package (`uv`, Pydantic, Typer CLI)** |
| **Point-in-Time Integrity** | ❌ None (look-ahead bias) | ❌ Static 2025 pickle applied across 25 years | ❌ Static historical CSVs | ❌ Global min-max scaling across time series | ❌ Retrospective view formulation | **✅ Enforced Point-in-Time store (`filing_date <= as_of`)** |
| **Data Provenance** | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | **✅ Full lineage (`source`, `url`, `as_of`, `transformation`)** |
| **Approved Universe Engine** | ❌ Hardcoded strings | ⚠️ Unvalidated text files | ⚠️ Manual CSVs | ❌ General S&P 500 | ❌ Scraping script | **✅ Authoritative Wharton universe validator & sector indexer** |
| **Screening Methodology** | Naive web sentiment | Heuristic weights (`Growth: 0.72`) + `always-include` bypass | Basic offensive / defensive split | Price indicators (RSI, Bollinger) | Basic stock screener | **✅ Winsorized, sector-neutral z-scores; 4 multi-model comparisons** |
| **Valuation Modeling** | ❌ None | ❌ None (only price ratios) | ❌ None | PE ratio baseline | ❌ None | **✅ Deterministic Multi-stage DCF, WACC, Reverse DCF, Comps, 2D Sensitivity** |
| **Portfolio Optimization** | ❌ None | Markowitz QP (Unconstrained) | Mean-Variance | ❌ None | Black-Litterman (Heuristic views) | **✅ `skfolio` 8-model suite (HRP, CVaR, Risk Budgeting, Max Sharpe) with Wharton box & sector caps** |
| **Constraint Enforcement** | ❌ None | ⚠️ Sector post-filter | ❌ None | ❌ None | ❌ None | **✅ CVXPY quadratic projection for 2.5% min, 15% max, 25% sector cap** |
| **Backtest Methodology** | ❌ None | Retrospective in-sample simulation | ❌ None | Train/test split with leakage | ❌ None | **✅ Walk-forward rolling out-of-sample backtester with turnover friction** |
| **Tail Risk & Scenarios** | ❌ None | Single historical drop | ❌ None | GBM Brownian motion | ❌ None | **✅ Crisis replays (2008, 2020, 2022), macro factor shocks, 5,000-path fat-tailed Student-t Monte Carlo** |
| **AI Governance & Council** | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | **✅ Independent multi-model council (Blind Phase A/B, Bull/Bear debate, Evidence Audit)** |
| **Decision Logging** | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | **✅ Immutable Decision Ledger (`00_metadata` to `15_human_decision`)** |
| **Human Approval Gate** | ❌ N/A | ❌ N/A | ❌ N/A | ❌ N/A | ❌ N/A | **✅ Mandatory human student signature block in `15_human_decision.md`** |
| **Wharton Report Pack** | Manual copy-paste | HTML / CSV export | Matplotlib plots | Streamlit UI | Terminal printout | **✅ Automated Report Pack: audited tables, figures, captions, and `AI_USE.md`** |

---

## 2. In-Depth Case Comparisons

### 2.1 vs. `gavin-ho1/wharton-investment-comp` (The Hotchkiss School - Semifinalist)
- **What Hotchkiss Did Well**: Hotchkiss demonstrated strong organizational maturity by parameterizing their workflow via `config.yaml` and exporting automated HTML tables for their final report.
- **Where Hotchkiss Fell Short**:
  1. *Look-Ahead Bias*: Hotchkiss pickled single-point fundamental data in November 2025 (`fundamentals_2025-11-10.pkl`) and applied those 2025 ratios to evaluate historical performance across a 25-year backtest window.
  2. *Subjective Overrides*: They included an `always_include_filename: 'stock-lists/always-include.txt'` configuration that bypassed their quantitative model for favored stocks, compromising quantitative objectivity.
  3. *Arbitrary Factor Weights*: Their fundamental screening model assigned fixed weights (`Growth: 0.7222`, `Value: 0.1111`, `Quality: 0.1666`) without statistical testing.
  4. *Lack of Intrinsic Valuation*: No DCF, WACC, or intrinsic valuation models were implemented; selection relied entirely on market price multiples and historical momentum.
- **How `wharton-ic` Improves**: `wharton-ic` eliminates look-ahead bias via strict point-in-time stores (`PointInTimeStore`), replaces subjective overrides with formal Client Fit scoring and audited decision ledgers, benchmarks multiple factor models, and provides institutional DCF and reverse DCF engines.

### 2.2 vs. `aaravp6/All-Wharton-Investment-Competition` (Amity - 2nd Place Global)
- **What Amity Did Well**: Successfully impressed judges by tying macroeconomic news sentiment to analyst growth expectations over three consecutive competition cycles.
- **Where Amity Fell Short**:
  1. *Codebase Hygiene*: Committed over 25,000 files including `.idea` settings and an entire Windows `.venv` virtual environment directly into Git.
  2. *Fragile Scrapers*: Depended on web scrapers targeting specific HTML tags on financial blogs, which broke when page designs changed.
  3. *Unconstrained Allocation*: Did not implement mathematical portfolio optimization or formal risk constraint enforcement.
- **How `wharton-ic` Improves**: Clean modern Python architecture managed by `uv` and `pyproject.toml`, robust API data providers with offline simulation fallbacks, convex portfolio optimization with strict Wharton constraints, and comprehensive automated test suites.

### 2.3 vs. `TauricResearch/TradingAgents` & `virattt/ai-hedge-fund`
- **What They Did Well**: Popularized multi-agent financial personas and adversarial Bull/Bear debates.
- **Where They Fell Short**:
  1. *LLM Arithmetic Hallucination*: Allowed LLMs to perform arithmetic calculations and ratio evaluations in natural language tokens.
  2. *Unconstrained Black Boxes*: High cost, high latency, and lack of reproducible point-in-time data storage.
- **How `wharton-ic` Improves**: Strictly adheres to Principle A: "Numbers from code; reasoning from models." Vectorized Python engines compute 100% of mathematical figures, and language models are restricted to qualitative synthesis, adversarial debate, and evidence auditing.
