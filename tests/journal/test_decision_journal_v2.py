"""Tests 26-28: Competition Decision Journal, Immutability, and Timeline Reconstruction."""

import time
from wharton_ic.journal.engine import DecisionJournalEngine
from wharton_ic.journal.models import JournalEvent, JournalEventType


def test_26_trade_and_decision_records_are_timestamped(tmp_path):
    """TEST 26: Every journal event receives an ISO timestamp upon creation."""
    engine = DecisionJournalEngine(journal_dir=tmp_path)
    evt = JournalEvent(
        event_id="EVT-001",
        event_type=JournalEventType.STRATEGY_PROPOSED,
        title="Quality Moats Philosophy Proposed",
        participants=["Ray (Lead PM)", "Sarah (Analyst)"],
        student_discussion="Discussed focus on ROIC/WACC spreads.",
        final_student_decision="Proceed with Strategy A as primary candidate.",
        reasoning="Matches Elena's long-term endowment objective.",
    )
    path = engine.add_event(evt)
    assert path.exists()

    loaded = engine.load_events()
    assert len(loaded) == 1
    assert loaded[0].timestamp is not None
    assert len(loaded[0].timestamp) >= 10


def test_27_later_edits_do_not_destroy_historical_state(tmp_path):
    """TEST 27: Journal is append-only; logging new events preserves historical decisions unchanged."""
    engine = DecisionJournalEngine(journal_dir=tmp_path)
    evt1 = JournalEvent(
        event_id="EVT-001",
        event_type=JournalEventType.COMPANY_RESEARCHED,
        title="Initial Research on TEST_ALPHA",
        participants=["Ray"],
        student_discussion="Initial look at machine automation moat.",
        final_student_decision="Shortlist for full DCF.",
        reasoning="High switching costs.",
    )
    engine.add_event(evt1)

    time.sleep(0.05)
    evt2 = JournalEvent(
        event_id="EVT-002",
        event_type=JournalEventType.MISTAKE_IDENTIFIED,
        title="Mistake: European Contract Renewal Overlooked",
        participants=["Ray", "Elena"],
        student_discussion="Realized European macro headwinds could slow automation orders.",
        final_student_decision="Pause buy order and add sensitivity shock.",
        reasoning="Intellectual honesty: address risk before allocating.",
        retrospective_lesson="Always verify international customer concentration before sizing.",
    )
    engine.add_event(evt2)

    events = engine.load_events()
    assert len(events) == 2
    # Event 1 remains unaltered
    assert events[0].event_id == "EVT-001"
    assert events[0].title == "Initial Research on TEST_ALPHA"
    # Event 2 recorded chronologically
    assert events[1].event_id == "EVT-002"
    assert events[1].event_type == JournalEventType.MISTAKE_IDENTIFIED


def test_28_timeline_can_reconstruct_decision_evolution(tmp_path):
    """TEST 28: Timeline and story engine reconstruct the authentic evolution of team thinking."""
    engine = DecisionJournalEngine(journal_dir=tmp_path)
    engine.add_event(JournalEvent(
        event_id="EVT-01",
        event_type=JournalEventType.STRATEGY_PROPOSED,
        title="Proposed Quality Moats",
        participants=["Team"],
        student_discussion="Initial debate",
        final_student_decision="Adopt Quality Moats",
        reasoning="Defensibility",
    ))
    engine.add_event(JournalEvent(
        event_id="EVT-02",
        event_type=JournalEventType.THESIS_REVISED,
        title="Revised Valuation Thresholds",
        participants=["Team"],
        student_discussion="Valuation was too aggressive",
        final_student_decision="Demand 15% margin of safety",
        reasoning="Prevent overpaying in volatile market",
        retrospective_lesson="Margin of safety is our most reliable risk management tool.",
    ))

    story = engine.reconstruct_evolution_story()
    assert "How Our Thinking Evolved Over the Competition" in story
    assert "Proposed Quality Moats" in story
    assert "Revised Valuation Thresholds" in story
    assert "Margin of safety is our most reliable risk management tool" in story
