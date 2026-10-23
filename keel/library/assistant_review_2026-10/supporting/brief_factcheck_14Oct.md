# Fact-check: Team Caplet draft brief

I checked the draft against the repo at 2affd4c, the official texts, live pages fetched 14 Oct 20:21–20:38 UTC, and my own recomputations. Most of it holds up. Two things were overtaken after the draft's status time: two Wharton public pages changed, and the 14 Oct Treasury curve is now posted. There are also about 25 smaller errors. The draft itself contains no personal data.

## A. Errors that must be fixed

**A1. "No rule has changed" is now out of date (§3 Rules row, §4, Appendix).** Two of the seven public SMApply pages changed after the draft's 13:26 UTC fetch. I fetched each one twice (20:34 and 20:38 UTC). The other five pages still match the snapshot word for word.
- **FAQ.** The snapshot (`faqs.txt:42-43`) says "Investments permitted (for BOTH contributions):" and "Any stock … priced at $5 … or higher." The live page now says "Investments permitted (for BOTH contributions, the IPS and Final Report):" and "Any stock from any exchange available on WInS." The $5 wording has been removed.
- **Trading Details.** The snapshot (`trading.txt:43`) says "Your team may invest in:". The live page now says "Your team may invest in (for BOTH contributions):". The $5 stock line is unchanged.
- **Effect on the draft:**
  - The $5 minimum now stands only on Trading Details. Cite that page, not `faqs.txt:42-43` (affects §2, §4 and item 31). The stricter-rule reading still gives $5, and no stocks are held.
  - The "only WInS-listed securities, for both contributions" rule from the 6 Oct email is now written on the public FAQ, which makes it stronger.
  - The team should save a dated copy of the new pages and log the change.
- Evidence: `scratchpad/oct14/factcheck/dl/sm_faqs.html` and `sm_trading.html`.

**A2. The status time is stale, and the 14 Oct curve is now posted.**
- The checks ran 20:21–20:38 UTC, which is Thu 15 Oct 07:21–07:38 Sydney. Items 1–4 (due "Thu 15 Oct") are due today.
- The draft (§10) says the 14 Oct curve was not yet posted. It is now. Par yields on 14 Oct: 1y 4.53, 2y 4.82, 5y 5.00, 7y 5.09, 10y 5.19, 20y 5.57, 30y 5.52.
- Since 6 Oct: 10y down 8bp, 20y down 11bp.
- Ladder cost on 14 Oct (MODEL, my own pricer):

| Basis | Cost | Room under $300k | Fall that uses it up |
|---|---|---|---|
| IBTR note's basis (yields unchanged) | $295,993 | $4,007 | 13.9bp |
| WInS-listed, forward rates | $295,163 | – | 16.7bp |
| STRIPS, forward rates | $293,884 | – | 21.1bp |

  - So "about 0.16" (§2, §6) is now **about 0.14 points**.
  - Trigger B still does not fire on the 14 Oct close, which is the close the October rule uses (`archive/rab/trades/october_trade.md:18`).
  - My pricer reproduces the draft's 13 Oct figure ($295,295, 16.3bp) and the 6 Oct figure ($293,453, 22.7bp).

**A3. Item 31 asks to fix the freeze time in competition/COMPETITION.md, but that file is already right.** competition/COMPETITION.md already says 4:00 pm (lines 21 and 72). The wrong "5:00 pm" is in:
- `toolkit/config/wharton_private_2026_27.yaml:76`
- `toolkit/config/competition.yaml:17-18`
- `toolkit/docs/wharton_workflow_v2.md:116`

**A4. Item 3 leaves out some places where the WInS username appears.**
- It is also in all 5 `caplet/ai_outputs/*.docx` files (inside `word/document.xml`).
- It is also in the .xlsx snapshot (`xl/comments4.xml` and `xl/sharedStrings.xml`).
- §9 lists these, but item 3 does not.

**A5. §5 gives the wrong date for the $301,950 value.**
- competition/COMPETITION.md:188 says "Value about $301,950 on 13 Oct", not 9 Oct.
- The figure's real basis is the 9 Oct curve plus 12 Oct ETF closes (`ops/monitor_reports/2026-10-13 Caplet check.md:11-12`). On that basis I get $301,940.
- 13 Oct value: I get $302,389 to $302,497 (+0.80% to +0.83%), not $302,350 (+0.78%). Quote it as "about $302.4k (+0.8%)". On 14 Oct it is about $302.6k.

**A6. §7 attributes a quote to the wrong file.** "refine and proofread" comes from the student comment at `caplet/google_drive/ips_report/01_version_5.md:36`. competition/COMPETITION.md:199-200 says something different: "render check … soften absolute claims … add the trade-off sentence; put back the certainty evidence".

**A7. §3 and §12 say the routine run times are not in the repo, but §12 also gives the lab's time.**
- `keel/routines/claude_lab/BACKLOG.md:3` says "scheduled evidence lab (Sun/Wed 9pm)". No time zone is given.
- The other tasks' times of day are not in the repo.
- Fix: "only the lab's time is recorded".

**A8. §6 swaps two percentages.**
- Nov-2039 is 33% overlap and Nov-2040 is 41%. I re-ran `note_rules.phrase_overlap` on `05_…md:14-24`.
- §8's "WInS notes (21%)": the average over the 11 filled notes is **20.0%**.

**A9. §6 (IBTR) says "payments are never cut".**
- This contradicts §10 ("no payment is missed unless yields fall about 425bp"; I get about 421–425bp on the 13 Oct curve).
- It also breaks the draft's own rule against the word "never".

**A10. §2 states "message, tag, comment or email means disqualification" as if it were the rule.** The official wording is:
- "Teams may not contact the Competition client. Teams that violate this rule will be disqualified." (Rules & Roles, live 14 Oct)
- "Teams are not permitted to contact Laura Gao." (`client.txt:23`)
- The list of message, tag, comment and email is the team's reading of that rule. Label it that way.

**A11. §4 lists two items as "disqualification rules" that are not.**
- **Changing the team leader** needs the Advisor's written request and approval, but no penalty is stated.
- **"Invent teamwork and experiential stories"** is in the Ethics section ("We trust that you will not…"). The stated penalty there is that plagiarism or cheating is "grounds for dismissal".
- The rules that explicitly say "disqualified" are:
  - contacting the client;
  - removing a member without prior approval;
  - having fewer than 4 or more than 6 members;
  - changing advisor without approval;
  - paid advisors, consultants, agents or non-Wharton courses;
  - an inappropriate team name.

**A12. §2 says the TNA and IPS "must not" give a 2031 range, a reserve size or projections.** Wharton's word is "not expected" (`TNA-FINAL.txt:20-23`; `IPS-FINAL.txt:68-70`). Leaving them out is a team choice, not a rule.

**A13. Item 25 puts the steps in the wrong order.**
- Submitting on Thu 5 Nov Sydney means submitting on Wed 4 Nov ET.
- A trade "in US market hours by Thu 5 Nov ET" happens on Fri 6 Nov, 01:30–08:00 Sydney. That is after the IPS has gone in.
- The real freeze is Fri 6 Nov 4:00 pm ET (Sat 7 Nov 08:00 Sydney).
- Any unavoidable trade should come first, then the IPS submission.

**A14. The Appendix says "1 disputed", but §5 and the UNVERIFIED list also mark the cash reconciliation as disputed.** That makes 2 disputed findings.
- My own rebuild with standard accrued interest:

| Item | Amount |
|---|---|
| ETFs | $183,850.85 |
| VT | $26,524.61 |
| Bonds (clean price) | $84,801.22 |
| Accrued interest | about $1,349 |
| Commissions | $200 |
| **Cash left** | **$3,273.90 (settlement 7 Oct) or $3,262.95 (8 Oct)** |

- WInS reports $3,513.79, so about $240–251 is unexplained. This matches the two verifiers.

## B. Minor corrections

1. **§5 fill gain.** The five iBonds gained $787 against the 7 Oct closes. Adding VT (filled at 158.83 against a 7 Oct close of 159.64) gives a total of about **$923**. Say "$0.8–0.9k".
2. **§5 "bonds filled within 7bp".** The result depends on the method. My zero-curve check gives −7.7 to +5.8bp against the 5 Oct curve, and −3.8 to +8.6bp against the 6 Oct curve (the Nov-2041 bond is +8.6bp). Name the curve and method, or say "within about 9bp".
3. **§10 / Appendix.** The draft gives both $293,448 and $293,447. MONITOR.md:22 says $293,447. Use one figure.
4. **§10 table.** The STRIPS row ($293,055, 23.9bp) is on the forward basis, while the first row uses unchanged yields. Label the basis. My STRIPS figures on 13 Oct: forward $293,130 / 23.7bp; unchanged yields $294,016 / 20.6bp.
5. **Item 24 "exactly 3 pages".** The official rule is a 1-page title page plus a 2-page maximum (`IPS-FINAL.txt:84-85, 103-104`). Three pages is the maximum, not a requirement.
6. **§8 citations.**
   - The "Need to Humanise" title is at `02_v4_need_to_humanise.md:1`. Line 36 is the comment "This page is for us to humanise V3".
   - `caplet/docs/AI_USE.md:65-66` says "remove AI-style patterns", "AI-voice detector" and "blind voice tests". The word "humanise" does not appear there.
7. **Sources list.** The live-page slugs leave out `home`. Seven pages were checked.
8. **§12 "every instruction file forbids … submitting".** That is true of WATCHER.md:6 and LAB.md:6, but not of MONITOR.md:5-9 or JUDGE.md:6. Those two are read-only on docs and orders but do not mention submitting.
9. **§12 "if the Mac is asleep, a run is skipped and catches up later".** There is no evidence for this in the repo. Mark it UNVERIFIED.
10. **competition/COMPETITION.md:199** gives the IPS as "47 + ~498". The exact count is 47 + 497.

## C. Confirmed (no change needed)

**Dates and rules**
- Every ET-to-Sydney conversion and weekday is correct, including 15 hours now, 16 from Sun 1 Nov, and the 6 Nov market hours of Sat 01:30–08:00 Sydney.
- All 6 official PDFs match their manifest hashes.
- These quotes are verbatim on the live pages:
  - main page: "While the client is real…";
  - Rules & Roles: team leader at least 16, 4–6 members, paid advisors banned, the letterhead request;
  - AI policy: "must use their voice and words" and "must be recorded in your Works Cited pages";
  - plagiarism: "another's words or ideas as if they are one's own" and "grounds for dismissal";
  - Global Finale 29–30 Apr.
- `client.txt:23`, `faqs.txt:34/61/65/76/89/93-94`, `trading.txt:44/53`, `wins.txt:23`, `deliverables.txt:20-29/51/53/59`, `TNA-FINAL.txt:11-31/42-54` and `IPS-FINAL.txt` all say what the draft says.
- The school template fields are as the draft lists them (template lines 1–28).

**Repo citations and status**
- These lines are as cited: competition/COMPETITION.md:3/13/49/66/77/84/87-88/117/132/144/147/155-157/181/183-185/192-193/204; `wins_notes.csv:5/9/10/17/19`; MONITOR.md:22/33; WATCHER.md:13; `refresh_tickets.py:550-551`; `check_gate_c.py:163`; `E5_premortem.md:468`.
- No `research/insight_v1/AI_USE*` file exists.
- The trade log is empty (rows 2–210). Portfolio shows $300,000 and no units (`portfolio.csv:7, 20-31`). TN Analysis is empty. The Team note column is empty in 33 of 33 rows.

**The WInS book and the notes**
- The book table matches competition/COMPETITION.md and `portfolio_check.py`.
- Commissions are $200. VT is +$476 and 8.84% at cost.
- The largest order was 1.28% of that day's volume (IBTM).
- The 11 filled notes are 252–294 characters. The two May-2038 notes are identical.
- The gaps of 47, 320, 231 and 17 days are correct.
- IBTP's premium was 0.07% on 2 Oct. VT holds 10,088 stocks (31 Aug) at a 0.06% fee. The iShares iBond lineup ends at IBTR.
- Overlap scores: IBTR 2%, Feb-2037 13%, May-2038 9%, IBTM 30%, VT 28% with a 12-word shared run.

**Numbers**
- 13 Oct par yields are as stated.
- The biggest one-day fall in 2026 was 10.1bp, which is about the 10.2bp given.
- The 2028 floor costs $117.4–117.5k depending on the day-count convention.
- The return the payments need is 5.09%.
- A ±50bp move changes the book by about ±$9.5k using the funds' published durations (the draft says $9.4k).
- The correlation window started 27 Mar 2026, because IBTR first traded on 26 Mar. A true year gives +0.42.
- My rough model puts the chance the ladder costs more than $300k at 23–33%, which supports "1 in 4 to 1 in 3".
- The $503k / $466k / $447k figures are in `archive/rab/assumptions.md:11`. The All-Treasury figures are in `D_rivals.md:37`.

**IPS drafts and AI record**
- V5 word counts: 47 + 497 by spaces, 50 + 505 with hyphen parts, 51 + 500 with headings.
- The V5 quotes at lines 16, 20, 24, 26, 28 and 30 are accurate. V5 never uses the word "liquidity".
- V1 matches an AI example at about 97%, and the 30 Sep PDFs at about 85%.
- `caplet/docs/AI_USE.md` lines 49 and 90 are as described, and section 5 (lines 53–76) is the real log. The file was last changed 30 Sep.
- The mock log has 242 rows, dated 19–27 Sep.

**Repo housekeeping**
- The repo is public, with 17 branches, 0 forks and 1 star. Its description names the school, and 17 tracked files name it. There are 167 commits.
- The username was removed on 30 Sep (commit 9840758) and came back on 14 Oct (44f1296).
- Three of this year's Google files return HTTP 401 to anonymous access.
- The working-paper PDF has no end-of-file marker (it is truncated).
- The tests pass: 59 passed in a scratch copy.

**Last year**
- The required return was 11.6%, and about 12.5% with withdrawals from Year 3 (I get 12.51%).
- UTF was 17.7% and XCEM 5.01%; neither is on last year's approved list.
- The "Make up stories" comment is in last year's doc.
- `team_list.md:69` ($500,000) and lines 95–106 are as described. `notes_and_discussions.md:29` and `final_report.md:16/21/23` are as described. The client portrait is empty.

## D. Personal data

**The draft itself:** none found. It uses only first name plus initial, and the school is redacted.

**In the repo, to remove:**
- **WInS username:**
  - competition/COMPETITION.md:3 and :117;
  - `keel/routines/tasks/MONITOR.md:33` and `WATCHER.md:13`;
  - both `caplet/ips_drafts/*.pdf` (file names and page 1);
  - all 5 `caplet/ai_outputs/*.docx`;
  - the .xlsx (`xl/comments4.xml`, `xl/sharedStrings.xml`);
  - git history (commits c11b02f and 44f1296).
- **Surname:**
  - The .xlsx `docProps/core.xml` "lastModifiedBy" field holds a full name in "Surname, First" form. Its first name is not one of the six on the title page; whether it is a teammate's legal name is UNVERIFIED.
  - The same surname appears nowhere else in the team's files. Other matches in the repo are unrelated people.
- **School email:**
  - The .xlsx `xl/workbook.xml` stores a OneDrive path that contains the school account name.
  - `archive/rab/rescued/r4_hist_original.py:6` holds a Google Drive path with the email written using dashes, so a search for "@" will not find it.
  - There are no literal email addresses in tracked text files. The ones in `.env.example:12`, `toolkit/config/data.yaml:23` and `toolkit/pyproject.toml:13` are placeholders.
- **Third parties:**
  - `caplet/google_drive/team_list.md:32-36, 43-52` lists 15 students from three other teams.
  - Last year's doc (`caplet/google_drive/2025_[school]_wharton.md`) names non-team people in its comments and contains a working ChatGPT share link near line 3805.
- **Lower risk:** `/Users/ray` paths in `check_gate_c.py:35, :163` and `keel/routines/tasks/scheduled_tasks/*.md` show a first name only.

## E. Not re-verified (keep these labelled UNVERIFIED or AI opinion)

- simulated judge scores;
- the contents of last year's three public Google files, the password-like value, and "no password found";
- the count of about 54 files without a banner;
- the $3,670 worst floor shortfall;
- $161k gift at a $125k floor (the arithmetic is consistent, but I could not find a committed source);
- the 41-of-46 line page fit;
- how Docs counts words;
- the 6 Oct email's text and arrival time.

The fact-checker's working scripts and downloaded pages stayed in the session's temporary folder and are not in the repo; the independent checks that matter are in `../checks/`.