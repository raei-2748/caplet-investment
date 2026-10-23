"""Test 3 & Test 7: Portfolio constraints enforcement and baseline benchmarking."""

import numpy as np
import pandas as pd
from wharton_ic.portfolio.optimizer import PortfolioOptimizer, project_weights_with_constraints

def test_portfolio_constraints_box_and_sector_caps():
    """TEST 3: Verify all output portfolio weights strictly satisfy min, max, and sector caps."""
    tickers = ["AAPL", "MSFT", "NVDA", "JNJ", "UNH", "JPM", "PG", "COST", "CAT", "NEE"]
    sector_map = {
        "AAPL": "Information Technology",
        "MSFT": "Information Technology",
        "NVDA": "Information Technology",
        "JNJ": "Health Care",
        "UNH": "Health Care",
        "JPM": "Financials",
        "PG": "Consumer Staples",
        "COST": "Consumer Staples",
        "CAT": "Industrials",
        "NEE": "Utilities"
    }

    # Simulate raw unconstrained weights with extreme tech overweight (60% Tech)
    raw_weights = np.array([0.25, 0.20, 0.15, 0.08, 0.08, 0.08, 0.06, 0.05, 0.03, 0.02])
    min_w = 0.025
    max_w = 0.150
    sector_cap = 0.250
    cash_buf = 0.020

    final_weights = project_weights_with_constraints(
        raw_weights=raw_weights,
        tickers=tickers,
        sector_map=sector_map,
        min_weight=min_w,
        max_weight=max_w,
        max_sector_weight=sector_cap,
        cash_buffer=cash_buf
    )

    # Assert sum equals 1 - cash
    assert abs(np.sum(final_weights) - (1.0 - cash_buf)) < 1e-4

    # Assert box bounds for every individual asset
    for i, w in enumerate(final_weights):
        assert w >= min_w - 1e-4, f"Weight {w} below min {min_w} for {tickers[i]}"
        assert w <= max_w + 1e-4, f"Weight {w} exceeds max {max_w} for {tickers[i]}"

    # Assert sector caps
    tech_sum = sum(final_weights[i] for i, t in enumerate(tickers) if sector_map[t] == "Information Technology")
    assert tech_sum <= sector_cap + 1e-4, f"Tech sector weight {tech_sum} exceeded {sector_cap}"

def test_complex_models_benchmarked_against_baselines():
    """TEST 7: Optimizer comparison benchmarks HRP / CVaR against Equal Weight and simple baselines."""
    rng = np.random.default_rng(42)
    dates = pd.date_range("2025-01-01", "2025-12-31", freq="B")
    tickers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    returns_data = rng.normal(0.0005, 0.012, (len(dates), len(tickers)))
    df = pd.DataFrame(returns_data, index=dates, columns=tickers)

    optimizer = PortfolioOptimizer(returns_df=df)
    weights_df, metrics_df = optimizer.compare_all_methods()

    methods_evaluated = set(metrics_df["Method"])
    assert "equal_weight" in methods_evaluated
    assert "inverse_volatility" in methods_evaluated
    assert "hrp" in methods_evaluated
    assert "max_sharpe" in methods_evaluated

    # Equal weight and complex models must both have computed Sharpe and drawdown
    ew_row = metrics_df[metrics_df["Method"] == "equal_weight"].iloc[0]
    hrp_row = metrics_df[metrics_df["Method"] == "hrp"].iloc[0]

    assert pd.notna(ew_row["Sharpe Ratio"])
    assert pd.notna(hrp_row["Sharpe Ratio"])
    assert pd.notna(ew_row["Max Drawdown"])
    assert pd.notna(hrp_row["Max Drawdown"])
