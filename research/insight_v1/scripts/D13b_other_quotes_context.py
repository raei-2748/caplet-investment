"""D13b helper: for every Phase B quote whose speaker is NOT Laura Gao, re-fetch the source page (fixed helper,
cached) and print the text around the quote so a human/agent can check speaker and context (not trimmed into a new
meaning).

Inputs (status labels):
- research/insight_v1/phase_B/quotes_raw.json (Phase B agents' quotes; claims to be checked)
- research/insight_v1/phase_D/D13_mechanical_check.json (mechanical VERBATIM/NOT_FOUND results; VERIFIED by script)
Output: research/insight_v1/phase_D/_work/D13b_contexts.json (id -> found flag + context window); stdout summary.
Run from the repo root: .venv/bin/python research/insight_v1/scripts/D13b_other_quotes_context.py
The Laura-speaker id list below is a judgement (ASSUMPTION) made by D13b from each quote's context field; quotes by
reporters, publishers or the case's unattributed pull quote are treated as NOT Laura's and are in scope here.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from fetch_text import fetch, to_text, norm  # noqa: E402

LAURA = set("""B1b-Q11 B2a-Q12 B2b-Q07 B2b-Q08 B2b-Q10 B3a-Q02 B3a-Q03 B3a-Q04 B3b-Q03 B3b-Q04 B3b-Q09 B3b-Q13""".split())
LAURA |= {f"B8b-Q{i:02d}" for i in range(2, 27)} | {f"B8b-Q{i:02d}" for i in range(30, 42)}
LAURA |= {f"B8a-Q{i:02d}" for i in range(1, 16)} | {f"B8a-Q{i:02d}" for i in range(17, 39)}
LAURA |= {f"B9b-Q{i:02d}" for i in range(1, 15)}
PRIVATE_HOSTS = ("inverse.com", "inputmag.com")


def main():
    quotes = json.load(open("research/insight_v1/phase_B/quotes_raw.json"))
    mech = {r["id"]: r for r in json.load(open("research/insight_v1/phase_D/D13_mechanical_check.json"))}
    out = {}
    for q in quotes:
        if q["id"] in LAURA:
            continue
        url = (q.get("url") or "").strip()
        rec = {"mechanical": mech[q["id"]]["result"], "url": url}
        if url.startswith("http"):
            try:
                page = norm(to_text(fetch(url)))
                phrase = norm(q["exact_text"]).strip().strip('"').strip()
                i = page.find(phrase)
                rec["found"] = i >= 0
                if i >= 0:
                    rec["context"] = page[max(0, i - 350): i + len(phrase) + 350]
                else:
                    words = phrase.split()
                    for n in (6, 4):
                        j = page.find(" ".join(words[:n]))
                        if j >= 0:
                            rec["partial_context"] = page[max(0, j - 200): j + len(phrase) + 300]
                            break
            except SystemExit as e:
                rec["found"] = None
                rec["error"] = str(e)
            except Exception as e:  # noqa: BLE001
                rec["found"] = None
                rec["error"] = repr(e)
        else:
            rec["found"] = None
            rec["error"] = "repo path, not a URL"
        if any(h in url for h in PRIVATE_HOSTS):  # privacy rule: page holds personal-life material
            for k in ("context", "partial_context"):
                if k in rec:
                    rec[k] = "[context withheld: surrounding text holds personal-life material (privacy rule)]"
        out[q["id"]] = rec
    os.makedirs("research/insight_v1/phase_D/_work", exist_ok=True)
    json.dump(out, open("research/insight_v1/phase_D/_work/D13b_contexts.json", "w"), indent=1, ensure_ascii=False)
    print("in scope:", len(out))
    from collections import Counter
    print(Counter((v["mechanical"], v.get("found")) for v in out.values()))


if __name__ == "__main__":
    main()
