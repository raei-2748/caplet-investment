"""Phase C main-loop step: build merged questions from the Librarian's clusters. Every source question id must be in
exactly one cluster; merged fields are the union/concatenation of member fields.
Run from repo root: .venv/bin/python research/insight_v1/scripts/build_merged_questions.py
Writes research/insight_v1/phase_C/merged_questions.json and prints counts."""
import json
from collections import Counter

qs = {q["id"]: q for q in json.load(open("research/insight_v1/phase_C/questions_deduped.json"))}
cl = json.load(open("research/insight_v1/phase_C/librarian_clusters.json"))
if isinstance(cl, dict):
    cl = cl["clusters"]
placed = Counter(i for c in cl for i in c["source_ids"])
missing = [i for i in qs if i not in placed]
dup = [i for i, n in placed.items() if n > 1]
unknown = [i for i in placed if i not in qs]
merged = []
for n, c in enumerate(cl, 1):
    mem = [qs[i] for i in c["source_ids"] if i in qs]
    merged.append({
        "mid": f"M{n:03d}", "canonical_text": c["canonical_text"], "domain_tag": c["domain_tag"],
        "source_ids": c["source_ids"], "lenses": sorted({m["lens"] for m in mem}, key=lambda x: int(x[1:])),
        "n_members": len(mem),
        "anchor_ids": sorted({a for m in mem for a in m.get("anchor_ids", [])}),
        "anchor_quotes": [m["anchor_quote"] for m in mem][:4],
        "would_change": [f'{m["would_change_type"]}: {m["would_change_detail"]}' for m in mem],
        "deliverables": sorted({d for m in mem for d in m.get("deliverables", [])}),
        "hypotheses": [f'[{m["id"]}] {m["hypothesis"]}' for m in mem],
        "north_star": [m.get("north_star", "") for m in mem][:3],
    })
# add any missing question as its own cluster so nothing is lost
for i in missing:
    m = qs[i]
    merged.append({"mid": f"M{len(merged)+1:03d}", "canonical_text": m["text"], "domain_tag": m["domain_tag"],
                   "source_ids": [i], "lenses": [m["lens"]], "n_members": 1, "anchor_ids": m["anchor_ids"],
                   "anchor_quotes": [m["anchor_quote"]], "would_change": [f'{m["would_change_type"]}: {m["would_change_detail"]}'],
                   "deliverables": m["deliverables"], "hypotheses": [f'[{i}] {m["hypothesis"]}'], "north_star": [m.get("north_star", "")],
                   "note": "added by main loop: not placed by Librarian"})
json.dump(merged, open("research/insight_v1/phase_C/merged_questions.json", "w"), indent=1)
print(json.dumps({"clusters": len(cl), "merged_total": len(merged), "missing_added": missing, "placed_twice": dup,
                  "unknown_ids": unknown, "size_dist": dict(Counter(m["n_members"] for m in merged)),
                  "by_tag": dict(Counter(m["domain_tag"] for m in merged)),
                  "multi_lens": sum(1 for m in merged if len(m["lenses"]) > 1)}, indent=1))
