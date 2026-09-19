# Reference Repository Audit & Architectural Deconstruction

This document records the forensic technical audit of nine reference codebases conducted prior to designing and implementing `wharton-ic`.

---

## 1. Wharton Competitor Repositories

### 1.1 `aaravp6/All-Wharton-Investment-Competition`
* **Result / Relevance**: 2nd Place Global Finalist (2022–2023 Wharton Global High School Investment Competition) across three competition cycles (2020-2023).
* **Architecture**: Script-based collection (`main.py`, `GrowthEstimateScraper.py`, `SentimentAnalysis.py`) across yearly folders. Monolithic virtual environment checked into Git (25,000+ files committed into repo).
* **Useful Concepts**: Sentiment scoring linked to growth estimation; automated scraping of analyst consensus growth.
* **Useful Code**: Basic pattern for scraping consensus growth projections.
* **Weaknesses**:
  - Committed entire `.venv` / `site-packages` into version control.
  - Zero modularity or configuration management; hardcoded ticker lists and scrapers.
  - Fragile web scraping without fallback or rate-limiting.
  - Naïve sentiment scoring (VADER/TextBlob without financial context).
* **Methodological Risks**: Survivor bias; lack of robust financial statement reconciliation; no formal portfolio risk constraints.
* **Data Issues**: Relied on scraping live web pages that break when HTML changes; unvalidated data schemas.
* **Look-Ahead Concerns**: Severe. Backtests and estimates intermingled historical prices with current analyst sentiment.
* **Dependencies**: `beautifulsoup4`, `nltk`, `pandas`, `requests`.
* **License**: None specified (All rights reserved by author).
* **What we will reuse directly**: None.
* **What we will reimplement**: Clean, structured analyst consensus ingestion via resilient API providers.
* **What we will reject**: Scraping unverified blog HTML, committing virtual environments, unconstrained sentiment-based ranking.
* **How our system improves**: Production Python package with strict schemas, decoupled data providers, point-in-time provenance, and deterministic financial accounting.

---

### 1.2 `gavin-ho1/wharton-investment-comp` (The Hotchkiss School - Bullish Bearcats)
* **Result / Relevance**: Semifinalist (Top 50 globally, 2025–2026 Wharton Competition).
* **Architecture**: YAML config-driven multi-phase pipeline (`config.yaml` -> `src/data_collection.py` -> `src/fundamental_screening.py` -> `src/quant_factor_analysis.py` -> `src/portfolio_optimization.py` -> `src/backtesting.py` -> `src/projection.py`).
* **Useful Concepts**: Clean phase separation; declarative YAML configuration; automated HTML/CSV report tables and charts for Final Report inclusion; sector distribution controls.
* **Useful Code**: Clean configuration structure and automated generation of report-ready metrics tables.
* **Weaknesses**:
  - Hardcoded heuristic weights (e.g. `Growth: 0.7222`, `Value: 0.1111`, `Quality: 0.1666`) without out-of-sample statistical justification.
  - `always_include_filename` mechanism bypassed the quantitative screening model for favored stocks.
  - Single-point fundamentals pickle (`fundamentals_2025-11-10.pkl`) applied across decades of price history.
  - Optimization relied on basic Markowitz quadratic programming without robust covariance estimators or tail risk bounds.
* **Methodological Risks**: Overfitting to recent bull-market regimes; high growth factor weighting ignores valuation risk.
* **Data Issues**: Pickled data files without schema evolution or provenance tracking.
* **Look-Ahead Concerns**: Critical look-ahead leakage in backtesting: historical prices over 25 years were evaluated against 2025 fundamental ratios.
* **Dependencies**: `yfinance`, `pandas`, `numpy`, `scipy`, `matplotlib`, `pyyaml`.
* **License**: MIT License.
* **What we will reuse directly**: Structural concept of declarative YAML pipeline configuration and automated Final Report table generation.
* **What we will reimplement**: Clean factor definitions, multi-model portfolio optimizers, and automated chart exports.
* **What we will reject**: Pickled static fundamentals for long backtests, arbitrary unvalidated factor weights, and "always-include" rule overrides.
* **How our system improves**: Genuine point-in-time fundamental databases, walk-forward out-of-sample testing, `skfolio` risk budgeting/CVaR, and comprehensive client mandate integration.

---

### 1.3 `davidliu-2008/wharton-investment-competition25-26`
* **Result / Relevance**: Semifinalist (2025–2026 Wharton Competition).
* **Architecture**: Procedural scripts (`config.py`, `cal_mu_sigma.py`, CSV price cache).
* **Useful Concepts**: Division of universe into offensive and defensive assets; basic ESG / client values filtering.
* **Useful Code**: Statistical calculation of asset return expectations and correlation matrices.
* **Weaknesses**:
  - Flat scripts without CLI or package structure.
  - Manual CSV maintenance for individual tickers.
  - Naïve mean-variance assumptions (historical $\mu, \sigma$ as expected future return/risk).
* **Methodological Risks**: Extreme estimation error in expected returns leading to corner portfolios (concentrated weights).
* **Data Issues**: Static CSV files with no provenance or automated update mechanism.
* **Look-Ahead Concerns**: High risk of survivorship and selection bias from retrospective universe curation.
* **Dependencies**: `numpy`, `pandas`, `matplotlib`.
* **License**: None specified.
* **What we will reuse directly**: None.
* **What we will reimplement**: Offensive/defensive asset role categorization mapped directly to client mandate rules.
* **What we will reject**: Static CSV data reliance and unconstrained mean-variance optimization.
* **How our system improves**: Shrinkage covariance estimators, robust risk parity/CVaR, automated data caching with integrity hashing.

---

### 1.4 `AdamMawani/TradingAlgorithms`
* **Result / Relevance**: Historical baseline / competitor-associated library.
* **Architecture**: Monolithic collection of disparate ML and econometric scripts (LSTM, RNN, ARIMA, GARCH, Brownian Monte Carlo, Streamlit UI).
* **Useful Concepts**: GARCH volatility modeling; Monte Carlo Brownian motion forecasting; VaR estimation.
* **Useful Code**: GARCH parameterization patterns and VaR implementations.
* **Weaknesses**:
  - Neural networks (LSTM/RNN) applied directly to raw non-stationary stock prices without walk-forward cross-validation.
  - Heavy model complexity with negative or zero out-of-sample risk-adjusted value.
  - Disconnected from Wharton rules, client mandates, and fundamental business valuation.
* **Methodological Risks**: Severe data snooping and overfitting; "black box" deep learning models fail Wharton defense.
* **Data Issues**: No corporate action adjustments; look-ahead scaling across full time series.
* **Look-Ahead Concerns**: Global feature scaling (MinMaxScaler fitted on entire dataset before train/test split).
* **Dependencies**: `tensorflow`, `keras`, `arch`, `statsmodels`, `streamlit`, `scikit-learn`.
* **License**: None specified.
* **What we will reuse directly**: None.
* **What we will reimplement**: Parametric and historical VaR / CVaR, calibrated Monte Carlo simulations with distributional sanity checks.
* **What we will reject**: Deep learning price predictors and black-box neural networks.
* **How our system improves**: Adheres to Principle G ("Simple Must Beat Complex"), benchmarking any model against naïve baselines.

---

### 1.5 `IrajShroff/Wharton-Investment-Competition---Blast-Strategy`
* **Result / Relevance**: Semifinalist (Top 50, 2024–2025 Wharton Competition).
* **Architecture**: Black-Litterman model implementation (`blm.py`, `blm_inputs.py`, `stockPicker.py`, `etfPicker.py`).
* **Useful Concepts**: Black-Litterman asset allocation combining market equilibrium prior with investor subjective views.
* **Useful Code**: Formulation of the Black-Litterman master formula ($\tau, P, Q, \Omega$).
* **Weaknesses**:
  - Highly subjective "views" matrix ($Q$) hardcoded without transparent empirical derivation.
  - Limited universe support; brittle ticker scraping.
  - No adversarial validation or stress testing of view uncertainty.
* **Methodological Risks**: Ill-conditioned view covariance matrix ($\Omega$) producing unstable portfolio allocations.
* **Data Issues**: Unverified input parameters.
* **Look-Ahead Concerns**: Views formulated using knowledge of subsequent price performance.
* **Dependencies**: `numpy`, `pandas`, `scipy`.
* **License**: MIT License.
* **What we will reuse directly**: Conceptual foundations of Bayesian view integration.
* **What we will reimplement**: Formal subjective/quantitative view generation anchored in deterministic valuation spreads.
* **What we will reject**: Arbitrary view generation without audited justification.
* **How our system improves**: Mathematical rigor in view confidence modeling and full comparison against Equal Weight and Min-Var baselines.

---

## 2. Institutional AI & Quantitative Frameworks

### 2.1 `TauricResearch/TradingAgents`
* **Result / Relevance**: State-of-the-art multi-agent financial framework with over 100,000 GitHub stars.
* **Architecture**: Multi-agent graph containing specialized analysts (Fundamental, Technical, Sentiment, Valuation), Bull/Bear debate, Risk Management, and Portfolio Execution.
* **Useful Concepts**:
  - Independent analyst specialization.
  - Adversarial Bull vs. Bear structured debate.
  - Distinct Risk Officer oversight with portfolio veto power.
  - Immutable persistent decision logs.
* **Useful Code**: Debate prompt schemas and turn-taking orchestration patterns.
* **Weaknesses**:
  - Agents often execute numeric arithmetic in LLM tokens rather than deterministic Python code.
  - Heavy reliance on external LLM APIs for metrics that should be calculated via vectorized NumPy.
  - High execution cost and latency for simple portfolio screening.
* **Methodological Risks**: Hallucination of financial statistics, P/E multiples, and DCF growth rates.
* **Data Issues**: Real-time web retrieval can introduce non-deterministic results across runs.
* **Look-Ahead Concerns**: RAG search queries can retrieve post-dated news during historical simulations.
* **Dependencies**: `langchain` / `langgraph`, `pydantic`, `rich`.
* **License**: Apache-2.0.
* **What we will reuse directly**: Concepts of independent analyst roles, adversarial Bull/Bear debate, and structured committee review.
* **What we will reimplement**: Multi-phase independent analysis where models cannot see each other's outputs initially.
* **What we will reject**: LLM-based arithmetic, unconstrained web browsing during backtests.
* **How our system improves**: Strict adherence to Principle A: "Numbers from code; reasoning from models".

---

### 2.2 `AI4Finance-Foundation/FinRobot`
* **Result / Relevance**: Open-source AI Agent platform for financial analysis backed by AI4Finance.
* **Architecture**: Hierarchical agent framework dividing tasks into Financial Perception, Financial Brain, and Financial Tools (smart valuation, financial statement modeling, report generation).
* **Useful Concepts**:
  - Explicit separation between deterministic financial tools (DCF engines) and LLM synthesis.
  - Investment Committee Memo generation.
  - Evidence linking and numerical provenance.
* **Useful Code**: Structured financial memo templates and DCF sensitivity parameterization.
* **Weaknesses**:
  - Complex configuration overhead; tight coupling to specific AutoGen / LLM library primitives.
  - Inconsistent handling of multi-model failover.
* **Methodological Risks**: Complex agent abstractions obscure underlying quantitative calculations.
* **Data Issues**: Financial statement formatting inconsistencies across disparate SEC filings.
* **Look-Ahead Concerns**: Tool execution must be strictly scoped to `as_of` timestamp.
* **Dependencies**: `autogen`, `pydantic`, `pandas`, `yfinance`.
* **License**: Apache-2.0.
* **What we will reuse directly**: Architecture pattern separating deterministic financial tools from LLM synthesis.
* **What we will reimplement**: Clean, standalone deterministic valuation engines (DCF, WACC, Comps, Reverse DCF) with zero framework lock-in.
* **What we will reject**: Heavy multi-layer agent orchestration frameworks that hinder determinism.
* **How our system improves**: Minimalist, auditable Python modules with explicit Pydantic input/output schemas.

---

### 2.3 `virattt/ai-hedge-fund`
* **Result / Relevance**: Popular multi-agent hedge fund simulation (>60,000 stars).
* **Architecture**: Specialized persona agents (Warren Buffett, Bill Ackman, Cathie Wood, Charlie Munger, Ben Graham, Risk Manager, Portfolio Manager).
* **Useful Concepts**:
  - Mandate abstraction (formal client investment parameters).
  - Explicit capital allocation and fund state management.
  - Backtestable mandate runner.
* **Useful Code**: Structured schema for agent signals and portfolio manager weight aggregation.
* **Weaknesses**:
  - Agents often act as simplistic prompt personas rather than rigorous empirical models.
  - Lack of deep financial statement decomposition or balance sheet forensics.
  - No point-in-time database backing historical agent decisions.
* **Methodological Risks**: Persona caricature over empirical finance.
* **Data Issues**: Shallow financial metrics passed into prompts.
* **Look-Ahead Concerns**: Relies on present-day knowledge encoded into model weights.
* **Dependencies**: `langchain`, `pydantic`, `yfinance`.
* **License**: MIT License.
* **What we will reuse directly**: Formal Mandate abstraction connecting client goals to portfolio decisions.
* **What we will reimplement**: Client Steward role enforcing client constraints rather than cartoonish investor personas.
* **What we will reject**: Subjective persona prompting without underlying financial evidence.
* **How our system improves**: Deep financial accounting (ROIC, Altman Z, Piotroski F, accruals) provided deterministically to the council.

---

### 2.4 `skfolio/skfolio`
* **Result / Relevance**: Leading institutional Python library for portfolio optimization built on top of scikit-learn.
* **Architecture**: Fully scikit-learn compliant estimators for MeanRisk, Minimum Variance, Maximum Sharpe, CVaR, Equal Risk Contribution (Risk Budgeting), Hierarchical Risk Parity (HRP), Hierarchical Equal Risk Contribution (HERC), and Nested Clustered Optimization (NCO).
* **Useful Concepts**:
  - Unified estimator API (`fit`, `predict`).
  - Integrated walk-forward and combinatorial cross-validation.
  - Mathematical robustness with CVXPY convex solvers.
  - Native support for portfolio weight constraints, transaction costs, and turnover constraints.
* **Useful Code**: Use directly as the core quantitative portfolio engine.
* **Weaknesses**:
  - Purely quantitative library; has no concept of client mandates, Wharton rules, qualitative theses, or evidence logging.
* **Methodological Risks**: Optimization without shrinkage or constraints can result in unrealistic turnover or concentration.
* **Data Issues**: Requires clean, synchronized return series.
* **Look-Ahead Concerns**: Must be wrapped in strict walk-forward cross-validation pipelines.
* **Dependencies**: `scikit-learn`, `cvxpy`, `scipy`, `numpy`.
* **License**: BSD-3-Clause.
* **What we will reuse directly**: `skfolio` optimization estimators (MeanRisk, Max Sharpe, Min Vol, CVaR, RiskBudgeting, HRP).
* **What we will reimplement**: Wharton-specific constraint wrappers (min/max weights, sector limits, cash buffer, trade count limits).
* **What we will reject**: None (we embrace `skfolio` as our authoritative numerical portfolio optimizer).
* **How our system improves**: Embeds `skfolio` within an audited, client-constrained, point-in-time Wharton competition operating system.

---

## 3. Summary of Core Architectural Principles Derived from Audit

| Flaw Identified in Reference Repos | Our Architectural Solution |
|---|---|
| Pickled static fundamentals applied across 25 years (`gavin-ho1`) | Point-in-time data store with strict filing date vs. period end date enforcement. |
| Hardcoded, arbitrary factor weights (e.g. `Growth: 0.7222`) | Cross-sectional percentile ranking with transparent, configurable factor families. |
| LLMs calculating financial arithmetic and P/E ratios (`TradingAgents`) | 100% deterministic valuation and risk calculations in pure Python (`src/wharton_ic/valuation`). |
| "Always-include" override lists that bypass quantitative models | Formal Client Fit scoring and human investment committee approval gate. |
| Black-box neural networks predicting raw prices (`AdamMawani`) | Principle G: Simple must beat complex; evaluate all models against naïve baselines. |
| Commit of virtual environment and secret keys (`aaravp6`) | Clean `src/` layout, `pyproject.toml`, `.env.example`, and strict `.gitignore`. |
| Unconstrained single-optimizer output presenting a false sense of certainty | Multi-optimizer comparison (Equal Weight, InvVol, Max Sharpe, CVaR, HRP) against SPY benchmark. |
