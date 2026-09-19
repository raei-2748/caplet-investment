"""Rule Conflict Detector enforcing strict authority precedence for Wharton IC."""

from typing import List, Optional, Tuple
from pydantic import BaseModel
from wharton_ic.rules.models import AuthorityLevel, RuleRecord, RuleStatus


class ConflictReport(BaseModel):
    """Report detailing a conflict between two rules."""
    rule_a_id: str
    rule_b_id: str
    category: str
    winning_rule_id: Optional[str]
    resolution_status: str
    description: str


class RuleConflictDetector:
    """Detects and resolves conflicts between competition rules."""

    @staticmethod
    def resolve_precedence(rule_a: RuleRecord, rule_b: RuleRecord) -> Tuple[Optional[RuleRecord], Optional[RuleRecord], str]:
        """Compares authority between two conflicting rules.
        
        Returns:
            (winner, loser, reason)
        """
        # Rule 1: Private Verified beats Public Verified
        if rule_a.authority_level > rule_b.authority_level:
            return rule_a, rule_b, f"{rule_a.rule_id} ({rule_a.authority_level.name}) has higher authority than {rule_b.rule_id} ({rule_b.authority_level.name})"
        elif rule_b.authority_level > rule_a.authority_level:
            return rule_b, rule_a, f"{rule_b.rule_id} ({rule_b.authority_level.name}) has higher authority than {rule_a.rule_id} ({rule_a.authority_level.name})"

        # Rule 2: If same authority level, current year beats historical
        if rule_a.effective_competition_year == "2026-2027" and rule_b.effective_competition_year != "2026-2027":
            return rule_a, rule_b, f"{rule_a.rule_id} is current year (2026-2027); historical rules cannot override current."
        elif rule_b.effective_competition_year == "2026-2027" and rule_a.effective_competition_year != "2026-2027":
            return rule_b, rule_a, f"{rule_b.rule_id} is current year (2026-2027); historical rules cannot override current."

        # Rule 3: Tie / Ambiguity
        return None, None, f"Tie between {rule_a.rule_id} and {rule_b.rule_id} with identical authority {rule_a.authority_level.name}; requires student clarification."

    @classmethod
    def find_conflicts(cls, rules: List[RuleRecord]) -> List[ConflictReport]:
        """Scans a list of rules for conflicts within the same category/topic."""
        conflicts = []
        n = len(rules)
        for i in range(n):
            for j in range(i + 1, n):
                r1 = rules[i]
                r2 = rules[j]
                if r1.category == r2.category and r1.rule_id != r2.rule_id:
                    # Check for explicit supersession or potential conflict
                    if r1.status != RuleStatus.SUPERSEDED and r2.status != RuleStatus.SUPERSEDED:
                        winner, loser, reason = cls.resolve_precedence(r1, r2)
                        # Flag if a historical rule attempts to contradict a current rule
                        if r1.authority_level == AuthorityLevel.HISTORICAL_ONLY and r2.authority_level in [AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED, AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED]:
                            conflicts.append(ConflictReport(
                                rule_a_id=r1.rule_id,
                                rule_b_id=r2.rule_id,
                                category=r1.category.value,
                                winning_rule_id=winner.rule_id if winner else None,
                                resolution_status="RESOLVED_BY_AUTHORITY" if winner else "UNRESOLVED",
                                description=f"Historical rule {r1.rule_id} superseded by active rule {r2.rule_id}. {reason}"
                            ))
                        elif r2.authority_level == AuthorityLevel.HISTORICAL_ONLY and r1.authority_level in [AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED, AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED]:
                            conflicts.append(ConflictReport(
                                rule_a_id=r1.rule_id,
                                rule_b_id=r2.rule_id,
                                category=r1.category.value,
                                winning_rule_id=winner.rule_id if winner else None,
                                resolution_status="RESOLVED_BY_AUTHORITY" if winner else "UNRESOLVED",
                                description=f"Historical rule {r2.rule_id} superseded by active rule {r1.rule_id}. {reason}"
                            ))
        return conflicts
