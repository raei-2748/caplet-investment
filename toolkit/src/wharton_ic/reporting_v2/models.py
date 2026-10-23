"""Report models and non-washable AI Authorship Firewall schemas for Wharton-IC V2.1."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class ContentOrigin(str, Enum):
    HUMAN = "HUMAN"
    AI = "AI"
    SOURCE = "SOURCE"
    DETERMINISTIC_CODE = "DETERMINISTIC_CODE"
    UNKNOWN = "UNKNOWN"


class EditorIdentity(str, Enum):
    HUMAN = "HUMAN"
    AI = "AI"
    NONE = "NONE"


class AuthorshipType(str, Enum):
    HUMAN_AUTHORED = "HUMAN_AUTHORED"
    HUMAN_EDITED = "HUMAN_EDITED"
    DETERMINISTIC_CODE = "DETERMINISTIC_CODE"
    SOURCE_QUOTATION = "SOURCE_QUOTATION"
    AI_GENERATED = "AI_GENERATED"
    AI_ASSISTED_IDEA = "AI_ASSISTED_IDEA"
    UNKNOWN = "UNKNOWN"


class ContentBlock(BaseModel):
    """An individual paragraph, table, or figure in a report with strict, non-washable authorship provenance."""
    model_config = ConfigDict(frozen=False)

    block_id: str
    section_id: str
    origin: ContentOrigin = ContentOrigin.UNKNOWN
    last_editor: EditorIdentity = EditorIdentity.NONE
    authorship_type: AuthorshipType = AuthorshipType.UNKNOWN
    author_identity: str = Field(description="Student name, Python module name, or model identifier")
    content_text: str
    citations: List[str] = Field(default_factory=list)
    has_mandatory_disclosure: bool = False
    edit_history: List[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def model_post_init(self, __context: Any) -> None:
        if self.origin == ContentOrigin.UNKNOWN:
            if self.authorship_type == AuthorshipType.HUMAN_AUTHORED:
                self.origin = ContentOrigin.HUMAN
                if self.last_editor == EditorIdentity.NONE:
                    self.last_editor = EditorIdentity.HUMAN
            elif self.authorship_type == AuthorshipType.AI_GENERATED:
                self.origin = ContentOrigin.AI
                if self.last_editor == EditorIdentity.NONE:
                    self.last_editor = EditorIdentity.AI
            elif self.authorship_type == AuthorshipType.DETERMINISTIC_CODE:
                self.origin = ContentOrigin.DETERMINISTIC_CODE
            elif self.authorship_type == AuthorshipType.SOURCE_QUOTATION:
                self.origin = ContentOrigin.SOURCE

    def record_human_edit(self, student_name: str, edit_notes: str) -> None:
        """Records a human revision.
        
        CRITICAL: If origin is AI, origin CANNOT be washed into HUMAN.
        """
        self.last_editor = EditorIdentity.HUMAN
        self.authorship_type = AuthorshipType.HUMAN_EDITED
        self.edit_history.append(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Edited by {student_name}: {edit_notes}"
        )


class ReportEvidencePack(BaseModel):
    """Comprehensive compilation of verified evidence, tables, and decisions for student authors."""
    model_config = ConfigDict(frozen=True)

    pack_id: str
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    architecture_label: str = "TEAM CAPLET REPORT ARCHITECTURE (Awaiting Official Private Rubric)"
    
    verified_rules: List[Dict[str, Any]]
    unknown_rules: List[Dict[str, Any]] = Field(default_factory=list)
    team_interpretations: List[Dict[str, Any]] = Field(default_factory=list)
    
    client_mandate: Dict[str, Any]
    approved_strategy: Dict[str, Any] = Field(default_factory=dict)
    decision_timeline: List[Dict[str, Any]] = Field(default_factory=list)
    trading_notes: str = ""
    lessons_learned: List[Dict[str, Any]] = Field(default_factory=list)
    
    # Quantitative & Evidence Tables (from deterministic calculations)
    research_proposals: List[Dict[str, Any]] = Field(default_factory=list)
    evidence_claims_summary: Dict[str, Any] = Field(default_factory=dict)
    
    # Missing / Weak Lineage Alerts
    missing_evidence_alerts: List[str] = Field(default_factory=list)
    unanswered_questions: List[str] = Field(default_factory=list)
    contradictions_detected: List[str] = Field(default_factory=list)
    
    ai_use_summary: Dict[str, Any] = Field(default_factory=dict)
