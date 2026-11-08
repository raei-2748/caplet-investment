"""Combine the blind readers' scores (judge_*.csv) into RANKING.md, then reveal origins from blind_key.json.

python3 -I keel/final_report/research/experience/aggregate.py
"""
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
key = json.load(open(HERE / "blind_key.json"))
titles = dict(re.findall(r"(?m)^### (X\d{3}): (.*)$", (HERE / "BLIND_POOL.md").read_text()))
judges = sorted(HERE.glob("judge_*.csv"))
scores = {i: {} for i in key}
for f in judges:
    for r in csv.DictReader(open(f)):
        i = r["id"].strip()
        if i in scores:
            scores[i][f.stem] = {m: float(r[m]) for m in ("W", "V", "C", "S", "total")}
ranks = {}
for f in judges:
    order = sorted(scores, key=lambda i: -scores[i].get(f.stem, {"total": 0})["total"])
    for n, i in enumerate(order, 1):
        ranks.setdefault(i, []).append(n)
rows = []
for i in key:
    t = [scores[i][j]["total"] for j in scores[i]]
    mean = sum(t) / len(t) if t else 0
    rows.append((i, mean, min(t) if t else 0, sum(ranks[i]) / len(ranks[i]), sum(1 for r in ranks[i] if r <= 15)))
rows.sort(key=lambda x: (-x[1], x[3]))
lines = ["# The blind ranking of the competition events", "",
         f"{len(judges)} readers scored all {len(key)} events blind (no origin, random ids); each measure 1-10, total out of 40.",
         "Origins and the candidate ids were revealed only after the scores were in.", "",
         "| Rank | Id | Event | Mean total | Lowest reader | Mean rank | Readers ranking it top 15 | Origin | Candidate |",
         "|---|---|---|---|---|---|---|---|---|"]
for n, (i, mean, lo, mr, top) in enumerate(rows, 1):
    lines.append(f"| {n} | {i} | {titles.get(i, '')} | {mean:.1f} | {lo:.0f} | {mr:.1f} | {top} | {key[i]['origin'].split()[0]} | {key[i]['cid']} |")
top30 = rows[:30]
from collections import Counter
lines += ["", "Origins in the top 10: " + str(dict(Counter(key[i]['origin'].split()[0] for i, *_ in rows[:10]))),
          "Origins in the top 30: " + str(dict(Counter(key[i]['origin'].split()[0] for i, *_ in top30)))]
(HERE / "RANKING.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[:40]))
print(lines[-2]); print(lines[-1])
