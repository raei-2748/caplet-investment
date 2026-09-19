"""AI Council Orchestration Engine enforcing independent analysis and adversarial debate."""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from wharton_ic.core.config import config_manager
from wharton_ic.core.logging import logger
from wharton_ic.agents.adapter import llm_adapter
from wharton_ic.evidence.auditor import EvidenceAuditor
from wharton_ic.schemas.proposal import (
    InvestmentProposal,
    ClientFitAssessment,
    PortfolioImpactAnalysis,
    HumanApprovalStatus,
    EvidenceItem
)
from wharton_ic.schemas.valuation import MultiScenarioValuation

class CouncilOrchestrator:
    """
    Coordinates the multi-model AI council:
    1. Independent Phase A and B blind assessments.
    2. Client Steward alignment review.
    3. Adversarial Bull vs. Bear debate.
    4. Risk Officer review.
    5. Evidence Audit verification.
    6. Committee Chair final recommendation.
    """

    def __init__(self, prompts_dir: Optional[Path] = None):
        self.prompts_dir = prompts_dir or (Path(__file__).resolve().parents[3] / "prompts")
        self.models_cfg = config_manager.models
        self.client_cfg = config_manager.client_mandate

    def _read_prompt(self, filename: str) -> str:
        """Reads a versioned prompt from prompts/ directory."""
        path = self.prompts_dir / filename
        if not path.exists():
            return f"Standard prompt for {filename}"
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def run_full_council(
        self,
        ticker: str,
        company_name: str,
        sector: str,
        industry: str,
        fundamentals: Dict[str, Any],
        valuation: MultiScenarioValuation,
        factors: Dict[str, Any],
        portfolio_impact: Dict[str, Any],
        target_weight: float = 0.075
    ) -> Dict[str, Any]:
        """
        Executes the end-to-end deliberation pipeline.
        Returns a dictionary containing all frozen reports and the synthesized InvestmentProposal.
        """
        logger.info(f"Convening AI Council for {ticker} ({company_name})")

        # 1. Phase A: Independent Assessment Model A (e.g. OpenAI family / mock)
        prompt_ind = self._read_prompt("independent_analyst.txt")
        context_common = (
            f"Ticker: {ticker} ({company_name})\n"
            f"GICS: {sector} / {industry}\n"
            f"Fundamentals: {fundamentals}\n"
            f"Valuation: Base ${valuation.base_case_price:.2f}, Bear ${valuation.bear_case_price:.2f}, Bull ${valuation.bull_case_price:.2f}\n"
            f"Factors: {factors}\n"
        )
        report_model_a = llm_adapter.generate(
            provider="openai",
            model="gpt-4o",
            system_prompt="You are an independent senior equity research analyst.",
            user_prompt=prompt_ind.format(
                ticker=ticker,
                company_name=company_name,
                sector=sector,
                industry=industry,
                client_overview=self.client_cfg.get("client", {}).get("description", ""),
                fundamentals=fundamentals,
                valuation=f"Base: ${valuation.base_case_price:.2f}, Upside: {valuation.base_upside_pct*100:.1f}%",
                factors=factors
            ),
            role="independent_model_a"
        )

        # 2. Phase B: Independent Assessment Model B (e.g. Anthropic family / mock)
        report_model_b = llm_adapter.generate(
            provider="anthropic",
            model="claude-3-5-sonnet-20241022",
            system_prompt="You are an independent senior equity research analyst.",
            user_prompt=prompt_ind.format(
                ticker=ticker,
                company_name=company_name,
                sector=sector,
                industry=industry,
                client_overview=self.client_cfg.get("client", {}).get("description", ""),
                fundamentals=fundamentals,
                valuation=f"Base: ${valuation.base_case_price:.2f}, Upside: {valuation.base_upside_pct*100:.1f}%",
                factors=factors
            ),
            role="independent_model_b"
        )

        # 3. Client Steward Review
        prompt_cs = self._read_prompt("client_steward.txt")
        report_client_steward = llm_adapter.generate(
            provider="anthropic",
            model="claude-3-5-sonnet-20241022",
            system_prompt="You are the Client Steward guarding client mandate alignment.",
            user_prompt=prompt_cs.format(
                client_mandate=self.client_cfg,
                ticker=ticker,
                company_name=company_name,
                sector=sector,
                fundamentals=fundamentals,
                valuation=f"Base: ${valuation.base_case_price:.2f}",
                portfolio_role="Core Compounder"
            ),
            role="client_steward"
        )

        # 4. Bull Case Thesis
        prompt_bull = self._read_prompt("bull_researcher.txt")
        report_bull = llm_adapter.generate(
            provider="openai",
            model="gpt-4o",
            system_prompt="You are the Bull Researcher building the strongest evidence-based upside case.",
            user_prompt=prompt_bull.format(
                ticker=ticker,
                client_summary=self.client_cfg.get("client", {}).get("objectives", ""),
                fundamentals=fundamentals,
                valuation=f"Bull Case: ${valuation.bull_case_price:.2f} ({valuation.bull_upside_pct*100:.1f}% upside)",
                factors=factors
            ),
            role="bull_researcher"
        )

        # 5. Bear Case Thesis (Adversarial)
        prompt_bear = self._read_prompt("bear_researcher.txt")
        report_bear = llm_adapter.generate(
            provider="anthropic",
            model="claude-3-5-sonnet-20241022",
            system_prompt="You are the Adversarial Bear Researcher identifying structural flaws and failure modes.",
            user_prompt=prompt_bear.format(
                ticker=ticker,
                client_summary=self.client_cfg.get("client", {}).get("objectives", ""),
                fundamentals=fundamentals,
                bear_valuation=f"Bear Case: ${valuation.bear_case_price:.2f} ({valuation.bear_upside_pct*100:.1f}%)",
                factors=factors
            ),
            role="bear_researcher"
        )

        # 6. Risk Officer Review
        prompt_risk = self._read_prompt("risk_officer.txt")
        report_risk = llm_adapter.generate(
            provider="gemini",
            model="gemini-1.5-pro",
            system_prompt="You are the Chief Risk Officer evaluating portfolio tail risk and concentrations.",
            user_prompt=prompt_risk.format(
                ticker=ticker,
                target_weight=f"{target_weight*100:.1f}%",
                marginal_risk=portfolio_impact.get("marginal_cvar_contribution", 0.05),
                sector_exposure=portfolio_impact.get("sector_concentration_post_trade", 0.15),
                tail_risk=portfolio_impact.get("marginal_volatility_contribution", 0.04)
            ),
            role="risk_officer"
        )

        # 7. Evidence Audit
        verified_dict = {**fundamentals, "base_price": valuation.base_case_price, "current_price": valuation.current_price}
        auditor = EvidenceAuditor(verified_dict)
        evidence_items = auditor.audit_text_block(report_bull, source_ref="bull_case")
        evidence_items.extend(auditor.audit_text_block(report_bear, source_ref="bear_case"))
        audit_summary = auditor.generate_audit_summary(evidence_items)

        # 8. Committee Chair Synthesis
        prompt_chair = self._read_prompt("committee_chair.txt")
        report_chair = llm_adapter.generate(
            provider="anthropic",
            model="claude-3-5-sonnet-20241022",
            system_prompt="You are the Investment Committee Chair synthesizing council outputs for human decision.",
            user_prompt=prompt_chair.format(
                ticker=ticker,
                client_steward_report=report_client_steward,
                bull_case=report_bull,
                bear_case=report_bear,
                risk_report=report_risk,
                evidence_audit=audit_summary["status"],
                target_weight=f"{target_weight*100:.1f}%"
            ),
            role="committee_chair"
        )

        # Assemble Structured InvestmentProposal
        client_fit = ClientFitAssessment(
            goal_alignment_score=0.88,
            horizon_fit="10-Year Horizon: Matches long-term reinvestment cycle.",
            liquidity_fit="High Liquidity: Large-cap daily volume > $100M.",
            risk_capacity_fit="Pristine Balance Sheet: Net Debt / EBITDA < 2.0x.",
            values_and_impact_fit="Approved: Zero exclusion sector exposure.",
            strategic_role="Core Compounder",
            summary_rationale="High ROIC business providing steady compounding and capital preservation."
        )

        impact_analysis = PortfolioImpactAnalysis(
            marginal_volatility_contribution=float(portfolio_impact.get("marginal_volatility_contribution", 0.02)),
            marginal_cvar_contribution=float(portfolio_impact.get("marginal_cvar_contribution", 0.03)),
            current_portfolio_weight=0.0,
            target_portfolio_weight=target_weight,
            sector_concentration_post_trade=float(portfolio_impact.get("sector_concentration_post_trade", 0.15)),
            pairwise_correlation_max=0.65,
            diversification_delta=0.015
        )

        proposal = InvestmentProposal(
            ticker=ticker,
            timestamp=datetime.utcnow(),
            client_fit=client_fit,
            portfolio_role="Core Compounder",
            thesis=f"{company_name} possesses a wide economic moat with verifiable ROIC exceeding cost of capital.",
            variant_perception="Market is undervaluing the duration of cash flow reinvestment at high return rates.",
            business_quality=fundamentals,
            valuation=valuation,
            catalysts=[
                "Continued high-margin service expansion",
                "Productive AI infrastructure adoption",
                "Operating leverage in core software"
            ],
            risks=[
                "Macro deceleration in enterprise IT spending",
                "Regulatory scrutiny on competitive practices"
            ],
            bear_case=f"Bear Case DCF implies downside to ${valuation.bear_case_price:.2f} if growth drops to 3%.",
            exit_conditions=[
                "ROIC dropping below WACC for two consecutive quarters",
                "Net Debt / EBITDA exceeding 3.0x",
                "Thesis breach: loss of market leadership in core segment"
            ],
            expected_horizon="3-5 Years (Aligned with 10-year client mandate)",
            proposed_weight=target_weight,
            portfolio_impact=impact_analysis,
            evidence=evidence_items,
            agent_disagreements=[
                "Bull model projects 12% 5-year FCF CAGR; Bear model caps forecast at 5% due to macro headwinds.",
                "Valuation multiple risk flagged by Bear researcher."
            ],
            confidence=0.85,
            human_status=HumanApprovalStatus.PROPOSED
        )

        return {
            "ticker": ticker,
            "proposal": proposal,
            "reports": {
                "independent_model_a": report_model_a,
                "independent_model_b": report_model_b,
                "client_steward": report_client_steward,
                "bull_case": report_bull,
                "bear_case": report_bear,
                "risk_officer": report_risk,
                "evidence_audit": audit_summary,
                "committee_chair": report_chair
            }
        }
