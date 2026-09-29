# RAB Kit: overnight run plan

Root-and-Branch Kit. A coordinated overnight run that turns the adopted IPS strategy into (1) a Friday trade kit with
exemplar Trading Notes, (2) a quant evidence base, and (3) decisions made for the team to ratify.
Status: PLAN, awaiting "I confirm" from Ray. Written 2026-09-30 (Sydney). Branch `rab/integration`, local only.

## 0. Ground rules

- **Never executes.** No WInS login, no orders, no edits to the IPS Google Doc, no `git push`, no emails.
  Existing Sheet tabs are read-only; the run only adds new tabs prefixed `RAB `.
- **Source of truth, in order:** (1) official Wharton docs in `competition/official/2026_27/` and the Drive folder;
  (2) Ray's WInS Session Rules notes (Sheet tab `WInS Notes`); (3) the adopted IPS (Google Doc "IPS Report");
  (4) this repo. Repo files that contradict (1)-(2) are stale (e.g. `config/competition.yaml` $100k / $0 commission).
- **The strategy is adopted, not reopened.** Root-and-Branch: 2027 deposit buys Treasuries dated to the ten $50k
  payments; 2028 deposit buys a floor repaying that deposit by late 2032, rest in a global stock fund; 2031 range =
  floor to floor + half the stock fund; 2033 gift capped at the top. The kit tests and implements it. Any finding
  that contradicts the IPS is classified *fix before 6 Nov* / *note in Final Report* / *ignore*, never silently applied.
- **Current WInS book = the Sheet `Portfolio` tab** (dated holdings IBTM-IBTR + Treasuries 2037-2041, VT ~8.7%,
  cash ~1%), which supersedes insight_v1's IEF+TLH book (ii)R ("match" was false: 74.7% of TLH matures after 2042).
  WS1 confirms this or flags it for decision D7.
- **Exemplar Trading Notes are authorised by Ray (2026-09-30)**, overriding the repo CLAUDE.md "do not write" rule
  for this run only. Every exemplar is labelled `EXAMPLE - team rewrites`, and logged in `docs/AI_USE.md`.
- Unverified facts are marked UNVERIFIED. No number appears in an output unless it traces to `rab/numbers.yaml`
  or a cited source.
- **Reuse first.** insight_v1 (~90 agents, 27-28 Sep) already built models and a Trading Notes pack
  (`research/insight_v1/scripts/D3_*`, `D5_*`, `wins_now/`, `trading_notes_pack.md`). New work fills gaps and
  re-verifies; it does not rebuild what exists and passes.

## 1. Backcast: what exists at 7am

1. `rab/BRIEF.md`: one page. Decisions to ratify, Friday checklist, top 3 risks, what failed.
2. **Friday trade kit** (Sheet tabs `RAB Tickets`, `RAB Notes`): ticker, name check, quantity, reference price,
   limit guidance, cost incl. commission, 2x-volume check, order sequence, running cash; per-trade note brief +
   exemplar note (<=300 chars, live counter) + the 3 recommended Trading Notes Analysis picks.
3. **Decision memos** (`rab/decisions/`): D6 cap share; pre-2027 rate hedge yes/no; WInS book (D7); fund choice
   for the branch (VT vs alternatives); the 3 featured notes; a planned second trade in October.
4. **Working paper** (`rab/paper/RAB_working_paper.pdf`) with methods, figures, model cards, references.
5. **Code** (`rab/models/`), pinned env, fixed seeds; `make all` reproduces every number.
6. **Interactive page** (private Artifact): co-sponsor range explorer, cost-of-certainty history.
7. **Post-mortem** (`rab/POSTMORTEM.md`) and `rab/STATUS.md` (live progress; survives a crash).

## 2. Techniques embedded

| Stage | Technique | Artifact |
|---|---|---|
| Before | Backcast (above); **pre-mortem** (s6, expanded by the run's first agent) | `rab/premortem.md` |
| Before | Key assumptions check: every assumption rated solid / caveated / unsupported | `rab/assumptions.md` |
| Before | Work breakdown + critical path (s3); Definition of Done per stream | this file |
| Before | Risk register with owner, response, trigger (s7) | this file |
| During | Gates A-D (go / fix / stop) | `rab/STATUS.md` |
| During | Dual computation: every headline number built twice, blind | `rab/verification/` |
| During | Decision log (options, evidence, choice, what would change it) | `rab/decisions/` |
| During | Red team, devil's advocate, judge "murder board" using the self-scoresheet | `rab/redteam/` |
| After | Completeness critic; post-mortem / after-action review | `rab/POSTMORTEM.md` |
| After | Handoff: decisions to ratify at breakfast | `rab/BRIEF.md` |

## 3. Workstreams, priority and critical path

Priority tiers decide what runs first, so a stop partway still leaves Friday covered.

| Tier | WS | Scope | Depends on |
|---|---|---|---|
| P0 | WS0 Coordinator | pre-mortem, gates, merges, STATUS, BRIEF | - |
| P0 | WS1 Data + ladder | inventory insight_v1; pull curve + prices; M1 ladder; lock `rab/numbers.yaml` | - |
| P0 | WS6 Trade kit + notes | M9 security selection; tickets; note briefs; exemplars; 3 picks; Oct second trade | Gate A |
| P1 | WS2 Range + cap | M3, M4, M8; D6 memo; stated confidence | Gate A |
| P2 | WS3 History + rivals | M5, M6 (incl. VT vs alternatives), M7 | Gate A |
| P2 | WS4 Timing risk | M2; pre-2027 hedge memo | Gate A |
| P2 | WS5 Literature | LDI / goals-based / dedicated portfolio / CPPI; references for Works Cited | - |
| P3 | WS7 Red team + judges | attack outputs; score notes; key-assumption challenge | Gate B, C |
| P3 | WS8 Assembly | paper, page, Sheet tabs, BRIEF, POSTMORTEM | Gate D |

Critical path: WS1 -> Gate A -> WS6 -> Gate C -> WS7 -> Gate D -> WS8. WS2-WS5 run in parallel.
Each code-writing stream works in its own git worktree (`rab/ws1` ...), merged into `rab/integration` by WS0.

### Definition of Done

- **WS1**: inventory table of insight_v1 models (reuse / re-verify / replace, with reason); official curve date and
  source URL; M1 prices every holding in the `Portfolio` tab; blind second pricing agrees to $1; `numbers.yaml`
  locked with a hash; stale WInS bond prices flagged by yield check.
- **WS6**: every ticket has a name-verified ticker (IBTN trap), quantity <= 2x daily volume or a split plan, cost
  with commission, cash never negative in sequence; every exemplar <= 300 chars, cites only `numbers.yaml`, links
  to a Laura goal; 3 picks justified against the TN Analysis criteria; a Friday-evening refresh script.
- **WS2**: range at stated confidence under 3 return models; D6 memo with a pre-registered decision rule; sensitivity
  (tornado + Sobol) naming the 3 assumptions the IPS must state.
- **WS3**: backtest over every start year the data allows; rivals scored on the same metrics; stress table incl.
  real value of the $50k payments.
- **WS4**: probability ladder cost > $300k by Jan 2027 (reconciled with insight_v1's "1 in 3"); hedge memo.
- **WS5**: 10-20 real, resolvable references (DOI/URL checked), each with one line on how it supports the plan.
- **WS7**: every critique tagged fix-now / Final Report / ignore; scoresheet scores for the 3 notes.
- **WS8**: BRIEF <= 1 page; paper compiles; every figure regenerates from code.

### Gates

- **A (data)**: ladder priced twice, agree to $1; curve and prices dated and sourced; `numbers.yaml` locked.
  Fail -> retry once with a third pricer; still failing -> WS6 proceeds using insight_v1's reconciled 28 Sep figures,
  flagged.
- **B (models)**: each model rebuilt blind from its spec; results within tolerance (range ends +-2%, probabilities
  +-2pp). Fail -> both versions reported, the discrepancy explained; no decision rests on an unreconciled model.
- **C (trade kit)**: all tickets and notes pass automated checks (length, ticker name, cash, volume, traceability).
- **D (red team)**: every fix-now item fixed or explicitly deferred with reason.

## 4. Models

Reuse-first: WS1 maps each to existing insight_v1 code before anything is written.

| ID | Model | Question | Method | Likely insight_v1 overlap |
|---|---|---|---|---|
| M1 | Ladder pricer | Cost of the ten payments now, per holding, WInS and curve prices | Curve fit (official par curve), PV per rung, yield check | `A2_curve_recheck`, `D1_*`, reconciliation in 84e7010 |
| M2 | Rate paths to 2027 | P(ladder > $300k at Jan 2027); worth pre-hedging? | AR/Vasicek fit + historical 15-month moves | AX1b rates audit |
| M3 | Branch Monte Carlo | 2028-2033 branch distribution | Shiller bootstrap; fat-tailed parametric; Bayesian (pymc) with uncertain mean | `D2_equity_premium`, `D5_range_and_flexibility` |
| M4 | Cap optimiser (D6) | What share of the branch to promise | pymoo: expected gift vs P(disappoint) vs range width | `D3_range_rules` |
| M5 | Century backtest | Root-and-Branch from every start year | Historical yields + returns | `D3_history_stress` |
| M6 | Rivals | All-bond, 60/40, TIPS ladder, CPPI, glide path; VT vs VTI+VXUS / US-only / tilt / +gold/REIT | Reuse M3/M5 | `D3_barbell`, `D3_lock_frontier` |
| M7 | Stress | 1970s, Japan, 2022, US downgrade; real value of $50k | Scenario engine | `D3_history_stress`, `D3_joint_tail` |
| M8 | Sensitivity | Which assumptions move the range | Tornado + Sobol | - |
| M9 | Security selection | Best security per slot + runner-up; 2x-volume; name check | Screen: maturity match, yield vs curve, cost, liquidity, WInS listing | `wins_now/securities_and_allocation_v1.md` |

Not built: yield forecasting / ML (contradicts the lock-in logic), SHAP (no ML model), single-stock models.
Every model ships a one-page model card: assumptions, data, limits, failure modes.
Env: `uv` venv in the worktree, pinned (numpy, scipy, pandas, statsmodels, pymc, pymoo, SALib, matplotlib), seed 20260930.

## 5. Data sources

| Data | Source | Fallback |
|---|---|---|
| Treasury par curve (daily, history) | home.treasury.gov daily par yield curve (CSV) | FRED DGS* via fredgraph CSV (no key) |
| ETF prices, volume | Longbridge MCP quotes (read-only) | yfinance |
| Long equity + bond history | Shiller data (Yale), Damodaran annual returns | cite gap, narrow backtest |
| WInS listing/prices | Sheet `WInS Notes` + insight_v1 `wins_now/` (29 Sep) | flag as needing Friday re-check in WInS |

Fetch with `.venv/bin/python research/insight_v1/scripts/fetch_text.py` or curl (WebFetch was blocked earlier).

## 6. Pre-mortem (seed; the run's first agent expands it)

"It's 7am and the kit is a failure." Likely causes and the safeguard built in:

1. Streams used different numbers -> single `numbers.yaml`, Gate C traceability check.
2. Rebuilt what insight_v1 already had, ran out of usage before the trade kit -> reuse-first inventory; P0 first.
3. A ticket buys the wrong security (IBTN = INSCORP) or exceeds 2x volume -> M9 name + volume checks.
4. Prices stale by Friday -> refresh script + Friday checklist; WInS price re-check by the team.
5. Exemplar notes read as AI / break 300 chars / cite unverified numbers -> automated checks + judge panel;
   labelled examples, team rewrites.
6. Kit quietly redesigns the strategy -> contradiction triage rule (s0).
7. Output flood (831-page problem) -> BRIEF <= 1 page, paper <= 20 pages, rest in appendices.
8. Models agree because they share code -> blind rebuild from spec, no code sharing between builders.
9. Fake or unresolvable references -> WS5 resolves every DOI/URL.
10. Run dies overnight with nothing usable -> STATUS.md + per-stream commits; resumable run.
11. Sheets connector unavailable headless -> write CSV in `rab/sheets/`, load in the morning.
12. Weekly usage cap hit (76% used at plan time, resets 2pm Sydney 30 Sep) -> P0 first; resume after reset.

## 7. Risk register

| Risk | Likelihood | Impact | Response | Trigger |
|---|---|---|---|---|
| Usage cap mid-run | Medium | Medium | Priority order; resume from run id after 2pm | agent calls fail |
| Ladder now > $300k at current curve | Low-Med | High | Flag fix-before-6-Nov; options memo (trim VT, IBTM floor share) | M1 total > $300k |
| WInS order types (limit?) unknown | High | Low | Friday checklist item; tickets give reference + max price | - |
| Thin volume in IBTQ/IBTR | Medium | Medium | Split orders across days; alternates | qty > 2x ADV |
| Stale repo facts leak into outputs | Medium | Medium | Source-of-truth order; audit agent greps for $100k etc. | - |
| Public repo exposes kit | Low | Medium | Local branches only, no push; D11 stays with team | - |
| Kit contradicts IPS | Medium | Medium | Triage rule; memo, not edit | any memo disagrees |
| Mac sleeps | Low | High | `caffeinate` background; plugged in, lid open | - |

## 8. Items the team must check on Friday (cannot be done by the run)

- WInS order types, whether prices shown match the ticket reference, cash after commissions.
- Each ticker's name in the WInS order screen before submitting.
- Note box: paste the team's rewritten note, count <= 300.
- Market open 9:30 am ET = 11:30 pm Fri Sydney (AEST; Sydney daylight saving starts Sun 4 Oct).

## 9. Admin carried in the BRIEF

AI-use log entries (`docs/AI_USE.md`, incl. exemplar notes); roster due 9 Oct; request the school documentation
letter now; optional Contact Us question on "for BOTH contributions"; PR raei-2748/caplet-investment#4 still to merge.
