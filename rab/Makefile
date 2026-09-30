# RAB Kit: one command rebuilds every number, figure and check (RUN_PLAN s1 item 5).
# AI-generated (Claude Code) for Team Caplet, completeness critic, 30 Sep 2026 (Sydney).
#
#   make -C rab all      # models -> stream numbers -> Friday kit (no network, seed 20260930)
#   make -C rab checks   # Gate A hash, Gate B (WS2/WS3/WS4), Gate C, note self-test, WS3 memo trace
#   make -C rab verify   # all + checks, then lists every tracked file under rab/ that changed
#   make -C rab blind    # the blind second builds (slower; M3 blind paths take a few minutes)
#
# Every script runs from the worktree root (its paths are relative to it). Nothing here touches the network,
# WInS, the IPS or the live Sheet: refresh_tickets.py runs on --basis locked (the Gate A basis). Friday's
# network refresh is a separate, manual step (rab/trades/friday_checklist.md).
# Env: the pinned venv in rab/requirements.lock (Python 3.12). Override with PY=/path/to/python.

PY   ?= /Users/ray/Research/rab-ws/.venv/bin/python
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/..)
RUN   = cd "$(ROOT)" && $(PY)

.PHONY: all models m1 numbers-lock m2 bookl ws2 m5 m6 m7 ws3-numbers stream-numbers kit m9 tickets notes sheets \
        redteam checks gate-a gate-b gate-c trace verify blind env page

all: models stream-numbers kit page

models: m1 m2 bookl ws2 m5 m6 m7

# M1 ladder pricer on the 28 Sep 2026 curve (latest row of the committed 2026 file), then the locked numbers.yaml.
m1:
	$(RUN) rab/models/m1_ladder.py
numbers-lock: m1
	$(RUN) rab/models/build_numbers.py --lock

# M2 rate paths to Jan 2027 (figures included) and WS4's Book L basis check.
m2: numbers-lock
	$(RUN) rab/models/m2_rate_paths.py
bookl: numbers-lock
	cd "$(ROOT)" && $(PY) rab/results/M2/bookL_basis_check.py > rab/results/M2/bookL_basis_check.txt

# M3 branch MC, M4 cap optimiser (+ coupon-gap variants), M8 sensitivity: WS2's own makefile, unchanged.
ws2: numbers-lock
	cd "$(ROOT)" && $(MAKE) -f rab/models/ws2.mk PY=$(PY) all

# M5 century backtest, M6 rivals + fund choice, M7 stress.
m5: numbers-lock
	$(RUN) rab/models/m5_backtest.py
m6: m5
	$(RUN) rab/models/m6_rivals.py
m7: m5
	$(RUN) rab/models/m7_stress.py
ws3-numbers: m5 m6 m7
	$(RUN) rab/models/ws3_numbers.py

# Stream numbers files the decision memos cite (numbers_ws4.yaml is hand-kept from m2_results.json; see its header).
stream-numbers: ws2 ws3-numbers
	$(RUN) rab/models/build_numbers_ws2.py
	$(RUN) rab/decisions/build_numbers_ws3.py

# Friday kit on the Gate A basis: M9 screen, tickets, notes, Sheet-tab mirrors.
kit: m9 tickets notes sheets
m9: numbers-lock
	$(RUN) rab/trades/m9_screen.py
tickets: m9
	$(RUN) rab/trades/refresh_tickets.py
notes: tickets
	$(RUN) rab/trades/build_notes.py
sheets: notes
	$(RUN) rab/sheets/build_sheet_tabs.py

# WS8 RAB Lab page (rab/page/index.html): exports M3/M4 paths, M5 history and the tickets; JS checked under node.
page: ws2 m5 tickets
	$(RUN) rab/page/build_page.py

# WS7 red-team scratch checks (single build, MODEL, UNVERIFIED until a stream reproduces them).
redteam: numbers-lock
	cd "$(ROOT)" && $(PY) rab/redteam/ws7_assumptions_reinvest_check.py > rab/redteam/ws7_assumptions_reinvest_check_output.txt
	cd "$(ROOT)" && $(PY) rab/redteam/ws7_devils_advocate_checks.py > rab/redteam/ws7_devils_advocate_checks_output.txt
	cd "$(ROOT)" && $(PY) rab/redteam/ws7_kac3_check.py > rab/redteam/ws7_kac3_check_output.txt
	cd "$(ROOT)" && $(PY) rab/redteam/ws7_da_r5_checks.py > rab/redteam/ws7_da_r5_checks_output.txt

checks: gate-a gate-b gate-c trace

gate-a:
	cd "$(ROOT)" && test "$$(shasum -a 256 rab/numbers.yaml | cut -c1-64)" = "$$(cut -c1-64 rab/numbers.yaml.sha256)" \
	  && echo "Gate A: numbers.yaml hash matches rab/numbers.yaml.sha256" || (echo "Gate A: HASH MISMATCH" && false)
	$(RUN) rab/verification/gateA_third_check.py

gate-b:
	$(RUN) rab/verification/gateB_ws2/gateB_ws2_checks.py
	$(RUN) rab/verification/gateB_ws3/gateB_ws3_checks.py
	$(RUN) rab/verification/gateB_ws4/gateB_ws4_checks.py
	$(RUN) rab/verification/blind_m1_2/breakeven_check.py   # blind 2nd build of WS7's coupon break-even

gate-c:
	$(RUN) rab/trades/check_gate_c.py
	$(RUN) rab/trades/check_gate_c.py --self-test
	$(RUN) rab/trades/note_check.py --self-test

# Every figure in the WS3 memos traced to a numbers file (the other memos: rab/verification/trace_memos.py).
trace:
	$(RUN) rab/decisions/build_numbers_ws3.py --check
	$(RUN) rab/verification/trace_memos.py

verify: all checks
	@cd "$(ROOT)" && echo "Tracked files under rab/ changed by the rebuild (expect none, or run stamps only):" \
	  && git status --porcelain -- rab/ && git diff --stat -- rab/

# Blind second builds (Gate A/B). The WS2 blind paths are gitignored and regenerated from the seed.
blind:
	cd "$(ROOT)/rab/verification/blind_m1" && $(PY) blind_pricer.py
	$(RUN) rab/verification/blind_m1_2/blind_m1_2.py
	$(RUN) rab/verification/blind/m2_blind.py
	$(RUN) rab/verification/blind/deterministic_check.py
	zsh "$(ROOT)/rab/verification/blind/run_all.sh"
	zsh "$(ROOT)/rab/verification/blind_ws2/run_all.sh"

env:
	$(PY) --version
	cd "$(ROOT)" && uv pip freeze --python $(PY) 2>/dev/null | diff - rab/requirements.lock | grep -v "^[0-9a-z,]*$$" | grep -v "^> #" ; test -z "$$(uv pip freeze --python $(PY) 2>/dev/null | diff - rab/requirements.lock | grep "^[<>] [^#]")" && echo "env matches rab/requirements.lock"
