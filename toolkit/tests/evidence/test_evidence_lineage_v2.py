"""Tests 17-21: Rebuilt Evidence Lineage, Anti-Hallucination, and DAG Lineage."""

from wharton_ic.evidence.auditor import EvidenceLineageAuditor
from wharton_ic.evidence.models import (
    ClaimType,
    EvidenceClaim,
    EvidenceGraphNode,
    VerificationStatus,
)


def test_17_fact_text_alone_does_not_verify_claim():
    """TEST 17: Simply prepending [FACT] to an ungrounded string does NOT verify it."""
    auditor = EvidenceLineageAuditor()  # Empty registry
    claim = EvidenceClaim(
        claim_id="CLM-01",
        claim_text="[FACT] Microsoft will double its cloud revenue next year.",
        claim_type_requested=ClaimType.FACTUAL,
        source_ids=["NONEXISTENT-SOURCE"],
        as_of_date="2026-09-19",
    )
    audited = auditor.audit_claim(claim)
    assert audited.verification_status != VerificationStatus.VERIFIED
    assert audited.verification_status == VerificationStatus.UNSUPPORTED
    assert "[FACT]" not in audited.claim_text


def test_18_unsupported_numeric_claim_fails_audit():
    """TEST 18: A calculated metric claim not in deterministic engine registry is UNSUPPORTED."""
    auditor = EvidenceLineageAuditor(known_metrics={"ROIC_MSFT": 0.245})
    claim = EvidenceClaim(
        claim_id="CLM-02",
        claim_text="ROIC is 48.5%",
        claim_type_requested=ClaimType.CALCULATION,
        metric_ids=["ROIC_FABRICATED"],
        as_of_date="2026-09-19",
    )
    audited = auditor.audit_claim(claim)
    assert audited.verification_status == VerificationStatus.UNSUPPORTED
    assert "FAILED_TO_LOCATE_DETERMINISTIC_CALCULATION" in audited.verification_method


def test_19_contradicted_claim_is_flagged():
    """TEST 19: A claim with recorded contradiction IDs is flagged as CONTRADICTED."""
    auditor = EvidenceLineageAuditor(known_source_ids={"FILING-10K-2025"})
    claim = EvidenceClaim(
        claim_id="CLM-03",
        claim_text="Company has zero long-term debt.",
        claim_type_requested=ClaimType.FACTUAL,
        source_ids=["FILING-10K-2025"],
        contradiction_ids=["NOTE-AUDITOR-DEBT-DISCLOSURE-PAGE-45"],
        as_of_date="2026-09-19",
    )
    audited = auditor.audit_claim(claim)
    assert audited.verification_status == VerificationStatus.CONTRADICTED
    assert "CONTRADICTED" in audited.verification_method


def test_20_inference_remains_inference():
    """TEST 20: Qualitative inferences remain INFERENCE and are not falsely promoted to VERIFIED empirical fact."""
    auditor = EvidenceLineageAuditor()
    claim = EvidenceClaim(
        claim_id="CLM-04",
        claim_text="[INFERENCE] Management capital allocation discipline will protect market share.",
        claim_type_requested=ClaimType.INFERENCE,
        as_of_date="2026-09-19",
    )
    audited = auditor.audit_claim(claim)
    assert audited.verification_status == VerificationStatus.INFERENCE
    assert "REASONING_INFERENCE" in audited.verification_method


def test_21_claim_lineage_can_be_traced_back_to_source():
    """TEST 21: Evidence DAG traces lineage: SOURCE -> CALCULATION -> CLAIM."""
    auditor = EvidenceLineageAuditor()
    auditor.register_source("SOURCE-SEC-10K", {"ticker": "TEST_ALPHA", "date": "2025-07-30"})
    auditor.register_calculation("CALC-ROIC", 0.185, parent_source_ids=["SOURCE-SEC-10K"])

    # Add claim node
    auditor.graph.add_node(EvidenceGraphNode(
        node_id="CLAIM-HIGH-ROIC",
        node_type="CLAIM",
        payload={"claim": "TEST_ALPHA achieves 18.5% ROIC"},
        parent_ids=["CALC-ROIC"],
    ))

    lineage = auditor.graph.trace_lineage("CLAIM-HIGH-ROIC")
    assert "CLAIM-HIGH-ROIC" in lineage
    assert "CALC-ROIC" in lineage
    assert "SOURCE-SEC-10K" in lineage
