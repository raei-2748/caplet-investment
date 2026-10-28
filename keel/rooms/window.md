# FICTION (the room) + real checks. The Window: what came in, what it changes

## Now
- **Doing:** Beat 2 of the daily round: gate yesterday's finds at source (the "so" beside the quote), then one primary-source find for the day's question
- **Decided:** Wed 28 Oct: seven false or overstated scout conclusions and five number mismatches marked in place; four were heading for the IPS (IRS trust yardstick, Perry, "no 2028 deposit still covered", coupon gap "shut"). The thin-coupon twin goes to the Final Report, no trade
- **Next:** Thu 29 Oct: gate the round's three scouts (settlements, retainage, cue sheets); check whether the Writing Room fixed D6's "$300,000 buys them" line
- **For the judges:** The IPS no longer leans on a tax rule or a 1935 case that says the opposite of what we claimed; the coupon gap stays called a soft spot, not a solved one
- **Updated:** 2026-10-28 09:55 Sydney

> **State (Wed 28 Oct 2026, 09:55 Sydney, fourth Window run, first as beat 2 of the loop).** Three official files of
> 27 Oct checked (PDF hash, v1-v2 diff, criteria diff, TIPS/STRIPS wording); manifest YAML broken -> PR #70 (human merge).
> Gate: 34 scout claims (27 verified, 7 false/overstated) + numbers re-run (5 mismatches), all marked `[Window 28 Oct]`.
> Own find W-01 (`window/W-01_low_coupon_rungs.md`). Near-breaches open: D6 "$300,000 buys them" (request to the Writing
> Room); W1 bills/short-ETF listing. Network: curl is blocked this session; WebSearch + WebFetch work.
> Next run: `git log --since="2026-10-27 22:40 UTC" -- competition/ keel/office/outbox keel/rooms keel/ips_rewrite keel/loop`.

> Room card: `../OFFICE.md`. Felix; agents `rules-verifier`, `integrity-officer`, `fact-checker`. House rules: `../office/CHARTER.md`.
> Everything from outside comes in here and nowhere else. Breaches first. Keel never opens WInS or SMApply, and
> never fetches SMApply pages either (this run's routine rule): a new page comes in only as a student's copy or an earlier snapshot.

## Log
| Date (Sydney) | Run | Found | Memo |
|---|---|---|---|
| Sun 25 Oct | first sweep | No breach. W1 near-breach (short ETF listing). 24 Oct FAQ snapshot was stranded on an unmerged branch: now filed. F1 "Taiwan residency" -> "Taiwan creative residency" (case :76-77); F2 "trade only..." contradicts the coupon sentence. Label gaps in raw .txt paste files fixed with LABEL.md | `../office/outbox/2026-10-25_window_sweep-ips-v4.md` |
| Mon 26 Oct | ground truth + re-runs | No breach. N1 GROUND_TRUTH s5 ladder cost stale (22 Oct: $298,861, 4bp headroom); N2 "floor $150k face" contradicts the locked NAV line. Six fixes to the rewrite spine (gate, form :75, case :119-120). C-01/LR-02/P06/R01 all match on re-run | `../office/outbox/2026-10-26_window_ground-truth-check.md` |
| Tue 27 Oct | ~137 claims, D4, instruction sample | No breach. Six false facts in research and memos (N1 7.5% edition; N2 List & Lucking-Reiley read backwards; N3 M² ranking; N4 Redington + "p5-p95" range; N5 Contac 1960; N6 "inside is guaranteed"), all marked in place. D4 clean; Lehman line verified. One label added | `../office/outbox/2026-10-27_window_7-5-and-three-checks.md` |
| Wed 28 Oct | gate (beat 2) + official files | No breach. N1 D6 "$300,000 buys them" stated as fact; N2 D6 names T-bills (W1); N3 manifest YAML broken (PR #70). 7 false/overstated scout conclusions (Tax Notes trusts, Perry, IRS yardstick, no-2028 coverage, ruin theorem, gift pyramid, Japan 42%) + 5 number mismatches, marked in place. Own find: thin-coupon twins (W-01) | `../office/outbox/2026-10-28_window_thin-coupons-and-four-wrong-sos.md` |
