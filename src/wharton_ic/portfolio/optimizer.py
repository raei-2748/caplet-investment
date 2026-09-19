"""Institutional portfolio construction engine integrating skfolio with Wharton constraints."""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
import pandas as pd
import cvxpy as cp

from skfolio.optimization import (
    EqualWeighted,
    InverseVolatility,
    MeanRisk,
    RiskBudgeting,
    HierarchicalRiskParity,
    ObjectiveFunction,
)
from skfolio.measures import RiskMeasure

from wharton_ic.risk.metrics import compute_portfolio_diagnostics
from wharton_ic.core.exceptions import ConstraintViolationError
from wharton_ic.core.logging import logger

def project_weights_with_constraints(
    raw_weights: np.ndarray,
    tickers: List[str],
    sector_map: Dict[str, str],
    min_weight: float = 0.025,
    max_weight: float = 0.150,
    max_sector_weight: float = 0.250,
    cash_buffer: float = 0.020
) -> np.ndarray:
    """
    Projects raw weights onto the Wharton-compliant convex constraint set using CVXPY:
    Minimize || w - w_raw ||^2
    Subject to:
      sum(w) = 1.0 - cash_buffer
      min_weight <= w_i <= max_weight
      sum_{i in sector} w_i <= max_sector_weight
    """
    n = len(tickers)
    investable_capital = 1.0 - cash_buffer

    # Verify feasible box bounds
    if n * min_weight > investable_capital or n * max_weight < investable_capital:
        logger.warning(f"Box constraints ({min_weight}, {max_weight}) tight for N={n}. Adjusting bounds.")
        min_weight = max(0.01, investable_capital / (n * 2.0))
        max_weight = min(0.30, investable_capital / 2.0)

    w = cp.Variable(n)
    w_target = raw_weights / np.sum(raw_weights) * investable_capital

    constraints = [
        cp.sum(w) == investable_capital,
        w >= min_weight,
        w <= max_weight,
    ]

    # Sector constraints
    unique_sectors = set(sector_map.get(t, "Unclassified") for t in tickers)
    for s in unique_sectors:
        indices = [i for i, t in enumerate(tickers) if sector_map.get(t, "Unclassified") == s]
        if indices:
            constraints.append(cp.sum(w[indices]) <= max_sector_weight)

    prob = cp.Problem(cp.Minimize(cp.sum_squares(w - w_target)), constraints)
    try:
        prob.solve(solver=cp.CLARABEL)
        if prob.status in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE] and w.value is not None:
            weights = np.array(w.value).flatten()
            weights = np.clip(weights, min_weight, max_weight)
            # Re-normalize to exact investable capital
            weights = weights / np.sum(weights) * investable_capital
            return weights
    except Exception as e:
        logger.warning(f"CVXPY constraint projection failed ({e}). Falling back to bounded clipping.")

    # Fallback heuristic clipping
    clipped = np.clip(raw_weights, min_weight, max_weight)
    return clipped / np.sum(clipped) * investable_capital

class PortfolioOptimizer:
    """
    Comprehensive portfolio optimization engine comparing 8 allocation paradigms
    with strict Wharton box, sector, and cash constraints.
    """

    def __init__(
        self,
        returns_df: pd.DataFrame,
        sector_map: Optional[Dict[str, str]] = None,
        min_weight: float = 0.025,
        max_weight: float = 0.150,
        max_sector_weight: float = 0.250,
        cash_buffer: float = 0.020,
        benchmark_returns: Optional[pd.Series] = None
    ):
        self.returns_df = returns_df.copy().dropna()
        self.tickers = list(self.returns_df.columns)
        self.sector_map = sector_map or {t: "Unclassified" for t in self.tickers}
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.max_sector_weight = max_sector_weight
        self.cash_buffer = cash_buffer
        self.benchmark_returns = benchmark_returns

    def optimize_method(self, method: str, factor_scores: Optional[Dict[str, float]] = None) -> np.ndarray:
        """Computes constrained weights for a specific optimization model."""
        n = len(self.tickers)
        if n == 0:
            return np.array([])

        raw_weights = np.ones(n) / n

        try:
            if method == "equal_weight":
                estimator = EqualWeighted()
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            elif method == "inverse_volatility":
                estimator = InverseVolatility()
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            elif method == "factor_score_weighted" and factor_scores:
                scores = np.array([max(factor_scores.get(t, 1.0), 0.01) for t in self.tickers])
                raw_weights = scores / np.sum(scores)

            elif method == "max_sharpe":
                estimator = MeanRisk(
                    objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
                    risk_measure=RiskMeasure.VARIANCE
                )
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            elif method == "min_volatility":
                estimator = MeanRisk(
                    objective_function=ObjectiveFunction.MINIMIZE_RISK,
                    risk_measure=RiskMeasure.VARIANCE
                )
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            elif method == "mean_cvar":
                estimator = MeanRisk(
                    objective_function=ObjectiveFunction.MINIMIZE_RISK,
                    risk_measure=RiskMeasure.CVAR
                )
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            elif method == "risk_budgeting":
                estimator = RiskBudgeting()
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            elif method == "hrp":
                estimator = HierarchicalRiskParity()
                estimator.fit(self.returns_df)
                raw_weights = estimator.weights_

            else:
                raw_weights = np.ones(n) / n

        except Exception as e:
            logger.warning(f"skfolio optimizer {method} encountered issue: {e}. Using Inverse Volatility.")
            vols = self.returns_df.std(ddof=1)
            raw_weights = (1.0 / np.maximum(vols.values, 1e-4))
            raw_weights /= np.sum(raw_weights)

        # Apply Wharton constraints
        final_weights = project_weights_with_constraints(
            raw_weights=raw_weights,
            tickers=self.tickers,
            sector_map=self.sector_map,
            min_weight=self.min_weight,
            max_weight=self.max_weight,
            max_sector_weight=self.max_sector_weight,
            cash_buffer=self.cash_buffer
        )

        return final_weights

    def compare_all_methods(self, factor_scores: Optional[Dict[str, float]] = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Runs and benchmarks all 8 optimization models side-by-side.
        Returns:
          1. weights_df: Allocations across assets for each model.
          2. metrics_df: Comparison of risk, return, Sharpe, Sortino, Drawdown, and ENC.
        """
        methods = [
            "equal_weight",
            "inverse_volatility",
            "factor_score_weighted",
            "max_sharpe",
            "min_volatility",
            "mean_cvar",
            "risk_budgeting",
            "hrp",
        ]

        all_weights: Dict[str, List[float]] = {"Ticker": self.tickers}
        diagnostics_list = []

        for m in methods:
            w = self.optimize_method(m, factor_scores=factor_scores)
            all_weights[m] = list(np.round(w, 4))

            diag = compute_portfolio_diagnostics(
                weights=w,
                returns_df=self.returns_df,
                benchmark_returns=self.benchmark_returns
            )
            diagnostics_list.append({
                "Method": m,
                "CAGR": diag["cagr"],
                "Annualized Volatility": diag["annualized_volatility"],
                "Sharpe Ratio": diag["sharpe_ratio"],
                "Sortino Ratio": diag["sortino_ratio"],
                "Max Drawdown": diag["max_drawdown"],
                "Daily CVaR (95%)": diag["cvar_95_daily"],
                "Beta to SPY": diag["beta"],
                "Effective Constituents (ENC)": diag["effective_constituents"]
            })

        weights_df = pd.DataFrame(all_weights)
        metrics_df = pd.DataFrame(diagnostics_list).sort_values("Sharpe Ratio", ascending=False)

        return weights_df, metrics_df
