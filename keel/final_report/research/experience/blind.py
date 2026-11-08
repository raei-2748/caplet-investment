"""Pool the candidate events (candidates_*.md), strip who produced them, shuffle, and write the blind pool.

python3 -I keel/final_report/research/experience/blind.py
Writes BLIND_POOL.md (no origin, no evidence, random ids) and blind_key.json (random id -> candidate id, origin).
The key is not shown to the readers.
"""
import json
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
cards = []
for f in sorted(HERE.glob("candidates_*.md")):
    text = f.read_text()
    for block in re.split(r"(?m)^### ", text)[1:]:
        head, *rest = block.split("\n")
        cid, _, title = head.partition(":")
        fields = {}
        for line in rest:
            m = re.match(r"^- ([A-Za-z /]+?)(?: \(Sydney\))?: (.*)$", line)
            if m:
                fields[m.group(1).strip().lower()] = m.group(2).strip()
        if "what happened" not in fields:
            continue
        cards.append({"cid": cid.strip(), "title": title.strip(), **fields})
SCRUB = [(r"\bour (research )?office'?s?\b", "our"), (r"\bthe (team's )?research office\b", "the team"),
         (r"\bthe office\b", "the team"), (r"\bthe students\b", "the team"), (r"\bKeel's\b", "our"), (r"\bKeel\b", "we"),
         (r"\bCaplet's\b", "our"), (r"\bCaplet\b", "we")]
VISIBLE = ("title", "date", "what happened", "stakes", "decision or response", "what changed afterwards", "vivid detail")
flags = []
for c in cards:
    for f in VISIBLE:
        v = c.get(f, "")
        for pat, rep in SCRUB:
            v = re.sub(pat, rep, v)
        c[f] = v
        for w in re.findall(r"\b(AI|Nora|Felix|Jun|Kai|Amara|Tess|Ray|Ahaan|Darren|Harry|Eric|Young|agent|agents|model run)\b", v):
            flags.append((c["cid"], f, w))
random.Random(2033).shuffle(cards)
key, lines = {}, ["# The blind pool of competition events", "",
                  "Each event below is real and confirmed in the team's records. Who produced it is hidden. Ids are random.", ""]
for i, c in enumerate(cards, 1):
    bid = f"X{i:03d}"
    key[bid] = {"cid": c["cid"], "origin": c.get("origin", "?"), "evidence": c.get("evidence", "")}
    lines += [f"### {bid}: {c['title']}", f"- Date: {c.get('date', '')}", f"- What happened: {c['what happened']}",
              f"- Stakes: {c.get('stakes', '')}", f"- Decision or response: {c.get('decision or response', '')}",
              f"- What changed afterwards: {c.get('what changed afterwards', '')}",
              f"- Vivid detail: {c.get('vivid detail', '')}", ""]
(HERE / "BLIND_POOL.md").write_text("\n".join(lines))
(HERE / "blind_key.json").write_text(json.dumps(key, indent=1))
print(len(cards), "events pooled"); print("words that may reveal origin:", flags)
