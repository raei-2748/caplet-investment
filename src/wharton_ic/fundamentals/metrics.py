"""Deterministic fundamental financial ratios and accounting forensics."""

from typing import Dict, Any, Optional
import numpy as np

def calculate_roic(operating_income: float, tax_rate: float, total_debt: float, total_equity: float, cash: float) -> float:
    """
    Return on Invested Capital (ROIC) = NOPAT / Invested Capital
    Invested Capital = Total Debt + Total Equity - Excess Cash
    """
    nopat = operating_income * (1.0 - tax_rate)
    invested_capital = max(total_debt + total_equity - cash, 1e6)
    return float(nopat / invested_capital)

def calculate_roe(net_income: float, total_equity: float) -> float:
    """Return on Equity (ROE) = Net Income / Total Equity"""
    if total_equity <= 0:
        return 0.0
    return float(net_income / total_equity)

def calculate_fcf_conversion(free_cash_flow: float, net_income: float) -> float:
    """Cash Flow Quality: FCF Conversion = Free Cash Flow / Net Income"""
    if net_income <= 0:
        return 0.0
    return float(free_cash_flow / net_income)

def calculate_operating_margin(operating_income: float, revenue: float) -> float:
    """Operating Margin = Operating Income / Revenue"""
    if revenue <= 0:
        return 0.0
    return float(operating_income / revenue)

def calculate_net_debt_ebitda(total_debt: float, cash: float, operating_income: float, da: float) -> float:
    """Net Debt to EBITDA = (Total Debt - Cash) / (EBIT + D&A)"""
    ebitda = operating_income + da
    if ebitda <= 0:
        return 999.0  # Distressed leverage flag
    net_debt = total_debt - cash
    return float(max(net_debt / ebitda, -5.0))

def calculate_interest_coverage(operating_income: float, interest_expense: float) -> float:
    """Interest Coverage = EBIT / Interest Expense"""
    if interest_expense <= 0:
        return 50.0  # Pristine balance sheet flag
    return float(operating_income / interest_expense)

def calculate_altman_z_score(
    working_capital: float,
    retained_earnings: float,
    ebit: float,
    market_cap: float,
    total_liabilities: float,
    revenue: float,
    total_assets: float
) -> float:
    """
    Altman Z-Score approximation for manufacturing and non-financial corporates:
    Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.999*X5
    """
    if total_assets <= 0 or total_liabilities <= 0:
        return 1.8  # Grey zone default
    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = market_cap / total_liabilities
    x5 = revenue / total_assets
    z = 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 0.999 * x5
    return float(z)

def calculate_sloan_accrual_ratio(net_income: float, operating_cash_flow: float, total_assets: float) -> float:
    """
    Sloan Accrual Ratio = (Net Income - Operating Cash Flow) / Total Assets
    Lower/negative accruals indicate higher cash quality of earnings.
    """
    if total_assets <= 0:
        return 0.0
    return float((net_income - operating_cash_flow) / total_assets)

def compute_comprehensive_fundamentals(record: Dict[str, Any], market_cap: float) -> Dict[str, float]:
    """Computes all audited fundamental metrics from a point-in-time financial statement record."""
    rev = float(record.get("revenue", 1e8))
    op_inc = float(record.get("operating_income", 2e7))
    net_inc = float(record.get("net_income", 1.5e7))
    fcf = float(record.get("free_cash_flow", 1.2e7))
    ocf = float(record.get("operating_cash_flow", 1.8e7))
    assets = float(record.get("total_assets", 1e8))
    debt = float(record.get("total_debt", 2e7))
    cash = float(record.get("cash_and_equivalents", 1e7))
    equity = float(record.get("total_equity", assets - debt))
    da = float(record.get("depreciation_amortization", op_inc * 0.15))

    roic = calculate_roic(op_inc, 0.21, debt, equity, cash)
    roe = calculate_roe(net_inc, equity)
    fcf_conv = calculate_fcf_conversion(fcf, net_inc)
    op_margin = calculate_operating_margin(op_inc, rev)
    net_debt_ebitda = calculate_net_debt_ebitda(debt, cash, op_inc, da)
    z_score = calculate_altman_z_score(
        working_capital=cash * 0.5,
        retained_earnings=equity * 0.6,
        ebit=op_inc,
        market_cap=market_cap,
        total_liabilities=debt,
        revenue=rev,
        total_assets=assets
    )
    accruals = calculate_sloan_accrual_ratio(net_inc, ocf, assets)

    return {
        "roic": roic,
        "roe": roe,
        "fcf_conversion": fcf_conv,
        "operating_margin": op_margin,
        "net_debt_to_ebitda": net_debt_ebitda,
        "altman_z_score": z_score,
        "accrual_ratio": accruals,
        "pe_ratio": float(market_cap / max(net_inc, 1e5)),
        "fcf_yield": float(fcf / max(market_cap, 1e5))
    }
