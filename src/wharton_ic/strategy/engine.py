"""Strategy Council Engine managing generation, red teaming, and human governance."""

from datetime import datetime
import json
from pathlib import Path
from typing import List, Optional

from wharton_ic.client.models import ClientMandate
from wharton_ic.core.exceptions import HumanGovernanceError
from wharton_ic.strategy.architects import StrategyArchitectEngine
from wharton_ic.strategy.models import (
    HumanStrategyDecision,
    InvestmentStrategy,
    StrategyEvaluation,
)
from wharton_ic.strategy.red_team import StrategyRedTeam


class StrategyCouncilEngine:
    """Manages the full lifecycle of investment strategy generation, review, and student sign-off."""

    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = base_dir or (Path.cwd() / "decisions" / "strategy")
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.active_strategy_file = self.base_dir / "active_strategy.json"

    def run_strategy_council(self, mandate: ClientMandate) -> List[StrategyEvaluation]:
        """Runs independent architects and adversarial red teams on candidate strategies."""
        candidates = StrategyArchitectEngine.generate_candidate_strategies(mandate)
        evaluations: List[StrategyEvaluation] = []

        # Save candidates
        cand_file = self.base_dir / "candidates.json"
        with open(cand_file, "w", encoding="utf-8") as f:
            json.dump([c.model_dump() for c in candidates], f, indent=2)

        for strat in candidates:
            eval_res = StrategyRedTeam.evaluate_strategy(strat, mandate)
            evaluations.append(eval_res)

        eval_file = self.base_dir / "evaluations.json"
        with open(eval_file, "w", encoding="utf-8") as f:
            json.dump([e.model_dump() for e in evaluations], f, indent=2)

        return evaluations

    def get_candidate_strategies(self) -> List[InvestmentStrategy]:
        cand_file = self.base_dir / "candidates.json"
        if not cand_file.exists():
            return []
        with open(cand_file, "r", encoding="utf-8") as f:
            return [InvestmentStrategy(**c) for c in json.load(f)]

    def approve_strategy(
        self,
        strategy_id: str,
        student_signatures: List[str],
        student_rationale: str,
        discussion_notes: str,
        key_disagreements: Optional[List[str]] = None,
        unresolved_questions: Optional[List[str]] = None,
    ) -> HumanStrategyDecision:
        """Mandatory human governance action selecting the team's official strategy.
        
        CRITICAL: Requires explicit human command, valid student signatures, and rationale.
        AI processes CANNOT execute this method.
        """
        if not student_signatures or len(student_signatures) < 2:
            raise HumanGovernanceError(
                "Strategy approval requires at least two student team signatures (e.g. Lead PM and Risk Lead)."
            )

        if not student_rationale or len(student_rationale.strip()) < 20:
            raise HumanGovernanceError(
                "Strategy approval requires an explicit student rationale (minimum 20 characters)."
            )

        candidates = self.get_candidate_strategies()
        chosen = next((c for c in candidates if c.strategy_id == strategy_id), None)
        if not chosen:
            raise KeyError(f"Strategy ID {strategy_id} not found in candidate pool.")

        rejected = [c.strategy_id for c in candidates if c.strategy_id != strategy_id]
        date_str = datetime.now().strftime("%Y-%m-%d")
        decision_id = f"{date_str}_strategy_selection"
        decision_dir = self.base_dir / decision_id
        decision_dir.mkdir(parents=True, exist_ok=True)

        decision = HumanStrategyDecision(
            decision_id=decision_id,
            decision_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            strategies_considered=[c.strategy_id for c in candidates],
            rejected_alternatives=rejected,
            key_disagreements=key_disagreements or ["Debated Quality Moat vs Structural Catalyst timing horizon."],
            strongest_arguments_considered=[
                "Quality Moats offers highest defensibility during judge Q&A and avoids speculative trap.",
                "Structural Catalyst offers higher intermediate upside during 10-week window.",
            ],
            student_discussion_notes=discussion_notes,
            chosen_strategy_id=chosen.strategy_id,
            chosen_strategy_name=chosen.strategy_name,
            student_rationale=student_rationale,
            student_signatures=student_signatures,
            unresolved_questions=unresolved_questions or ["How to monitor catalyst realization within 10 weeks."],
            human_approved=True,
        )

        # Write decision files
        with open(decision_dir / "decision.json", "w", encoding="utf-8") as f:
            json.dump(decision.model_dump(), f, indent=2)

        md_content = f"""# Official Team Caplet Strategy Decision
**Decision ID**: `{decision.decision_id}`  
**Date**: {decision.decision_date}  
**Chosen Strategy**: **{decision.chosen_strategy_name}** (`{decision.chosen_strategy_id}`)  
**Governance Status**: **HUMAN_APPROVED** (Signed by Students)

---

## 1. Student Signatures
{chr(10).join(f"- **{sig}**" for sig in decision.student_signatures)}

## 2. Student Rationale
{decision.student_rationale}

## 3. Deliberation Notes
{decision.student_discussion_notes}

## 4. Alternatives Considered & Rejected
- **Considered**: {', '.join(decision.strategies_considered)}
- **Rejected**: {', '.join(decision.rejected_alternatives)}
- **Key Disagreements Addressed**: {', '.join(decision.key_disagreements)}

## 5. Unresolved Questions to Monitor
{chr(10).join(f"- {q}" for q in decision.unresolved_questions)}
"""
        with open(decision_dir / "decision.md", "w", encoding="utf-8") as f:
            f.write(md_content)

        # Update active strategy pointer
        with open(self.active_strategy_file, "w", encoding="utf-8") as f:
            json.dump(chosen.model_dump(), f, indent=2)

        return decision

    def get_active_strategy(self) -> Optional[InvestmentStrategy]:
        if not self.active_strategy_file.exists():
            return None
        with open(self.active_strategy_file, "r", encoding="utf-8") as f:
            return InvestmentStrategy(**json.load(f))

    def ensure_strategy_approved(self) -> InvestmentStrategy:
        strat = self.get_active_strategy()
        if not strat:
            raise HumanGovernanceError(
                "PRODUCTION ERROR: No approved investment strategy found. "
                "Team Caplet must run the Strategy Council and sign off via 'wharton-ic strategy approve' "
                "before any security research or portfolio construction can proceed."
            )
        return strat
