# L05 (Trades and Trading Notes Analysis forensic): adversarial verification

AI-generated verification (Claude Code) for Team Caplet, Fri 16 Oct 2026 (Sydney). Analysis only. It drafts no
deliverable prose. Every claim was re-opened at the cited source. Web pages were fetched on 16 Oct 2026 with the
page.py fetcher. Scripts and fetched pages: `oct16/verify/L05w/` (decomp.py, rules.txt, smhelp.txt, vt.txt).

**Tally:** 20 findings checked. 11 confirmed, 9 adjusted, 0 refuted, 0 unverifiable. 3 findings added (a fourth point, the [AI]-suggestion rule, is folded into TNA-15).
Personal data removed: TNA-17 quoted a teammate's surname initial from the 15 Oct brief. It is now stripped.

---

## 0. The number conflict: $294,453 vs $298,624. Both are right, on different bases

I rebuilt both numbers from the official October curve in the unmerged branch
(`caplet-latest/competition/official_market_data/daily-treasury-rates_2026-10.csv`). I used the same bootstrap
as `caplet-latest/research/ips_numbers_2026-10/ips_numbers.py:70-89`. Script: `verify/L05w/decomp.py`.

| 15 Oct close | Forward-implied to 1 Jan 2027 | Yields unchanged to 1 Jan 2027 |
|---|---|---|
| $50k on each **payment date** (1 Jan 2033-42) | **$294,453** (room $5,547) = number sheet | $295,246 (room $4,754) |
| $50k on each **holding's maturity** (15 Dec 2032 ... 15 Nov 2041) | $297,841 (room $2,159) | **$298,624** (room $1,376, 4.7bp) = L05/L03/L08 |

The same grid on 6 Oct gives $293,448 on the maturity and unchanged basis. That is exactly the "$293,447, and a
22.7bp fall" in `ops/routines/MONITOR.md:22`, the basis behind the IBTR note's "about 0.2 percentage points".

Why they differ (the $4,171 gap on 15 Oct):
- **Dates priced to, about $3,390.** The sheet puts each $50,000 on its 1 Jan payment date. L05 puts it on the
  WInS holding's earlier maturity date. The gap is 17 days for the iBonds, 10.5 months for Feb-2037, 7.5 months for
  May-2038 and about 47 days for the Nov bonds. The sheet assumes cash waiting between maturity and payment earns
  today's forward rates. L05 assumes it earns nothing.
- **Curve assumption, about $780.** The sheet rolls the curve along forward rates to 1 Jan 2027. L05 holds today's
  yields fixed and dates the curve 1 Jan 2027.
- Same payments (ten x $50,000), same valuation date (1 Jan 2027), same curve date (15 Oct), same bootstrap. The
  date and the method are what differ.
- The sheet is also out of step with itself. `results.json` stores a second cost, $295,924, with headroom $4,076
  and 13.4bp (`ladder_cost_1jan2027_today_curve`, `ladder_headroom_bp`), next to the $294,453 headline. The code
  comment "C1: ~$200 difference" (`ips_numbers.py:57`) understates this gap of about $1,470. The sheet's "about 0.19
  points" is $5,547 divided by DV01. It does not appear in results.json.

Which figure is right for which claim:
- **IBTR note and its "about 0.2 points" test, the MONITOR check, and any TNA reflection.** Use the maturity basis
  with yields unchanged: 22.7bp of room on 6 Oct, 4.7bp on 15 Oct. That is the basis the test was set on. Switching
  to the sheet's basis would quietly move the goalposts by about 14bp.
- **IPS headline "cost of the ten payments".** Either basis can be defended, but the IPS must name one. $294k is
  the market (forward) price and assumes the waiting cash earns forward rates. $298.6k is the cautious price for
  WInS-only holdings. For a "high certainty" claim the cautious basis is safer, or the IPS can say "about
  $294-299k" with its date.
- **Probability of crossing $300k by 1 Jan 2027.** About 35% on the sheet's basis (`results.json`
  p_ladder_over_300k_on_1jan2027 0.352). About 45% on L05's basis (`lenses/L05/ladder_series_out.txt`). Both are
  MODEL. Say "roughly 1 in 3 to 1 in 2", or quote one basis only.

---

## 1. Verdicts

### TNA-01. IBTR threshold almost used up: ADJUSTED (high -> medium)
- Confirmed: the note's text (`05_...md:15`) and MONITOR.md:22. The curve rows (6 Oct 20y 5.68, 15 Oct 20y 5.48)
  are on `daily-treasury-rates_2026-10.csv:2,8`. $298,624 / $1,376 reproduces exactly.
- Wrong in the lens:
  - "Re-run the committed script" fails, because no committed repo script produces this basis. grep finds the
    figure only in MONITOR.md. The pricer lives in the scratchpad (`oct14/factcheck/ladder.py`) and in an external
    monitor. The committed `ips_numbers.py` uses the other basis (section 0).
  - The note is not false. It is dated ("On the 6 Oct Treasury curve") and conditional.
  - The TNA brief says the team is "not expected to ... complete long-term portfolio projections"
    (`2026_WGY_Trading_Notes_Analysis-FINAL.txt:20-23`). It also says the focus is "not simply whether an
    investment gained or lost value" (:15-16). So the simplest safe reflection needs no fresh number at all.
- Why the severity drops: the risk is only a reflection that states a stale or wrong current status.

### TNA-02. IPS "$292,000" and the "2027 leftover first" backstop: ADJUSTED (stays high)
- Confirmed: V5:16, :24 and :26, and Tab 15:7.
- Corrected: "$292,000" is not wrong for its date. On the forward, payment-date basis, late September was about
  $292.8k (L08 COH-08). The fault is that it has no basis label and is stale.
- The 2027 leftover on 15 Oct is $5.5k on the sheet's basis or $1.4k on L05's. It is zero if the line is crossed.
- The better official anchor is TNA:29-31 ("consistent with the strategic approach your team is developing and will
  later articulate in its IPS"). Deliverables.txt:55 is a general evaluation criterion.
- New risk from 412e9e3: CLAUDE.md on the branch tells the team to use the sheet's $294k in the IPS, while the IBTR
  note was set on the other basis.

### TNA-03. Trigger B on the WInS basis: ADJUSTED (medium)
- Confirmed: october_trade.md:20, :42 and :62-63. My arithmetic reproduces the lens: $2,500 / (2/3) = $3,750,
  which is 17.7bp beyond $1,376. At one-fifth, it is 69bp.
- No ratification of trigger B is recorded in the team docs. A grep of `team/google_drive` and COMPETITION.md
  finds none.
- Added: the rule's own check date (14 Oct close, :18) has passed with no logged outcome. The trade window has been
  open since Fri 16 Oct 1:30 AEDT and closes Wed 21 Oct 6:30 AEDT (:19-20). On the sheet's basis each bp figure is
  about 14bp larger.

### TNA-04. 11 trades and "hold" reads as passive: ADJUSTED (high -> medium)
- All quotes confirmed (wins.txt:23, :41; faqs.txt:39; trading.txt:53).
- The 6 Oct 7:55 PM to 7 Oct 8:27 PM ET span (05_...md:14-24) is about 24.5 hours.
- "WInS shows nothing since" is only inferred from the repo (COMPETITION.md:172 "11 of 200"). It is not seen in
  WInS.
- Wharton says plainly that trade count is not scored and discourages frequent trading. So "high" overstates the
  risk to Top 50. The fix is cheap and sound.

### TNA-05. Do not add notes to the picked trades: CONFIRMED
wins_notes.csv:17, wins.txt:43 and TNA:44 all say what the lens claims.

### TNA-06. Liquidity never mentioned: CONFIRMED
- TNA:4-6, Guide:85-86 and note_rules.py:50 all verified.
- The 17 days (15 Dec to 1 Jan) is correct.

### TNA-07. Wharton's example models a glide path: CONFIRMED
TNA:36-39 and Client Profile:90 verified.

### TNA-08. Three kinds of decision; VT "copout" outcome: CONFIRMED
- final_report.md:23-24 verified. The outcome is still "[fill in]".
- A first name only, with no ranking.

### TNA-09. Top 50 = IPS + Final Report: ADJUSTED (medium -> low; known, not new)
- The Rules page quote is verified (rules.txt:459).
- But the source conflict was already logged in `research/insight_v1/phase_A/case_register.md:32` and in L08
  (line 458: "treat all three as scored").
- The same Rules page says teams must "submit the competition deliverables by the published deadlines" to stay
  eligible (:457). So time-boxing is fine, but the TNA must be complete and compliant.

### TNA-10. "Required trading activity" undefined; Week-One email unread: CONFIRMED
- Rules page :451 and :421, faqs.txt:76 and wins_notes.csv:19 verified.
- The public trading.txt has no activity minimum (only "no required sector allocation", :48).

### TNA-11. "Mark as Complete" is not the same as submitting: CONFIRMED
- Both SurveyMonkey help quotes are verified (smhelp.txt:379, :428).
- Wharton's own flow stays UNVERIFIED, as stated.

### TNA-12. Identifier lines: ADJUSTED (medium -> low)
- This is optional polish. The TNA only requires the note "exactly as it appears in WInS" (:44).
- Added: COMPETITION.md:181 calls the Feb-2037 bond "5.000%". WInS (`B-T-4.750-15022037`, 05_...md:16) and
  portfolio.csv:25 say 4.750%. So identifier lines must come from WInS, not COMPETITION.md (see TNA-V03).

### TNA-13. Straight-quote ASCII: CONFIRMED
- Re-scanned: the 11 filled notes are all ASCII. IBTR is 294 characters, IBTM 292 and VT 288.
- Tab 15 has 5 curly apostrophes.
- Caveat: the export is a copy, so the WInS page stays the source.

### TNA-14. VT note faults; AI overlap low: CONFIRMED (with detail)
- The stockanalysis VT page shows "Expense Ratio 0.06%" and "Holdings 10180" (vt.txt:97, :112).
- My 4-word overlap against the 6 Oct AI-draft column: IBTR 0%, IBTM 4%, VT 4%.
- Against the exemplar column (also AI): IBTM 15%, VT 22%. This is consistent with "limited to the exemplars
  already flagged".

### TNA-15. AI disclosure for the TNA: ADJUSTED (medium -> high)
- The Rules page wording is verified: "AI-generated work may not be submitted as your own" and "Any AI-generated
  material included in your report must be properly cited" (rules.txt:471-473). So is :551 ("cited like any other
  reference material").
- The IPS bans formal citations (IPS-FINAL:123-124). The TNA brief has no ban.
- The 412e9e3 rule change (caplet-latest/CLAUDE.md:27-30; COMPETITION.md:142-144) now lets [AI] suggestions into
  the TNA and IPS. But it records accepted AI wording only in the 4 Dec Works Cited, after both are judged. That
  raises this from a residue issue to a live process gap.

### TNA-16. Volume rule wording: ADJUSTED (low)
- The "at most half" line is the team's own transcription of the WInS Portfolio FAQ (wins_notes.csv:14). It is not
  a primary copy, so it is unverified.
- The public rule is verified (trading.txt:41).
- The fix (follow the stricter reading) stands.

### TNA-17. Fix the figure's date to the 20 Oct close: ADJUSTED (medium -> low)
- The teammate initial is removed from the evidence.
- Merged logic with TNA-01: the date only matters if the reflection quotes a number, which the TNA brief does not
  require (TNA:20-23).
- If a number is used, it must also name its basis (section 0).

### TNA-18. Past years rewarded learning notes: CONFIRMED (low)
- R2 page :143 is verified (2 notes, stock and ETF, 150 words).
- 2025_knox_wharton.md:100 and :306 show "beta 0.52" and "supercycle".
- "No Australian team made the Top 50 in 2024, 2025 or 2026" is in `team/Winning Team Portrait and
  Scoresheet.md:45`. That supports the claim that last year's team missed the semis.

### TNA-19. "Only Ray trades" framing: CONFIRMED (low)
Rules page :393 and faqs.txt:34 verified.

### TNA-20. Scale: about $197k of payment holdings: CONFIRMED
- Recomputed from COMPETITION.md:176-185: iBonds $183,851, less 3,361 x $21.65 ($72,766), plus bonds $84,801.
  That gives $195.9k before accrued interest.
- The 3,361 floor shares are on portfolio.csv:39.

---

## 2. Findings the lens missed (verifier-added)

- **TNA-V01 (high). Two ladder bases are now in circulation.** See section 0. The 16 Oct sheet ($294k, $5.5k) and
  the IBTR note and MONITOR basis ($298.6k, $1.4k on 15 Oct) differ by $4.2k. The branch CLAUDE.md:13-14 pushes the
  sheet's figure into the IPS. The sheet also stores a third value ($295,924, 13.4bp).
- **TNA-V02 (medium). Coupon reinvestment and the IBTR reflection.** The IBTR note says the first $300,000 "is
  enough" for all ten payments. On the WInS holdings that holds only if coupons are reinvested at today's forward
  rates. The 16 Oct sheet finds a shortfall of about $21k if yields fall 2 points for good. The chain does not cover
  it in about 6-7 of 100 paths (IPS_number_sheet.md:28-50). Any TNA wording such as "secured" or "locked" would
  conflict with the IPS the team is about to adopt. The five T-bond notes already admit reinvested coupons fund part
  of each payment (05_...md:16-18, :23-24).
- **TNA-V03 (low). COMPETITION.md:181 has the Feb-2037 coupon wrong (5.000% vs 4.750%).** COMPETITION.md calls
  itself the single source of truth, so this error would spread into identifier lines and the Final Report holdings
  table.
- (The [AI]-suggestion rule vs the TNA timeline is folded into the TNA-15 upgrade rather than listed twice: if [AI] wording is accepted into the reflections, the TNA is submitted on 23 Oct with uncited AI text, against 'AI-generated work may not be submitted as your own'.)
