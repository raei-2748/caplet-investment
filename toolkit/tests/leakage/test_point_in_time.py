"""Test 1 & Test 6: Point-in-time integrity and look-ahead bias prevention."""

from datetime import date, datetime, timedelta
import pandas as pd
import pytest
from wharton_ic.core.provenance import ProvenanceMetadata
from wharton_ic.core.exceptions import PointInTimeViolationError
from wharton_ic.data.point_in_time import PointInTimeStore

def test_provenance_metadata_lookahead_rejection():
    """TEST 1A: Provenance metadata raises PointInTimeViolationError when published_at > as_of."""
    as_of = date(2025, 6, 1)
    future_pub = datetime(2025, 6, 15, 10, 0, 0)

    prov = ProvenanceMetadata(
        source="SEC 10-Q",
        provider="sec_edgar",
        published_at=future_pub,
        as_of=as_of,
        field="net_income",
        raw_value=1e8,
        transformed_value=1e8
    )

    with pytest.raises(PointInTimeViolationError) as exc_info:
        prov.validate_point_in_time(strict=True)

    assert "Look-Ahead Bias Violation" in str(exc_info.value)
    assert exc_info.value.as_of_date == "2025-06-01"
    assert exc_info.value.published_date == "2025-06-15"

def test_point_in_time_store_price_isolation():
    """TEST 1B: PointInTimeStore strictly filters out prices timestamped after as_of_date."""
    store = PointInTimeStore(strict_mode=True)
    dates = pd.date_range("2025-01-01", "2025-12-31", freq="B")
    prices = pd.DataFrame({"Adj Close": range(len(dates))}, index=dates)
    store.store_prices("AAPL", prices)

    as_of = date(2025, 6, 1)
    retrieved = store.get_prices("AAPL", start_date=date(2025, 1, 1), as_of_date=as_of)

    # Must contain data up to June 1, 2025 and ZERO points thereafter
    assert retrieved.index.max().date() <= as_of
    assert len(retrieved) < len(prices)

def test_point_in_time_store_financial_records_filing_date():
    """TEST 1C: PointInTimeStore filters fundamental records using filing date, not period end."""
    store = PointInTimeStore(strict_mode=True)
    records = [
        {"filing_date": "2025-04-15", "period_end": "2025-03-31", "revenue": 1e8}, # Q1 filed on time
        {"filing_date": "2025-07-20", "period_end": "2025-06-30", "revenue": 1.2e8}, # Q2 filed July 20
    ]
    store.store_financial_records("MSFT", records)

    # As of May 1, 2025: Q1 is visible, Q2 is NOT yet filed
    visible = store.get_financial_records("MSFT", as_of_date=date(2025, 5, 1))
    assert len(visible) == 1
    assert visible[0]["revenue"] == 1e8

    # As of August 1, 2025: Both Q1 and Q2 are visible
    visible_aug = store.get_financial_records("MSFT", as_of_date=date(2025, 8, 1))
    assert len(visible_aug) == 2
