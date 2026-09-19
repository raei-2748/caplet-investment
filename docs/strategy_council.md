# Strategy Council, Adversarial Red Team & Human Strategy Gate
**Target**: Team Caplet — Pre-Trading Strategy Formation  
**Competition Phase**: September 15 – September 28, 2026.

---

## 1. Why Strategy Precedes Stock Picking

Wharton rules explicitly state:
> *"A strategy is not merely a collection of stocks. Teams are evaluated on the quality and articulation of their overall investment strategy... Overly technical strategies are not automatically better."*

Top global finalist teams do not begin by scanning stock tickers. They establish an authentic, coherent, and defensible investment philosophy designed around the client's life objectives.

---

## 2. Independent Strategy Formation (Phase 1 Blind)

The `StrategyCouncilEngine` deploys three independent strategy architects who formulate distinct philosophies without seeing each other's work:

### Strategy Architect A: Resilient Quality Moats (RQM)
- **Central Philosophy**: Enduring competitive advantages and non-replicable business moats.
- **Core Screen**: 5+ year track record of ROIC > 15%, negative Sloan accruals, and low financial leverage.
- **Portfolio Roles**: Core Compounders (50-60%), Defensive Stabilizers (25-35%), Tactical Cash (10-15%).
- **Key Edge**: High defensibility during judge Q&A; avoids speculative traps.

### Strategy Architect B: Structural Transitions & Asymmetry (STVA)
- **Central Philosophy**: Capitalizing on structural macroeconomic transitions (automation, energy grid) where market mispricing creates 3:1 asymmetric risk-reward.
- **Core Screen**: Depressed peer multiples with verified operational catalysts.
- **Portfolio Roles**: Structural Catalyst Leaders (40-50%), Cash Flow Moats (30-40%), Risk Hedges (10-20%).
- **Key Edge**: Connects macro industry trends with micro valuation discipline.

### Strategy Architect C: All-Weather Endowment Discipline (AWED)
- **Central Philosophy**: Modeled on university endowments; balances risk contributions across all 4 economic quadrants (Growth, Recession, Inflation, Deflation).
- **Core Screen**: Uncorrelated cash generators and inflation-protected infrastructure.
- **Portfolio Roles**: Growth Drivers (35-40%), Inflation Protectors (20-25%), Defensive Anchors (30-35%).
- **Key Edge**: Mathematical compounding superiority via drawdown minimization.

---

## 3. Adversarial Strategy Red Team

Every candidate strategy is evaluated across six rigorous adversarial lenses:

1. **Client Red Team**: "Where does this fail the client? What if liquidity needs arise early?"
2. **Investment Red Team**: "What assumptions about economic moats are fragile under technological disruption?"
3. **Simplicity Editor**: "Where are financial acronyms (WACC, ROIC, DCF) burying the core human story?"
4. **Originality Auditor**: "Does this sound like a generic Warren Buffett summary, or distinctly Team Caplet?"
5. **Wharton Narrative Critic**: "Will a judge remember this 10 weeks from now during report reading?"
6. **Implementation Critic**: "Can high school students realistically execute this in a 10-week simulator?"

### Team Internal Qualitative Dimensions
Evaluations are categorized into structured qualitative dimensions:
- `Client Fit Assessment`
- `Coherence Assessment`
- `Explainability Assessment`
- `Originality Assessment`
- `Intellectual Defensibility`
- `Practicality for Student Team`

**Mandatory Disclaimer**: These dimensions are explicitly labeled `TEAM INTERNAL REVIEW DIMENSIONS`. The system **never** invents fake Wharton scoring numbers.

---

## 4. The Human Strategy Gate

AI agents propose philosophies and identify flaws. **AI never selects Team Caplet's strategy.**

Approval requires an explicit CLI action:
- Minimum of **two student team signatures** (e.g. Lead Portfolio Manager and Risk Lead).
- Documented student rationale (minimum 20 characters) explaining why this strategy was chosen over the rejected alternatives.
- Preserves rejected alternatives and key disagreements in `decisions/strategy/YYYY-MM-DD_strategy_selection/`.

---

## 5. CLI Workflow

```bash
# Generate candidate strategies and run adversarial red team
wharton-ic strategy run-council

# List candidate strategies and red-team findings
wharton-ic strategy candidates

# Human Strategy Gate: Formally approve the chosen strategy
wharton-ic strategy approve \
  --id "STRAT-A-QUALITY-MOAT" \
  --signer "Ray (Lead PM)" \
  --signer "Sarah (Risk Lead)" \
  --rationale "Chosen unanimously for superior Q&A defensibility and rigorous accounting quality screening." \
  --notes "Debated 10-week catalyst horizon vs quality compounding; selected Quality Moats."

# Display active strategy
wharton-ic strategy show

# Query durable strategy memory for report reflection
wharton-ic strategy memory
```
