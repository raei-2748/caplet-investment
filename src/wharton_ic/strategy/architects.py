"""Independent Strategy Architects generating distinct investment philosophies."""

from typing import List, Optional
from wharton_ic.client.models import ClientMandate
from wharton_ic.strategy.models import InvestmentStrategy


class StrategyArchitectEngine:
    """Orchestrates independent, blind generation of strategy philosophies."""

    @staticmethod
    def generate_strategy_a(mandate: ClientMandate) -> InvestmentStrategy:
        """Strategy Architect A: Resilient Quality Moats & Cash Flow Durability."""
        client_name = mandate.client_name
        return InvestmentStrategy(
            strategy_id="STRAT-A-QUALITY-MOAT",
            architect_role="Strategy Architect A",
            strategy_name="Resilient Quality Moats (RQM)",
            central_philosophy=(
                f"Long-term wealth creation for {client_name} is best achieved by owning high-conviction companies "
                "with enduring economic moats, non-replicable competitive advantages, and consistent ROIC well above WACC."
            ),
            relationship_to_client=(
                f"Directly serves {client_name}'s core objective by shielding capital from competitive obsolescence "
                "while capturing sustained secular compounding without speculative forecasting."
            ),
            guiding_principles=[
                "Pricing power beats macroeconomic forecasting.",
                "High return on invested capital with negative accruals signals authentic cash generation.",
                "Low turnover and disciplined position sizing minimize uncompensated trading friction.",
            ],
            portfolio_selection_rules=[
                "Company must demonstrate 5+ year track record of ROIC > 15%.",
                "Operating margins must be stable or expanding across cycle.",
                "Net Debt / EBITDA must not exceed 2.5x unless contractually backed by recurring revenue.",
            ],
            portfolio_roles=[
                "Core Compounders (50-60% of portfolio): High-moat secular leaders.",
                "Defensive Stabilizers (25-35% of portfolio): Inelastic demand cash-cows.",
                "Tactical Reinvestment Cash (10-15%): Dry powder for drawdown dislocations.",
            ],
            diversification_logic="Diversify by business model resilience and fundamental economic drivers, not artificial sector quotas.",
            risk_philosophy="True risk is permanent capital impairment through business degradation, not short-term simulator volatility.",
            valuation_philosophy="Reverse DCF to ascertain market-implied growth, requiring a margin of safety against conservative baseline DCF.",
            qualitative_philosophy="Forensic examination of customer switching costs, management capital allocation, and supplier bargaining power.",
            quantitative_philosophy="Deterministic Sloan accrual screening, Altman Z solvency check, and factor-neutral quality Z-scores.",
            deliberate_avoids=[
                "Unprofitable hyper-growth technology companies.",
                "Highly levered cyclical commodity producers.",
                "Companies requiring continuous external equity financing.",
            ],
            buy_criteria=[
                "ROIC > WACC spread exceeds 500 bps.",
                "Reverse DCF implied revenue growth is lower than management conservative guidance.",
                "Clear alignment with client's ethical and long-term values.",
            ],
            sell_criteria=[
                "Deterioration of primary competitive moat.",
                "Management undertakes value-destructive debt-fueled M&A.",
                "Valuation expands beyond 2.5x intrinsic DCF value.",
            ],
            monitoring_framework="Quarterly earnings review verifying FCF conversion, debt leverage, and competitive moat stability.",
            justification_for_modification="Fundamental thesis invalidation or severe negative change in client personal circumstances.",
            why_distinctive="Avoids chasing momentum; anchors on rigorous accounting quality and forensic free cash flow proof.",
            why_understandable="Any judge can immediately understand: buy proven companies with monopolistic moats at fair prices.",
            why_appropriate_for_client=f"Respects {client_name}'s investment horizon by avoiding boom-bust cycles.",
            weaknesses_and_tradeoffs=[
                "May lag sharp speculative bull runs in low-quality momentum stocks.",
                "Requires high patience during short 10-week simulator trading window.",
            ],
        )

    @staticmethod
    def generate_strategy_b(mandate: ClientMandate) -> InvestmentStrategy:
        """Strategy Architect B: Structural Transitions & Cash Flow Asymmetry."""
        client_name = mandate.client_name
        return InvestmentStrategy(
            strategy_id="STRAT-B-ASYMMETRIC-TRANSITION",
            architect_role="Strategy Architect B",
            strategy_name="Structural Transitions & Value Asymmetry (STVA)",
            central_philosophy=(
                f"Capitalizes on macroeconomic and industrial structural transformations where market mispricing creates "
                f"asymmetric risk-reward profiles for {client_name}."
            ),
            relationship_to_client=(
                f"Targets {client_name}'s growth and capital efficiency needs by entering essential industrial and supply-chain "
                "leaders undergoing mispriced cyclical re-ratings."
            ),
            guiding_principles=[
                "Seek asymmetric payoff: 3:1 upside-to-downside risk distribution.",
                "Identify mispriced structural demand shifts (e.g., energy grid upgrade, automation).",
                "Never compromise on balance sheet solvency.",
            ],
            portfolio_selection_rules=[
                "Discounted valuation multiple relative to historical peer medians.",
                "Identifiable catalyst for multiple re-expansion within 12-24 months.",
                "Downside protected by tangible asset backing or strong free cash flow yield.",
            ],
            portfolio_roles=[
                "Structural Catalyst Leaders (40-50%): Beneficiaries of durable industry shifts.",
                "Cash Flow Moats (30-40%): Stable dividend/cash generators providing liquidity.",
                "Risk Hedge Positions (10-20%): Low-beta uncorrelated ballast.",
            ],
            diversification_logic="Balance structural theme exposures with uncorrelated utility and consumer staple anchors.",
            risk_philosophy="Manage drawdown risk through rigorous entry valuation discipline and scenario stress testing.",
            valuation_philosophy="Scenario DCF analysis (Bear, Base, Bull) coupled with peer multiple harmonic mean comparisons.",
            qualitative_philosophy="Focus on industry regulatory trends, supply-chain bottlenecks, and technological disruption barriers.",
            quantitative_philosophy="Valuation factor ranking, EV/EBITDA peer dispersion, and historical drawdown distribution analysis.",
            deliberate_avoids=[
                "High-multiple momentum stocks with no tangible cash flows.",
                "Turnarounds with decaying customer balance sheets.",
                "Pure speculative micro-cap stories.",
            ],
            buy_criteria=[
                "Base-case upside > 20% with bear-case drawdown < 10%.",
                "Strong liquidity and institutional sponsorship.",
            ],
            sell_criteria=[
                "Structural thesis catalyst plays out and multiple normalizes.",
                "Catalyst fails to materialize after two consecutive quarters.",
            ],
            monitoring_framework="Bi-weekly monitoring of industry leading indicators and relative valuation spreads.",
            justification_for_modification="Regulatory or macroeconomic shocks that structurally eliminate the identified transition trend.",
            why_distinctive="Connects macro industry trends with hard-headed micro value discipline.",
            why_understandable="Framed around tangible real-world transitions that judges encounter daily.",
            why_appropriate_for_client=f"Balances {client_name}'s risk tolerance by capping downside while capturing upside.",
            weaknesses_and_tradeoffs=[
                "Catalysts may take longer to materialize than the competition timeline.",
                "Higher cyclical sensitivity if macroeconomic headwinds accelerate.",
            ],
        )

    @staticmethod
    def generate_strategy_c(mandate: ClientMandate) -> InvestmentStrategy:
        """Strategy Architect C: All-Weather Endowment Discipline."""
        client_name = mandate.client_name
        return InvestmentStrategy(
            strategy_id="STRAT-C-ALL-WEATHER",
            architect_role="Strategy Architect C",
            strategy_name="All-Weather Endowment Discipline (AWED)",
            central_philosophy=(
                f"Modeled on top university endowments: protect {client_name}'s capital across all 4 economic quadrants "
                "(growth, recession, inflation, deflation) through balanced risk allocation."
            ),
            relationship_to_client=(
                f"Addresses {client_name}'s drawdown concerns directly while ensuring steady purchasing power growth."
            ),
            guiding_principles=[
                "Balance risk contributions across macroeconomic regimes, not just dollar capital.",
                "Resilience in downturns creates mathematical compounding superiority.",
                "Cost discipline and simplicity beat opaque financial engineering.",
            ],
            portfolio_selection_rules=[
                "Constituents must possess demonstrated non-correlation during historical market panics.",
                "Holdings distributed across growth compounders, inflation hedges, and defensive anchors.",
            ],
            portfolio_roles=[
                "Economic Growth Drivers (35-40%): Tech/Industrial leaders.",
                "Inflation/Commodity Protectors (20-25%): Energy/Materials cash generators.",
                "Defensive Anchors (30-35%): Healthcare/Staples/Utilities.",
                "Liquidity Cushion (5-10%): Cash equivalents for rebalancing.",
            ],
            diversification_logic="Explicit regime diversification across Growth, Recession, Inflation, and Deflation.",
            risk_philosophy="Risk is not volatility; risk is being caught unprepared for regime changes.",
            valuation_philosophy="Multi-period dividend discount and normalized through-cycle cash flow multiples.",
            qualitative_philosophy="Evaluating pricing power resilience under inflation and volume resilience under recession.",
            quantitative_philosophy="Hierarchical Risk Parity (HRP) clustering and historical shock drawdown modeling.",
            deliberate_avoids=[
                "Concentration in single tech/growth sectors.",
                "Unhedged cyclical exposures.",
            ],
            buy_criteria=["Fills a specific regime risk gap while trading within reasonable valuation bounds."],
            sell_criteria=["Correlation shift that degrades regime diversification or deterioration of dividend safety."],
            monitoring_framework="Monthly correlation monitoring and macroeconomic regime risk audits.",
            justification_for_modification="Permanent structural regime break.",
            why_distinctive="Prioritizes holistic portfolio harmony and risk contribution over individual stock picking.",
            why_understandable="Instantly relatable to judges through the recognized institutional endowment model.",
            why_appropriate_for_client=f"Minimizes sleep-loss risk for {client_name} by preventing catastrophic drawdown.",
            weaknesses_and_tradeoffs=[
                "Will underperform high-beta strategies during one-way momentum bull runs.",
            ],
        )

    @classmethod
    def generate_candidate_strategies(cls, mandate: ClientMandate) -> List[InvestmentStrategy]:
        """Generates all 3 candidate strategies in isolation (Phase 1 Blind)."""
        return [
            cls.generate_strategy_a(mandate),
            cls.generate_strategy_b(mandate),
            cls.generate_strategy_c(mandate),
        ]
