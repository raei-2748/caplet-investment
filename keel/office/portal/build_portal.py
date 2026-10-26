"""Build the Keel Office portal (GitHub Pages) from the repo.

    python3 keel/office/portal/build_portal.py --out _site

Writes a one-page app: index.html, app.js, style.css (copied from this folder), data.js (window.KEEL, everything the
pages need) and d/<path>.html (every Keel markdown file rendered, fetched when someone opens it). Sources, all in the
repo so git stays the one truth:
  rooms, members, projects, changes, asks, instructions  keel/office/dashboard/build_data.py (the same parsers)
  IPS versions                                            keel/ips_rewrite/VERSIONS.md (+ the files it names)
  activity                                                git log of keel/ and keel/pm/RUNLOG.md
  memos, episodes, every other page                       keel/office/outbox/, keel/episodes/, keel/**/*.md
The workflow .github/workflows/keel-portal.yml merges the newest Keel day branch (and keel/office/portal/branches.txt)
into a scratch copy of main first, so a room's run shows within minutes, before the evening merge.
Needs: pip install markdown.
"""
import argparse
import datetime as dt
import html
import json
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
from zoneinfo import ZoneInfo

import markdown

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
KEEL = ROOT / "keel"
SYD = ZoneInfo("Australia/Sydney")
REPO = "https://github.com/raei-2748/caplet-investment"
sys.path.insert(0, str(HERE.parent / "dashboard"))
sys.path.insert(0, str(HERE.parent / "tools"))
import build_data as bd  # noqa: E402
import textcheck as tc  # noqa: E402

# id -> (runbook, work folders/files besides the room log)
ROOM_EXTRA = {
    "noticeboard": ("noticeboard.md", ["pm/STANDUP.md", "pm/BOARD.md"]),
    "window": ("window.md", []),
    "trading_desk": ("trading-desk.md", []),
    "library": ("library.md", ["rooms/library_S-01_candidates.md", "rooms/library_S-02_lab_facts.md"]),
    "genius_lab": ("genius-lab.md", ["rooms/lab/"]),
    "lauras_room": ("lauras-room.md", ["rooms/lauras_room/"]),
    "writing_room": ("writing-room.md", ["ips_rewrite/drafts/"]),
    "courtroom": ("courtroom.md", ["rooms/courtroom/"]),
    "long_room": ("long-room.md", ["rooms/long_room/", "meetings/"]),
    "archive": ("archive.md", []),
    "kitchen": ("kitchen.md", []),
    "rooftop": ("rooftop.md", ["drafts/rooftop_2026-10-26/"]),
}
# words in commit subjects, memo names and run-log rows -> room id (first match wins; longest names first)
ROOM_WORDS = [
    ("noticeboard", r"noticeboard|daily loop|morning brief|keel loop|stand-?up|nora"),
    ("trading_desk", r"trading desk|markets?( and rules)? check|trading-desk"),
    ("genius_lab", r"genius[ -]lab|\blab\b|SD-LAB"),
    ("lauras_room", r"laura'?s[ -]room|lauras-room|LR-0"),
    ("writing_room", r"writing[ -]room|SD-WR|WO-0003|rewrite"),
    ("long_room", r"long[ -]room|meeting|weekly plan|LR-2026"),
    ("courtroom", r"courtroom|mock judge"),
    ("window", r"window|fact[- ]check|SD-W0"),
    ("library", r"library|concept"),
    ("archive", r"archive|ledger|records"),
    ("kitchen", r"kitchen"),
    ("rooftop", r"rooftop"),
]
DEADLINES = [
    ("IPS due, trading locks", "2026-11-07T09:00:00+11:00", "Fri 6 Nov 5 pm ET"),
    ("Final Report instructions", "2026-11-10T09:00:00+11:00", "Mon 9 Nov 5 pm ET"),
    ("Final Report due", "2026-12-05T09:00:00+11:00", "Fri 4 Dec 5 pm ET"),
]
SKIP_DOCS = ("keel/library/assistant_review_2026-10/temporary_deposit/",)
# personal data never goes on a public page (CLAUDE.md): surnames' initials, account numbers, emails
SCRUB = [
    (re.compile(r"\b(Ray|Ahaan|Darren|Harry|Eric|Young|JinRui) [A-Z]\.(?=[\s|,;)'’]|$)"), r"\1"),
    (re.compile(r"Caplet-\d{6,}"), "Caplet-[account]"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "[email]"),
    (re.compile(r"(?im)^\**WInS Username:.*$"), ""),
]


def scrub(s):
    for rx, rep in SCRUB:
        s = rx.sub(rep, s)
    return s


def git(*args):
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def room_of(text):
    """The room named earliest in the text (a run's commit starts with its room: "Rooftop 26 Oct: ...")."""
    best = None
    for rid, rx in ROOM_WORDS:
        m = re.search(rx, text or "", re.I)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), rid)
    return best[1] if best else ""


# ---------- markdown pages ----------

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])


def title_of(text, path):
    for line in text.splitlines():
        if line.startswith("#"):
            return bd.clean(line.lstrip("#").strip())
    return pathlib.PurePosixPath(path).name


def render(text, path, known):
    """Markdown -> HTML; links to other Keel pages open inside the portal, other repo links go to GitHub."""
    MD.reset()
    body = MD.convert(scrub(text).replace("<", "&lt;"))

    def fix(m):
        href = html.unescape(m.group(1))
        if re.match(r"https?://", href, re.I):
            return f'href="{html.escape(href)}" target="_blank" rel="noopener"'
        if href.startswith("#") or re.match(r"mailto:", href, re.I):
            return m.group(0)
        if re.match(r"[a-z][a-z0-9+.-]*:", href.strip(), re.I):  # javascript:, data: and any other scheme
            return 'href="#" class="dead"'
        target, _, frag = href.partition("#")
        full = posixpath.normpath(posixpath.join(posixpath.dirname(path), target)) if target else path
        if full in known:
            return f'href="#/doc/{html.escape(full)}"'
        if full.startswith("/mnt/"):
            return 'href="#" class="dead" title="a shared project file, not in the repo"'
        return f'href="{REPO}/blob/main/{html.escape(full)}" target="_blank" rel="noopener"'

    body = re.sub(r'href="([^"]*)"', fix, body)
    return body


def collect_docs(out):
    files = [f for f in git("ls-files", "keel").splitlines() if f.endswith(".md")]
    if not files:  # not a git checkout
        files = [p.relative_to(ROOT).as_posix() for p in KEEL.rglob("*.md")]
    files = [f for f in files if (ROOT / f).exists() and not f.startswith(SKIP_DOCS)]
    known = set(files)
    docs = []
    for f in sorted(files):
        text = (ROOT / f).read_text(encoding="utf-8", errors="replace")
        dest = out / "d" / (f + ".html")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(text, f, known), encoding="utf-8")
        docs.append({"path": f, "title": scrub(title_of(text, f))[:160], "kb": round(len(text) / 1024, 1)})
    return docs, known


# ---------- IPS versions ----------

PITCH_RX = re.compile(r"^(investment strategy )?(elevator )?pitch\b|^elevator pitch\b", re.I)
IPS_RX = re.compile(r"^(ips\b|investment policy statement\b)", re.I)


def label_of(line):
    s = line.strip()
    if not s:
        return None
    if s.startswith("#") or (s.startswith("**") and s.rstrip(" :").endswith("**")) or len(s) < 40:
        return re.sub(r"[#*_]", "", s).strip()
    return None


def extract(path_spec, want):
    """Text of the pitch or the IPS from a registry cell (see keel/ips_rewrite/VERSIONS.md)."""
    if not path_spec:
        return ""
    rel, _, after = path_spec.strip("`").partition("#")
    p = ROOT / rel
    if not p.exists():
        return None
    lines = p.read_text(encoding="utf-8").splitlines()
    if after:
        start = next((i for i, l in enumerate(lines) if after in l), None)
        lines = lines[start + 1:] if start is not None else lines
    labels = [(i, label_of(l)) for i, l in enumerate(lines)]
    pi = next((i for i, lab in labels if lab and PITCH_RX.search(lab)), None)
    ii = next((i for i, lab in labels if lab and IPS_RX.search(lab) and (pi is None or i > pi)), None)
    if pi is None and ii is None:  # a bare text file
        body = [l for l in lines if not l.startswith((">", "# "))]
        if any(l.startswith("## ") for l in body):
            body = body[:next(i for i, l in enumerate(body) if l.startswith("## "))]
        return "" if want == "pitch" and rel.endswith(".md") else "\n".join(body).strip()
    if want == "pitch":
        if pi is None:
            return ""
        block = lines[pi + 1: ii if ii is not None else len(lines)]
    else:
        if ii is None:
            return ""
        block = []
        for l in lines[ii + 1:]:
            if l.startswith("#") or l.strip() in ("---", "***") or (l.startswith("**") and "".join(block).strip()):
                break
            block.append(l)
    text = "\n".join(block).strip()
    text = re.sub(r"\*\*|__", "", text)
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def ips_versions():
    rows = bd.table(bd.read("ips_rewrite/VERSIONS.md"), "V")
    out = []
    for r in rows:
        pitch = extract(r.get("Pitch", ""), "pitch")
        ips = extract(r.get("IPS", ""), "ips")
        missing = pitch is None or ips is None
        pitch, ips = scrub(pitch or ""), scrub(ips or "")
        v = tc.voice(ips) if ips else {}
        out.append({
            "n": int(r["V"]), "label": r.get("Version", ""), "date": r.get("Date (Sydney)", ""),
            "line": r.get("Line", ""), "note": r.get("What changed", ""),
            "pitch_src": r.get("Pitch", "").split("#")[0], "ips_src": r.get("IPS", "").split("#")[0],
            "pitch": pitch, "ips": ips, "missing": missing,
            "pitch_words": tc.words_strict(pitch) if pitch else 0, "ips_words": tc.words_strict(ips) if ips else 0,
            "sentences": v.get("sentences", 0), "mean_sentence": round(v.get("mean", 0), 1),
            "longest_sentence": v.get("longest", 0), "short_lines": v.get("blunt", 0),
            "paragraphs": v.get("paragraphs", 0),
        })
    return out


# ---------- activity ----------

def commits():
    fmt = "%x1e%H%x1f%cI%x1f%s"
    # every Keel branch, not just main: room runs commit to day branches, threads to their own branches
    log = git("log", "--no-merges", "--since=2026-09-20", f"--format={fmt}", "--name-only", "HEAD",
              "--remotes=origin/claude/*", "--", "keel")
    out = []
    for chunk in log.split("\x1e"):
        chunk = chunk.strip("\n")
        if not chunk.strip():
            continue
        head, _, files = chunk.partition("\n")
        parts = head.strip().split("\x1f")
        if len(parts) < 3:
            continue
        sha, when, subj = parts
        files = [f for f in files.splitlines() if f.strip()]
        rooms_touched = {room_of(f.replace("_", " ")) for f in files} - {""}
        rid = room_of(subj) or (rooms_touched.pop() if len(rooms_touched) == 1 else "")
        out.append({"sha": sha[:7], "at": when, "subject": scrub(subj)[:200], "room": rid, "files": len(files)})
    return out


def runlog():
    rows = bd.table(bd.read("pm/RUNLOG.md"), "Date")
    return [{"date": r.get("Date (Sydney)", ""), "room": r.get("Room", ""), "rid": room_of(r.get("Room", "")),
             "output": scrub(r.get("Output (link)", "")), "aim": r.get("Score aimed at", ""),
             "used_by": r.get("Used by (filled later)", "")} for r in rows]


def memos():
    out = []
    for f in sorted((KEEL / "office/outbox").glob("*.md"), reverse=True):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"(\d{4}-\d{2}-\d{2})_(.+)\.md", f.name)
        takes = []
        for name in [x[1] for x in bd.MEMBERS]:
            t = re.search(rf"^\s*-?\s*\*\*{name}:\*\*\s*(.+?)(?=\n\s*-?\s*\*\*[A-Z][a-z]+:\*\*|\n\n|\Z)", text, re.M | re.S)
            if t:
                takes.append({"name": name, "text": scrub(bd.clean(" ".join(t.group(1).split())))[:600]})
        out.append({"path": f.relative_to(ROOT).as_posix(), "date": m.group(1) if m else "",
                    "room": room_of(m.group(2).replace("-", " ") if m else f.name),
                    "title": scrub(title_of(text, f.name))[:200], "takes": takes})
    return out


def episodes():
    rows = []
    for line in bd.read("episodes/INDEX.md").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 8 and re.fullmatch(r"\d+", cells[0]):
            link = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cells[2])
            bp = re.match(r"(-?\d+)\s*bp", cells[7])
            rows.append({"ep": int(cells[0]), "date": cells[1], "title": link.group(1) if link else bd.clean(cells[2]),
                         "path": f"keel/episodes/{link.group(2)}" if link else "", "pov": cells[3],
                         "what": scrub(bd.clean(cells[5])), "milestone": bd.clean(cells[6]),
                         "headroom_bp": int(bp.group(1)) if bp else None})
    return rows


def cast():
    """Columns of keel/CAST.md's table, one dict per member."""
    rows = [l for l in bd.read("CAST.md").splitlines() if l.startswith("|")]
    if not rows:
        return {}
    head = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    out = {h.split()[0].lower(): {"full": bd.clean(h)} for h in head[1:] if h}
    for l in rows[2:]:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        key = bd.clean(cells[0]).split(" (")[0]
        if not key:
            continue
        for h, c in zip(head[1:], cells[1:]):
            if h:
                out[h.split()[0].lower()][key] = bd.clean(c)
    return out


def decisions(path):
    """Every '- **Decided:**' line a room has written into its Now block, newest first, from git history."""
    if not path:
        return []
    out, seen, when = [], set(), ""
    log = git("log", "--format=%x1e%cI", "-p", "HEAD", "--remotes=origin/claude/*", "--", path)
    for line in log.split("\n"):  # not splitlines(): it also splits on the \x1e record mark
        if line.startswith("\x1e"):
            when = dt.datetime.fromisoformat(line[1:].strip()).astimezone(SYD).strftime("%a %d %b")
        elif line.startswith("+- **Decided:**"):
            text = scrub(line.split("**Decided:**", 1)[1].strip())
            if text and text not in seen:
                seen.add(text)
                out.append({"date": when, "text": text})
    return sorted(out, key=lambda d: d["date"], reverse=True)[:12]


def bible():
    """keel/BIBLE.md (Ray's 26 Oct message, read first by every run) and the six members' takes on it."""
    txt = (ROOT / "keel/BIBLE.md").read_text(encoding="utf-8") if (ROOT / "keel/BIBLE.md").exists() else ""
    if not txt:
        return {}
    rules, cur = [], None
    sec = txt.split("## Keel's reading", 1)[1].split("\n## ", 1)[0] if "## Keel's reading" in txt else ""
    for line in sec.splitlines():
        m = re.match(r"\d+\. \*\*(.+?)\*\*\s*(.*)", line)
        if m:
            cur = {"lead": m.group(1), "text": m.group(2)}
            rules.append(cur)
        elif cur and line.startswith("   "):
            cur["text"] += " " + line.strip()
    for r in rules:
        r["text"] = re.sub(r"[`*]", "", r["text"]).strip()
    takes = []
    tk = ROOT / "keel/BIBLE_TAKES.md"
    if tk.exists():
        for para in tk.read_text(encoding="utf-8").split("\n\n"):
            m = re.match(r"\*\*(\w+) \((.+?)\)\.\*\*\s*(.*)", para.strip(), re.S)
            if m:
                takes.append({"name": m.group(1), "room": m.group(2), "text": " ".join(m.group(3).split())})
    books = [{"title": m.group(1), "date": m.group(2)} for m in re.finditer(r"^## (Book \d: .+?) \((.+?)\)$", txt, re.M)]
    return {"rules": rules, "takes": takes, "books": books, "doc": "keel/BIBLE.md", "takes_doc": "keel/BIBLE_TAKES.md",
            "quote": "This is supposed to be a long process because it should take an extraordinary amount of thinking and "
                     "ideation and research and analysis and so on. ... THINK. That's your job.",
            "said": "Caplet, Mon 26 Oct 2026, cover note to the five books (all equal)"}


# ---------- assemble ----------

def room_docs(rid, known):
    paths = []
    for spec in ROOM_EXTRA[rid][1]:
        full = f"keel/{spec}"
        if full.endswith("/"):
            paths += sorted(p for p in known if p.startswith(full))
        elif full in known:
            paths.append(full)
    return paths


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_site")
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    sys.argv = [sys.argv[0], "GitHub Pages"]
    bd.main()
    rows = json.loads(bd.OUT.read_text(encoding="utf-8"))["rows"]
    of = lambda k: [r for r in rows if r["kind"] == k]
    docs, known = collect_docs(out)
    titles = {d["path"]: d["title"] for d in docs}
    cs, rl, ms = commits(), runlog(), memos()
    sched = {r[0]: r for r in bd.ROOMS}
    rooms = []
    for r in of("room"):
        rid = r["id"].removeprefix("room-")
        runbook = f"keel/pm/runbooks/{ROOM_EXTRA[rid][0]}"
        rooms.append({**{k: scrub(v) if isinstance(v, str) else v for k, v in r.items()}, "id": rid,
                      "cadence": sched[rid][5], "runbook": runbook if runbook in known else "",
                      "log": r["file"] if r["file"] in known else "",
                      "work": [{"path": p, "title": titles.get(p, p)} for p in room_docs(rid, known)],
                      "commits": sum(1 for c in cs if c["room"] == rid),
                      "memos": sum(1 for m in ms if m["room"] == rid),
                      "decisions": decisions(r["file"] if r["file"] in known else "")})
    cst = cast()
    members = []
    for m in of("member"):
        mid = m["id"].removeprefix("member-")
        c = cst.get(mid, {})
        members.append({**m, "id": mid, "take": scrub(m["take"]), "full": c.get("full", m["name"]),
                        "profile": {k: c.get(k, "") for k in ("Role", "Strength", "Weakness", "Fear", "Says", "Arc", "Outside")},
                        "home_id": next((x["id"] for x in rooms if x["name"] == m["home"]), ""),
                        "doc": f"keel/members/{mid}.md" if f"keel/members/{mid}.md" in known else ""})
    meta = of("meta")[0]
    data = {
        "meta": {"built": meta["updated"], "built_iso": dt.datetime.now(SYD).isoformat(timespec="minutes"),
                 "health": meta["health"], "repo": REPO,
                 "head": git("rev-parse", "--short", "HEAD").strip(),
                 "branches": [b for b in (ROOT / ".portal_branches").read_text().split() if b]
                 if (ROOT / ".portal_branches").exists() else [],
                 "deadlines": [{"name": n, "at": t, "et": e} for n, t, e in DEADLINES]},
        "rooms": rooms, "members": members,
        "projects": [{**p, "id": p["id"].removeprefix("project-")} for p in of("project")],
        "changes": of("change"), "asks": of("ask"), "instructions": of("instruction"),
        "ips": ips_versions(), "commits": cs, "runlog": rl, "memos": ms, "episodes": episodes(), "docs": docs,
        "bible": bible(),
    }
    data = json.loads(scrub(json.dumps(data, ensure_ascii=False)))
    (out / "data.js").write_text("window.KEEL = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    for f in ("index.html", "app.js", "style.css"):
        shutil.copy(HERE / f, out / f)
    (out / ".nojekyll").write_text("")
    print(f"wrote {out}/: {len(rooms)} rooms, {len(data['ips'])} IPS versions, {len(cs)} commits, "
          f"{len(ms)} memos, {len(docs)} pages")


if __name__ == "__main__":
    main()
