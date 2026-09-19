"""Evidence models and lineage graph structures for Wharton-IC V2."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ClaimType(str, Enum):
    FACTUAL = "FACTUAL"
    CALCULATION = "CALCULATION"
    INFERENCE = "INFERENCE"
    OPINION = "OPINION"


class VerificationStatus(str, Enum):
    VERIFIED = "VERIFIED"
    PARTIALLY_VERIFIED = "PARTIALLY_VERIFIED"
    UNSUPPORTED = "UNSUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    INFERENCE = "INFERENCE"
    OPINION = "OPINION"
    PENDING = "PENDING"


class EvidenceClaim(BaseModel):
    """An individual factual, calculated, or inferential claim with strict lineage."""
    claim_id: str
    claim_text: str
    claim_type_requested: ClaimType
    source_ids: List[str] = Field(default_factory=list, description="IDs of primary filings, official PDFs, or raw tables")
    metric_ids: List[str] = Field(default_factory=list, description="IDs of deterministic quantitative calculations")
    as_of_date: str
    verification_status: VerificationStatus = VerificationStatus.PENDING
    verification_method: str = "AWAITING_AUDIT"
    contradiction_ids: List[str] = Field(default_factory=list)
    notes: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class EvidenceGraphNode(BaseModel):
    """A node in the end-to-end evidence lineage graph."""
    node_id: str
    node_type: str = Field(description="SOURCE, DATUM, CALCULATION, CLAIM, THESIS, DECISION, REPORT_STATEMENT")
    payload: Dict[str, Any] = Field(default_factory=dict)
    parent_ids: List[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class EvidenceGraph(BaseModel):
    """Directed Acyclic Graph (DAG) tracing lineage: SOURCE -> DATUM -> CALCULATION -> CLAIM -> THESIS -> DECISION -> REPORT."""
    nodes: Dict[str, EvidenceGraphNode] = Field(default_factory=dict)

    def add_node(self, node: EvidenceGraphNode) -> None:
        self.nodes[node.node_id] = node

    def trace_lineage(self, node_id: str) -> List[str]:
        """Recursively traces ancestor node IDs back to roots (SOURCE / DATUM)."""
        visited = []
        queue = [node_id]
        while queue:
            curr = queue.pop(0)
            if curr in self.nodes and curr not in visited:
                visited.append(curr)
                queue.extend(self.nodes[curr].parent_ids)
        return visited
