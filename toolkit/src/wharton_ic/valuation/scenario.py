"""Multi-scenario valuation engine (Bear, Base, Bull cases)."""

from datetime import date
from typing import Dict, Any, Optional
from wharton_ic.schemas.valuation import MultiScenarioValuation, WACCParameters
from wharton_ic.valuation.dcf import run_dcf_valuation

def run_multi_scenario_valuation(
    ticker: str,
    current_share_price: float,
    shares_outstanding: float,
    base_revenue: float,
    wacc_params: WACCParameters,
    total_debt: float = 0.0,
    cash_and_equivalents: float = 0.0,
    valuation_date: Optional[date] = None
) -> MultiScenarioValuation:
    """
    Computes audited Base, Bear, and Bull DCF scenarios under explicit differing assumptions.
    - Base Case: Expected secular growth & historical operating margins.
    - Bear Case: Macro headwinds, margin compression (-300 bps), lower terminal growth.
    - Bull Case: Faster adoption (+300 bps revenue CAGR), operating leverage (+200 bps margin).
    """
    if valuation_date is None:
        valuation_date = date.today()

    # 1. Base Case (5-year forecast: 8% CAGR, 25% margin, 2.5% terminal)
    base_res = run_dcf_valuation(
        ticker=ticker,
        current_share_price=current_share_price,
        shares_outstanding=shares_outstanding,
        base_revenue=base_revenue,
        revenue_growth_rates=[0.08, 0.08, 0.07, 0.06, 0.05],
        target_operating_margins=[0.25, 0.25, 0.25, 0.25, 0.25],
        wacc_params=wacc_params,
        terminal_growth_rate=0.025,
        total_debt=total_debt,
        cash_and_equivalents=cash_and_equivalents,
        valuation_date=valuation_date
    )

    # 2. Bear Case (5-year forecast: 3% CAGR, 22% margin, 2.0% terminal, higher cost of capital +100 bps)
    bear_wacc = WACCParameters(
        risk_free_rate=wacc_params.risk_free_rate,
        equity_risk_premium=wacc_params.equity_risk_premium,
        beta=wacc_params.beta * 1.15,
        cost_of_equity=wacc_params.cost_of_equity + 0.01,
        pre_tax_cost_of_debt=wacc_params.pre_tax_cost_of_debt + 0.01,
        marginal_tax_rate=wacc_params.marginal_tax_rate,
        after_tax_cost_of_debt=wacc_params.after_tax_cost_of_debt + 0.008,
        market_value_equity=wacc_params.market_value_equity,
        total_debt=wacc_params.total_debt,
        weight_equity=wacc_params.weight_equity,
        weight_debt=wacc_params.weight_debt,
        wacc=wacc_params.wacc + 0.01
    )
    bear_res = run_dcf_valuation(
        ticker=ticker,
        current_share_price=current_share_price,
        shares_outstanding=shares_outstanding,
        base_revenue=base_revenue,
        revenue_growth_rates=[0.03, 0.03, 0.02, 0.02, 0.015],
        target_operating_margins=[0.22, 0.22, 0.21, 0.21, 0.20],
        wacc_params=bear_wacc,
        terminal_growth_rate=0.020,
        total_debt=total_debt,
        cash_and_equivalents=cash_and_equivalents,
        valuation_date=valuation_date
    )

    # 3. Bull Case (5-year forecast: 14% CAGR, 28% margin, 3.0% terminal)
    bull_res = run_dcf_valuation(
        ticker=ticker,
        current_share_price=current_share_price,
        shares_outstanding=shares_outstanding,
        base_revenue=base_revenue,
        revenue_growth_rates=[0.15, 0.14, 0.12, 0.10, 0.08],
        target_operating_margins=[0.26, 0.27, 0.28, 0.28, 0.29],
        wacc_params=wacc_params,
        terminal_growth_rate=0.030,
        total_debt=total_debt,
        cash_and_equivalents=cash_and_equivalents,
        valuation_date=valuation_date
    )

    bear_price = float(bear_res.implied_share_price)
    base_price = float(base_res.implied_share_price)
    bull_price = float(bull_res.implied_share_price)

    return MultiScenarioValuation(
        ticker=ticker,
        valuation_date=valuation_date,
        current_price=float(current_share_price),
        bear_case_price=bear_price,
        base_case_price=base_price,
        bull_case_price=bull_price,
        bear_upside_pct=float((bear_price - current_share_price) / current_share_price),
        base_upside_pct=float((base_price - current_share_price) / current_share_price),
        bull_upside_pct=float((bull_price - current_share_price) / current_share_price),
        key_assumptions={
            "wacc_base": wacc_params.wacc,
            "wacc_bear": bear_wacc.wacc,
            "terminal_growth_base": 0.025,
            "terminal_growth_bear": 0.020,
            "terminal_growth_bull": 0.030,
            "base_cagr_5yr": 0.068,
            "bear_cagr_5yr": 0.022,
            "bull_cagr_5yr": 0.117
        }
    )
