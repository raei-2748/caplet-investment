# Reference Integration Forensic Audit (Caplet V2.1)

**Inspection Date**: September 19, 2026  
**Auditor**: Team Caplet Architecture & Quantitative Engineering  
**Scope**: Direct local source-code inspection of 6 required reference repositories.

---

## 1. Executive Summary

This forensic audit evaluates three mature financial AI frameworks (`TradingAgents`, `FinRobot`, `ai-hedge-fund`) and three proven Wharton Investment Competition codebases (`Hotchkiss`, `Amity 7 Chakras`, `David Liu`).

The purpose of this audit is **not** to merge external code blindly, nor to import automatic trading bots. The objective is to identify mature, proven mechanisms that replace V2's simplistic or canned implementations with reference-grounded architecture, while strictly upholding Wharton's rules:
- **Wharton is the Root Configuration**.
- **Numbers from Code, Reasoning from Models, Provenance for Everything**.
- **Mandate Exists Independently of Any Stock**.
- **AI Recommendation $\to$ Human Student Sovereign Decision**.

---

## 2. Detailed Forensic Audit per Repository

### A. TauricResearch/TradingAgents
- **Repository Slug**: `TauricResearch/TradingAgents`
- **Exact Commit SHA**: `2d17df8da1536c121e4d7395ac5a5dcec9e96d6f`
- **Default Branch**: `main`
- **Latest Commit Date**: September 17, 2026, 22:42:27 -0700
- **License**: Apache License 2.0 (Permissive)
- **Primary Directories/Files**:
  - `tradingagents/graph/trading_graph.py` (Graph topology, state propagation)
  - `tradingagents/graph/checkpointer.py` (Per-ticker SQLite checkpointing, `thread_id` with input signature)
  - `tradingagents/graph/reflection.py` (`Reflector` class, outcome review, compact prompt injection)
  - `tradingagents/agents/utils/agent_states.py` (`InvestDebateState`, `RiskDebateState`, typed dicts)
  - `tradingagents/agents/researchers/` (`bull_researcher.py`, `bear_researcher.py`)
  - `tradingagents/agents/risk_mgmt/` (`conservative_debator.py`, `aggressive_debator.py`, `neutral_debator.py`)
  - `tradingagents/agents/managers/` (`research_manager.py`, `portfolio_manager.py`)
- **Architectural Patterns**:
  - Shared Typed State: Explicit state schemas defining conversation histories, speaker turns, and intermediate decisions.
  - Checkpoint and Resume: Deterministic run thread IDs combining ticker, date, and configuration signature (`hashlib.sha256(f"{ticker}:{date}:{sig}".encode()).hexdigest()[:16]`). Resumes at the exact failed node without re-executing completed stages.
  - Multi-Round Adversarial Debate: Iterative debate rounds between Bull and Bear, mediated by a Research Manager who extracts key disagreements and assumptions.
  - Persistent Reflection Memory: Post-decision reflection extracting compact lessons that are fed into future analyst context.
- **Weaknesses & Wharton Incompatibilities**:
  - Direct execution philosophy (`trader` executing orders automatically). In Wharton, AI must never execute trades.
  - Heavy dependence on live scraping and social media sentiment (Reddit, StockTwits) which lacks academic rigor for Wharton judges.
  - Potential lookahead data leakage in retrospective reflection if timestamping is not strictly point-in-time bounded.
- **Integration Classification**: **ADAPT** for state graph, checkpoint hashing, and multi-round debate; **REJECT** for automatic trading and social media scraping.

---

### B. AI4Finance-Foundation/FinRobot
- **Repository Slug**: `AI4Finance-Foundation/FinRobot`
- **Exact Commit SHA**: `6d6ccd32c1b8b1904dc656cf06897438aba3daec`
- **Default Branch**: `master`
- **Latest Commit Date**: September 11, 2026, 22:19:04 +0800
- **License**: Apache License 2.0 (Permissive)
- **Primary Directories/Files**:
  - `finrobot/agents/workflow.py` (Lead-agent orchestration, tool registration, Autogen GroupChat integration)
  - `finrobot/agents/agent_library.py` (Centralized registry of specialist financial agents)
  - `finrobot_equity/core/src/modules/equity_agents/` (Specialized modules: `risks_agent.py`, `valuation_overview_agent.py`, `company_overview_agent.py`)
  - `finrobot_equity/core/src/modules/report_structure.py` (Structured financial report templates)
- **Architectural Patterns**:
  - Specialist Agent Library: Explicit decomposition of investment analysis into modular, role-specific agents registered in a central registry.
  - Tool-Call Boundaries: Strict separation between code-based numerical execution and natural language interpretation.
  - Hierarchical Report Assembly: Structured report sections synthesized from typed agent outputs.
- **Weaknesses & Wharton Incompatibilities**:
  - Auto-generated complete PDF reports: In Wharton, automated ghostwriting violates the competition's academic integrity rules.
  - Hardcoded assumptions in prompt profiles that could introduce bias without student oversight.
- **Integration Classification**: **ADAPT** for specialist agent registration and structured computation-vs-reasoning boundaries; **REJECT** for automated report prose generation.

---

### C. virattt/ai-hedge-fund
- **Repository Slug**: `virattt/ai-hedge-fund`
- **Exact Commit SHA**: `154a8b2f46dca0f40764d814e4e747b0ad71f4c4`
- **Default Branch**: `main`
- **Latest Commit Date**: September 18, 2026, 10:54:20 -0400
- **License**: MIT License (Permissive)
- **Primary Directories/Files**:
  - `hedge_fund/fund/spec.py` (`FundSpec`, `ModelSpec`, `BlendPolicy`, serializable mandate specification)
  - `hedge_fund/models.py` (Order, position, and portfolio representations)
  - `hedge_fund/signals/base.py` (`AlphaModel` interface, signal contract)
  - `hedge_fund/risk/limits.py` (`RiskLimits`, net/gross exposure constraints)
  - `hedge_fund/pipeline/run_cycle.py` (End-to-end rebalance cycle execution)
- **Architectural Patterns**:
  - Mandate as First-Class Object: `FundSpec` defines fund constraints, risk limits, target leverage, and strategy blend policies completely independent of individual tickers.
  - Pluggable Strategy/Model Architecture: Strategies are declarative configurations over signals, completely decoupled from ticker universes.
  - Clean Serializable Data Contracts: Pydantic models with `model_config = ConfigDict(extra="forbid")`.
- **Weaknesses & Wharton Incompatibilities**:
  - Long/Short market-neutral hedge fund assumptions (gross leverage, shorting, borrow fees). Wharton strictly forbids short sales and leverage.
  - Continuous automated rebalancing loops unsuited for Wharton's 10-week low-turnover competition.
- **Integration Classification**: **ADAPT** for first-class mandate modeling (`CapletMandate`); **REJECT** for short-selling and leverage models.

---

### D. Hotchkiss — Bullish Bearcats
- **Repository Slug**: `gavin-ho1/wharton-investment-comp`
- **Exact Commit SHA**: `ac08d15fce77d06064bf8dd7303a6bf04c3ec2f0`
- **Default Branch**: `main`
- **Latest Commit Date**: June 5, 2026, 21:03:30 -0700
- **License**: MIT License (Permissive)
- **Competition Status**: 2025–26 Wharton Global High School Investment Competition Top 50 Semifinalist (Verified via competition records).
- **Primary Directories/Files**:
  - `config.yaml` (End-to-end pipeline settings across 7 phases)
  - `src/fundamental_screening.py` (Percentile cutoffs, Value/Growth/Quality weighting)
  - `src/quant_factor_analysis.py` (Momentum, Volatility, Beta, Sharpe calculation)
  - `src/correlation_analysis.py` (Correlation threshold clustering, max sector weights)
  - `src/simulation_models.py` (Monte Carlo and historical stress simulation)
  - `final-images/create_table.py` (Deterministic table generation for competition report)
- **Architectural Patterns & Strengths**:
  - Phase-based workflow: Clear separation into Data Collection $\to$ Screening $\to$ Factor Analysis $\to$ Correlation $\to$ Allocation $\to$ Stress Testing $\to$ Report Figures.
  - Correlation-based diversification: Used an explicit correlation cutoff ($0.75$) and sector ceilings ($20\%$) to prevent concentrated sector risk.
  - Deliverable-oriented outputs: Output tables directly formatted for the competition report submission.
- **Weaknesses & Wharton Incompatibilities**:
  - Hardcoded `always-include.txt`: Bypassed quantitative screening for favored stocks without documented rationale, introducing subjective bias.
  - Retrospective lookahead risks: Mixed in-sample and out-of-sample data in factor scoring.
  - Arbitrary screening weights ($72.2\%$ growth, $11.1\%$ value) lacking client-mandate derivation.
- **Integration Classification**: **ADAPT** for report-table automation and correlation clustering workflows; **REJECT** for arbitrary factor weights and `always-include` bypasses.

---

### E. Amity 7 Chakras Investments
- **Repository Slug**: `aaravp6/All-Wharton-Investment-Competition`
- **Exact Commit SHA**: `9b6a93bb79a4a33298e057bd96be92b149d0cbee`
- **Default Branch**: `main`
- **Latest Commit Date**: September 1, 2024, 16:33:13 -0400
- **License**: **NO LICENSE FILE** (Unlicensed / All Rights Reserved)
- **Competition Status**: 2nd Place Globally, 2022–23 Wharton Global High School Investment Competition (Verified).
- **Primary Directories/Files**:
  - `WhartonInvestmentCompetition2023/monte_carlo_consulting.py` (Client liability survival simulation)
  - `WhartonInvestmentCompetition2022/PythonCode/GrowthEstimateScraper.py` (Consensus estimates)
  - `WhartonInvestmentCompetition2022/PythonCode/SentimentAnalysis.py` (Lexicon sentiment)
- **Architectural Patterns & Strengths**:
  - Client-Goal Survival Simulation: Rather than running abstract Monte Carlo simulations of portfolio variance, Amity modeled the client's actual liability schedule (salary expenses, initial capital expenditures, inflation adjustments over 10–25 years) to calculate the **probability of goal survival** (`% survival 10 years`, `% survival 25 years`). This directly connected quantitative finance to the client mandate.
- **Weaknesses & Wharton Incompatibilities**:
  - Unlicensed repository: Code cannot be copied legally.
  - Poor repository hygiene: Nested `venv` directories committed directly to git; unorganized scripts without testing or packaging.
  - Fragile web scraping (`GrowthEstimateScraper.py` parsing raw HTML).
- **Integration Classification**: **LEARN_ONLY** (strictly no code copying due to absence of license). Adapt the conceptual insight: **Monte Carlo simulations must model client liability survival probabilities, not generic abstract returns.**

---

### F. David Liu — 2025–26 Wharton Repository
- **Repository Slug**: `davidliu-2008/wharton-investment-competition25-26`
- **Exact Commit SHA**: `89526f3e284d84c64b2d799739290c9148d42b6d`
- **Default Branch**: `main`
- **Latest Commit Date**: February 22, 2026, 16:49:21 -0500
- **License**: **NO LICENSE FILE** (Unlicensed / All Rights Reserved)
- **Competition Status**: 2025–26 Wharton Semifinalist campaign (Claimed in repository).
- **Primary Directories/Files**:
  - `defensive_internal_allocations.py` (Defensive sleeve allocation and goal-probability Monte Carlo)
  - `portfolio_optimization.py` (Markowitz mean-variance optimization)
  - `cal_mu_sigma.py` (Historical return and volatility estimation)
- **Architectural Patterns & Strengths**:
  - Barbell Portfolio Sleeve Architecture: Divided portfolio into a 60% defensive sleeve (`ig_bonds`, `intl_esg`, `essential_svc`, `low_vol_equity`) and a 40% offensive growth sleeve.
  - Goal Probability Metric: Evaluated win rate defined as reaching client target wealth ($1,000,000$) subject to annual drawdowns ($10,000$).
- **Weaknesses & Wharton Incompatibilities**:
  - Unlicensed repository: Code cannot be copied legally.
  - Subjective, hardcoded expected return and volatility parameters (`m=0.045, v=0.05`) without verifiable provenance links.
  - Simple mean-variance optimization sensitive to estimation error.
- **Integration Classification**: **LEARN_ONLY** (strictly no code copying due to absence of license). Adapt the conceptual insight: **explicit defensive/offensive portfolio sleeve categorization aligned with client drawdown constraints.**

---

## 3. Forensic Comparison & Synthesis

| Repository | License | Verified Wharton Outcome? | Primary Architectural Strength | Primary Weakness | Caplet Classification |
|:---|:---|:---|:---|:---|:---|
| **TradingAgents** | Apache-2.0 | N/A (General FinTech) | Graph state, deterministic checkpointing, multi-round debate | Auto-trading, social media noise | **ADAPT** |
| **FinRobot** | Apache-2.0 | N/A (General FinTech) | Specialist agent library, computation/reasoning boundary | Auto-written PDF reports (ghostwriting) | **ADAPT** |
| **ai-hedge-fund** | MIT | N/A (General FinTech) | First-class `FundSpec` mandate independent of tickers | Short-selling & leverage assumptions | **ADAPT** |
| **Hotchkiss** | MIT | Yes (2025-26 Top 50 Semifinalist) | Multi-phase pipeline, correlation clustering, report table scripts | Arbitrary factor weights, `always-include` bypass | **ADAPT** |
| **Amity 7 Chakras** | NONE | Yes (2022-23 2nd Global) | Client liability survival simulation | Unlicensed, fragile scrapers, poor hygiene | **LEARN_ONLY** |
| **David Liu** | NONE | Yes (2025-26 Semifinalist) | Barbell sleeve structure (60% defensive / 40% offensive) | Unlicensed, hardcoded parameters | **LEARN_ONLY** |
