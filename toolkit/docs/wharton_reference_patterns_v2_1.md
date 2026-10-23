# Wharton Reference Patterns & Forensic Lessons (Caplet V2.1)

**Inspection Date**: September 19, 2026  
**Audience**: Team Caplet Strategy, Quantitative Research, and Software Architecture  
**Subject**: Comparative analysis of three high-performing Wharton competition repositories:
1. **Hotchkiss — Bullish Bearcats** (`gavin-ho1/wharton-investment-comp`, 2025–26 Top 50 Semifinalist)
2. **Amity 7 Chakras Investments** (`aaravp6/All-Wharton-Investment-Competition`, 2022–23 2nd Globally)
3. **David Liu** (`davidliu-2008/wharton-investment-competition25-26`, 2025–26 Semifinalist)

---

## 1. Forensic Inventory of Competitor Tooling

### A. Hotchkiss — Bullish Bearcats (2025–26 Top 50)
- **Tools Built**:
  - Python scripts (`data_collection.py`, `fundamental_screening.py`, `quant_factor_analysis.py`, `correlation_analysis.py`, `simulation_models.py`, `monitoring.py`, `backtesting.py`, `projection.py`).
  - Report graphic generators in `final-images/` (`create_table.py`, `create_interest_table.py`, `create_metrics_table.py`, `etf-table.py`).
  - Unified configuration in `config.yaml` controlling thresholds across 7 phases.
- **What Mattered Operationally**:
  - The scriptable report table generation (`final-images/`) allowed the team to compile clean, institutional-looking exhibits for their submission directly from computational outputs.
  - Correlation-based clustering ($0.75$ cutoff, $20\%$ sector cap) prevented unintentional overconcentration in correlated tech or growth stocks.
- **What Was Report-Oriented vs. Portfolio-Oriented**:
  - Report-oriented: Automated generation of HTML monitoring summaries and publication-quality CSV/image tables.
  - Portfolio-oriented: Quant factor Z-scores and Monte Carlo return cones.
- **What Was Technically Weak or Redundant**:
  - Subjective `always-include.txt` list: Stocks were manually forced into the portfolio regardless of their quantitative or fundamental scores, creating an obvious tension between objective screening and subjective bias.
  - Arbitrary factor weighting ($72.2\%$ growth, $16.7\%$ quality, $11.1\%$ value) without empirical or client-mandate justification.
  - Retrospective lookahead leakage across historical windows.

### B. Amity 7 Chakras Investments (2022–23 2nd Globally)
- **Tools Built**:
  - Client liability survival Monte Carlo simulation (`monte_carlo_consulting.py`).
  - HTML scrapers for Yahoo Finance growth estimates (`GrowthEstimateScraper.py`).
  - Basic lexicon-based sentiment analysis (`SentimentAnalysis.py`).
- **What Mattered Operationally**:
  - **The Client Liability Survival Simulation**: This was Amity's most significant quantitative contribution. Instead of running generic stock return simulations, they modeled the client's actual cash outflow obligations (initial capital needs, ongoing salary/rent expenses, and $4\%$ inflation over 10–25 years) to compute the **probability of financial survival** (`% survival 10 years`, `% survival 25 years`). Wharton judges prize client-centricity above all else, and this tool proved that the portfolio directly supported the client's life goals.
- **What Was Technically Weak or Redundant**:
  - Unlicensed repository with severe repository hygiene issues (nested virtual environments and IDE caches committed to git).
  - Fragile, unmaintained web scrapers parsing raw HTML.
  - Naive keyword sentiment scoring with no predictive power or point-in-time protections.

### C. David Liu (2025–26 Semifinalist)
- **Tools Built**:
  - Defensive sleeve allocation and drawdown simulation (`defensive_internal_allocations.py`).
  - Mean-variance optimizer (`portfolio_optimization.py`).
  - Historical parameter calculator (`cal_mu_sigma.py`).
- **What Mattered Operationally**:
  - **Barbell Portfolio Sleeve Architecture**: Explicitly structured the portfolio into a $60\%$ defensive sleeve (IG bonds, international ESG, essential services, low-vol equity) and a $40\%$ offensive growth sleeve.
  - Goal probability modeling: Calculating the probability of reaching a target portfolio value while surviving an annual drawdown hurdle.
- **What Was Technically Weak or Redundant**:
  - Hardcoded return and volatility expectations (`assets_data = {"AGG": {"m": 0.045, "v": 0.05}}`) with zero provenance or underlying empirical calibration.
  - Unconstrained Markowitz mean-variance optimization, well-known in institutional finance to be an "error maximizer."

---

## 2. Synthesis: What Team Caplet Must Build vs. What We Must Reject

### What Team Caplet MUST Build (Proven Useful):
1. **Client-Liability Survival Simulation**:
   - Inspired by Amity: Simulate whether the portfolio fulfills the specific client liability schedule (cash flows, inflation, major milestones) rather than generating abstract Sharpe ratios.
2. **Defensive/Offensive Sleeve Framework in the Mandate**:
   - Inspired by David Liu: Formalize portfolio roles (Core Compounders, Defensive Stabilizers, Tactical Reinvestment Cash) as first-class constraints inside `CapletMandate`.
3. **Automated Submission-Ready Report Exhibits**:
   - Inspired by Hotchkiss: Generate deterministic, publication-quality tables and exhibits (`outputs/report_pack/`) with cryptographic provenance hashes and footnote citations.
4. **Correlation & Sector Concentration Firewalls**:
   - Inspired by Hotchkiss: Enforce pairwise correlation maximums and sector ceilings to guarantee genuine structural diversification.

### What Team Caplet MUST NOT Copy (Flawed or Prohibited):
1. **NO Subjective `always-include.txt` Bypasses**: Bypassing research criteria to force pet stocks destroys credibility with judges. Every security must withstand the 11-member council.
2. **NO Arbitrary or Uncalibrated Scoring Weights**: Weights must be derived from the approved client mandate, not plucked from thin air.
3. **NO Fragile Web Scrapers or Unlicensed Code**: Amity and David Liu have no open-source license; their code must never enter Caplet. All market data must route through tested, cached, point-in-time providers.
4. **NO Unconstrained Markowitz Optimization**: Classical mean-variance optimization produces unstable corner solutions. Caplet maintains Hierarchical Risk Parity (HRP) and CVaR-constrained allocation.
5. **NO Uncalibrated Subjective Return Assumptions**: Expected returns must be grounded in reverse DCF market-implied growth rates and audited financial filings.
