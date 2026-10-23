"""Pydantic model for structured investment proposals."""

from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from wharton_ic.schemas.valuation import MultiScenarioValuation

class HumanApprovalStatus(str, Enum):
    DRAFT = "DRAFT"
    PROPOSED = "PROPOSED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"

class EvidenceItem(BaseModel):
    claim: str = Field(..., description="The substantive statement made")
    claim_type: str = Field(..., description="'FACT', 'CALCULATION', 'INFERENCE', 'HYPOTHESIS'")
    source_reference: str = Field(..., description="Citation or calculation pointer")
    is_verified: bool = Field(False, description="Whether audited against empirical source data")

class ClientFitAssessment(BaseModel):
    goal_alignment_score: float = Field(..., ge=0.0, le=1.0)
    horizon_fit: str
    liquidity_fit: str
    risk_capacity_fit: str
    values_and_impact_fit: str
    strategic_role: str
    summary_rationale: str

class PortfolioImpactAnalysis(BaseModel):
    marginal_volatility_contribution: float
    marginal_cvar_contribution: float
    current_portfolio_weight: float
    target_portfolio_weight: float
    sector_concentration_post_trade: float
    pairwise_correlation_max: float
    diversification_delta: float

class InvestmentProposal(BaseModel):
    """Authoritative structured proposal required for every security before human decision."""
    ticker: str = Field(..., description="Authorized ticker symbol")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="UTC creation timestamp")
    client_fit: ClientFitAssessment = Field(..., description="Structured alignment with Wharton client mandate")
    portfolio_role: str = Field(..., description="Role in portfolio (e.g. 'Core Compounder', 'Secular Growth')")
    thesis: str = Field(..., description="Primary evidence-based investment thesis")
    variant_perception: str = Field(..., description="How our view differs from market consensus")
    business_quality: Dict[str, Any] = Field(..., description="ROIC, moat durability, margin profile, pricing power")
    valuation: MultiScenarioValuation = Field(..., description="Base, Bear, and Bull DCF valuation results")
    catalysts: List[str] = Field(..., description="Identified secular or operational value realization catalysts")
    risks: List[str] = Field(..., description="Key fundamental, operational, and macroeconomic risk factors")
    bear_case: str = Field(..., description="Adversarial failure mode and downside price target")
    exit_conditions: List[str] = Field(..., description="Explicit conditions triggering a complete divestment")
    expected_horizon: str = Field(..., description="Target holding horizon matching client profile")
    proposed_weight: float = Field(..., ge=0.0, le=0.30, description="Recommended portfolio allocation (0.0 to 0.30)")
    portfolio_impact: PortfolioImpactAnalysis = Field(..., description="Incremental portfolio risk metrics")
    evidence: List[EvidenceItem] = Field(..., description="Audited empirical citations backing assertions")
    agent_disagreements: List[str] = Field(default_factory=list, description="Key points of contention during debate")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Overall conviction score (0.0 to 1.0)")
    human_status: HumanApprovalStatus = Field(
        default=HumanApprovalStatus.PROPOSED,
        description="Governance status (Must be APPROVED by human team member before trading)"
    )
    human_notes: Optional[str] = Field(None, description="Recorded notes from the human investment committee")
    approved_by: Optional[str] = Field(None, description="Name of student investment officer recording approval")
    approval_timestamp: Optional[datetime] = None

    def validate_approval_gate(self) -> bool:
        """Enforces that a proposal cannot be executed without human approval."""
        return self.human_status == HumanApprovalStatus.APPROVED and self.approved_by is not None
