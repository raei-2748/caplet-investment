"""Tests 1-5: Wharton Rule Custodian, Precedence, and Provenance."""

import pytest
from pathlib import Path
from wharton_ic.rules.models import (
    AuthorityLevel,
    RuleCategory,
    RuleRecord,
    RuleStatus,
)
from wharton_ic.rules.registry import RuleRegistry
from wharton_ic.rules.validator import RuleValidator, RuleValidationError
from wharton_ic.rules.conflicts import RuleConflictDetector
from wharton_ic.rules.ingestion import OfficialMaterialIngestor, IngestedDocumentRecord


def test_1_unknown_rule_cannot_become_authoritative():
    """TEST 1: Unknown rule cannot have positive confidence or be marked official without verification."""
    rule = RuleRecord(
        rule_id="WHARTON-TEST-UNKNOWN-01",
        category=RuleCategory.PORTFOLIO_CONSTRAINTS,
        title="Unknown Sector Limit",
        exact_or_paraphrased_requirement="Sector limit for 2026-27 is unknown",
        authority_level=AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED,
        source_type="SURVEYMONKEY_APPLY",
        source_title="Portal",
        source_url_or_file="competition/official/2026_27/",
        retrieved_at="2026-09-19",
        status=RuleStatus.UNKNOWN,
        confidence=0.8,  # Invalid: UNKNOWN must have confidence 0.0
    )
    with pytest.raises(RuleValidationError) as exc:
        RuleValidator.assert_valid(rule)
    assert "UNKNOWN rules must have 0.0 confidence" in str(exc.value)


def test_2_private_official_supersedes_public_and_historical():
    """TEST 2: Current private official rule supersedes public and historical rules."""
    public_rule = RuleRecord(
        rule_id="WHARTON-PUB-01",
        category=RuleCategory.TRADING_RULES,
        title="General Trading Guidelines",
        exact_or_paraphrased_requirement="Trade during competition period.",
        authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
        source_type="PUBLIC_WEBSITE",
        source_title="Public Site",
        source_url_or_file="https://wharton.upenn.edu",
        retrieved_at="2026-09-19",
        status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
    )
    private_rule = RuleRecord(
        rule_id="WHARTON-PRIV-01",
        category=RuleCategory.TRADING_RULES,
        title="Specific WInS Simulator Constraints",
        exact_or_paraphrased_requirement="Exactly minimum 10 trades required.",
        authority_level=AuthorityLevel.OFFICIAL_PRIVATE_VERIFIED,
        source_type="SURVEYMONKEY_APPLY",
        source_title="Private Portal PDF",
        source_url_or_file="competition/official/2026_27/rules.pdf",
        retrieved_at="2026-09-19",
        verified_at="Verified by Lead PM",
        status=RuleStatus.OFFICIAL_PRIVATE_VERIFIED,
    )
    winner, loser, reason = RuleConflictDetector.resolve_precedence(public_rule, private_rule)
    assert winner.rule_id == "WHARTON-PRIV-01"
    assert loser.rule_id == "WHARTON-PUB-01"
    assert "higher authority" in reason


def test_3_historical_rule_cannot_overwrite_current_rule():
    """TEST 3: Historical competition rules cannot overwrite active 2026-2027 rules."""
    hist_rule = RuleRecord(
        rule_id="WHARTON-HIST-2024-01",
        category=RuleCategory.PORTFOLIO_CONSTRAINTS,
        title="2024 Historical Position Limit",
        exact_or_paraphrased_requirement="Position cap was 20% in 2024.",
        authority_level=AuthorityLevel.HISTORICAL_ONLY,
        source_type="SURVEYMONKEY_APPLY",
        source_title="2024 Guide",
        source_url_or_file="archive/2024.pdf",
        effective_competition_year="2024-2025",
        retrieved_at="2024-09-19",
        status=RuleStatus.HISTORICAL_ONLY,
    )
    current_rule = RuleRecord(
        rule_id="WHARTON-PUB-2026-01",
        category=RuleCategory.PORTFOLIO_CONSTRAINTS,
        title="2026 Current Philosophy",
        exact_or_paraphrased_requirement="Strategy is not merely a collection of stocks.",
        authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
        source_type="PUBLIC_WEBSITE",
        source_title="Public Webpage",
        source_url_or_file="https://wharton.upenn.edu",
        effective_competition_year="2026-2027",
        retrieved_at="2026-09-19",
        status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
    )
    winner, loser, reason = RuleConflictDetector.resolve_precedence(hist_rule, current_rule)
    assert winner.rule_id == "WHARTON-PUB-2026-01"
    assert loser.rule_id == "WHARTON-HIST-2024-01"
    assert "higher authority" in reason or "current year" in reason


def test_4_unverified_parsed_rule_remains_pending():
    """TEST 4: Ingestion parser proposes rules with status PENDING_HUMAN_VERIFICATION."""
    ingestor = OfficialMaterialIngestor()
    doc_record = IngestedDocumentRecord(
        filename="test_case.pdf",
        sha256_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        document_type="client_case",
        received_date="2026-09-19",
    )
    proposed = ingestor.propose_parsed_rules(doc_record, "Client requires capital preservation over 10 years.")
    assert len(proposed) > 0
    for r in proposed:
        assert r.status == RuleStatus.PENDING_HUMAN_VERIFICATION
        assert r.verified_at is None
        assert "PROPOSED VIA PARSER" in r.notes


def test_5_rule_conflict_is_surfaced():
    """TEST 5: Conflicting rules in the same category are surfaced in ConflictReport."""
    rules = [
        RuleRecord(
            rule_id="R-HIST-01",
            category=RuleCategory.PORTFOLIO_CONSTRAINTS,
            title="Historical Rule",
            exact_or_paraphrased_requirement="Max position 20%",
            authority_level=AuthorityLevel.HISTORICAL_ONLY,
            source_type="SURVEYMONKEY_APPLY",
            source_title="Historical",
            source_url_or_file="hist.pdf",
            effective_competition_year="2024-2025",
            retrieved_at="2024-09-01",
            status=RuleStatus.HISTORICAL_ONLY,
        ),
        RuleRecord(
            rule_id="R-CURR-01",
            category=RuleCategory.PORTFOLIO_CONSTRAINTS,
            title="Current Rule",
            exact_or_paraphrased_requirement="Diversification aligned with client",
            authority_level=AuthorityLevel.OFFICIAL_PUBLIC_VERIFIED,
            source_type="PUBLIC_WEBSITE",
            source_title="Active site",
            source_url_or_file="https://site.org",
            effective_competition_year="2026-2027",
            retrieved_at="2026-09-19",
            status=RuleStatus.OFFICIAL_PUBLIC_VERIFIED,
        ),
    ]
    conflicts = RuleConflictDetector.find_conflicts(rules)
    assert len(conflicts) > 0
    assert conflicts[0].winning_rule_id == "R-CURR-01"
    assert "RESOLVED_BY_AUTHORITY" in conflicts[0].resolution_status
