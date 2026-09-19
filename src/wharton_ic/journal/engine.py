"""Decision Journal Engine managing immutable timeline reconstruction and Trading Notes."""

from datetime import datetime
import json
from pathlib import Path
from typing import Dict, List, Optional
from wharton_ic.journal.models import JournalEvent, JournalEventType


class DecisionJournalEngine:
    """Manages the append-only competition decision journal and story reconstruction."""

    def __init__(self, journal_dir: Optional[Path] = None):
        self.journal_dir = journal_dir or (Path.cwd() / "decisions" / "journal")
        self.journal_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.journal_dir / "events.jsonl"

    def add_event(self, event: JournalEvent) -> Path:
        """Appends an immutable event to the journal."""
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
            JournalEventType.TRADE_EXECUTED,
            JournalEventType.POSITION_RESIZED,
            JournalEventType.POSITION_SOLD,
        ]]
        if not events:
            return "No trading events recorded in the decision journal yet."

        lines = [
            "# Team Caplet — Official Trading Notes & Execution Log",
            "**Competition Period**: September 28 – December 4, 2026",
            "**Governance Requirement**: Every trade must be justified by strategy alignment and human approval.",
            "",
            "| Date & Time | Action | Ticker / Target | Strategy Justification | Human Approvers |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ]
        for e in events:
            lines.append(
                f"| {e.timestamp} | `{e.event_type.value}` | {e.title} | {e.reasoning} | {', '.join(e.participants)} |"
            )
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
                "date": e.timestamp[:10],
                "event": e.title,
                "what_happened": e.student_discussion,
                "lesson_learned": e.retrospective_lesson or e.reasoning,
            }
            for e in events
        ]

    def reconstruct_evolution_story(self) -> str:
        """Generates the authentic competition narrative: How our thinking evolved."""
        events = self.load_events()
        if not events:
            return "No journal events recorded yet. Begin documenting team discussions to build the competition journey."

        lines = [
            "# How Our Thinking Evolved Over the Competition",
            "### An Authentic Record of Team Caplet's 10-Week Journey",
            "",
        ]

        # Group by phase
        for e in events:
            lines.append(f"### {e.timestamp[:10]}: {e.title}")
            lines.append(f"- **Event Type**: `{e.event_type.value}`")
            lines.append(f"- **Team Members Involved**: {', '.join(e.participants)}")
            lines.append(f"- **The Discussion**: {e.student_discussion}")
            lines.append(f"- **Decision Made**: {e.final_student_decision}")
            lines.append(f"- **Why We Decided This**: {e.reasoning}")
            if e.retrospective_lesson:
                lines.append(f"- **Retrospective Insight**: {e.retrospective_lesson}")
            lines.append("")

        return "\n".join(lines)
