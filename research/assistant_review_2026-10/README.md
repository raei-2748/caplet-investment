# Assistant review, 30 Sep to 15 Oct 2026

AI-generated research and review (Claude Code), made at the request of the team. **It is not submission text.**
Nothing here may be copied into the Trading Notes, IPS or Final Report. Wharton's AI policy allows AI for brainstorming,
says AI-generated work may not be submitted as the students' own, and asks that AI use be recorded in the Final
Report's Works Cited. Log every file below in the team's AI-use record (date, tool, purpose, what was kept).

## Read in this order

| File | What it is | Basis |
|---|---|---|
| `01_Caplet_Team_Brief_15Oct2026.pdf` (+ `.md`) | **Start here.** 19-page team brief: the list of instructions and nuances first, then the reasons. Covers the TNA picks, the IPS V5 problems, WInS checks, the AI-use record, privacy, and the calendar to 4 Dec. | Repo at commit `2affd4c` (14 Oct); market data to 14 Oct close |
| `04_North_Star_Memo_16Oct2026.md` | Ray's tips (simplicity, coherence, growth, creativity, audience) checked against Wharton's FAQ and rubric. The one idea and its system, a rule budget for the IPS, what is genuinely creative, what Wharton students and professionals recognise (Penn course catalog), the growth story to curate, judge questions, and decisions for vote set A. | Repo at commit `6144dd7`; sources read 16 Oct |
| `02_Caplet_Team_Brief_1Oct2026.pdf` | 3-page brief sent before the first trades. Superseded by the 15 Oct brief; kept for the record. | 30 Sep repo, 29 Sep curve |
| `03_Repo_Review_30Sep2026.md` | The first full repo review (plan, numbers checked independently, risks, judge questions). Parts are superseded by the 6 Oct Wharton email (WInS-listed securities only, so STRIPS numbers no longer apply). | 30 Sep repo |
| `supporting/tna_review_merged_14Oct.md` | Three simulated-judge reviews of the WInS trade notes, merged. Picks and swap rules; no drafted reflections. | 14 Oct |
| `supporting/ips_v5_review_merged_14Oct.md` | Three simulated-judge reviews of IPS Version 5, merged. Says what each fix must achieve; no replacement wording. | 14 Oct |
| `supporting/brief_factcheck_14Oct.md`, `brief_critique_14Oct.md` | The fact-check and critique passes run on the 15 Oct brief before it was finalised. | 14 Oct |

Anything a file marks UNVERIFIED is not checked; confirm it before relying on it. Dollar figures are dated; re-price
them before they go into anything the judges read.

## `checks/`: the independent number checks

Written separately from the repo's own models, so they can cross-check them. Python 3 with `numpy` (and `scipy` for
`floor_mc.py`). Run from inside `checks/` in a checkout of this repo (some scripts read `../../../rab/...`).

| Script | Checks |
|---|---|
| `indep_pricer.py` | The shared pricer: bootstraps discount factors from the Treasury par curve; prices the ten $50k payments and coupon bonds. |
| `run_bases.py`, `sept_series.py` | Ladder cost on 1 Jan 2027 on several bases; the Aug-Sep daily series (`sept_series.json`). |
| `series.py`, `series2.py`, `count_over.py`, `daily_max.py` | Daily ladder-cost series to 14 Oct and how often it was above $300,000 (`ladder_cost_series*.csv`). |
| `bondcheck.py`, `bonds_check.py`, `recon.py` | WInS bond fills against a model price; cash reconciliation of the 11 filled orders. |
| `headroom.py` | Room under the deposit on the WInS-listed basis (`tsy_202610.csv` = October curve). |
| `both_deposits.py`, `floor_split.py`, `floor_mc.py`, `reinvest.py` | The 2028 deposit, the floor split, and coupon reinvestment. |
| `hist_cost.py`, `hist_prob.py` | The same ladder priced on historical curves (reads `rab/data/treasury_par_2000_2026/`). |
| `repo_cross.py` | Cross-check against the repo's `rab/models/m1_ladder.py`. |
| `ipsfit2.py`, `sim.py` | IPS word and line fit; trade-note text checks (run `sim.py` from the repo root). |
| `build/` | Scripts that rendered the PDFs and the private review page (fonts not included). |

Data: `par2026.csv` (to 29 Sep) and `par2026_to_14Oct.csv` are the daily Treasury par yield curves from
home.treasury.gov.
