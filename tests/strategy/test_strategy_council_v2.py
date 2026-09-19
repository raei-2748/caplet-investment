"""Tests 13-16: Strategy Council, Red Team, and Human Strategy Gate."""

import pytest
from wharton_ic.client.models import ClientMandate, FactCategory, MandateLineItem
from wharton_ic.core.exceptions import HumanGovernanceError
from wharton_ic.strategy.engine import StrategyCouncilEngine
from conftest import make_sample_mandate as _make_sample_mandate


def test_13_ai_cannot_approve_strategy(tmp_path):
    """TEST 13: Strategy cannot be marked approved by automated agent without human signatures."""
    engine = StrategyCouncilEngine(base_dir=tmp_path)
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    engine.run_strategy_council(mandate)

    # Empty signatures raises HumanGovernanceError
    with pytest.raises(HumanGovernanceError) as exc:
        engine.approve_strategy(
            strategy_id="STRAT-A-QUALITY-MOAT",
            student_signatures=[],
            student_rationale="Long enough rationale to pass length test",
            discussion_notes="Deliberation notes"
        )
    assert "at least two student team signatures" in str(exc.value)


def test_14_human_strategy_approval_requires_explicit_rationale(tmp_path):
    """TEST 14: Human strategy approval requires minimum 20 characters of authentic rationale."""
    engine = StrategyCouncilEngine(base_dir=tmp_path)
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    engine.run_strategy_council(mandate)

    # Short rationale fails
    with pytest.raises(HumanGovernanceError) as exc:
        engine.approve_strategy(
            strategy_id="STRAT-A-QUALITY-MOAT",
            student_signatures=["Student A", "Student B"],
            student_rationale="Too short",
            discussion_notes="Notes"
        )
    assert "minimum 20 characters" in str(exc.value)

    # Valid approval succeeds
    decision = engine.approve_strategy(
        strategy_id="STRAT-A-QUALITY-MOAT",
        student_signatures=["Student A (Lead PM)", "Student B (Risk Lead)"],
        student_rationale="Unanimously chosen for economic moat defensibility against judge Q&A scrutiny.",
        discussion_notes="Extensive debate over 10-week catalyst horizon vs quality compounding."
    )
    assert decision.human_approved is True
    assert decision.chosen_strategy_id == "STRAT-A-QUALITY-MOAT"


def test_15_strategy_alternatives_and_rejections_preserved(tmp_path):
    """TEST 15: Decision records preserve rejected candidate strategies for report reflection."""
    engine = StrategyCouncilEngine(base_dir=tmp_path)
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    engine.run_strategy_council(mandate)

    decision = engine.approve_strategy(
        strategy_id="STRAT-A-QUALITY-MOAT",
        student_signatures=["Student A", "Student B"],
        student_rationale="Chosen for long-term client suitability and defensibility in finals.",
        discussion_notes="Debated A vs B vs C."
    )
    assert len(decision.strategies_considered) == 3
    assert len(decision.rejected_alternatives) == 2
    assert "STRAT-B-ASYMMETRIC-TRANSITION" in decision.rejected_alternatives
    assert "STRAT-C-ALL-WEATHER" in decision.rejected_alternatives


def test_16_every_final_strategy_principle_links_to_client(tmp_path):
    """TEST 16: Approved strategy explicitly documents relationship to client and rationale."""
    engine = StrategyCouncilEngine(base_dir=tmp_path)
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    engine.run_strategy_council(mandate)

    engine.approve_strategy(
        strategy_id="STRAT-A-QUALITY-MOAT",
        student_signatures=["Student A", "Student B"],
        student_rationale="Optimal fit for long-term capital compounding and preservation.",
        discussion_notes="Notes"
    )
    strat = engine.get_active_strategy()
    assert strat is not None
    assert strat.relationship_to_client is not None
    assert len(strat.relationship_to_client) > 20
    assert strat.why_appropriate_for_client is not None
