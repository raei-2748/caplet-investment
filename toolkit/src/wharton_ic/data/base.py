"""Abstract base class for all data providers."""

from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional, Dict, Any
import pandas as pd
from wharton_ic.core.provenance import ProvenanceMetadata

class BaseDataProvider(ABC):
    """Base provider contract enforcing point-in-time integrity across all data sources."""

    def __init__(self, name: str, cache_dir: Optional[str] = None):
        self.name = name
        self.cache_dir = cache_dir

    @abstractmethod
    def get_historical_prices(
        self,
        tickers: List[str],
        start_date: date,
        end_date: date,
        as_of_date: Optional[date] = None
    ) -> pd.DataFrame:
        """
        Retrieves adjusted close price series for given tickers between start and end date.
        If as_of_date is specified, strictly rejects any prices timestamped after as_of_date.
        """
        pass

    @abstractmethod
    def get_financial_statements(
        self,
        ticker: str,
        as_of_date: date
    ) -> List[Dict[str, Any]]:
        """
        Retrieves historical quarterly or annual financial records filed on or before as_of_date.
        Must use filing date (not period end date) to determine point-in-time visibility.
        """
        pass

    @abstractmethod
    def get_risk_free_rate(self, as_of_date: date) -> float:
        """Retrieves the effective risk-free rate (e.g. US 10Y Treasury yield) as of the given date."""
        pass
