# Team Caplet brief: what to do next, and why

**Status:** Prepared Wed 14 Oct 2026, about 23:45 Sydney (12:45 UTC), from the repo at commit 2affd4c. Fact-checked against live pages and data until Thu 15 Oct 07:38 Sydney (20:38 UTC Wed 14 Oct). Because of that, items due "Thu 15 Oct" are due **today**. This is an **AI-prepared review for planning only. It is not submission text.** Do not copy any of it into the Trading Notes Analysis (TNA), the IPS or the Final Report. Record this review in the team's AI-use log.

**Terms used in this brief**
- **bp (basis point):** 0.01 percentage point. So 14bp = 0.14 points.
- **ET:** US Eastern time. Sydney is 15 hours ahead of ET now. From Sun 1 Nov it is 16 hours ahead.
- **iBonds (IBTM to IBTR):** iShares funds. Each holds Treasuries that mature in one year, then the fund winds up. IBTM = Dec 2032, IBTO = Dec 2033, up to IBTR = Dec 2036. A fund's final payout is not fixed.
- **IBTM:** in WInS this one fund does two jobs. It pays the 1 Jan 2033 payment, and it stands in for the floor.
- **Floor:** the part of the 2028 deposit put into IBTM so that it returns about $150k by 2033. The exact size is decided in vote set B. The floor sets the bottom of the 2031 co-sponsor range.
- **Ladder:** the holdings that pay Laura's ten $50,000 payments, 2033 to 2042.
- **STRIPS:** zero-coupon Treasuries. Since the 6 Oct Wharton email they are not allowed in Laura's real plan.
- **Tab 15:** a tab in the IPS Google Doc. It holds change notes written by an AI assistant.
- **Vote set A / vote set B:** two bundles of team decisions (items 11 and 19).
- **Gates G1-G6:** six checks to finish before writing the TNA reflections (§6).
- **October rule, triggers A-D:** the team's pre-set rule for one possible October trade (archive/rab/trades/october_trade.md). A = repair an unfilled order, B = yields fall, C = spare cash, D = bond swap.
- **Routines:** scheduled AI checks on Ray's Mac. They are the *watcher* (reads rules pages), the *monitor* (portfolio and drafts), the *mock judges*, the *gates* (checklists) and the *evidence lab*.
- **archive/rab/ ("the kit"):** AI-built research and trade tools in the repo.
- **Readers / verifiers:** the AI reviewers that checked the repo for this brief.
- **MODEL:** a computed estimate, not a fact.
- **AI opinion:** a simulated judge, not Wharton.
- **supported / aligned / tested / refined:** Wharton's own words for how a trade relates to the strategy (Trading_Notes_Analysis-FINAL.txt:12, :29).

---

## 1. Do this

All dates are **Sydney** unless marked ET. Each item gives: **what to do**, *who · by when*, then → the section that explains why.

**If you do only seven things before the TNA:** items 1, 4, 11, 13, then 15, 16 and 18.

### Now / this week (Thu 15 to Sun 18 Oct)
1. **Agree that students write every word that is submitted.** Label IPS V5, Tab 15 and the AI example notes "AI reference only". Do not edit or "humanise" them. *Whole team · Thu 15 Oct.* → §8
2. **Keep AI out of WInS and SMApply.** Delete the rule "AI may fill a ticket up to Preview". It is in competition/COMPETITION.md:193 and in the live routine copies on the Mac. For every trade, hold a team vote and have a second student read the ticket back. *Ray W. · Thu 15 Oct.* → §5, §12
3. **Make the GitHub repo private.** Add teammates as collaborators first. If it stays public, write down why. *Ray W. (his decision) · Thu 15 Oct.* → §9
4. **Name owners** in the team sheet, not the repo. Roles: trader, checker/recorder, rates analyst, 3 reflection writers, TNA editor, IPS section authors, format checker, historian/AI-log keeper, rules lead, privacy lead (not Ray), repo helper (not Ray), and one unpaid outside reader. *Ray W. + team · Fri 16 Oct.* → §11
5. **Remove personal data from current files** using the list in §9. On archive/rab/rescued/r4_hist_original.py:6, blank out the path; keep the file, because other files cite it. Remove the two IPS-draft PDFs from the repo. *Privacy lead · Fri 16 Oct.* → §9
6. **Set last year's three link-shared Google files to Restricted, and unshare last year's ChatGPT link.** Change last year's WInS password anywhere else it is used. If the owner has left, ask the advisor and record what happened. *File owner, else advisor · Fri 16 Oct.* → §9
7. **Tell all six students: Laura is a real person, so never contact her.** Also go over the other disqualification rules. Save dated copies of the two public pages that changed on 14 Oct, and log the change. *Rules lead · Fri 16 Oct.* → §4
8. **Log the October-rule check on the 14 Oct close.** Triggers A, B and C do not fire (MODEL). Check in WInS whether the 1.375% Nov-2040 bond is now listed (trigger D). *Trader + checker · Fri 16 Oct.* → §10
9. **Record these privately on the team Drive:** the exact team name and roster names from SMApply; the TNA form's fields and limits; the Week-One, 6 Oct and later Wharton emails (date, sender, subject, arrival time in ET); and any activity rule, word for word. *Ray W. + rules lead · Sat 17 Oct.* → §4, §6
10. **Ask the advisor to request the signed school letter now.** Have it in hand by Fri 20 Nov. The names must match the roster. Never put it in the repo. *Ray W. via advisor · ask Fri 16 Oct.* → §4
11. **Hold vote set A and log it.** Confirm the name Root-and-Branch. Agree one floor description with no absolute words, what "rounded down" means, the full shortfall order and the ladder-cost basis. Decide whether to run trigger D or retire the October rule (D's trade window closes Wed 21 Oct 06:30). *Whole team · Sun 18 Oct.* → §6, §7, §10
12. **Back-fill a real AI-use log from 1 Oct.** Include who wrote and who typed each WInS note, and which AI example notes each person saw. *AI-log keeper + every student · Sun 18 Oct.* → §8

### Trading Notes Analysis (due Sat 24 Oct 08:00 = Fri 23 Oct 5:00 pm ET; do these in order)
13. **Fill the Trade Log from WInS Order History and Transaction History:** fills, accrued interest, commissions and cash after each trade. Settle the cash gap. Confirm that each candidate note's order shows "Filled". Save screenshots to the team Drive only. *Recorder + checker · Sun 18 Oct.* → §5
14. **Re-run the ladder cost on the IBTR note's basis** using the latest posted curve. Commit the script and its dated output. Writers quote this figure with its date. *Rates analyst · Mon 19 Oct.* → §10
15. **Vote on the three picks.** Suggested: IBTR (7 Oct 4:42 AM ET), IBTM (6 Oct 10:01 PM ET) and VT (7 Oct 8:27 PM ET). Alternate: the Feb-2037 bond (7 Oct 12:24 AM ET). Never pick a note on a cancelled order. *Whole team · Mon 19 Oct.* → §6
16. **Students write the three reflections themselves.** Each is 100 words or fewer (aim for 95 or fewer). The topics are in §6. No AI drafting. *Reflection writers · Tue 20 Oct.* → §6, §8
17. **The outside reader scores the drafts. The editor checks** word counts, numbers and the match with vote set A. *TNA editor + outside reader · Wed 21 Oct.* → §6
18. **Paste each note straight from WInS.** A second student checks it character by character. Ray submits and screenshots the confirmation. *Ray W. + checker · Thu 22 Oct.* → §6

### IPS (due Sat 7 Nov 09:00; trading freezes Sat 7 Nov 08:00)
19. **Hold vote set B and log it:** floor size; where the 2027 leftover and cash from early-maturing bonds wait; the certainty standard; review triggers; and which figures, if any, go in the IPS. *Whole team · Tue 27 Oct.* → §7
20. **After the vote, write a bullet outline, then a fresh draft** in a new one-tab Doc with every AI draft closed. Give each section one named author. One human outside reader reads it. *IPS authors · outline Wed 28 Oct, draft Sat 31 Oct.* → §7
21. **Check the exported PDF.** Our safety targets (Wharton's limits are 50 and 500 words):
    - pitch 45 words or fewer and IPS 470 or fewer, taking the higher count from two counters, with headings counted;
    - title page plus at most 2 pages;
    - Times New Roman 12, double-spaced, 1-inch margins;
    - 5 MB or less, with no links, images or comments.

    Copy the title page from the private roster note and the username from the WInS login. Two students check it. *Format checker · Wed 4 Nov.* → §7
22. **Submit the IPS on Thu 5 Nov, then make no more trades.** If a trade is unavoidable, it comes first: vote, second check, and place it by Wed 4 Nov 4:00 pm ET (= Thu 5 Nov 08:00). *Ray W.* → §4, §5

### Final Report (due Sat 5 Dec 09:00 = Fri 4 Dec 5:00 pm ET)
23. **Keep the experience journal true.** Fill its blanks. Back-fill 1-14 Oct from real notes. Write short minutes after every meeting. Say where AI was involved. *Historian · back-fill Sun 25 Oct, then weekly.* → §11, §13
24. **Draft the Works Cited AI entry only from the real log.** Never use caplet/docs/AI_USE.md sections 1-4. *AI-log keeper · draft Sun 29 Nov.* → §8
25. **Take holdings and numbers only from WInS and one dated numbers sheet** on the team Drive. Use no toolkit charts and no "PASSED" outputs. *Rates analyst · 10 Nov to 4 Dec.* → §10, §14
26. **Check the SMApply Deliverables page each morning from Tue 10 Nov** until the instructions appear. *Rules lead.* → §4, §12

### Housekeeping
27. **Update the routines on the Mac** using the table in §12:
    - move the TNA judge and gate to Wed 21 Oct, and the IPS gate to Wed 4 Nov;
    - point the 1 Nov judge at the student draft;
    - check authorship first;
    - check that each pick shows "Filled";
    - take names from the private roster note.

    *Ray W. · Sun 18 Oct.* → §12
28. **Fix the stale repo facts listed in §14:** competition/COMPETITION.md; the 5:00 pm freeze time in three files; `min_share_price_usd: 3` (should be 5) in two configs; roster "pending"; and every pointer that calls V5 "current". *Repo helper · Sun 18 Oct.* → §4, §14
29. **Fix the live Google Docs:** the portfolio is $300,000, not $500,000; add the TNA date; delete the "practice account" line. *Rules lead · Fri 16 Oct.* → §4
30. **Add a "superseded" banner to stale files, or archive them.** Mark caplet/docs/AI_USE.md sections 1-4 and toolkit/outputs/ai_use_log.jsonl "do not use". Remove the unrelated personal PDF. Fix check_gate_c.py:163. *Repo helper · Sun 25 Oct.* → §14

---

## 2. Nuances and traps

**Rules**
- **Laura is a real Wharton alum.** Only the financial scenario is invented. The official rule is "Teams may not contact the Competition client", and breaking it means disqualification. The team's cautious reading: any message, tag, comment or email counts as contact.
- **What Wharton says leads to disqualification:**
  - fewer than 4 or more than 6 members at any time;
  - removing a member, or changing the advisor, without prior approval;
  - paid advisors, consultants or agents, or non-Wharton courses;
  - contacting the client;
  - an inappropriate team name.
- **Other rules:**
  - Changing the team leader needs the advisor's written request and approval (no penalty is stated).
  - The Ethics section asks teams not to invent teamwork or experience stories.
  - Plagiarism is "grounds for dismissal".
- **Only the team leader submits** in SMApply, and must be 16 or older. No substitute is named, so the only backup plan is to submit early.
- **Stock minimum: use $5.**
  - After our 14 Oct snapshot, the live FAQ dropped its "$5" wording, but Trading Details still says $5.
  - WInS accepts $3 stocks; that does not make them allowed. The stricter rule wins.
  - We hold no stocks.
- **Laura's real plan may use only WInS-listed securities.** Both public pages now say the permitted list is "for BOTH contributions", and the FAQ adds "the IPS and Final Report". So this rule is now on a public page, not only in the 6 Oct email.
- **Cash is not on the permitted list** shown on 14 Oct. A 27 Sep capture listed it; whether Wharton changed this is UNVERIFIED. WInS holds cash at 0% anyway. For the real plan, say where waiting money sits (vote set B).
- **WInS accepting an order does not mean the order is allowed.** Last year WInS accepted closed-end funds that were off the approved list.
- **No minimum trading activity** appears in any rule found so far. Never trade just to reach a count.

**Times (time-zone traps)**
- **TNA:** Fri 23 Oct 5:00 pm ET = Sat 24 Oct 08:00 Sydney.
- **Trading stops** Fri 6 Nov 4:00 pm ET = Sat 7 Nov 08:00 Sydney. The IPS is due one hour later.
- **Order fills:** orders placed while the US market is closed fill at the next open. Bond orders fill at end-of-day prices (archive/rab/trades/friday_checklist.md:22).
- **Thu 5 Nov in Sydney is Wed 4 Nov in ET.** A trade "on Thu 5 Nov ET" happens after a Thu 5 Nov Sydney submission. So any trade must come first.
- **US clocks change on Sun 1 Nov.** Sydney goes from 15 to 16 hours ahead.

**WInS and the notes**
- **Notes cannot be edited.** The TNA quotes each one exactly, and Wharton checks it against an executed trade.
- **Four notes sit on cancelled orders:** IBTR, Feb-2037, May-2038 and Nov-2039. There are two IBTR notes. The cancelled one says "0.3"; the filled one (7 Oct 4:42 AM ET) says "about 0.2". Use only the filled one.
- **The Feb-2037 bond is the 4.750% issue.** competition/COMPETITION.md:181 wrongly says 5.000%.
- **Repo values are model estimates, not WInS readings.** WInS profit is not judged.
- **The WInS pie chart labels the iBonds "Long Equities".** They are Treasury funds (competition/COMPETITION.md:98).
- **iBond distributions arrive as cash at 0%.** That needs no trade. But V5 says income is "reinvested", so settle which it is.

**Numbers**
- **The IBTR note's "about 0.2 points" was true on 6 Oct.** On the 14 Oct close it is about **14bp (0.14 points)** (MODEL). Always quote it with its date, and quote only the first row of the §10 table.
- **IPS V5's "$292,000 at late-September yields"** uses the old STRIPS basis. Do not quote it.
- **Do not quote:**
  - ±$10.8k for a 0.5-point move (about ±$9.5k is better);
  - "+0.55 correlation over 1 year" (the window was about 6.5 months; a true year gives +0.42);
  - "about 20bp left" (9 Oct);
  - "$289,200".
- **Model results dated 28 Sep on the STRIPS basis are background only.** Re-run them before quoting.

**Wording**
- **The real floor is IBTM, whose payout is not fixed.** Never write "never below the floor", "cannot miss", "guaranteed", "secure", "promised", "risk-free" or "never". Do not say iBonds are "matched", "locked" or "owned" payments.
- **All three deliverables are judged together.** Use one name, one floor description and the same dated numbers in all three.
- **The TNA and IPS are "not expected" to give** a final 2031 range, a reserve size or projections (TNA-FINAL.txt:20-23; IPS-FINAL.txt:68-70). Leaving them out is the team's choice, not a rule.
- **The IPS should focus on the framework,** "rather than … presenting detailed financial calculations" (IPS-FINAL.txt:51-52). Keep figures few.
- **The client profile's pull quote is the case's words.** Do not present it as Laura speaking.

**AI policy**
- AI may be used for brainstorming. "AI-generated work may not be submitted as your own." Students "must use their voice and words".
- Rewording ("humanising") AI text does not make it yours.
- The IPS allows no citations, so AI use is recorded in the Final Report's Works Cited.
- **Overlap scores do not prove who wrote something.** Keep dated drafts as proof instead.
- caplet/docs/AI_USE.md contains a false, ready-made "student-authored" statement. Never use it.

**Privacy**
- The repo is public, and git history keeps every old version.
- **Never commit:** the school letter, roster screenshots, the final IPS PDF (its title page shows the WInS username), surnames or emails.

---

## 3. Where we stand

| Area | Status (14-15 Oct) | Next |
|---|---|---|
| Rules | Two public pages (FAQ, Trading Details) were edited on 14 Oct after our 13:26 UTC snapshot. The other five are unchanged. The $5 rule is still on Trading Details. | Item 7 |
| Roster | Submitted and locked. The exact names are not on file. | Item 9 |
| WInS | 11 of 200 trades used; all 11 orders filled 7-8 Oct. Cash $3,513.79 (reconciliation DISPUTED). Value about $302.6k on 14 Oct (MODEL). Plan: hold. | Item 8 |
| Trade Log | Empty | Item 13 |
| TNA | Picks suggested, not voted. No reflections yet. Form fields unknown. | Items 13-18 |
| IPS | V5 is AI-generated (team comment). 47 + 497 words. No student draft. | Items 19-22 |
| Final Report | Instructions arrive 9 Nov ET | Item 26 |
| School letter | Not requested as of 13 Oct | Item 10 |
| AI-use record | The real log stops 30 Sep. Parts of caplet/docs/AI_USE.md are false. | Item 12 |
| Roles | None recorded | Item 4 |
| Journal | 10 entries, stops 7 Oct | Item 23 |
| Privacy | Repo public. The username, an email inside a file path and a full name are exposed. | Items 3, 5, 6 |
| Ladder room | About 14bp on 14 Oct (IBTR note's basis, MODEL) | Item 14 |
| AI routines | 10 tasks on Ray's Mac. Three are scheduled too late or too early for the plan. | Item 27 |

---

## 4. Rules and dates

**Checked:**
- the seven public SMApply pages (home, guide, client, deliverables, trading, wins, faqs), live at 13:26 UTC and again at 20:34 and 20:38 UTC on 14 Oct;
- the Wharton main page, Rules & Roles, FAQ and AI-policy pages (live, 14 Oct);
- the six official PDFs against their manifest hashes;
- the Sydney/ET conversions;
- competition/COMPETITION.md, caplet/START_HERE.md and the configs.

**Found:**
- **Two public pages changed on 14 Oct, after our snapshot.**
  - **FAQ.** The snapshot (faqs.txt:42-43) reads "for BOTH contributions" and "priced at $5 … or higher". The live page now reads "for BOTH contributions, the IPS and Final Report" and "Any stock from any exchange available on WInS.", so the $5 wording is gone.
  - **Trading Details.** It now reads "Your team may invest in (for BOTH contributions):". Its $5 line is unchanged (trading.txt:44).
  - The other five pages match the snapshot word for word, and all six PDFs match their hashes.
  - Effects: cite Trading Details for the $5 minimum. The WInS-only rule now stands on a public page. Save dated copies of both pages.
- **Possible change to cash: UNVERIFIED.** The 27 Sep capture listed "Cash" first under the permitted list (keel/library/insight_v1/phase_A/case_register.md:941-944). The 14 Oct snapshot and the live page do not. It is unknown whether Wharton edited the page or the earlier capture was a slip.
- **The sample school-letter template is now posted** (deliverables.txt:53).
- **Deadlines** are all 5:00 pm ET, with no extensions (deliverables.txt:20-29, :51):

  | Deadline | ET | Sydney |
  |---|---|---|
  | TNA | Fri 23 Oct | Sat 24 Oct 08:00 |
  | Trading ends | Fri 6 Nov 4:00 pm | Sat 7 Nov 08:00 |
  | IPS | Fri 6 Nov | Sat 7 Nov 09:00 |
  | Final Report instructions | Mon 9 Nov | about Tue 10 Nov |
  | Final Report + school letter | Fri 4 Dec | Sat 5 Dec 09:00 |

  - The 4:00 pm trading end comes from the team's copy of the Session Rules (wins_notes.csv:5).
  - Semifinal dates are TBD. The Global Finale is 29-30 Apr 2027.
- **The freeze time is wrong in three files, not in competition/COMPETITION.md.** competition/COMPETITION.md:21 and :72 correctly say 4:00 pm. These say 5:00 pm:
  - toolkit/config/wharton_private_2026_27.yaml:76;
  - toolkit/config/competition.yaml:17-18;
  - toolkit/docs/wharton_workflow_v2.md:116.

  caplet/START_HERE.md:47 gives no time. How WInS treats an order still open at the freeze is UNVERIFIED.
- **Laura is real.** competition/COMPETITION.md:49 says she is fictional. Wharton's main page says: "While the client is real, the financial scenario is developed specifically for the competition." Client page: "Teams are not permitted to contact Laura Gao" (client.txt:23). No onboarding file says this.
- **Disqualification wording** (Rules & Roles, live 14 Oct):
  - "disqualified": contacting the client; removing a member without prior approval; fewer than 4 or more than 6 members; changing the advisor without approval; paid advisors, consultants or agents, or non-Wharton courses; an inappropriate team name (Wharton may instead require a new name).
  - Changing the team leader needs the advisor's written request and approval; no penalty is stated.
  - "Invent teamwork and experiential stories" is in the Ethics section. That section's penalty: plagiarism and cheating are "grounds for dismissal".
  - None of this is in competition/COMPETITION.md.
- **Stock minimum.**
  - competition/COMPETITION.md:66 says the Session Rules "apply" where they differ. That points the wrong way: the stricter rule ($5) wins.
  - toolkit/config/competition.yaml:44 and toolkit/config/wharton_private_2026_27.yaml:72 hold `min_share_price_usd: 3`.
  - No stocks are held, so nothing was breached.
- **The 6 Oct email** exists in the repo only as a quote (competition/COMPETITION.md:87-88). competition/COMPETITION.md:77 credits "US Treasuries" to that email, but the US-only limit comes from the Session Rules (wins_notes.csv:9).
- **"Required trading activity"** (faqs.txt:76) is not defined anywhere.
  - Trading Details says frequent trading is not required (trading.txt:53).
  - Trades are not scored (wins.txt:23).
  - The Week-One email is still logged as unread (wins_notes.csv:19).
  - Risk: low.
- **Who submits:** the team leader, who must be 16 or older. The TNA form's fields are recorded nowhere, and the team's own task to record them by 12 Oct is overdue (keel/library/insight_v1/phase_E/E5_premortem.md:468).
- **TNA format** (TNA-FINAL.txt:11-31, 42-54):
  - three notes from executed trades, quoted "exactly as it appears in WInS";
  - one reflection per note, 100 words or fewer;
  - each reflection covers why, fit with the strategy, and the link to Laura's goals, funding or risk;
  - must be consistent with the later IPS.
- **IPS format** (IPS-FINAL.txt:29-41, 68-74, 81-131):
  - a 1-page title page with the official team name, names exactly as on the roster ("First Name, Last Initial") and the WInS username;
  - then at most 2 pages: pitch of 50 words or fewer, IPS of 500 words or fewer;
  - Times New Roman 12, double-spaced, 1-inch margins, PDF of 5 MB or less;
  - no charts, images, links, footnotes or citations;
  - non-compliant = "not considered for semifinal selection"; the strategy cannot change after the deadline.
- **Title page against the roster.**
  - The repo has no record of the names as submitted.
  - CLAUDE.md:46-47 and toolkit/config/team_roster.json still say "pending", although CLAUDE.md:8 says submitted.
  - One Doc comment author uses a first name that is not on the title page (01_version_5.md:36). Treat this only as a reason to check.
  - Whether the roster says "Caplet" or "Team Caplet" is UNVERIFIED.
- **The school letter template** asks for: letterhead; a date; the administrator's position; school name, country and full address; the advisor's full name; team name; each student's first and last name, team leader first; the administrator's signature and date (template lines 1-28). It was not requested as of 13 Oct (competition/COMPETITION.md:132). Rules & Roles also asks semifinalists for letterhead documentation; whether that is a second request is UNVERIFIED.
- **Small errors to fix:**
  - competition/COMPETITION.md:13 says the gap "changes from 14 to 16 hours". It is 15 now and 16 from 1 Nov.
  - The team info pack says the portfolio is $500,000 and leaves out the TNA date (caplet/google_drive/team_list.md:69, 95-106).
  - The STRATEGY tab says the TNA uses "a practice account" (notes_and_discussions.md:29).

**Action:** items 7, 9, 10, 22, 26, 28, 29.

---

## 5. WInS book and trade notes

**Checked:** competition/COMPETITION.md:172-193; keel/routines/tasks/portfolio_check.py; the 15 notes copied on 13 Oct (caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md); and opening prices and volumes, the treasury.gov curve, and the iShares and Vanguard pages (14 Oct).

**The book: 11 filled orders, 11 of 200 trades**

| Holding | Quantity | Fill |
|---|---|---|
| IBTM | 4,503 shares | 21.65 |
| IBTO | 1,024 shares | 22.86 |
| IBTP | 927 shares | 23.90 |
| IBTQ | 894 shares | 23.46 |
| IBTR | 853 shares | 23.24 |
| VT | 167 shares | 158.83 |
| 4.750% Treasury 15 Feb 2037 | $20,000 face | 96.019 |
| 4.500% 15 May 2038 | $20,000 | 93.076 |
| 4.375% 15 Nov 2039 | $18,000 | 90.005 |
| 4.250% 15 Nov 2040 | $18,000 | 87.724 |
| 3.125% 15 Nov 2041 | $20,000 | 74.955 |

**Found:**
- **Fills.**
  - The ETFs filled at the next open: 7 Oct for the iBonds and 8 Oct for VT. Those prices were below the 7 Oct closes, by about $0.8-0.9k in total. That was luck.
  - The bonds filled within about 9bp of the curve (the exact figure depends on the method).
  - Every order went in while the US market was closed (6 Oct 7:55 PM to 7 Oct 8:27 PM ET). The plan had been Fri 2 Oct.
- **Rule checks** (from the execution reader):
  - every security is allowed;
  - the largest order was 1.3% of that day's volume (IBTM);
  - commissions were $200 (6 × $25 + 5 × $10);
  - nothing was sold;
  - cancelled orders are not trades and cost nothing (faqs.txt:61, 65).
- **The Trade Log is empty** (trade_log.csv:2-210). The Portfolio tab still shows $300,000 cash and no units (portfolio.csv:7, 20-31), and TN Analysis is empty. The notes themselves are safely copied. What is missing: fills, accrued interest, commissions and cash after each trade.
- **The Feb-2037 coupon is wrong in competition/COMPETITION.md.** WInS shows B-T-4.750-15022037 (CUSIP 912810PT9). competition/COMPETITION.md:181 says 5.000%, which is a May-2037 bond WInS does not list. Lines 183-185 leave out the coupons.
- **VT: 167 shares bought against 164 planned** (+$476; 8.84% at cost against 8.7%). That breaks the kit's own rule, "never more than the plan share" (archive/rab/trades/refresh_tickets.py:550-551). No reason is recorded. Keep the position and record why.
- **Cash reconciliation: DISPUTED.**

  | Rebuild | Cash left |
  |---|---|
  | Standard accrued interest (fact-check): ETFs $183,850.85 + VT $26,524.61 + bonds $84,801.22 + accrued about $1,349 + commissions $200 | $3,273.90 (settled 7 Oct) or $3,262.95 (settled 8 Oct) |
  | One reader, using WInS's 15 Aug last-coupon date for May-2038 (competition/COMPETITION.md:96) | $3,498.90 to $3,509.84 |
  | WInS reports | $3,513.79 |

  Between about $4 and $251 is unexplained, depending on the method. Settle it from Transaction History (item 13).
- **Notes.**
  - The 11 notes on filled orders are 252-294 characters long (limit 300).
  - 4 notes sit on cancelled orders; the two May-2038 notes are identical.
  - Notes cannot be edited (competition/COMPETITION.md:84).
- **The 7 Oct incident.**
  - An AI browser click cancelled the open May-2038 order (competition/COMPETITION.md:192-193). Only that one cancellation is attributed to AI. Why the other three orders were re-placed is not recorded.
  - No rule was broken and nothing was lost.
  - The rule adopted afterwards still lets AI "fill a ticket up to Preview", and notes are typed at Preview (wins_notes.csv:17). WInS cancels instantly with no confirmation (competition/COMPETITION.md:85).
- **Claims inside the notes:**
  - Correct: the payment dates; the 47-, 320-, 231- and 17-day gaps; "no iBonds fund ends 2037-43"; "no WInS Treasury matures in 2033 or 2035".
  - Verified: IBTP's "0.07% on 2 Oct" (iShares daily history; save a dated copy) and VT's "about 10,000 stocks at 0.06%" (10,088 stocks on 31 Aug; Vanguard, fetched 14 Oct).
  - Unsupported: Nov-2039's "chose Nov over May 2039". Nothing records WInS listing a May-2039 bond.
  - The May-2038 wording is loose, and the Nov-2041 note uses unexplained jargon.
- **Values are model estimates.**
  - competition/COMPETITION.md:188 gives about $301,950 (+0.65%) and labels it "13 Oct". Its real basis is the 9 Oct curve plus 12 Oct ETF closes (ops/monitor_reports/2026-10-13 Caplet check.md:11-12).
  - Recomputed: about $302.4k (+0.8%) on 13 Oct and about $302.6k on 14 Oct (MODEL).
- **iBond distributions** (rough estimate: about $600 a month) will sit as cash at 0%. The November payment may land around 6 Nov, freeze day (competition/COMPETITION.md:190). No trade is needed.

**Action:** items 2, 13, 18, 22, 25.

---

## 6. Trading Notes Analysis picks

**Checked:** three simulated judges (AI opinion, not Wharton), the execution reader, the authorship reader, the official TNA brief and the IPS drafts.

**Recommendation (the team decides):**

| Pick | Order time (ET) | Wharton label | AI judge average |
|---|---|---|---|
| IBTR | 7 Oct 4:42 AM | tested | 8.2 |
| IBTM | 6 Oct 10:01 PM | refined if gate G3 confirms; otherwise aligned | 8.2 |
| VT | 7 Oct 8:27 PM | aligned | 7.0 |
| Alternate: 4.750% Feb-2037 bond | 7 Oct 12:24 AM (copy the exact time from WInS) | aligned | 6.0 |

The other notes scored: Nov-2040 6.2, IBTO 6.0, Nov-2041 5.8, Nov-2039 5.7, IBTP 4.7, May-2038 4.2, IBTQ 4.0. These are AI opinion. Gaps under 1 point mean nothing.

**Why this trio** (all three judges ranked it first):
- **IBTR** is the only note with a test set before trading.
- **IBTM** is the only trade that serves both objectives: the first payment and the facility floor.
- **VT** is the only growth decision, and the TNA brief opens with "approach to growth".
- Together they cover the plan's three parts in order.

**How much each note's wording overlaps the AI example notes.** Two measures exist, and neither proves who wrote a note:
- **Shared three-word phrases** (archive/rab/trades/note_check.py:16):
  - Nov-2040 41%, Nov-2039 33%, IBTM 30%, VT 28% (with a 12-word run copied word for word): "rewrite or disclose";
  - Feb-2037 13%, May-2038 9%, IBTR 2%: pass;
  - average over the 11 filled notes: 20.0%.
- **Whole-text similarity** (0-100): 54.5 to 77.1 across all 11 filled notes. IBTR scores 61.0; Nov-2040 is highest at 77.1. Notes on the same facts always look somewhat alike.

**Authorship trade-off:**
- VT's note repeats a 12-word clause from an AI example note and uses "promised". If VT is picked, name that AI example in the Works Cited.
- The pick with the least AI wording is IBTR + IBTM + Feb-2037, but it loses the growth decision.
- Recommendation: keep VT and disclose. Avoid Nov-2040 (41%) and Nov-2039 (33%), which also has an unsupported claim.

**Swap rules (decided with vote set A, Sun 18 Oct):**
- Feb-2037 replaces IBTM only if no shared floor wording is agreed.
- Feb-2037 replaces IBTR only if the team cannot explain IBTR's basis.
- Feb-2037 never replaces VT.
- If Feb-2037 is used, the IPS must say where its early cash waits (Tab 15 suggests a short-term Treasury ETF; 15_tab_15.md:35).

**Gates before the pick vote (Mon 19 Oct):**
- **G1. Vote set A** (Sun 18 Oct): name (Root-and-Branch, settled 1 Oct, final_report.md:21), floor wording, shortfall order, where the 2027 leftover sits, ladder-cost basis.
- **G2. Ladder re-run** committed (Mon 19 Oct, item 14).
- **G3. IBTM timeline** (Sun 18 Oct). Check Gmail and Doc history: did the 6 Oct email arrive before the 10:01 PM ET order? That decides "refined" against "aligned". The email's text and arrival time are UNVERIFIED.
- **G4. October rule** logged or retired (Sun 18 Oct; §10).
- **G5. Trade Log** filled, with each pick shown as "Filled" (Sun 18 Oct).
- **G6. AI-use log** entry for after 30 Sep (Sun 18 Oct).

**Topics each reflection should cover.** These are labels only. Students choose the words.
- **IBTR:**
  - what the fund holds and when it pays out; that the payout is not fixed;
  - the test done before trading, and its result (6 Oct curve, WInS-listed holdings only);
  - the pre-set rule for a shortfall: what tops it up, what shrinks, and the MODEL limit (§10);
  - the client link (the case's "high degree of certainty"; portfolio-only funding);
  - the dated room-left figure from item 14;
  - WInS scale against the real plan.
- **IBTM:**
  - its two jobs, and why one fund does both (WInS lists no Treasury maturing Feb 2031 to Feb 2036);
  - what changed on 6 Oct, and how the team's floor wording changed (depends on G3);
  - what "rounded down" means (vote set A);
  - the co-sponsor link, with no dollar figure.
- **VT:**
  - breadth and fee (verified figures above);
  - its share of all the money, and why;
  - the trade-off, in the team's own words;
  - its role in 2033 (the half-split rule);
  - the case's risk words;
  - what a stock fall can and cannot affect.

**Traps:**
- Use only the filled IBTR note. Its "about 0.2" is now about 0.14 (14 Oct, MODEL); give the date.
- IBTM's note says "provides a floor" next to "payout not fixed". Explain the rounding down.
- VT's "promised minimum" overclaims. Do not repeat it.
- Give no 2031 dollar range, reserve size or WInS gain.
- Use no wording from V5, Tab 15, the AI example notes or this brief.

**Decided here (the team can overrule):**
- The story of "0.3" becoming "0.2" stays out of the TNA and goes in the Final Report.
- Submit on Thu 22 Oct Sydney (= Wed 21 Oct ET).

**Action:** items 11, 13-18.

---

## 7. IPS review

**Checked:** V5, Tab 15, the older tabs and the 30 Sep PDFs; the official IPS brief and the case; three simulated judges (AI opinion); and two compliance verifiers.

**Found:**
- **V5 cannot be submitted.**
  - A student's Doc comment calls it "Best version that AI generated; We cannot submit as it is and we still need to refine and proofread it" (01_version_5.md:36).
  - competition/COMPETITION.md:199-200 plans to edit V5 ("soften absolute claims … add the trade-off sentence; put back the certainty evidence").
  - Editing AI text does not make it the students' own work. Write fresh from an outline.
- **Format passes, but only just.**
  - V5 word counts: 47 + 497 counting by spaces; 50 + 505 if each part of a hyphenated word counts; 51 + 500 if headings count. Wharton does not say how it counts (UNVERIFIED).
  - Google Docs may count a figure like "$292,000" as two words (a 2017 test; UNVERIFIED today).
  - So the plan uses 45 / 470 on the higher of two counters. That is stricter than the AI spec's 48 / 470 (keel/library/insight_v1/ips_spec.md:7, :47).
  - Headings are allowed ("You do not need to address these points separately", IPS-FINAL.txt:66). If you use them, count them.
  - Page fit: about 41 of 46 lines on Letter paper (not re-verified). One blank line between paragraphs can push it to a 4th page.
  - The 30 Sep PDFs in caplet/ips_drafts/ are stale. They contain old wording and the username. Never upload them.
- **Absolute claims in V5.** V5 says:
  - "secure" (:16);
  - "depends mainly on the US government" (:20);
  - "sized to return that remainder" (:24);
  - "never below the floor" (:28);
  - "cannot miss the range" (:30).

  The IBTM note says "the final payout is not fixed" (05_…md:19). The modelled worst floor shortfall is about $3,670, which a floor quoted rounded down to $145k covers (MODEL, not re-verified). So this is a wording fix, not a strategy flaw.
- **"High degree of certainty" is not defined, though the case asks for it** (Client_Profile.txt:97-99). "Liquidity" never appears.
  - Under the WInS-only rule, what coupons earn matters: the ten holdings deliver about $503k at their own yields, $466k if coupons earn 2%, and $447k at 0%, against $500k needed (archive/rab/assumptions.md:11; MODEL, 28 Sep).
  - Re-run this before quoting it.
- **Rules that can be read two ways:**
  - floor size: V5 says "the remainder"; competition/COMPETITION.md:155-157 says "about $150k";
  - "rounded down" (V5:30 against Tab 15:30);
  - where the 2027 leftover sits (Tab 7 puts it in VT);
  - "held without trading" (V5:26) contradicts the 2028 purchase.
- **The pitch's co-sponsor claim is unsupported.** The case does not say co-sponsors "rarely pay to run it"; it says they "may" fund operations (Client_Profile.txt:85-86). The case's own reason for putting payments first is that the portfolio must fund them (:91-92).
- **V5:28's "raise the expected contribution" is wrong under the plan's own rule.** A smaller floor lowers the median gift: about $174k at a $150k floor against $161k at $125k (MODEL; no committed source; not re-verified). Only the total money rises.
- **"Why not all Treasuries?" needs an answer ready.** An old model gave All-Treasury a bigger gift because it gives everything away. The case values Laura's flexibility (Client_Profile.txt:102-103). Those model figures (rab D_rivals.md:37) are on the superseded STRIPS basis. Do not quote them.
- **Two specs conflict on figures.** The AI spec allows "at most one" computed figure (ips_spec.md:70). The official brief only asks for framework over "detailed financial calculations" (IPS-FINAL.txt:51-52). The official brief wins. Decide the number of figures in vote set B.

**Simulated judge consensus (0-10; AI opinion, not re-verified):**

| Criterion | Score |
|---|---|
| Investment Strategy | 7 |
| Client Knowledge | 6 |
| Portfolio Analysis | 5 |
| Articulation of Competition Experience | 4 |
| Creativity & Presentation | 5 |
| Format | Passes, thin margins |

**Content objectives for the students' own draft** (outcomes, not wording):
1. Every certainty word is literally true and matches the TNA.
2. One stated standard for "high degree of certainty". Name the remaining risks and which part of the portfolio covers each. State the priority order between the payments and facility money, floor included. Cover liquidity.
3. One definition each for: the floor, the 2031 bottom and top, the 2033 gift, Laura's cushion, and where the leftover and early cash wait.
4. One principle each for: floor size, the half split, the cap, no lock in 2031, no de-risking before 2033. State the trade-off once. Optional figures, if vote set B keeps them: the rough mix after 2028 (about 66% ladder, 25% floor, 9% stocks) and the return the payments need (about 5.1% a year on $300k; MODEL).
5. A pitch built on the case's rule. No dollar figure. 45 words or fewer.
6. Time order: 2027, 2028, review, 2031, 2033, 2033-42, then risks. Define each term the first time it appears. One strategy name.
7. Base Laura's risk view on the case's words ("willing to take thoughtful risks"; "an appropriate balance"). Show what a bad market year does.
8. Any dollar figure is on the WInS-listed basis and dated, or it comes out.

**Vote set A (Sun 18 Oct):** confirm the name; floor description; banned words; what "rounded down" means; the full shortfall order, floor included; the October rule.
**Vote set B (Tue 27 Oct):** floor size; where the leftover sits; where early-maturity cash waits; the certainty standard and its test; review triggers; Laura's cushion after 2033; the principles in objective 4; which figures, if any.

**Process:**
- Bullet outline: one row per decision, with the reason, the evidence and an owner. No sentences.
- Section authors draft with every AI file closed.
- Word budget of about 470: objectives about 80, risk profile 65, construction 105, review 55, 2031/2033 rules 95, risks 70.
- Each author must be able to defend every sentence aloud.
- AI may only check facts, numbers and format.

**Action:** items 1, 11, 19-22.

---

## 8. AI policy and authorship

**The policy** (live pages, fetched 14 Oct):
- AI is allowed for brainstorming and idea generation.
- "AI-generated work may not be submitted as your own."
- Any AI use "must be recorded in your Works Cited pages".
- Students "must use their voice and words".
- Plagiarism includes "another's words or ideas as if they are one's own" and is "grounds for dismissal".
- The criteria reward "an authentic team voice" (deliverables.txt:59).
- The IPS bans citations; its sources go in the Final Report (IPS-FINAL.txt:123-125).

**Found:**
- **Where the IPS drafts came from.**
  - V1 is an AI example with the name swapped (about 97% match; marked "EXEMPLAR ONLY", 13_old_versions_v1.md:6).
  - The 30 Sep PDFs match the AI examples at about 85%.
  - V4 is titled "Need to Humanise" (02_v4_need_to_humanise.md:1), and a comment says "This page is for us to humanise V3" (:36).
  - The team calls V5 "AI generated" (01_version_5.md:36).
  - Tab 15's change notes are written in an assistant's voice (15_tab_15.md:22-36; author UNVERIFIED).
  - Who wrote V2, V3, V4 and Tab 10 is UNVERIFIED.
- **Overlap scores cannot prove authorship.** Claude's own 6 Oct rewrites overlap its 30 Sep examples by about 20% on average. That is the same as the WInS notes (20.0%).
- **WInS notes.**
  - The checker's flags are in §6.
  - Nothing records who wrote or typed any note: the "Team note" column is empty in 33 of 33 rows.
  - Whether AI typed any note at Preview is UNVERIFIED.
  - Notes cannot be edited, so the fix is honest disclosure plus reflections written by students.
- **The AI-use record.**
  - caplet/docs/AI_USE.md was last changed 30 Sep.
  - Its sections 1-4 describe a different platform. Lines 49 and 90 hold false, ready-made "student-authored" statements.
  - toolkit/outputs/ai_use_log.jsonl is 242 mock rows dated 19-27 Sep.
  - competition/COMPETITION.md:144 points to a log that does not exist.
  - Section 5 (lines 53-76) is a real log up to 30 Sep. Keep it and extend it.
  - Not logged anywhere: V4, V5, Tab 15, AI example notes v13 and v14, the 6 Oct AI-draft notes column, the AI browser in WInS, the routines.
- **The public repo records plans to "remove AI-style patterns"** and to use an "AI-voice detector" and "blind voice tests" (caplet/docs/AI_USE.md:65-66). If the IPS stays close to V5, that record looks like evasion. Keep the record and describe it honestly. Do not delete it.
- **DISPUTED: should the team email Wharton before the TNA about AI help with the notes?** Both verifiers say it is optional. The Works Cited is the official place to disclose, and judges read all three deliverables together. If unsure, use the official Contact Us form (faqs.txt:93-94).

**From now on:**
- AI **may**: check facts and numbers; count words, pages and format; list problems as bullets; brainstorm.
- AI **may not**: draft, rephrase or "humanise" deliverable sentences; act in WInS or SMApply.

**Action:** items 1, 2, 12, 16, 20, 24.

---

## 9. Privacy

**Checked:** the GitHub API (14 Oct); git grep across all 167 commits; file metadata (PDF, docx, xlsx); and anonymous access to every Google link in the repo.

**Found. This is the list for item 5.**
- **The repo is public.** Its description names the school. It has 17 branches, 0 forks and 1 star.
- **The WInS username appears in:**
  - competition/COMPETITION.md:3 and :117;
  - keel/routines/tasks/MONITOR.md:33 and WATCHER.md:13;
  - both caplet/ips_drafts/*.pdf files (in the file name and on page 1);
  - all 5 caplet/ai_outputs/*.docx files;
  - the .xlsx (cells Portfolio!G16 and "WInS Notes"!A2; also xl/comments4.xml);
  - git history (commits c11b02f and 44f1296).

  It was removed on 30 Sep and came back on 14 Oct. The username is not secret by itself, since the IPS title page needs it. But the password is now the only barrier until the freeze. Removing it breaks the ips-final gate check (MONITOR.md:33), so re-point that check at the same time (item 27).
- **The .xlsx metadata** (docProps/core.xml) holds a full name in "Surname, First" form. Its first name is not one of the six on the title page; whether it belongs to a teammate is UNVERIFIED. The file's xl/workbook.xml also stores a school OneDrive path that spells out a school account.
- **A student's school email** sits inside a file path at archive/rab/rescued/r4_hist_original.py:6. It is written with dashes, so a search for "@" will not find it. Blank out the path but keep the file: archive/rab/inventory.md:210 and archive/rab/rescued/ladder_history_2000_2026.py:6 cite it.
- **team_list.md** (lines 32-36, 43-52) lists 15 students from three other teams at the school.
- **Last year's doc** (caplet/google_drive/2025_knox_wharton.md):
  - names people who are not on this team in its comments;
  - contains comments saying to "make up stories";
  - has a ChatGPT share link that still works (near line 3805).
- **The school is named** in 17 tracked files.
- **Three of last year's Google files open to anyone with the link.** One appears to contain last year's username, a value that looks like a password, and another school's emails (not re-verified).
- **This year's team Docs and Sheets refused anonymous access (HTTP 401).** They are safe while set to Restricted. Whether they are shared across the school domain is UNVERIFIED.
- **No literal email addresses** are in the tracked text files. The ones in .env.example:12, toolkit/config/data.yaml:23 and toolkit/pyproject.toml:13 are placeholders.
- **Lower risk:** `/Users/ray` paths (check_gate_c.py:35, :163; keel/routines/tasks/scheduled_tasks/*.md) show a first name only.
- **The 14 Oct commit message says "PII and credentials removed".** That is misleading. The export READMEs are accurate for their own folder.
- **Making the repo private** hides the files, branches, history and PRs. It cannot recall copies already cloned. Deleting branches or renaming the PDFs does not remove the username. A history rewrite also needs GitHub Support.
- **Rivals at the same school can read the drafts and notes.** The WInS note timestamps and the Doc version history prove the team wrote them first.

**Action:** items 3, 5, 6, 10.

---

## 10. Numbers refresh

**Checked:** the official Treasury par curve up to the 14 Oct close (posted after the first draft of this brief; 12 Oct was a holiday). Two independent pricers, plus the repo's own curve code. All numbers here are MODEL.

**Par yields:**

| Date | 1y | 2y | 5y | 7y | 10y | 20y | 30y |
|---|---|---|---|---|---|---|---|
| 13 Oct | 4.48 | 4.79 | 5.00 | 5.11 | 5.21 | 5.60 | 5.56 |
| 14 Oct | 4.53 | 4.82 | 5.00 | 5.09 | 5.19 | 5.57 | 5.52 |

Since 6 Oct, the 10y is down 8bp and the 20y down 11bp.

**Cost on 1 Jan 2027 of the ten payments (14 Oct close). Quote only row 1.**

| Basis | Cost | Room under $300k | Fall in yields that uses it up |
|---|---|---|---|
| **WInS-listed, yields unchanged (the IBTR note's basis)** | **$295,993** | **$4,007** | **13.9bp** |
| WInS-listed, forward rates | $295,163 | $4,837 | 16.7bp |
| Old STRIPS, forward rates (superseded; trigger B's written basis) | $293,884 | $6,116 | 21.1bp |

On row 1's basis over time: 6 Oct $293,447 (22.7bp; MONITOR.md:22; no committed script produces it), 13 Oct $295,290 (16.3bp), 14 Oct $295,993 (13.9bp).

**Found:**
- **Chance the ladder costs more than $300k by January:** about 1 in 4 to 1 in 3 (13 Oct). If it does:
  - the 2028 deposit tops it up (expected $1.6k-4.3k; at the 95th percentile $10k-22k);
  - the facility shrinks; for example, a 50bp fall gives a floor of about $140.6k and a stock fund of about $27.8k;
  - no payment is missed unless yields fall about 420bp.
- **October rule on the 14 Oct close** (the close it specifies; archive/rab/trades/october_trade.md:18):
  - A: does not fire. All orders filled.
  - B: does not fire. Every basis is under $300k. On 13 Oct the biggest one-day fall in 2026 was about 10bp.
  - C: does not fire. Cash of $3,514 is below $6,300.
  - D: unknown. The 1.375% Nov-2040 bond was not listed on 5 Oct; check WInS now. If D applies, it means selling the 4.250% Nov-2040 bond and buying the 1.375%: 2 trades, against the "hold" plan. The window runs Fri 16 Oct 01:30 to Wed 21 Oct 06:30 Sydney (october_trade.md:20-24, :43). Running D or retiring the rule is a whole-team vote (vote set A).
  - archive/rab/trades/refresh_tickets.py still prints the STRIPS basis. Do not copy its wording.
- **The 2028 floor:**
  - $150k at Dec 2032 costs about $117.5k at a 5.00% five-year yield.
  - The stock fund is about $32.5k without the 2027 leftover, or about $38.4k with it (13 Oct).
  - Split: 66.4% / 25.3% / 8.3%, against WInS's 65.9% / 24.3% + 1% cash / 8.7%. No rebalancing is needed.
- **Do not use:**
  - ±$10.8k (about ±$9.4-9.5k, or 3.1%, using the funds' published durations);
  - "+0.55 over 1 year" (the window started 27 Mar 2026; a true year gives +0.42);
  - "about 20bp left" (9 Oct);
  - "$289,200" (a 28 Sep present value, not a January cost).

**Action:** items 8, 11, 14, 25.

---

## 11. Team process and roles

**Checked:** the team's Google Drive export (journal, notes, team list, sheets) and competition/COMPETITION.md.

**Found:**
- **No roles are recorded** (team_list.md:37-42). Wharton strongly encourages roles (faqs.txt:34), and every member must take part in the semifinal presentation (faqs.txt:89).
- **The 1 Oct votes** are not in minutes. The book was the Portfolio tab. The swap rule became moot. No roles were set.
- **Single point of failure.** Ray W. trades, runs the routines, owns the repo and submits. Nothing shows anyone else can use SMApply (UNVERIFIED). This brief therefore gives Ray only the items that need the leader, the repo owner or his Mac (items 2, 3, 4, 9, 10, 18, 22, 27). Privacy and repo fixes go to other students.
- **Journal.**
  - It has 10 entries and stops at 7 Oct. "[who argued what]" and "[fill in]" are still blank.
  - Missing: the 6 Oct email; trades slipping to 6-7 Oct; the 7 Oct incident; the 13 Oct "humanise" decision.
  - Say where AI was the source: the strategy idea came from the 27 Sep AI council, and the 7 Oct click was AI.
- **Darren W.'s 5 Oct challenge** (stock picking, EWT, GLD) has no recorded outcome, and the "too timid" criticism is still open. Write a one-page decision record in the team's words, with Darren giving his side.
- **The Client Portrait is empty.** The client tab has AI-like text with old numbers. Write the portrait from the case in the team's words.
- **Three of six students** have no work attributed to them in the exported docs. That is a record-keeping gap, not a judgement on anyone.
- **Any adult who sees a draft** must be unpaid and give guidance only. Keep a list.

**Roles for item 4** (one student can hold several; the team chooses):
- lead and submitter;
- trader, plus a separate checker/recorder;
- rates analyst (keeps the one numbers sheet);
- three reflection writers and a TNA editor;
- IPS section authors and a format checker;
- historian and AI-log keeper;
- rules lead (emails, pages, SMApply watch);
- privacy lead and repo helper (not Ray);
- growth/risk analyst and devil's advocate;
- client and co-sponsor lead;
- one outside reader who is not on the team.

**Action:** items 4, 23.

---

## 12. AI routines on Ray's Mac (keel/routines/)

**Checked:** keel/routines/README.md, keel/routines/tasks/*, the scheduled task files, the 13 Oct report and portfolio_check.py.

**Found:**
- **There are 10 tasks:** a daily rules watcher, a twice-weekly monitor, an evidence lab, mock judges and gate checks.
  - Dates (competition/COMPETITION.md:29-30): mock judges 19 Oct, 1 Nov, 22 and 30 Nov; gates 23 Oct, 6 Nov, 4 Dec.
  - Only the lab's time is recorded ("Sun/Wed 9pm", no time zone; keel/routines/claude_lab/BACKLOG.md:3).
- **Three are timed wrongly for the plan:**
  - the TNA judge (19 Oct) runs before the reflections exist (20 Oct);
  - the TNA gate (23 Oct) runs after the planned 22 Oct submission;
  - the IPS gate (6 Nov) runs after the planned 5 Nov submission.
- **What is fine:**
  - WATCHER.md:6 and LAB.md:6 forbid submitting, and LAB.md forbids WInS orders.
  - MONITOR.md and JUDGE.md are read-only on docs and orders but do not mention submitting.
  - The bond maths and the 13 Oct report's yields are correct.
- **Risks:**
  - The monitor and watcher may read logged-in WInS and SMApply pages, and WInS cancels with no confirmation (competition/COMPETITION.md:85). The routines date from about 13 Oct, so they did not cause the 7 Oct click, but the risk returns whenever an order is open.
  - The judge and monitor never check who wrote a draft, so they would polish AI text.
  - The TNA gate does not check that each pick is a filled order.
  - The IPS gate checks hard-coded names that include the username (MONITOR.md:33).
  - The lab is built "so the team only has to write". The judge-lens brief contains ready-made "high-school voice" example phrasings.
  - The mock scores come from one AI model using a partly unofficial scoresheet.
  - The watcher is silent when nothing changes, and it writes unconfirmed "rules" into its memory.
  - Everything depends on one laptop. What happens to a run while the Mac sleeps is UNVERIFIED.

**Changes for item 27** (edit the live copies at ~/Research/caplet-monitor/, not the repo copies):

| Routine | Do |
|---|---|
| Watcher | Keep. Public pages and forwarded Wharton mail only. Post a weekly "still running, no change" line. Rule changes stay "unconfirmed" until a student checks them. |
| Monitor | Keep. No logged-in WInS. Check authorship first. Date every number. Point it at the new IPS tab. |
| Gates | Move the TNA gate to Wed 21 Oct and the IPS gate to Wed 4 Nov. A human runs the checklist too. Check each pick is "Filled". Check names against the private roster note. |
| Mock judges | Move the TNA judge to Wed 21 Oct. Point the 1 Nov IPS judge at the student draft. Problems only, scored on the official criteria, labelled "AI opinion". |
| Evidence lab | Methods and sourced numbers only, which a student then rebuilds. No example phrasings, co-sponsor statements or experience timeline. |

**Action:** items 2, 26, 27.

---

## 13. Last year's lessons

**Checked:** last year's doc and resource.md, plus a 7-word overlap check against this year's files.

**Found:**
- **Rules broken.** UTF, a closed-end fund, was at one point the largest holding (17.7%). THQ was also a closed-end fund, and XCEM (5.01%) was off the approved list. WInS accepted all of them, and the AI analysis never flagged the problem.
- **Over-complex packaging.** The team's own report admits its frameworks did not drive decisions.
- **Inconsistent numbers.** The required return was stated as 11.6%; with the yearly payouts from Year 3 it was about 12.5%. The sleeve weights also conflict.
- **Strategy drift** after the midterm.
- **Integrity.**
  - Comments said to "make up stories".
  - ChatGPT shaped drafts, but the Works Cited lists no AI.
  - An outside reviewer of unknown role edited drafts (whether they were paid is UNVERIFIED).
  - What was actually submitted is UNVERIFIED.
- **No text from last year was reused this year.**
- **Links labelled "past semifinalist"** are UNVERIFIED. Copying is banned ("plagiarize existing strategies").
- **Last year's approved list and sector minimum do not apply this year.**

**What carries over:**
- Check the instrument type against this year's rules before every trade.
- Keep one numbers sheet.
- Keep one plain name and one plan.
- Make sure the IPS matches the frozen book.
- Keep a real, dated journal and a real AI log.
- Have an editor.

**Action:** items 5, 23, 25.

---

## 14. Remaining contradictions and earlier review items

**Contradictions to settle (the list for items 28 and 30):**

| Topic | Conflict |
|---|---|
| Name | "Roots First" (competition/COMPETITION.md:147, :204; keel/routines/claude_lab/00-judge-lens/README.md:3, :36; file names of AI example notes v13 and v14) against Root-and-Branch (every IPS draft; the 1 Oct log) |
| V5 called current | CLAUDE.md:12; caplet/START_HERE.md:9; competition/COMPETITION.md:22 and :199-201 (also says "47 + ~498"; it is 47 + 497); caplet/google_drive/ips_report/README.md:6, :10 |
| Freeze time | 5:00 pm in toolkit/config/wharton_private_2026_27.yaml:76, toolkit/config/competition.yaml:17-18 and toolkit/docs/wharton_workflow_v2.md:116; caplet/START_HERE.md:47 gives no time |
| Stock minimum | `min_share_price_usd: 3` (toolkit/config/competition.yaml:44; toolkit/config/wharton_private_2026_27.yaml:72); competition/COMPETITION.md:66 says the session rules win |
| competition/COMPETITION.md facts | :49 says Laura is fictional; :13 says 14 to 16 hours; :77 credits "US Treasuries" to the email; :144 points to a log that does not exist; :181 says 5.000%; :193 has the AI-at-Preview rule; no disqualification rules |
| Roster | "pending" in toolkit/config/team_roster.json and CLAUDE.md:46-47; "submitted" in CLAUDE.md:8 |
| Floor | "about $150k" against "the remainder"; two readings of "rounded down"; the 14 Oct decision was never logged |
| Shortfall order | competition/COMPETITION.md and V5 against the rab memos, which end in "her own money" (the case forbids outside money) |
| Ladder cost | $292,000 / $293k / $294k / $297k / $289,200, on different dates and bases |
| Plan vs rule | "Hold" against the October rule, which has not been retired |
| TNA picks | Four sources disagree. The sheet labels IBTR "Pick 1 (tested)". CLAUDE.md:97-99 names TLH, which was never bought. |
| VT | 164 (sheet) against 167 (actual) |
| Old-plan numbers | caplet/deliverables/final_report_outline.md, cosponsor_talking_points.md, caplet/decisions/ D4-D6 and the root Strategy Brief PDF ($298k, $113k minimum, "keeps 20%") |
| Certainty | decisions/02 (99.5%, "DECIDED") against the rab definition, which is due 20 Oct |
| Source of truth | caplet/docs/START_HERE_TEAM_CAPLET.md:11 also calls itself the "single source of truth" |
| Toolkit (toolkit/src/) | "Wharton Max Sector Limit (25%)", "Max Asset Limit (15%)", a default "approved = True"; `report audit-ai` always passes |
| Low priority | The smapply_public_2026-10-14 snapshots have no manifest hashes. Decide whether to keep the Doc and Sheet IDs at competition/COMPETITION.md:223 and MONITOR.md:25-26. |

**Earlier review items (30 Sep):**

| Item | Status 14 Oct | Action |
|---|---|---|
| P1 AI-written IPS heading for submission | Not fixed, and worse (V5) | Items 1, 20 |
| P2 false AI disclosure and mock log | Not fixed | Items 24, 30 |
| P3 student email in a file path | Not fixed | Item 5 |
| P4 WInS username | Back in current files | Items 3, 5 |
| P5 school named | Now 17 files plus the repo description | Item 3 |
| P6 Mac path in check_gate_c.py:163 | Not fixed (crashes on every other computer) | Item 30 |
| P7 truncated working-paper PDF (no end-of-file marker) | Not fixed | Item 30: banner it or remove it |
| P8 unrelated personal PDF | Not fixed | Item 30 |
| P9 stale files | Partly fixed; about 54 older STRIPS-era files have no banner (not re-verified) | Item 30, including CLAUDE.md's older sections |
| P10 invented rules in src | Partly fixed ($300k; sector default now 1.0) | Item 25: no toolkit outputs |
| P11 flat 5.26% in strategy_mc.py | Labelled as an assumption; old results remain at CLAUDE.md:152-155 | Item 30: banner them |

Tests (run on a scratch copy): 59 passed, 0 failed. They cover only the demo toolkit, not the strategy numbers.

**Action:** items 28, 30.

---

## Appendix: verification log and sources

**Counts:**
- **First review pass** (11 reader areas, 164 findings): about 130 confirmed by two independent verifiers, many with lower severity; 33 low-severity findings not separately verified; 0 refuted outright.
- **Disputed: 2.** Whether to email Wharton before the TNA (decision: optional). The cash reconciliation (§5).
- **Fact-check of the draft brief:** 14 errors and 10 minor points corrected. Two findings were overtaken after 13:26 UTC on 14 Oct: the edits to the FAQ and Trading Details pages, and the 14 Oct curve.
- **Completeness critique:** wrong file targets, sequencing, owners and missing actions fixed. Ready-to-copy phrasing in §6 and §7 was cut back to topic labels.

**Claims corrected during checking (do not repeat these):**
- "No rule has changed": two public pages changed on 14 Oct.
- "Fix the freeze time in competition/COMPETITION.md": it is already right; three other files are wrong.
- "$301,950 on 9 Oct": competition/COMPETITION.md labels it 13 Oct; its basis is the 9 Oct curve plus 12 Oct closes.
- "About 0.16 points left": 0.14 on 14 Oct.
- "Exactly 3 pages": 3 is the maximum.
- "Message, tag, comment or email is the rule": the rule is "may not contact"; the list is the team's reading.
- "Changing the team leader and inventing stories are disqualification rules": no such penalty is stated for either (see §4).
- "The TNA and IPS must not give a range": Wharton says "not expected".
- "Every routine forbids submitting": only WATCHER and LAB say so.
- "V4 'Need to Humanise' at line 36": the title is at :1; line 36 is a comment.
- "AI_USE.md says 'humanise'": it says "remove AI-style patterns", "AI-voice detector" and "blind voice tests".
- "Nov-2039 41%": Nov-2040 is 41% and Nov-2039 33%. The average is 20.0%, not 21%.
- "'Refine and proofread' is in competition/COMPETITION.md": it is a student's Doc comment.
- "$293,448": use $293,447 (MONITOR.md:22).
- "Bonds filled within 7bp": it depends on the method; say within about 9bp.
- "Delete r4_hist_original.py": blank out line 6 instead; other files cite it.
- "Payments are never cut": no payment is missed unless yields fall about 420bp (MODEL).
- "Word and Docs count a hyphenated word as one word" (Docs UNVERIFIED): the real risks are headings, numbers and the thin margin.
- "This year's Docs are public": they returned HTTP 401. Only last year's three files are open.
- "The case contradicts the co-sponsor 'rarely' claim": the claim is unsupported, not contradicted.
- "$293,447 cannot be reproduced": it can be reproduced on the WInS-listed basis; it just has no committed script.
- "Trigger B needs 31bp": about 24bp on its written basis on 13 Oct; 21.1bp on 14 Oct.
- "The cancelled note's '0.3' is unexplained": it matches the old STRIPS basis (30.8bp on 6 Oct).
- "The 7 Oct click happened in a scheduled routine": it was an AI-assisted trading session.
- "The FAQ's 'students place trades' is about AI": it is about advisors.
- "Renaming the PDFs or deleting branches removes the username": it does not.
- "A 1 in 3 chance": say 1 in 4 to 1 in 3.

**UNVERIFIED:**
- how Wharton counts words, and whether Google Docs splits numbers;
- the exact roster names and team-name form;
- the TNA form's fields;
- the 6 Oct email's text and arrival time;
- who wrote or typed each note, and whether AI typed any;
- the authors of V2-V4, Tab 10 and Tab 15;
- whether "Cash" was removed from the permitted list or mis-captured on 27 Sep;
- whether WInS stays viewable after 6 Nov;
- how WInS treats an order still open at the freeze;
- whether the 1.375% Nov-2040 bond is now listed;
- whether a second student can use SMApply;
- whether the semifinal letterhead request is a second request;
- the domain sharing of the team Docs;
- the contents of last year's public files;
- whether the name in the .xlsx metadata belongs to a teammate;
- what happens to routine runs while the Mac sleeps;
- the cash reconciliation (DISPUTED);
- whether Wharton checks public repos or runs similarity checks.

**Not re-verified in the final pass** (keep them labelled): the simulated judge scores; the $3,670 worst floor shortfall; $161k at a $125k floor; the 41-of-46 line page fit; the count of about 54 files without a banner; last year's public-file contents.

**Learning notes (for Ray's learning goal; not for any deliverable; do not reuse their wording):**
- A broker accepting an order is not a compliance check. The Trade Log and screenshots are what prove compliance later.
- When yields fall, bonds already held rise in price, but a future purchase gets dearer. A gain on the WInS screen can be a cost to Laura's January purchase. Longer bonds (longer duration) move more.

**Sources:**
- competition/official/2026_27/: the TNA and IPS PDFs and text, the Competition Guide, Laura_Gao_2026_Client_Profile, the School Documentation Template, and smapply_public_2026-10-14/*.
- Live pages fetched 14 Oct 2026 (13:26 UTC, re-checked 20:21-20:38 UTC): wghsinvcomp.smapply.us/res/p/{home, guide, client, deliverables, trading, wins, faqs}/; globalyouth.wharton.upenn.edu/competitions/investment-competition/ (main page, rules-roles, faq); globalyouth.wharton.upenn.edu/ai-policy/.
- Market data fetched 14 Oct: the home.treasury.gov daily par yield curve CSV (2026, up to the 14 Oct close); the Yahoo chart API; the iShares IBTP and IBTR pages and screener; the Vanguard VT API.
- The GitHub API for this repo.
- Reviewer scripts and downloads in scratchpad/oct14/ (the fact-check ladder pricer: factcheck/ladder.py and ladder_lib.py; downloaded pages: factcheck/dl/).