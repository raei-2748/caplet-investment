# Verification of `oct20/forward/forward_view.md` (Wave H forward view)

AI verifier (Claude Code), Tue 20 Oct 2026, about 10:50-11:05 Sydney (23:50-00:05 UTC). This is MODEL checking for Team Caplet, **not text to submit**. Nothing here is TNA, IPS or Final Report wording. `forward_view.md` and every other file were left unedited. Nothing was committed.

Folder: `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct20/verify_forward/`, written `VF/` below. In the paths below, `FWD/` = `oct20/forward/`.

## Verdict

**The file mostly holds, but it needs one material fix before any of it is used.**
- **What reproduces.**
  - The engine, the D numbers, the analytic odds, the bottom-step rule, the WInS book and the calendar dates all reproduce.
  - A third seed (99) matched every table to within about 0.5 points.
  - An independent pricer gives D = $297,162 exactly.
- **The material fix: basis M2 inherits the iBond fee bug.** It is the "engY version", and engY treats the 0.07% fee as free. The file says the opposite ("M2 includes it").
  - Charged properly, M2 on 19 Oct is **$300,652, about $650 over the line**. The file says it is $139 under.
  - This contradicts the canonical `reconcile_3r.md` banner (3) and `fr_prep_v2_checked.md` §4.1 items 3-4.
- **Two Medium wording errors:**
  - The "correlation 0.97" with "Laura's January cost" is really correlation with the 6 Nov reading of that cost. Against the real 31 Dec cost it is about 0.51.
  - "8 of the 10 largest moves had no scheduled release" is wrong: two of those days had PCE and PPI releases.
- **Calendar.** Every date holds. One Sydney time is wrong and one auction time is wrong.
- **Personal data.** No PII-token hits and no drafted deliverable prose.

## Error table

| # | Location | Claim | Evidence | Severity | Exact fix |
|---|---|---|---|---|---|
| 1 | §0 item 1; §1 bases table M2 row; §1 bullet "M2 is the realistic one"; §2a-2e M2 rows; §4.1 "Fees" bullet (line 247) | M2 = $299,861, room **$139**, 0.5bp; "M2 includes it" (the 0.07% fee) | `fwd_lib.cost_M2` prices the fund on the net coupon (WAC − 0.07) and projects on the net coupon too, so the fee cancels. This is the same N1 bug as `verify_reconcile.md:28, 154` ("the 0.07% iBond fee is effectively free … $300.4k, not $299.9k"), carried into `reconcile_3r.md:3` banner (3) and `fr_prep_v2_checked.md` §4.1 item 3 ("about $300.4k with the 0.07% fee counted") and item 4 ("the 0.07% iBond fee is missing from the models"). Buying at the PV of the gross coupon and receiving net (`VF/scripts/indep.py`) gives **$300,652 (+$791), room −$652**. The break-even is a **2.25bp rise**. Odds over $300k are 54-55% at 6 Nov and 52-53% at 1 Jan (σ 0.71-1.0). The 1 Jan bottom survives in about 52-53% of paths (not 54-57%). Two or more steps down: 27-33% (not 24-31%) | **High** | Label M2 "fee-free (engY convention; the fee is NOT charged)". Add a fee-charged line: "about $300.6k on 19 Oct, about $0.65k over; over at 6 Nov in about 55%, at 1 Jan about 52%". Delete "M2 includes it". Change §0 item 1 "only $139 under the line" to "fee-free $139 under; about $650 over with the 0.07% fee charged". In line 247 write "about $1.4k nominal, about $0.93k in today's money (`fr_prep_v2_checked.md` §4.1 item 4); M2 as built also omits it in effect" |
| 2 | §0 item 4 (bold sentence); §3b "The trap"; §4.2 B1 "(correlation 0.97; R6)" | "The book and Laura's January cost move together (correlation 0.97)"; "A WInS gain therefore usually means a dearer January purchase" | `forward_sim.py:259-261` correlates the book with the D cost **on the 6 Nov curve** ("yields unchanged"). Against the cost on the 31 Dec curve (the real 1 Jan purchase), the correlation is **0.51-0.52** (σ 0.71 / 1.0, `VF/data/indep_out.txt`). Given the book is up, P(1 Jan D > $300k) is 51-56%. The "3 in 10 both" figure still holds (30-31%) | Medium | Write "the book and the 6 Nov reading of Laura's January cost (correlation 0.97; about 0.5 with the actual 31 Dec cost)". In §3b, change "usually means a dearer January purchase" to "usually comes with a dearer January cost as read on 6 Nov" |
| 3 | §0 item 5; §5d bullet "The ten largest"; §8 bullet 3 | "8 of the 10 largest one-day moves … came on days with no scheduled release" | `events_vol.py` tags only CPI, jobs and FOMC days. The FRED calendars (re-fetched) show **28 Mar 2025 = Personal Income and Outlays** (rid=54) and **10 Sep 2026 = PPI** (rid=46) | Medium | Write "8 of the 10 fell on days with no CPI, jobs report or FOMC decision (two of them had PCE or PPI releases)". In §8, write "most of the biggest days had no CPI, jobs or Fed release" |
| 4 | §5a row "Thu 22 Oct" | Sydney "Fri 23 Oct" for the TIPS auction *and* jobless claims (8:30) | zoneinfo: claims 8:30 EDT = **Thu 22 Oct 23:30** Sydney; TIPS close 1:00 pm = Fri 23 Oct 04:00 | Low | Write "Thu 22 Oct 23:30 (claims) / Fri 23 Oct 04:00 (TIPS)" |
| 5 | §5a row "Mon 26 … Thu 29 Oct" | All four auctions "+1 day 04:00" | The 2-year FRN closes at **11:30 AM ET** (TreasuryDirect FRN records). The 28 Oct FRN is therefore Thu 29 Oct **02:30** Sydney | Low | Write "04:00 (FRN 02:30)" |
| 6 | §1 Horizons | "33 to the 3 Dec close" | The code's own day list: 3 Dec is bond day **31** (`days` in both JSONs). Count: 9 in Oct, 19 in Nov, 3 in Dec. Results use the correct index | Low | Change 33 → 31 |
| 7 | §5 "FRED release times" | "FRED appears to show US Central time (my inference, UNVERIFIED)" | The FRED page states it: "All times are US Central Time" (`VF/web/fred_50.txt:274`) | Low | Mark VERIFIED and quote the line |
| 8 | §0 item 5; §4.0 timing fact; §5a freeze row | Freeze close Fri 6 Nov 4:00 pm ET with no caveat | `attribution_pack_checked.md` §7 (A11): "exact WInS cut-off UNVERIFIED; trading.txt:24 says only 'ends on November 6'" | Low | Add "(exact WInS cut-off UNVERIFIED)" |
| 9 | §2e title; §4.0 R4 | Rule "(150k − reserve − top-up − $3.7k)" | The source code has R = 150,000 − gap27 − buffer and bottom = floor((R − 3,700)/5,000)×5,000 (`oct19/coupon/scripts/coupon_options.py:182, 213`). "Reserve" = the 3r **buffer B = $10k** (and **$0 for option 1**), not Laura's 2033 operating reserve. `numbers_refresh.md:143` gives only (R − $3,700). The arithmetic is right: boundaries $301,300 / $306,300 / $311,300 | Low | Write "(150k − B − top-up − $3.7k), where B = $0 (option 1) or the $10k 3r buffer; not the 2033 operating reserve" |
| 10 | §4.0 R4 (and §2e) | Cites `fr_prep_v2.md:265`; no fee caveat | The checked copy (R13, `fr_prep_v2_checked.md:283`) adds "with the 0.07% fee counted option 1's median minimum sits on the $140k/$145k edge (REC banner (3))" | Low | Cite `fr_prep_v2_checked.md:283` and carry the caveat |
| 11 | §2b; §4.0 R5; §4.1 "Fees"; §4.3 | Cites `oct20/frblue/fr_prep_v2.md` §4.1 "lines 288-313" | The file is superseded (banner). In the checked copy §4.1 is at **lines 304-334**, and items 3-4 changed (see #1) | Low | Re-point to `oct20/verify_frblue/fr_prep_v2_checked.md` §4.1 (304-334) |
| 12 | §3a, §3c, §4, §5 (all `attribution_pack.md` cites) | Cites the superseded pack | Every cited fact is unchanged in `artic_fixed/attribution_pack_checked.md`: $303,393.47 total; holdings at 121-135; DV01 $187.2; distribution schedule; −$225 May-2038; $1,538.75; timing table; DST. Changed: freeze cut-off UNVERIFIED (#8), "about $601", and $600.95 = an unchecked synthetic input (see #13) | Low | Re-point every cite to the checked copy |
| 13 | §6 book row | "$600.81 against the pack's $600.95 (rounding of the per-share amounts)" | Checked pack A10: the cited amounts give $600.81; the $600.95 came from the synthetic run, "its input was not rechecked". No rounding explanation is supported | Low | Write "$600.81 = cited amounts × holdings; the pack's $600.95 is an unchecked synthetic input (A10)" |
| 14 | §4.0 R4 | Quotes "Freeze the rule, not the dollars" at `numbers_refresh.md:143` and `fr_prep_v2.md:265` | That wording is at `numbers_refresh.md:409` (lower case). Line 143 and fr_prep read "Freeze the rule, not '$145,000'". §2e's "minimum steps of $5k" (in quote marks) is in no source found | Low | Fix the cite to `:409`, or quote fr_prep's wording. Drop the quote marks on "minimum steps of $5k" |
| 15 | §4.0 R2 | "The IBTR note … reads: 'On the 6 Oct Treasury curve, …'" | The filed note (7 Oct 4:42:53 AM, `snap/main/team/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md:15`) begins "Future funding: IBTR is for Laura's fifth payment in 2037." The quoted two sentences are exact. The cancelled 6 Oct note (:37) says "0.3", not "about 0.2" | Low | Prefix the full first sentence, or say "(sentences 2-3, exact)". Cite the filed export. `tna_fact_kits_v2.md` is unchecked; same text in `oct20/out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:430` |
| 16 | Header | "about 10:55-11:50 Sydney" | The fetches ran 23:18-23:35 UTC = 10:18-10:35 Sydney, and the file was saved 23:43 UTC = 10:43 Sydney | Low | Write "about 10:15-10:45 Sydney" |
| 17 | §4.2 B1/B2 | B2 ($300,000-303,400) "As B1: attribute the gain" | Against the 19 Oct value, B2 is a fall. Against the $300k start, it is a gain. The reference point is unstated | Low | Name the reference point (the $300,000 start or the 19 Oct value) |
| 18 | `FWD/scripts/check_repro.py` (output only) | Prints "DV01 per bp: 2.9" | `(o[1]-o[2])/200` over a ±1bp bump should be /2: the true value is $289/bp. The doc's $289 comes from `forward_sim` and is right | Low | Script display only. No doc change |

## What holds (checked)

**Levels**
- **D $297,162, room $2,838, DV01 $289/bp, break-even −9.8bp.** Re-run `check_repro.py` and an independent bootstrap (`VF/scripts/indep.py`) both give exactly $297,162.
- **M1 $298,446.**
- **M2 (fee-free) $299,861.** The engY `rung_terms` give $299,861 / $307,148 / $292,768 at 0 / ∓25bp.

**Seeds and analytic odds**
- Seed 99 (20,000 paths, `VF/data/fwd_seed99.json`, `tables_seed99_vs_A.md`, `bands_seed99.txt`) matches every §2 table, band, path-wise figure, bottom figure and book figure to within about 0.5 points.
- Analytic P(D > $300k):
  - 6 Nov: 27.9% (σ 0.71) and 33.9% (σ 1.0).
  - 1 Jan: **37.9% (σ 0.71) and 41.3% (σ 1.0)**, matching `numbers_refresh.md:99`.
- Shifts to the step boundaries: −14.2bp to $301,300 and −31.1bp to $306,300.

**The 2031 bottom**
- The steps fall at $301,300 and $306,300 (option 1: 145 → 140 → 135; 3r: 135 → 130 → 125).
- D survival of 63-68% is consistent with the sheet's 61.1% (D) to 71.5% (A).

**Simulation mechanics**
- **Dates:** weekdays 20 Oct-31 Dec, less SIFMA's 11 Nov, 26 Nov and 25 Dec. That gives 14 days to 6 Nov and 50 to 31 Dec.
- **Demeaning:** per node. The mean D change is −$141 a day, about 24bp over 50 days.
- **Same-day bootstrap:** curve and VT changes are drawn as one shared index. 198 of 200 days have a VT value; the 2 gaps are around Good Friday.
- **Correlations:** ρ(10y, VT) is −0.475 in 2026 and −0.127 over two years.
- **Accrued interest at 9 Nov settlement = $1,710.6.** A hand check gives 222.0 + 435.3 + 380.9 + 370.0 + 302.3. At 20 Oct it is $1,491.70 (= pack).

**The WInS book**
- No-move value $304,112. Median $304.0-304.2k. P(< $300k) 13-21%.
- Analytic SD $3,786 at σ 0.71. IBTM DV01 is $49/bp.

**Decision table (§4) against the team rules**
- No requirement conflicts with "quote no level; state the rule": the TNA and IPS carry rules only, and levels appear only in the Final Report, dated.
- No requirement adds WInS P&L to Laura's projections (case:132-133; Guide:70-79 verified).
- The valuation date, the 6 Nov close, matches `fr_prep_v2_checked.md` §4.1 item 1.
  - That is an AI prep-pack rule pending the official 9 Nov instructions.
  - Note that `attribution_pack_checked.md:321` suggests a 3 Dec WInS run "or the team's chosen valuation date". The FR pack should settle this.
- The odds ranges in §4.1 (10-32%, 21-45%, 43-50%, $1.3-6.3k) match §2f.

**Calendar (all dates confirmed on the re-fetched pages)**
- **FOMC:** 27-28 Oct; 8-9 Dec* with SEP; minutes "three weeks after", so Wed 18 Nov.
- **BEA:**
  - 29 Oct: GDP advance and September PCE.
  - 4 Nov: trade.
  - 25 Nov: GDP second estimate and October PCE.
  - 23 Dec: GDP third estimate and November PCE.
- **FRED:**
  - Jobs: Fri 6 Nov and Fri 4 Dec.
  - CPI: Tue 10 Nov and Thu 10 Dec.
  - PPI: 13 Nov and 15 Dec.
  - Retail sales: 17 Nov and 16 Dec.
  - JOLTS: 3 Nov and 1 Dec.
- **Treasury:**
  - Refunding releases "scheduled for November 2" and "November 4" (August releases at 3:00 PM and 8:30 AM).
  - Auctions: 21 Oct 20-year reopening, $13bn, 1:00 PM; 22 Oct 5-year TIPS; 26-29 Oct; 9/10/12 Nov; 18-19 Nov; 23-25 Nov.
- **SIFMA:** closed 11 Nov, 26 Nov and 25 Dec; early closes 27 Nov, 24 Dec and 31 Dec.
- **2 U.S.C. §7:** quote exact, so the election is Tue 3 Nov 2026.
- **Sydney times** (zoneinfo; AEDT is UTC+11; US DST ends Sun 1 Nov):
  - The freeze and IPS fall at 08:00 and 09:00 on Sat 7 Nov.
  - The jobs releases fall at 00:30 on Sat 7 Nov and 00:30 on Sat 5 Dec.
  - The TNA deadline is Sat 24 Oct 08:00 and the FOMC statement is Thu 29 Oct 05:00.
  - All of these are right.
- **BLS** returned 403 "Access Denied" even with a browser User-Agent, so it is still UNVERIFIED directly.

**Privacy and prose**
- **Personal data:** 0 hits for the `.pii_tokens` list in `forward_view.md` and in the `FWD/` folder. No student names, usernames or account numbers. "her" always means Laura.
- **Drafted prose:** none. §4 is requirements and §8 is learning notes.

## Sources (re-fetched with plain curl through the proxy and a cache-buster; UTC on Mon 19 Oct 2026 = Tue 20 Oct Sydney +11h)

Every page except BLS was byte-identical to the forward folder's copy, apart from page tokens.

| Source | URL | Fetched (UTC) |
|---|---|---|
| Fed FOMC calendar | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | 23:52:26 |
| BEA release schedule | https://www.bea.gov/news/schedule | 23:52:27 |
| FRED release calendars, 2026 (rid 50, 10, 46, 9, 192, 180) | https://fred.stlouisfed.org/releases/calendar?rid=N&y=2026 | 23:52:28-31 |
| FRED release calendars, 2025 and 2026 (rid 54, 53, 9, 46, 192) | same pattern | 23:54:56-23:55:07 |
| Treasury quarterly refunding | https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/most-recent-quarterly-refunding-documents | 23:52:41 |
| SIFMA holidays | https://www.sifma.org/resources/general/holiday-schedule/ | 23:52:42 |
| 2 U.S.C. §7 | https://www.law.cornell.edu/uscode/text/2/7 | 23:52:42 |
| TreasuryDirect upcoming auctions | https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json | 23:52:43 |
| TreasuryDirect FRN search | https://www.treasurydirect.gov/TA_WS/securities/search?type=FRN&format=json | 23:58:20 |
| Tentative auction schedule | https://home.treasury.gov/system/files/221/TentativeAuctionScheduleQ32026.xml | 23:52:53 |
| BLS (403) | https://www.bls.gov/schedule/news_release/empsit.htm, …/cpi.htm, …/schedule/2026/home.htm | 23:52:54 |
| treasury.gov 2026 par curve (identical; last row 19 Oct) | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv | 23:59:06 |

**Files:**
- `VF/web/` (pages and `fetch_log.txt`)
- `VF/scripts/indep.py`, `tz_check.py`, `h2t.py`
- `VF/data/fwd_seed99.json`, `tables_seed99_vs_A.md`, `bands_seed99.txt`, `indep_out.txt`, `run_seed99.log`
