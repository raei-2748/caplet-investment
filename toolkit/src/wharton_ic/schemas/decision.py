"""Schemas for the immutable decision ledger entries."""

from datetime import datetime, date
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

class DecisionMetadata(BaseModel):
    decision_id: str
    ticker: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    as_of_date: date
    decision_type: str  # 'BUY', 'SELL', 'HOLD', 'REBALANCE'
    target_weight: float
    author: str
    status: str

class DecisionSources(BaseModel):
    sources: List[Dict[str, Any]]
    verification_hash: str
    extracted_at: datetime = Field(default_factory=datetime.utcnow)

class CommitteeVerdict(BaseModel):
    ticker: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    recommendation: str  # 'APPROVE', 'REJECT', 'HOLD'
    target_weight: float
    conviction_score: float
    chair_summary: str
    key_conditions: List[str]
    unresolved_risks: List[str]
