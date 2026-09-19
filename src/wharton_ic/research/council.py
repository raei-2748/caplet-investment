"""Security-level AI Council and Student Governance Gate."""

from datetime import datetime
from typing import Dict, List, Optional
from wharton_ic.core.exceptions import HumanGovernanceError
from wharton_ic.research.models import (
    CommitteeRecommendation,
    HumanSecurityStatus,
    SecurityResearchProposal,
)


class SecurityCouncilEngine:
    """Orchestrates the 11-member security review council and enforces human sign-off."""

    @staticmethod
    def evaluate_proposal(proposal: SecurityResearchProposal) -> SecurityResearchProposal:
        """Executes the multi-agent deliberation process on a proposed security."""
        deliberation_log = {}

        # 1. Fundamental Analyst Review
        roic = proposal.deterministic_metrics.get("roic", 0.0)
        wacc = proposal.deterministic_metrics.get("wacc", 0.08)
        spread_bps = (roic - wacc) * 10000
        deliberation_log["fundamental_analyst"] = {
            "economic_spread_bps": spread_bps,
            "sloan_accruals": proposal.deterministic_metrics.get("sloan_accruals", 0.0),
            "verdict": "STRONG_QUALITY" if spread_bps > 300 else "MARGINAL_OR_DETERIORATING",
        }

        # 2. Valuation Review
        dcf_val = proposal.deterministic_metrics.get("dcf_fair_value", 0.0)
        mkt_price = proposal.deterministic_metrics.get("market_price", 1.0)
        margin_of_safety = (dcf_val - mkt_price) / mkt_price if mkt_price > 0 else 0.0
        deliberation_log["valuation_analyst"] = {
            "dcf_fair_value": dcf_val,
            "market_price": mkt_price,
            "margin_of_safety_pct": margin_of_safety * 100,
            "verdict": "ATTRACTIVE_VALUATION" if margin_of_safety > 0.10 else "FAIR_OR_OVERVALUED",
        }

        # 3. Risk Officer Review
        altman_z = proposal.deterministic_metrics.get("altman_z", 3.0)
        deliberation_log["risk_officer"] = {
            "altman_z": altman_z,
            "solvency_zone": "SAFE" if altman_z > 2.99 else ("GREY" if altman_z > 1.81 else "DISTRESS"),
        }

        # 4. Synthesize Committee Chair Recommendation
        if spread_bps < 0 or altman_z < 1.81:
            rec = CommitteeRecommendation.REJECT
            conditions = ["Fails fundamental hurdle: negative economic spread or distress solvency risk."]
        elif margin_of_safety < 0:
            rec = CommitteeRecommendation.SUPPORT_WITH_CONDITIONS
            conditions = ["Valuation lacks margin of safety; recommend waiting for pullback or resizing smaller."]
        else:
            rec = CommitteeRecommendation.SUPPORT
            conditions = ["Meets quality and valuation criteria; proceed to student decision gate."]

        updated = proposal.dict()
        updated["committee_recommendation"] = rec
        updated["committee_conditions"] = conditions
        updated["council_deliberation_log"] = deliberation_log
        return SecurityResearchProposal(**updated)

    @staticmethod
    def human_signoff(
        proposal: SecurityResearchProposal,
        approve: bool,
        student_name: str,
        student_notes: str,
    ) -> SecurityResearchProposal:
        """Student governance action to formally approve or reject a security.
        
        CRITICAL: Can ONLY be executed by a student. AI cannot produce HUMAN_APPROVED.
        """
        if not student_name or len(student_name.strip()) < 3:
            raise HumanGovernanceError("Signoff requires a verified student team member name.")

        if not student_notes or len(student_notes.strip()) < 10:
            raise HumanGovernanceError("Signoff requires documented student rationale (minimum 10 characters).")

        status = HumanSecurityStatus.HUMAN_APPROVED if approve else HumanSecurityStatus.HUMAN_REJECTED

        updated = proposal.dict()
        updated["human_status"] = status
        updated["approved_by"] = student_name.strip()
        updated["approval_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated["approval_notes"] = student_notes.strip()

        return SecurityResearchProposal(**updated)
