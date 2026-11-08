#!/usr/bin/env python3
"""Build the Final Report insight store from the harvest tables and the rating overrides.

Inputs
  ../harvest/H*.md          one table row per idea (format in ../HARVEST_BRIEF.md)
  ../cards/*.md             (later) new research cards, same table format
  ratings.csv               judgement overrides: id,F,R,S,C,status,merged_into,note
Outputs
  insights.jsonl            every idea, with its ratings and score (nothing is ever dropped)
  by_tag/<TAG>.md           every idea under each tag, ranked
  ../INSIGHT_STORE.md       how the store works, counts, the top of each tag

Ratings, each 1-5:
  F  fit: how much it explains or tests a decision in Caplet's IPS, or answers something the case asks
  R  rarity: 1 textbook, 3 known to practitioners, 5 niche or from another field
  S  source: 5 verified at source, 3 partly or our own model, 2 unverified, 1 no source or shown false
  C  clarity: how plainly it can be said to a smart reader
Score = 2F + R + S + C (max 25). The first pass sets F from the clash column and C at 3; ratings.csv holds the
judgement passes that replace them. Status: keep, adapt (clash to fix), refuse (kept for the record), merged.
"""
import csv, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent
SOURCES = sorted((RESEARCH / "harvest").glob("H*.md")) + sorted((RESEARCH / "cards").glob("*.md"))
ROW = re.compile(r"^\|\s*(\d+)\s*\|")

TAG_ORDER = ["CAREER", "CERTAINTY", "LADDER", "COMPLETE2028", "FLOOR", "CEILING", "HALFKEPT", "MOVE2031",
             "RESERVE2033", "TWOREASONS", "COSPONSOR", "FUNDRAISING", "RESIDENCY", "INFLATION_TWD", "REINVEST",
             "LAURA", "PROCESS", "PRESENTATION", "OTHER"]
TAG_NAMES = {
    "CAREER": "Laura's career as an unsellable stock", "CERTAINTY": "A high degree of certainty",
    "LADDER": "The ten Treasuries", "COMPLETE2028": "The 2028 deposit completes the ladder",
    "FLOOR": "The 2032 Treasury fund (bottom of the range)", "CEILING": "VT (top of the range)",
    "HALFKEPT": "Half the shares promised to no one", "MOVE2031": "The move into Treasuries before 2031",
    "RESERVE2033": "The operating reserve from 2033", "TWOREASONS": "Only two reasons to change",
    "COSPONSOR": "The 2031 range and the co-sponsors", "FUNDRAISING": "The fundraising text",
    "RESIDENCY": "The residency itself", "INFLATION_TWD": "Inflation, Taiwan costs, the Taiwan dollar",
    "REINVEST": "Reinvesting the ladder's interest", "LAURA": "Laura's working life and values",
    "PROCESS": "How the team decided and learned", "PRESENTATION": "How the report shows its work",
    "OTHER": "Other"}


def cells(line):
    parts = [p.strip() for p in line.rstrip().strip("|").split("|")]
    return parts


def rate_rarity(v):
    v = v.upper()
    if v.startswith("NICHE"):
        return 5
    if v.startswith("KNOWN"):
        return 3
    if v.startswith("TEXTBOOK"):
        return 1
    return 2


def rate_source(v):
    u = v.upper()
    if "CONFLICT" in u or "FALSE" in u or u.startswith("NO SOURCE"):
        return 1
    if re.search(r"(?<!UN)VERIFIED", u):
        return 3 if "PARTLY" in u or "PARTIAL" in u else 5
    if "MODEL" in u:
        return 3
    return 2


def rate_fit(clash, critique):
    c = clash.lower().strip()
    if re.search(r"\bbin(ned)?\b", critique.lower()):
        return 1
    if c.startswith("no"):
        return 4
    if "partly" in c or "imagery" in c or "partial" in c or "wording" in c:
        return 3
    if c.startswith("yes"):
        return 1
    return 3


def status_for(clash):
    c = clash.lower().strip()
    if c.startswith("no") or not c:
        return "keep"
    return "adapt"


def load_overrides():
    path = HERE / "ratings.csv"
    out = {}
    if path.exists():
        with path.open() as fh:
            for r in csv.DictReader(fh):
                out[r["id"].strip()] = r
    return out


def main():
    ideas = []
    for src in SOURCES:
        prefix = src.stem.split("_")[0]
        in_idea_table = False
        seen = set()
        for line in src.read_text().splitlines():
            if line.startswith("|") and not ROW.match(line):
                # a header or separator row: an idea table has an "Idea" column and at least ten columns
                if not set(line.replace("|", "").strip()) <= set("-: "):
                    in_idea_table = ("Idea" in line and len(cells(line)) >= 10)
                continue
            if not line.startswith("|"):
                if line.strip() == "" or line.startswith("#"):
                    pass
                continue
            m = ROW.match(line)
            if not m or not in_idea_table:
                continue
            if m.group(1) in seen:
                continue
            seen.add(m.group(1))
            c = cells(line)
            if len(c) < 10:
                c += [""] * (10 - len(c))
            num, idea, sources, tags, niche, use, critique, verified, clash, where = c[:10]
            tag_list = [t.strip().upper() for t in re.split(r"[,;/]", tags) if t.strip()]
            tag_list = [t for t in tag_list if re.fullmatch(r"[A-Z0-9_]+", t)] or ["OTHER"]
            ideas.append({
                "id": f"{prefix}-{int(num):03d}", "idea": idea, "sources": sources, "tags": tag_list,
                "niche": niche, "use": use, "critique": critique, "verified": verified, "clash": clash,
                "where": where, "file": str(src.relative_to(RESEARCH)),
                "F": rate_fit(clash, critique), "R": rate_rarity(niche), "S": rate_source(verified), "C": 3,
                "status": status_for(clash), "merged_into": "", "note": "", "rated_by": "first pass"})
    overrides = load_overrides()
    for it in ideas:
        o = overrides.get(it["id"])
        if not o:
            continue
        for k in ("F", "R", "S", "C"):
            if o.get(k, "").strip():
                it[k] = int(o[k])
        for k in ("status", "merged_into", "note"):
            if o.get(k, "").strip():
                it[k] = o[k].strip()
        it["rated_by"] = "judgement"
    for it in ideas:
        it["score"] = 2 * it["F"] + it["R"] + it["S"] + it["C"]
        it["tier"] = "A" if it["score"] >= 19 else ("B" if it["score"] >= 15 else "C")
        if it["status"] in ("refuse", "merged"):
            it["tier"] = "-"

    with (HERE / "insights.jsonl").open("w") as fh:
        for it in ideas:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    def short(s, n=160):
        s = s.replace("|", "/")
        return s if len(s) <= n else s[: n - 1] + "…"

    by_tag = HERE / "by_tag"
    by_tag.mkdir(exist_ok=True)
    live = [i for i in ideas if i["status"] not in ("merged",)]
    tags_present = [t for t in TAG_ORDER if any(t in i["tags"] for i in live)]
    extra = sorted({t for i in live for t in i["tags"]} - set(TAG_ORDER))
    for tag in tags_present + extra:
        rows = sorted([i for i in live if tag in i["tags"]], key=lambda i: (-i["score"], i["id"]))
        lines = [f"# {TAG_NAMES.get(tag, tag)} ({tag}): {len(rows)} ideas, ranked", "",
                 "Built by `../build_store.py`; do not edit by hand (change `../ratings.csv` instead). Full rows are in "
                 "`../insights.jsonl` and in the harvest file named in each row.", "",
                 "| Rank | Id | Score (F R S C) | Tier | Status | Idea | Sources | Clash |", "|---|---|---|---|---|---|---|---|"]
        for n, i in enumerate(rows, 1):
            lines.append(f"| {n} | {i['id']} | {i['score']} ({i['F']} {i['R']} {i['S']} {i['C']}) | {i['tier']} | "
                         f"{i['status']} | {short(i['idea'], 220)} | {short(i['sources'], 140)} | {short(i['clash'], 90)} |")
        (by_tag / f"{tag}.md").write_text("\n".join(lines) + "\n")

    # The front page
    total = len(ideas)
    counts = {t: sum(1 for i in live if t in i["tags"]) for t in tags_present + extra}
    tiers = {k: sum(1 for i in ideas if i["tier"] == k) for k in ("A", "B", "C", "-")}
    judged = sum(1 for i in ideas if i["rated_by"] == "judgement")
    adapt = sum(1 for i in ideas if i["status"] == "adapt")
    per_file = {}
    for i in ideas:
        per_file[i["file"]] = per_file.get(i["file"], 0) + 1
    out = ["# The insight store: every idea for the Final Report, ranked", "",
           "Caplet, Book 14: \"Keep a store of every single insight you have. They should be organised or categorised"
           " ... some kind of ranking or rating system ... You must not lose a thing.\" This page is the front door."
           " It is rebuilt by `store/build_store.py`; nothing is ever deleted, only ranked lower.", "",
           "## How it works", "",
           "- **Where ideas come from.** Every idea Keel found between 27 Sep and 6 Nov was gathered by eight readers into"
           " the harvest tables in `harvest/` (one row per idea, with sources, critique, whether it was checked, and"
           " whether it clashes with Caplet's FINAL IPS or the Trading Notes). New research from 8 Nov arrives as cards"
           " in `cards/` in the same format.",
           "- **How each idea is filed.** Under every part of Caplet's plan, or of the case, that it serves (the tags"
           " below). An idea can sit under several.",
           "- **How each idea is rated** (1 to 5 each): **F** fit (how much it explains or tests a decision in the IPS, or"
           " answers something the case asks; counted twice), **R** rarity (textbook 1, practitioners' 3, niche or from"
           " another field 5), **S** source (verified at source 5, our own model or partly checked 3, unverified 2, none"
           " or shown false 1), **C** clarity (how plainly it can be said). Score = 2F + R + S + C, out of 25. Tier A is"
           " 19 or more, B 15 to 18, C below 15.",
           "- **Status.** keep; adapt (the substance is good but a detail clashes with the FINAL IPS or the TNA, so it must"
           " be reframed before use); refuse (kept for the record, and as evidence of what we rejected and why);"
           " merged (a duplicate, pointing to the row that carries it).",
           "- **First pass, then judgement.** The first pass sets R and S from the harvest columns, F from the clash"
           " column, and C at 3. Judgement passes replace them, row by row, in `store/ratings.csv`; the build applies"
           " them and records which rows have been judged.", "",
           "## Where it stands", "",
           f"- **{total} ideas** in the store; {judged} judged so far, the rest on the first pass.",
           f"- Tiers: A {tiers['A']}, B {tiers['B']}, C {tiers['C']}; refused or merged {tiers['-']}.",
           f"- {adapt} ideas need reframing before use (they clash in some detail with the FINAL IPS or the TNA).",
           "- Rows per source: " + "; ".join(f"`{k}` {v}" for k, v in sorted(per_file.items())) + ".", "",
           "## The parts of the plan and the case", "", "| Tag | What it covers | Ideas | Ranked list |", "|---|---|---|---|"]
    for t in tags_present + extra:
        out.append(f"| {t} | {TAG_NAMES.get(t, t)} | {counts[t]} | [by_tag/{t}.md](store/by_tag/{t}.md) |")
    out += ["", "## The top 40 across the store (current ratings)", "",
            "| Rank | Id | Score | Tags | Idea | Status |", "|---|---|---|---|---|---|"]
    ranked = sorted([i for i in ideas if i["tier"] != "-"], key=lambda i: (-i["score"], i["id"]))
    for n, i in enumerate(ranked[:40], 1):
        out.append(f"| {n} | {i['id']} | {i['score']} | {', '.join(i['tags'])} | {short(i['idea'], 200)} | {i['status']} |")
    out += ["", "## The thinnest parts (fewest ideas rated B or better)", ""]
    thin = sorted(tags_present, key=lambda t: sum(1 for i in live if t in i["tags"] and i["tier"] in ("A", "B")))
    for t in thin[:8]:
        good = sum(1 for i in live if t in i["tags"] and i["tier"] in ("A", "B"))
        out.append(f"- {t} ({TAG_NAMES.get(t, t)}): {good} rated B or better, {counts[t]} in all.")
    (RESEARCH / "INSIGHT_STORE.md").write_text("\n".join(out) + "\n")
    print(f"{total} ideas; tiers {tiers}; judged {judged}; adapt {adapt}")


if __name__ == "__main__":
    sys.exit(main())
