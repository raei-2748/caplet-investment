# WS2 models (M3, M4, M8). From the worktree root:  make -f rab/models/ws2.mk all
# Order matters: M4 and M8 read M3's cached Bayesian posterior and M3's summary.
PY ?= /Users/ray/Research/rab-ws/.venv/bin/python

all: m3 m4 m4-gap m8

# WS2 headline numbers for the decision memos (reads results + blind outputs + Gate B outputs; no model run)
numbers:
	$(PY) rab/models/build_numbers_ws2.py

data:
	$(PY) rab/data/ws2_returns/fetch_returns.py
	$(PY) rab/data/ws2_returns/build_returns.py

m3:
	$(PY) rab/models/m3_branch.py

m3-refit:
	$(PY) rab/models/m3_branch.py --refit

m4: m3
	$(PY) rab/models/m4_cap.py

# The blind paths are not committed (64 MB, gitignored); blind_m3.py regenerates them from the seed (a few minutes).
blind-paths:
	test -f rab/verification/blind_ws2/out/paths/T.npy || (cd rab/verification/blind_ws2 && $(PY) blind_m3.py)

# D6 with a Book L coupon-reinvestment gap charged to Laura's kept money (primary and blind builds side by side)
m4-gap: m3 blind-paths
	$(PY) rab/models/m4_ladder_gap.py

m8: m3
	$(PY) rab/models/m8_sensitivity.py

.PHONY: all data m3 m3-refit m4 m4-gap blind-paths m8 numbers
