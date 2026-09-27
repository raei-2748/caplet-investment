"""D13 step 1 (mechanical): re-fetch every Phase B quote's source page and test whether the exact text appears
verbatim (after normalising whitespace and curly quotes). No judgement; agents review context and failures after.

Run from the repo root: .venv/bin/python research/insight_v1/scripts/D13_mechanical_quote_check.py
Input: research/insight_v1/phase_B/quotes_raw.json. Output: research/insight_v1/phase_D/D13_mechanical_check.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from fetch_text import fetch, to_text, norm  # noqa: E402

quotes = json.load(open("research/insight_v1/phase_B/quotes_raw.json"))
pages, out = {}, []
for q in quotes:
    url = (q.get("url") or "").strip()
    rec = {"id": q["id"], "url": url, "claimed_status": q.get("fetch_status"), "exact_text": q.get("exact_text", "")}
    if not url.startswith("http"):
        rec["result"] = "NO_URL"
        out.append(rec)
        continue
    if url not in pages:
        try:
            pages[url] = norm(to_text(fetch(url)))
        except SystemExit as e:
            pages[url] = None
            rec["fetch_error"] = str(e)
        except Exception as e:  # noqa: BLE001
            pages[url] = None
            rec["fetch_error"] = repr(e)
    page = pages[url]
    if page is None:
        rec["result"] = "FETCH_FAILED"
    else:
        phrase = norm(rec["exact_text"]).strip().strip('"').strip()
        rec["result"] = "VERBATIM" if phrase and phrase in page else (
            "VERBATIM_CASE_INSENSITIVE" if phrase.lower() in page.lower() else "NOT_FOUND")
    out.append(rec)
os.makedirs("research/insight_v1/phase_D", exist_ok=True)
json.dump(out, open("research/insight_v1/phase_D/D13_mechanical_check.json", "w"), indent=1)
from collections import Counter
print(Counter(r["result"] for r in out))
print("pages:", len(pages), "failed pages:", sum(1 for v in pages.values() if v is None))
