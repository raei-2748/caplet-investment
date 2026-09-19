"""Schemas for deterministic valuation models."""

from datetime import datetime, date
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class WACCParameters(BaseModel):
    risk_free_rate: float = Field(..., description="Risk-free rate (e.g. 10Y US Treasury)")
    equity_risk_premium: float = Field(0.055, description="Expected equity market risk premium")
    beta: float = Field(..., description="Stock beta relative to market")
    cost_of_equity: float = Field(..., description="CAPM derived cost of equity: Rf + Beta * ERP")
    pre_tax_cost_of_debt: float = Field(..., description="Effective interest rate on company debt")
    marginal_tax_rate: float = Field(0.21, description="Corporate tax rate")
    after_tax_cost_of_debt: float = Field(..., description="Cost of debt net of tax shield")
    market_value_equity: float = Field(..., description="Current equity market cap")
    total_debt: float = Field(..., description="Total outstanding interest-bearing debt")
    weight_equity: float = Field(..., description="Equity / (Equity + Debt)")
    weight_debt: float = Field(..., description="Debt / (Equity + Debt)")
    wacc: float = Field(..., description="Weighted Average Cost of Capital")

class ProjectedCashFlow(BaseModel):
    year: int
    projected_revenue: float
    revenue_growth_rate: float
    operating_margin: float
    operating_income: float
    tax_rate: float
    nopat: float
    depreciation_amortization: float
    capital_expenditures: float
    change_in_working_capital: float
    free_cash_flow: float
    discount_factor: float
    present_value_fcf: float

class DCFValuationResult(BaseModel):
    ticker: str
    valuation_date: date
    current_share_price: float
    shares_outstanding: float
    wacc_details: WACCParameters
    projection_horizon_years: int
    projected_cash_flows: List[ProjectedCashFlow]
    sum_pv_fcf: float
    terminal_growth_rate: float
    terminal_value_undiscounted: float
    pv_terminal_value: float
    enterprise_value: float
    total_debt: float
    cash_and_equivalents: float
    implied_equity_value: float
    implied_share_price: float
    implied_upside_downside_pct: float
    reverse_dcf_implied_growth: Optional[float] = None
    sensitivity_matrix: Dict[str, Dict[str, float]] = Field(
        default_factory=dict,
        description="2D Matrix of implied share price: Outer key = WACC, Inner key = Terminal Growth Rate"
    )

class ComparableCompanyValuation(BaseModel):
    target_ticker: str
    valuation_date: date
    peer_tickers: List[str]
    target_metric_values: Dict[str, float]  # e.g. {'pe': 25.0, 'ev_ebitda': 18.0}
    peer_multiples_median: Dict[str, float]
    peer_multiples_mean: Dict[str, float]
    implied_price_by_pe: Optional[float] = None
    implied_price_by_ev_ebitda: Optional[float] = None
    implied_price_by_ps: Optional[float] = None
    composite_implied_price: float

class MultiScenarioValuation(BaseModel):
    ticker: str
    valuation_date: date
    current_price: float
    bear_case_price: float
    base_case_price: float
    bull_case_price: float
    bear_upside_pct: float
    base_upside_pct: float
    bull_upside_pct: float
    key_assumptions: Dict[str, Any]
    model_timestamp: datetime = Field(default_factory=datetime.utcnow)
