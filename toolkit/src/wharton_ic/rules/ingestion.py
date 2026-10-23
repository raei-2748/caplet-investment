"""Official Material Ingestion System for Wharton IC 2026-2027."""

from datetime import datetime
import hashlib
from pathlib import Path
import shutil
from typing import Any, Dict, List, Optional
import yaml
from pydantic import BaseModel, Field

from wharton_ic.rules.models import (
    AuthorityLevel,
    RuleCategory,
    RuleRecord,
    RuleStatus,
)


class IngestedDocumentRecord(BaseModel):
    """Manifest record for an official competition document."""
    filename: str
    sha256_hash: str
    document_type: str = Field(
        description="client_case, trading_rules, approved_securities_list, ips_instructions, final_report_instructions, trading_notes_instructions, judging_evaluation_criteria, official_updates_amendments"
    )
    source: str = "SurveyMonkey Apply"
    received_date: str
    competition_year: str = "2026-2027"
    authority: str = "OFFICIAL_PRIVATE_VERIFIED"
    version: str = "1.0"
    parsed: bool = False
    human_verified: bool = False
    verified_by: Optional[str] = None
    verification_notes: Optional[str] = None


class OfficialMaterialIngestor:
    """Manages secure ingestion and tracking of official Wharton competition materials."""

    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = root_dir or Path.cwd()
        self.target_dir = self.root_dir / "competition" / "official" / "2026_27"
        self.manifest_path = self.target_dir / "manifest.yaml"
        self.target_dir.mkdir(parents=True, exist_ok=True)

    def _calculate_hash(self, file_path: Path) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()

    def load_manifest(self) -> Dict[str, Any]:
        if not self.manifest_path.exists():
            return {"competition_year": "2026-2027", "documents": []}
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {"competition_year": "2026-2027", "documents": []}

    def save_manifest(self, manifest_data: Dict[str, Any]) -> None:
        with open(self.manifest_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(manifest_data, f, sort_keys=False)

    def ingest_file(
        self,
        source_path: Path,
        document_type: str,
        received_date: Optional[str] = None,
        version: str = "1.0",
    ) -> IngestedDocumentRecord:
        """Ingests a file into competition/official/2026_27/ and registers it in manifest.yaml."""
        if not source_path.exists():
            raise FileNotFoundError(f"Source file {source_path} does not exist.")

        dest_path = self.target_dir / source_path.name
        if dest_path.resolve() != source_path.resolve():
            shutil.copy2(source_path, dest_path)

        file_hash = self._calculate_hash(dest_path)
        rec_date = received_date or datetime.now().strftime("%Y-%m-%d")

        record = IngestedDocumentRecord(
            filename=dest_path.name,
            sha256_hash=file_hash,
            document_type=document_type,
            received_date=rec_date,
            competition_year="2026-2027",
            authority="OFFICIAL_PRIVATE_VERIFIED",
            version=version,
            parsed=False,
            human_verified=False,
        )

        manifest = self.load_manifest()
        docs = [d for d in manifest.get("documents", []) if d.get("filename") != dest_path.name]
        docs.append(record.dict())
        manifest["documents"] = docs
        manifest["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_manifest(manifest)

        return record

    def propose_parsed_rules(self, doc_record: IngestedDocumentRecord, raw_text: str) -> List[RuleRecord]:
        """Proposes rules extracted from an official document.
        
        CRITICAL: All extracted rules are flagged as PENDING_HUMAN_VERIFICATION.
        They CANNOT become authoritative until verified by a student.
        """
        proposed: List[RuleRecord] = []
        now_str = datetime.now().strftime("%Y-%m-%d")
        
        # Create a rule proposal representing the parsed document
        rule_id = f"WHARTON-PROP-{doc_record.document_type.upper()[:5]}-{doc_record.sha256_hash[:6]}"
        proposed.append(
            RuleRecord(
                rule_id=rule_id,
                category=RuleCategory.TRADING_RULES if "trading" in doc_record.document_type else RuleCategory.DELIVERABLES,
                title=f"Parsed Requirement from {doc_record.filename}",
                exact_or_paraphrased_requirement=raw_text[:250].strip() + ("..." if len(raw_text) > 250 else ""),
                authority_level=AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED,
                source_type="SURVEYMONKEY_APPLY",
                source_title=f"Official 2026-27 File: {doc_record.filename}",
                source_url_or_file=str(self.target_dir / doc_record.filename),
                effective_competition_year="2026-2027",
                retrieved_at=doc_record.received_date,
                verified_at=None,
                status=RuleStatus.PENDING_HUMAN_VERIFICATION,
                confidence=0.5,
                notes="PROPOSED VIA PARSER. Requires human verification before promotion to OFFICIAL_PRIVATE_VERIFIED.",
            )
        )
        return proposed
