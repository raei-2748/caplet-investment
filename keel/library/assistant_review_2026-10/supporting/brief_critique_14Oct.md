**Completeness critique of the draft team brief (repo at 2affd4c)**

Scope: the evidence pack I received stops partway through finding rules-11. I compared rules-1 to rules-10 in full, and rules-11 as far as it goes. For the other sections I spot-checked claims directly in the repo, read-only. I have not reproduced any personal data.

## A. Errors and mis-citations in the draft (fix first)

1. **Item 31 sends one fix to the wrong file.** It says "Fix competition/COMPETITION.md: … the freeze is 4:00 pm ET". competition/COMPETITION.md already says 4:00 pm (competition/COMPETITION.md:21, :72). The files that are actually wrong appear in §4 but in no action item:
   - toolkit/config/wharton_private_2026_27.yaml:76
   - toolkit/config/competition.yaml:17-18
   - toolkit/docs/wharton_workflow_v2.md:116 ("Any last trades must be placed before 6 Nov, 5:00 pm ET")
   - caplet/START_HERE.md:47, which gives no time at all
   Point item 31 at these files instead.

2. **Item 25 contradicts itself.** It says "Submit on Thu 5 Nov (Sydney)… If a trade is unavoidable, place it in US market hours by Thu 5 Nov ET".
   - Thu 5 Nov ET market hours are Fri 6 Nov 01:30-08:00 Sydney, which is after the IPS has gone in. The IPS would then describe a book that changed after submission.
   - Fix: last trade by Wed 4 Nov ET close (= Thu 5 Nov 08:00 Sydney), then submit.
   - Add the reason from rules-6: bond orders fill at end-of-day prices (archive/rab/trades/friday_checklist.md:22).

3. **§5 mis-cites a date.** It says "about $301,950 (+0.65%) on 9 Oct (competition/COMPETITION.md:188)". competition/COMPETITION.md:188 actually reads "Value about $301,950 on 13 Oct (+0.65%)". Either cite it correctly or explain why the date was changed.

4. **Item 3: delete is the wrong fix for r4_hist_original.py.** The item says "line 6 of archive/rab/rescued/r4_hist_original.py (delete that one file only…)". That file is itself cited as preserved evidence, at archive/rab/inventory.md:210 and archive/rab/rescued/ladder_history_2000_2026.py:6. Redact the path on line 6 rather than deleting the file.

5. **Item 3 misses places the username appears.** I verified two that §9 lists but item 3 leaves out:
   - all 5 caplet/ai_outputs/*.docx files (one hit each);
   - the .xlsx cells Portfolio!G16 and "WInS Notes"!A2. Item 3 only mentions the xlsx "hidden metadata".
   Item 3 should also say "delete or re-export" the two IPS PDFs, because the appendix notes that renaming them is not enough.

6. **§6 IBTR bullet uses a banned word.** It says "…the facility gets less, while payments are never cut". The brief bans "never" elsewhere, and §10 says payments fail only if yields fall about 425bp (MODEL).

7. **Overlap percentages are given with no metric, and they clash with the evidence.** The brief quotes "IBTR … 2% overlap", "41% and 33%" and "21%".
   - These come from note_check.py, which measures the share of three-word phrases (archive/rab/trades/note_check.py:16).
   - Evidence pack rules-2 measured all 11 filled notes at a rapidfuzz ratio of 54-77 against the AI exemplars, with IBTR at 61.
   - A student reading "2%" will conclude IBTR is AI-free. Name the metric and give both figures.

8. **§4 "No rule has changed … The only change since 27 Sep" leaves out a flagged possible change.**
   - The 27 Sep capture listed "Cash" first under "Investments permitted (for BOTH contributions)" (keel/library/insight_v1/phase_A/case_register.md, R-W89).
   - The 14 Oct snapshot does not list Cash (faqs.txt:42-45; trading.txt:43-46).
   - Whether Wharton edited the page or the 27 Sep capture was a transcription slip is UNVERIFIED.
   - This matters because §2 says cash at 0% "is fine", and vote set B asks where the 2027 leftover and the cash from early-maturing bonds will wait.

9. **Item 10 asks for a vote that has already happened.** It lists "the strategy name" as a vote item, but §6 G1 says "Root-and-Branch, settled 1 Oct", and rules-10 says no new naming decision is needed.
   - Change the item to "confirm".
   - Add the places where "Roots First" still appears: competition/COMPETITION.md:147 and :204, keel/routines/claude_lab/00-judge-lens/README.md:3 and :36, and the file names of AI exemplars v13 and v14.

10. **The word-count targets conflict with each other.**
    - The draft uses "pitch 45 … IPS 485" (item 24), "Word budget about 480" (§7) and "45 words or fewer" (§7 objective 5).
    - The repo's existing spec is ≤470 IPS words and ≤48 pitch words, "by two counters, the higher count wins" (keel/library/insight_v1/ips_spec.md:7, :47, :229). Rules-1 says to restore it.
    - The draft also leaves out the number-splitting risk. Google Docs counted "$4.99" as 2 words in a 2017 test, so figures like "$292,000" could push V5 to 502 (UNVERIFIED today). The appendix's line "The real risks are headings and the thin margin" is therefore incomplete.
    - ips_spec.md:70 also says no headings inside the IPS and at most one computed figure. That conflicts with §7 objective 4 (the mix percentages plus 5.1%). Say which spec wins.

11. **§2 states one rule more firmly than the evidence allows.** "Contacting her by message, tag … means disqualification": whether a tag counts as contact is UNVERIFIED (rules-5). Write "treat any tag as contact", and add "or her publisher or representatives" (rules-5 correction).

## B. Confirmed findings or decisions missing from the "Do this" list

- **Stock minimum in the configs:** `min_share_price_usd: 3` at toolkit/config/competition.yaml:44 and toolkit/config/wharton_private_2026_27.yaml:72 should become 5.
- **competition/COMPETITION.md:77 wrong source:** it credits "US Treasuries" to the 6 Oct email. That limit comes from the Session Rules (wins_notes.csv:9). §4 notes the error, but item 31 does not fix it.
- **Weekly emails:**
  - Save Week-1, the 6 Oct email and every later email privately, with date, sender and subject.
  - Write down the 6 Oct email's arrival time in ET. Gate G3 depends on it, but item 12 only says to copy activity rules.
  - Record the outcome ("activity requirement: none found, [date]") in competition/COMPETITION.md (rules-9).
- **Roster status:** toolkit/config/team_roster.json and CLAUDE.md:46-47 still say "pending", although CLAUDE.md:8 says the roster was submitted. No item fixes this.
- **Repo pointers that still call V5 current or say to refine it:**
  - CLAUDE.md:12
  - caplet/START_HERE.md:9
  - competition/COMPETITION.md:22 ("Version 5 draft") and :199-201
  - caplet/google_drive/ips_report/README.md:6 and :10 ("CURRENT")
  Item 1 marks only the Google tabs.
- **Item 6 gives no location for the rule to delete.** Give competition/COMPETITION.md:193 plus the live routine copies on Ray's Mac.
- **Removing the username will break the ips-final gate.** The gate check at keel/routines/tasks/MONITOR.md:33 uses the hard-coded names. Re-point it to the private roster note at the same time.
- **The October rule needs a decision path.**
  - Under archive/rab/trades/october_trade.md:20-24 and :43, the check uses the 14 Oct close, and the trade window closes Wed 21 Oct 06:30 Sydney.
  - Trigger D (the 1.375% Nov-2040 bond newly listed and passing the price check) means selling the 4.250% bond and buying the 1.375%. That is 2 trades, against the "hold" plan.
  - Item 11 says only "check whether … listed". Add: "if it is listed, the team votes by Sun 18 Oct to run D or retire the rule; record the result in the decision log."
  - "Formally retire the rule" is a whole-team vote, not a job for the trader and checker. Fold it into vote set A.
- **Item 33 leaves out §12's own gate fixes:**
  - The TNA gate runs 23 Oct (competition/COMPETITION.md:29-30), after the planned Thu 22 Oct submission.
  - The TNA mock judge runs 19 Oct, before the student reflections exist (item 16, Tue 20 Oct).
  - The IPS gate runs 6 Nov, after the Thu 5 Nov submission.
  - Add: move or pause these routines, check that each pick shows "Filled", and check names against the private roster note.
- **Earlier review items with no action:** P7 (truncated PDF) and P11 (old results at CLAUDE.md:152-155) appear in §14 but have no item. Item 32 should name CLAUDE.md's STRIPS-era older sections (for example the TLH note pick) explicitly.
- **Low priority:** the smapply_public_2026-10-14 snapshots have no manifest hashes. The Doc and Sheet IDs at competition/COMPETITION.md:223 and MONITOR.md:25-26 need a keep-or-remove decision.

## C. Sequencing problems

- **Item 16 comes before item 17.** Reflections are due Tue 20 Oct, but the ladder re-run is Wed 21 Oct, and the IBTR reflection needs "a dated update of the room left". Run the number first, or tell writers to quote the 13 Oct figure with its date. G2 says "around 21-22 Oct"; use one date.
- **Vote set A has three dates.** Item 10 says Sun 18 Oct, while the swap rules say "agreed by Mon 19 Oct" and the gates say "target Mon 19 Oct". Use one date.
- **Item 15 should come before item 14.** The Trade Log confirming each pick is "Filled" should be done before the pick vote; both are dated Mon 19 Oct.
- **Item 8 creates only six roles, but the list assigns more.** These owners would not exist:
  - Trader (items 11, 12)
  - checker (11, 15, 19, 25)
  - Rates analyst (17, 30)
  - Historian (28)
  - "Named student" (26)
  - outside reader (18, 22)
- **Item 21:** the outline is due Tue 27 Oct, the same day as vote set B. Write "after the vote".

## D. Owners and deadlines that are vague or overloaded

- **Ray carries too much.** He owns or co-owns 15 of 34 items (2, 3, 5, 6, 7, 8, 13, 19, 22, 25, 27, 31, 32, 33, 34), plus the trader items if he trades. Seven of these fall between Thu 15 and Sat 17 Oct, yet §11 calls him a single point of failure.
  - Only items 2, 7, 19, 25 and 33 (and arguably 6) need the leader, repo owner or his Mac.
  - Reassign 3, 5, 31, 32 and 34 to a collaborator once item 2 adds collaborators.
- **Item 4, "Owner of those files":** they may belong to former students who are not on the team (§9). Give a fallback (ask the advisor) and a record-if-blocked step.
- **Item 6, "now":** give a date and the file location.
- **Items 18 and 22, "outside reader":** nobody is named, and no recruit date is given. §11 says this person must be unpaid, give guidance only, and be on a list.
- **Item 29, "Fri 4 Dec":** that is the due date, and it is unclear whether it is Sydney or ET. Set an earlier draft date.
- **Item 30, "from 10 Nov":** there is no end date, and no owner or location for the "one dated numbers sheet".
- **Time zones are mixed.** Most dates are implicitly Sydney, item 25 and §6 use ET, and nothing says which is which. Add one line: "All dates in §1 are Sydney unless marked ET."

## E. Text that reads like submission prose (cut to topic labels)

- **§6 IBTM:** "the refinement: the 5 Oct log kept 'never below the floor' because the real plan used STRIPS; the 6 Oct email moved the real floor into IBTM, whose payout is not fixed, so the floor is quoted rounded down". This is the whole reflection argument in sentence form.
- **§6 IBTR:** "if yields fall past the line, the 2028 deposit tops up and the facility gets less, while payments are never cut". Also "one clause on scale: WInS shows the plan after both deposits, at about two-thirds size".
- **§6 VT:**
  - "a lower median gift for a much better bad case" repeats the AI wording at competition/COMPETITION.md:162, so students who reuse it would be submitting AI wording.
  - "half lifts the gift; half is Laura's cushion" is also ready to paste.
- **§6:** "Together they follow the IPS order: roots, then floor, then branch." This is a ready-made slogan.
- **§7 objective 2:** "The payments rank above every facility dollar, the floor included." This reads as an IPS sentence.
- **"What this teaches" boxes (§5, §10):** the §10 box lines up exactly with the IBTR reflection. Label both "learning note, not for any deliverable", or move them to an appendix.

## F. Things that would confuse a high-school reader

- **Undefined internal labels:**
  - "vote set A/B"
  - "gate G1-G6", used in the §6 table before it is defined
  - "October rule" and "triggers A-D", defined nowhere in the brief
  - "the kit", "rab memos"
  - "execution reader", "authorship reader", "verifiers"
  - "Tab 15", which is missing from the Terms list
  - "ips-final gate", "heartbeat line", "glosses"
  - "watcher", "monitor", "evidence lab"
- **Mixed units:** "about 0.16 points" (§2, §6) versus "16.3bp" or "About 16bp" (§3, §10).
- **Two bases with no guidance.** "The IBTR note's basis" and "forward rates" both appear, and the reader is not told which to quote. Say "quote only row 1 of the §10 table".
- **Superseded figures are still quoted,** although objective 8 says to use only WInS-listed, dated numbers. Mark each "do not quote" or recompute it:
  - $191k/$202k/$213k against $165k/$174k/$189k ("STRIPS basis, 28 Sep")
  - $503k/$466k/$447k (28 Sep)
  - $174k/$161k (basis not stated)
- **The floor definition is incomplete.** The glossary defines the floor as "the 2028 Treasury holding (IBTM)". In WInS, IBTM also covers the 2033 payment (competition/COMPETITION.md:178), so the IBTM reflection's "two jobs" will be confusing unless both are defined.
- **"tested / refined / aligned" look like jargon,** but they are Wharton's own words (Trading_Notes_Analysis-FINAL.txt:12, :29). Say so.
- **The AI judge scores look precise** (8.2, 7.0). Add: "AI opinion; gaps under 1 point mean nothing."

## G. The "Do this" list is too long to act on

The list has 34 numbered items. Items 3, 7, 10, 20, 24, 28, 31 and 33 each bundle 3-9 sub-tasks; item 31 alone has 9 competition/COMPETITION.md fixes plus 3 Google Doc fixes. Week 1 has 13 items in 4 days.

Suggested restructure:
- **A "Top 6 before the TNA" box:**
  1. Item 1: students write every submitted word.
  2. Item 8, with all roles: name owners.
  3. Item 10, including the October-rule decision: vote set A.
  4. Item 15, then item 14: fill the Trade Log, then vote on the picks.
  5. Item 16: students write the reflections.
  6. Item 19: paste, check and submit.
- **A separate privacy track (items 2-4)** with one owner other than Ray.
- **Move the Final Report (26-30) and Housekeeping (31-34) items** into a checklist to be reissued on 25 Oct and 9 Nov.
- **Split item 31** into "competition/COMPETITION.md and config fixes" and "live Google Doc fixes", each with its own owner.