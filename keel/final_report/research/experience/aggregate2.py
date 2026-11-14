"""Combine the second pool's blind readers (judge2_*.csv, criteria A-E of RERANK_RUBRIC.md) into RANKING_2.md,
then reveal origins from blind_key_2.json.

python3 -I keel/final_report/research/experience/aggregate2.py
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
key = json.load(open(HERE / "blind_key_2.json"))
titles = dict(re.findall(r"(?m)^### (Y\d{3}): (.*)$", (HERE / "BLIND_POOL_2.md").read_text()))
judges = sorted(HERE.glob("judge2_*.csv"))
crit = ("A", "B", "C", "D", "E")
scores = {i: {} for i in key}
for f in judges:
    for r in csv.DictReader(open(f)):
        i = r["id"].strip()
        if i in scores:
            scores[i][f.stem] = {m: float(r[m]) for m in crit}
rows = []
for i in key:
    js = scores[i]
    tot = [sum(v.values()) for v in js.values()]
    mean = sum(tot) / len(tot) if tot else 0
    cm = {m: sum(v[m] for v in js.values()) / len(js) if js else 0 for m in crit}
    split = [m for m in crit if js and max(v[m] for v in js.values()) - min(v[m] for v in js.values()) >= 2]
    rows.append((i, mean, cm, min(tot) if tot else 0, split))
# ties under 1.0 broken on A then E (rubric): sort by mean, then A, then E
rows.sort(key=lambda x: (-x[1], -x[2]["A"], -x[2]["E"]))
lines = ["# The blind ranking of the second event pool (scored Sat 14 Nov 2026)", "",
         f"{len(judges)} readers scored all {len(key)} events of `BLIND_POOL_2.md` blind, each criterion A-E of "
         "`RERANK_RUBRIC.md` from 1 to 5 (total out of 25). Origins were revealed only after the scores were in. "
         "Figures are as recorded that day; the Mon 16 Nov run corrects the top events' fact sheets and re-scores them.", "",
         "| Rank | Id | Event | Mean total | A | B | C | D | E | Lowest reader | Split (2+) on | Origin | Candidate |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for n, (i, mean, cm, lo, split) in enumerate(rows, 1):
    lines.append(f"| {n} | {i} | {titles.get(i, '')} | {mean:.1f} | " + " | ".join(f"{cm[m]:.1f}" for m in crit)
                 + f" | {lo:.0f} | {','.join(split) or '-'} | {key[i]['origin'].split()[0]} | {key[i]['cid']} |")
for k in (10, 20, 40):
    lines.append("")
    lines.append(f"Origins in the top {k}: " + str(dict(Counter(key[i]['origin'].split()[0] for i, *_ in rows[:k]))))
lines.append("")
lines.append("Origins in the whole pool: " + str(dict(Counter(v['origin'].split()[0] for v in key.values()))))
(HERE / "RANKING_2.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[:30]))
