"""Deterministic Checkpointing and Resumability Engine.

Adapted from TauricResearch/TradingAgents checkpointer design.
Folds run_id, input hashes, and prompt signatures into deterministic checkpoint IDs.
"""

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Optional
from wharton_ic.orchestration.state import CheckpointStatus, CouncilRunState


class CouncilCheckpointer:
    """Manages stage-level persistence and recovery for Council runs."""

    def __init__(self, checkpoints_dir: Optional[Path] = None):
        self.checkpoints_dir = checkpoints_dir or Path("decisions/checkpoints")
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def compute_signature(
        run_id: str,
        input_hashes: Dict[str, str],
        prompt_versions: Dict[str, str],
        model_config: Dict[str, Any],
    ) -> str:
        """Deterministic signature folding in all graph-shape and input affecting choices."""
        payload = {
            "run_id": run_id,
            "inputs": sorted(input_hashes.items()),
            "prompts": sorted(prompt_versions.items()),
            "models": sorted((k, str(v)) for k, v in model_config.items()),
        }
        canonical = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]

    def save_checkpoint(self, state: CouncilRunState) -> Path:
        """Persists the current CouncilRunState to disk."""
        sig = self.compute_signature(
            run_id=state.run_id,
            input_hashes=state.input_artifact_hashes,
            prompt_versions=state.prompt_metadata,
            model_config=state.model_metadata,
        )
        file_path = self.checkpoints_dir / f"{state.run_id}_{sig}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(state.model_dump(), f, indent=2, default=str)
        return file_path

    def load_checkpoint(
        self,
        run_id: str,
        current_input_hashes: Dict[str, str],
        prompt_versions: Dict[str, str],
        model_config: Dict[str, Any],
    ) -> Optional[CouncilRunState]:
        """Loads an existing checkpoint. Returns None if signature differs (invalidation)."""
        expected_sig = self.compute_signature(
            run_id=run_id,
            input_hashes=current_input_hashes,
            prompt_versions=prompt_versions,
            model_config=model_config,
        )
        file_path = self.checkpoints_dir / f"{run_id}_{expected_sig}.json"
        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return CouncilRunState(**data)

    def is_stage_completed(
        self,
        run_id: str,
        stage_name: str,
        current_input_hashes: Dict[str, str],
        prompt_versions: Dict[str, str],
        model_config: Dict[str, Any],
    ) -> bool:
        """Checks if a specific stage was completed in a valid checkpoint."""
        state = self.load_checkpoint(run_id, current_input_hashes, prompt_versions, model_config)
        if not state:
            return False
        return stage_name in state.completed_stages
