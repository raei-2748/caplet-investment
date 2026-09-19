# Data Dictionary & Lineage Specification: `wharton-ic`

This document defines all standard data fields, financial variables, and provenance schemas utilized across the `wharton-ic` investment operating system.

---

## 1. Provenance Schema Fields (`ProvenanceMetadata`)

| Field Name | Type | Description | Example / Allowed Values |
|---|---|---|---|
| `source` | String | Original document or filing source | `"SEC Form 10-K"`, `"Yahoo Finance"` |
| `source_url` | String (Optional) | Direct API endpoint or web URL of origin | `"https://data.sec.gov/..."` |
| `provider` | String | Internal ingestion provider adapter | `"yfinance"`, `"sec_edgar"`, `"fred"` |
| `retrieved_at` | DateTime (UTC) | Exact timestamp when data was pulled | `"2026-09-19T12:00:00Z"` |
| `published_at` | DateTime (UTC) | Public availability or official filing timestamp | `"2025-07-30T21:00:00Z"` |
| `as_of` | Date | Effective point-in-time date for the simulation | `"2025-08-01"` |
| `period_end` | Date (Optional) | End date of the fiscal operating period | `"2025-06-30"` |
| `ticker` | String | Standardized equity or ETF ticker symbol | `"MSFT"`, `"NVDA"`, `"SPY"` |
| `field` | String | Standardized metric or attribute identifier | `"free_cash_flow"`, `"adj_close"` |
| `raw_value` | Any | Value as directly returned by provider | `74070000000.0` |
| `transformed_value` | Any | Cleaned, normalized, or currency-adjusted value | `74.07` |
| `transformation` | String (Optional) | Explicit mathematical formula applied | `"Division by 1e9"` |

---

## 2. Fundamental & Accounting Fields

| Variable | Unit | Definition | Point-in-Time Rule |
|---|---|---|---|
| `revenue` | USD | Total gross corporate revenues | Reported on filed 10-Q / 10-K |
| `operating_income` | USD | Operating income before interest and tax (EBIT) | Filed statement |
| `net_income` | USD | Bottom-line net income attributable to common | Filed statement |
| `operating_cash_flow` | USD | Cash flow from operating activities (CFO) | Filed cash flow statement |
| `capital_expenditures` | USD | Capital reinvestment in property, plant & equip | Cash flow statement |
| `free_cash_flow` | USD | $\text{CFO} - \text{CapEx}$ | Derived calculation |
| `total_assets` | USD | Total balance sheet assets | Filed balance sheet |
| `total_debt` | USD | Short-term + Long-term interest-bearing debt | Filed balance sheet |
| `cash_and_equivalents` | USD | Total liquid cash and marketable securities | Filed balance sheet |
| `shares_outstanding` | Count | Diluted weighted average common shares | Filed statement |
| `roic` | Ratio | $\text{NOPAT} / (\text{Total Debt} + \text{Equity} - \text{Cash})$ | Calculated via `wharton_ic.fundamentals` |
| `fcf_conversion` | Ratio | $\text{Free Cash Flow} / \text{Net Income}$ | Calculated |
| `net_debt_to_ebitda` | Ratio | $(\text{Total Debt} - \text{Cash}) / \text{EBITDA}$ | Calculated |
| `altman_z_score` | Score | Multi-factor balance sheet distress metric | Calculated |
| `accrual_ratio` | Ratio | $(\text{Net Income} - \text{CFO}) / \text{Total Assets}$ | Calculated |

---

## 3. Quantitative Risk & Portfolio Metrics

| Variable | Unit | Definition |
|---|---|---|
| `cagr` | Percentage | Compound Annual Growth Rate over the evaluation period |
| `annualized_volatility` | Percentage | Sample standard deviation scaled by $\sqrt{252}$ |
| `sharpe_ratio` | Ratio | $(\text{CAGR} - R_f) / \sigma_p$ (Excess return per unit total risk) |
| `sortino_ratio` | Ratio | $(\text{CAGR} - R_f) / \sigma_{\text{downside}}$ (Excess return per unit downside risk) |
| `max_drawdown` | Percentage | Peak-to-trough historical or simulated maximum loss |
| `var_95_daily` | Percentage | Daily Value at Risk at 95% confidence level |
| `cvar_95_daily` | Percentage | Expected loss conditional on breaching VaR (Expected Shortfall) |
| `beta` | Ratio | Sensitivity of portfolio returns to SPY benchmark returns |
| `alpha` | Percentage | Annualized excess return above CAPM benchmark expectation |
| `effective_constituents` | Count | $1 / \sum w_i^2$ (Inverse Herfindahl diversification index) |
| `marginal_risk` (MCR) | Percentage | $(\Sigma w)_i / \sigma_p$ (Rate of change of portfolio risk with weight) |
| `turnover` | Percentage | $\sum |w_{\text{new}, i} - w_{\text{old}, i}|$ at each rebalance date |
