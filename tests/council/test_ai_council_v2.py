"""Tests 22-25: AI Council Orchestration, Independence, and Governance Bounds."""

import pytest
from wharton_ic.agents.adapter import LLMAdapter
from wharton_ic.core.config import ConfigManager, ExecutionMode
from wharton_ic.core.exceptions import CouncilPartialError, HumanGovernanceError
from wharton_ic.research.council import SecurityCouncilEngine
from wharton_ic.research.fixtures import get_mock_security_proposals
from wharton_ic.research.models import CommitteeRecommendation, HumanSecurityStatus


def test_22_independent_phase_does_not_leak_other_model_answers():
    """TEST 22: Independent architect inputs do not contain other architect outputs."""
    from wharton_ic.strategy.architects import StrategyArchitectEngine
    from conftest import make_sample_mandate as _make_sample_mandate

    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    strat_a = StrategyArchitectEngine.generate_strategy_a(mandate)
    strat_b = StrategyArchitectEngine.generate_strategy_b(mandate)

    # Distinct philosophies without cross-contamination
    assert strat_a.strategy_name != strat_b.strategy_name
    assert "Moats" in strat_a.strategy_name
    assert "Transitions" in strat_b.strategy_name
    assert strat_a.strategy_id not in strat_b.central_philosophy


def test_23_model_failure_creates_partial_council_not_fake_substitute(monkeypatch):
    """TEST 23: In production, provider failure raises CouncilPartialError rather than substituting fake advice."""
    monkeypatch.setenv("WHARTON_MODE", "PRODUCTION")
    adapter = LLMAdapter(ConfigManager(mode=ExecutionMode.PRODUCTION))

    with pytest.raises(CouncilPartialError) as exc:
        adapter.generate(
            provider="openai",
            model="gpt-4o",
            system_prompt="Test",
            user_prompt="Analyze",
        )
    assert "PRODUCTION ERROR" in str(exc.value)


def test_24_human_approval_cannot_be_created_by_agent():
    """TEST 24: Security council Committee Chair recommendation cannot set HUMAN_APPROVED status."""
    props = get_mock_security_proposals()
    test_alpha = props["TEST_ALPHA"]

    evaluated = SecurityCouncilEngine.evaluate_proposal(test_alpha)
    assert evaluated.committee_recommendation == CommitteeRecommendation.SUPPORT
    # Human status remains PENDING_STUDENT_DECISION until human acts
    assert evaluated.human_status == HumanSecurityStatus.PENDING_STUDENT_DECISION
    assert evaluated.approved_by is None

    # Signoff with empty student name fails
    with pytest.raises(HumanGovernanceError):
        SecurityCouncilEngine.human_signoff(evaluated, approve=True, student_name="", student_notes="Valid notes")


def test_25_council_disagreements_are_preserved():
    """TEST 25: Council preserves opposing recommendations and adversarial conditions."""
    props = get_mock_security_proposals()
    test_gamma = props["TEST_GAMMA"]  # High cash-burn asset

    evaluated = SecurityCouncilEngine.evaluate_proposal(test_gamma)
    assert evaluated.committee_recommendation == CommitteeRecommendation.REJECT
    assert len(evaluated.committee_conditions) > 0
    assert "negative economic spread or distress" in evaluated.committee_conditions[0]
