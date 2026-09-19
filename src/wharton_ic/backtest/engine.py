"""Rigorous point-in-time walk-forward backtesting engine."""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
import pandas as pd
from wharton_ic.risk.metrics import (
    calculate_cagr,
    calculate_annualized_volatility,
    calculate_sharpe_ratio,
    calculate_sortino_ratio,
    calculate_max_drawdown,
    calculate_var_cvar,
)
from wharton_ic.portfolio.optimizer import PortfolioOptimizer
from wharton_ic.core.exceptions import PointInTimeViolationError
from wharton_ic.core.logging import logger

class WalkForwardBacktester:
    """
    Executes an out-of-sample rolling walk-forward backtest.
    At each rebalancing date T, the model fits exclusively on returns[T - lookback : T].
    Applies realistic transaction costs and slippage on turnover.
    """

    def __init__(
        self,
        prices_df: pd.DataFrame,
        benchmark_prices: Optional[pd.Series] = None,
        sector_map: Optional[Dict[str, str]] = None,
        lookback_days: int = 252,        # 1 year rolling estimation window
        rebalance_freq_days: int = 63,   # Quarterly rebalance (63 business days)
        transaction_cost_bps: float = 5.0, # 5 bps transaction cost/slippage
        cash_buffer: float = 0.020,
        risk_free_rate: float = 0.04
    ):
        self.prices_df = prices_df.copy().dropna()
        self.returns_df = self.prices_df.pct_change().dropna()
        self.benchmark_prices = benchmark_prices
        self.benchmark_returns = (
            benchmark_prices.pct_change().dropna() if benchmark_prices is not None else None
        )
        self.sector_map = sector_map or {}
        self.lookback_days = lookback_days
        self.rebalance_freq_days = rebalance_freq_days
        self.transaction_cost = transaction_cost_bps / 10000.0
        self.cash_buffer = cash_buffer
        self.risk_free_rate = risk_free_rate

    def run_backtest(
        self,
        strategy_method: str = "hrp",
        min_weight: float = 0.025,
        max_weight: float = 0.150,
        max_sector_weight: float = 0.250
    ) -> Dict[str, Any]:
        """Runs the walk-forward simulation across time."""
        dates = self.returns_df.index
        n_days = len(dates)
        if n_days <= self.lookback_days + 10:
            raise ValueError(f"Insufficient history ({n_days} days) for {self.lookback_days}-day lookback window.")

        tickers = list(self.returns_df.columns)
        n_assets = len(tickers)

        # Storage
        portfolio_returns: List[float] = []
        portfolio_dates: List[pd.Timestamp] = []
        weight_history: List[Dict[str, float]] = []
        turnover_history: List[float] = []

        current_weights = np.zeros(n_assets)
        days_since_rebalance = self.rebalance_freq_days  # Force rebalance on day 1

        for t_idx in range(self.lookback_days, n_days):
            current_date = dates[t_idx]
            
            # Rebalance trigger
            if days_since_rebalance >= self.rebalance_freq_days:
                # STRICT LOOK-AHEAD CHECK: Window is strictly [t_idx - lookback : t_idx]
                estimation_returns = self.returns_df.iloc[t_idx - self.lookback_days : t_idx]
                
                optimizer = PortfolioOptimizer(
                    returns_df=estimation_returns,
                    sector_map=self.sector_map,
                    min_weight=min_weight,
                    max_weight=max_weight,
                    max_sector_weight=max_sector_weight,
                    cash_buffer=self.cash_buffer
                )
                new_weights = optimizer.optimize_method(strategy_method)
                
                # Compute turnover & friction: delta = sum(|w_new - w_old|)
                turnover = float(np.sum(np.abs(new_weights - current_weights)))
                fee_impact = turnover * self.transaction_cost
                turnover_history.append(turnover)
                current_weights = new_weights
                days_since_rebalance = 0
            else:
                fee_impact = 0.0
                days_since_rebalance += 1

            # Day return: sum(w_i * r_i) - fee_impact
            day_asset_returns = self.returns_df.iloc[t_idx].values
            gross_return = float(np.dot(current_weights, day_asset_returns))
            net_return = gross_return - fee_impact

            portfolio_returns.append(net_return)
            portfolio_dates.append(current_date)
            weight_history.append({tickers[i]: float(current_weights[i]) for i in range(n_assets)})

        port_ret_series = pd.Series(portfolio_returns, index=pd.DatetimeIndex(portfolio_dates))
        equity_curve = (1.0 + port_ret_series).cumprod()

        # Benchmark calculations
        aligned_benchmark = None
        if self.benchmark_returns is not None:
            aligned_benchmark = self.benchmark_returns.reindex(port_ret_series.index).fillna(0.0)

        cagr = calculate_cagr(port_ret_series)
        vol = calculate_annualized_volatility(port_ret_series)
        sharpe = calculate_sharpe_ratio(port_ret_series, self.risk_free_rate)
        sortino = calculate_sortino_ratio(port_ret_series, self.risk_free_rate)
        max_dd = calculate_max_drawdown(port_ret_series)
        tail = calculate_var_cvar(port_ret_series, 0.95)

        beta, alpha = 1.0, 0.0
        if aligned_benchmark is not None and len(aligned_benchmark) > 20:
            cov = np.cov(port_ret_series, aligned_benchmark)[0, 1]
            b_var = np.var(aligned_benchmark)
            beta = float(cov / max(b_var, 1e-8))
            bench_cagr = calculate_cagr(aligned_benchmark)
            alpha = float(cagr - (self.risk_free_rate + beta * (bench_cagr - self.risk_free_rate)))

        # Hit rate: % of positive monthly returns
        monthly_ret = port_ret_series.resample("ME").apply(lambda r: (1.0 + r).prod() - 1.0)
        hit_rate = float((monthly_ret > 0).mean()) if len(monthly_ret) > 0 else 0.5

        return {
            "strategy": strategy_method,
            "equity_curve": equity_curve,
            "daily_returns": port_ret_series,
            "cagr": cagr,
            "volatility": vol,
            "sharpe_ratio": sharpe,
            "sortino_ratio": sortino,
            "max_drawdown": max_dd,
            "cvar_95": tail["cvar_historical"],
            "beta": beta,
            "alpha": alpha,
            "average_turnover": float(np.mean(turnover_history)) if turnover_history else 0.0,
            "monthly_hit_rate": hit_rate,
            "weight_history": pd.DataFrame(weight_history, index=port_ret_series.index)
        }

    def compare_strategies_walk_forward(self) -> pd.DataFrame:
        """Benchmarks the chosen strategy against Equal Weight and Benchmark ETF."""
        results = []
        for method in ["hrp", "equal_weight", "min_volatility", "max_sharpe"]:
            try:
                res = self.run_backtest(strategy_method=method)
                results.append({
                    "Strategy": method.upper(),
                    "CAGR": res["cagr"],
                    "Volatility": res["volatility"],
                    "Sharpe": res["sharpe_ratio"],
                    "Sortino": res["sortino_ratio"],
                    "Max Drawdown": res["max_drawdown"],
                    "CVaR 95%": res["cvar_95"],
                    "Beta": res["beta"],
                    "Turnover": res["average_turnover"],
                    "Hit Rate": res["monthly_hit_rate"]
                })
            except Exception as e:
                logger.warning(f"Backtest for {method} failed: {e}")

        # Add Benchmark if present
        if self.benchmark_returns is not None:
            aligned = self.benchmark_returns.iloc[self.lookback_days:]
            if len(aligned) > 10:
                results.append({
                    "Strategy": "BENCHMARK (SPY)",
                    "CAGR": calculate_cagr(aligned),
                    "Volatility": calculate_annualized_volatility(aligned),
                    "Sharpe": calculate_sharpe_ratio(aligned, self.risk_free_rate),
                    "Sortino": calculate_sortino_ratio(aligned, self.risk_free_rate),
                    "Max Drawdown": calculate_max_drawdown(aligned),
                    "CVaR 95%": calculate_var_cvar(aligned, 0.95)["cvar_historical"],
                    "Beta": 1.0,
                    "Turnover": 0.0,
                    "Hit Rate": float((aligned.resample("ME").apply(lambda r: (1.0 + r).prod() - 1.0) > 0).mean())
                })

        return pd.DataFrame(results).sort_values("Sharpe", ascending=False)
