"""Client Mandate models and provenance-aware fact classification."""

from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class FactCategory(str, Enum):
    CLIENT_FACT = "CLIENT_FACT"                       # Directly extracted from official Wharton case text
    TEAM_INTERPRETATION = "TEAM_INTERPRETATION"       # Deduced by student team; explicitly marked
    STRATEGIC_ASSUMPTION = "STRATEGIC_ASSUMPTION"     # Chosen by team to bridge ambiguities


class MandateLineItem(BaseModel):
    """An individual requirement or preference in the client mandate with strict provenance."""
    item_id: str
    category: FactCategory
    statement: str
    official_source_citation: Optional[str] = Field(None, description="Exact paragraph/page in official case PDF")
    rationale_or_notes: Optional[str] = None


class ClientMandate(BaseModel):
    """Audited, structured representation of the Wharton competition client."""
    client_id: str
    client_name: str
    mandate_version: str = "1.0"
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Core Objectives
    financial_objectives: List[MandateLineItem] = Field(default_factory=list)
    nonfinancial_objectives: List[MandateLineItem] = Field(default_factory=list)
    
    # Time & Liquidity
    investment_horizon: MandateLineItem
    liquidity_requirements: MandateLineItem
    return_objectives: MandateLineItem
    
    # Risk Profile
    risk_tolerance: MandateLineItem
    risk_capacity: MandateLineItem
    drawdown_concerns: MandateLineItem
    income_needs: MandateLineItem

    # Values, ESG & Sectors
    ethical_preferences: List[MandateLineItem] = Field(default_factory=list)
    impact_objectives: List[MandateLineItem] = Field(default_factory=list)
    sector_preferences: List[MandateLineItem] = Field(default_factory=list)
    explicit_exclusions: List[MandateLineItem] = Field(default_factory=list)
    implicit_constraints: List[MandateLineItem] = Field(default_factory=list)

    # Uncertainty & Dialectics
    uncertainties: List[str] = Field(default_factory=list)
    tensions_or_conflicts: List[str] = Field(default_factory=list)
    assumptions_requiring_student_judgment: List[str] = Field(default_factory=list)
    evidence_source_ids: List[str] = Field(default_factory=list)

    # Human Governance Sign-Off (MANDATORY before strategy generation)
    human_approved: bool = False
    approved_by: Optional[str] = None
    approval_timestamp: Optional[str] = None
    approval_rationale: Optional[str] = None
