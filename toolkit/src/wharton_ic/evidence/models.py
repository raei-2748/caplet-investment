"""Evidence models and lineage graph structures for Wharton-IC V2.1."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


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


class SourceSupportType(str, Enum):
    DIRECT_SUPPORT = "DIRECT_SUPPORT"
    PARTIAL_SUPPORT = "PARTIAL_SUPPORT"
    CONTEXT_ONLY = "CONTEXT_ONLY"
    CONTRADICTS = "CONTRADICTS"
    NO_SUPPORT = "NO_SUPPORT"


class SourceEvidenceLink(BaseModel):
    """Explicit link proving whether and how an existing source actually supports a claim proposition."""
    model_config = ConfigDict(frozen=True)

    link_id: str = Field(default_factory=lambda: f"LINK-{datetime.now().strftime('%Y%m%d%H%M%S')}")
    source_id: str
    locator: str = Field(description="Page, paragraph, row, or table coordinate in source document")
    extracted_datum: str = Field(default="", description="Exact snippet, figure, or quoted text from source")
    extraction_method: str = Field(default="EXACT_MATCH", description="EXACT_MATCH, DETERMINISTIC_CALCULATION, TABLE_LOOKUP")
    claim_id: str = Field(default="", description="Associated claim identifier")
    support_type: SourceSupportType = SourceSupportType.DIRECT_SUPPORT
    verbatim_quote: Optional[str] = None
    verified_by: Optional[str] = None
    audit_notes: Optional[str] = None


class EvidenceClaim(BaseModel):
    """An individual factual, calculated, or inferential claim with strict lineage."""
    model_config = ConfigDict(frozen=False)

    claim_id: str
    claim_text: str
    claim_type_requested: ClaimType
    source_ids: List[str] = Field(default_factory=list, description="IDs of primary filings, official PDFs, or raw tables")
    metric_ids: List[str] = Field(default_factory=list, description="IDs of deterministic quantitative calculations")
    as_of_date: str
    verification_status: VerificationStatus = VerificationStatus.PENDING
    verification_method: str = "AWAITING_AUDIT"
    contradiction_ids: List[str] = Field(default_factory=list)
    support_links: List[SourceEvidenceLink] = Field(default_factory=list)
    notes: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class EvidenceGraphNode(BaseModel):
    """A node in the end-to-end evidence lineage graph."""
    model_config = ConfigDict(frozen=True)

    node_id: str
    node_type: str = Field(description="SOURCE, DATUM, CALCULATION, CLAIM, THESIS, DECISION, REPORT_STATEMENT")
    payload: Dict[str, Any] = Field(default_factory=dict)
    parent_ids: List[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class EvidenceGraph(BaseModel):
    """Directed Acyclic Graph (DAG) tracing lineage: SOURCE -> DATUM -> CALCULATION -> CLAIM -> THESIS -> DECISION -> REPORT."""
    model_config = ConfigDict(frozen=False)

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
