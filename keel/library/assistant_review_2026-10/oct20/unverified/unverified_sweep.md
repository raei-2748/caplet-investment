# UNVERIFIED sweep of the 20 Oct pack (public sources only)

AI-generated research (Claude Code) for Team Caplet, Tue 20 Oct 2026. These are fact checks only. Nothing here is wording for a deliverable. No login, no form, no contact with anyone. Pack files were not edited.

Paths: `W/` = `oct20/unverified/web/` (text copies; raw copies in `W/raw/`; every fetch is logged in `W/fetch_log.txt`). All fetches were made with curl through the proxy with a `?cb=` cache-buster, **Tue 20 Oct 2026 00:08-00:16 UTC = 11:08-11:16 Sydney (AEDT)**.

## 1. Summary

- Candidates: `grep -n UNVERIFIED` over the 4,165 `.md` files in `oct20/` (web/raw/data folders and `consistency/pre_fix_backup/` skipped) gives 10,142 hits. The checked copies (`*_checked.md`, `out/*.md`, `master/master_playbook.md`; 21 files) hold 241 hits. After de-duplication, about 60 distinct claims are left. Most of them need WInS, SMApply, Drive, GitHub or the team. **15 claims could be checked publicly. 9 are RESOLVED (all TRUE or sharpened; none FALSE), 2 are partly resolved, and 6 are STILL UNVERIFIED.**
- Most useful results:
  - FOMC statement on Wed 28 Oct is at **2:00 pm ET** (Fed calendar feed), with the press conference at 2:30.
  - treasury.gov says curves are "usually available ... by 6:00 PM Eastern Time". The 6 Nov curve is therefore expected by **Sat 7 Nov 10:00 Sydney**, after the 09:00 IPS deadline.
  - 27 Nov: NYSE closes at **1:00 pm ET**, and SIFMA recommends a **2:00 pm ET** bond close.
  - A **new 10-year note** is tentatively scheduled for auction on **Tue 10 Nov 2026** (announced 4 Nov, settles 16 Nov).
  - BLS dates via FRED: jobs report Fri 6 Nov, CPI Tue 10 Nov, both 8:30 am ET.
  - The iShares 2 Nov / 5 Nov distribution dates are reconfirmed. The schedule says BlackRock "reserves the right to change distribution dates".
  - APRA SPG 160 is listed as **Current**.
- Wharton's public pages still do **not** give the exact freeze cut-off, how headings count, the hour the Final Report instructions come out, or whether the TIPS/STRIPS ban covers ETFs. One new public line ties the freeze to the IPS due time (`W/sm_wins.txt:29`, quoted in R11).
- The AI-statement question is covered in `oct20/aistatement/ai_statement.md` and is not repeated here. Its verdict: the "Statement of AI Use" is a section of the AI Policy page that teams are "strongly encouraged to review". It is not a form to sign, and AI use is recorded in the Works Cited.
- Personal data: this file was scanned with the tokens in `oct16/tools/.pii_tokens` (tokens not printed). It contains no staff emails.

## 2. Resolved

| # | Claim (as in the pack) | Where it appears | Result | Exact quote (≤30 words) | Source, fetch time, saved line |
|---|---|---|---|---|---|
| R1 | FOMC 28 Oct statement at 2:00 pm ET "is the usual time … UNVERIFIED" | `master/master_playbook.md:51`; `master/parts/p1.md:51`; `forward/forward_view.md:288, 366`; `consistency/consistency_audit.md:55, 79` | **RESOLVED-TRUE.** Statement Wed 28 Oct 2:00 pm EDT = **Thu 29 Oct 05:00 Sydney**. Press conference 2:30 pm EDT = 05:30 Sydney | Feed: `"title": "FOMC Meeting", "time": "2:00 p.m.", "month": "2026-10", "days": "28"` and `"FOMC Press Conference", "time": "2:30 p.m."`. Practice (16 Sep statement): "For release at 2:00 p.m. EDT" | https://www.federalreserve.gov/json/calendar.json (the data behind /newsevents/calendar.htm), 00:09:57Z / 11:09 Sydney, `W/fed_calendar_json.txt:330, 179`. https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm, 00:10:29Z / 11:10, `W/fomc_sep16.txt:530`. The calendar page names no time zone; the Fed's releases are in ET |
| R2 | treasury.gov curve posting time UNVERIFIED (19 Oct curve was up by 5:38 pm ET); 6 Nov curve "about 09:30-10:00 Sat 7 Nov"; 20 Oct close "expected about Wed 21 Oct morning Sydney" | `artic_fixed/attribution_pack_checked.md:315`; `attrib/attribution_pack.md:304`; `forward/forward_view.md:366`; `verify_tnakit2/tna_fact_kits_v2_checked.md:237`; `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:237` | **RESOLVED-TRUE (a target, not a promise).** "By 6:00 PM ET": the 6 Nov curve is due by **Sat 7 Nov 10:00 Sydney** (after the 09:00 IPS deadline), and the 20 Oct curve by **Wed 21 Oct 09:00 Sydney**. Inputs are quotes taken at about 3:30 pm | "Yield curve rates are usually available at Treasury's interest rate website by 6:00 PM Eastern Time each trading day, but may be delayed due to system problems or other issues." | https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology, 00:11:57Z / 11:11 Sydney, `W/tsy_ycm.txt:329` (3:30 PM inputs: `:322`) |
| R3 | iBond next distribution "probably early November (UNVERIFIED)"; "dates UNVERIFIED" | `verify_tnakit2/tna_fact_kits_v2_checked.md:640`; `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:641`; `verify_drill2/drill_v2_checked.md:89` (V1 row); `verify_frblue/fr_prep_v2_checked.md:661` (old row) | **RESOLVED-TRUE.** Declared 30 Oct, ex/record **Mon 2 Nov**, paid **Thu 5 Nov 2026**. The next one is ex 1 Dec, paid 4 Dec. These dates apply to the monthly group that includes IBTM, IBTO, IBTP, IBTQ and IBTR. The dates can change. Amounts and WInS crediting remain unverified | "Blackrock intends to follow the above noted distribution cadence but reserves the right to change distribution dates or omit dividends as necessary" | https://www.ishares.com/us/literature/shareholder-letters/isharesandblackrocketfsdistributionschedule.pdf (dated "October 16, 2026"), 00:12:49Z / 11:12 Sydney, `W/distsched.txt:53, 58-60, 466`; tickers `:102-107` |
| R4 | New 15-Nov-2036 notes: "future issuance UNVERIFIED"; "Due from the Nov 2026 10-year auction" | `verify_rematch/verify_rematch.md:58, 122`; `rematch1R/rematch_1R.md:47, 276` (per verify_rematch) | **RESOLVED-TRUE (tentative).** A new (not reopened) 10-year note is announced **Wed 4 Nov**, auctioned **Tue 10 Nov** and settles **Mon 16 Nov 2026**. The schedule does not state the maturity date. By the usual mid-month convention it is 15 Nov 2036 (INFERENCE) | `<SecurityTermWeekYear>10-Year` … `<ReOpeningIndicator>N` … `<AnnouncementDate>2026-11-04` `<AuctionDate>2026-11-10` `<SettlementDate>2026-11-16` | https://home.treasury.gov/system/files/221/TentativeAuctionScheduleQ32026.xml ("Aug2026 Refunding Auction Calendar Official Ver 2", runs to 2027-01-30), 00:09:39Z / 11:09 Sydney, `W/tsy_tent_q3.txt:3, 1024-1031` |
| R5 | 27 Nov early close "time UNVERIFIED; a 1:00 pm ET close would be Sat 05:00 Sydney"; Thanksgiving times "UNVERIFIED (check NYSE/SIFMA)" | `verify_frblue/fr_prep_v2_checked.md:590, 704`; `frblue/fr_prep_v2.md:570`; `charts/charts_data_pack.md:362-363`; `artic_fixed/attribution_pack_checked.md:401` | **RESOLVED-TRUE.** Thu 26 Nov closed. Fri 27 Nov: stocks/ETFs close **1:00 pm ET = Sat 28 Nov 05:00 Sydney**; SIFMA bond close **2:00 pm ET = 06:00 Sydney**. SIFMA also confirms Wed 11 Nov (Veterans Day) as a bond holiday | NYSE: "Each market will close early at 1:00 p.m. … on Friday, November 27, 2026". SIFMA: "Early Close (2:00 p.m. Eastern Time): Friday, November 27, 2026" | https://www.nyse.com/markets/hours-calendars, 00:13:27Z / 11:13 Sydney, `W/nyse_hours.txt:26, 30`; https://www.sifma.org/resources/general/holiday-schedule/, 00:13:27Z, `W/sifma_hol.txt:51-56` |
| R6 | Employment Situation Fri 6 Nov 8:30 am: "BLS-direct confirmation UNVERIFIED"; BLS dates UNVERIFIED | `forward/forward_view.md:295, 366` | **RESOLVED-TRUE via the St. Louis Fed (FRED).** The BLS site still returns 403. Jobs report Fri 6 Nov 7:30 am CT = 8:30 am EST = **Sat 7 Nov 00:30 Sydney**. October CPI: **Tue 10 Nov**, 8:30 am EST = **Wed 11 Nov 00:30 Sydney**. Next jobs report Fri 4 Dec | "Friday November 06, 2026 / 7:30 am / Employment Situation"; "All times are US Central Time." CPI: "Tuesday November 10, 2026 / 7:30 am / Consumer Price Index" | https://fred.stlouisfed.org/releases/calendar?rid=50&y=2026, 00:13:39Z / 11:13 Sydney, `W/fred_empsit.txt:293-295, 299`; ...?rid=10&y=2026, 00:13:40Z, `W/fred_cpi.txt:293-295`. BLS 403s: `W/fetch_log.txt` |
| R7 | APRA SPG 160 (Nov 2013): "Whether it is still current was not checked"; SPS 160 "Not tried" | `verify_resnorms/verify_resnorms.md:68, 108`; `verify_resnorms/reservenorms_checked.md:104, 240`; `reservenorms/reservenorms.md:104, 240` | **RESOLVED-TRUE.** SPG 160 is "Current" (1 Nov 2013). SPS 160 is "In force" (1 Jul 2013) | "SPG 160 Defined Benefit Matters / Current / 1 November 2013"; "SPS 160 Defined Benefit Matters / In force / 1 July 2013" | https://www.apra.gov.au/industries/33/standards (browser UA), 00:15:57Z / 11:15 Sydney, `W/apra_super_std.txt:1182-1189`; https://www.apra.gov.au/standard/sps-160, `W/apra_std_sps160.txt:1011-1015` |
| R8 | Knox: Term 4 ends Thu 3 Dec; Fri 4 Dec is a staff PD day | `verify_pm2/premortem2_checked.md:256`; `verify_frblue/fr_prep_v2_checked.md:705` | **RESOLVED-TRUE (re-checked).** Whether anyone will sign on 4 Dec is still a school question (U-list) | "Thursday 3 December Presentation Day and Term 4 Concludes"; "Friday 4 December Staff Professional Development Day" | https://www.knox.nsw.edu.au/about/public-information/term-dates/, 00:15:15Z / 11:15 Sydney, `W/knox_terms.txt:345-349` |
| R9 | HSC written exams 13 Oct - 5 Nov; Business Studies Mon 26 Oct am, Economics Tue 27 Oct pm, Legal Studies Mon 2 Nov am, Physics Thu 5 Nov am | `verify_pm2/premortem2_checked.md:153, 158`; `master/master_playbook.md:51`; `ops/operating_plan.md:33` | **RESOLVED-TRUE (re-checked).** Whether any member sits the HSC is not public (team only) | "HSC Day 15 HSC Day 16 HSC Day 17 HSC Day 18 No exams"; "AM Legal Studies 9.25 am – 12.30 pm" | https://www.nsw.gov.au/sites/default/files/noindex/2026-05/2026-hsc-written-exam-timetable-01-05-26.pdf, 00:15:31Z / 11:15 Sydney, `W/hsc_tt.txt:126, 151, 168-172` |

### Partly resolved

| # | Claim | Where | Result | Quote | Source |
|---|---|---|---|---|---|
| P1 | Final Report instructions: "9 Nov ET"; "the instructions' release hour" UNVERIFIED | `master/master_playbook.md:51, 637`; `verify_frblue/fr_prep_v2_checked.md:704` | **Date RESOLVED-TRUE (9 Nov). Hour STILL UNVERIFIED.** No public page gives the time | "Instructions: Detailed Final Report instructions and requirements will be shared on November 9." | https://wghsinvcomp.smapply.us/res/p/deliverables/, 00:14:15Z / 11:14 Sydney, `W/sm_deliverables.txt:52` |
| P2 | Quarterly refunding Nov times UNVERIFIED (3:00 pm / 8:30 am in Aug) | `forward/forward_view.md:291, 293, 366` | **Dates RESOLVED-TRUE (Mon 2 Nov financing estimates; Wed 4 Nov refunding statement). Times STILL UNVERIFIED.** The usual time-of-day notice is not yet in Treasury's press releases (latest listed 19 Oct). Re-check about 26-30 Oct | "(The next release is scheduled for November 2, 2026)"; "(The next release is scheduled for November 4, 2026)" | https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/most-recent-quarterly-refunding-documents, 00:08:51Z / 11:08 Sydney, `W/tsy_qr.txt:325, 338`; press list `W/tsy_press.txt:305-325` |

## 3. Still unverified (public sources checked, no answer)

| # | Claim | Where (main) | Why still open | Best public quote | Source |
|---|---|---|---|---|---|
| U1 | Exact WInS freeze cut-off | `master/master_playbook.md:92, 639`; `artic_fixed/attribution_pack_checked.md:12, 313`; `artic_fixed/artic_bank_checked.md:22, 816`; `verify_pm2/premortem2_checked.md:15, 415`; `verify_runbook/runbooks_checked.md:130`; `verify_frblue/fr_prep_v2_checked.md:572`; `out/Caplet_Login_Checks_20Oct2026.md:22` | The public pages give the date only. **New:** the WInS page ties the freeze to the IPS due time (5:00 pm ET), not to the 4:00 pm close. The safe reading is unchanged: the last fill is at or before the Fri 6 Nov 4:00 pm ET close. A closed-market order fills "at the security's opening price when the market reopens" (`W/sm_trading.txt:34`), which would be after the freeze | "Official trading will end on November 6, when your Investment Policy Statement is due. At that time, your WInS portfolio will be frozen" | https://wghsinvcomp.smapply.us/res/p/wins/, 00:14:16Z / 11:14 Sydney, `W/sm_wins.txt:29`; also `W/sm_trading.txt:24`; `W/guide.txt:10-11` |
| U2 | Whether the TIPS/STRIPS ban covers ETFs built on them | `master/master_playbook.md:637`; `verify_vote2/votepack_v2_checked.md:903`; `verify_ipsfix/ips_fix_list_checked.md:294`; `verify_frblue/fr_prep_v2_checked.md:697`; `verify_drill2/drill_v2_checked.md:605` | The public FAQ bans TIPS and STRIPS by name and separately allows "Any ETFs available on WInS". It does not say which rule wins for TIP-type ETFs. This needs Wharton's answer (batch 2) | "TIPS (Treasury Inflation-Protected Securities)"; "STRIPS (Separate Trading …)" listed under "NOT permitted"; permitted: "Any Exchange-Traded Funds (ETFs) available on WInS." | https://wghsinvcomp.smapply.us/res/p/faqs/, 00:14:13Z / 11:14 Sydney, `W/sm_faqs.txt:44-56` |
| U3 | How Wharton counts words (headings, hyphens, numbers) | `master/master_playbook.md:316, 637`; `verify_ipsfix/ips_fix_list_checked.md:103, 213, 290`; `verify_semiblue/semiblue_checked.md:328`; `verify_vote2/votepack_v2_checked.md:904` | No public page or PDF defines a counting rule. Keep the strictest reading | "Maximum 50 words"; "Maximum 500 words" | IPS instructions PDF https://upenn.box.com/shared/static/0iib496jhswp30c12zhn6b2fret8dl30.pdf, 00:14:55Z / 11:14 Sydney, `W/ips_instr.txt:27, 31, 85-86`; TNA PDF `W/tna_instr.txt:43` |
| U4 | Any "required trading activity" | `master/master_playbook.md:637`; `verify_pm2/premortem2_checked.md:415`; `verify_vote2/votepack_v2_checked.md:901` | The public FAQ still says it exists but does not define it. The definition is probably on a logged-in page or in a weekly email | "Additionally, teams must meet the required trading activity and portfolio management guidelines throughout the competition." | `W/sm_faqs.txt:79` (same fetch as U2) |
| U5 | Candid's and NCN's reserve guidance | `verify_resnorms/reservenorms_checked.md:61, 236` | Both sites still return 403 with a browser User-Agent (Cloudflare "Just a moment..."). No content can be used | — | `W/fetch_log.txt` (ncn_reserves, ncn_reserves2, candid_reserves, candid_kb: 403; 00:16:18-26Z) |
| U6 | Live element at the semifinal | `verify_semiblue/semiblue_checked.md:68, 493` | No change: the same FAQ line was already weighed in the pack (semiblue 0.4). The 2026-27 format is not yet published | "deliver a short presentation (via video conference for the Semifinals …) … to a live panel of judges." | `W/sm_faqs.txt:92` |

Not attempted because of the time limit; all are publicly checkable later:
- JPM 2027 LTCMA figures (`verify_learn/learn_guide_checked.md:333`)
- VT country weights on Vanguard (`verify_drill2/drill_v2_checked.md:99`)
- US rating history (`verify_drill2/drill_v2_checked.md:606`)
- iBond SAI early-closure powers (sec.gov returned 403 earlier)
- Google Docs PDF-export behaviour (`verify_runbook/runbooks_checked.md:65, 155, 197`)
- the Taiwan Ministry of Culture cap

## 4. Login-only or team-only (not attempted)

- **WInS:**
  - Session Rules screenshot (position limit, trade-note limit, minimum price)
  - the 11 fill times and Transaction History
  - whether the book value counts accrued interest
  - when coupons and iBond payouts are credited
  - the May-2038 coupon schedule in WInS
  - the live Nov-2041 price
  - the 2x-volume rule for bonds
  - listings of SGOV/BIL/SHV and the 5.000% May-2037 and 2.000% Nov-2041 bonds
  - whether any Treasury is listed between Feb-2031 and Feb-2036
  - whether IEF/TLT are listed
  - whether WInS stays viewable after the freeze
  - the Week-1 email and announcements
  - the messages area label
  - the logged-in Trading Details page
- **SMApply (logged in):**
  - one application or separate tasks
  - Mark as Complete vs Submit
  - form fields and limits (date or ticker fields)
  - whether the form reopens or locks
  - the confirmation
  - who may submit
  - whether Contact Us sends a copy
  - Wharton's reply to batch 1
  - the exact name strings on the roster
- **Team email / Gmail:** when the 6 Oct email arrived and its exact text.
- **Google Drive / Docs:**
  - version history (who accepted v11; the 17-18 Oct edits)
  - who typed each comment
  - whether the two account names are one person
  - sharing settings
  - suggestion and print behaviour tested in a blank test Doc
- **GitHub (owner settings):**
  - Insights > Traffic and Forks
  - collaborators
  - whether outsiders visited or cloned the repo
- **Leader's machine:** the Claude desktop scheduled-tasks list, and whether the old `caplet-*` routines still run.
- **Team / school only:**
  - whether any member sits the HSC
  - Knox internal exam dates
  - whether staff will sign on Fri 4 Dec
  - school policy on crest and uniform
  - the "former Wharton judge" and the outside reader
  - why 167 VT shares were bought
  - the "0.3 to 0.2" story
  - which AI browser product was used

## 5. Files to update (fact wording only)

- `master/master_playbook.md:51` → "FOMC statement Wed 28 Oct 2:00 pm ET = Thu 29 Oct 05:00 Sydney; press conference 2:30 pm ET (Fed calendar feed, read 20 Oct; VERIFIED)."
- `forward/forward_view.md:288` → "Thu 29 Oct 05:00 Sydney (statement 2:00 pm ET, Fed calendar; VERIFIED)."
- `forward/forward_view.md:366` → "FOMC time VERIFIED (2:00 pm ET). The treasury.gov curve is 'usually available … by 6:00 PM Eastern Time' (VERIFIED). November refunding times not yet announced (UNVERIFIED). BLS dates confirmed by FRED; bls.gov itself returns 403."
- `forward/forward_view.md:295` → "Employment Situation Fri 6 Nov 8:30 am ET (FRED, 7:30 am CT; VERIFIED via FRED, bls.gov 403)." Add: "October CPI Tue 10 Nov 8:30 am ET = Wed 11 Nov 00:30 Sydney."
- `forward/forward_view.md:291/293` → keep "time UNVERIFIED". Dates VERIFIED (2 Nov, 4 Nov).
- `artic_fixed/attribution_pack_checked.md:315` → "usually by 6:00 pm ET (treasury.gov, VERIFIED, 'may be delayed') = by Sat 7 Nov 10:00 Sydney, after the 09:00 IPS deadline."
- `verify_tnakit2/tna_fact_kits_v2_checked.md:237` and `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:237` → "usually by 6:00 pm ET = by Wed 21 Oct 09:00 Sydney (treasury.gov; VERIFIED as usual practice)."
- `verify_tnakit2/tna_fact_kits_v2_checked.md:640` and `out/Caplet_TNA_Fact_Kits_v2_20Oct2026.md:641` → "Next ex/record date Mon 2 Nov, paid Thu 5 Nov (iShares schedule dated 16 Oct; VERIFIED; BlackRock 'reserves the right to change distribution dates')."
- `artic_fixed/attribution_pack_checked.md:74` → add "(dates may change: 'reserves the right to change distribution dates', schedule p.7)."
- `verify_frblue/fr_prep_v2_checked.md:590` → "Fri 27 Nov: NYSE closes 1:00 pm ET = Sat 28 Nov 05:00 Sydney; SIFMA bond close 2:00 pm ET (VERIFIED)."
- `charts/charts_data_pack.md:362-363` → "Closed Thu 26 Nov; Fri 27 Nov stocks close 1:00 pm ET, bonds 2:00 pm ET (NYSE, SIFMA; VERIFIED 20 Oct)."
- `artic_fixed/attribution_pack_checked.md:401` → "Thanksgiving week times: VERIFIED (closed 26 Nov; 1:00 pm ET stocks / 2:00 pm ET bonds on 27 Nov)."
- `verify_rematch/verify_rematch.md:58, 122` → "A new 10-year note is on Treasury's tentative schedule: announce 4 Nov, auction 10 Nov, settle 16 Nov 2026 (VERIFIED, tentative). Maturity 15 Nov 2036 by convention (INFERENCE)."
- `verify_resnorms/verify_resnorms.md:68, 108` → "SPG 160 listed 'Current' (1 Nov 2013) and SPS 160 'In force' (1 Jul 2013) on APRA's superannuation standards page (VERIFIED 20 Oct)."
- `verify_resnorms/reservenorms_checked.md:240` → "SPS 160 status checked: In force from 1 July 2013."
- `master/master_playbook.md:637` → "the instructions' release hour (date 9 Nov VERIFIED; hour UNVERIFIED)."
- `verify_frblue/fr_prep_v2_checked.md:704` → same split: date 9 Nov VERIFIED; release hour UNVERIFIED.
- `artic_fixed/attribution_pack_checked.md:313` (and the other freeze rows in U1) → add the public quote: the WInS page says trading ends "when your Investment Policy Statement is due. At that time, your WInS portfolio will be frozen". Exact cut-off is still UNVERIFIED. The last market fill is at or before 4:00 pm ET.
