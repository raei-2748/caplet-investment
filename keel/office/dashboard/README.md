# The Keel Office dashboard (one place to see the whole office)

**Link:** https://claude.ai/artifact/NTBamRzChW4niBLYpkm19M (Dashboard artifact "Keel Office", private to Ray's account
until he shares it). Built 26 Oct 2026 after Ray wrote "I have no idea what is happening in the office".

It shows, from the repo and nothing else: what changed in the judge-facing drafts (`../../pm/CHANGES.md`), every room's
card (the `## Now` block at the top of its room file), each member's newest take, Keel's own projects
(`../../pm/PROJECTS.md`), the questions for Caplet with Keel's defaults (`../../pm/ASK_HUMANS.md`) and Caplet's
instructions with whether Keel applies them (`../../INSTRUCTIONS.md`).

## Refresh it (the last step of every Keel run)
1. Update your room's `## Now` block (Doing / Decided / Next / For the judges / Updated, with today's Sydney date and
   time as `YYYY-MM-DD HH:MM`), and add a row to `../../pm/CHANGES.md` if your run changed a judge-facing draft.
   Commit and push first, so git stays the one truth.
2. `python3 keel/office/dashboard/build_data.py "<Room name>"` (writes `office.json`, which is not committed).
3. Artifact tool: `action: "read"` with the link above (needed once per session before you may publish to it).
4. Artifact tool: publish with `url` = the link, `file_path` = `keel/office/dashboard/office.json`, `asset: true`.
   The result gives a url like `/_blob/<id>`.
5. ArtifactData tool: `get` collection `datasets`, doc `office` (note its `version`), then `update` it with
   `if_version` = that version and `data` = `{"source": {"kind": "file", "url": "/_blob/<id>", "name": "office.json"},
   "updated": {"at": "<UTC ISO time>", "by": "<Room name>"}}`.
6. If any of steps 3-5 is refused or the tool is missing, don't retry: write "dashboard not refreshed" in your
   `../../pm/RUNLOG.md` row. The next run's refresh includes your work, because it rebuilds from git.

Never upload anything else to the artifact and never touch its page files except to change the page itself
(`index.html` here is the source of the page; to change the page, edit it, then `set` collection `files`, doc
`index.html`, `{text: <the file>}`, pinned with `if_version`).

## The GitHub Pages portal (Ray, 26 Oct: "Make a portal of the office ... Host it on github Pages")
`.github/workflows/keel-portal.yml` rebuilds a static copy of the office from the newest Keel day branch every hour
(07:00-21:00 Sydney) and on every push to main, with `build_data.py` then `build_site.py`. Rooms don't need to do
anything for it: updating their `## Now` block and pushing is enough. A Pages site is public to anyone with the link,
so the default view (`PORTAL_MODE` = `progress`) shows progress only, with no strategy text; `full` shows everything.
One-time setup by a repo admin: Settings > Pages > Source "GitHub Actions" (a private repo needs GitHub Pro or Team).
