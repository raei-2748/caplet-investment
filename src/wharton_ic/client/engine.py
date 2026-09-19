"""Client Mandate Engine managing lifecycle, persistence, and human approvals."""

from datetime import datetime
import json
from pathlib import Path
from typing import List, Optional, Union

from wharton_ic.client.models import ClientMandate
from wharton_ic.core.exceptions import HumanGovernanceError
from wharton_ic.governance.roster import TeamRoster


class ClientMandateEngine:
    """Manages the persistence, validation, and human approval of the client mandate."""

    def __init__(self, storage_dir: Optional[Path] = None, roster: Optional[TeamRoster] = None):
        self.storage_dir = storage_dir or (Path.cwd() / "decisions" / "client")
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.mandate_file = self.storage_dir / "mandate.json"
        self.roster = roster or TeamRoster()

    def save_mandate(self, mandate: ClientMandate) -> Path:
        """Saves client mandate to disk."""
        with open(self.mandate_file, "w", encoding="utf-8") as f:
            json.dump(mandate.model_dump(), f, indent=2)
        return self.mandate_file

    def load_mandate(self) -> Optional[ClientMandate]:
        """Loads active client mandate from disk."""
        if not self.mandate_file.exists():
            return None
        with open(self.mandate_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return ClientMandate(**data)

    def approve_mandate(
        self,
        approved_by: Union[str, List[str]],
        rationale: str,
        discussion_notes: Optional[str] = None,
    ) -> ClientMandate:
        """Student governance action to formally approve the client mandate.
        
        CRITICAL: Can ONLY be executed with verified student identities from TeamRoster.
        """
        mandate = self.load_mandate()
        if not mandate:
            raise FileNotFoundError("No active client mandate found to approve.")

        # Convert to list if single string
        signatures = [approved_by] if isinstance(approved_by, str) else list(approved_by)
        if not approved_by or not any(isinstance(s, str) and s.strip() for s in signatures):
            raise HumanGovernanceError("Approval requires a valid student team member name.")
        
        # Verify signatures against team roster (requires at least 1, default 2 if multiple signers expected)
        min_signers = 1 if isinstance(approved_by, str) and len(signatures) == 1 else 2
        validated_members = self.roster.validate_signatures(signatures, min_signers=min_signers)

        if not rationale or len(rationale.strip()) < 10:
            raise HumanGovernanceError("Approval requires an explicit rationale (minimum 10 characters).")

        # Create updated mandate
        updated_dict = mandate.model_dump()
        updated_dict["human_approved"] = True
        updated_dict["approved_by"] = approved_by if isinstance(approved_by, str) else ", ".join(signatures)
        updated_dict["approval_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_dict["approval_rationale"] = rationale.strip()
        
        # Never fabricate discussion notes
        notes = discussion_notes.strip() if discussion_notes and discussion_notes.strip() else "NOT_RECORDED"
        updated_dict["discussion_notes"] = notes

        approved_mandate = ClientMandate(**updated_dict)
        self.save_mandate(approved_mandate)
        return approved_mandate
