"""Pydantic schemas for the Wharton Client Mandate."""

from typing import List, Optional, Tuple, Dict, Any
from pydantic import BaseModel, Field

class InvestmentHorizon(BaseModel):
    timeframe_years: int = Field(..., ge=1, le=50)
    timeframe_description: str

class FinancialGoals(BaseModel):
    primary: str
    secondary: Optional[str] = None
    target_wealth_multiplier: Optional[float] = None

class LiquidityNeeds(BaseModel):
    minimum_cash_buffer_pct: float = Field(..., ge=0.0, le=1.0)
    annual_liquidity_draw_pct: float = Field(0.0, ge=0.0, le=1.0)
    emergency_liquidity_days: int = Field(5, ge=1)

class ClientValues(BaseModel):
    impact_objectives: List[str] = Field(default_factory=list)
    exclusion_sectors: List[str] = Field(default_factory=list)

class ClientConstraints(BaseModel):
    min_market_cap_usd: float = Field(..., ge=0)
    min_daily_volume_usd: float = Field(..., ge=0)
    max_emerging_market_exposure: float = Field(0.10, ge=0.0, le=1.0)
    us_exchange_listed_only: bool = True

class SpecialPreferences(BaseModel):
    preferred_themes: List[str] = Field(default_factory=list)

class ClientProfile(BaseModel):
    name: str
    description: str
    investment_horizon: InvestmentHorizon
    financial_goals: FinancialGoals
    liquidity_needs: LiquidityNeeds
    risk_capacity: str
    risk_tolerance: str
    values: ClientValues
    constraints: ClientConstraints
    special_preferences: SpecialPreferences

class PortfolioRoleDefinition(BaseModel):
    target_weight_range: Tuple[float, float]
    description: str

class StrategyRules(BaseModel):
    core_thesis: str
    investment_principles: List[str]
    stock_selection_rules: Dict[str, float]
    portfolio_roles: Dict[str, PortfolioRoleDefinition]
    sell_rules: List[str]
    rebalance_rules: Dict[str, Any]
    review_rules: Dict[str, Any]

class RiskParameters(BaseModel):
    max_position: float = Field(..., ge=0.01, le=1.0)
    min_position: float = Field(..., ge=0.0, le=1.0)
    max_sector: float = Field(..., ge=0.05, le=1.0)
    max_industry: float = Field(..., ge=0.05, le=1.0)
    max_factor_exposure: float = 1.5
    volatility_target: float = 0.14
    drawdown_threshold: float = 0.20
    concentration_limits: Dict[str, Any]

class ClientMandate(BaseModel):
    client: ClientProfile
    strategy: StrategyRules
    risk: RiskParameters
