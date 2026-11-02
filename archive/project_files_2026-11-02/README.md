# Project-folder copies not otherwise in the repo (snapshot, Mon 2 Nov 2026)

The Team Keel project keeps a shared folder of copies made for Caplet (IPS drafts, briefs, charts, portal
screenshots). On 2 Nov 2026 every file in it was compared with `main` by content. Most were already in the repo
under their working paths (for example `ips/rewrite/V50/` = `keel/ips_rewrite/drafts/D30/`, V53 =
`keel/ips_rewrite/drafts/D33/`). The files below were not byte-for-byte in the repo, so they are kept here, at the
folder's own paths. Where a working copy exists in the repo, that copy is newer and wins.

| File here | Nearest working copy in the repo |
|---|---|
| `ips/IPS_edits_2026-10-24.md` | `keel/library/ips_road_2026-10/04_IPS_EDITS_2026-10-24.md` (90% of lines match) |
| `ips/IPS_edits_v4_1_2026-10-25.md` | `keel/drafts/ips_v4_1_2026-10-25/` |
| `ips/IPS_name_packages_2026-10-24.md` | `keel/rooms/lab/L-06_creativity.md`, `keel/rooms/lab/L-06_cp/packages.md` |
| `ips/Keel_IPS_road_2026-10-23.md` | `keel/library/ips_road_2026-10/` (the files there, joined into one) |
| `ips/rewrite/PLAN.md` | `keel/ips_rewrite/README.md` (an earlier plan) |
| `ips/rewrite/V25/`, `V30/`, `V45/` `*_pitch_and_IPS.txt` | pitch + IPS in one file; the parts are in `keel/ips_rewrite/drafts/D5a/`, `D10/`, `D25/` |
| `models/c1_price_of_certainty.png`, `models/c2_rivals.png` | earlier renders of `keel/models/charts/` (rerun `keel/models/run_suite.py`) |
| `office/keel_office_map.png` | a render of `keel/office/office_map.svg` |
| `portal/*.png` | screenshots of the Keel Office portal as it was built (26-27 Oct) |

Left out on purpose:
- `voice/ahaan_essays_2026-10-24.txt`: its header says "PRIVATE project file: never commit to the repo or put on the
  portal" (the portal is public).
- `uploads/`: a WInS export carrying a student's surname and the WInS username (personal data; the repo's summary is
  `competition/wins/2026-10-23_snapshot.md`), trade-note and holdings CSVs already summarised there, a settings
  screenshot and a skill file. None of it is Keel work.
- `UPGRADE-NOTES.md`: a note about the project's own set-up, not competition work.
