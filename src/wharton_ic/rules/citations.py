"""Rule Citation Exporter for Wharton Report Evidence Packages."""

import json
from typing import List
from wharton_ic.rules.models import RuleRecord


class RuleCitationExporter:
    """Exports verified rule citations in institutional report formats."""

    @staticmethod
    def to_markdown_table(rules: List[RuleRecord]) -> str:
        """Generates a Markdown table of rule provenance for report appendix."""
        lines = [
            "| Rule ID | Category | Authority Level | Title / Requirement | Source & Verification |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ]
        for r in rules:
            lines.append(
                f"| `{r.rule_id}` | {r.category.value} | {r.authority_level.name} | **{r.title}**: {r.exact_or_paraphrased_requirement} | {r.source_title} ({r.source_url_or_file}) |"
            )
        return "\n".join(lines)

    @staticmethod
    def to_json(rules: List[RuleRecord]) -> str:
        """Exports full JSON schema of verified rules for machine auditing."""
        data = [r.dict() for r in rules]
        return json.dumps(data, indent=2, default=str)
