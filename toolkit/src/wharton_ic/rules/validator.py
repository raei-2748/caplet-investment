"""Rule Validator enforcing provenance, authority consistency, and no-hallucination rules."""

from typing import List, Tuple
from wharton_ic.rules.models import AuthorityLevel, RuleRecord, RuleStatus


class RuleValidationError(Exception):
    """Raised when a rule record violates competition provenance or integrity standards."""
    pass


class RuleValidator:
    """Validates rule records before ingestion into the registry."""

    @staticmethod
    def validate_rule(rule: RuleRecord) -> Tuple[bool, List[str]]:
        """Returns (is_valid, list_of_errors)."""
        errors = []

        # 1. Authority vs Source Type Consistency
        if rule.authority_level == AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED:
            if rule.source_type not in ["SURVEYMONKEY_APPLY", "OFFICIAL_COMMUNICATION"]:
                errors.append(f"Authority {rule.authority_level} requires source SURVEYMONKEY_APPLY, got {rule.source_type}")
        elif rule.authority_level == AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED:
            if rule.source_type not in ["PUBLIC_WEBSITE", "OFFICIAL_PRESS_RELEASE"]:
                errors.append(f"Authority {rule.authority_level} requires source PUBLIC_WEBSITE, got {rule.source_type}")
        elif rule.authority_level == AuthorityLevel.AI_REASONING:
            if rule.status in [RuleStatus.OFFICIAL_PRIVATE_VERIFIED, RuleStatus.OFFICIAL_PUBLIC_VERIFIED]:
                errors.append("AI reasoning can NEVER produce an OFFICIAL status rule.")

        # 2. Status Consistency
        if rule.status == RuleStatus.OFFICIAL_PRIVATE_VERIFIED and not rule.verified_at:
            errors.append("OFFICIAL_PRIVATE_VERIFIED rules must have verified_at metadata.")

        # 3. Source Provenance
        if not rule.source_url_or_file or rule.source_url_or_file.strip() == "":
            errors.append("Rule must have an explicit source URL or local file path.")

        # 4. Unknown State Prohibition from Becoming Authoritative
        if rule.status == RuleStatus.UNKNOWN and rule.confidence > 0.0:
            errors.append("UNKNOWN rules must have 0.0 confidence.")

        return len(errors) == 0, errors

    @classmethod
    def assert_valid(cls, rule: RuleRecord) -> None:
        valid, errors = cls.validate_rule(rule)
        if not valid:
            raise RuleValidationError(f"Rule {rule.rule_id} validation failed: {'; '.join(errors)}")
