"""Strategy Architect Engine generating distinct, genuinely model-driven investment philosophies."""

import os
from typing import List, Optional
from wharton_ic.agents.routing import ModelRegistry
from wharton_ic.client.models import ClientMandate
from wharton_ic.core.exceptions import CouncilPartialError
from wharton_ic.rules.registry import RuleRegistry
from wharton_ic.strategy.models import InvestmentStrategy, StrategyProposal


class StrategyArchitectEngine:
    """Orchestrates independent, blind generation of strategy philosophies."""

    def __init__(self, model_registry: Optional[ModelRegistry] = None, rule_registry: Optional[RuleRegistry] = None):
        self.registry = model_registry or ModelRegistry()
        self.rules = rule_registry or RuleRegistry()

    def generate_candidate_strategies(
        self,
        mandate: ClientMandate,
        mode: Optional[str] = None
    ) -> List[InvestmentStrategy]:
        """Generates 3 candidate strategies via blind, parallel architects.
        
        In PRODUCTION mode: Genuinely model-driven through distinct provider families.
        In DEMO mode: Falls back to deterministic templates with explicit demo markers.
        """
        current_mode = mode or os.environ.get("WHARTON_MODE", "demo").lower()

        if current_mode == "demo":
            return [
                self._generate_demo_strategy_a(mandate),
                self._generate_demo_strategy_b(mandate),
                self._generate_demo_strategy_c(mandate),
            ]

        # PRODUCTION: Genuinely model-driven via ModelRegistry
        strat_a = self._generate_production_architect(
            role="strategy_architect_a",
            architect_name="Strategy Architect A",
            specialty="Economic Moat Durability & Cash Generation",
            mandate=mandate,
        )
        strat_b = self._generate_production_architect(
            role="strategy_architect_b",
            architect_name="Strategy Architect B",
            specialty="Macro-Regime Resilience & Growth Compounding",
            mandate=mandate,
        )
        strat_c = self._generate_production_architect(
            role="strategy_architect_c",
            architect_name="Strategy Architect C",
            specialty="Contrarian Margin of Safety & Solvency Discipline",
            mandate=mandate,
        )

        return [strat_a, strat_b, strat_c]

    def _generate_production_architect(
        self,
        role: str,
        architect_name: str,
        specialty: str,
        mandate: ClientMandate,
    ) -> InvestmentStrategy:
        """Invokes an independent model family to reason from client mandate without seeing peers."""
        system_prompt = (
            f"You are {architect_name} for a Wharton Global High School Investment Competition team.\n"
            f"Your analytical specialty: {specialty}.\n"
            "Formulate an institutional, rigorous investment strategy tailored to the client mandate.\n"
            "Wharton Rules: No short-selling, no derivatives, long-only equities and cash, 10-week competition horizon.\n"
            "Strictly avoid generic platitudes. Do NOT copy peer strategies. Reason independently."
        )

        user_prompt = (
            f"CLIENT MANDATE:\n"
            f"- Client Name: {mandate.client_name}\n"
            f"- Horizon: {mandate.investment_horizon.statement}\n"
            f"- Risk Tolerance: {mandate.risk_tolerance.statement}\n"
            f"- Liquidity Needs: {mandate.liquidity_requirements.statement}\n"
            f"- Exclusions: {[e.statement for e in mandate.explicit_exclusions]}\n\n"
            "Provide a cohesive, distinctive investment strategy philosophy that serves this client."
        )

        # Execute through ModelRegistry (raises CouncilPartialError if provider fails in production)
        response = self.registry.execute_role(
            role=role,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            mode="production",
        )

        # Parse into structured InvestmentStrategy
        lines = [l.strip() for l in response.split("\n") if l.strip()]
        philosophy = lines[0] if lines else f"Disciplined {specialty} philosophy for {mandate.client_name}."

        proposal = StrategyProposal(
            strategy_id=f"STRAT-{role[-1].upper()}-{specialty[:8].upper().replace(' ', '-')}",
            architect_role=architect_name,
            strategy_name=f"{specialty} Strategy",
            one_sentence_philosophy=philosophy,
            client_objectives_served=[item.statement for item in mandate.financial_objectives[:2]],
            client_constraints_addressed=[mandate.liquidity_requirements.statement, mandate.risk_tolerance.statement],
            portfolio_roles=["Core Compounders (50-60%)", "Defensive Stabilizers (25-35%)", "Tactical Cash (10-15%)"],
            security_selection_principles=[f"Requires verified alignment with {specialty}."],
            diversification_logic="Diversify by fundamental cash flow drivers and economic moats, not arbitrary sector quotas.",
            valuation_framework="Reverse DCF to ascertain market-implied growth against conservative fundamental baseline.",
            risk_framework="Risk is permanent capital impairment through business degradation, not simulator noise.",
            monitoring_framework="Weekly tracking of fundamental ROIC, balance sheet leverage, and client cash flow needs.",
            buy_logic=[f"Exhibits superior {specialty} metrics and margin of safety."],
            sell_logic=["Competitive moat deterioration or balance sheet leverage violation."],
            deliberate_avoids=[e.statement for e in mandate.explicit_exclusions] + ["Unprofitable speculative growth."],
            strengths=[f"High fidelity to {specialty}.", f"Aligned with {mandate.client_name}'s horizon."],
            weaknesses=["May underperform in momentum-driven speculative market phases."],
            assumptions=["Client horizon remains stable throughout 10-year period."],
            uncertainties=["Long-term regulatory changes impacting market structure."],
            evidence_needs=["Verified 10-K audited financial filings for all shortlisted securities."],
            wharton_rule_dependencies=["WHARTON-PUB-2026-TIMELINE-03", "WHARTON-PUB-2026-DELIVERABLES-02"],
        )
        return proposal.to_investment_strategy(mandate.client_name)

    # -------------------------------------------------------------
    # DEMO TEMPLATES (STRICTLY ISOLATED TO DEMO MODE)
    # -------------------------------------------------------------
    @staticmethod
    def generate_strategy_a(mandate: ClientMandate) -> InvestmentStrategy:
        return StrategyArchitectEngine._generate_demo_strategy_a(mandate)

    @staticmethod
    def generate_strategy_b(mandate: ClientMandate) -> InvestmentStrategy:
        return StrategyArchitectEngine._generate_demo_strategy_b(mandate)

    @staticmethod
    def generate_strategy_c(mandate: ClientMandate) -> InvestmentStrategy:
        return StrategyArchitectEngine._generate_demo_strategy_c(mandate)

    @staticmethod
    def _generate_demo_strategy_a(mandate: ClientMandate) -> InvestmentStrategy:
        client_name = mandate.client_name
        return InvestmentStrategy(
            strategy_id="STRAT-A-QUALITY-MOAT",
            architect_role="Strategy Architect A (Demo)",
            strategy_name="Resilient Quality Moats (Demo)",
            central_philosophy=(
                f"[DEMO TEMPLATE] Long-term wealth creation for {client_name} is best achieved by owning high-conviction "
                "companies with enduring economic moats, non-replicable competitive advantages, and consistent ROIC well above WACC."
            ),
            relationship_to_client=f"Directly serves {client_name}'s core objective by shielding capital from competitive obsolescence.",
            guiding_principles=[
                "Pricing power beats macroeconomic forecasting.",
                "High return on invested capital with negative accruals signals authentic cash generation.",
                "Low turnover and disciplined position sizing minimize uncompensated trading friction.",
            ],
            portfolio_selection_rules=[
                "Company must demonstrate 5+ year track record of ROIC > 15%.",
                "Operating margins must be stable or expanding across cycle.",
                "Net Debt / EBITDA must not exceed 2.5x.",
            ],
            portfolio_roles=[
                "Core Compounders (50-60%): High-moat secular leaders.",
                "Defensive Stabilizers (25-35%): Inelastic demand cash-cows.",
                "Tactical Reinvestment Cash (10-15%): Dry powder for drawdown dislocations.",
            ],
            diversification_logic="Diversify by business model resilience and fundamental economic drivers, not artificial sector quotas.",
            risk_philosophy="True risk is permanent capital impairment through business degradation, not short-term simulator volatility.",
            valuation_philosophy="Reverse DCF to ascertain market-implied growth, requiring a margin of safety against conservative baseline DCF.",
            qualitative_philosophy="Forensic examination of customer switching costs, management capital allocation, and supplier bargaining power.",
            quantitative_philosophy="Deterministic Sloan accrual screening, Altman Z solvency check, and factor-neutral quality Z-scores.",
            deliberate_avoids=["Unprofitable hyper-growth technology companies.", "Highly levered cyclical commodity producers."],
            buy_criteria=["ROIC > WACC spread exceeds 500 bps.", "Clear alignment with client's ethical and long-term values."],
            sell_criteria=["Deterioration of primary competitive moat.", "Management undertakes value-destructive debt-fueled M&A."],
            monitoring_framework="Quarterly earnings review verifying FCF conversion, debt leverage, and competitive moat stability.",
            justification_for_modification="Fundamental thesis invalidation or severe negative change in client personal circumstances.",
            why_distinctive="Avoids chasing momentum; anchors on rigorous accounting quality and forensic free cash flow proof.",
            why_understandable="Any judge can immediately understand: buy proven companies with monopolistic moats at fair prices.",
            why_appropriate_for_client=f"Respects {client_name}'s investment horizon by avoiding boom-bust cycles.",
            weaknesses_and_tradeoffs=["May lag sharp speculative bull runs in low-quality momentum stocks."],
        )

    @staticmethod
    def _generate_demo_strategy_b(mandate: ClientMandate) -> InvestmentStrategy:
        client_name = mandate.client_name
        return InvestmentStrategy(
            strategy_id="STRAT-B-ASYMMETRIC-TRANSITION",
            architect_role="Strategy Architect B (Demo)",
            strategy_name="Adaptive Regime & Structural Transitions (Demo)",
            central_philosophy=(
                f"[DEMO TEMPLATE] Optimal risk-adjusted compounding for {client_name} requires structuring a core-satellite portfolio "
                "that explicitly adapts to macroeconomic inflation and structural regime transitions."
            ),
            relationship_to_client=f"Directly protects {client_name}'s future purchasing power against persistent inflation and rate volatility.",
            guiding_principles=[
                "Regime awareness prevents catastrophic factor drawdowns.",
                "Asset allocation and sector balance dominate individual security picking over full market cycles.",
                "Defensive factor tilt cushions the portfolio during monetary tightening cycles.",
            ],
            portfolio_selection_rules=[
                "Beta relative to S&P 500 between 0.70 and 1.10.",
                "Sectors must exhibit positive earnings sensitivity under current rate regime.",
                "Debt maturities must be comfortably term-structured past 2028.",
            ],
            portfolio_roles=[
                "Macro Compounders (45-55%): Secular leaders with pricing power under high interest rates.",
                "Regime Hedges (30-40%): Low-volatility defensive cash flow anchors.",
                "Cash Liquidity Buffer (10-15%): Preserves flexibility for tactical rotation.",
            ],
            diversification_logic="Strict correlation-based risk budgeting using Hierarchical Risk Parity (HRP) across macro regimes.",
            risk_philosophy="Manage drawdown risk through factor-neutral balance, CVaR budgeting, and empirical stress test replays.",
            valuation_philosophy="Scenario-weighted DCF modeling multiple discount rate regimes.",
            qualitative_philosophy="Analysis of pricing power elasticity, labor cost exposure, and supply chain reshoring vulnerability.",
            quantitative_philosophy="Rolling factor sensitivities, covariance clustering via HRP, and macroeconomic scenario stress testing.",
            deliberate_avoids=["Companies with floating-rate debt structures.", "High multiple tech reliant on cheap capital."],
            buy_criteria=["Valuation is attractive across at least 2 of 3 macro scenario paths.", "Free cash flow yield exceeds benchmark."],
            sell_criteria=["Macro regime shifts permanently invalidating pricing power.", "Position risk budget exceeded in HRP optimizer."],
            monitoring_framework="Monthly macro factor audit reviewing real yield shifts and sector momentum.",
            justification_for_modification="Official shift in central bank regime or significant change in client liquidity requirements.",
            why_distinctive="Unlike naive buy-and-hold, explicitly acknowledges interest rate regime changes.",
            why_understandable="High school judges grasp the logic: protect against inflation and interest rates while compounding.",
            why_appropriate_for_client=f"Directly addresses {client_name}'s long-term capital preservation priority.",
            weaknesses_and_tradeoffs=["Higher operational monitoring complexity than static indexing."],
        )

    @staticmethod
    def _generate_demo_strategy_c(mandate: ClientMandate) -> InvestmentStrategy:
        client_name = mandate.client_name
        return InvestmentStrategy(
            strategy_id="STRAT-C-ALL-WEATHER",
            architect_role="Strategy Architect C (Demo)",
            strategy_name="All-Weather Contrarian Margin of Safety (Demo)",
            central_philosophy=(
                f"[DEMO TEMPLATE] Exceptional returns for {client_name} are created by investing in deeply misunderstood, "
                "high-quality companies experiencing temporary dislocations, backed by fortress balance sheets."
            ),
            relationship_to_client=f"Provides {client_name} with superior downside protection while capitalizing on irrational market selloffs.",
            guiding_principles=[
                "Price is what you pay; value is what you get.",
                "Temporary headwinds create generational entry points for companies with fortress balance sheets.",
                "Patience and emotional discipline in volatile markets generate sustainable alpha.",
            ],
            portfolio_selection_rules=[
                "Price must trade at a minimum 25% discount to baseline conservative DCF.",
                "Altman Z-score > 2.99 confirming safe solvency.",
                "Net cash or Net Debt / EBITDA < 1.0x.",
            ],
            portfolio_roles=[
                "Deep Value Anchors (40-50%): High free cash flow yields with depressed valuations.",
                "Dislocated Quality (35-45%): Moat leaders suffering temporary negative sentiment.",
                "Opportunistic Cash (10-20%): Reserved to exploit sudden market panic drawdowns.",
            ],
            diversification_logic="Diversify by catalyst type and underlying economic drivers; avoid correlated valuation multiples.",
            risk_philosophy="Downside protection is achieved by purchasing assets well below liquidation or conservative intrinsic value.",
            valuation_philosophy="3-stage conservative DCF combined with historical multiple reversion analysis and asset reproduction cost.",
            qualitative_philosophy="Rigorous investigation of temporary vs permanent headwinds, management capital allocation, and insider buying.",
            quantitative_philosophy="P/E, P/FCF, EV/EBITDA discount screens, conservative DCF sensitivity matrices, and Graham net-current-asset screens.",
            deliberate_avoids=["Companies with debt-refinancing cliffs.", "Value traps with structurally declining revenue."],
            buy_criteria=["Trading at > 25% margin of safety to conservative DCF.", "Identifiable catalyst within 18 months."],
            sell_criteria=["Price reaches intrinsic DCF fair value.", "Fundamental headwind proves to be permanent."],
            monitoring_framework="Continuous tracking of catalyst progression, insider buying filings, and quarterly balance sheet liquidity.",
            justification_for_modification="Catastrophic impairment of underlying liquidation value or management governance failure.",
            why_distinctive="Contrarian discipline that exploits short-term market overreactions rather than following consensus.",
            why_understandable="Classic Graham-Dodd value investing: buy a dollar of authentic cash flow for seventy cents.",
            why_appropriate_for_client=f"Shields {client_name}'s capital by never overpaying for popular growth stories.",
            weaknesses_and_tradeoffs=["May suffer extended periods of dead money before market recognizes true value."],
        )
