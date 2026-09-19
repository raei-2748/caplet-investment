"""Security and universe schemas for Wharton IC."""

from enum import Enum
from typing import Optional, List, Dict, Any
from datetime import date
from pydantic import BaseModel, Field

class AssetType(str, Enum):
    EQUITY = "EQUITY"
    ETF = "ETF"
    CASH = "CASH"

class SecurityMetadata(BaseModel):
    ticker: str = Field(..., description="Standardized ticker symbol")
    name: str = Field(..., description="Company or ETF name")
    asset_type: AssetType = AssetType.EQUITY
    gics_sector: str = Field(..., description="GICS Sector classification")
    gics_industry: str = Field(..., description="GICS Industry classification")
    exchange: str = Field("NASDAQ/NYSE", description="Primary listing exchange")
    country: str = Field("USA", description="Country of domicile")
    currency: str = Field("USD", description="Trading currency")
    is_wharton_approved: bool = Field(True, description="Whether the security is on the official Wharton list")
    market_cap_usd: Optional[float] = None
    average_daily_volume_usd: Optional[float] = None
    delisted: bool = False
    notes: Optional[str] = None

class SecurityPriceBar(BaseModel):
    ticker: str
    timestamp: date
    open: float
    high: float
    low: float
    close: float
    adjusted_close: float
    volume: float

class FinancialStatementRecord(BaseModel):
    ticker: str
    as_of: date
    filing_date: date
    fiscal_period: str
    revenue: float
    gross_profit: float
    operating_income: float
    net_income: float
    operating_cash_flow: float
    capital_expenditures: float
    free_cash_flow: float
    total_assets: float
    total_liabilities: float
    total_equity: float
    total_debt: float
    cash_and_equivalents: float
    shares_outstanding: float
