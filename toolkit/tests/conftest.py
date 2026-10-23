"""Pytest fixtures and shared helpers for Wharton IC test suite."""

import pytest
from wharton_ic.client.models import ClientMandate, FactCategory, MandateLineItem


@pytest.fixture
def sample_client_mandate() -> ClientMandate:
    """Provides an audited sample client mandate for testing."""
    return make_sample_mandate()


def make_sample_mandate(with_citation: bool = True, human_approved: bool = False) -> ClientMandate:
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
