"""D13a step 1: re-check every Phase B quote whose speaker is (or is presented as) Laura Gao against its source page
with the fixed fetch helper, and save the text around each quote so speaker, context and trimming can be judged.

Inputs (status labels):
- research/insight_v1/phase_B/quotes_raw.json (Phase B agents' claims; to be checked)
- research/insight_v1/phase_D/D13_mechanical_check.json (script re-fetch: VERBATIM / NOT_FOUND / NO_URL / FETCH_FAILED)
- competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt (official case text; VERIFIED-REPO-FILE)
- LAURA_IDS below: the 100 ids that D13b assigned to D13a as Laura's own words, plus the 4 ids of the case pull quote
  (a scoping judgement, ASSUMPTION, re-checked by D13a on each source page).
- NEW below: candidate quotes D13a found on primary pages while searching for the pull quote's source (not in Phase B).
Output: research/insight_v1/phase_D/_work/D13a_contexts.json (id -> found flag, mechanical result, context window);
stdout summary.
Run from the repo root: .venv/bin/python research/insight_v1/scripts/D13a_laura_quotes_check.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from fetch_text import fetch, to_text, norm  # noqa: E402

LAURA_IDS = set("B1b-Q11 B2a-Q12 B2b-Q07 B2b-Q08 B2b-Q10 B3a-Q02 B3a-Q03 B3a-Q04 B3b-Q03 B3b-Q04 B3b-Q09 B3b-Q13".split())
LAURA_IDS |= {f"B8b-Q{i:02d}" for i in range(2, 27)} | {f"B8b-Q{i:02d}" for i in range(30, 42)}
LAURA_IDS |= {f"B8a-Q{i:02d}" for i in range(1, 16)} | {f"B8a-Q{i:02d}" for i in range(17, 39)}
LAURA_IDS |= {f"B9b-Q{i:02d}" for i in range(1, 15)}
PULL_IDS = {"B2a-Q13", "B2b-Q11", "B8b-Q01", "B8a-Q39"}
CASE_TXT = "competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt"
DP = "https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a"
NEW = {
    "D13a-N01": (DP, "It’s actually harder as an entrepreneur because not only are you letting yourself down, but more "
                     "importantly, you’re also letting other people down — people who were your earliest supporters and "
                     "were the first to believe in you."),
    "D13a-N02": (DP, "As girls, it is easy for us to put too much weight on other people’s opinions. There’s a social "
                     "stigma that many women aren’t mentally brave or prepared enough to explore the unknown alone. I "
                     "don’t think any of that matters though, if you are able to get past the hardest part: actually "
                     "launching the venture."),
}
WINDOW = 350


def window(page, phrase):
    i = page.find(phrase)
    if i < 0:
        return False, ""
    return True, page[max(0, i - WINDOW): i + len(phrase) + WINDOW]


def main():
    quotes = {q["id"]: q for q in json.load(open("research/insight_v1/phase_B/quotes_raw.json"))}
    mech = {r["id"]: r for r in json.load(open("research/insight_v1/phase_D/D13_mechanical_check.json"))}
    missing = (LAURA_IDS | PULL_IDS) - set(quotes)
    if missing:
        sys.exit(f"ids not in quotes_raw.json: {sorted(missing)}")
    pages, out = {}, {}
    todo = [(i, quotes[i]["url"], quotes[i]["exact_text"]) for i in sorted(LAURA_IDS | PULL_IDS)]
    todo += [(i, u, t) for i, (u, t) in NEW.items()]
    for qid, url, text in todo:
        url = (url or "").strip()
        phrase = norm(text).strip().strip('"').strip()
        rec = {"url": url, "mechanical": mech[qid]["result"] if qid in mech else "NEW"}
        if url.startswith("http"):
            if url not in pages:
                try:
                    pages[url] = norm(to_text(fetch(url)))
                except SystemExit as e:  # helper exits on HTTP errors
                    pages[url] = None
                    rec["fetch_error"] = str(e)
            page = pages[url]
        else:  # repo file (the case pull quote)
            page = norm(open(CASE_TXT, encoding="utf-8").read())
            rec["checked_in"] = CASE_TXT
        if page is None:
            rec["found"] = False
        else:
            rec["found"], rec["context"] = window(page, phrase)
        out[qid] = rec
    os.makedirs("research/insight_v1/phase_D/_work", exist_ok=True)
    json.dump(out, open("research/insight_v1/phase_D/_work/D13a_contexts.json", "w"), indent=1, ensure_ascii=False)
    found = sum(1 for r in out.values() if r["found"])
    print(f"checked {len(out)} quotes ({len(LAURA_IDS)} Laura ids, {len(PULL_IDS)} pull-quote ids, {len(NEW)} new); "
          f"found verbatim: {found}; not found: {[k for k, r in out.items() if not r['found']]}")


if __name__ == "__main__":
    main()
