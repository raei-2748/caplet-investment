#!/bin/zsh
# Blind rebuild of M5, M6, M7 (WS3) from the specs only. Run from anywhere; writes rab/verification/blind/out/.
# AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.
set -e
PY=/Users/ray/Research/rab-ws/.venv/bin/python
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
cd "$ROOT"
mkdir -p "$HERE/out/M5" "$HERE/out/M6" "$HERE/out/M7"
echo "[blind] M5 ..."; "$PY" "$HERE/blind_m5.py" > "$HERE/out/M5/run_log.txt"
echo "[blind] M6 (200,000 paths + 20 robustness seeds; a few minutes) ..."; "$PY" "$HERE/blind_m6.py" > "$HERE/out/M6/run_log.txt"
echo "[blind] M7 ..."; "$PY" "$HERE/blind_m7.py" > "$HERE/out/M7/run_log.txt"
echo "[blind] headlines + report ..."; "$PY" "$HERE/collect_headlines.py"
echo "[blind] done: $HERE/out/blind_headlines.json, $HERE/BLIND_REPORT.md"
