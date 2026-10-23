"""Caplet Mandate Engine: Manages lifecycle and validation of CapletMandate."""

import json
from pathlib import Path
from typing import Optional
from wharton_ic.mandate.models import CapletMandate


class MandateEngine:
    """Manages the creation, persistence, and retrieval of CapletMandate."""

    def __init__(self, storage_dir: Optional[Path] = None):
        self.storage_dir = storage_dir or Path("config/mandates")
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.active_mandate_file = self.storage_dir / "active_caplet_mandate.json"

    def save_mandate(self, mandate: CapletMandate) -> Path:
        """Saves a CapletMandate to storage."""
        target = self.storage_dir / f"{mandate.mandate_id}.json"
        with open(target, "w", encoding="utf-8") as f:
            json.dump(mandate.model_dump(), f, indent=2)

        # Set as active mandate
        with open(self.active_mandate_file, "w", encoding="utf-8") as f:
            json.dump(mandate.model_dump(), f, indent=2)

        return target

    def load_active_mandate(self) -> Optional[CapletMandate]:
        """Loads the current active CapletMandate."""
        if not self.active_mandate_file.exists():
            return None
        with open(self.active_mandate_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return CapletMandate(**data)
