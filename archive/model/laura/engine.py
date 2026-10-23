"""Core engine for the Laura Gao case.

Timeline (case convention): all cash flows at the BEGINNING of a year.
Model index t = 0..6  <->  start of 2027 .. start of 2033.
Market moves happen *during* year t (from start of t to start of t+1).

Assets
------
* Ladder: a fraction ``h`` of every future $50k payment, held as Treasury zero-coupon claims
  maturing on each payment date (a cash-flow-matched ladder). Valued at the flat yield y_t.
* Sleeve: the growth portfolio (equity share ``w``; the rest in an intermediate Treasury index).
* Locked: surplus moved into a 2-year Treasury maturing at the start of 2033 (2031 "announce then protect").

Everything is plain numpy so the model runs on any laptop in seconds.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import numpy as np
import yaml

HERE = Path(__file__).resolve().parent
T_STEPS = 6  # 2027 -> 2033


# --------------------------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------------------------
def load_config(path: Optional[Path] = None) -> dict:
    with open(path or HERE / "assumptions.yaml") as f:
        return yaml.safe_load(f)


def load_history() -> Dict[str, np.ndarray]:
    """Damodaran annual US history 1928-2025 (see CSV header for source)."""
    rows = [
        line.strip().split(",")
        for line in (HERE / "data" / "us_history_1928_2025.csv").read_text().splitlines()
        if line and not line.startswith("#")
    ]
    head, body = rows[0], rows[1:]
    cols = {k: np.array([float(r[i]) for r in body]) for i, k in enumerate(head)}
    cols["year"] = cols["year"].astype(int)
    return cols


# --------------------------------------------------------------------------------------------
# Liability
# --------------------------------------------------------------------------------------------
def liability_pv(y, year: int, cfg: dict) -> np.ndarray:
    """PV at the START of ``year`` of all remaining fixed payments, flat yield ``y``.

    Payments occur at the start of each payment year, so a payment in ``year`` itself is
    undiscounted (annuity-due when year == first payment year).
    """
    y = np.asarray(y, dtype=float)
    pay = cfg["client"]["payment"]
    pv = np.zeros_like(y)
    for T in cfg["client"]["payment_years"]:
        if T >= year:
            pv = pv + pay / (1.0 + y) ** (T - year)
    return pv


# --------------------------------------------------------------------------------------------
# Markets
# --------------------------------------------------------------------------------------------
@dataclass
class Market:
    """Yields at the start of each year (n, 7) and returns during each year (n, 6)."""

    y: np.ndarray
    equity: np.ndarray
    bond: np.ndarray
    cash: np.ndarray
    label: str = ""

    @property
    def n(self) -> int:
        return self.y.shape[0]


def _bond_return(y_start, y_end, cfg):
    r = cfg["rates"]
    dy = y_end - y_start
    return y_start - r["bond_duration"] * dy + 0.5 * r["bond_convexity"] * dy ** 2


def _cash_return(y_start, cfg):
    return np.maximum(y_start - cfg["rates"]["cash_spread"], 0.0)


def simulate_market(cfg: dict, scenario: str = "base", rho: float = 0.0,
                    n: Optional[int] = None, seed: Optional[int] = None,
                    y0: Optional[float] = None) -> Market:
    sim, rt, eq = cfg["simulation"], cfg["rates"], cfg["equity"]
    n = n or sim["n_paths"]
    rng = np.random.default_rng(sim["seed"] if seed is None else seed)
    dof = eq["t_dof"]
    # Student-t shocks rescaled to unit variance, correlated via a shared normal structure.
    z1 = rng.standard_normal((n, T_STEPS))
    z2 = rng.standard_normal((n, T_STEPS))
    chi = rng.chisquare(dof, (n, T_STEPS)) / dof
    scale = np.sqrt((dof - 2) / dof) / np.sqrt(chi)          # common mixing -> joint fat tails
    z_rate = z1 * scale
    z_eq = (rho * z1 + np.sqrt(1 - rho ** 2) * z2) * scale

    y = np.empty((n, T_STEPS + 1))
    y[:, 0] = rt["y0"] if y0 is None else y0
    for t in range(T_STEPS):
        y[:, t + 1] = np.maximum(
            y[:, t] + rt["kappa"] * (rt["long_run"] - y[:, t]) + rt["sigma"] * z_rate[:, t],
            rt["floor"])
    p = eq["scenarios"][scenario]
    equity = p["mu"] + p["sigma"] * z_eq
    equity = np.maximum(equity, -0.95)
    bond = _bond_return(y[:, :-1], y[:, 1:], cfg)
    cash = _cash_return(y[:, :-1], cfg)
    return Market(y, equity, bond, cash, label=f"{scenario}|rho={rho:+.2f}")


def historical_market(cfg: dict, start_year: int, hist=None, y0: Optional[float] = None) -> Market:
    """Replay the actual 6-year sequence starting in ``start_year`` onto today's starting yield.

    Equity = actual S&P 500 total return. Yield *changes* = actual 10Y changes, applied to our y0.
    """
    hist = hist or load_history()
    idx = np.where(hist["year"] == start_year)[0]
    if len(idx) == 0 or idx[0] + T_STEPS > len(hist["year"]):
        raise ValueError(f"no complete 6-year window from {start_year}")
    i = idx[0]
    sl = slice(i, i + T_STEPS)
    dy = hist["tbond10_yield_end"][sl] - hist["tbond10_yield_start"][sl]
    y = np.empty((1, T_STEPS + 1))
    y[0, 0] = cfg["rates"]["y0"] if y0 is None else y0
    for t in range(T_STEPS):
        y[0, t + 1] = max(y[0, t] + dy[t], cfg["rates"]["floor"])
    equity = hist["sp500_tr"][sl][None, :]
    bond = _bond_return(y[:, :-1], y[:, 1:], cfg)
    cash = _cash_return(y[:, :-1], cfg)
    return Market(y, equity, bond, cash, label=f"history {start_year}-{start_year + 5}")


def all_historical_windows(cfg: dict) -> List[Market]:
    hist = load_history()
    years = hist["year"]
    return [historical_market(cfg, int(s), hist) for s in years if s + T_STEPS - 1 <= years[-1]]


# --------------------------------------------------------------------------------------------
# Strategies
# --------------------------------------------------------------------------------------------
@dataclass
class Strategy:
    name: str
    hedge_schedule: Sequence[float]          # target hedge ratio at t = 0..5 (2027..2032)
    sleeve_equity: float                     # equity share of the growth sleeve
    lock_trigger: Optional[float] = None     # funded ratio (assets / liability PV) that triggers 100% hedge
    description: str = ""


def default_strategies(cfg: dict) -> Dict[str, Strategy]:
    w = cfg["policy"]["growth_sleeve_equity"]
    return {
        "A": Strategy("A: Lock early", [1, 1, 1, 1, 1, 1], w,
                      description="Buy the whole Treasury ladder in 2027 (top up with 2028 money if needed)."),
        "B": Strategy("B: Staged hedge", [0.5, 0.6, 0.7, 0.8, 1.0, 1.0], w, lock_trigger=1.25,
                      description="Hedge 50% in 2027 rising to 100% by 2031; lock 100% early once assets reach 125% of the reserve cost."),
        "C60": Strategy("C: Build in 2033 (60/40)", [0] * 6, 0.60,
                        description="Balanced 60/40 portfolio until 2033, then buy the ladder."),
        "C80": Strategy("C: Build in 2033 (80/20)", [0] * 6, 0.80,
                        description="Growth 80/20 portfolio until 2033, then buy the ladder."),
    }


@dataclass
class Result:
    strategy: Strategy
    market: Market
    V: np.ndarray            # total assets at start of t (after contributions, before trades), (n, 7)
    L: np.ndarray            # liability PV at start of t, (n, 7)
    h: np.ndarray            # hedge ratio after trading at t, (n, 7)
    surplus: np.ndarray      # V - L at start of 2033, (n,)
    announce: Optional[dict] = None

    @property
    def funded(self) -> np.ndarray:
        return self.surplus >= -1e-6


def run(market: Market, strat: Strategy, cfg: dict, announce: bool = False,
        lock_fraction: Optional[float] = None, g_quantiles: Optional[np.ndarray] = None) -> Result:
    """Simulate one strategy on one set of market paths.

    If ``announce`` is True the 2031 rule is applied: hedge -> 100%, then ``lock_fraction`` of the
    surplus is moved into a 2-year Treasury maturing at the start of 2033.  ``g_quantiles`` are the
    team's (base-case) quantiles of 2-year sleeve growth used to state the range.
    """
    c = cfg["client"]
    start = c["start_year"]
    contrib = {int(k): float(v) for k, v in c["contributions"].items()}
    n = market.n
    w = strat.sleeve_equity
    p_lock = cfg["policy"]["announce_lock_fraction"] if lock_fraction is None else lock_fraction
    buffer = cfg["policy"]["flexibility_buffer"]

    S = np.zeros(n)            # sleeve
    h = np.zeros(n)            # hedge ratio
    locked = np.zeros(n)       # 2031 locked surplus (value)
    y2_lock = np.zeros(n)
    V = np.zeros((n, T_STEPS + 1)); L = np.zeros((n, T_STEPS + 1)); H = np.zeros((n, T_STEPS + 1))
    ann = None
    t_ann = c["announce_year"] - start

    for t in range(T_STEPS):
        year = start + t
        S = S + contrib.get(year, 0.0)
        Lt = liability_pv(market.y[:, t], year, cfg)
        Vt = h * Lt + S + locked
        V[:, t], L[:, t] = Vt, Lt

        target = np.full(n, float(strat.hedge_schedule[t]))
        if strat.lock_trigger is not None:
            target = np.where(Vt / Lt >= strat.lock_trigger, 1.0, target)
        if announce and t >= t_ann:
            target = np.ones(n)
        target = np.maximum(target, h)                     # never un-hedge
        target = np.minimum(target, h + S / Lt)            # can only buy with sleeve cash
        S = S - (target - h) * Lt
        h = target
        H[:, t] = h

        if announce and t == t_ann:
            s4 = S - (1 - h) * Lt                         # surplus over the reserve cost
            s4 = np.maximum(s4, 0.0)
            lock_amt = np.minimum(p_lock * s4, S)
            S = S - lock_amt
            y2_lock = np.maximum(market.y[:, t] - 0.003, cfg["rates"]["floor"])  # 2Y ~0.3pp below 6-15Y curve
            locked = lock_amt
            floor_2033 = lock_amt * (1 + y2_lock) ** 2
            rest = S - (1 - h) * Lt                       # unhedged liability still owed from sleeve
            gq = g_quantiles if g_quantiles is not None else np.array([1.0, 1.0])
            lo = (1 - buffer) * np.maximum(floor_2033 + rest * gq[0], 0)
            hi = (1 - buffer) * np.maximum(floor_2033 + rest * gq[-1], 0)
            committed = (1 - buffer) * floor_2033
            ann = {"surplus_2031": s4, "locked": lock_amt, "low": lo, "high": hi, "committed_min": committed}

        # market moves during the year
        S = S * (1 + w * market.equity[:, t] + (1 - w) * market.bond[:, t])
        if announce and t >= t_ann:
            locked = locked * (1 + y2_lock)

    L6 = liability_pv(market.y[:, T_STEPS], start + T_STEPS, cfg)
    V6 = h * L6 + S + locked
    V[:, T_STEPS], L[:, T_STEPS], H[:, T_STEPS] = V6, L6, h
    surplus = V6 - L6
    if ann is not None:
        F = facility(surplus, cfg)
        ann["facility"] = F
        ann["in_range"] = (F >= ann["low"] - 1e-6) & (F <= ann["high"] + 1e-6)
        ann["at_or_above_low"] = F >= ann["low"] - 1e-6
        ann["at_or_above_committed"] = F >= ann["committed_min"] - 1e-6
        ann["at_or_below_high"] = F <= ann["high"] + 1e-6
    return Result(strat, market, V, L, H, surplus, ann)


def facility(surplus: np.ndarray, cfg: dict, buffer: Optional[float] = None) -> np.ndarray:
    b = cfg["policy"]["flexibility_buffer"] if buffer is None else buffer
    return (1 - b) * np.maximum(surplus, 0.0)


def sleeve_growth_quantiles(cfg: dict, w: float, qs: Sequence[float], years: int = 2,
                            scenario: str = "base", rho: float = 0.0, n: int = 50000) -> np.ndarray:
    """Quantiles of the sleeve's growth factor over ``years`` under the TEAM's base assumptions."""
    m = simulate_market(cfg, scenario, rho, n=n, seed=cfg["simulation"]["seed"] + 7)
    g = np.prod(1 + w * m.equity[:, :years] + (1 - w) * m.bond[:, :years], axis=1)
    return np.quantile(g, qs)


# --------------------------------------------------------------------------------------------
# Summaries
# --------------------------------------------------------------------------------------------
def summarize(res: Result, cfg: dict, qs=(0.05, 0.10, 0.25, 0.50, 0.75, 0.90)) -> dict:
    s = res.surplus
    F = facility(s, cfg)
    infl = cfg["inflation"]["us_breakeven"]
    short = np.maximum(-s, 0)
    out = {
        "strategy": res.strategy.name,
        "market": res.market.label,
        "n": int(len(s)),
        "p_funded": float(np.mean(res.funded)),
        "p_shortfall": float(np.mean(~res.funded)),
        "avg_shortfall_if_short": float(short[short > 0].mean()) if np.any(short > 0) else 0.0,
        "reserve_cost_2033": {f"p{int(q*100)}": float(np.quantile(res.L[:, -1], q)) for q in qs},
        "surplus_2033": {f"p{int(q*100)}": float(np.quantile(s, q)) for q in qs},
        "facility_2033_nominal": {f"p{int(q*100)}": float(np.quantile(F, q)) for q in qs},
        "facility_2033_in_2027_dollars": {f"p{int(q*100)}": float(np.quantile(F, q) / (1 + infl) ** 6) for q in qs},
        "mean_facility_2033": float(F.mean()),
        "p_hedged_100_by": {str(2027 + t): float(np.mean(res.h[:, t] >= 0.999)) for t in range(T_STEPS)},
    }
    return out
