#!/bin/zsh
# Reproduce the WS2 blind rebuild (M3 -> M4 -> M8). Seed 20260930; pinned env /Users/ray/Research/rab-ws/.venv.
# pytensor's C compiler fails on this Mac (Apple clang 21, "ld: library 'd64' not found"); blind_common.py sets
# PYTENSOR_FLAGS=cxx= so pymc runs its pure-Python ops. Total wall time here: about 6 minutes on 10 cores.
set -e
cd "$(dirname "$0")"
PY=/Users/ray/Research/rab-ws/.venv/bin/python
mkdir -p out
$PY blind_common.py | tee out/common_check.log      # Gate A numbers from the raw curve; t-scale constant
$PY blind_m3.py     2>&1 | tee out/M3_run.log
$PY blind_m4.py     2>&1 | tee out/M4_run.log
$PY blind_m8.py     2>&1 | tee out/M8_run.log
$PY collect_headlines.py 2>&1 | tee out/collect.log        # headline keys for WS0's Gate B comparison
