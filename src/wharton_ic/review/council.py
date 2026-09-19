"""Wharton Judge Review Council auditing deliverables against competition quality standards."""

from datetime import datetime
from pathlib import Path
from typing import List, Optional

from wharton_ic.reporting_v2.models import ReportEvidencePack
from wharton_ic.review.models import JudgeCouncilReview, JudgeRoleCritique


class JudgeReviewCouncil:
    """Simulates multi-perspective judge review to identify weaknesses before submission."""

    @classmethod
    def evaluate_pack(cls, pack: ReportEvidencePack, output_dir: Optional[Path] = None) -> JudgeCouncilReview:
        target_dir = output_dir or (Path.cwd() / "outputs" / "report_pack")
        target_dir.mkdir(parents=True, exist_ok=True)

        critiques: List[JudgeRoleCritique] = [
            JudgeRoleCritique(
                role_name="Client Alignment Reviewer",
                focus_area="Direct connection of portfolio to client mandate",
                strengths=["Mandate structure clearly outlines investment horizon and liquidity needs."],
                weaknesses=["Ensure every single holding explicitly names the client objective it serves."],
                specific_critique="Do not let company profiles read like generic sell-side research; tie to client values.",
                revision_target="Add explicit 'Why this fits Elena' callout box to each security thesis.",
            ),
            JudgeRoleCritique(
                role_name="Strategy Coherence Reviewer",
                focus_area="Internal logic and clarity of investment philosophy",
                strengths=["Central philosophy is established around economic moats and ROIC persistence."],
                weaknesses=["Verify that defensive holdings actually exhibit low historical drawdown."],
                specific_critique="Ensure tactical rebalancing rules do not contradict the low-turnover philosophy.",
                revision_target="Define exact quantitative thresholds that trigger thesis re-examination.",
            ),
            JudgeRoleCritique(
                role_name="Research Reviewer",
                focus_area="Depth of primary evidence and forensic rigor",
                strengths=["Integration of Sloan accruals and Altman Z provides empirical edge."],
                weaknesses=["Avoid relying solely on secondary multiple aggregates."],
                specific_critique="Ensure 10-K risk factor disclosures are directly addressed in company theses.",
                revision_target="Trace every financial ratio back to audited balance sheet filings.",
            ),
            JudgeRoleCritique(
                role_name="Portfolio/Risk Reviewer",
                focus_area="Risk management beyond standard variance",
                strengths=["Historical stress replays (2008, 2020, 2022) provide intuitive scenario context."],
                weaknesses=["Do not present CVaR or Sharpe ratios without explaining their real-world meaning."],
                specific_critique="Judges care about how the team prevented catastrophic loss, not formula derivation.",
                revision_target="Explain what a 15% drawdown feels like to the client and how the team buffers it.",
            ),
            JudgeRoleCritique(
                role_name="Narrative Reviewer",
                focus_area="Competition journey, learning, and team reflection",
                strengths=["Decision journal timeline allows authentic storytelling of team debate."],
                weaknesses=["Highlight mistakes more prominently; judges love intellectual honesty."],
                specific_critique="A report that claims zero mistakes is unconvincing. Document lessons learned.",
                revision_target="Dedicate a full subsection to 'Our Most Significant Strategic Pivot'.",
            ),
            JudgeRoleCritique(
                role_name="Simplicity Reviewer",
                focus_area="Elimination of academic jargon and complex bloat",
                strengths=["Core strategy can be explained in plain English."],
                weaknesses=["Watch out for acronym soup in the portfolio optimization section."],
                specific_critique="If a judge needs a finance degree to understand a chart, replace the chart.",
                revision_target="Simplify optimization discussion to focus on balance rather than quadratic math.",
            ),
            JudgeRoleCritique(
                role_name="Originality Reviewer",
                focus_area="Distinctive Team Caplet identity vs cookie-cutter finalist tropes",
                strengths=["Accounting forensic screening gives a distinctive investigative flavor."],
                weaknesses=["Differentiate beyond standard 'Warren Buffett quality investing' tropes."],
                specific_critique="Focus on Team Caplet's unique decision-making protocols and adversarial debates.",
                revision_target="Include snippets of actual team disagreements from the decision ledger.",
            ),
            JudgeRoleCritique(
                role_name="Skeptical Judge",
                focus_area="Cross-examination and vulnerability detection",
                strengths=["Reverse DCF approach prevents naive hockey-stick growth projections."],
                weaknesses=["What if the client needs their capital sooner than projected?"],
                specific_critique="Check if terminal growth rates exceed long-term GDP growth.",
                revision_target="Cap all terminal growth assumptions at a conservative 2.5%.",
            ),
            JudgeRoleCritique(
                role_name="Compliance Reviewer",
                focus_area="Wharton rules, deliverable guidelines, and AI citation",
                strengths=["Verified rules loaded from official public configuration."],
                weaknesses=["Private 2026-27 rules must be verified upon September 15 release."],
                specific_critique="Ensure word count, page count, and submission formatting strictly match official PDF.",
                revision_target="Audit against official SurveyMonkey Apply packet immediately upon ingestion.",
            ),
        ]

        review = JudgeCouncilReview(
            review_id=f"REV-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            target_deliverable=pack.pack_id,
            role_critiques=critiques,
            unanswered_questions=pack.unanswered_questions or ["How does the team handle severe mid-competition market drawdowns?"],
            unsupported_claims=[],
            inconsistencies=[],
            rule_compliance_risks=pack.missing_evidence_alerts,
            narrative_problems=["Ensure student voices shine through rather than dry corporate prose."],
            high_priority_revision_targets=[
                "Document at least two authentic team disagreements and mistakes in the journal.",
                "Verify official private client case upon September 15 portal release.",
                "Ensure all AI ideas carry proper citations in report bibliography.",
            ],
        )

        # Write markdown review
        md_file = target_dir / "judge_review.md"
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(cls._render_markdown_review(review))

        return review

    @staticmethod
    def _render_markdown_review(review: JudgeCouncilReview) -> str:
        lines = [
            f"# Wharton Judge Council Review — `{review.review_id}`",
            f"**Target Deliverable**: `{review.target_deliverable}`",
            f"**Review Date**: {review.created_at}",
            f"> [!IMPORTANT]",
            f"> **{review.rubric_disclaimer}**",
            "",
            "## 1. High-Priority Revision Targets",
            chr(10).join(f"- [ ] {t}" for t in review.high_priority_revision_targets),
            "",
            "## 2. Rule Compliance & Lineage Risks",
            chr(10).join(f"- [!] {r}" for r in review.rule_compliance_risks) or "- No rule violations detected.",
            "",
            "## 3. Individual Council Critiques",
        ]
        for c in review.role_critiques:
            lines.append(f"### {c.role_name} (`{c.focus_area}`)")
            lines.append(f"- **Specific Critique**: {c.specific_critique}")
            lines.append(f"- **Identified Weakness**: {', '.join(c.weaknesses)}")
            lines.append(f"- **Actionable Target**: **{c.revision_target}**")
            lines.append("")

        return "\n".join(lines)
