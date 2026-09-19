"""Quantitative risk metrics, tail risk, and marginal risk contributions."""

from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd

def calculate_portfolio_returns(weights: np.ndarray, returns_df: pd.DataFrame) -> pd.Series:
    """Computes daily portfolio return series given weight vector and asset returns matrix."""
    return (returns_df * weights).sum(axis=1)

def calculate_cagr(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Computes Compound Annual Growth Rate (CAGR)."""
    if len(returns) == 0:
        return 0.0
    cum_ret = (1.0 + returns).prod()
    n_years = len(returns) / periods_per_year
    if n_years <= 0 or cum_ret <= 0:
        return 0.0
    return float((cum_ret ** (1.0 / n_years)) - 1.0)

def calculate_annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    """Computes sample annualized standard deviation."""
    if len(returns) < 2:
        return 0.0
    return float(returns.std(ddof=1) * np.sqrt(periods_per_year))

def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.04, periods_per_year: int = 252) -> float:
    """Computes annualized Sharpe ratio."""
    vol = calculate_annualized_volatility(returns, periods_per_year)
    if vol <= 1e-6:
        return 0.0
    rf_daily = risk_free_rate / periods_per_year
    excess = returns - rf_daily
    return float(excess.mean() / returns.std(ddof=1) * np.sqrt(periods_per_year))

def calculate_sortino_ratio(returns: pd.Series, risk_free_rate: float = 0.04, periods_per_year: int = 252) -> float:
    """Computes annualized Sortino ratio using downside semi-deviation."""
    rf_daily = risk_free_rate / periods_per_year
    excess = returns - rf_daily
    downside = excess[excess < 0]
    if len(downside) < 2:
        return 0.0
    downside_vol = float(downside.std(ddof=1) * np.sqrt(periods_per_year))
    if downside_vol <= 1e-6:
        return 0.0
    return float(excess.mean() * periods_per_year / downside_vol)

def calculate_max_drawdown(returns: pd.Series) -> float:
    """Computes peak-to-trough maximum drawdown."""
    if len(returns) == 0:
        return 0.0
    wealth_index = (1.0 + returns).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    return float(drawdowns.min())

def calculate_var_cvar(
    returns: pd.Series,
    confidence_level: float = 0.95
) -> Dict[str, float]:
    """
    Computes historical Value at Risk (VaR) and Conditional Value at Risk (CVaR / Expected Shortfall).
    Returned as positive loss percentages.
    """
    if len(returns) == 0:
        return {"var_historical": 0.0, "cvar_historical": 0.0, "var_parametric": 0.0}

    # Historical VaR and CVaR
    quantile = 1.0 - confidence_level
    var_hist = -float(np.percentile(returns, quantile * 100.0))
    tail_losses = returns[returns <= -var_hist]
    cvar_hist = -float(tail_losses.mean()) if not tail_losses.empty else var_hist

    # Parametric Gaussian VaR
    mu = returns.mean()
    sigma = returns.std(ddof=1)
    # Z-score for 95% = 1.64485
    z = 1.644853 if abs(confidence_level - 0.95) < 0.01 else 2.326348
    var_param = float(-(mu - z * sigma))

    return {
        "var_historical": max(var_hist, 0.0),
        "cvar_historical": max(cvar_hist, 0.0),
        "var_parametric": max(var_param, 0.0)
    }

def calculate_marginal_risk_contributions(
    weights: np.ndarray,
    cov_matrix: pd.DataFrame
) -> Dict[str, Dict[str, float]]:
    """
    Computes Marginal Contribution to Risk (MCR) and Percent Contribution to Risk (PCR)
    for each portfolio asset:
    MCR_i = (Sigma @ w)_i / sigma_p
    PCR_i = w_i * MCR_i / sigma_p  (sum of PCR_i = 1.0)
    """
    w = np.array(weights).reshape(-1, 1)
    sigma_mat = cov_matrix.values
    port_var = float((w.T @ sigma_mat @ w).item())
    port_vol = np.sqrt(max(port_var, 1e-12))

    # MCR: (Sigma @ w) / port_vol
    mcr = (sigma_mat @ w) / port_vol
    # Absolute risk contribution: w_i * MCR_i
    rc = w * mcr
    # Percent contribution
    pcr = rc / port_vol

    tickers = list(cov_matrix.columns)
    results = {}
    for i, t in enumerate(tickers):
        results[t] = {
            "weight": float(w[i, 0]),
            "marginal_contribution": float(mcr[i, 0]),
            "risk_contribution": float(rc[i, 0]),
            "percent_risk_contribution": float(pcr[i, 0])
        }

    return results

def calculate_effective_number_of_constituents(weights: np.ndarray) -> float:
    """Effective Number of Constituents (Herfindahl-Hirschman inverse): ENC = 1 / sum(w_i^2)"""
    w_clean = np.array(weights)[np.array(weights) > 1e-6]
    if len(w_clean) == 0:
        return 0.0
    sum_sq = float(np.sum(w_clean ** 2))
    return float(1.0 / max(sum_sq, 1e-6))

def compute_portfolio_diagnostics(
    weights: np.ndarray,
    returns_df: pd.DataFrame,
    benchmark_returns: Optional[pd.Series] = None,
    risk_free_rate: float = 0.04
) -> Dict[str, Any]:
    """Generates complete auditable portfolio risk and performance diagnostics."""
    port_ret = calculate_portfolio_returns(weights, returns_df)
    cov = returns_df.cov() * 252.0

    cagr = calculate_cagr(port_ret)
    vol = calculate_annualized_volatility(port_ret)
    sharpe = calculate_sharpe_ratio(port_ret, risk_free_rate)
    sortino = calculate_sortino_ratio(port_ret, risk_free_rate)
    mdd = calculate_max_drawdown(port_ret)
    tail = calculate_var_cvar(port_ret, 0.95)
    enc = calculate_effective_number_of_constituents(weights)
    mcr = calculate_marginal_risk_contributions(weights, cov)

    beta = 1.0
    alpha = 0.0
    tracking_error = 0.0

    if benchmark_returns is not None:
        aligned = pd.concat([port_ret, benchmark_returns], axis=1, join="inner").dropna()
        if len(aligned) > 10:
            p_r = aligned.iloc[:, 0]
            b_r = aligned.iloc[:, 1]
            b_cov = np.cov(p_r, b_r)[0, 1]
            b_var = np.var(b_r)
            beta = float(b_cov / max(b_var, 1e-8))
            alpha = float(cagr - (risk_free_rate + beta * (calculate_cagr(b_r) - risk_free_rate)))
            tracking_error = float((p_r - b_r).std(ddof=1) * np.sqrt(252.0))

    return {
        "cagr": cagr,
        "annualized_volatility": vol,
        "sharpe_ratio": sharpe,
        "sortino_ratio": sortino,
        "max_drawdown": mdd,
        "var_95_daily": tail["var_historical"],
        "cvar_95_daily": tail["cvar_historical"],
        "beta": beta,
        "alpha": alpha,
        "tracking_error": tracking_error,
        "effective_constituents": enc,
        "marginal_risk": mcr
    }
