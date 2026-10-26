# FICTION (the room) + real checks. The Window: what came in, what it changes

## Now
- **Doing:** Fact-checking the rewrite's ground-truth page against the form, the case and the submitted Trading Notes
- **Decided:** All quotes in the ground truth are exact; six fixes made (semifinal gate, coherence rule, range rule, assumptions, degree name, stale ladder cost)
- **Next:** Each morning: check one sample of yesterday's work against Caplet's instruction register; from Fri 30 Oct check each IPS draft line by line
- **For the judges:** Stops a false fact or a rule breach reaching the IPS
- **Updated:** 2026-10-26 08:40 Sydney


> **State (Mon 26 Oct 2026, 08:40 Sydney, second Window run).** No new official file since 24 Oct. Checked this run:
> `keel/ips_rewrite/00_GROUND_TRUTH.md` (quotes all exact; six fixes in `../ips_rewrite/inbox/2026-10-26_window.md`),
> C-01, LR-02, P06, R01 re-run (all match), labels of 21 new files (LABEL.md added to courtroom/, lauras_room/).
> Open: N1 stale ladder cost in GROUND_TRUTH s5 (Trading Desk re-price by Thu 29 Oct); N2 "face" for IBTM (by Fri 30 Oct);
> W1 short Treasury ETF listing (Ray, Sat 31 Oct); 10:30-check gaps (AI clause, Week 2 email, Sat 31 Oct).
> Next run: `git log --since="2026-10-26 08:40" -- competition/ keel/office/outbox keel/rooms keel/ips_rewrite`; from 30 Oct,
> check Draft 1 against GROUND_TRUTH line by line.

> Room card: `../OFFICE.md`. Felix; agents `rules-verifier`, `integrity-officer`, `fact-checker`. House rules: `../office/CHARTER.md`.
> Everything from outside comes in here and nowhere else. Breaches first. Keel never opens WInS or SMApply, and
> never fetches SMApply pages either (this run's routine rule): a new page comes in only as a student's copy or an earlier snapshot.

## Log
| Date (Sydney) | Run | Found | Memo |
|---|---|---|---|
| Sun 25 Oct | first sweep | No breach. W1 near-breach (short ETF listing). 24 Oct FAQ snapshot was stranded on an unmerged branch: now filed. F1 "Taiwan residency" -> "Taiwan creative residency" (case :76-77); F2 "trade only..." contradicts the coupon sentence. Label gaps in raw .txt paste files fixed with LABEL.md | `../office/outbox/2026-10-25_window_sweep-ips-v4.md` |
| Mon 26 Oct | ground truth + re-runs | No breach. N1 GROUND_TRUTH s5 ladder cost stale (22 Oct: $298,861, 4bp headroom); N2 "floor $150k face" contradicts the locked NAV line. Six fixes to the rewrite spine (gate, form :75, case :119-120). C-01/LR-02/P06/R01 all match on re-run | `../office/outbox/2026-10-26_window_ground-truth-check.md` |
