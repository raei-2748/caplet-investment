"""Client Mandate Engine managing lifecycle, persistence, and human approvals."""

from datetime import datetime
import json
from pathlib import Path
from typing import Optional

from wharton_ic.client.models import ClientMandate
from wharton_ic.core.exceptions import HumanGovernanceError


class ClientMandateEngine:
    """Manages the persistence, validation, and human approval of the client mandate."""

    def __init__(self, storage_dir: Optional[Path] = None):
        self.storage_dir = storage_dir or (Path.cwd() / "decisions" / "client")
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.mandate_file = self.storage_dir / "mandate.json"

    def save_mandate(self, mandate: ClientMandate) -> Path:
        """Saves client mandate to disk."""
        with open(self.mandate_file, "w", encoding="utf-8") as f:
            json.dump(mandate.dict(), f, indent=2)
        return self.mandate_file

    def load_mandate(self) -> Optional[ClientMandate]:
        """Loads active client mandate from disk."""
        if not self.mandate_file.exists():
            return None
        with open(self.mandate_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return ClientMandate(**data)

    def approve_mandate(self, approved_by: str, rationale: str) -> ClientMandate:
        """Student governance action to formally approve the client mandate.
        
        CRITICAL: Can ONLY be executed with an explicit student identity and rationale.
        """
        mandate = self.load_mandate()
        if not mandate:
            raise FileNotFoundError("No active client mandate found to approve.")

        if not approved_by or len(approved_by.strip()) < 3:
            raise HumanGovernanceError("Approval requires a valid student team member name.")

        if not rationale or len(rationale.strip()) < 10:
            raise HumanGovernanceError("Approval requires an explicit rationale (minimum 10 characters).")

        # Create updated mandate
        updated_dict = mandate.dict()
        updated_dict["human_approved"] = True
        updated_dict["approved_by"] = approved_by.strip()
        updated_dict["approval_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_dict["approval_rationale"] = rationale.strip()

        approved_mandate = ClientMandate(**updated_dict)
        self.save_mandate(approved_mandate)
        return approved_mandate
