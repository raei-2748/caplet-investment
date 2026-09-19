"""Point-in-time provenance and data lineage tracking."""

from datetime import datetime, date
from typing import Any, Optional, Union
from pydantic import BaseModel, Field
from wharton_ic.core.exceptions import PointInTimeViolationError

class ProvenanceMetadata(BaseModel):
    """Metadata tracking the origin, publication date, and transformation lineage of a data point."""
    source: str = Field(..., description="Entity or document that originated the data (e.g. 'SEC 10-K', 'Yahoo Finance')")
    source_url: Optional[str] = Field(None, description="Direct URL or API endpoint of origin")
    provider: str = Field(..., description="Data ingestion provider interface (e.g. 'sec_edgar', 'yfinance', 'fred')")
    retrieved_at: datetime = Field(default_factory=datetime.utcnow, description="UTC timestamp of extraction")
    published_at: datetime = Field(..., description="UTC timestamp or filing date when the data became public knowledge")
    as_of: date = Field(..., description="The effective point-in-time date for the analysis")
    period_end: Optional[date] = Field(None, description="Fiscal period end date (e.g. Q3 2025 end date)")
    ticker: Optional[str] = Field(None, description="Associated asset ticker symbol")
    field: str = Field(..., description="Name of the financial metric or observation")
    raw_value: Any = Field(..., description="Unmodified value as extracted from provider")
    transformed_value: Any = Field(..., description="Cleaned, standardized, or normalized value")
    transformation: Optional[str] = Field(None, description="Description of mathematical transformation applied")

    def validate_point_in_time(self, strict: bool = True) -> None:
        """Enforces that published_at <= as_of to prevent look-ahead bias."""
        pub_date = self.published_at.date() if isinstance(self.published_at, datetime) else self.published_at
        if pub_date > self.as_of:
            if strict:
                raise PointInTimeViolationError(
                    message="Information was published after the effective as_of date",
                    as_of_date=str(self.as_of),
                    published_date=str(pub_date),
                    field=self.field
                )

class TrackedValue(BaseModel):
    """A financial value accompanied by its full point-in-time provenance."""
    value: Union[float, int, str, bool, None]
    provenance: ProvenanceMetadata

    def __float__(self) -> float:
        if self.value is None:
            raise ValueError(f"Cannot cast None value for field {self.provenance.field} to float")
        return float(self.value)

    def __repr__(self) -> str:
        return f"TrackedValue({self.value}, as_of={self.provenance.as_of}, src={self.provenance.source})"
