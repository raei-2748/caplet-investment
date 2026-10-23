"""Wharton Rule Custodian Data Models and Authority Hierarchy."""

from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class AuthorityLevel(int, Enum):
    """Programmatically enforced hierarchy of authority for Wharton IC rules."""
    OFFICIAL_PRIVATE_VERIFIED = 100  # SurveyMonkey Apply official materials
    OFFICIAL_PUBLIC_VERIFIED = 80    # Public Wharton Global Youth site
    OFFICIAL_GUIDEBOOK_VERIFIED = 60 # Current Wharton handbook/resources
    TEAM_INTERPRETATION = 40         # Explicit student team interpretations
    HISTORICAL_ONLY = 20             # 2025 or earlier competition rules
    INSPIRATION = 10                 # Previous winner repo techniques
    AI_REASONING = 0                 # LLM generation - NEVER authoritative evidence


class RuleStatus(str, Enum):
    """Lifecycle status of a competition rule."""
    OFFICIAL_PRIVATE_VERIFIED = "OFFICIAL_PRIVATE_VERIFIED"
    OFFICIAL_PUBLIC_VERIFIED = "OFFICIAL_PUBLIC_VERIFIED"
    HISTORICAL_ONLY = "HISTORICAL_ONLY"
    TEAM_INTERPRETATION = "TEAM_INTERPRETATION"
    UNKNOWN = "UNKNOWN"
    SUPERSEDED = "SUPERSEDED"
    PENDING_HUMAN_VERIFICATION = "PENDING_HUMAN_VERIFICATION"


class RuleCategory(str, Enum):
    """Categories of competition rules and constraints."""
    TIMELINE = "TIMELINE"
    PHILOSOPHY = "PHILOSOPHY"
    DELIVERABLES = "DELIVERABLES"
    TEAM_RULES = "TEAM_RULES"
    AI_POLICY = "AI_POLICY"
    TRADING_RULES = "TRADING_RULES"
    PORTFOLIO_CONSTRAINTS = "PORTFOLIO_CONSTRAINTS"
    EVALUATION_CRITERIA = "EVALUATION_CRITERIA"
    CLIENT_CONSTRAINTS = "CLIENT_CONSTRAINTS"


class RuleRecord(BaseModel):
    """Immutable, provenance-aware representation of a competition rule."""
    rule_id: str = Field(description="Unique identifier, e.g., WHARTON-PUB-2026-TIMELINE-01")
    category: RuleCategory
    title: str
    exact_or_paraphrased_requirement: str
    authority_level: AuthorityLevel
    source_type: str = Field(description="SURVEYMONKEY_APPLY, PUBLIC_WEBSITE, GUIDEBOOK, TEAM_MEETING, HISTORICAL")
    source_title: str
    source_url_or_file: str
    effective_competition_year: str = Field(default="2026-2027")
    retrieved_at: str
    verified_at: Optional[str] = None
    status: RuleStatus
    confidence: float = Field(ge=0.0, le=1.0, default=1.0)
    notes: Optional[str] = None
    supersedes: Optional[List[str]] = Field(default_factory=list)
    superseded_by: Optional[str] = None

    model_config = ConfigDict(frozen=True)

