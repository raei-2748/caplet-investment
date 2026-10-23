"""Wharton Report Engine V2 assembling audited Report Evidence Packs."""

from datetime import datetime
import json
from pathlib import Path
from typing import Dict, List, Optional

from wharton_ic.client.engine import ClientMandateEngine
from wharton_ic.evidence.auditor import EvidenceLineageAuditor
from wharton_ic.journal.engine import DecisionJournalEngine
from wharton_ic.reporting_v2.firewall import AIAuthorshipFirewall
from wharton_ic.reporting_v2.models import (
    AuthorshipType,
    ContentBlock,
    ReportEvidencePack,
)
from wharton_ic.rules.models import AuthorityLevel, RuleStatus
from wharton_ic.rules.registry import RuleRegistry
from wharton_ic.strategy.engine import StrategyCouncilEngine


class WhartonReportEngineV2:
    """Builds institutional Report Evidence Packs and compiles verified student submissions."""

    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = root_dir or Path.cwd()
        self.output_dir = self.root_dir / "outputs" / "report_pack"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.student_text_dir = self.root_dir / "report" / "student_authored"
        self.student_text_dir.mkdir(parents=True, exist_ok=True)
        self.research_assist_dir = self.root_dir / "outputs" / "research_assistance"
        self.research_assist_dir.mkdir(parents=True, exist_ok=True)

    def assemble_evidence_pack(
        self,
        rule_registry: Optional[RuleRegistry] = None,
        mandate_engine: Optional[ClientMandateEngine] = None,
        strategy_engine: Optional[StrategyCouncilEngine] = None,
        journal_engine: Optional[DecisionJournalEngine] = None,
        evidence_auditor: Optional[EvidenceLineageAuditor] = None,
    ) -> ReportEvidencePack:
        """Assembles all verified competition components into a comprehensive evidence pack."""
        rules = rule_registry or RuleRegistry(self.root_dir)
        m_engine = mandate_engine or ClientMandateEngine(self.root_dir / "decisions" / "client")
        s_engine = strategy_engine or StrategyCouncilEngine(self.root_dir / "decisions" / "strategy")
        j_engine = journal_engine or DecisionJournalEngine(self.root_dir / "decisions" / "journal")
        auditor = evidence_auditor or EvidenceLineageAuditor()

        # 1. Rules: Distinguish Verified vs Unknown vs Team Interpretations
        all_rules = rules.list_rules()
        verified_rules = [
            r.model_dump() for r in all_rules
            if r.status in (RuleStatus.OFFICIAL_PUBLIC_VERIFIED, RuleStatus.OFFICIAL_PRIVATE_VERIFIED) and r.authority_level > AuthorityLevel.TEAM_INTERPRETATION
        ]
        unknown_rules = [
            r.model_dump() for r in all_rules
            if r.status == RuleStatus.UNKNOWN
        ]
        team_interpretations = [
            r.model_dump() for r in all_rules
            if r.authority_level == AuthorityLevel.TEAM_INTERPRETATION
        ]

        # 2. Client Mandate
        mandate = m_engine.load_mandate()
        mandate_dict = mandate.model_dump() if mandate else {"status": "AWAITING_STUDENT_APPROVAL", "client_name": "Unspecified"}

        # 3. Strategy
        strategy = s_engine.get_active_strategy()
        strategy_dict = strategy.model_dump() if strategy else {"status": "AWAITING_STUDENT_SELECTION", "strategy_name": "Unspecified"}

        # 4. Journal & Timeline
        timeline = j_engine.get_timeline()
        trading_notes = j_engine.get_trading_notes()
        lessons = j_engine.get_lessons()

        # 5. Missing Evidence & Unanswered Questions
        missing_alerts = []
        unanswered = []
        if not mandate or not mandate.human_approved:
            missing_alerts.append("Client Mandate has not received official student approval.")
        if not strategy:
            missing_alerts.append("Investment Strategy has not received official student approval.")
        if not timeline:
            missing_alerts.append("No competition decision events recorded in journal.")

        pack = ReportEvidencePack(
            pack_id=f"PACK-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            verified_rules=verified_rules,
            unknown_rules=unknown_rules,
            team_interpretations=team_interpretations,
            client_mandate=mandate_dict,
            approved_strategy=strategy_dict,
            decision_timeline=timeline,
            trading_notes=trading_notes,
            lessons_learned=lessons,
            research_proposals=[],
            evidence_claims_summary={},
            missing_evidence_alerts=missing_alerts,
            unanswered_questions=unanswered,
            contradictions_detected=[],
            ai_use_summary={"total_logged_prompts": 0, "status": "TRACKED_IN_JSONL"},
        )

        # Save pack to disk
        pack_json = self.output_dir / "report_evidence_pack.json"
        with open(pack_json, "w", encoding="utf-8") as f:
            json.dump(pack.model_dump(), f, indent=2, default=str)

        # Render Markdown summary
        pack_md = self.output_dir / "report_evidence_pack.md"
        with open(pack_md, "w", encoding="utf-8") as f:
            f.write(self._render_markdown_pack(pack))

        return pack

    def _render_markdown_pack(self, pack: ReportEvidencePack) -> str:
        lines = [
            f"# Wharton Report Evidence Pack — `{pack.pack_id}`",
            f"**Generated**: {pack.created_at}",
            f"**Architecture Label**: {pack.architecture_label}",
            "",
            "> [!NOTE]",
            "> This evidence pack compiles verified rules, client facts, strategy foundations, and decision logs.",
            "> It is designed to empower Team Caplet students to write their authentic Final Report.",
            "> In accordance with Wharton AI policy, raw AI-generated text must NOT be copied directly into submission drafts.",
            "",
            "## 1. Verified Competition Rules & Timeline",
            f"- **Verified Rules Loaded**: {len(pack.verified_rules)} rules in registry.",
            "",
            "## 2. Client Mandate & Objectives",
            f"- **Client Name**: {pack.client_mandate.get('client_name', 'None')}",
            f"- **Approval Status**: {'APPROVED' if pack.client_mandate.get('human_approved') else 'PENDING'}",
            "",
            "## 3. Approved Investment Strategy",
            f"- **Strategy Name**: {pack.approved_strategy.get('strategy_name', 'None')}",
            f"- **Central Philosophy**: {pack.approved_strategy.get('central_philosophy', 'None')}",
            "",
            "## 4. Trading Notes & Decision Timeline",
            pack.trading_notes,
            "",
            "## 5. Lessons Learned & Strategy Evolution",
            chr(10).join(f"- **{item.get('date')} ({item.get('event')})**: {item.get('lesson_learned')}" for item in pack.lessons_learned) or "- No lessons logged yet.",
            "",
            "## 6. Audit & Evidence Alerts",
            chr(10).join(f"- [WARNING] {alert}" for alert in pack.missing_evidence_alerts) or "- All core elements present.",
        ]
        return "\n".join(lines)

    def compile_final_report(self, blocks: List[ContentBlock]) -> str:
        """Audits content blocks through AI Authorship Firewall and compiles final submission text."""
        AIAuthorshipFirewall.assert_compliant(blocks)
        
        output_file = self.output_dir / "final_compiled_report.md"
        content = "\n\n".join(f"<!-- Section: {b.section_id} | Author: {b.author_identity} -->\n{b.content_text}" for b in blocks)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        return str(output_file)
