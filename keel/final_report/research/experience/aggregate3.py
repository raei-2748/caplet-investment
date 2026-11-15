"""Combine the third pool's blind readers (judge3_*.csv, criteria A-E of RERANK_RUBRIC.md) and print the ranking,
then reveal each event's source from blind_key_3.json. Ties under 1.0 are broken on D, then A, then E (I115).

python3 -I keel/final_report/research/experience/aggregate3.py
"""
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
key = json.load(open(HERE / "blind_key_3.json"))["events"]
titles = dict(re.findall(r"(?m)^### (E\d): (.*)$", (HERE / "BLIND_POOL_3.md").read_text()))
judges = sorted(HERE.glob("judge3_*.csv"))
crit = ("A", "B", "C", "D", "E")
scores = {i: {} for i in key}
gates = {i: [] for i in key}
for f in judges:
    for r in csv.DictReader(open(f)):
        i = r["id"].strip()
        if i in scores:
            scores[i][f.stem] = {m: float(r[m]) for m in crit}
            gates[i].append(r["gate"].strip().lower())
rows = []
for i in key:
    js = scores[i]
    tot = [sum(v.values()) for v in js.values()]
    mean = sum(tot) / len(tot)
    cm = {m: sum(v[m] for v in js.values()) / len(js) for m in crit}
    split = [m for m in crit if max(v[m] for v in js.values()) - min(v[m] for v in js.values()) >= 2]
    rows.append((i, mean, cm, min(tot), max(tot), split))
rows.sort(key=lambda x: (-x[1], -x[2]["D"], -x[2]["A"], -x[2]["E"]))
print(f"{len(judges)} readers")
print("| Rank | Event | Mean total | A | B | C | D | E | Readers' totals (low-high) | Gate (pass of readers) | Split (2+) on | Source |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
for n, (i, mean, cm, lo, hi, split) in enumerate(rows, 1):
    src = key[i]["source"].split(" (")[0]
    print(f"| {n} | {i}: {titles.get(i, '')} | {mean:.1f} | " + " | ".join(f"{cm[m]:.1f}" for m in crit)
          + f" | {lo:.0f}-{hi:.0f} | {gates[i].count('pass')} of {len(gates[i])} | {','.join(split) or '-'} | {src} |")
