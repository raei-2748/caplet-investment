"""Build the Keel Office portal (a static page for GitHub Pages) from office.json.

    python3 keel/office/dashboard/build_data.py "GitHub Pages"
    python3 keel/office/dashboard/build_site.py --mode progress --out _site

--mode progress (the default): room health and run times, projects' status and due dates, counts of
    questions and instructions. No strategy text, because a Pages site is public to anyone with the link.
--mode full: everything on the private Keel Office dashboard (rooms' decisions, changes to the drafts,
    questions with Keel's defaults, Caplet's instructions with evidence).
The workflow .github/workflows/keel-portal.yml runs this every hour (07:00-21:00 Sydney) and on every push to main;
the repository variable PORTAL_MODE picks the mode.
"""
import argparse
import collections
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
PRIVATE = "https://claude.ai/artifact/NTBamRzChW4niBLYpkm19M"

CSS = """
:root{--bg:#f6f7f4;--panel:#ffffff;--fg:#1d2321;--muted:#5d6763;--line:#dde1dc;--accent:#2f5d50;--ok:#2e7d4f;--warn:#a2650b;--bad:#b3261e;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#131715;--panel:#1b201e;--fg:#e8ece9;--muted:#9aa5a0;--line:#2c3330;--accent:#8cc5b1;--ok:#79c99a;--warn:#e0a84a;--bad:#f08a80;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 "IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:72rem;margin:0 auto;padding:2rem max(16px,env(safe-area-inset-right)) 4rem max(16px,env(safe-area-inset-left));display:grid;gap:2.25rem}
h1{font:400 2.1rem/1.15 "Fraunces",Georgia,serif;margin:0}h2{font-size:1.15rem;font-weight:600;margin:0}
.lede{color:var(--muted);margin:.4rem 0 0;max-width:68ch}.lede b{color:var(--fg);font-weight:600}
section{display:grid;gap:.9rem}.note{color:var(--muted);font-size:.85rem;margin:0;max-width:70ch}
.grid{display:grid;gap:.9rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,18.5rem),1fr))}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:1rem 1.1rem;display:grid;gap:.5rem;align-content:start;min-width:0}
.card h3{margin:0;font-size:1rem;font-weight:600;display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap;align-items:baseline}
.meta{color:var(--muted);font-size:.8rem;margin:0;overflow-wrap:anywhere}
dl{margin:0;display:grid;gap:.15rem}dt{font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-top:.35rem}dd{margin:0;overflow-wrap:anywhere}
.pill{font-size:.75rem;font-weight:500;padding:0 .55rem;border:1px solid currentColor;border-radius:999px;white-space:nowrap}
.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}.mute{color:var(--muted)}
.stats{display:flex;flex-wrap:wrap;gap:.6rem;list-style:none;margin:0;padding:0}
.stats li{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.6rem .9rem;min-width:9rem}
.stats b{display:block;font:400 1.6rem/1.1 "Fraunces",Georgia,serif;font-variant-numeric:tabular-nums}
.stats span{color:var(--muted);font-size:.8rem}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:.85rem}th,td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600}td.w{min-width:16rem}tr:last-child td{border-bottom:0}
a{color:var(--accent)}footer{color:var(--muted);font-size:.8rem}
"""


def esc(s):
    return html.escape(str(s or "—"))


def tone(s):
    t = (s or "").lower()
    if t.startswith(("on time", "applied", "done", "answered", "fixed", "doing")):
        return "ok"
    if t.startswith(("late", "partly", "open")):
        return "warn"
    if t.startswith(("ignored", "no update", "killed")):
        return "bad"
    return "mute"


def pill(s):
    return f'<span class="pill {tone(s)}">{esc(s)}</span>'


def table(rows, cols):
    head = "".join(f"<th>{esc(label)}</th>" for _, label, _ in cols)
    body = "".join("<tr>" + "".join(
        f'<td class="{"w" if wide else ""}">{pill(r.get(f)) if f == "status" else esc(r.get(f))}</td>'
        for f, _, wide in cols) + "</tr>" for r in rows)
    return f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def build(rows, mode):
    of = lambda k: [r for r in rows if r["kind"] == k]
    meta = of("meta")[0]
    full = mode == "full"
    rooms, members, projects = of("room"), of("member"), of("project")
    asks, instr, changes = of("ask"), of("instruction"), of("change")
    open_asks = [a for a in asks if not a["status"].startswith("answered")]
    st = collections.Counter(i["status"] for i in instr)
    out = [f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow">
<title>Keel Office</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz@9..144&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>{CSS}</style></head><body><main>
<header><h1>Keel Office</h1>
<p class="lede"><b>{esc(meta['health'])}</b> · updated {esc(meta['updated'])}. Team Keel is a simulated team, AI-written,
working for Team Caplet in the Wharton Global High School Investment Competition; Caplet decides and submits.</p>
<p class="lede">{"Full view." if full else f'Progress view. The detail (decisions, draft changes, questions and instructions) is on the private <a href="{PRIVATE}">Keel Office dashboard</a>.'}</p></header>
<ul class="stats">
<li><b>{sum(r['health'] == 'on time' for r in rooms)} / {len(rooms)}</b><span>rooms on time</span></li>
<li><b>{len(changes)}</b><span>changes to judge-facing drafts</span></li>
<li><b>{sum(p['status'] in ('open', 'doing') for p in projects)}</b><span>Keel projects open</span></li>
<li><b>{len(open_asks)}</b><span>questions for Caplet (Keel goes ahead on defaults)</span></li>
<li><b>{len(instr)}</b><span>Caplet instructions tracked</span></li></ul>"""]
    if full:
        out.append("<section><h2>What changed in what the judges will see</h2>"
                   + table(changes, [("date", "Date", False), ("deliverable", "Deliverable", False),
                                     ("name", "What changed", True), ("owner", "Room", False)]) + "</section>")
    cards = []
    for r in rooms:
        body = ""
        if full:
            body = "<dl>" + "".join(f"<dt>{lab}</dt><dd>{esc(r[f])}</dd>" for lab, f in
                                    (("Doing", "doing"), ("Decided", "decided"), ("Next", "next"),
                                     ("For the judges", "for_judges"))) + "</dl>"
        cards.append(f'<article class="card"><h3>{esc(r["name"])} {pill(r["health"])}</h3>{body}'
                     f'<p class="meta">{esc(r["who"])} · {esc(r["schedule"])} · updated {esc(r["updated"])}</p></article>')
    out.append('<section><h2>The rooms</h2><p class="note">Each room updates its card at the end of every run; '
               '"late" means it missed its schedule.</p><div class="grid">' + "".join(cards) + "</div></section>")
    pcards = []
    for p in projects:
        body = (f"<dl><dt>Changes for the judges</dt><dd>{esc(p['for_judges'])}</dd>"
                f"<dt>Next step</dt><dd>{esc(p['next'])}</dd></dl>") if full else ""
        title = p["name"] if full else p["id"].replace("project-", "")
        pcards.append(f'<article class="card"><h3>{esc(title)} {pill(p["status"])}</h3>{body}'
                      f'<p class="meta">{esc(p["owner"])} · due {esc(p["due"])}</p></article>')
    out.append("<section><h2>Keel's own projects</h2><div class=\"grid\">" + "".join(pcards) + "</div></section>")
    mcards = []
    for m in members:
        take = f'<p style="margin:0;font-family:Fraunces,Georgia,serif">{esc(m["take"])}</p>' if full else ""
        mcards.append(f'<article class="card"><h3>{esc(m["name"])} <span class="pill mute">{esc(m["home"])}</span></h3>'
                      f'{take}<p class="meta">{esc(m["role"])}</p></article>')
    out.append("<section><h2>The six</h2><div class=\"grid\">" + "".join(mcards) + "</div></section>")
    if full:
        out.append("<section><h2>Questions for Caplet</h2><p class=\"note\">Keel goes ahead with its default by the date; "
                   "your answer overrides it.</p>" + table(asks, [("date", "Asked", False), ("owner", "Room", False),
                   ("name", "Question", True), ("default", "Keel's default", True), ("due", "By", False),
                   ("status", "Status", False)]) + "</section>")
        out.append("<section><h2>Caplet's instructions, and whether Keel applies them</h2>" + table(
            instr, [("date", "Date", False), ("name", "Instruction", True), ("status", "Status", False),
                    ("evidence", "What we found", True), ("file", "Now enforced in", True)]) + "</section>")
    else:
        out.append("<section><h2>Caplet's instructions</h2><ul class=\"stats\">" + "".join(
            f"<li><b>{n}</b><span>{esc(s)}</span></li>" for s, n in sorted(st.items())) + "</ul></section>")
    out.append(f"<footer>Built from the repo by keel/office/dashboard/build_site.py ({esc(mode)} view) · "
               f"{esc(meta['updated'])}</footer></main></body></html>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["progress", "full"], default="progress")
    ap.add_argument("--out", default="_site")
    a = ap.parse_args()
    rows = json.loads((HERE / "office.json").read_text(encoding="utf-8"))["rows"]
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(build(rows, a.mode), encoding="utf-8")
    (out / ".nojekyll").write_text("")
    print(f"wrote {out / 'index.html'} ({a.mode} view)")


if __name__ == "__main__":
    main()
