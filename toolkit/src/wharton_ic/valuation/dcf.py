"""Deterministic Discounted Cash Flow (DCF) and Reverse DCF models."""

from datetime import date
from typing import List, Dict, Optional, Tuple
import numpy as np
from scipy.optimize import root_scalar
from wharton_ic.schemas.valuation import (
    DCFValuationResult,
    ProjectedCashFlow,
    WACCParameters,
)

def run_dcf_valuation(
    ticker: str,
    current_share_price: float,
    shares_outstanding: float,
    base_revenue: float,
    revenue_growth_rates: List[float],
    target_operating_margins: List[float],
    wacc_params: WACCParameters,
    terminal_growth_rate: float = 0.025,
    tax_rate: float = 0.21,
    reinvestment_rate: float = 0.25,
    total_debt: float = 0.0,
    cash_and_equivalents: float = 0.0,
    valuation_date: Optional[date] = None
) -> DCFValuationResult:
    """
    Executes a multi-stage deterministic DCF model with explicit cash flow schedules,
    terminal value calculation, enterprise-to-equity bridge, and 2D sensitivity analysis.
    """
    if valuation_date is None:
        valuation_date = date.today()

    wacc = wacc_params.wacc
    n_years = len(revenue_growth_rates)
    projected_flows: List[ProjectedCashFlow] = []
    
    current_rev = base_revenue
    sum_pv_fcf = 0.0

    for i in range(n_years):
        year = i + 1
        growth = revenue_growth_rates[i]
        op_margin = target_operating_margins[i]

        current_rev = current_rev * (1.0 + growth)
        operating_income = current_rev * op_margin
        nopat = operating_income * (1.0 - tax_rate)

        # Reinvestment: Capex - D&A + Delta NWC
        reinvestment = nopat * reinvestment_rate
        fcf = nopat - reinvestment

        discount_factor = 1.0 / ((1.0 + wacc) ** year)
        pv_fcf = fcf * discount_factor
        sum_pv_fcf += pv_fcf

        projected_flows.append(ProjectedCashFlow(
            year=year,
            projected_revenue=float(current_rev),
            revenue_growth_rate=float(growth),
            operating_margin=float(op_margin),
            operating_income=float(operating_income),
            tax_rate=float(tax_rate),
            nopat=float(nopat),
            depreciation_amortization=float(reinvestment * 0.4),
            capital_expenditures=float(reinvestment * 1.2),
            change_in_working_capital=float(reinvestment * 0.2),
            free_cash_flow=float(fcf),
            discount_factor=float(discount_factor),
            present_value_fcf=float(pv_fcf)
        ))

    # Terminal Value calculation (Gordon Growth Model)
    # FCF_{N+1} = FCF_N * (1 + g)
    terminal_fcf = projected_flows[-1].free_cash_flow * (1.0 + terminal_growth_rate)
    terminal_discount = max(wacc - terminal_growth_rate, 0.005)
    tv_undiscounted = terminal_fcf / terminal_discount
    pv_tv = tv_undiscounted / ((1.0 + wacc) ** n_years)

    enterprise_value = sum_pv_fcf + pv_tv
    implied_equity_value = enterprise_value - total_debt + cash_and_equivalents
    implied_share_price = implied_equity_value / max(shares_outstanding, 1.0)
    upside_pct = (implied_share_price - current_share_price) / current_share_price

    # Reverse DCF: Solve for implied terminal growth rate matching current price
    def price_error(g: float) -> float:
        t_disc = max(wacc - g, 0.002)
        u_tv = (projected_flows[-1].free_cash_flow * (1.0 + g)) / t_disc
        p_tv = u_tv / ((1.0 + wacc) ** n_years)
        eq_val = sum_pv_fcf + p_tv - total_debt + cash_and_equivalents
        return (eq_val / shares_outstanding) - current_share_price

    reverse_dcf_growth: Optional[float] = None
    try:
        sol = root_scalar(price_error, bracket=[-0.05, min(wacc - 0.005, 0.08)], method="brentq")
        if sol.converged:
            reverse_dcf_growth = float(sol.root)
    except Exception:
        reverse_dcf_growth = None

    # 2D Sensitivity Matrix: WACC (+- 1.5%) vs Terminal Growth (+- 1.0%)
    wacc_steps = [wacc - 0.015, wacc - 0.0075, wacc, wacc + 0.0075, wacc + 0.015]
    g_steps = [
        terminal_growth_rate - 0.010,
        terminal_growth_rate - 0.005,
        terminal_growth_rate,
        terminal_growth_rate + 0.005,
        terminal_growth_rate + 0.010
    ]

    sensitivity: Dict[str, Dict[str, float]] = {}
    for w in wacc_steps:
        w_key = f"{w*100:.2f}%"
        sensitivity[w_key] = {}
        for g in g_steps:
            g_key = f"{g*100:.2f}%"
            denom = max(w - g, 0.002)
            pv_cash_flows = sum(
                pf.free_cash_flow / ((1.0 + w) ** pf.year) for pf in projected_flows
            )
            sim_tv = (projected_flows[-1].free_cash_flow * (1.0 + g)) / denom
            sim_pv_tv = sim_tv / ((1.0 + w) ** n_years)
            sim_eq = pv_cash_flows + sim_pv_tv - total_debt + cash_and_equivalents
            sim_price = sim_eq / shares_outstanding
            sensitivity[w_key][g_key] = round(float(sim_price), 2)

    return DCFValuationResult(
        ticker=ticker,
        valuation_date=valuation_date,
        current_share_price=float(current_share_price),
        shares_outstanding=float(shares_outstanding),
        wacc_details=wacc_params,
        projection_horizon_years=n_years,
        projected_cash_flows=projected_flows,
        sum_pv_fcf=float(sum_pv_fcf),
        terminal_growth_rate=float(terminal_growth_rate),
        terminal_value_undiscounted=float(tv_undiscounted),
        pv_terminal_value=float(pv_tv),
        enterprise_value=float(enterprise_value),
        total_debt=float(total_debt),
        cash_and_equivalents=float(cash_and_equivalents),
        implied_equity_value=float(implied_equity_value),
        implied_share_price=float(implied_share_price),
        implied_upside_downside_pct=float(upside_pct),
        reverse_dcf_implied_growth=reverse_dcf_growth,
        sensitivity_matrix=sensitivity
    )
