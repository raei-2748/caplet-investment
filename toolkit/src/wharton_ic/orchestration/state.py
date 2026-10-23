"""Typed shared state model for Council runs, inspired by TradingAgents."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class CheckpointStatus(str, Enum):
    INITIALIZED = "INITIALIZED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PAUSED_FOR_HUMAN = "PAUSED_FOR_HUMAN"
    PARTIAL_COUNCIL = "PARTIAL_COUNCIL"


class CouncilRunState(BaseModel):
    """Immutable, typed shared state model tracking multi-agent execution."""
    model_config = ConfigDict(frozen=False, extra="forbid")

    run_id: str
    council_type: str = Field(description="'STRATEGY', 'SECURITY', or 'REVIEW'")
    wharton_rules_snapshot_id: str
    client_mandate_version: str
    strategy_version: Optional[str] = None
    as_of_timestamp: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    mode: str = Field(default="production", description="'production' or 'demo'")
    
    # Input hashes for checkpoint invalidation
    input_artifact_hashes: Dict[str, str] = Field(default_factory=dict)

    # Stages and Agent Outputs
    completed_stages: List[str] = Field(default_factory=list)
    agent_outputs: Dict[str, Any] = Field(default_factory=dict)
    evidence_references: List[str] = Field(default_factory=list)
    
    # Deliberation, Uncertainty & Disagreements
    disagreements: List[str] = Field(default_factory=list)
    uncertainties: List[str] = Field(default_factory=list)
    unresolved_questions: List[str] = Field(default_factory=list)
    
    # Failure & Resilience
    failures: List[Dict[str, Any]] = Field(default_factory=list)
    retries: int = 0
    max_retries: int = 2

    # Human Gate Decisions
    human_decisions: List[Dict[str, Any]] = Field(default_factory=list)
    
    # Metadata & Tracking
    model_metadata: Dict[str, Any] = Field(default_factory=lambda: {"model_diversity_limited": False, "providers": []})
    prompt_metadata: Dict[str, Any] = Field(default_factory=dict)
    checkpoint_status: CheckpointStatus = CheckpointStatus.INITIALIZED

    def record_stage_output(self, stage_name: str, agent_name: str, output: Any):
        """Records the output of a specific agent at a specific stage."""
        if stage_name not in self.agent_outputs:
            self.agent_outputs[stage_name] = {}
        self.agent_outputs[stage_name][agent_name] = output
        if stage_name not in self.completed_stages:
            self.completed_stages.append(stage_name)

    def record_failure(self, stage_name: str, agent_name: str, error_message: str):
        """Records an agent or provider failure."""
        self.failures.append({
            "stage": stage_name,
            "agent": agent_name,
            "error": error_message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.checkpoint_status = CheckpointStatus.PARTIAL_COUNCIL

    def record_disagreement(self, disagreement_text: str):
        """Preserves a core disagreement between agents."""
        if disagreement_text not in self.disagreements:
            self.disagreements.append(disagreement_text)
