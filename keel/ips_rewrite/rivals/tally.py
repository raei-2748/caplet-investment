"""AI-generated (Claude Code), 27 Oct 2026. Counts how many simulated rival IPSs (A*.md = raw AI, H*.md = human
archetypes) make each move, by keyword. Crude on purpose: a hit means the words are there, not that the idea is used
well. Run: python3 keel/ips_rewrite/rivals/tally.py   (writes tally.json next to it)"""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
F = {
 "ladder/matched Treasuries for the payments": r"ladder|matur\w+ (?:just |shortly )?before each|one (?:bond|rung|matur\w*) (?:per|for each)",
 "held to maturity": r"held to maturity|hold (?:each|every|them|it)? ?(?:bond )?to maturity",
 "2028 deposit completes the ladder first": r"2028 (?:deposit|contribution)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,60}(?:complet|finish|fill|first claim|top)",
 "stocks stepped DOWN toward 2031-33 (glide/reef/harvest/lock gains)": r"glide|reef|step(?:s|ped)? ?down|de-?risk|harvest|shift\w* (?:from|toward)|move\w* (?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,40}into (?:short|Treasur)|lock\w* (?:in )?(?:gains|a meaningful)|ink the pencil",
 "range bottom = secured/locked amount": r"(?:bottom|low end|floor|minimum)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,80}(?:lock|secur|Treasur|inked|guarant|already)",
 "keeps part of the surplus as flexibility": r"flexib\w+ (?:buffer|cushion|fund|reserve)|keep(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,40}(?:portion|part|share|third|meaningful)|white space|not all of it|never commits the last|breathing room",
 "certainty = only US default risk left": r"(?:only|remaining)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,40}(?:default|government (?:failing|itself))|default(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,30}only",
 "inflation hits facility costs, not the fixed payments": r"inflation(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,120}(?:facility|construction|pricier)|(?:fixed|nominal)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,80}inflation",
 "coupon reinvestment named": r"coupon",
 "longest-dated / most distant payments first": r"(?:most distant|longest|latest)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,30}(?:first|payments)",
 "her income moves with markets (human capital)": r"(?:income|advances|royalt|speaking)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,120}(?:recession|slump|downturn|same time|fall together|correlat)",
 "defined-maturity iBond funds": r"iBond|IBT[A-Z]|defined[- ]maturity",
 "one global fund (VT)": r"\bVT\b|Total World",
 "a probability for the payments (e.g. 95%)": r"\b9\d(?:\.\d)?\s?%|\b9\d in 100",
 "contribution capped at the top of the range": r"capped|cap(?:s)? (?:at|the)|never (?:above|more than) the top",
 "over- vs under-promising costs weighed": r"(?:over-?promis|promis\w+ more)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,120}(?:under|too little|less|shrug)|asymmetr",
 "sequence-of-returns risk": r"sequence",
 "funding ratio / funded status": r"fund(?:ing|ed) (?:ratio|status)",
 "a metaphor or motif frames the plan": r"\b(?:sailboat|ballast|sail|anchor|lantern|foundation|garden|roots?|wings|pencil|ink|bridge|pillars|seasons|acts?|panel|chapter|runway|pots?|bucket)\b",
 "'promise' in the name or pitch": None,
 "Laura's credibility with co-sponsors": r"credib",
 "annual review / rebalance": r"(?:annual|each|every) (?:review|January|year)(?:[^.]|\.(?=\S)|(?<=[A-Z])\.){0,40}(?:review|rebalanc|check)|rebalanc",
}
rows = {}
files = sorted(HERE.glob("[AH][0-9][0-9].md"))
for f in files:
    t = f.read_text(encoding="utf-8")
    ips = t.split("## SIMULATOR NOTES")[0]
    head = ips.split("## IPS")[0]
    rows[f.stem] = {k: bool(re.search(r"promise", head, re.I)) if v is None else bool(re.search(v, ips, re.I)) for k, v in F.items()}
out = {"n": len(files), "ai": sum(1 for f in files if f.stem[0] == "A"), "human": sum(1 for f in files if f.stem[0] == "H"),
       "counts": {k: {"all": sum(r[k] for r in rows.values()), "ai": sum(r[k] for s, r in rows.items() if s[0] == "A"),
                      "human": sum(r[k] for s, r in rows.items() if s[0] == "H")} for k in F},
       "by_rival": rows}
(HERE / "tally.json").write_text(json.dumps(out, indent=1))
for k, v in out["counts"].items():
    print(f'{v["all"]:>3}/{out["n"]}  AI {v["ai"]:>2}/{out["ai"]}  human {v["human"]:>2}/{out["human"]}  {k}')
