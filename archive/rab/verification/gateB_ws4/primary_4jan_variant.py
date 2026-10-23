#!/usr/bin/env python
"""Gate B helper (WS4, M2): run the PRIMARY build with the purchase on Mon 4 Jan 2027 instead of Fri 1 Jan 2027.

WS4 Gate B reconciler, 2026-09-30 (Sydney). AI-generated verification code (Claude Code) for Team Caplet; MODEL outputs.

Why: the blind build reports a five-estimator 4 Jan sensitivity (P_median_4jan_purchase), but the primary build only
computes E1 on 4 Jan. To reconcile that key, this script runs the primary's own code with A = 2027-01-04.
- rab/models/m2_rate_paths.py is read and patched IN MEMORY only. The file on disk is never changed.
- Patches: (1) purchase date A = 2027-01-04; (2) the two numbers.yaml anchor asserts (`if D == date(2026, 9, 28):`)
  are switched off, because they hold only for the 1 Jan purchase; (3) optionally, --n-h forces the business-day count
  (the spec's 4 Jan sensitivity says n_h = 65; a strict count gives 64 because 1 Jan 2027 is a bond-market holiday).
- Output goes only to OUT_DIR (never rab/results/M2).
Usage (from the worktree root):
    /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/gateB_ws4/primary_4jan_variant.py OUT_DIR [--n-h 65]
"""
from __future__ import annotations

import argparse
import os
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "rab/models/m2_rate_paths.py"

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("--n-h", type=int, default=None)
a = ap.parse_args()
out = os.path.abspath(a.out)
assert not out.startswith(str(ROOT / "rab/results")), "never write into rab/results"

src = SRC.read_text()
pat_a = "A, B = A27, B28"
pat_anchor = "if D == date(2026, 9, 28):"
pat_nh = "n_h = int(np.busday_count((D + timedelta(days=1)).isoformat(), A.isoformat(), holidays=HOLIDAYS))"
assert src.count(pat_a) == 1 and src.count(pat_anchor) == 2 and src.count(pat_nh) == 1
src = src.replace(pat_a, "A, B = date(2027, 1, 4), B28").replace(pat_anchor, "if False:")
if a.n_h is not None:
    src = src.replace(pat_nh, f"n_h = {int(a.n_h)}")

mod = types.ModuleType("m2_primary_4jan")
mod.__file__ = str(SRC)
mod.__dict__["__name__"] = "m2_primary_4jan"
sys.argv = ["m2_primary_4jan", "--no-figs", "--out", out]
exec(compile(src, str(SRC), "exec"), mod.__dict__)
mod.main()
