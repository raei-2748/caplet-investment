"""Decision Journal Engine managing immutable timeline reconstruction and Trading Notes."""

from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from wharton_ic.journal.models import JournalEvent, JournalEventType


class DecisionJournalEngine:
    """Manages the append-only, tamper-evident competition decision journal."""

    def __init__(self, journal_dir: Optional[Path] = None):
        self.journal_dir = journal_dir or (Path.cwd() / "decisions" / "journal")
        self.journal_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.journal_dir / "events.jsonl"

    def get_latest_event(self) -> Optional[JournalEvent]:
        """Returns the most recent event in the journal."""
        events = self.load_events()
        return events[-1] if events else None

    def add_event(self, event: JournalEvent) -> Path:
        """Appends an immutable, hash-chained event to the journal."""
        latest = self.get_latest_event()
        prev_hash = latest.event_hash if latest else "GENESIS"

        # Calculate hash if not set
        if not event.event_hash:
            computed_hash = event.compute_canonical_hash(prev_hash=prev_hash)
            event_dict = event.model_dump()
            event_dict["previous_event_hash"] = prev_hash
            event_dict["event_hash"] = computed_hash
            event = JournalEvent(**event_dict)

        # Append to JSONL
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(event.model_dump()) + "\n")

        # Save single event file
        event_path = self.journal_dir / f"{event.timestamp[:10]}_{event.event_id}.json"
        with open(event_path, "w", encoding="utf-8") as f:
            json.dump(event.model_dump(), f, indent=2)

        return event_path

    def load_events(self) -> List[JournalEvent]:
        """Loads all events in chronological order."""
        if not self.log_file.exists():
            return []
        events = []
        with open(self.log_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    events.append(JournalEvent(**json.loads(line.strip())))
        events.sort(key=lambda x: x.timestamp)
        return events

    def verify_chain(self) -> Dict[str, Any]:
        """Verifies cryptographic hash-chain integrity of all journal events."""
        events = self.load_events()
        if not events:
            return {"valid": True, "event_count": 0, "status": "EMPTY_CHAIN"}

        prev_hash = "GENESIS"
        for idx, event in enumerate(events):
            # Check previous hash link
            if event.previous_event_hash != prev_hash:
                return {
                    "valid": False,
                    "tampered_event_id": event.event_id,
                    "index": idx,
                    "reason": f"previous_event_hash mismatch: expected '{prev_hash}', got '{event.previous_event_hash}'"
                }

            # Check canonical payload hash
            expected_hash = event.compute_canonical_hash(prev_hash=prev_hash)
            if event.event_hash != expected_hash:
                return {
                    "valid": False,
                    "tampered_event_id": event.event_id,
                    "index": idx,
                    "reason": f"event_hash mismatch: expected '{expected_hash}', got '{event.event_hash}'"
                }

            prev_hash = event.event_hash

        return {
            "valid": True,
            "event_count": len(events),
            "head_hash": prev_hash,
            "status": "TAMPER_FREE"
        }

    def get_timeline(self) -> List[Dict[str, str]]:
        """Returns simplified timeline of dates, event types, and decisions."""
        events = self.load_events()
        return [
            {
                "timestamp": e.timestamp,
                "type": e.event_type.value,
                "title": e.title,
                "decision": e.final_student_decision,
                "participants": ", ".join(e.participants),
            }
            for e in events
        ]

    def get_trading_notes(self) -> str:
        """Formats Trading Notes required by Wharton deliverable rules."""
        events = [e for e in self.load_events() if e.event_type in [
            JournalEventType.TRADE_PROPOSED,
            JournalEventType.TRADE_APPROVED,
            JournalEventType.TRADE_REJECTED,
            JournalEventType.TRADE_EXECUTED,
            JournalEventType.POSITION_RESIZED,
            JournalEventType.POSITION_SOLD,
        ]]
        if not events:
            return "No trading events recorded in competition decision journal."

        lines = ["# Team Caplet Official Trading Notes\n"]
        for e in events:
            lines.append(f"### [{e.timestamp}] {e.title}")
            lines.append(f"- **Action**: `{e.event_type.value}`")
            lines.append(f"- **Participants**: {', '.join(e.participants)}")
            lines.append(f"- **Final Student Decision**: {e.final_student_decision}")
            lines.append(f"- **Investment Rationale**: {e.reasoning}")
            if e.evidence_available_at_time:
                lines.append(f"- **Evidence Basis**: {', '.join(e.evidence_available_at_time)}")
            if e.alternatives_considered:
                lines.append(f"- **Alternatives Considered**: {', '.join(e.alternatives_considered)}")
            lines.append("")
        return "\n".join(lines)

    def get_lessons(self) -> List[Dict[str, str]]:
        """Extracts mistakes identified and lessons learned."""
        events = [e for e in self.load_events() if e.event_type in [
            JournalEventType.MISTAKE_IDENTIFIED,
            JournalEventType.LESSON_LEARNED,
            JournalEventType.THESIS_REVISED,
        ]]
        return [
            {
                "timestamp": e.timestamp,
                "type": e.event_type.value,
                "title": e.title,
                "reflection": e.retrospective_lesson or e.reasoning,
            }
            for e in events
        ]

    def get_evolution_narrative(self) -> str:
        """Reconstructs the narrative of how the team's thinking evolved."""
        events = self.load_events()
        if not events:
            return "No historical events recorded."
        
        lines = ["# How Our Thinking Evolved: Team Caplet Decision Journey\n"]
        for e in events:
            lines.append(f"**{e.timestamp[:10]} — {e.title}**")
            lines.append(f"*{e.student_discussion}*")
            lines.append(f"→ Decision: {e.final_student_decision}\n")
        return "\n".join(lines)

    def reconstruct_evolution_story(self) -> str:
        """Reconstructs the evolution of team thinking over the competition."""
        events = self.load_events()
        if not events:
            return "# How Our Thinking Evolved Over the Competition\n\nNo events recorded."

        lines = ["# How Our Thinking Evolved Over the Competition\n"]
        for e in events:
            lines.append(f"## [{e.timestamp[:10]}] {e.title}")
            lines.append(f"- **Discussion**: {e.student_discussion}")
            lines.append(f"- **Decision**: {e.final_student_decision}")
            lines.append(f"- **Reasoning**: {e.reasoning}")
            if e.retrospective_lesson:
                lines.append(f"- **Retrospective Lesson**: {e.retrospective_lesson}")
            lines.append("")
        return "\n".join(lines)
