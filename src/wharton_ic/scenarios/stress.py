"""Scenario stress testing, factor shocks, and fat-tailed Monte Carlo simulations."""

from typing import Dict, List, Optional, Tuple, Any
import numpy as np
import pandas as pd
from scipy import stats
from wharton_ic.risk.metrics import (
    calculate_portfolio_returns,
    calculate_max_drawdown,
    calculate_var_cvar,
)

class ScenarioStressEngine:
    """
    Executes historical replay stress tests, factor/macro shocks, and fat-tailed
    Student-t Monte Carlo simulations to evaluate client goal attainment and downside risk.
    """

    def __init__(
        self,
        weights: np.ndarray,
        returns_df: pd.DataFrame,
        sector_map: Optional[Dict[str, str]] = None,
        starting_capital: float = 100000.0
    ):
        self.weights = np.array(weights).flatten()
        self.returns_df = returns_df.copy()
        self.tickers = list(returns_df.columns)
        self.sector_map = sector_map or {t: "Unclassified" for t in self.tickers}
        self.starting_capital = starting_capital
        self.port_daily_returns = calculate_portfolio_returns(self.weights, self.returns_df)

    def run_historical_replay(self) -> Dict[str, Dict[str, float]]:
        """
        Evaluates portfolio resilience across historical market stress regimes.
        Matches available history or scales asset volatilities to match crisis severity.
        """
        results = {}

        # 1. GFC 2008 Style Shock (Market -45%, High Correlation, Vol x2.5)
        gfc_sim_ret = self.port_daily_returns.mean() - (2.2 * self.port_daily_returns.std() * np.sqrt(126))
        results["gfc_2008"] = {
            "name": "2008 Global Financial Crisis Replay",
            "simulated_drawdown": float(min(gfc_sim_ret, -0.38)),
            "estimated_capital_trough": float(self.starting_capital * (1.0 + min(gfc_sim_ret, -0.38))),
            "recovery_months_estimate": 24
        }

        # 2. Covid 2020 Liquidity Shock (Rapid 30-day liquidation)
        covid_sim = -1.8 * self.port_daily_returns.std() * np.sqrt(25)
        results["covid_2020"] = {
            "name": "2020 Covid Liquidity Shock Replay",
            "simulated_drawdown": float(min(covid_sim, -0.22)),
            "estimated_capital_trough": float(self.starting_capital * (1.0 + min(covid_sim, -0.22))),
            "recovery_months_estimate": 6
        }

        # 3. 2022 Inflation & Rate Hike Shock
        rate_sim = -1.2 * self.port_daily_returns.std() * np.sqrt(180)
        results["inflation_2022"] = {
            "name": "2022 Stagflation / Fed Rate Hikes Replay",
            "simulated_drawdown": float(min(rate_sim, -0.16)),
            "estimated_capital_trough": float(self.starting_capital * (1.0 + min(rate_sim, -0.16))),
            "recovery_months_estimate": 14
        }

        return results

    def run_synthetic_shocks(self) -> Dict[str, Dict[str, float]]:
        """Simulates targeted macro and sector shocks."""
        results = {}

        # Shock 1: +200 bps Parallel Yield Curve Shift
        # Tech / Growth multiples drop -15%, Defensives -5%
        shock_rates = np.zeros(len(self.tickers))
        for i, t in enumerate(self.tickers):
            sec = self.sector_map.get(t, "Unclassified")
            if sec in ["Information Technology", "Communication Services", "Consumer Discretionary"]:
                shock_rates[i] = -0.15
            elif sec in ["Utilities", "Consumer Staples", "Health Care"]:
                shock_rates[i] = -0.05
            else:
                shock_rates[i] = -0.09
        port_impact_rates = float(np.dot(self.weights, shock_rates))
        results["rate_shock_200bps"] = {
            "name": "+200 bps Interest Rate Shift",
            "portfolio_impact_pct": port_impact_rates,
            "capital_impact_usd": float(self.starting_capital * port_impact_rates)
        }

        # Shock 2: Tech Valuation Reset (-25% Tech multiples)
        shock_tech = np.zeros(len(self.tickers))
        for i, t in enumerate(self.tickers):
            sec = self.sector_map.get(t, "Unclassified")
            if sec == "Information Technology":
                shock_tech[i] = -0.25
            elif sec == "Communication Services":
                shock_tech[i] = -0.18
            else:
                shock_tech[i] = -0.02
        port_impact_tech = float(np.dot(self.weights, shock_tech))
        results["tech_valuation_reset"] = {
            "name": "Tech Multiple Compression (-25%)",
            "portfolio_impact_pct": port_impact_tech,
            "capital_impact_usd": float(self.starting_capital * port_impact_tech)
        }

        return results

    def run_fat_tailed_monte_carlo(
        self,
        num_simulations: int = 5000,
        horizon_days: int = 252,
        degrees_of_freedom: int = 5,
        target_return_pct: float = 0.09,
        seed: int = 42
    ) -> Dict[str, Any]:
        """
        Executes fat-tailed Student-t Monte Carlo simulation.
        Evaluates range of forward outcomes, goal attainment probability,
        and downside drawdown probabilities.
        """
        rng = np.random.default_rng(seed)
        mu = float(self.port_daily_returns.mean())
        sigma = float(self.port_daily_returns.std(ddof=1))

        # Standard Student-t has variance = df / (df - 2)
        scale = sigma * np.sqrt((degrees_of_freedom - 2.0) / degrees_of_freedom)
        
        # Simulate matrix of daily returns: (horizon_days, num_simulations)
        t_dist_random = stats.t.rvs(
            df=degrees_of_freedom,
            loc=mu,
            scale=scale,
            size=(horizon_days, num_simulations),
            random_state=seed
        )

        price_paths = np.vstack([
            np.ones(num_simulations) * self.starting_capital,
            self.starting_capital * np.cumprod(1.0 + t_dist_random, axis=0)
        ])

        ending_wealth = price_paths[-1, :]
        total_returns = (ending_wealth - self.starting_capital) / self.starting_capital

        # Calculate drawdowns for each simulated trajectory
        running_max = np.maximum.accumulate(price_paths, axis=0)
        path_drawdowns = (price_paths - running_max) / running_max
        max_drawdowns = np.min(path_drawdowns, axis=0)

        # Probabilities
        prob_goal_attained = float(np.mean(total_returns >= target_return_pct))
        prob_drawdown_gt_20pct = float(np.mean(max_drawdowns <= -0.20))
        prob_negative_year = float(np.mean(total_returns < 0.0))

        # Percentile outcome cones
        p5 = float(np.percentile(ending_wealth, 5))
        p25 = float(np.percentile(ending_wealth, 25))
        p50 = float(np.percentile(ending_wealth, 50))
        p75 = float(np.percentile(ending_wealth, 75))
        p95 = float(np.percentile(ending_wealth, 95))

        return {
            "num_simulations": num_simulations,
            "horizon_days": horizon_days,
            "target_annual_return": target_return_pct,
            "probability_goal_attained": prob_goal_attained,
            "probability_drawdown_gt_20pct": prob_drawdown_gt_20pct,
            "probability_loss": prob_negative_year,
            "expected_ending_wealth": float(np.mean(ending_wealth)),
            "percentiles_ending_wealth": {
                "p05_bearish": p5,
                "p25_conservative": p25,
                "p50_median": p50,
                "p75_optimistic": p75,
                "p95_bullish": p95
            },
            "percentiles_total_return": {
                "p05": float(np.percentile(total_returns, 5)),
                "p50": float(np.percentile(total_returns, 50)),
                "p95": float(np.percentile(total_returns, 95))
            },
            "sample_path_dates": list(range(horizon_days + 1)),
            "median_path": list(np.percentile(price_paths, 50, axis=1)),
            "p05_path": list(np.percentile(price_paths, 5, axis=1)),
            "p95_path": list(np.percentile(price_paths, 95, axis=1))
        }
