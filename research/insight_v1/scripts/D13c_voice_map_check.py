"""D13c (Voice-of-Laura mapper): re-check every Laura quote that D13c_voice_map.md uses, plus the new candidate
lines D13c found, against a FRESH copy of each source page, and check the case lines the map quotes.

Why: the map may use a line as Laura's words only if D13a marked it VERIFIED-PRIMARY. This script (1) confirms that
status in D13a's JSON, (2) re-fetches each page (curl, default user agent first, then the helper's browser user
agent; falls back to the shared helper cache only if both fail, and says so) and (3) checks the exact words with the
helper's own text extraction and normalisation (fetch_text.to_text / fetch_text.norm, fixed ~13:50 UTC 2026-09-27).

Inputs (status labels):
- research/insight_v1/phase_D/D13a_laura_quotes_verified.json (D13a's verdicts; VERIFIED-PRIMARY gate)
- USED below: the D13a ids quoted in D13c_voice_map.md (a D13c selection, ASSUMPTION about usefulness)
- CANDIDATES below: lines D13c read on primary pages that are NOT in D13a's register (VERIFIED-PRIMARY for wording
  only once this script finds them; they still need D13a's speaker/context/privacy ruling before use as her words)
- CASE_LINES below: case wording quoted in the map (VERIFIED-REPO-FILE check against the official case text)
- competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt (official case, VERIFIED-REPO-FILE)
Output: stdout table only. It prints NO page text, because the words around a quote can contain private material that
the privacy screen excludes. Fresh page copies are written only to the session scratchpad given by --tmp (outside
the repo); nothing is written inside the repo.
Run from the repo root:
    .venv/bin/python research/insight_v1/scripts/D13c_voice_map_check.py [--tmp DIR]
Exit code 1 if any used quote is not VERIFIED-PRIMARY in D13a's file or is not found verbatim.
"""
import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from fetch_text import fetch, to_text, norm, UA  # noqa: E402

D13A = "research/insight_v1/phase_D/D13a_laura_quotes_verified.json"
CASE_TXT = "competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt"

USED = """B1b-Q11 B8a-Q09 B8b-Q18 B8b-Q04 B8a-Q32 B8a-Q13 D13a-N01 D13a-N02 B8b-Q30 B8b-Q31 B8b-Q32 B8b-Q12 B8b-Q13
B8a-Q28 B2b-Q07 B8a-Q14 B8b-Q10 B8b-Q11 B8b-Q37 B8b-Q38 B8b-Q39 B8b-Q05 B8b-Q21 B8b-Q22 B8b-Q20 B8b-Q26
B8a-Q04 B8b-Q35 B8a-Q18 B8a-Q19 B9b-Q09 B9b-Q10 B9b-Q11 B9b-Q01 B9b-Q02 B8a-Q37 B2b-Q08 B3b-Q13 B8b-Q06 B8a-Q34
B8a-Q33 B8b-Q41 B2b-Q10 B8a-Q03 B8b-Q14 B8b-Q07 B8b-Q17 B9b-Q12 B9b-Q06 B8b-Q08""".split()

OA = "https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid"
DP16 = "https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a"
PQ = "https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/"
PS = "https://pulsespikes.org/story/laura-gao"
LNM = "https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/"
HUF = "https://www.huffpost.com/entry/chinese-american-illustrator-life-in-wuhan_n_5ea9c739c5b63115cec2be5a"
INV = "https://www.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel"

CANDIDATES = {
    "D13c-C1": (OA, "I think for me, that took a lot of fear out of it."),
    "D13c-C2": (DP16, "My biggest advice is to be OK with the fact that your significant projects will never be finished. "
                      "It must constantly be sketched, erased, dropped in rain, ripped apart and sketched again."),
    "D13c-C3": (PQ, "After all, the Laura Gao I knew loved building apps, not excel models; perfected her artwork, not her "
                    "resume; and devoted herself to art galleries, not corporate coffee chats."),
    "D13c-C4": (PS, "And to my peers, who were like ‘why aren’t you going for McKinsey or Goldman Sachs instead of "
                    "wasting your time doing art,’ it seemed like a failure, too."),
    "D13c-C5": (LNM, "There’s a vibrant community of queer comic creators here in San Francisco, but why wasn’t there any "
                     "single event where we could celebrate that community and bring everyone together?"),
    "D13c-C6": (HUF, "When we discuss COVID and how it connects with Chinese or Wuhanese people, we have to be mindful of "
                     "how our perspective may negatively bias us against people from that region, and instead, focus on "
                     "the full human story."),
    "D13c-C7": (PS, "mainly because I’m so interested in them and I don’t want to pigeon-hole myself into one thing."),
    "D13c-C8": (PS, "[I shared an anti-resume] mainly because I started off in business school, and then I ended up "
                    "gravitating towards other things,"),
    # Facts from her 2018 questionnaire list (professional record, not value quotes):
    "D13c-F1": (PQ, "Trading Intern at Belvedere Trading in Chicago"),
    "D13c-F2": (PQ, "Policy Analyst Intern at Consumer Financial Protection Bureau"),
    # Reporter sentence Phase B used as her decision rule (checked so the map can say exactly what it is):
    "D13c-R1": (INV, "So when she got the book deal with HarperCollins, she gave Twitter her notice."),
    # Reporter text on the festival (fact, not her words):
    "D13c-R2": (LNM, "remaining free for exhibitors and attendees"),
    # Paper's leading ellipsis on B8b-Q38 (exact form to quote):
    "D13c-P1": (LNM, "…Our No. 1 priority is to get as many diverse voices and stories in the room as possible"),
}

CASE_LINES = [
    "Laura Gao believes stories have the power to change how people see the world.",
    "she has combined artistic passion with strategic thinking and a willingness to pursue unconventional opportunities.",
    "Laura has no shortage of ideas for the future.",
    "Although she has been willing to take thoughtful risks throughout her entrepreneurial career, she wants her "
    "investment team to recommend an appropriate balance between pursuing growth and protecting the capital required "
    "for her goals.",
    "She recognizes that committing all remaining assets could limit her financial flexibility as the project develops.",
    "If Laura promises more than she can ultimately contribute, she could damage her credibility and lose the confidence "
    "or participation of co-sponsors.",
    "Originally intended as a response to misinformation and anti-Asian racism",
    "The only person who needs to believe in something is yourself.",
]


def fresh(url, tmp):
    """Download a fresh copy (outside the repo). Returns (raw bytes, how)."""
    os.makedirs(tmp, exist_ok=True)
    path = os.path.join(tmp, "d13c_" + hashlib.sha1(url.encode()).hexdigest())
    for label, ua in (("fresh-curl-default-UA", None), ("fresh-helper-UA", UA)):
        cmd = ["curl", "-sSL", "-m", "40", "-o", path, "-w", "%{http_code}", url]
        if ua:
            cmd[1:1] = ["-A", ua]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip().startswith("2") and os.path.getsize(path) > 2000:
            return open(path, "rb").read(), label
    try:
        return fetch(url), "helper-cache (fresh fetch failed)"
    except SystemExit as e:
        return None, f"FAILED: {e}"


def main():
    tmp = sys.argv[sys.argv.index("--tmp") + 1] if "--tmp" in sys.argv else "/tmp/d13c_fresh_pages"
    d13a = {r["id"]: r for r in json.load(open(D13A, encoding="utf-8"))}
    pages, rows, bad = {}, [], 0

    def page_text(url):
        if url not in pages:
            raw, how = fresh(url, tmp)
            pages[url] = (norm(to_text(raw)) if raw else None, how)
        return pages[url]

    for qid in USED:
        rec = d13a.get(qid)
        if rec is None:
            rows.append((qid, "NOT IN D13a", "-", "-")); bad += 1; continue
        status = rec["status"]
        text, how = page_text(rec["url"])
        found = bool(text) and norm(rec["exact_text"]).strip() in text
        ok = status == "VERIFIED-PRIMARY" and found
        bad += 0 if ok else 1
        rows.append((qid, status, "YES" if found else "NO", how))
    print("USED QUOTES (must be D13a VERIFIED-PRIMARY and verbatim on a fresh copy)")
    for r in rows:
        print("  %-9s | %-21s | verbatim %-3s | %s" % r)
    print(f"  -> {len(rows) - bad} of {len(rows)} pass")

    print("\nCANDIDATES AND FACTS (not in D13a's register; wording check only)")
    for cid, (url, phrase) in CANDIDATES.items():
        text, how = page_text(url)
        found = bool(text) and norm(phrase).strip() in text
        print("  %-8s | verbatim %-3s | %s | %s" % (cid, "YES" if found else "NO", how, url))

    case = norm(open(CASE_TXT, encoding="utf-8").read())
    print("\nCASE LINES (VERIFIED-REPO-FILE check)")
    for line in CASE_LINES:
        print("  %-3s | %s" % ("YES" if norm(line) in case else "NO", line[:90]))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
