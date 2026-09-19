# Mandate as a First-Class Object Architecture (Caplet V2.1)

Adapted from `virattt/ai-hedge-fund` (`FundSpec`), the **Caplet Mandate** architecture decouples the investment mandate from individual stock selection.

---

## 1. Core Architectural Principle

> **A Caplet Investment Mandate exists independently of any stock.**

In naive competition workflows, teams begin by picking popular stocks (e.g. Nvidia, Apple) and retrofitting a narrative to justify them. In institutional asset management and Wharton competition judging, this is an immediate failure mode.

The Caplet V2.1 hierarchy enforces a strict top-down operational flow:
```
Wharton Rules Snapshot (Official Constraints)
      ↓
Client Mandate (Verified Facts, Horizons, Ethics)
      ↓
Caplet Mandate (Strategic Sleeves, Role Definitions, Decision Thresholds)
      ↓
Approved Strategy (Investment Philosophy & Principles)
      ↓
Portfolio Role Framework (Core Compounders, Defensive Stabilizers, Tactical Cash)
      ↓
Research Criteria (ROIC Hurdles, Reverse DCF Margin of Safety)
      ↓
Approved Security Universe (Official Wharton CSV)
      ↓
Candidate Securities
```

---

## 2. Key Components of `CapletMandate`

1. **Objective Hierarchy**: Prioritized list of client life goals (e.g., secular growth vs. income preservation).
2. **Risk Philosophy**: Quantitative drawdown boundaries and risk tolerance definitions.
3. **Portfolio Role Framework**:
   - **Core Compounders ($45\%\text{--}65\%$)**: High ROIC, durable moats, secular tailwinds.
   - **Defensive Stabilizers ($20\%\text{--}35\%$)**: Inelastic demand, low beta, strong balance sheets.
   - **Tactical Cash Reserve ($5\%\text{--}15\%$)**: Buffer for market dislocation rebalancing and liquidity.
4. **Evaluation Principles**: Minimum economic hurdle rates (e.g., ROIC > WACC spread $\ge 300$ bps).
5. **Forbidden Exposures**: Negative ESG screens and exclusions derived directly from client instructions.
6. **Decision & Rebalancing Thresholds**: Position sizing ceilings ($20\%$), floor ($5\%$), and turnover limits.

---

## 3. Ticker-Independence Validation

`CapletMandate` enforces a programmatic Pydantic validator: **no stock tickers may appear in the mandate**. If any ticker string is detected, initialization fails immediately. This guarantees that strategy and portfolio roles are defined purely on client requirements before any individual company is evaluated.
