"""Build the Keel Office dashboard data (office.json) from the repo.

Every Keel run calls this at the end, then uploads office.json to the Keel Office dashboard
(https://claude.ai/artifact/NTBamRzChW4niBLYpkm19M). Steps: keel/office/dashboard/README.md.

Sources (all in the repo, so git is the one truth and no run can overwrite another's state):
  rooms        "## Now" block at the top of each room file (ROOMS below)
  members      the newest labelled take ("- **Jun:** ...") in keel/office/outbox/ and keel/pm/STANDUP.md
  projects     keel/pm/PROJECTS.md table
  changes      keel/pm/CHANGES.md table (what changed in a judge-facing draft)
  asks         keel/pm/ASK_HUMANS.md table (questions for Caplet, each with Keel's default)
  instructions keel/INSTRUCTIONS.md table (Caplet's standing instructions and whether Keel applies them)

Run: python3 keel/office/dashboard/build_data.py   (writes keel/office/dashboard/office.json)
"""
import datetime as dt
import json
import pathlib
import re
import sys
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parents[3]
KEEL = ROOT / "keel"
OUT = pathlib.Path(__file__).with_name("office.json")
SYD = ZoneInfo("Australia/Sydney")

# id, name, room file, who sits there, schedule label, cadence in days (for "ran on time")
ROOMS = [
    ("noticeboard", "The Noticeboard", "rooms/noticeboard.md", "Nora", "daily 07:00 (morning brief)", 1),
    ("window", "The Window", "rooms/window.md", "Felix", "daily 08:40", 1),
    ("trading_desk", "The Trading Desk", "rooms/trading_desk.md", "Jun, Kai, Felix", "Tue-Sat 10:30", 3),
    ("library", "The Library", "rooms/library.md", "Felix, Kai", "daily 12:10", 1),
    ("genius_lab", "The Genius Lab", "rooms/lab.md", "Jun, Kai", "daily 13:40", 1),
    ("lauras_room", "Laura's Room", "rooms/lauras_room.md", "Amara", "daily 15:10", 1),
    ("writing_room", "The Writing Room", "rooms/writing_room.md", "Tess, Amara", "daily 16:20", 1),
    ("courtroom", "The Courtroom", "rooms/courtroom.md", "Kai, Nora", "odd dates 18:20", 2),
    ("long_room", "The Long Room", "rooms/long_room.md", "all six (Nora chairs)", "even dates 18:20", 2),
    ("archive", "The Archive", "rooms/archive.md", "Tess", "daily 19:10 (merges the day)", 1),
    ("kitchen", "The Kitchen", "rooms/kitchen.md", "everyone, off duty", "odd dates 20:20", 2),
    ("rooftop", "The Rooftop", "rooms/rooftop.md", "Tess hosts, everyone", "even dates 20:20", 2),
]

MEMBERS = [
    ("nora", "Nora", "Leads the team; chairs the Long Room; writes the morning brief", "The Noticeboard"),
    ("felix", "Felix", "Rules and facts; librarian", "The Window"),
    ("jun", "Jun", "Numbers and models", "The Genius Lab"),
    ("kai", "Kai", "Challenger; trades and reads widely", "The Trading Desk"),
    ("amara", "Amara", "The client and the case", "Laura's Room"),
    ("tess", "Tess", "Writing and records", "The Writing Room"),
]

STATE_KEYS = {"doing": "doing", "decided": "decided", "next": "next",
              "for the judges": "for_judges", "updated": "updated"}


def clean(s):
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*([^*]*)\*\*", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return s.strip()


def read(rel):
    p = KEEL / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def now_block(text):
    """Bullets under the '## Now' heading: '- **Doing:** ...'."""
    out = {}
    m = re.search(r"^## Now\b.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return out
    key = None
    for line in m.group(1).splitlines():
        b = re.match(r"\s*-\s*\*\*([^*:]+):\*\*\s*(.*)", line)
        if b and b.group(1).strip().lower() in STATE_KEYS:
            key = STATE_KEYS[b.group(1).strip().lower()]
            out[key] = b.group(2).strip()
        elif key and line.startswith("  ") and line.strip():
            out[key] += " " + line.strip()
        else:
            key = None
    return {k: clean(v) for k, v in out.items()}


def table(text, first_header):
    """Rows of the first markdown table whose header starts with first_header."""
    rows, header, on = [], None, False
    for line in text.splitlines():
        if line.startswith("|") and not on:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and cells[0].lower().startswith(first_header.lower()):
                header, on = cells, True
            continue
        if on:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(dict(zip(header, [clean(c) for c in cells])))
    return rows


def parse_updated(s):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", s or "")
    if m:
        return dt.date.fromisoformat(m.group(1))
    m = re.search(r"(\d{1,2}) (Oct|Nov|Dec)", s or "")
    if m:
        month = {"Oct": 10, "Nov": 11, "Dec": 12}[m.group(2)]
        return dt.date(2026, month, int(m.group(1)))
    return None


def latest_takes():
    files = sorted((KEEL / "office/outbox").glob("*.md"), reverse=True)
    takes = {}
    sources = [(f, f.read_text(encoding="utf-8")) for f in files]
    standup = read("pm/STANDUP.md")
    if standup:
        sources.insert(0, (KEEL / "pm/STANDUP.md", standup.split("\n## ", 2)[0] + "\n" +
                           "\n".join(standup.split("\n## ")[1:2])))
    for f, text in sources:
        date = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        for name in [m[1] for m in MEMBERS]:
            if name in takes:
                continue
            m = re.search(rf"^\s*-?\s*\*\*{name}:\*\*\s*(.+?)(?=\n\s*-?\s*\*\*[A-Z][a-z]+:\*\*|\n\n|\Z)", text, re.M | re.S)
            if m:
                takes[name] = (clean(" ".join(m.group(1).split())),
                               date.group(1) if date else "latest brief", f.relative_to(ROOT).as_posix())
    return takes


def main():
    today = dt.datetime.now(SYD).date()
    rows = []
    ran = due = 0
    for rid, name, rel, who, sched, cadence in ROOMS:
        st = now_block(read(rel))
        upd = parse_updated(st.get("updated"))
        age = (today - upd).days if upd else None
        fresh = age is not None and age <= cadence
        due += 1
        ran += bool(fresh)
        rows.append({"kind": "room", "id": f"room-{rid}", "name": name, "who": who, "schedule": sched,
                     "doing": st.get("doing", "—"), "decided": st.get("decided", "—"),
                     "next": st.get("next", "—"), "for_judges": st.get("for_judges", "—"),
                     "updated": st.get("updated", "never"),
                     "health": "on time" if fresh else ("late" if upd else "no update yet"),
                     "file": f"keel/{rel}"})
    takes = latest_takes()
    for mid, name, role, home in MEMBERS:
        t = takes.get(name, ("—", "", ""))
        rows.append({"kind": "member", "id": f"member-{mid}", "name": name, "role": role, "home": home,
                     "take": t[0], "take_date": t[1], "file": t[2]})
    for r in table(read("pm/PROJECTS.md"), "ID"):
        rows.append({"kind": "project", "id": f"project-{r.get('ID')}", "name": r.get("Project", ""),
                     "owner": r.get("Owner", ""), "for_judges": r.get("Changes for the judges", ""),
                     "due": r.get("Due (Sydney)", ""), "status": r.get("Status", ""),
                     "next": r.get("Next step", "")})
    for i, r in enumerate(table(read("pm/CHANGES.md"), "Date")):
        rows.append({"kind": "change", "id": f"change-{i + 1}", "date": r.get("Date", ""),
                     "deliverable": r.get("Deliverable", ""), "name": r.get("What changed", ""),
                     "owner": r.get("Room", ""), "file": r.get("Where", "")})
    for i, r in enumerate(table(read("pm/ASK_HUMANS.md"), "Asked")):
        answered = bool(r.get("Answer (student, date)", "").strip())
        rows.append({"kind": "ask", "id": f"ask-{i + 1}", "date": r.get("Asked (Sydney)", ""),
                     "owner": r.get("Room", ""), "name": r.get("Question", ""),
                     "default": r.get("Keel's default if no answer", ""), "due": r.get("By", ""),
                     "status": "answered" if answered else "open: Keel goes ahead with the default",
                     "answer": r.get("Answer (student, date)", "")})
    for r in table(read("INSTRUCTIONS.md"), "#"):
        rows.append({"kind": "instruction", "id": f"instr-{r.get('#')}", "date": r.get("Date", ""),
                     "name": r.get("Instruction (Caplet's words, short)", ""), "status": r.get("Status", ""),
                     "evidence": r.get("Evidence (26 Oct)", ""), "file": r.get("Now enforced in", "")})
    stamp = dt.datetime.now(SYD).strftime("%a %d %b %Y, %H:%M Sydney")
    by = sys.argv[1] if len(sys.argv) > 1 else "a Keel run"
    rows.insert(0, {"kind": "meta", "id": "meta", "name": "Keel Office", "updated": stamp, "owner": by,
                    "health": f"{ran} of {due} rooms on time", "date": today.isoformat()})
    OUT.write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(rows)} rows; {ran} of {due} rooms on time")


if __name__ == "__main__":
    main()
