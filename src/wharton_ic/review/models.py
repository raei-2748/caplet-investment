"""Judge Review Council models and review schemas for Wharton-IC V2."""

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class JudgeRoleCritique(BaseModel):
    role_name: str
    focus_area: str
    strengths: List[str]
    weaknesses: List[str]
    specific_critique: str
    revision_target: str


class JudgeCouncilReview(BaseModel):
    """Complete multi-perspective review of a draft deliverable or evidence pack."""
    review_id: str
    target_deliverable: str
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    rubric_disclaimer: str = (
        "TEAM INTERNAL QUALITATIVE REVIEW DIMENSIONS — DOES NOT REPRESENT OFFICIAL WHARTON NUMERIC SCORES."
    )
    
    role_critiques: List[JudgeRoleCritique]
    unanswered_questions: List[str]
    unsupported_claims: List[str]
    inconsistencies: List[str]
    rule_compliance_risks: List[str]
    narrative_problems: List[str]
    high_priority_revision_targets: List[str]
