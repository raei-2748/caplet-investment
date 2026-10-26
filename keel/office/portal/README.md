# Keel Office portal (GitHub Pages)

**Live:** https://raei-2748.github.io/caplet-investment/ (public; built from this repo, nothing is typed in by hand).

Ray asked on 26 Oct 2026 for a portal "so we can always track progress": clickable rooms, pixel-art avatars for the
six, real progress, and above all every IPS version (V1, V2 ... V100) with what changed. Pages:

| Page | Shows | Reads |
|---|---|---|
| Office | countdowns, latest IPS, rooms on time, commits, IPS chart, the six, rooms, changes for the judges, work by day | everything below |
| IPS | every version's word counts against the limits, how much each changed, any two compared word by word, each version's text | `keel/ips_rewrite/VERSIONS.md` and the files it names |
| Rooms / a room | Now block, memos, commits, run log, the room's work files, its log and runbook | `keel/rooms/*.md` (`## Now`), outbox, `git log`, `keel/pm/RUNLOG.md` |
| Team / a member | pixel avatar, profile, latest take, every labelled take in the memos | `keel/CAST.md`, outbox memos, `keel/pm/STANDUP.md` |
| Activity | commits per Sydney day, by room, filterable feed, run log | `git log` of `keel/` on main and every `claude/*` branch |
| Episodes | the season, with Jun's ladder headroom by episode | `keel/episodes/INDEX.md` |
| Plan | Keel's projects, questions for Caplet, Caplet's instructions | `keel/pm/PROJECTS.md`, `ASK_HUMANS.md`, `keel/INSTRUCTIONS.md` |
| Library | every Keel markdown page, rendered, searchable | `keel/**/*.md` |

**How it updates.** `.github/workflows/keel-portal.yml` builds on every push to main, hourly 07:00-21:00 Sydney and
every 3 hours overnight; `keel-portal-poke.yml` starts a build whenever a `claude/*` branch pushes to `keel/`. Each
build merges the newest `claude/keel-loop-*` day branch and the branches in `branches.txt` into a scratch copy of main
(skipping any that conflict), so a room's run shows within minutes, before the evening merge.

**What rooms must do** (already in `keel/pm/runbooks/README.md`, step 6): keep the `## Now` block current, end memos
with labelled takes (`- **Jun:** ...`), log runs, and add a row to `keel/ips_rewrite/VERSIONS.md` for every new full
draft of the pitch + IPS. Snapshots of Caplet's own IPS Report doc go in `keel/ips_rewrite/caplet_doc/` as new dated
files (read only, never edit the doc).

**Build locally:** `pip install markdown && python3 keel/office/portal/build_portal.py --out /tmp/site`, then serve
that folder (`python3 -m http.server --directory /tmp/site`). Files: `build_portal.py` (data), `index.html`,
`app.js` (pages, charts, word diff, avatars), `style.css`.

**Privacy.** The site is public. The builder removes the six students' surname initials, account numbers, emails and
the WInS username line, and skips `keel/library/assistant_review_2026-10/temporary_deposit/`. Never put personal data
in a Keel file in the first place (CLAUDE.md).
