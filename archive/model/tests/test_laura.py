"""Tests for the Laura Gao model.  Run: python -m pytest model/tests -q"""
import numpy as np
import pytest

from model.laura.engine import (Market, all_historical_windows, default_strategies, facility, liability_pv,
                                load_config, run, simulate_market, sleeve_growth_quantiles)

CFG = load_config()
STRATS = default_strategies(CFG)


def flat_market(y=0.05, eq=0.0, bond=0.0, cash=0.0, y_path=None):
    ys = np.array([y_path if y_path is not None else [y] * 7], dtype=float)
    return Market(ys, np.full((1, 6), eq), np.full((1, 6), bond), np.full((1, 6), cash), "flat")


# ---- liability valuation -------------------------------------------------------------------
def test_pv_matches_hand_annuity_due():
    y = 0.04
    hand = 50000 * (1 - (1 + y) ** -10) / y * (1 + y)   # annuity-due: first payment at start of 2033
    assert liability_pv(y, 2033, CFG) == pytest.approx(hand, rel=1e-12)


def test_pv_zero_rate_is_500k():
    assert liability_pv(0.0, 2033, CFG) == pytest.approx(500000)


def test_pv_from_2027_discounts_6_to_15_years():
    y = 0.05
    hand = sum(50000 / (1 + y) ** k for k in range(6, 16))
    assert liability_pv(y, 2027, CFG) == pytest.approx(hand)


def test_payment_due_this_year_is_not_discounted():
    assert liability_pv(0.07, 2042, CFG) == pytest.approx(50000)


# ---- cash-flow timing ------------------------------------------------------------------------
def test_contributions_at_start_of_2027_and_2028_only():
    # zero returns, flat yields, no hedging: assets in 2033 must equal 300k + 150k exactly
    r = run(flat_market(0.05), STRATS["C60"], CFG)
    assert r.V[0, 0] == pytest.approx(300000)
    assert r.V[0, 1] == pytest.approx(450000)
    assert r.V[0, 6] == pytest.approx(450000)


# ---- the hedge works -------------------------------------------------------------------------
@pytest.mark.parametrize("y_end", [0.005, 0.02, 0.08, 0.12])
def test_lock_early_is_immune_to_rates_and_equity_crash(y_end):
    path = np.linspace(CFG["rates"]["y0"], y_end, 7)
    m = flat_market(y_path=path, eq=-0.5, bond=-0.2)
    r = run(m, STRATS["A"], CFG)
    assert r.funded[0], "strategy A must fund the reserve regardless of markets once locked"


def test_build_late_can_fail_when_crash_and_falling_rates_coincide():
    path = np.linspace(CFG["rates"]["y0"], 0.01, 7)
    r = run(flat_market(y_path=path, eq=-0.3, bond=0.0), STRATS["C80"], CFG)
    assert not r.funded[0]


# ---- reproducibility -------------------------------------------------------------------------
def test_same_seed_same_numbers():
    a = run(simulate_market(CFG, "base", 0.0, n=2000), STRATS["B"], CFG).surplus
    b = run(simulate_market(CFG, "base", 0.0, n=2000), STRATS["B"], CFG).surplus
    assert np.array_equal(a, b)


# ---- history ---------------------------------------------------------------------------------
def test_historical_windows_cover_1928_2020_starts():
    wins = all_historical_windows(CFG)
    assert len(wins) == 93
    gfc_last = next(w for w in wins if w.label.startswith("history 2003"))
    assert gfc_last.equity[0, -1] == pytest.approx(-0.365523, abs=1e-6)   # 2008 S&P 500 total return


# ---- 2031 announce-then-protect ----------------------------------------------------------------
def test_committed_minimum_is_never_breached():
    m = simulate_market(CFG, "bear", -0.2, n=5000)
    gq = sleeve_growth_quantiles(CFG, 0.8, [0.1, 0.9], n=5000)
    a = run(m, STRATS["A"], CFG, announce=True, lock_fraction=0.7, g_quantiles=gq).announce
    ok = a["surplus_2031"] > 0
    assert np.all(a["facility"][ok] >= a["committed_min"][ok] - 1e-6)


def test_facility_respects_buffer_and_never_negative():
    s = np.array([-10.0, 0.0, 100.0])
    assert np.allclose(facility(s, CFG, 0.2), [0, 0, 80])
