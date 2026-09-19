"""Approved Universe Engine enforcing Wharton security constraints."""

from pathlib import Path
from typing import Dict, List, Optional, Set
import pandas as pd
from wharton_ic.schemas.security import SecurityMetadata, AssetType
from wharton_ic.universe.default_universe import DEFAULT_APPROVED_SECURITIES
from wharton_ic.core.exceptions import UniverseViolationError
from wharton_ic.core.logging import logger

class ApprovedUniverseEngine:
    """
    Authoritative manager of Wharton-approved securities.
    Guarantees no investment agent can research or propose a non-approved asset.
    """

    def __init__(self, official_csv_path: Optional[Path] = None):
        self._securities: Dict[str, SecurityMetadata] = {}
        self._sectors: Dict[str, List[str]] = {}
        self._load_universe(official_csv_path)

    def _load_universe(self, official_csv_path: Optional[Path]) -> None:
        """Loads securities from official Wharton CSV if available, or default universe."""
        loaded_from_official = False

        if official_csv_path and official_csv_path.exists():
            try:
                df = pd.read_csv(official_csv_path)
                logger.info(f"Ingesting official Wharton approved securities from {official_csv_path}")
                for _, row in df.iterrows():
                    ticker = self.normalize_ticker(str(row.get("ticker", row.get("Symbol", ""))))
                    if not ticker:
                        continue
                    sec = SecurityMetadata(
                        ticker=ticker,
                        name=str(row.get("name", row.get("Company", ticker))),
                        asset_type=AssetType.ETF if "ETF" in str(row.get("type", "")).upper() else AssetType.EQUITY,
                        gics_sector=str(row.get("sector", row.get("Sector", "Unclassified"))),
                        gics_industry=str(row.get("industry", row.get("Industry", "Unclassified"))),
                        market_cap_usd=float(row.get("market_cap", 1e10)) if pd.notna(row.get("market_cap")) else None,
                        is_wharton_approved=True
                    )
                    self._securities[ticker] = sec
                loaded_from_official = True
            except Exception as e:
                logger.warning(f"Could not load official CSV ({e}). Falling back to verified default universe.")

        if not loaded_from_official:
            for sec in DEFAULT_APPROVED_SECURITIES:
                self._securities[sec.ticker] = sec

        # Index sectors
        for ticker, sec in self._securities.items():
            sector = sec.gics_sector
            if sector not in self._sectors:
                self._sectors[sector] = []
            self._sectors[sector].append(ticker)

        logger.info(f"ApprovedUniverseEngine initialized with {len(self._securities)} eligible securities.")

    @staticmethod
    def normalize_ticker(raw_ticker: str) -> str:
        """Standardizes ticker symbols across exchanges and data providers."""
        if not raw_ticker:
            return ""
        ticker = raw_ticker.strip().upper()
        ticker = ticker.replace("/", "-").replace(".", "-")
        return ticker

    def is_eligible(self, ticker: str) -> bool:
        """Checks if ticker exists in the approved list and is active."""
        norm_ticker = self.normalize_ticker(ticker)
        sec = self._securities.get(norm_ticker)
        if sec is None or sec.delisted or not sec.is_wharton_approved:
            return False
        return True

    def validate_ticker(self, ticker: str) -> SecurityMetadata:
        """Validates eligibility or raises UniverseViolationError."""
        norm_ticker = self.normalize_ticker(ticker)
        if not self.is_eligible(norm_ticker):
            raise UniverseViolationError(
                ticker=norm_ticker,
                reason="Ticker is not present in the authoritative Wharton approved securities universe."
            )
        return self._securities[norm_ticker]

    def get_metadata(self, ticker: str) -> SecurityMetadata:
        """Returns metadata for a valid ticker."""
        return self.validate_ticker(ticker)

    def get_all_tickers(self, equities_only: bool = False) -> List[str]:
        """Returns list of all approved ticker symbols."""
        if equities_only:
            return [t for t, s in self._securities.items() if s.asset_type == AssetType.EQUITY and not s.delisted]
        return [t for t, s in self._securities.items() if not s.delisted]

    def get_sector_map(self) -> Dict[str, str]:
        """Returns mapping from ticker to GICS sector."""
        return {t: s.gics_sector for t, s in self._securities.items()}

    def get_tickers_by_sector(self, sector: str) -> List[str]:
        """Returns all approved tickers in a given GICS sector."""
        return self._sectors.get(sector, [])

    def get_all_sectors(self) -> List[str]:
        """Returns unique list of GICS sectors."""
        return list(self._sectors.keys())

# Default universe engine instance
universe_engine = ApprovedUniverseEngine()
