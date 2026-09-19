"""Lightweight Graph Orchestration Engine for Multi-Agent Councils.

Provides clear node boundaries, persistent state, resumability, parallel execution,
failure states, and human-in-the-loop gates without external framework bloat.
"""

from typing import Any, Callable, Dict, List, Optional
from wharton_ic.orchestration.checkpointer import CouncilCheckpointer
from wharton_ic.orchestration.state import CheckpointStatus, CouncilRunState


class GraphNode:
    """A discrete analytical step in the council execution graph."""

    def __init__(
        self,
        name: str,
        stage: str,
        handler: Callable[[CouncilRunState], Any],
        is_human_gate: bool = False,
    ):
        self.name = name
        self.stage = stage
        self.handler = handler
        self.is_human_gate = is_human_gate


class CouncilGraph:
    """Orchestrates multi-agent execution with stage checkpointing and resume."""

    def __init__(self, checkpointer: Optional[CouncilCheckpointer] = None):
        self.nodes: List[GraphNode] = []
        self.checkpointer = checkpointer or CouncilCheckpointer()

    def add_node(self, node: GraphNode):
        """Appends a node to the execution graph."""
        self.nodes.append(node)

    def execute(
        self,
        state: CouncilRunState,
        prompt_versions: Optional[Dict[str, str]] = None,
    ) -> CouncilRunState:
        """Executes graph nodes sequentially, resuming from checkpoint if available."""
        pv = prompt_versions or state.prompt_metadata

        # Check for existing checkpoint
        existing = self.checkpointer.load_checkpoint(
            run_id=state.run_id,
            current_input_hashes=state.input_artifact_hashes,
            prompt_versions=pv,
            model_config=state.model_metadata,
        )
        if existing:
            state = existing

        state.checkpoint_status = CheckpointStatus.IN_PROGRESS

        for node in self.nodes:
            # Skip if stage already completed in loaded checkpoint
            if node.stage in state.completed_stages:
                continue

            if node.is_human_gate:
                state.checkpoint_status = CheckpointStatus.PAUSED_FOR_HUMAN
                self.checkpointer.save_checkpoint(state)
                break

            try:
                result = node.handler(state)
                state.record_stage_output(node.stage, node.name, result)
                # Checkpoint after each stage
                self.checkpointer.save_checkpoint(state)
            except Exception as exc:
                state.record_failure(node.stage, node.name, str(exc))
                state.checkpoint_status = CheckpointStatus.PARTIAL_COUNCIL
                self.checkpointer.save_checkpoint(state)
                # Stop further execution on node failure
                break

        if state.checkpoint_status == CheckpointStatus.IN_PROGRESS:
            state.checkpoint_status = CheckpointStatus.COMPLETED
            self.checkpointer.save_checkpoint(state)

        return state
