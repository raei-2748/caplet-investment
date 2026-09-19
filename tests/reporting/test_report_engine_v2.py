"""Tests 29-33: Report Engine V2, AI Authorship Firewall, and Deliverable Compliance."""

import pytest
from pathlib import Path
from wharton_ic.reporting_v2.engine import WhartonReportEngineV2
from wharton_ic.reporting_v2.firewall import AIAuthorshipFirewall, AIAuthorshipViolationError
from wharton_ic.reporting_v2.models import AuthorshipType, ContentBlock
from wharton_ic.rules.registry import RuleRegistry
from wharton_ic.client.engine import ClientMandateEngine
from wharton_ic.strategy.engine import StrategyCouncilEngine
from wharton_ic.journal.engine import DecisionJournalEngine
from conftest import make_sample_mandate as _make_sample_mandate


def test_29_final_report_compiler_rejects_unlabeled_ai_prose(tmp_path):
    """TEST 29: Compiler fails if an unlabeled AI_GENERATED prose block attempts to enter submission text."""
    engine = WhartonReportEngineV2(root_dir=tmp_path)
    blocks = [
        ContentBlock(
            block_id="B-01",
            section_id="intro",
            authorship_type=AuthorshipType.HUMAN_AUTHORED,
            author_identity="Student A",
            content_text="Team Caplet approaches this mandate with disciplined fiduciary care."
        ),
        ContentBlock(
            block_id="B-02",
            section_id="analysis",
            authorship_type=AuthorshipType.AI_GENERATED,  # Prohibited without synthesis/disclosure
            author_identity="frontier_llm",
            content_text="This company has strong competitive moats and should be bought immediately."
        )
    ]
    with pytest.raises(AIAuthorshipViolationError) as exc:
        engine.compile_final_report(blocks)
    assert "raw AI_GENERATED text" in str(exc.value)


def test_30_factual_claims_in_evidence_pack_have_source_linkage(tmp_path):
    """TEST 30: All verified rules and client facts in the evidence pack carry source tracking."""
    registry = RuleRegistry(Path.cwd())
    engine = WhartonReportEngineV2(root_dir=tmp_path)
    pack = engine.assemble_evidence_pack(rule_registry=registry)

    assert len(pack.verified_rules) > 0
    for r in pack.verified_rules:
        assert "source_url_or_file" in r
        assert r["source_url_or_file"] is not None


def test_31_missing_evidence_is_surfaced(tmp_path):
    """TEST 31: Evidence pack detects and surfaces missing approvals or unverified mandates."""
    engine = WhartonReportEngineV2(root_dir=tmp_path)
    # With empty client and strategy engines, pack alerts must trigger
    pack = engine.assemble_evidence_pack()

    assert len(pack.missing_evidence_alerts) >= 2
    assert any("Client Mandate" in alert for alert in pack.missing_evidence_alerts)
    assert any("Investment Strategy" in alert for alert in pack.missing_evidence_alerts)


def test_32_official_requirement_coverage_can_be_audited(tmp_path):
    """TEST 32: System verifies that all mandatory public deliverables are accounted for."""
    registry = RuleRegistry()
    rules = registry.list_rules()
    deliverable_rules = [r for r in rules if r.category.value == "DELIVERABLES"]

    deliv_names = [r.title for r in deliverable_rules]
    assert any("Investment Policy Statement" in name for name in deliv_names)
    assert any("Comprehensive Final Report" in name for name in deliv_names)
    assert any("Trading Notes" in name for name in deliv_names)


def test_33_compiler_distinguishes_official_requirements_from_team_design(tmp_path):
    """TEST 33: Evidence pack labels section blueprint as TEAM CAPLET REPORT ARCHITECTURE until official private rubric is ingested."""
    engine = WhartonReportEngineV2(root_dir=tmp_path)
    pack = engine.assemble_evidence_pack()
    assert "TEAM CAPLET REPORT ARCHITECTURE" in pack.architecture_label
    assert "Awaiting Official Private Rubric" in pack.architecture_label
