"""Test 10: Human Approval Governance Gate Enforcement."""

import pytest
from datetime import date
from wharton_ic.decisions.ledger import DecisionLedger
from wharton_ic.core.exceptions import HumanApprovalRequiredError
from wharton_ic.schemas.proposal import (
    InvestmentProposal,
    HumanApprovalStatus,
    ClientFitAssessment,
    PortfolioImpactAnalysis,
    MultiScenarioValuation
)

def test_governance_gate_blocks_unapproved_investment(tmp_path):
    """TEST 10: InvestmentProposal cannot proceed to APPROVED without recorded human signature."""
    ledger = DecisionLedger(base_dir=tmp_path)
    ticker = "TEST"
    test_date = date(2025, 10, 1)

    # Verify unapproved state raises HumanApprovalRequiredError
    with pytest.raises(HumanApprovalRequiredError):
        ledger.verify_human_approval(ticker, as_of_date=test_date)

    # Simulate proposal creation
    client_fit = ClientFitAssessment(
        goal_alignment_score=0.9,
        horizon_fit="10-Year",
        liquidity_fit="High",
        risk_capacity_fit="Low Leverage",
        values_and_impact_fit="Aligned",
        strategic_role="Core Compounder",
        summary_rationale="Solid business"
    )
    impact = PortfolioImpactAnalysis(
        marginal_volatility_contribution=0.01,
        marginal_cvar_contribution=0.02,
        current_portfolio_weight=0.0,
        target_portfolio_weight=0.05,
        sector_concentration_post_trade=0.10,
        pairwise_correlation_max=0.5,
        diversification_delta=0.01
    )
    val = MultiScenarioValuation(
        ticker=ticker,
        valuation_date=test_date,
        current_price=100.0,
        bear_case_price=80.0,
        base_case_price=120.0,
        bull_case_price=150.0,
        bear_upside_pct=-0.2,
        base_upside_pct=0.2,
        bull_upside_pct=0.5,
        key_assumptions={}
    )
    proposal = InvestmentProposal(
        ticker=ticker,
        client_fit=client_fit,
        portfolio_role="Core Compounder",
        thesis="Test thesis",
        variant_perception="Test variant",
        business_quality={},
        valuation=val,
        catalysts=["C1"],
        risks=["R1"],
        bear_case="Bear",
        exit_conditions=["E1"],
        expected_horizon="5 Years",
        proposed_weight=0.05,
        portfolio_impact=impact,
        evidence=[],
        confidence=0.8,
        human_status=HumanApprovalStatus.PROPOSED
    )

    ledger.write_decision_record(ticker, proposal, {}, {}, as_of_date=test_date)

    # Initial state must fail verification
    with pytest.raises(HumanApprovalRequiredError):
        ledger.verify_human_approval(ticker, as_of_date=test_date)

    # Record explicit human signature
    ledger.record_human_approval(
        ticker=ticker,
        student_name="Ray (Lead Student Portfolio Manager)",
        allocated_weight=0.05,
        notes="Approved after human debate.",
        as_of_date=test_date
    )

    # Now verification succeeds
    assert ledger.verify_human_approval(ticker, as_of_date=test_date) is True
