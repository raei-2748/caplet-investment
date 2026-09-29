# Decision Log: Laura Gao Strategy Session

Read this file first. Each stage ends with a 5-line summary. The details are in the files it names.

---

## Stage 1: Housekeeping (done 25 Sep 2026)
1. `config/client_mandate.yaml` now holds Laura Gao's mandate, transcribed from the case with facts and TEAM_DECISION items separated. The demo client stays in `config/demo_client_mandate.yaml`. `human_approved: false` until the team checks the transcription.
2. `config/wharton_public_2026_27.yaml` now includes the **Trading Notes Analysis deadline of 23 Oct 2026** (5pm ET) and the Final Report instructions release date (9 Nov).
3. The case PDF is saved at `competition/official/2026_27/client_case_laura_gao_2026.pdf`.
4. `decisions/00_open_questions.md` lists 8 questions only humans can answer. The most urgent are WInS starting cash and whether ETFs are allowed.
5. The only `src/` change is one line in `src/wharton_ic/core/config.py`: production mode now fails closed until `human_approved: true`, so the existing governance test still passes. Checked on the Mac VM: 47 existing tests pass; 5 couldn't be collected because that Python 3.10 environment lacks cvxpy/scipy/yfinance. Re-run the full suite in the repo's `.venv` (Python 3.12).

## Stage 2: Core model (done)
1. `model/laura/` has about 400 lines of numpy and 14 passing tests. It runs in about 5 seconds and gives identical results on the Mac VM and the cloud machine. Commands: `python -m model.laura.run` and `python -m pytest model/tests -q`.
2. **Main finding:** at today's yields (~5.15% for 6–15 year Treasuries), locking all ten payments costs about **$298k at the start of 2027**, i.e. the first contribution. After that, the payments are funded under every market scenario tested.
3. **Strategy comparison (base case):**
   - A (lock early): 100% funded; facility p10/p50/p90 = $118k / $167k / $230k.
   - C80 (build in 2033): 93.1% funded; $26k / $187k / $392k. In the bear + inflation case it drops to 86.6% funded.
   - Taking equity risk before the reserve is locked raises the median by only ~$20k, but it adds a 7–13% chance of breaking the promise.
4. **History:** replaying all 93 six-year windows since 1928, A funds the reserve in 93/93 with at least $102k to spare. C80 falls short in 3/93 windows, by up to $102k (1929).
5. **2028 contribution:** if the $150k never arrives, A still funds 100% of the payments. B drops to 56% and C60 to 60%.

## Stage 3: Debates (done)
| # | Decision |
|---|---|
| D1 | **Strategy A, "Lock, then grow".** Buy the full Treasury ladder in Jan 2027. If yields are below ~5.0% and the ladder costs more than $300k, top it up from the 2028 money. |
| D2 | **"High certainty"** has two parts: a mechanism (Treasuries held to maturity, matched to each payment) and a standard (≥99.5% in every modelled scenario, 93/93 historical windows, and still funded if the 2028 money never arrives). |
| D3 | **Reserve** = nominal Treasuries, not TIPS. Use iBonds ETFs IBTM, IBTO, IBTP, IBTQ and IBTR for the 2033–2037 payments and individual Treasury notes/bonds for 2038–2042. No trading after that; one rung matures each year. |
| D4 | **Growth sleeve** = 80% equity / 20% intermediate Treasuries. Equity is a broad index core (~60%) plus 8–12 conviction stocks (~40%). Values show up through engagement and themes, with no concentrated theme bets. |
| D5 | **Facility contribution** = 80% of the 2033 surplus; keep a 20% flexibility buffer. Projected (base): **$118k / $167k / $230k** (p10/p50/p90). |
| D6 | **2031 announcement** uses two tiers. Move 70% of the surplus into Treasuries maturing Dec 2032, then say: "At least $X is committed; we expect $L–$H." The committed amount was never breached in any simulated path. On the median path this is $113k committed and $153–174k expected. |
| D7 | **WInS:** if ETFs are allowed, mirror the full strategy (~65% Treasury ETFs / ~35% growth sleeve). If stocks only, WInS is the equity sleeve and the reserve is a "shadow ladder" tracked in a spreadsheet. |
| D8 | **2028 contribution:** keep the case's assumption, but show one chart proving A still works if the money is late or smaller. This is a robustness point, not a contradiction of the case. |

## Stage 4: Red team (done)
`redteam/judge_review.md` lists the top 10 weaknesses and their fixes. The three most important:
1. **Answer "isn't this just buying bonds?"** Show the decision process: yields, cost, evidence, and the rule we would follow if yields were low.
2. **Stock picks must not look disconnected** from a strategy that is mostly bonds. The WInS notes should tie every trade to the growth sleeve's role.
3. **Explain model limits honestly:** flat yield curve, US-only history, the equity return assumptions. Then show that the decision does not depend on them.

## Stage 5: Deliverable scaffolding (done)
Outlines only, no submission prose:
- `deliverables/trading_notes_plan.md` (due 23 Oct)
- `deliverables/ips_outline.md` (due 6 Nov)
- `deliverables/final_report_outline.md` (provisional)
- `deliverables/cosponsor_talking_points.md`

AI use is logged in `docs/AI_USE.md` §5.
