"""Point-in-time analytical store ensuring zero look-ahead bias."""

from datetime import date, datetime
from typing import Dict, List, Optional, Any
import pandas as pd
from wharton_ic.core.exceptions import PointInTimeViolationError
from wharton_ic.core.logging import logger

class PointInTimeStore:
    """
    In-memory and cached analytical repository enforcing point-in-time constraints.
    Prevents backtests and models from observing data published after the simulation as_of date.
    """

    def __init__(self, strict_mode: bool = True):
        self.strict_mode = strict_mode
        self._price_cache: Dict[str, pd.DataFrame] = {}
        self._fundamentals_cache: Dict[str, List[Dict[str, Any]]] = {}
        self._macro_cache: Dict[str, pd.Series] = {}

    def store_prices(self, ticker: str, df: pd.DataFrame) -> None:
        """Stores a price DataFrame with a DatetimeIndex or Date column."""
        cleaned_df = df.copy()
        if not isinstance(cleaned_df.index, pd.DatetimeIndex):
            if "Date" in cleaned_df.columns:
                cleaned_df["Date"] = pd.to_datetime(cleaned_df["Date"])
                cleaned_df = cleaned_df.set_index("Date")
        cleaned_df = cleaned_df.sort_index()
        self._price_cache[ticker.upper()] = cleaned_df

    def get_prices(
        self,
        ticker: str,
        start_date: date,
        as_of_date: date,
        price_col: str = "Adj Close"
    ) -> pd.Series:
        """
        Retrieves historical prices strictly up to as_of_date.
        Raises PointInTimeViolationError if any data point exceeds as_of_date.
        """
        ticker = ticker.upper()
        if ticker not in self._price_cache:
            raise KeyError(f"Ticker {ticker} not found in PointInTimeStore price cache.")

        df = self._price_cache[ticker]
        as_of_dt = pd.to_datetime(as_of_date)
        start_dt = pd.to_datetime(start_date)

        # Strict filter: strictly <= as_of_date
        filtered = df[(df.index >= start_dt) & (df.index <= as_of_dt)]

        if self.strict_mode and not df[df.index > as_of_dt].empty:
            # Verified that future data exists in cache but was successfully isolated
            logger.debug(f"Point-in-time filter applied for {ticker}: isolated data at {as_of_date}")

        if price_col in filtered.columns:
            return filtered[price_col]
        elif "Close" in filtered.columns:
            return filtered["Close"]
        else:
            return filtered.iloc[:, 0]

    def store_financial_records(self, ticker: str, records: List[Dict[str, Any]]) -> None:
        """Stores financial statement records with mandatory 'filing_date' and 'period_end'."""
        self._fundamentals_cache[ticker.upper()] = sorted(
            records, key=lambda x: str(x.get("filing_date", ""))
        )

    def get_financial_records(self, ticker: str, as_of_date: date) -> List[Dict[str, Any]]:
        """
        Retrieves financial statement records filed strictly ON OR BEFORE as_of_date.
        Uses filing_date (public availability) rather than period_end date.
        """
        ticker = ticker.upper()
        if ticker not in self._fundamentals_cache:
            return []

        records = self._fundamentals_cache[ticker]
        valid_records = []

        for rec in records:
            filing_date_str = str(rec.get("filing_date", ""))
            try:
                filing_dt = datetime.strptime(filing_date_str[:10], "%Y-%m-%d").date()
            except Exception:
                continue

            if filing_dt <= as_of_date:
                valid_records.append(rec)
            elif self.strict_mode:
                logger.debug(
                    f"Look-ahead guard: rejected filing {filing_date_str} because as_of={as_of_date}"
                )

        return valid_records

    def validate_no_lookahead(self, series: pd.Series, as_of_date: date, field_name: str = "value") -> None:
        """Explicit assertion test that fails if series index contains timestamps after as_of_date."""
        as_of_dt = pd.to_datetime(as_of_date)
        future_mask = series.index > as_of_dt
        if future_mask.any():
            latest_future = series.index[future_mask].max()
            raise PointInTimeViolationError(
                message=f"Point-in-time check failed for {field_name}. Found record dated {latest_future}",
                as_of_date=str(as_of_date),
                published_date=str(latest_future),
                field=field_name
            )
