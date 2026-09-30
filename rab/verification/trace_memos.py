"""Trace every $, %, bp and decimal figure in the decision memos to a numbers file (a typo screen, not a proof).

Completeness critic, RAB Kit, 30 Sep 2026 (Sydney). AI-generated verification code (Claude Code) for Team Caplet.
Generalises rab/decisions/build_numbers_ws3.py --check (which covers only the three WS3 memos) to every memo in
rab/decisions/ and the October trade memo. A figure is TRACED if it matches, at its printed precision, a value in
rab/numbers.yaml, rab/numbers_ws2.yaml, rab/numbers_ws3.yaml, rab/numbers_ws4.yaml, rab/trades/tickets.csv, tickets.md or the
M9 screen output; case facts and rule thresholds in ALLOW are skipped. Text in `backticks` (file names, keys) is
ignored. A round figure ("about $31,000") can match an unrelated value by chance, so TRACED means "a value like this
exists", and UNTRACED means "no numbers file holds this figure: cite its source or add it at the Friday re-lock".

Run from the worktree root:  /Users/ray/Research/rab-ws/.venv/bin/python rab/verification/trace_memos.py [--strict]
Writes rab/verification/trace_memos.txt. Exit code 1 with --strict if any figure is untraced.
"""
import csv
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
P = lambda *a: os.path.join(ROOT, *a)

MEMOS = sorted(glob.glob(P("rab", "decisions", "*.md"))) + [P("rab", "trades", "october_trade.md")]
SOURCES = ["rab/numbers.yaml", "rab/numbers_ws2.yaml", "rab/numbers_ws3.yaml", "rab/numbers_ws4.yaml"]

# Case facts, rule thresholds, commissions, scenario inputs (not model outputs). Same idea as build_numbers_ws3.ALLOW.
ALLOW = {
    "$": {50000, 150000, 300000, 450000, 500000, 2500, 2000, 1000, 500, 250, 100, 25, 10, 3, 5, 0},  # 2500: Oct trigger
    "%": {0, 1, 2, 3, 4, 5, 10, 20, 25, 30, 38, 40, 50, 60, 62, 65, 70, 75, 80, 90, 95, 99, 99.5, 100, 200},
    "bp": {25, 50, 100, 150, 200},
    "dec": {0.90, 0.95, 0.50},
}
PAT = re.compile(r"(\$\d[\d,]*(?:\.\d+)?k?)|(\d+(?:\.\d+)?%)|(-?\d+(?:\.\d+)?bp)|(\b\d\.\d{2,4}\b)")


def leaves(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from leaves(v)
    elif isinstance(x, list):
        for v in x:
            yield from leaves(v)
    elif isinstance(x, bool):
        return
    elif isinstance(x, (int, float)):
        yield float(x)
    elif isinstance(x, str):
        for m in re.finditer(r"-?\d[\d,]*\.?\d*", x):  # numbers inside strings ("0/149", "$41,000")
            s = m.group(0).replace(",", "").rstrip(".")
            try:
                yield float(s)
            except ValueError:
                pass


def values():
    vals = []
    for s in SOURCES:
        vals += list(leaves(yaml.safe_load(open(P(s)))))
    with open(P("rab", "trades", "tickets.csv")) as fh:
        for row in csv.DictReader(fh):
            vals += list(leaves(list(row.values())))
    vals += list(leaves(open(P("rab", "trades", "tickets.md")).read()))  # expected / worst-case cash columns
    for f in glob.glob(P("rab", "trades", "out", "m9_screen_*.json")):
        vals += list(leaves(json.load(open(f))))
    return [abs(v) for v in vals]


def check(avals, path):
    text = re.sub(r"`[^`]*`", "", open(path).read())
    out, n = [], 0
    for mt in PAT.finditer(text):
        tok = mt.group(0)
        if mt.group(1):
            k = tok.endswith("k")
            s = tok[1:].rstrip("k").replace(",", "")
            x = float(s) * (1000 if k else 1)
            dec = len(s.split(".")[1]) if "." in s else 0
            if dec:
                prec = 10 ** (-dec) * (1000 if k else 1)
            else:
                ip = s.split(".")[0]
                prec = 1000 if k else 10 ** min(len(ip) - len(ip.rstrip("0")), 3)
            kind, cands = "$", avals
        elif mt.group(2):
            s = tok[:-1]
            x = float(s)
            prec = 10 ** (-(len(s.split(".")[1]) if "." in s else 0))
            kind, cands = "%", [v * 100 for v in avals] + avals
        elif mt.group(3):
            s = tok[:-2].lstrip("-")
            x = float(s)
            prec = 10 ** (-(len(s.split(".")[1]) if "." in s else 0))
            kind, cands = "bp", avals + [v * 10000 for v in avals]
        else:
            x = float(tok)
            prec = 10 ** (-len(tok.split(".")[1]))
            kind, cands = "dec", avals
        n += 1
        if x in ALLOW[kind]:
            continue
        if not any(abs(c - x) <= prec / 2 + 1e-9 for c in cands):
            ctx = text[max(0, mt.start() - 60): mt.end() + 30].replace("\n", " ")
            out.append(f"  UNTRACED {tok:>12}  ...{ctx}...")
    return n, out


def main():
    avals = values()
    lines, total, bad = [], 0, 0
    for m in MEMOS:
        n, out = check(avals, m)
        total += n
        bad += len(out)
        lines.append(f"{os.path.relpath(m, ROOT)}: {n} figures, {len(out)} untraced")
        lines += out
    head = (f"trace_memos: {total} figures in {len(MEMOS)} memos, {bad} untraced "
            f"(sources: {', '.join(SOURCES)}, rab/trades/tickets.csv + tickets.md, rab/trades/out/m9_screen_*.json)")
    report = "\n".join([head, ""] + lines) + "\n"
    open(P("rab", "verification", "trace_memos.txt"), "w").write(report)
    print(report)
    if "--strict" in sys.argv and bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
