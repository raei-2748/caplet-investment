"""Test 4: Data Lineage & Provenance Verification."""

from datetime import date, datetime
from wharton_ic.core.provenance import ProvenanceMetadata, TrackedValue

def test_data_provenance_full_lineage_fields():
    """TEST 4: Every calculated metric contains mandatory provenance tracking fields."""
    prov = ProvenanceMetadata(
        source="SEC Form 10-K",
        source_url="https://www.sec.gov/edgar/data/789019/000095017025000001",
        provider="sec_edgar",
        retrieved_at=datetime.utcnow(),
        published_at=datetime(2025, 7, 30, 20, 0, 0),
        as_of=date(2025, 8, 1),
        period_end=date(2025, 6, 30),
        ticker="MSFT",
        field="free_cash_flow",
        raw_value=74070000000.0,
        transformed_value=74.07,
        transformation="Division by 1e9 to billions USD"
    )

    tracked = TrackedValue(value=74.07, provenance=prov)

    assert tracked.provenance.source == "SEC Form 10-K"
    assert tracked.provenance.provider == "sec_edgar"
    assert tracked.provenance.ticker == "MSFT"
    assert tracked.provenance.field == "free_cash_flow"
    assert tracked.provenance.raw_value == 74070000000.0
    assert tracked.provenance.transformed_value == 74.07
    assert tracked.provenance.transformation is not None
    assert float(tracked) == 74.07
