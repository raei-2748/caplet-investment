"""Collect Phase B question-generation results from the workflow journals into one file, give every question an id,
and do the exact-duplicate step of Phase C (normalised text match). Main-loop utility; no model inputs.

Run from the repo root:  .venv/bin/python research/insight_v1/scripts/collect_phase_B.py JOURNAL [JOURNAL ...]
Writes research/insight_v1/phase_B/questions.json, research/insight_v1/phase_B/quotes_raw.json and
research/insight_v1/phase_C/questions_deduped.json, and prints counts for the filter log.
"""
import json
import re
import sys

qs, quotes = [], []
for j in sys.argv[1:]:
    for line in open(j):
        o = json.loads(line)
        if o.get("type") != "result":
            continue
        r = o.get("result")
        if not isinstance(r, dict) or "questions" not in r:
            continue
        path = r.get("path", "")
        m = re.search(r"(B\d+[ab])_", path)
        agent = m.group(1) if m else "B?"
        for i, q in enumerate(r["questions"], 1):
            q = dict(q)
            q["id"] = f"{agent}-{i:02d}"
            q["agent"] = agent
            q["lens"] = re.match(r"B\d+", agent).group(0)
            q["source_file"] = path
            qs.append(q)
        for k, qu in enumerate(r.get("quotes") or [], 1):
            qu = dict(qu)
            qu["id"] = f"{agent}-Q{k:02d}"
            qu["agent"] = agent
            quotes.append(qu)

qs.sort(key=lambda q: (int(q["lens"][1:]), q["id"]))


def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", t.lower())).strip()


seen, dedup, dups = {}, [], []
for q in qs:
    k = norm(q["text"])
    if k in seen:
        seen[k]["duplicate_ids"].append(q["id"])
        dups.append(q["id"])
    else:
        q["duplicate_ids"] = []
        seen[k] = q
        dedup.append(q)

missing_anchor = [q["id"] for q in dedup if not q.get("anchor_ids") or not q.get("would_change_detail")]

json.dump(qs, open("research/insight_v1/phase_B/questions.json", "w"), indent=1)
json.dump(quotes, open("research/insight_v1/phase_B/quotes_raw.json", "w"), indent=1)
json.dump(dedup, open("research/insight_v1/phase_C/questions_deduped.json", "w"), indent=1)
by_lens = {}
for q in qs:
    by_lens[q["lens"]] = by_lens.get(q["lens"], 0) + 1
by_tag = {}
for q in dedup:
    by_tag[q["domain_tag"]] = by_tag.get(q["domain_tag"], 0) + 1
print(json.dumps({"agents": sorted({q['agent'] for q in qs}), "questions_total": len(qs), "by_lens": by_lens,
                  "exact_duplicates_removed": len(dups), "after_exact_dedupe": len(dedup),
                  "missing_anchor_or_would_change": missing_anchor, "by_domain_tag": by_tag,
                  "quotes_total": len(quotes),
                  "quotes_by_status": {s: sum(1 for x in quotes if x.get('fetch_status') == s) for s in
                                       {x.get('fetch_status') for x in quotes}}}, indent=1))
