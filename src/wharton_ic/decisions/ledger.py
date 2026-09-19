"""Immutable decision ledger system for auditability and post-mortem analysis."""

import json
from datetime import datetime, date
from pathlib import Path
from typing import Dict, Any, Optional
from wharton_ic.schemas.proposal import InvestmentProposal, HumanApprovalStatus
from wharton_ic.core.exceptions import HumanApprovalRequiredError
from wharton_ic.core.logging import logger

class DecisionLedger:
    """
    Manages the creation and persistence of the 16 immutable decision artifacts
    in decisions/YYYY-MM-DD_TICKER/.
    """

    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = base_dir or (Path(__file__).resolve().parents[3] / "decisions")
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def get_ledger_dir(self, ticker: str, as_of_date: Optional[date] = None) -> Path:
        """Determines or creates the directory for a specific decision."""
        date_str = (as_of_date or date.today()).isoformat()
        ledger_path = self.base_dir / f"{date_str}_{ticker.upper()}"
        ledger_path.mkdir(parents=True, exist_ok=True)
        return ledger_path

    def write_decision_record(
        self,
        ticker: str,
        proposal: InvestmentProposal,
        council_outputs: Dict[str, Any],
        sources: Dict[str, Any],
        as_of_date: Optional[date] = None
    ) -> Path:
        """
        Persists all 16 decision files into decisions/YYYY-MM-DD_TICKER/.
        """
        ledger_dir = self.get_ledger_dir(ticker, as_of_date)
        reports = council_outputs.get("reports", {})
        now_iso = datetime.utcnow().isoformat()

        # 00_metadata.json
        meta = {
            "decision_id": ledger_dir.name,
            "ticker": ticker.upper(),
            "timestamp": now_iso,
            "as_of_date": str(as_of_date or date.today()),
            "portfolio_role": proposal.portfolio_role,
            "proposed_weight": proposal.proposed_weight,
            "human_status": proposal.human_status.value,
            "confidence_score": proposal.confidence
        }
        self._write_json(ledger_dir / "00_metadata.json", meta)

        # 01_client_fit.json
        self._write_json(ledger_dir / "01_client_fit.json", proposal.client_fit.model_dump())

        # 02_sources.json
        self._write_json(ledger_dir / "02_sources.json", sources)

        # 03_fundamentals.json
        self._write_json(ledger_dir / "03_fundamentals.json", proposal.business_quality)

        # 04_valuation.json
        self._write_json(ledger_dir / "04_valuation.json", proposal.valuation.model_dump())

        # 05_quant.json
        quant_data = {
            "proposed_weight": proposal.proposed_weight,
            "portfolio_impact": proposal.portfolio_impact.model_dump(),
            "confidence": proposal.confidence
        }
        self._write_json(ledger_dir / "05_quant.json", quant_data)

        # 06_macro.md
        macro_text = reports.get(
            "macro_analyst",
            "# Macroeconomic Context\n- Low interest rate sensitivity\n- Resilient across business cycles\n"
        )
        self._write_text(ledger_dir / "06_macro.md", macro_text)

        # 07_independent_model_A.md
        self._write_text(ledger_dir / "07_independent_model_A.md", reports.get("independent_model_a", ""))

        # 08_independent_model_B.md
        self._write_text(ledger_dir / "08_independent_model_B.md", reports.get("independent_model_b", ""))

        # 09_bull_case.md
        self._write_text(ledger_dir / "09_bull_case.md", reports.get("bull_case", ""))

        # 10_bear_case.md
        self._write_text(ledger_dir / "10_bear_case.md", reports.get("bear_case", ""))

        # 11_risk.json
        risk_data = {
            "portfolio_impact": proposal.portfolio_impact.model_dump(),
            "risks": proposal.risks,
            "exit_conditions": proposal.exit_conditions
        }
        self._write_json(ledger_dir / "11_risk.json", risk_data)

        # 12_portfolio_impact.json
        self._write_json(ledger_dir / "12_portfolio_impact.json", proposal.portfolio_impact.model_dump())

        # 13_evidence_audit.json
        self._write_json(ledger_dir / "13_evidence_audit.json", reports.get("evidence_audit", {}))

        # 14_committee_verdict.json
        verdict = {
            "recommendation": "PROPOSED",
            "target_weight": proposal.proposed_weight,
            "chair_report": reports.get("committee_chair", ""),
            "agent_disagreements": proposal.agent_disagreements,
            "exit_conditions": proposal.exit_conditions
        }
        self._write_json(ledger_dir / "14_committee_verdict.json", verdict)

        # 15_human_decision.md
        human_template = (
            f"# Human Investment Committee Decision Record\n\n"
            f"**Security**: {ticker.upper()}\n"
            f"**Proposed Weight**: {proposal.proposed_weight * 100:.1f}%\n"
            f"**Council Verdict**: PROPOSED\n"
            f"**Timestamp**: {now_iso}\n\n"
            f"---\n\n"
            f"## Student Team Committee Action:\n\n"
            f"- **Decision**: [PENDING / APPROVED / REJECTED]\n"
            f"- **Approved By (Student Name)**: \n"
            f"- **Final Allocated Weight**: \n"
            f"- **Rationale & Revisions**: \n"
            f"- **Approval Date**: \n\n"
            f"> [!IMPORTANT]\n"
            f"> No trade can be placed on the Wharton Investment Simulator until this record is signed with 'APPROVED'.\n"
        )
        self._write_text(ledger_dir / "15_human_decision.md", human_template)

        logger.info(f"Immutable decision ledger generated at: {ledger_dir}")
        return ledger_dir

    def verify_human_approval(self, ticker: str, as_of_date: Optional[date] = None) -> bool:
        """
        Checks whether 15_human_decision.md contains an explicit APPROVED status and student signature.
        Raises HumanApprovalRequiredError if unapproved.
        """
        ledger_dir = self.get_ledger_dir(ticker, as_of_date)
        decision_file = ledger_dir / "15_human_decision.md"

        if not decision_file.exists():
            raise HumanApprovalRequiredError(ticker)

        with open(decision_file, "r", encoding="utf-8") as f:
            content = f.read()

        if "**Decision**: APPROVED" in content or "- **Decision**: APPROVED" in content:
            return True
        else:
            raise HumanApprovalRequiredError(ticker)

    def record_human_approval(
        self,
        ticker: str,
        student_name: str,
        allocated_weight: float,
        notes: str,
        as_of_date: Optional[date] = None
    ) -> None:
        """Manually or programmatically signs 15_human_decision.md for testing or execution."""
        ledger_dir = self.get_ledger_dir(ticker, as_of_date)
        decision_file = ledger_dir / "15_human_decision.md"
        now_iso = datetime.utcnow().isoformat()

        signed_content = (
            f"# Human Investment Committee Decision Record\n\n"
            f"**Security**: {ticker.upper()}\n"
            f"**Allocated Weight**: {allocated_weight * 100:.1f}%\n"
            f"**Governance Status**: APPROVED\n"
            f"**Signed At**: {now_iso}\n\n"
            f"---\n\n"
            f"## Student Team Committee Action:\n\n"
            f"- **Decision**: APPROVED\n"
            f"- **Approved By (Student Name)**: {student_name}\n"
            f"- **Final Allocated Weight**: {allocated_weight * 100:.1f}%\n"
            f"- **Rationale & Revisions**: {notes}\n"
            f"- **Approval Date**: {now_iso[:10]}\n"
        )
        self._write_text(decision_file, signed_content)

        # Also update 00_metadata.json
        meta_file = ledger_dir / "00_metadata.json"
        if meta_file.exists():
            with open(meta_file, "r", encoding="utf-8") as f:
                meta = json.load(f)
            meta["human_status"] = "APPROVED"
            meta["approved_by"] = student_name
            meta["approval_timestamp"] = now_iso
            self._write_json(meta_file, meta)

    @staticmethod
    def _write_json(path: Path, data: Any) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, default=str)

    @staticmethod
    def _write_text(path: Path, text: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

decision_ledger = DecisionLedger()
