"""AI Authorship Firewall protecting authentic student authorship."""

from typing import List, Tuple
from wharton_ic.core.exceptions import WhartonICException
from wharton_ic.reporting_v2.models import AuthorshipType, ContentBlock


class AIAuthorshipViolationError(WhartonICException):
    """Raised when uncredited or raw generative AI text attempts to enter submission deliverables."""
    pass


class AIAuthorshipFirewall:
    """Enforces strict academic integrity and Wharton AI policy compliance."""

    @staticmethod
    def audit_blocks(blocks: List[ContentBlock]) -> Tuple[bool, List[str]]:
        """Audits a collection of report content blocks for compliance with Wharton AI rules."""
        violations = []

        for b in blocks:
            # Rule 1: Raw AI_GENERATED prose cannot be submitted directly
            if b.authorship_type == AuthorshipType.AI_GENERATED:
                violations.append(
                    f"Block {b.block_id} in section '{b.section_id}' is raw AI_GENERATED text. "
                    "Wharton rules prohibit submitting generative AI text as student work. "
                    "Students must rewrite and synthesize in 'report/student_authored/'."
                )

            # Rule 2: UNKNOWN authorship cannot be submitted
            elif b.authorship_type == AuthorshipType.UNKNOWN:
                violations.append(
                    f"Block {b.block_id} has UNKNOWN authorship. All text must be verified as student-authored or deterministic code."
                )

            # Rule 3: AI_ASSISTED_IDEA must carry mandatory disclosure
            elif b.authorship_type == AuthorshipType.AI_ASSISTED_IDEA:
                if not b.has_mandatory_disclosure and not b.citations:
                    violations.append(
                        f"Block {b.block_id} is flagged as AI_ASSISTED_IDEA but lacks formal citation or disclosure."
                    )

        is_compliant = len(violations) == 0
        return is_compliant, violations

    @classmethod
    def assert_compliant(cls, blocks: List[ContentBlock]) -> None:
        compliant, violations = cls.audit_blocks(blocks)
        if not compliant:
            raise AIAuthorshipViolationError(
                f"REPORT COMPILATION HALTED — AI AUTHORSHIP VIOLATIONS DETECTED:\n" + "\n".join(f"- {v}" for v in violations)
            )
