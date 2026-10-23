"""Rule Registry for Wharton Global High School Investment Competition 2026-2027."""

from pathlib import Path
from typing import Dict, List, Optional
import yaml

from wharton_ic.rules.models import (
    AuthorityLevel,
    RuleCategory,
    RuleRecord,
    RuleStatus,
)


class RuleRegistry:
    """Central repository and query engine for competition rules."""

    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = root_dir or Path.cwd()
        self._rules: Dict[str, RuleRecord] = {}
        self._load_public_rules()
        self._load_private_rules_placeholder()

    def _load_public_rules(self) -> None:
        """Loads and converts public verified rules from config/wharton_public_2026_27.yaml."""
        pub_path = self.root_dir / "config" / "wharton_public_2026_27.yaml"
        if not pub_path.exists():
            return

        with open(pub_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        retrieved_at = data.get("retrieved_at", "2026-09-19")
        year = data.get("competition_year", "2026-2027")
        src_url = data.get("source_url", "https://globalyouth.wharton.upenn.edu/investment-competition/")
        src_title = data.get("source_name", "Wharton Global Youth Program Official Public Webpages")

        # 1. Timeline rules
        timeline = data.get("timeline", {})
        timeline_rules = [
            ("WHARTON-PUB-2026-TIME-01", "Materials Release Date", f"Official competition materials released to registered teams on {timeline.get('materials_release_date')}."),
            ("WHARTON-PUB-2026-TIME-02", "Competition Start Date", f"Trading begins on WInS on {timeline.get('competition_start_date')}."),
            ("WHARTON-PUB-2026-TIME-03", "Team Roster Deadline", f"Official team roster due on {timeline.get('team_roster_deadline')}."),
            ("WHARTON-PUB-2026-TIME-04", "Investment Policy Statement Deadline", f"Investment Policy Statement (IPS) due on {timeline.get('ips_deadline')}."),
            ("WHARTON-PUB-2026-TIME-05", "Trading Period End Date", f"WInS trading simulator concludes on {timeline.get('trading_period_end_date')}."),
            ("WHARTON-PUB-2026-TIME-06", "Final Report Deadline", f"Final Report and school documentation due on {timeline.get('final_report_deadline')}."),
        ]
        for rid, title, req in timeline_rules:
            self._rules[rid] = RuleRecord(
                rule_id=rid,
                category=RuleCategory.TIMELINE,
                title=title,
                exact_or_paraphrased_requirement=req,
                authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
                source_type="PUBLIC_WEBSITE",
                source_title=src_title,
                source_url_or_file=src_url,
                effective_competition_year=year,
                retrieved_at=retrieved_at,
                verified_at=retrieved_at,
                status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
                confidence=1.0,
            )

        # 2. Philosophy rules
        phil = data.get("philosophy", {})
        self._rules["WHARTON-PUB-2026-PHIL-01"] = RuleRecord(
            rule_id="WHARTON-PUB-2026-PHIL-01",
            category=RuleCategory.PHILOSOPHY,
            title="Portfolio Performance Does Not Determine Winner",
            exact_or_paraphrased_requirement="Portfolio performance does not determine the winner. WInS return performance has little to do with the final outcome; teams are evaluated on quality and articulation of investment strategy and competition experience.",
            authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
            source_type="PUBLIC_WEBSITE",
            source_title=src_title,
            source_url_or_file=src_url,
            effective_competition_year=year,
            retrieved_at=retrieved_at,
            verified_at=retrieved_at,
            status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
            confidence=1.0,
        )
        self._rules["WHARTON-PUB-2026-PHIL-02"] = RuleRecord(
            rule_id="WHARTON-PUB-2026-PHIL-02",
            category=RuleCategory.PHILOSOPHY,
            title="Strategy Definition & Complexity Warning",
            exact_or_paraphrased_requirement="A strategy is not merely a collection of stocks. Overly technical strategies are not automatically better; judges must not be buried in technical jargon.",
            authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
            source_type="PUBLIC_WEBSITE",
            source_title=src_title,
            source_url_or_file=src_url,
            effective_competition_year=year,
            retrieved_at=retrieved_at,
            verified_at=retrieved_at,
            status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
            confidence=1.0,
        )

        # 3. Deliverables
        delivs = data.get("deliverables", [])
        for i, d in enumerate(delivs, 1):
            rid = f"WHARTON-PUB-2026-DELIV-0{i}"
            self._rules[rid] = RuleRecord(
                rule_id=rid,
                category=RuleCategory.DELIVERABLES,
                title=f"Required Deliverable: {d.get('name')}",
                exact_or_paraphrased_requirement=f"Teams must submit {d.get('name')} by {d.get('deadline')}.",
                authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
                source_type="PUBLIC_WEBSITE",
                source_title=src_title,
                source_url_or_file=src_url,
                effective_competition_year=year,
                retrieved_at=retrieved_at,
                verified_at=retrieved_at,
                status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
                confidence=1.0,
            )

        # 4. Team Rules
        tr = data.get("team_rules", {})
        self._rules["WHARTON-PUB-2026-TEAM-01"] = RuleRecord(
            rule_id="WHARTON-PUB-2026-TEAM-01",
            category=RuleCategory.TEAM_RULES,
            title="Team Size and Composition",
            exact_or_paraphrased_requirement=f"Teams must consist of {tr.get('min_students')} to {tr.get('max_students')} students enrolled in the same secondary school with one shared WInS account.",
            authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
            source_type="PUBLIC_WEBSITE",
            source_title=src_title,
            source_url_or_file=src_url,
            effective_competition_year=year,
            retrieved_at=retrieved_at,
            verified_at=retrieved_at,
            status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
            confidence=1.0,
        )

        # 5. AI Policy
        self._rules["WHARTON-PUB-2026-AI-01"] = RuleRecord(
            rule_id="WHARTON-PUB-2026-AI-01",
            category=RuleCategory.AI_POLICY,
            title="Generative AI Usage & Academic Integrity",
            exact_or_paraphrased_requirement="Generative AI may be used for brainstorming and idea generation, but AI content may be inaccurate or misleading. AI-generated work may NOT be submitted as the students' own work. Any AI use in reports must be explicitly cited.",
            authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
            source_type="PUBLIC_WEBSITE",
            source_title=src_title,
            source_url_or_file=src_url,
            effective_competition_year=year,
            retrieved_at=retrieved_at,
            verified_at=retrieved_at,
            status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
            confidence=1.0,
        )

    def _load_private_rules_placeholder(self) -> None:
        """Encodes explicit UNKNOWN status for private registered-team rules."""
        priv_path = self.root_dir / "config" / "wharton_private_2026_27.yaml"
        if not priv_path.exists():
            return

        unknown_items = [
            ("WHARTON-PRIV-2026-CLIENT-01", RuleCategory.CLIENT_CONSTRAINTS, "Official Client Mandate", "Official 2026-27 client identity, objectives, and constraints released in September 15 case study."),
            ("WHARTON-PRIV-2026-TRADE-01", RuleCategory.TRADING_RULES, "Official Trading and Position Constraints", "Official portfolio position minimums/maximums, sector caps, and trade counts for 2026-27 WInS simulation."),
            ("WHARTON-PRIV-2026-UNIV-01", RuleCategory.PORTFOLIO_CONSTRAINTS, "Approved Securities List", "The official approved competition stock universe CSV/Excel provided on SurveyMonkey Apply."),
            ("WHARTON-PRIV-2026-RUBRIC-01", RuleCategory.EVALUATION_CRITERIA, "Official Judging Rubric & Weights", "Official evaluation criteria and score weight distribution published in deliverable instructions."),
        ]

        for rid, cat, title, req in unknown_items:
            self._rules[rid] = RuleRecord(
                rule_id=rid,
                category=cat,
                title=title,
                exact_or_paraphrased_requirement=req,
                authority_level=AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED,
                source_type="SURVEYMONKEY_APPLY",
                source_title="Wharton Global Youth SurveyMonkey Apply Portal (2026-27)",
                source_url_or_file="competition/official/2026_27/",
                effective_competition_year="2026-2027",
                retrieved_at="AWAITING_RELEASE",
                verified_at=None,
                status=RuleStatus.UNKNOWN,
                confidence=0.0,
                notes="UNKNOWN / AWAITING_OFFICIAL_MATERIAL. No assumption or proxy permitted in production.",
            )

    def get_rule(self, rule_id: str) -> Optional[RuleRecord]:
        return self._rules.get(rule_id)

    def list_rules(self, status: Optional[RuleStatus] = None, category: Optional[RuleCategory] = None) -> List[RuleRecord]:
        rules = list(self._rules.values())
        if status:
            rules = [r for r in rules if r.status == status]
        if category:
            rules = [r for r in rules if r.category == category]
        return rules

    def register_rule(self, rule: RuleRecord) -> None:
        """Registers a new rule record."""
        self._rules[rule.rule_id] = rule

    def verify_rule(self, rule_id: str, verified_by: str) -> RuleRecord:
        """Student verification of a rule record, elevating PENDING to VERIFIED."""
        rule = self._rules.get(rule_id)
        if not rule:
            raise KeyError(f"Rule ID {rule_id} not found in registry.")

        verified_rule = RuleRecord(
            rule_id=rule.rule_id,
            category=rule.category,
            title=rule.title,
            exact_or_paraphrased_requirement=rule.exact_or_paraphrased_requirement,
            authority_level=rule.authority_level,
            source_type=rule.source_type,
            source_title=rule.source_title,
            source_url_or_file=rule.source_url_or_file,
            effective_competition_year=rule.effective_competition_year,
            retrieved_at=rule.retrieved_at,
            verified_at=f"Verified by {verified_by}",
            status=RuleStatus.OFFICIAL_PRIVATE_VERIFIED if rule.authority_level == AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED else RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
            confidence=1.0,
            notes=f"{rule.notes or ''} [Student Verified: {verified_by}]".strip(),
            supersedes=rule.supersedes,
            superseded_by=rule.superseded_by,
        )
        self._rules[rule_id] = verified_rule
        return verified_rule

    def get_status_summary(self) -> Dict[str, int]:
        counts = {}
        for r in self._rules.values():
            counts[r.status.value] = counts.get(r.status.value, 0) + 1
        return counts
