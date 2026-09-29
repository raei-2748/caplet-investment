# WS3 blind rebuild of M5, M6, M7

Second, independent implementation of the three WS3 models for Gate B (RUN_PLAN s3: "each model rebuilt blind from
its spec"). AI-generated verification code (Claude Code, blind builder) for Team Caplet; no deliverable text.

## Protocol

- Read: `rab/models/M5_SPEC.md`, `M6_SPEC.md`, `M7_SPEC.md`; `rab/data/**` (curves, FRED, history snapshot, JPM
  tables, market inflation); the locked `rab/numbers.yaml` (sha256 492ed320..., unchanged).
- Not read: any `.py` under `rab/models/` or `rab/results/`, anything under `research/insight_v1/`, the primary's
  result files. The only leak was one-sentence headline lines in `rab-ws/STATUS.md` and the primary's commit message,
  seen while checking conventions; they were not used to write or tune code (`BLIND_REPORT.md`, Disclosure).
- Curve method (`blind_curve.py`) written from M5_SPEC section 2 alone; it reproduces the Gate A headline to the cent.

## Files

| File | What |
|---|---|
| `blind_curve.py` | Par-curve bootstrap (D1 method), dates and constants of the plan |
| `blind_m5.py` | Cost-of-certainty series 1871-2026 and the start-year backtest 1872-2020 |
| `blind_m6.py` | Rivals (REC, R1-R6) in the history and MC lenses; branch-fund alternatives and the switch rule |
| `blind_m7.py` | Stress scenarios S0-S7 with thresholds, and the real value of the payments |
| `collect_headlines.py` | Flattens the three `*_results.json` into `out/blind_headlines.json` and writes `BLIND_REPORT.md` |
| `run_all.sh` | Runs everything in order (about 15 s) |
| `out/M5`, `out/M6`, `out/M7` | The spec's named outputs (CSV, PNG, JSON, report and run log) |
| `BLIND_REPORT.md` | Headline numbers, checks and the readings chosen where the spec is ambiguous |

## Run

```
zsh rab/verification/blind/run_all.sh
```

Python: `/Users/ray/Research/rab-ws/.venv/bin/python` (numpy, pandas, scipy, matplotlib, pyyaml). Seeds: 20260930
(returns), 20260936 (inflation). Deterministic apart from the MC lens, whose tolerances are in M6_SPEC section 7.
