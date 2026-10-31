"""AI-generated (Claude Code), 31 Oct 2026. Tally panel_C04: map each judge's ranking to codes, mean ranks, Kendall tau, head-to-heads."""
import itertools, json, pathlib, re
D = pathlib.Path(__file__).parent; key = json.loads((D / "KEY.json").read_text())
R = {}
for j in range(1, 7):
    t = (D / f"judge{j}_scores.md").read_text()
    sec = t.split("## Ranking", 1)[1].split("\n## ", 1)[0]
    nums = []
    for n in re.findall(r"Entry\s+(\d)", sec):
        if n not in nums: nums.append(n)
    R[f"judge{j}"] = [key[f"judge{j}"][f"Entry {n}"] for n in nums[:6]]
codes = sorted(R["judge1"])
def tau(a, b):
    s = 0
    for x, y in itertools.combinations(codes, 2):
        s += 1 if (a.index(x) - a.index(y)) * (b.index(x) - b.index(y)) > 0 else -1
    return s / 15
taus = [tau(R[a], R[b]) for a, b in itertools.combinations(R, 2)]
mean = {c: round(sum(r.index(c) + 1 for r in R.values()) / 6, 2) for c in codes}
h2h = {f"{a} v {b}": f"{sum(r.index(a) < r.index(b) for r in R.values())}-{sum(r.index(b) < r.index(a) for r in R.values())}"
       for a, b in itertools.combinations(["LR2", "LRa", "V45", "A09", "S01"], 2)}
out = {"rankings": R, "mean_rank": dict(sorted(mean.items(), key=lambda kv: kv[1])), "mean_kendall_tau": round(sum(taus) / len(taus), 2), "head_to_head": h2h}
(D / "rankings.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
