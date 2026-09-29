# WS2 models (M3, M4, M8). From the worktree root:  make -f rab/models/ws2.mk all
# Order matters: M4 and M8 read M3's cached Bayesian posterior and M3's summary.
PY ?= /Users/ray/Research/rab-ws/.venv/bin/python

all: m3 m4 m8

data:
	$(PY) rab/data/ws2_returns/fetch_returns.py
	$(PY) rab/data/ws2_returns/build_returns.py

m3:
	$(PY) rab/models/m3_branch.py

m3-refit:
	$(PY) rab/models/m3_branch.py --refit

m4: m3
	$(PY) rab/models/m4_cap.py

m8: m3
	$(PY) rab/models/m8_sensitivity.py

.PHONY: all data m3 m3-refit m4 m8
