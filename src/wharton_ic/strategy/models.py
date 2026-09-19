"""Strategy models and structured evaluation criteria for Team Caplet."""

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class InvestmentStrategy(BaseModel):
    """Full architectural specification of an investment strategy candidate."""
    strategy_id: str
    architect_role: str = Field(description="Strategy Architect A, B, or C")
    strategy_name: str
    central_philosophy: str
    relationship_to_client: str
    guiding_principles: List[str]
    portfolio_selection_rules: List[str]
    portfolio_roles: List[str] = Field(description="e.g., Core Compounders, Defensive Balancers, Tactical Growth")
    diversification_logic: str
    risk_philosophy: str
    valuation_philosophy: str
    qualitative_philosophy: str
    quantitative_philosophy: str
    deliberate_avoids: List[str]
    buy_criteria: List[str]
    sell_criteria: List[str]
    monitoring_framework: str
    justification_for_modification: str
    why_distinctive: str
    why_understandable: str
    why_appropriate_for_client: str
    weaknesses_and_tradeoffs: List[str]
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class RedTeamCritique(BaseModel):
    """Critique from an adversarial red-team reviewer."""
    reviewer_role: str
    critique_focus: str
    strengths_identified: List[str]
    vulnerabilities_and_failure_modes: List[str]
    jargon_or_complexity_warnings: List[str]
    unanswered_questions: List[str]
    recommended_revisions: List[str]


class StrategyEvaluation(BaseModel):
    """Comprehensive evaluation of a candidate strategy with qualitative review dimensions."""
    strategy_id: str
    strategy_name: str
    # Note: These are explicitly labeled TEAM INTERNAL REVIEW DIMENSIONS, never Wharton rubric scores.
    review_label: str = "TEAM INTERNAL QUALITATIVE REVIEW DIMENSIONS"
    client_fit_assessment: str
    coherence_assessment: str
    explainability_assessment: str
    originality_assessment: str
    intellectual_defensibility: str
    practicality_for_high_school_team: str
    red_team_critiques: List[RedTeamCritique]


class HumanStrategyDecision(BaseModel):
    """Mandatory student governance record selecting the team's official strategy."""
    decision_id: str
    decision_date: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    strategies_considered: List[str]
    rejected_alternatives: List[str]
    key_disagreements: List[str]
    strongest_arguments_considered: List[str]
    student_discussion_notes: str
    chosen_strategy_id: str
    chosen_strategy_name: str
    student_rationale: str
    student_signatures: List[str]
    unresolved_questions: List[str]
    human_approved: bool = True
