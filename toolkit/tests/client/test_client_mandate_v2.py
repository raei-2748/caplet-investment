"""Tests 10-12: Client Mandate Provenance, Classification, and Governance Gate."""

import pytest
from wharton_ic.client.models import ClientMandate, FactCategory, MandateLineItem
from wharton_ic.client.auditor import ClientMandateAuditor
from wharton_ic.client.engine import ClientMandateEngine
from wharton_ic.core.exceptions import HumanGovernanceError


def _make_sample_mandate(with_citation: bool = True, human_approved: bool = False) -> ClientMandate:
    return ClientMandate(
        client_id="CLI-2026-TEST",
        client_name="Test Beneficiary",
        financial_objectives=[
            MandateLineItem(
                item_id="FO-01",
                category=FactCategory.CLIENT_FACT,
                statement="Achieve 7-9% annualized return to fund foundation endowment.",
                official_source_citation="Case Study PDF Page 2, Para 3" if with_citation else None,
            )
        ],
        nonfinancial_objectives=[
            MandateLineItem(
                item_id="NFO-01",
                category=FactCategory.TEAM_INTERPRETATION,
                statement="Preference for clean tech innovation inferred from educational background.",
                official_source_citation=None,
                rationale_or_notes="Deduced by team during initial case briefing.",
            )
        ],
        investment_horizon=MandateLineItem(
            item_id="IH-01",
            category=FactCategory.CLIENT_FACT,
            statement="10-year investment horizon.",
            official_source_citation="Case Study PDF Page 1",
        ),
        liquidity_requirements=MandateLineItem(
            item_id="LR-01",
            category=FactCategory.CLIENT_FACT,
            statement="Low annual liquidity requirement ($50,000 annual distribution).",
            official_source_citation="Case Study PDF Page 2",
        ),
        return_objectives=MandateLineItem(
            item_id="RO-01",
            category=FactCategory.CLIENT_FACT,
            statement="Preserve capital and beat inflation.",
            official_source_citation="Case Study PDF Page 2",
        ),
        risk_tolerance=MandateLineItem(
            item_id="RT-01",
            category=FactCategory.CLIENT_FACT,
            statement="Moderate risk tolerance; drawdown sensitive.",
            official_source_citation="Case Study PDF Page 3",
        ),
        risk_capacity=MandateLineItem(
            item_id="RC-01",
            category=FactCategory.CLIENT_FACT,
            statement="Substantial liquid reserves outside investment portfolio.",
            official_source_citation="Case Study PDF Page 3",
        ),
        drawdown_concerns=MandateLineItem(
            item_id="DC-01",
            category=FactCategory.CLIENT_FACT,
            statement="Client becomes uneasy with drawdowns exceeding 15%.",
            official_source_citation="Case Study PDF Page 3",
        ),
        income_needs=MandateLineItem(
            item_id="IN-01",
            category=FactCategory.CLIENT_FACT,
            statement="No immediate quarterly dividend requirements.",
            official_source_citation="Case Study PDF Page 2",
        ),
        human_approved=human_approved,
    )


def test_10_client_fact_must_have_source():
    """TEST 10: Client facts lacking official citations fail mandate audit."""
    mandate_no_cite = _make_sample_mandate(with_citation=False, human_approved=True)
    audit = ClientMandateAuditor.audit_mandate(mandate_no_cite)
    assert audit.is_compliant is False
    assert len(audit.unsupported_facts) > 0
    assert "lacks official source citation" in audit.unsupported_facts[0]


def test_11_team_interpretation_distinguishable_from_client_fact():
    """TEST 11: Mandate categorizes items into CLIENT_FACT vs TEAM_INTERPRETATION vs STRATEGIC_ASSUMPTION."""
    mandate = _make_sample_mandate(with_citation=True, human_approved=True)
    audit = ClientMandateAuditor.audit_mandate(mandate)
    assert audit.supported_facts_count >= 1
    assert audit.interpretations_count >= 1
    # Check that interpretation cannot claim to be CLIENT_FACT
    assert mandate.nonfinancial_objectives[0].category == FactCategory.TEAM_INTERPRETATION


def test_12_client_mandate_cannot_become_approved_without_human_action(tmp_path):
    """TEST 12: Client mandate cannot be approved without explicit student name and rationale."""
    engine = ClientMandateEngine(storage_dir=tmp_path)
    mandate = _make_sample_mandate(with_citation=True, human_approved=False)
    engine.save_mandate(mandate)

    # Empty name fails
    with pytest.raises(HumanGovernanceError) as exc1:
        engine.approve_mandate(approved_by="", rationale="Valid rationale text here")
    assert "valid student team member name" in str(exc1.value)

    # Short rationale fails
    with pytest.raises(HumanGovernanceError) as exc2:
        engine.approve_mandate(approved_by="Ray (Lead PM)", rationale="Short")
    assert "minimum 10 characters" in str(exc2.value)

    # Valid human approval succeeds
    approved = engine.approve_mandate(approved_by="Ray (Lead PM)", rationale="Approved after team consensus review of official case.")
    assert approved.human_approved is True
    assert approved.approved_by == "Ray (Lead PM)"
