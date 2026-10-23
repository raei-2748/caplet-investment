"""Security Research Models and Future Proposal Schemas for Wharton-IC V2."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class CommitteeRecommendation(str, Enum):
    SUPPORT = "SUPPORT"
    SUPPORT_WITH_CONDITIONS = "SUPPORT_WITH_CONDITIONS"
    RESEARCH_MORE = "RESEARCH_MORE"
    REJECT = "REJECT"


class HumanSecurityStatus(str, Enum):
    HUMAN_APPROVED = "HUMAN_APPROVED"
    HUMAN_REJECTED = "HUMAN_REJECTED"
    PENDING_STUDENT_DECISION = "PENDING_STUDENT_DECISION"


class SecurityResearchProposal(BaseModel):
    """Institutional 13-question security research proposal template."""
    proposal_id: str
    ticker: str
    company_name: str
    sector: str
    as_of_date: str

    # The 13 Mandatory Questions
    why_in_strategy: str = Field(description="1. Why does this security belong in OUR strategy?")
    client_objective_served: str = Field(description="2. Which client objective does it serve?")
    portfolio_role: str = Field(description="3. What portfolio role does it play? (Core Compounder, Defensive Stabilizer, etc.)")
    investment_thesis: str = Field(description="4. What is the investment thesis?")
    variant_perception: str = Field(description="5. What is the variant perception vs consensus?")
    supporting_evidence_ids: List[str] = Field(description="6. What evidence supports it?")
    contradicting_evidence_ids: List[str] = Field(description="7. What evidence contradicts it?")
    key_risks: List[str] = Field(description="8. What are the key risks?")
    falsification_conditions: List[str] = Field(description="9. What would falsify the thesis?")
    review_triggers: List[str] = Field(description="10. What conditions trigger review?")
    why_better_than_alternatives: str = Field(description="11. Why this security rather than the strongest alternative?")
    portfolio_impact: str = Field(description="12. How does it affect the portfolio as a whole?")
    jargon_free_summary: str = Field(description="13. Plain-English summary accessible to judges without jargon.")

    # Quantitative Deterministic Backing (Must come from verified Python math)
    deterministic_metrics: Dict[str, float] = Field(default_factory=dict)
    
    # Council Deliberation Output
    committee_recommendation: CommitteeRecommendation = CommitteeRecommendation.RESEARCH_MORE
    committee_conditions: List[str] = Field(default_factory=list)
    council_deliberation_log: Dict[str, Any] = Field(default_factory=dict)
    council_disagreements: List[str] = Field(default_factory=list)

    # Mandatory Human Governance Gate
    human_status: HumanSecurityStatus = HumanSecurityStatus.PENDING_STUDENT_DECISION
    approved_by: Optional[str] = None
    approval_timestamp: Optional[str] = None
    approval_notes: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
