"""Journal event models and immutable decision tracking for Team Caplet."""

from datetime import datetime
from enum import Enum
import hashlib
import json
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, ConfigDict


class JournalEventType(str, Enum):
    STRATEGY_PROPOSED = "STRATEGY_PROPOSED"
    STRATEGY_CHANGED = "STRATEGY_CHANGED"
    COMPANY_RESEARCHED = "COMPANY_RESEARCHED"
    COMPANY_REJECTED = "COMPANY_REJECTED"
    COMPANY_SHORTLISTED = "COMPANY_SHORTLISTED"
    TRADE_PROPOSED = "TRADE_PROPOSED"
    TRADE_APPROVED = "TRADE_APPROVED"
    TRADE_REJECTED = "TRADE_REJECTED"
    TRADE_EXECUTED = "TRADE_EXECUTED"
    POSITION_RESIZED = "POSITION_RESIZED"
    POSITION_SOLD = "POSITION_SOLD"
    THESIS_REVISED = "THESIS_REVISED"
    RISK_CONCERN_RAISED = "RISK_CONCERN_RAISED"
    CLIENT_FIT_CONCERN_RAISED = "CLIENT_FIT_CONCERN_RAISED"
    UNEXPECTED_MARKET_EVENT = "UNEXPECTED_MARKET_EVENT"
    MISTAKE_IDENTIFIED = "MISTAKE_IDENTIFIED"
    LESSON_LEARNED = "LESSON_LEARNED"


class JournalEvent(BaseModel):
    """An immutable, tamper-evident record of an authentic team decision or learning event."""
    model_config = ConfigDict(frozen=True)

    event_id: str
    timestamp: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    event_type: JournalEventType
    title: str
    participants: List[str] = Field(description="Student team members present")
    evidence_available_at_time: List[str] = Field(default_factory=list)
    alternatives_considered: List[str] = Field(default_factory=list)
    ai_recommendations: Optional[str] = None
    student_discussion: str
    final_student_decision: str
    reasoning: str
    expected_outcome: Optional[str] = None
    later_outcome: Optional[str] = None
    retrospective_lesson: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    
    # Hash-chain integrity fields
    previous_event_hash: Optional[str] = None
    event_hash: Optional[str] = None

    def compute_canonical_hash(self, prev_hash: Optional[str] = None) -> str:
        """Computes deterministic SHA-256 hash over event payload and previous hash."""
        data = self.model_dump(exclude={"event_hash", "previous_event_hash"})
        canonical_json = json.dumps(data, sort_keys=True)
        prev = prev_hash or self.previous_event_hash or "GENESIS"
        to_hash = f"{prev}:{self.timestamp}:{canonical_json}"
        return hashlib.sha256(to_hash.encode("utf-8")).hexdigest()
