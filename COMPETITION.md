# Wharton Global High School Investment Competition 2026-27: everything we know

Team **Caplet** (Knox Grammar School, Sydney). WInS account `Caplet-10465936`. Last updated 2026-10-14.

This file is the single source of truth for competition rules, dates, the client case and where our work stands.
When it disagrees with an older file in this repo, this file wins. Primary sources are listed in section 10.

---

## 1. Key dates

All official deadlines are **5:00 pm ET** with no extensions. The Sydney time is shown because the team is in AEDT.
US daylight saving ends on 1 Nov, so the gap changes from 14 to 16 hours.

| What | ET deadline | Sydney (AEDT) | Status |
|---|---|---|---|
| Practice trading (WInS wiped afterwards) | 15-25 Sep | | done |
| Official trading starts | Mon 28 Sep, 9:30 am | | done |
| Team roster (locked once submitted) | Fri 9 Oct | Sat 10 Oct 08:00 | **submitted** |
| **Trading Notes Analysis (TNA)** | **Fri 23 Oct** | **Sat 24 Oct 08:00** | drafting |
| **Trading ends, WInS portfolio frozen** | **Fri 6 Nov, 4:00 pm** | Sat 7 Nov 08:00 | |
| **Investment Policy Statement (IPS)** | **Fri 6 Nov** | **Sat 7 Nov 09:00** | Version 5 draft |
| Final Report instructions released | Mon 9 Nov | ~Tue 10 Nov | |
| **Final Report + school documentation letter** | **Fri 4 Dec** | **Sat 5 Dec 09:00** | not started |
| Semifinal (Top 50) teams announced | after judging | | |
| Semifinals: short video presentation, all members present | early 2027 | | |
| Global Finale (costs are ours; virtual attendance allowed) | 2027 | | |

Our own internal check dates (scheduled routines, see `ops/`): mock-judge TNA 19 Oct, TNA gate check 23 Oct,
mock-judge IPS 1 Nov, IPS gate check 6 Nov, mock-judge Final Report 22 Nov and 30 Nov, final gate check 4 Dec.

## 2. How we are judged

- Three deliverables are scored, and judged together: **Trading Notes Analysis, IPS, Final Report**.
- Five criteria: **Investment Strategy · Client Knowledge & Objectives · Portfolio Analysis · Articulation of
  Competition Experience · Creativity & Presentation**. Creativity & Presentation includes communicating Laura's
  facility-contribution range and its uncertainty credibly to co-sponsors.
- **WInS ranking, profit and number of trades are NOT scored.** WInS gains/losses must never be added to Laura's
  projections. Projections start from $300k in 2027 + $150k in 2028 + reasonable return assumptions.
- Judges want reasoning, assumptions and trade-offs. "There is no single correct strategy." No individual feedback.
- The Top 50 semifinalists are chosen on the written deliverables (2026 post credits Wharton School student
  evaluators plus Aberdeen asset managers; whether students review in 2026-27 is UNVERIFIED). Semis = panels of
  alumni + industry; finale = industry leaders.
- Non-compliant submissions (format, length) are excluded from semifinal selection.

## 3. The client: Laura Gao

Official case: [`competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`](competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf).
Laura is a fictional client. She is funding a community residency facility in Taiwan with co-sponsors.

- **Money in:** $300,000 at the start of 2027 and $150,000 at the start of 2028. Nothing else goes in or comes out
  before 2033.
- **Operating commitment:** ten fixed nominal payments of **$50,000 at the start of each year 2033-2042**, funded by
  the portfolio with a "high degree of certainty". No reliance on co-sponsors.
- **Operating reserve** is set aside at the start of 2033.
- **Facility contribution** comes from what is left over. No preset amount, and flexibility should be preserved.
- **In 2031** Laura tells co-sponsors a **dollar range** for her 2033 contribution, with a stated confidence. The
  range must protect the operating commitment. Overpromising damages credibility.
- Teams also draft part of the **co-sponsor fundraising materials** (in the Final Report).
- **Out of scope:** taxes, the Taiwan legal setup and the total facility cost.
- Convention: year number = calendar year - 2026; cash flows happen at the start of the year.

## 4. WInS trading rules (the simulator)

Public rules: [`smapply_public_2026-10-14/trading.txt`](competition/official/2026_27/smapply_public_2026-10-14/trading.txt)
and `wins.txt`. Where the **logged-in WInS Session Rules** differ, they are marked "(session)" and they apply.

| Rule | Value |
|---|---|
| Starting cash | **$300,000** virtual (= Laura's 2027 deposit; the $150k is NOT added) |
| Account | One shared team account, 4-6 students; students (not the advisor) place trades |
| Trading window | 28 Sep 9:30 am ET to 6 Nov 4:00 pm ET, then frozen |
| Max trades | 200 |
| Order size | at most 2x the security's daily volume |
| Commission | $25 per stock/ETF trade, $10 per Treasury bond trade |
| Allowed | stocks priced >= $5 (public) / **>= $3 (session)**; **any ETF on WInS**; **Treasury bonds on WInS** |
| Bonds | public page lists US, UK, Germany, France, Italy, Netherlands; the session rules and the 6 Oct email say **US Treasuries** |
| Banned | margin, shorting, stock-secured debt, crypto, derivatives, anything else |
| Position limit (session) | 200% per stock/ETF; 100% per bond and for all bonds (so effectively no cap) |
| Other (session) | no fractional shares; 0% interest on cash; no day trading |
| Fills | US orders fill in real time when the market is open, else at the next open; international orders fill at the end of the trading day (+1 day); FX is automatic |
| Bond pricing | prices update once a day; coupons every 6 months; bonds count in the final value. Orders are entered in **units of $1,000 face** |
| Sector rules | **none**: "no required sector allocation or minimum number of sectors" (the "one stock per sector" rule on en.wghs.org.cn is from old years) |
| Trade notes | box max **300 characters**; notes cannot be edited, only added ("Add Note") |
| Open orders | only open orders can be cancelled; WInS cancels instantly with no confirmation; WInS does not reserve cash for open orders |

**Week-2 email (6 Oct 2026), important:** "Portfolio construction and recommendations for both contributions may
include only approved investment types: eligible stocks, ETFs and Treasury bonds available on WInS." So Laura's
*real* plan (both the $300k and the $150k) may only use WInS-listed securities. STRIPS, single zero-coupon
Treasuries and direct T-bills are out. Older repo files that rely on STRIPS carry a banner saying so.

WInS quirks we found (read-only checks):
- WInS lists 43 US T-bonds, none maturing Feb 2031 to Feb 2036. iBonds Treasury ETFs fill that gap: IBTK 2030,
  IBTL 2031, IBTM Dec 2032, IBTO 2033, IBTP 2034, IBTQ 2035, IBTR Dec 2036. (IBTN on WInS is INSCORP Inc, not an iBond.)
- Some WInS bond prices are stale (Feb-2036 and Feb-2038 were about 1pp off the curve). Always yield-check a bond
  price before ordering.
- WInS shows the May-2038 bond's last coupon as 15 Aug instead of 15 May, so it charges less accrued interest.
- The WInS pie chart labels the iBond ETFs "Long Equities" (61.6%). The true mix is about 91% Treasuries. Explain
  this in the Final Report.
- After-hours bid/ask on iBonds is very wide, so use limit orders near the last price.

## 5. Deliverable formats

### Trading Notes Analysis (due 23 Oct)
Official instructions: [`2026_WGY_Trading_Notes_Analysis-FINAL.pdf`](competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.pdf).
- Pick **3 Trading Notes from real WInS trades**, copied **exactly** as in WInS (they are verified).
- A reflection of **at most 100 words each**: why the trade, how it fits the strategy, the link to Laura's
  goals/funding/risk. The position does not have to be still held.
- Not expected to size the reserve or the facility yet. Submitted through the SMApply form.
- Our suggested picks (team decides): **IBTM** (6 Oct 10:01 PM), **IBTR** re-placed version (7 Oct 4:42 AM),
  **VT** (7 Oct 8:27 PM); runner-up the Feb-2037 bond. All notes verbatim:
  `team/google_drive/ips_report/` (tab "WInS Trading Notes").

### Investment Policy Statement (due 6 Nov)
Official instructions: [`2026_WGY_Investment_Policy-FINAL.pdf`](competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.pdf).
- Title page: official team name, members as "First Name, Last Initial", WInS username. Must match the roster.
  Ours: **Caplet** · Ray W. | Ahaan D. | Darren W. | Harry Y. | Eric Z. | Young Y. · Caplet-10465936.
- Then **max 2 pages**: elevator pitch (**max 50 words**) + IPS (**max 500 words**).
- Times New Roman 12 pt, double-spaced, 1" margins, PDF <= 5 MB, via SMApply.
- **No** graphics, charts, links, footnotes or citations (sources go in the Final Report).
- Focus on framework and principles, not individual securities or detailed calculations.
- **Strategy lock:** after the IPS deadline the strategy is final. The Final Report must follow it and evaluate the
  implementation. We may say what we'd do differently, but not redesign. The IPS does not need final reserve
  numbers, projections, the facility range or the co-sponsor text; those go in the Final Report.

### Final Report + school documentation (due 4 Dec)
- Detailed instructions arrive **9 Nov**. Evaluate how we implemented the strategy; give analysis and
  recommendations for Laura's goals (reserve calculation, projections, the 2031 range, co-sponsor draft).
- **School documentation:** a signed letter on official school letterhead from a school administrator, confirming
  the advisor, the team name and the 4-6 students (team leader first) are enrolled at the same school location and
  approved to take part. Template: [`2026_27_School_Documentation_Template.pdf`](competition/official/2026_27/2026_27_School_Documentation_Template.pdf).
  Separate file. **Request it early (not yet requested as of 13 Oct).**

### Roster (submitted, locked)
Per student: full name, unique email, birthday, graduation year; plus team name, school country/state/city,
school website. (Personal details are deliberately not stored in this public repo.)

## 6. AI policy and how we work

- Wharton: AI may be used for brainstorming. AI-generated work may not be submitted as the students' own; any AI
  use must be recorded in the Final Report's Works Cited. Students use their own voice and words.
- So in this repo, everything AI-made is research, numbers, checks and blueprints. **The team writes every
  deliverable.** Files in `team/ai_outputs/` are labelled "AI, not for submission".
- Log AI use as you go: `research/insight_v1/AI_USE*` and the AI-use rows in the team sheet.
- The advisor handles admin only; all strategy decisions are the students'.

## 7. Our strategy ("Roots First")

Locked in principle in the IPS drafts; the team still words it. Plain version:

1. **Jan 2027, $300k:** buy a Treasury ladder that pays the ten $50k payments (2033-42). This becomes the
   operating reserve in 2033. Built only from WInS securities: iBond ETFs IBTM (2032) to IBTR (2036) for the
   payments in 2033-37, and T-bonds Feb-2037, May-2038, Nov-2039, Nov-2040, Nov-2041 for 2038-42. It costs about
   $293k on the 6 Oct curve; a fall in yields of about 0.2 percentage points would push it above $300k.
2. **Jan 2028, $150k:** first fill any gap in the ladder, then buy a **floor** in IBTM (the Dec-2032 Treasury ETF)
   sized to return about $150k by 2033, and put the rest (~9% of all money) in one world stock fund, **VT**,
   untouched until 2033.
3. **2031:** trade nothing. Quote the co-sponsors a range from the floor (rounded down after any expected
   shortfall) up to the floor + half the stock fund's value.
4. **2033:** the ladder is the reserve; the contribution = floor + half the fund (capped at the announced top);
   the rest stays with Laura. Any expected shortfall is covered first from the 2027 leftover, then Laura's half,
   then the part of the contribution above the floor.

Trade-off we accept (and should state): less stock means a lower median contribution, in exchange for a much
better bad case. Model work: `research/insight_v1/` (with STRIPS banners), F2 grid
`research/insight_v1/scripts/F2_floor_split_grid.py`, strategy log in `team/google_drive/strategy_notes.md`.
Wording rules from the judge-lens brief: floor + VT is a static floor-plus-cushion (**not** CPPI); the ladder is
cash-flow matching (**not** immunisation); never say "risk-free" or "guaranteed".

## 8. The WInS portfolio now

All 11 orders filled 7-8 Oct 2026 (placed by Ray). 11 of 200 trades used.

| Holding | Quantity | Fill (per share / per $100 face) | Pays for |
|---|---|---|---|
| IBTM (iBonds Dec 2032 Treasury ETF) | 4,503 sh | 21.65 | 2033 payment + 2028 floor stand-in |
| IBTO (Dec 2033) | 1,024 sh | 22.86 | 2034 |
| IBTP (Dec 2034) | 927 sh | 23.90 | 2035 |
| IBTQ (Dec 2035) | 894 sh | 23.46 | 2036 |
| IBTR (Dec 2036) | 853 sh | 23.24 | 2037 |
| 4.750% T-bond Feb-2037 | 20 units ($20k face) | 96.019 | 2038 |
| 4.500% T-bond May-2038 | 20 units | 93.076 | 2039 |
| T-bond Nov-2039 | 18 units | 90.005 | 2040 |
| T-bond Nov-2040 | 18 units | 87.724 | 2041 |
| T-bond Nov-2041 | 20 units | 74.955 | 2042 |
| VT (Vanguard Total World Stock) | 167 sh | 158.83 | growth sleeve |

Cash $3,513.79. Value about $301,950 on 13 Oct (+0.65%). Every weight is within 0.2 pt of target. **Plan: hold,
no more trades** (the IPS says hold; drift is trivial; extra trades cost $25 each). The WInS portfolio mirrors
Laura's plan scaled to $300k. Watch for the November iBond distributions, which may pay around 6 Nov (freeze day).

Incident to learn from: on 7 Oct an AI browser click cancelled the wrong order (May-2038) because the page had
scrolled. Rule since then: **only Ray places or cancels WInS orders.** AI may fill a ticket up to Preview.

## 9. Open items (as of 14 Oct)

- [ ] **TNA**: write the 3 reflections (<= 100 words each) in the IPS doc "Deliverables" tab; copy the notes exactly.
- [ ] Fill the team sheet's Trade Log and units-held columns (needed to evaluate the implementation).
- [ ] **IPS Version 5** (47 + ~498 words): render check of the page/line count; soften absolute claims
      ("never below the floor", "cannot miss") or back them; add the trade-off sentence; put back the certainty evidence.
- [ ] **Request the school documentation letter** now.
- [ ] Final Report: start the experience log (dates, decisions, turning points) and the sources list now; the time
      between 9 Nov and 4 Dec is short.
- [ ] Make the Messy Roots -> "Roots First" link visible (explain it once, literally).

## 10. Sources and where things are in this repo

| What | Where |
|---|---|
| Official PDFs (guide, infographic, IPS + TNA instructions, client case, school template) + text versions | `competition/official/2026_27/` |
| Public SMApply pages snapshot (home, guide, client, deliverables, trading, wins, faqs) | `competition/official/2026_27/smapply_public_2026-10-14/` (live: https://wghsinvcomp.smapply.us/res/p/{slug}/) |
| Team's paste of the official rules pages | `team/google_drive/rules_readme.md` |
| Team Google Docs/Sheets, exported 14 Oct (IPS all tabs, Final Report, Strategy Notes, Notes & Discussions, sheets) | `team/google_drive/` |
| Old IPS PDF drafts (30 Sep) and the sheet snapshot | `team/ips_drafts/`, `team/Portfolio_and_Trading_Notes_snapshot.xlsx` |
| AI IPS exemplars (not for submission) | `team/ai_outputs/` |
| Judging criteria, winning-team portrait and self-scoresheet | `team/Winning Team Portrait and Scoresheet.md` |
| Scheduled checks (monitor, rules watcher, mock judges, evidence lab) and their reports | `ops/` |
| Research office (AI desks for checks and numbers, house rules, memos, `textcheck.py`) | `office/`, `.claude/agents/` |
| Strategy research (AI) | `research/insight_v1/`, `research/council_2026-09-27/`, `rab/` |
| Market data (Treasury curve, fact sheets, JPM LTCMA) | `competition/official_market_data/` |
| Last year (2025-26), benchmarking only | `competition/historical/`, `team/google_drive/2025_knox_wharton.md` |

Live team files (Google Drive, Knox account): IPS Report, Final Report, Strategy Notes, Notes & Discussions,
"Portfolio and Trading Notes" sheet (`1kvuN-Uz3_bBYOVJiyBHfkHSsTchKOioKELyxepe8h3M`), PM Dashboard sheet. The
exports in `team/google_drive/` are snapshots; **edit the Google versions, not the exports.**
