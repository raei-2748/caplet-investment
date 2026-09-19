"""Strategy Memory Query Engine answering the 14 competition reflection questions."""

from pathlib import Path
from typing import Any, Dict, List, Optional
from wharton_ic.client.engine import ClientMandateEngine
from wharton_ic.journal.engine import DecisionJournalEngine
from wharton_ic.strategy.engine import StrategyCouncilEngine


class StrategyMemoryQueryEngine:
    """Durable structured memory for Team Caplet throughout the competition."""

    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = root_dir or Path.cwd()
        self.client_engine = ClientMandateEngine(self.root_dir / "decisions" / "client")
        self.strategy_engine = StrategyCouncilEngine(self.root_dir / "decisions" / "strategy")
        self.journal_engine = DecisionJournalEngine(self.root_dir / "decisions" / "journal")

    def answer_competition_questions(self) -> Dict[str, Any]:
        """Synthesizes structural answers to the 14 core competition questions."""
        mandate = self.client_engine.load_mandate()
        strategy = self.strategy_engine.get_active_strategy()
        events = self.journal_engine.load_events()
        candidates = self.strategy_engine.get_candidate_strategies()

        # Extract lessons and rejections
        lessons = [e for e in events if e.event_type.value in ["MISTAKE_IDENTIFIED", "LESSON_LEARNED"]]
        rejections = [e for e in events if e.event_type.value in ["COMPANY_REJECTED", "TRADE_REJECTED"]]
        human_decisions = [e for e in events if e.final_student_decision]

        return {
            "1_what_is_our_strategy": strategy.strategy_name if strategy else "Awaiting Student Selection",
            "2_why_did_we_choose_it": (
                strategy.why_appropriate_for_client if strategy else "Awaiting Student Selection"
            ),
            "3_what_alternatives_did_we_reject": [
                c.strategy_name for c in candidates if strategy and c.strategy_id != strategy.strategy_id
            ],
            "4_what_client_facts_motivated_it": [
                f.statement for f in (mandate.financial_objectives if mandate else [])
            ],
            "5_what_assumptions_did_we_make": (
                mandate.assumptions_requiring_student_judgment if mandate else []
            ),
            "6_what_changed": [
                e.title for e in events if e.event_type.value in ["STRATEGY_CHANGED", "THESIS_REVISED"]
            ],
            "7_why_did_it_change": [
                e.reasoning for e in events if e.event_type.value in ["STRATEGY_CHANGED", "THESIS_REVISED"]
            ],
            "8_what_mistakes_did_we_make": [
                {"title": e.title, "details": e.student_discussion} for e in events if e.event_type.value == "MISTAKE_IDENTIFIED"
            ],
            "9_what_did_we_learn": [
                {"title": e.title, "lesson": e.retrospective_lesson or e.reasoning} for e in lessons
            ],
            "10_what_securities_did_we_reject_and_why": [
                {"security": e.title, "reason": e.reasoning} for e in rejections
            ],
            "11_what_risks_worried_us": [
                e.reasoning for e in events if e.event_type.value == "RISK_CONCERN_RAISED"
            ],
            "12_which_decisions_were_made_by_humans": [
                {"date": e.timestamp[:10], "decision": e.final_student_decision, "approvers": e.participants}
                for e in human_decisions
            ],
            "13_which_ideas_originated_from_ai": [
                {"event": e.title, "ai_suggestion": e.ai_recommendations}
                for e in events if e.ai_recommendations
            ],
            "14_status_summary": "All memory dimensions structured and queryable for Final Report.",
        }

    def format_as_markdown(self) -> str:
        data = self.answer_competition_questions()
        lines = [
            "# Team Caplet — Structured Competition Memory",
            "**Durable answers to the 14 core reflection questions for the Final Report.**",
            "",
            f"### 1. What is our strategy?\n{data['1_what_is_our_strategy']}\n",
            f"### 2. Why did we choose it?\n{data['2_why_did_we_choose_it']}\n",
            f"### 3. What alternatives did we reject?\n{', '.join(data['3_what_alternatives_did_we_reject']) or 'None logged'}\n",
            f"### 4. What client facts motivated it?\n{chr(10).join(f'- {f}' for f in data['4_what_client_facts_motivated_it']) or 'None logged'}\n",
            f"### 5. What assumptions did we make?\n{chr(10).join(f'- {a}' for a in data['5_what_assumptions_did_we_make']) or 'None logged'}\n",
            f"### 8. What mistakes did we make?\n{chr(10).join(f'- **{m['title']}**: {m['details']}' for m in data['8_what_mistakes_did_we_make']) or 'None logged yet'}\n",
            f"### 9. What did we learn?\n{chr(10).join(f'- **{l['title']}**: {l['lesson']}' for l in data['9_what_did_we_learn']) or 'None logged yet'}\n",
            f"### 10. What securities did we reject and why?\n{chr(10).join(f'- **{r['security']}**: {r['reason']}' for r in data['10_what_securities_did_we_reject_and_why']) or 'None logged yet'}\n",
        ]
        return "\n".join(lines)
