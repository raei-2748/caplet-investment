"""Client Mandate Auditor enforcing provenance and objective tension detection."""

from typing import Any, Dict, List
from wharton_ic.client.models import ClientMandate, FactCategory


class MandateAuditResult:
    """Structured output of a client mandate audit."""
    def __init__(
        self,
        is_compliant: bool,
        supported_facts_count: int,
        interpretations_count: int,
        assumptions_count: int,
        tensions: List[str],
        ambiguities: List[str],
        unsupported_facts: List[str],
        approval_status: str,
    ):
        self.is_compliant = is_compliant
        self.supported_facts_count = supported_facts_count
        self.interpretations_count = interpretations_count
        self.assumptions_count = assumptions_count
        self.tensions = tensions
        self.ambiguities = ambiguities
        self.unsupported_facts = unsupported_facts
        self.approval_status = approval_status

    def to_dict(self) -> Dict[str, Any]:
        return {
            "is_compliant": self.is_compliant,
            "supported_facts_count": self.supported_facts_count,
            "interpretations_count": self.interpretations_count,
            "assumptions_count": self.assumptions_count,
            "tensions": self.tensions,
            "ambiguities": self.ambiguities,
            "unsupported_facts": self.unsupported_facts,
            "approval_status": self.approval_status,
        }


class ClientMandateAuditor:
    """Audits a ClientMandate for strict provenance, objective conflict, and human sign-off."""

    @staticmethod
    def audit_mandate(mandate: ClientMandate) -> MandateAuditResult:
        all_items = (
            mandate.financial_objectives
            + mandate.nonfinancial_objectives
            + [
                mandate.investment_horizon,
                mandate.liquidity_requirements,
                mandate.return_objectives,
                mandate.risk_tolerance,
                mandate.risk_capacity,
                mandate.drawdown_concerns,
                mandate.income_needs,
            ]
            + mandate.ethical_preferences
            + mandate.impact_objectives
            + mandate.sector_preferences
            + mandate.explicit_exclusions
            + mandate.implicit_constraints
        )

        supported_facts = 0
        interpretations = 0
        assumptions = 0
        unsupported_facts = []

        for item in all_items:
            if item.category == FactCategory.CLIENT_FACT:
                if not item.official_source_citation or item.official_source_citation.strip() == "":
                    unsupported_facts.append(f"Fact '{item.statement}' ({item.item_id}) lacks official source citation.")
                else:
                    supported_facts += 1
            elif item.category == FactCategory.TEAM_INTERPRETATION:
                interpretations += 1
            elif item.category == FactCategory.STRATEGIC_ASSUMPTION:
                assumptions += 1

        # Detect tensions
        tensions = list(mandate.tensions_or_conflicts)
        
        # Dialectical checks:
        # 1. Horizon vs Liquidity
        if "short" in mandate.investment_horizon.statement.lower() and "illiquid" in mandate.liquidity_requirements.statement.lower():
            tensions.append("Short horizon directly tensions with illiquid investment holdings.")
        # 2. Return vs Risk
        if "aggressive" in mandate.return_objectives.statement.lower() and "capital preservation" in mandate.risk_tolerance.statement.lower():
            tensions.append("Aggressive return goals tension with capital preservation risk tolerance.")

        is_compliant = len(unsupported_facts) == 0 and mandate.human_approved
        approval_status = "HUMAN_APPROVED" if mandate.human_approved else "PENDING_STUDENT_APPROVAL"

        return MandateAuditResult(
            is_compliant=is_compliant,
            supported_facts_count=supported_facts,
            interpretations_count=interpretations,
            assumptions_count=assumptions,
            tensions=tensions,
            ambiguities=mandate.uncertainties,
            unsupported_facts=unsupported_facts,
            approval_status=approval_status,
        )
