"""Test 2: Deterministic Repeatability & Bitwise Reproducibility."""

import numpy as np
import pandas as pd
from wharton_ic.valuation.wacc import calculate_wacc
from wharton_ic.valuation.dcf import run_dcf_valuation
from wharton_ic.factors.engine import FactorScreeningEngine
from wharton_ic.portfolio.optimizer import PortfolioOptimizer

def test_wacc_and_dcf_deterministic_reproducibility():
    """TEST 2A: Valuation calculations produce identical floating-point numbers across runs."""
    wacc1 = calculate_wacc(0.04, 1.1, 0.055, 0.05, 0.21, 1e11, 2e10)
    wacc2 = calculate_wacc(0.04, 1.1, 0.055, 0.05, 0.21, 1e11, 2e10)
    assert wacc1.wacc == wacc2.wacc
    assert wacc1.cost_of_equity == wacc2.cost_of_equity

    dcf1 = run_dcf_valuation("MSFT", 150.0, 1e9, 5e10, [0.08]*5, [0.25]*5, wacc1)
    dcf2 = run_dcf_valuation("MSFT", 150.0, 1e9, 5e10, [0.08]*5, [0.25]*5, wacc2)
    assert dcf1.implied_share_price == dcf2.implied_share_price
    assert dcf1.sum_pv_fcf == dcf2.sum_pv_fcf
    assert dcf1.sensitivity_matrix == dcf2.sensitivity_matrix

def test_factor_screening_deterministic_reproducibility():
    """TEST 2B: Cross-sectional factor ranking produces identical ranks for identical inputs."""
    data = pd.DataFrame({
        "ticker": ["A", "B", "C", "D"],
        "sector": ["Tech", "Tech", "Health", "Health"],
        "quality": [0.8, 0.4, 0.9, 0.2],
        "value": [0.3, 0.7, 0.5, 0.6],
        "growth": [0.1, 0.2, 0.05, 0.3],
        "momentum": [0.15, -0.05, 0.20, 0.0],
        "low_volatility": [-0.15, -0.30, -0.12, -0.25]
    })
    engine1 = FactorScreeningEngine(data)
    res1 = engine1.process_and_rank("wharton_garp")

    engine2 = FactorScreeningEngine(data)
    res2 = engine2.process_and_rank("wharton_garp")

    pd.testing.assert_series_equal(res1["composite_score"], res2["composite_score"])
    pd.testing.assert_series_equal(res1["final_rank"], res2["final_rank"])
