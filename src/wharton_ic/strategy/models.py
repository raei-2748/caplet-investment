"""Strategy models and structured evaluation criteria for Team Caplet (V2.1)."""

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class InvestmentStrategy(BaseModel):
    """Full architectural specification of an investment strategy candidate."""
    model_config = ConfigDict(frozen=False)

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
    
    # Structured V2.1 fields
    client_objectives_served: List[str] = Field(default_factory=list)
    client_constraints_addressed: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    uncertainties: List[str] = Field(default_factory=list)
    evidence_needs: List[str] = Field(default_factory=list)
    wharton_rule_dependencies: List[str] = Field(default_factory=list)

    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class StrategyProposal(BaseModel):
    """Typed Pydantic-style structured output from an individual Strategy Architect."""
    model_config = ConfigDict(frozen=True)

    strategy_id: str
    architect_role: str
    strategy_name: str
    one_sentence_philosophy: str
    client_objectives_served: List[str]
    client_constraints_addressed: List[str]
    portfolio_roles: List[str]
    security_selection_principles: List[str]
    diversification_logic: str
    valuation_framework: str
    risk_framework: str
    monitoring_framework: str
    buy_logic: List[str]
    sell_logic: List[str]
    deliberate_avoids: List[str]
    strengths: List[str]
    weaknesses: List[str]
    assumptions: List[str]
    uncertainties: List[str]
    evidence_needs: List[str]
    wharton_rule_dependencies: List[str]

    def to_investment_strategy(self, client_name: str) -> InvestmentStrategy:
        """Converts structured proposal into full InvestmentStrategy."""
        return InvestmentStrategy(
            strategy_id=self.strategy_id,
            architect_role=self.architect_role,
            strategy_name=self.strategy_name,
            central_philosophy=self.one_sentence_philosophy,
            relationship_to_client=f"Serves {client_name}'s goals by addressing: {', '.join(self.client_objectives_served)}",
            guiding_principles=self.security_selection_principles,
            portfolio_selection_rules=self.security_selection_principles,
            portfolio_roles=self.portfolio_roles,
            diversification_logic=self.diversification_logic,
            risk_philosophy=self.risk_framework,
            valuation_philosophy=self.valuation_framework,
            qualitative_philosophy="Deep analysis of business model durability, customer retention, and management alignment.",
            quantitative_philosophy="Rigorous deterministic ROIC vs. WACC spreads, Sloan accruals, and cash flow conversion.",
            deliberate_avoids=self.deliberate_avoids,
            buy_criteria=self.buy_logic,
            sell_criteria=self.sell_logic,
            monitoring_framework=self.monitoring_framework,
            justification_for_modification="Fundamental thesis invalidation or structural client objective change.",
            why_distinctive=f"Emphasizes {', '.join(self.strengths[:2])}.",
            why_understandable=self.one_sentence_philosophy,
            why_appropriate_for_client=f"Respects client constraints: {', '.join(self.client_constraints_addressed[:2])}.",
            weaknesses_and_tradeoffs=self.weaknesses,
            client_objectives_served=self.client_objectives_served,
            client_constraints_addressed=self.client_constraints_addressed,
            assumptions=self.assumptions,
            uncertainties=self.uncertainties,
            evidence_needs=self.evidence_needs,
            wharton_rule_dependencies=self.wharton_rule_dependencies,
        )


class RedTeamCritique(BaseModel):
    """Critique from an adversarial red-team reviewer."""
    model_config = ConfigDict(frozen=True)

    reviewer_role: str
    critique_focus: str
    strengths_identified: List[str]
    vulnerabilities_and_failure_modes: List[str]
    jargon_or_complexity_warnings: List[str]
    unanswered_questions: List[str]
    recommended_revisions: List[str]


class StrategyEvaluation(BaseModel):
    """Comprehensive evaluation of a candidate strategy with qualitative review dimensions."""
    model_config = ConfigDict(frozen=True)

    strategy_id: str
    strategy_name: str
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
    model_config = ConfigDict(frozen=True)

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
