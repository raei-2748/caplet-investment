"""Deterministic Weighted Average Cost of Capital (WACC) calculator."""

from wharton_ic.schemas.valuation import WACCParameters

def calculate_wacc(
    risk_free_rate: float,
    beta: float,
    equity_risk_premium: float = 0.055,
    pre_tax_cost_of_debt: float = 0.050,
    marginal_tax_rate: float = 0.21,
    market_value_equity: float = 1e11,
    total_debt: float = 2e10
) -> WACCParameters:
    """
    Computes rigorous WACC using CAPM and after-tax cost of debt.
    Cost of Equity = Rf + Beta * ERP
    After-tax Cost of Debt = Rd * (1 - Tax Rate)
    WACC = (E/V)*Re + (D/V)*Rd*(1-t)
    """
    beta = max(beta, 0.2)  # Floor beta
    cost_of_equity = risk_free_rate + (beta * equity_risk_premium)
    after_tax_cost_of_debt = pre_tax_cost_of_debt * (1.0 - marginal_tax_rate)

    total_value = market_value_equity + total_debt
    if total_value <= 0:
        total_value = 1.0
    weight_equity = market_value_equity / total_value
    weight_debt = total_debt / total_value

    wacc = (weight_equity * cost_of_equity) + (weight_debt * after_tax_cost_of_debt)
    wacc = max(wacc, 0.04)  # Practical economic hurdle rate floor

    return WACCParameters(
        risk_free_rate=risk_free_rate,
        equity_risk_premium=equity_risk_premium,
        beta=beta,
        cost_of_equity=cost_of_equity,
        pre_tax_cost_of_debt=pre_tax_cost_of_debt,
        marginal_tax_rate=marginal_tax_rate,
        after_tax_cost_of_debt=after_tax_cost_of_debt,
        market_value_equity=market_value_equity,
        total_debt=total_debt,
        weight_equity=weight_equity,
        weight_debt=weight_debt,
        wacc=wacc
    )
