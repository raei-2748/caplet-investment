"""Build Keel's daily digest: what the six discussed, read and ticked off, one Sydney day per file.

Why (Ray, 27 Oct 2026): "I cannot really see the dialogues you guys had ... the research you guys have done ... the
to-do list you have crossed off ... there's no summary or list of things you guys done today." This script reads the
huddles (keel/huddles/<YYYY-MM-DD>_<slug>/) and the run log and writes, for each day:

  keel/today/<YYYY-MM-DD>.md  the day in plain words, for a person
  keel/today/feed.json        every day, newest first, for the portal's "Today" page

It never overwrites a day file's "## In plain words" section (rooms append one line there per finished job); it only
replaces the part between the GENERATED markers. It also writes each huddle's to-do counts back into its huddle.json
and rebuilds keel/huddles/INDEX.md. Re-running it is safe.

Usage (repo root):  python3 keel/scripts/build_today.py            (all days)
                    python3 keel/scripts/build_today.py --check    (validate huddle folders, write nothing)
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KEEL = ROOT / "keel"
HUDDLES = KEEL / "huddles"
TODAY = KEEL / "today"
RUNLOG = KEEL / "pm" / "RUNLOG.md"
START, END = "<!-- GENERATED: build_today.py (do not edit below) -->", "<!-- /GENERATED -->"
PLAIN = "## In plain words"
MONTHS = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
TODO_RE = re.compile(r"^\s*[-*] \[( |x|X)\] (.+)$")
DONE_ON = re.compile(r"done (?:\w{3} )?(\d{1,2}) (\w{3})")


def rel(p):
    return p.relative_to(ROOT).as_posix()


def title_of(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return re.sub(r"^#\s+(FICTION\.\s*)?", "", line).strip()
    return path.stem


def day_from(text, year=2026):
    """'Tue 27 Oct 12:55' or '27 Oct' -> '2026-10-27'."""
    m = re.search(r"(\d{1,2}) (\w{3})", text)
    if not m or m.group(2) not in MONTHS:
        return None
    return date(year, MONTHS[m.group(2)], int(m.group(1))).isoformat()


def todos(folder, fallback_day):
    f = folder / "todo.md"
    out = []
    if not f.exists():
        return out
    for line in f.read_text(encoding="utf-8").splitlines():
        m = TODO_RE.match(line)
        if not m:
            continue
        done, text = m.group(1).lower() == "x", m.group(2).strip()
        owner = re.search(r"\(([A-Z][a-z]+)[;,)]", text)
        when = DONE_ON.search(text)
        day = date(2026, MONTHS[when.group(2)], int(when.group(1))).isoformat() if done and when and when.group(2) in MONTHS else (fallback_day if done else None)
        out.append({"text": text, "done": done, "owner": owner.group(1) if owner else None, "day": day})
    return out


POST_HEAD = re.compile(r"^\*\*([A-Z][a-z]+)\*\*\s*\(([^)]*)\)\s*$")


def speaker_post(text):
    """'**Nora** (round 1)' + body -> '**Nora (round 1):** first paragraph' + the rest, so the portal's chat view
    (build_portal.py dialogue()) shows each post's opening as a line of conversation."""
    text = text.strip()
    first, _, rest = text.partition("\n")
    m = POST_HEAD.match(first.strip())
    if not m:
        return text
    paras = rest.strip().split("\n\n", 1)
    head = f"**{m.group(1)} ({m.group(2)}):** " + paras[0].strip()
    return head + ("\n\n" + paras[1].strip() if len(paras) > 1 else "")


def write_transcript(folder, h):
    """transcript.md is derived: the question, then every post in round order, then the close. Never edit it by hand;
    edit the posts (or chair.md, the chair's own notes between rounds, headed '## Round N')."""
    order = {m.lower(): i for i, m in enumerate(h.get("members", []))}
    chair = {}
    if (folder / "chair.md").exists():
        parts = re.split(r"(?m)^## Round (\d+)[^\n]*\n", (folder / "chair.md").read_text(encoding="utf-8"))
        chair = {int(parts[i]): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}
    L = [f"# FICTION. {h['id']} {h['title']}: the conversation", "",
         f"> Built from the posts by `keel/scripts/build_today.py`. Keel is a simulated team, AI-written; each member "
         f"was played by its own agent, reading the others' posts. Brief: [BRIEF.md](BRIEF.md).", "",
         f"**The question.** {h['question']}", ""]
    if h.get("essence"):
        L += ["**The essence.** " + " ".join(h["essence"]), ""]
    for r in h.get("rounds", []):
        n = r["n"]
        L += [f"## Round {n}: {r.get('name', '')} ({r.get('date', '')})", ""]
        if chair.get(n):
            L += [chair[n], ""]
        posts = sorted(folder.glob(f"posts/r{n}_*.md"), key=lambda p: order.get(p.stem.split("_", 1)[1], 99))
        for p in posts:
            L += [speaker_post(p.read_text(encoding="utf-8")), ""]
            name = p.stem.split("_", 1)[1]
            notes = sorted(folder.glob(f"research/{name}{'' if n == 1 else f'_r{n}'}.md"))
            if notes:
                L += [f"*{name.title()}'s research: [{notes[0].name}](research/{notes[0].name})*", ""]
    if h.get("decided"):
        L += ["## What we decided", ""] + [f"- {d}" for d in h["decided"]] + [""]
    if h.get("seeds"):
        L += ["## Still open (seeds for the next huddle)", ""] + [f"- {d}" for d in h["seeds"]] + [""]
    (folder / "transcript.md").write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")


def load_huddles(check=False):
    hs, problems = [], []
    for folder in sorted(p for p in HUDDLES.glob("20*_*") if p.is_dir()):
        meta = folder / "huddle.json"
        if not meta.exists():
            problems.append(f"{rel(folder)}: no huddle.json")
            continue
        h = json.loads(meta.read_text(encoding="utf-8"))
        for key in ("id", "title", "question", "opened", "status", "members", "rounds", "essence"):
            if key not in h:
                problems.append(f"{rel(meta)}: missing '{key}'")
        h["path"] = rel(folder)
        if isinstance(h["rounds"], int):  # legacy card (H-002, H-003): a count, hand-written transcript kept
            h["rounds"] = [{"n": n, "date": h.get("opened")} for n in range(1, h["rounds"] + 1)]
        elif not check:
            write_transcript(folder, h)
        h["transcript"] = rel(folder / "transcript.md") if (folder / "transcript.md").exists() else None
        h["research_notes"] = [{"path": rel(p), "title": title_of(p), "member": p.stem.split("_")[0].title()}
                               for p in sorted((folder / "research").glob("*.md"))]
        h["todo_items"] = todos(folder, h.get("closed") or h.get("opened"))
        h["todos"] = {"done": sum(t["done"] for t in h["todo_items"]), "total": len(h["todo_items"])}
        h["days"] = sorted({r.get("date") for r in h.get("rounds", []) if r.get("date")} | {h.get("opened")} | ({h["closed"]} if h.get("closed") else set()))
        hs.append(h)
        if not check:
            on_disk = json.loads(meta.read_text(encoding="utf-8"))
            if on_disk.get("todos") != h["todos"]:
                on_disk["todos"] = h["todos"]
                meta.write_text(json.dumps(on_disk, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return hs, problems


def runs():
    if not RUNLOG.exists():
        return []
    out = []
    for line in RUNLOG.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not re.match(r"\w{3} \d{1,2} \w{3}", cells[0]):
            continue
        out.append({"day": day_from(cells[0]), "when": cells[0], "room": cells[1],
                    "what": re.sub(r":\s*`[^`]+`\s*$", "", cells[2])})
    return out


def build(hs, rs):
    days = sorted({d for h in hs for d in h["days"]} | {r["day"] for r in rs if r["day"]}, reverse=True)
    feed = []
    for d in days:
        today = [h for h in hs if d in h["days"]]
        entry = {
            "date": d,
            "weekday": datetime.fromisoformat(d).strftime("%a"),
            "essence": [s for h in today for s in h["essence"]],
            "huddles": [{k: h.get(k) for k in ("id", "title", "question", "status", "room", "chair", "members", "essence",
                                               "decided", "seeds", "todos", "path", "transcript", "changes")}
                        | {"rounds": len(h["rounds"]), "rounds_today": sum(1 for r in h["rounds"] if r.get("date") == d)}
                        for h in today],
            "research": [n | {"huddle": h["id"]} for h in today for n in h["research_notes"]],
            "done": [t | {"huddle": h["id"]} for h in hs for t in h["todo_items"] if t["done"] and t["day"] == d],
            "open": [t | {"huddle": h["id"]} for h in today for t in h["todo_items"] if not t["done"]],
            "runs": [r for r in rs if r["day"] == d],
        }
        feed.append(entry)
    return feed


def day_markdown(e):
    """Short on purpose: the portal's Today page already shows research and room runs. This block adds only the
    day's conversations (with their essence) and the to-dos ticked or still open."""
    nice = datetime.fromisoformat(e["date"]).strftime("%a %-d %b %Y")
    L = []
    if e["huddles"]:
        L += ["## Conversations (huddles)", ""]
        for h in e["huddles"]:
            link = f"../{h['transcript'].split('keel/', 1)[1]}" if h.get("transcript") else f"../{h['path'].split('keel/', 1)[1]}/"
            L.append(f"- **{h['title']}** ({', '.join(h['members'])}; {h['rounds']} rounds, {h['status']}): "
                     f"{' '.join(h['essence']) or 'still going.'} ([the conversation]({link}))")
        L.append("")
    if e["done"] or e["open"]:
        L += ["## To-do from the conversations", ""] + [f"- [x] {t['text']}" for t in e["done"]] + [f"- [ ] {t['text']}" for t in e["open"]] + [""]
    return nice, "\n".join(L).rstrip() + "\n"


def write_day(e):
    nice, body = day_markdown(e)
    f = TODAY / f"{e['date']}.md"
    head = (f"# {nice}: what Keel did today\n\nAI-generated by the Keel Office (Claude Code); Keel is a simulated team. "
            f"Plain words for Caplet, not for submission.\n\n## For Caplet\n\n{PLAIN}\n\n")
    old = f.read_text(encoding="utf-8") if f.exists() else head
    if PLAIN not in old:
        old = old.rstrip() + f"\n\n{PLAIN}\n\n"
    if START in old:
        pre, rest = old.split(START, 1)
        post = rest.split(END, 1)[1] if END in rest else ""
    else:
        pre, post = old.rstrip() + "\n\n", ""
    f.write_text(f"{pre.rstrip()}\n\n{START}\n\n{body}\n{END}\n{post.lstrip()}", encoding="utf-8")


def write_index(hs):
    rows = ["# FICTION. Keel's huddles (every multi-round discussion, newest first)", "",
            "> Built by `../scripts/build_today.py`; do not edit by hand. How a huddle works: `README.md`.", "",
            "| ID | Opened | Title | Status | Rounds | Members | To-dos | Essence |", "|---|---|---|---|---|---|---|---|"]
    for h in sorted(hs, key=lambda h: (h["opened"], h["id"]), reverse=True):
        folder = h["path"].split("keel/huddles/", 1)[1]
        rows.append(f"| {h['id']} | {h['opened']} | [{h['title']}]({folder}/transcript.md) | {h['status']} | "
                    f"{len(h['rounds'])} | {', '.join(h['members'])} | {h['todos']['done']}/{h['todos']['total']} | "
                    f"{' '.join(h['essence'])[:220]} |")
    seeds = [(h["id"], s) for h in hs for s in h.get("seeds") or []]
    if seeds:
        rows += ["", "## Open seeds (the next huddle starts from one of these)", ""] + [f"- {i}: {s}" for i, s in seeds]
    (HUDDLES / "INDEX.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def main():
    check = "--check" in sys.argv
    hs, problems = load_huddles(check)
    for p in problems:
        print("PROBLEM:", p)
    if check:
        print(f"{len(hs)} huddles checked")
        return 1 if problems else 0
    feed = build(hs, runs())
    TODAY.mkdir(exist_ok=True)
    for e in feed:
        if e["huddles"]:
            write_day(e)
    (TODAY / "feed.json").write_text(json.dumps({"built": datetime.now().isoformat(timespec="minutes"), "days": feed},
                                                indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    write_index(hs)
    print(f"{len(hs)} huddles, {len(feed)} days -> keel/today/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
