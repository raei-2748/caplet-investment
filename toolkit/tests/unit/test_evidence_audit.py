"""Test 5: Evidence Classification and Fact Verification."""

from wharton_ic.evidence.auditor import EvidenceAuditor

def test_evidence_auditor_claim_classification():
    """TEST 5: EvidenceAuditor accurately classifies fact, calculation, and unsupported claims."""
    verified_numbers = {
        "roic": 0.245,
        "operating_margin": 0.382,
        "base_price": 420.50
    }
    auditor = EvidenceAuditor(verified_numbers)

    # Claim 1: Explicitly tagged calculation matching verified number
    c1 = auditor.audit_claim("- [CALCULATION] The company achieves an ROIC of 0.245.")
    assert c1.claim_type == "CALCULATION"
    assert c1.is_verified is True

    # Claim 2: Tagged fact
    c2 = auditor.audit_claim("- [FACT] The company filed its 10-K on July 30, 2025.")
    assert c2.claim_type == "FACT"
    assert c2.is_verified is True

    # Claim 3: Qualitative inference
    c3 = auditor.audit_claim("- [INFERENCE] High customer switching costs protect enterprise market share.")
    assert c3.claim_type == "INFERENCE"
    assert c3.is_verified is True

    # Claim 4: Untagged claim with invented number not in verified numbers
    c4 = auditor.audit_claim("- Company expects revenue to grow by 45.8% next quarter.")
    assert c4.claim_type == "UNSUPPORTED"
    assert c4.is_verified is False
