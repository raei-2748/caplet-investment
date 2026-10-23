"""Shared inputs, seeds, the Root-and-Branch rule and chart style for WS2 models M3, M4 and M8.

WS2, RAB Kit, 2026-09-30 (Sydney). AI-generated research (Claude Code) for Team Caplet; no deliverable text.
Specs: rab/models/M3_SPEC.md, M4_SPEC.md, M8_SPEC.md. Every input is read from the Gate A files; nothing is typed in
except the case facts (the $150,000 deposit) and the JPM figures, whose source is cited next to them.
"""
import hashlib
import json
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RESULTS = os.path.join(ROOT, "rab", "results")
SEED = 20260930
N_PATHS = 200_000
LOCK_SHA = "492ed3203958a93ddd3fd7345dcc41e46dd93c9e67f9c2adec1ca63a0771f638"   # rab/numbers.lock (Gate A)

# J.P. Morgan Asset Management 2026 LTCMA, AC World Equity (USD): compound 7.00%, arithmetic 8.28%, volatility 16.78%.
# competition/official_market_data/JPM_LTCMA_2026_US_matrix_USD.pdf p.2, data as of 30 Sep 2025 (main checkout).
JPM_COMPOUND, JPM_ARITH = 0.0700, 0.0828
MU_L = float(np.log1p(JPM_COMPOUND))
SIG_L = float(np.sqrt(2 * np.log((1 + JPM_ARITH) / (1 + JPM_COMPOUND))))
DEP2 = 150_000.0          # case p.2: $150,000 at the beginning of 2028
S_ADOPTED = 0.5           # the adopted D6 default ("half")

# Seed streams, fixed order (M3_SPEC section 1). Each model draws from its own child stream.
STREAMS = ["L", "T", "BOOT", "BOOT-raw", "BOOT-b1", "BOOT-b60", "BAYES-mcmc", "BAYES", "BAYES-hist", "floor",
           "M8-luck", "M8-sobol"]


def rng(name):
    kids = np.random.SeedSequence(SEED).spawn(len(STREAMS))
    return np.random.default_rng(kids[STREAMS.index(name)])


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def inputs():
    """Read the Gate A numbers; refuse to run if numbers.yaml is not the Gate A file."""
    ny = os.path.join(ROOT, "rab", "numbers.yaml")
    h = sha256(ny)
    if h != LOCK_SHA:
        raise SystemExit(f"rab/numbers.yaml hash {h} is not the Gate A lock {LOCK_SHA}")
    N = yaml.safe_load(open(ny))["numbers"]
    m1 = json.load(open(os.path.join(ROOT, "rab", "models", "out", "m1_results.json")))
    b0 = m1["F"]["nov15"]["fund_usd"]
    assert round(b0) == N["laura.stock_fund_2028_usd.strips"]["value"], "B0 does not match numbers.yaml"
    assert round(m1["F"]["nov15"]["floor_cost"]) == N["laura.floor_cost_2028"]["value"]
    par = N["market.par_curve"]["value"]
    return {"B0": b0, "F": DEP2, "floor_cost": m1["F"]["nov15"]["floor_cost"], "y1": par["1 Yr"] / 100,
            "y5": par["5 Yr"] / 100, "leftover_2027": m1["F"]["nov15"]["leftover_2027"],
            "V_A": N["laura.ladder.cost_2027_strips"]["value"], "curve_date": N["market.par_curve"]["curve_date"],
            "numbers_sha": h}


def rule(x, B0, F, s=S_ADOPTED, phi=1.0):
    """Root-and-Branch Branch rule on annual log returns x (paths x 5): M3_SPEC section 2 / M4_SPEC section 3."""
    B3 = B0 * np.exp(x[:, :3].sum(axis=1))
    B5 = B3 * np.exp(x[:, 3:5].sum(axis=1))
    U = F + s * B3
    G = np.minimum(phi * F + s * np.minimum(B5, B3), U)
    K = phi * F + B5 - G
    return {"B3": B3, "B5": B5, "U": U, "G": G, "K": K, "T": phi * F + B5, "pos": np.minimum(B5 / B3, 1.0)}


def stamp():
    t = datetime.now(timezone.utc)
    return (f"{t:%Y-%m-%d %H:%M} UTC | {t.astimezone(ZoneInfo('America/New_York')):%Y-%m-%d %H:%M %Z} | "
            f"{t.astimezone(ZoneInfo('Australia/Sydney')):%Y-%m-%d %H:%M %Z}")


# ------------------------------------------------------------------ charts (dataviz reference palette, light mode)
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
COL = {"T": "#2a78d6", "BOOT": "#eb6834", "BAYES": "#1baf7a", "L": "#8a8984"}      # validated: validate_palette.js
LS = {"T": "-", "BOOT": "--", "BAYES": "-.", "L": ":"}
LABEL = {"T": "Fat tails (Student-t)", "BOOT": "History (Shiller bootstrap)", "BAYES": "Uncertain mean (Bayesian)",
         "L": "Reference (lognormal, insight_v1)"}


def style(plt):
    plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
                         "axes.edgecolor": INK2, "axes.labelcolor": INK, "text.color": INK, "xtick.color": INK2,
                         "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
                         "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                         "axes.titlesize": 11, "axes.titleweight": "bold", "legend.frameon": False,
                         "lines.linewidth": 2, "text.parse_math": False})


def footer(fig, text):
    fig.text(0.01, 0.01, text, fontsize=7.5, color=INK2, ha="left", va="bottom")
