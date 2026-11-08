# Candidate experience events: Keel's side (27 Sep to 9 Nov 2026)

Mined Mon 9 Nov 2026 from the repo record (git log in Sydney time, `keel/pm/RUNLOG.md`, `keel/office/outbox/`,
`keel/rooms/`, `keel/library/`, `keel/ips_rewrite/`, `keel/INSTRUCTIONS.md`, `keel/final_report/`). Every event below
is confirmed in the record; invented diary scenes are excluded. Episodes 0-24 were used only as pointers and each
event was checked against a file or commit. Ordered from most compelling to least. "We" means the team; "our office"
means the team's research office. Times are Sydney. "MODEL" in evidence means a simulated figure.

### K-01: The number we were told to delete was right
- Date (Sydney): Wed 21 Oct, 15:20 and 18:28; settled Tue 27 Oct, 07:16
- Origin: KEEL (keeping the line in the submitted Trading Notes Analysis was CAPLET's action)
- What happened: Two days before the Trading Notes Analysis was due, one of our own checks told us to delete "about 7.5% a year (as per JPMorgan)" from the VT reflection as a false fact, because J.P. Morgan's 2026 tables gave world stocks 7.0% and gave 7.5% to developed markets outside the US. Three hours earlier a separate search had found J.P. Morgan's new 2027 release, dated 19 Oct, putting global equities at 7.5%. The line went in as written. Over the next six days two more of our checks repeated the "it's the wrong index" mistake, until a reread of the release settled it: 7.5% is the 2027 world-stocks figure, and the 2026 overseas number matched it only by coincidence of editions.
- Stakes: Had the "correction" stuck, the IPS and Final Report would have told judges our own submitted reflection was wrong when it was right, against Wharton's demand for "a clear and consistent investment strategy across all three" deliverables.
- Decision or response: The correction was withdrawn in writing, and 7.5% was kept as the one stated return that agrees with the submitted reflection.
- What changed afterwards: Every number now carries its source edition and date. Model runs at the old 7.0% were redone at 7.5% (one tail figure moved from 29% to 28%).
- Vivid detail: J.P. Morgan, 19 Oct 2026: "Global equities are projected to return 7.5% (USD), increasing from 7.0%." Our own memo, 27 Oct: "the match was a coincidence of editions."
- Strand: research and decision process
- Evidence: commit `a0bea2d` (Wed 21 Oct 15:20) and `keel/office/outbox/2026-10-21_WO-0003_equity-return-projections.md` ("Global equities 7.5% (up from 7.0% in the 2026 edition the IPS cites)"); `keel/library/assistant_review_2026-10/oct21_tna/TNA_Teardown_21Oct2026.md:20` (commit `314701b`, 18:28: "Delete 'about 7.5% a year per JPMorgan' ... 7.5% is JPMorgan's non-US developed (EAFE) figure"); `keel/office/outbox/2026-10-24_rooftop_our-own-dates.md` ("The 21 Oct teardown called the submitted 7.5% FALSE, reading the 2026 LTCMA"); commit `70819cf` (Mon 26 Oct 23:32, "7.5% is EAFE not world"); `keel/office/outbox/2026-10-27_noticeboard_7-5-is-world-stocks.md` ("The rewrite's correction is wrong"); commit `696f0f5`; commit `dac1d5b` ("P06 re-run at JPM 2027 7.5% (only 29% -> 28% moves)").

### K-02: The promise we called certain was the weakest one in the plan
- Date (Sydney): Tue 27 Oct, 13:53 (model) and 19:21 (check against the submitted notes)
- Origin: KEEL
- What happened: All week our risk figures (0.75% to 1.43%) had measured the bottom of the 2031 range. Reading the plan the way a lender reads a company's debts (who is paid first, and when) showed the ten payments were the weakest promise in it: after the gift left in 2033, the only thing behind the bond-interest gap was Laura's half of the share fund, and a payment came up short after 2033 in 6.8% of model paths (8.4% when yields and shares fall together). That evening a check against our submitted Trading Notes found the draft now contradicted reflection 3, which tells judges VT is "the only investment not standing between Laura and a payment deadline". In the draft her shares stood behind a payment in 33% of paths.
- Stakes: The ten payments are the one thing the case says must be met "with a high degree of certainty", and the reflection the draft contradicted was already with the judges.
- Decision or response: We borrowed the rule loan funds use to protect their safest notes: money for any visible shortfall is set aside before anything goes to the facility. Payments short fell from 8.4% to 0.01% of paths; the median gift stayed about $165,000.
- What changed afterwards: "Move the gap into Treasuries before anything else is promised" ran through every later draft, and a test that deletes every share became a standing check that no payment depends on a share price.
- Vivid detail: "The ten payments, the promise the case says must be protected, are the weakest one."
- Strand: research and decision process
- Evidence: commit `b68907c`/`d5f2053` (13:53, "Payments are the weakest promise (short after 2033 in 6.8-8.4% of MODEL paths); a 2033 coverage test cuts it to 0.01%"); `keel/office/outbox/2026-10-27_genius-lab_last-in-line.md` ("from how CLOs protect senior notes"; "Payments short 8.4% -> 0.01%"); commit `c546f9b` (19:21) and `keel/office/outbox/2026-10-27_archive_stocks-behind-the-cheques.md` ("gets used that way in 33% of MODEL paths").

### K-03: A knife edge: $300,000 had bought the ten payments on only 12 days of 2026
- Date (Sydney): Mon 28 Sep (research run) to Tue 29 Sep, 13:03
- Origin: KEEL
- What happened: The plan's opening claim was that Laura's first $300,000 buys all ten $50,000 payments. Pricing the ten on every Treasury curve of 2026 showed they cost more than $300,000 on 173 of 185 trading days, and fitted only from 10 Sep, after long yields jumped about 30 basis points in a week (on 22 Sep the cost was $300,485). Priced on the real bonds' dates, our first headroom of $7,700 shrank to $5,613, and about 1 in 3 model rate paths cost more than $300,000 by January. Two independent pricings of the 28 Sep curve differed by $204; changing two conventions (day count and the 1-3 month rates) reproduced the gap to the cent.
- Stakes: If January 2027 prices were higher, "the first deposit buys all ten" would simply be false.
- Decision or response: "Fits inside $300k" was dropped as a headline. Certainty was defined by what is bought plus two named gaps, and the 2028 deposit was given the job of completing the ladder.
- What changed afterwards: The submitted IPS carries the rule: "Even if yields fall and the total cost of the ladder ends up being above $300,000, we'll simply complete it with the 2028 deposit."
- Vivid detail: "The ten-payment ladder cost more than $300,000 on 173 of 185 trading days of 2026."
- Strand: research and decision process
- Evidence: `keel/library/insight_v1/00_executive_summary.md:52-53`; `keel/library/insight_v1/strategy_changes.md:36` (I4: "headroom $5,613 ... supersedes CLAUDE.md's $7.7k/27bp ... ~1 in 3 rate paths cost >$300k"); commit `81663b2`; commit `84e7010` and `keel/library/insight_v1/verification/ladder_2026-09-28/README.md` ("The $204 gap ... reproduces the GPT figures to the cent"); `keel/library/assistant_review_2026-10/03_Repo_Review_30Sep2026.md:100` ("On 22 Sep it did not fit ($300,485)"); `keel/final_report/FINAL_IPS_as_submitted.txt`.

### K-04: The capsule you are told to open
- Date (Sydney): Mon 2 Nov, 09:02 (fixed 09:06)
- Origin: KEEL
- What happened: The draft built its picture on the team's name: an extended-release caplet that releases its dose on schedule, with the line "Break it open and you ruin how it works." Checking that sentence against real medicine labels found it false. The patient guides for two of the best-known extended-release capsules tell anyone who can't swallow them to open them and sprinkle the contents on applesauce; what they forbid is crushing. A real extended-release caplet's label says "Swallow whole; do not crush, chew, split, or dissolve."
- Stakes: A judge whose child takes one of those medicines would know the plan's central image was wrong.
- Decision or response: Rewritten as "Crush it and the schedule is gone", two words shorter and true of both the caplet and the plan (selling a holding before it matures is the crushing).
- What changed afterwards: Every image or analogy in a draft got the same source check as a number.
- Vivid detail: Adderall XR Medication Guide (rev. 04/2026): "open it and sprinkle the medicine on applesauce."
- Strand: research and decision process
- Evidence: commit `a09fc8b` ("V52 P2 false at its source (XR capsule labels say open it; crushing is the harm)"); commit `7de6289` (09:06 fix); `keel/office/outbox/2026-11-02_window_the-capsule-you-may-open.md`; `keel/rooms/window/W-07_the_capsule_you_may_open.md`.

### K-05: Our best line said the opposite of our own test
- Date (Sydney): Wed 28 Oct, 19:21 (test); Fri 30 Oct, 08:51 (caught)
- Origin: KEEL
- What happened: On 28 Oct we ran a deletion test: wipe out every share Laura owns and see whether any payment gets worse. Its summary was read as "no payment is worse off", and that became the draft's strongest line: "Wipe out every share she owns and no cheque is worse off, only the gift." Two days later, the check before a review draft went out reread the raw results and found the line backwards. The key said the shares never make a payment worse; with the shares wiped, a payment was worse off in 364, 354 and 412 of 200,000 paths in three model worlds, by up to $2,953, because money banked from her shares in 2031 stays behind the payments.
- Stakes: The line sat in all three drafts lined up for the next day's review; a judge who tested the claim would have found our central certainty argument false.
- Decision or response: Replaced with a shorter line the results support: "The shares can help a cheque, never hurt one."
- What changed afterwards: Claims built on a model result are read against the raw output, not a summary of it.
- Vivid detail: "a cheque is worse off in 364 / 354 / 412 of 200,000 paths"; the memo: "both cannot be true."
- Strand: response to challenges
- Evidence: commit `d62e431` (Wed 28 Oct 19:21, "shares wiped: no cheque worse off in 600,000 MODEL paths"); commit `2a19628` (Fri 30 Oct 08:51, "BREACH, the wipe-out line reads A19 backwards"); `keel/office/outbox/2026-10-30_window_the-wipe-out-line.md`; `keel/rooms/archive_checks/A19_results_S0.json`.

### K-06: We set aside more than sixty drafts and wrote our own IPS as a letter
- Date (Sydney): Fri 6 Nov, 00:06 to Sat 7 Nov, 01:54 (IPS due 09:00)
- Origin: CAPLET
- What happened: Our research office's final pitch and IPS went up at 00:06 on Friday after ten overnight rounds of writing and blind review, and one more version followed at 07:30. Seven hours before the deadline we set all of it aside and sent our own IPS: a letter that begins "Dear Laura," and ends "Yours, Caplet", built on one idea, that her career behaves like shares she cannot sell. It went in before 09:00, when trading froze and the portfolio locked.
- Stakes: The judged IPS, with a hard deadline and no extensions.
- Decision or response: The team's own two tests, in its own order: "First and foremost, and most importantly, it sounds HUMAN. Even more importantly, it's COMPREHENSIBLE to humans".
- What changed afterwards: The letter became the frozen basis of the Final Report. The next day the office corrected its research to the letter (24 replacements) and compared its own last draft with the letter idea by idea.
- Vivid detail: "Frankly, your IPS was just too unacceptably bad for us to work with."
- Strand: response to challenges
- Evidence: commit `fae84d1` (Fri 6 Nov 00:06, "FINAL pitch + IPS (R10 + punctuation), every gate passed"); `archive/bible_2026-11-08/BIBLE.md:792` (Book 16, 01:54 Sat 7 Nov); `keel/INSTRUCTIONS.md` I92 ("Keel's V57-V63 were set aside"); `keel/final_report/FINAL_IPS_as_submitted.txt`; `keel/episodes/2026-11-08_ep41.md` Record table.

### K-07: Every outside reader called the ending corny, and we left it in
- Date (Sydney): Wed 4 Nov, 19:14 (earlier warning Sun 25 Oct, 00:10)
- Origin: KEEL
- What happened: On the evening the final draft went to the team, six outside readers in two blind reads tested it. In all 27 of their answers, the closing line about the caplet was the one called corny. We put that on a card for the team's own rewrite and offered only a two-word cut, reasoning that the ending still had to pay off the "do not crush" set-up the team had asked for on 1 Nov. Our own review on the night of 24-25 Oct had already found that the motif lines "cost human-read and crowd out the investing".
- Stakes: The tone of the whole IPS, two days before the deadline.
- Decision or response: Left as "their call". The next evening the team leader wrote that the tablet image made Laura sound like a rehab patient.
- What changed afterwards: The medicine was dropped from the overnight rewrite of 5-6 Nov, and the IPS the team submitted has no tablet in it.
- Vivid detail: "every reader in both reads (27 of 27 answers) called the corny one".
- Strand: learning and growth
- Evidence: commit `ac0b8e5`; `keel/meetings/2026-11-04_why-this-for-her.md:48`; `keel/office/outbox/2026-11-04_long-room_why-this-for-her.md:18`; commit `a496114` (Sun 25 Oct 00:10, "Courtroom on v4 (plain body wins; motif lines cost human-read and crowd out the investing)"); `keel/ips_rewrite/final_night/README.md` (call 1); `keel/final_report/FINAL_IPS_as_submitted.txt`.

### K-08: Our mock judges agreed too much; rebuilt, they ranked our newest draft fifth of six
- Date (Sydney): Fri 30 Oct, 18:53 to 20:30
- Origin: KEEL (prompted by the team's criticism)
- What happened: For a week our drafts were scored by panels of simulated judges; on 27 and 28 Oct panels put our draft first with all three judges. On 30 Oct a teammate wrote that the judges were "thinking suspiciously similarly". We found why: one model with different job titles, briefed with our own change notes, comparing our drafts only with each other. We rebuilt the panel as six judges on different models with different beliefs (a skimmer, a growth hawk, an actuary, a teacher, a professor, a programme manager), each reading six blind entries in a different order, with a rule that agreement above 0.6 means rebuild. The new panels disagreed (average agreement 0.23 to 0.39), and the draft our daily meeting had just voted 5-1 to send for review came fifth of six, behind the team's own version of 14 Oct.
- Stakes: A week of polishing had been tuned to judges who agreed with us.
- Decision or response: The voted draft was dropped; later drafts were scored only by the disagreeing panel.
- What changed afterwards: Unanimous rankings are treated as a warning, not confidence. Our looking-back note: "Ideas survived, sentences didn't."
- Vivid detail: Mean rank out of six: the team's own 14 Oct version 3.83; the draft our meeting had just voted 5-1 to send, 4.5.
- Strand: learning and growth
- Evidence: commit `93d64a4` (Tue 27 Oct 22:01, "blind rival panel (V25 1st with all 3 judges)"); commit `04da14b` (Wed 28 Oct, "V27 first with all three judges"); `keel/ips_rewrite/judges/README.md` (diagnosis and new panel); `keel/ips_rewrite/judges/panel_V35/SUMMARY.md:16`; commit `ae292c1` (18:34, "V30 ... = Keel's Sat 31 review draft, 5-1"); `keel/office/outbox/2026-10-30_rooftop_the-vote-after-the-message.md` ("The loop's own V30 came 5th of 6 in panel 4 (mean rank 4.5), behind Caplet's own Version 5 of 14 Oct").

### K-09: A bond fund never matures
- Date (Sydney): Mon 28 Sep (fund pages read about 10:35); plan changed by Tue 29 Sep
- Origin: KEEL (the finding; the change of plan was the team's)
- What happened: Our first research run matched Laura's payments with two Treasury bond funds (IEF and TLH), chosen so their sensitivity to interest rates matched the payments'. Reading TLH's holdings on the issuer's page showed 74.7% of its bonds, by weight, mature after Laura's last payment in 2042. A fund itself never matures, so nothing in it turns into cash on the date a payment falls due. The plan switched from matching rate sensitivity to owning one dated holding for each payment.
- Stakes: A matched-sensitivity pair needs constant rebalancing, and every payment would depend on what a fund happened to sell for that January.
- Decision or response: One holding per payment: term Treasury funds for 2033-37 (WInS listed no Treasury bond maturing Feb 2031 to Feb 2036) and Treasury bonds for 2038-42.
- What changed afterwards: That is the portfolio filled on 7-8 Oct, and the submitted IPS's "10 Treasuries ... each maturing just before it's needed".
- Vivid detail: TLH: "61 holdings maturing 2037-2046, 74.7% after 2042".
- Strand: research and decision process
- Evidence: `keel/library/insight_v1/securities_and_allocation.md:81`; `keel/library/assistant_review_2026-10/03_Repo_Review_30Sep2026.md:263-267` ("Until 28 Sep the plan used bond ETFs (IEF and TLH) ... a bond fund never matures, so it cannot end when a payment is due. The strategy changed from duration matching to one dated holding per payment"); CLAUDE.md (WInS book filled 7-8 Oct).

### K-10: $300,000 could buy the ten payments in only one month in four since 1871
- Date (Sydney): Tue 27 Oct, 22:20
- Origin: KEEL
- What happened: We tested the plan against every start month of US market history since 1871 as well as three model worlds. Two findings changed the argument. $300,000 could have bought all ten payments outright in only about one month in four since 1871, and in no month from mid-2007 until this autumn; at the 2020 low they would have cost $469,000, more than both deposits. And the sceptic's case was answered with history: start a 60/40 plan in January 1923, shares return about 7% a year for fifteen years and beat bonds, yet the pot runs dry and the 1937 and 1938 payments bounce.
- Stakes: Without this, "buy the payments now" read as caution; with it, it was timing.
- Decision or response: "Certainty is on sale, briefly" became the reason to buy in January 2027. Rival plans broke a promise in 22-36% of tested worlds, ours in 0-1.6%.
- What changed afterwards: The next morning a check found one quoted "closest call" figure ($8,400) was not in the results file and marked it to re-derive before use.
- Vivid detail: "in no month from mid-2007 until this autumn".
- Strand: research and decision process
- Evidence: commit `57dca24`; `keel/ips_rewrite/inbox/2026-10-27_model-suite.md` (items 1-2); `keel/models/README.md:35-36` (incl. "[Window 28 Oct: not in suite_results.json ... Re-derive before use]"); RUNLOG Tue 27 Oct 22:20 ("the champion breaks a promise in 0-1.6% of worlds vs 22-36% for rival plans").

### K-11: Fifty-six per cent of history says the ladder needs a margin
- Date (Sydney): Wed 30 Sep, 10:27 (first found); Mon 9 Nov, 07:40 (sized)
- Origin: KEEL
- What happened: Since 30 Sep we had known the Treasury ladder delivers $500,000 only if its interest is reinvested at about 4.97% or more. On 9 Nov we tested the submitted design against 585 sixteen-year stretches of US rates since 1962. Sized at today's forward rates, the ten Treasuries fell short somewhere in 55.6% of them: usually by a little (median $1,592), but 1 time in 20 by $34,555, and at worst $45,266, for a July 2007 start. The bond desk's standard answer (each coupon pays the next payment due) halved the risk at the same cost, but would have broken the submitted IPS's promise to buy all ten in January 2027.
- Stakes: The central promise of the IPS the team had already submitted.
- Decision or response: Keep the ten exactly as the IPS says, and let the 2028 deposit complete them to a stated standard: a $21,149 margin so all ten are paid even if every coupon is reinvested 3 points below today's forward rates. That pays in full in 94% of historical stretches; the worst is $12,117 short.
- What changed afterwards: The IPS's "we'll simply complete it with the 2028 deposit" became a sized number, and the bond desk's design was kept as the alternative a bond reader would expect.
- Vivid detail: "585 windows of 16 years, one starting each month from Jan 1962 to Sep 2010."
- Strand: research and decision process
- Evidence: commit `9db8d35` (Wed 30 Sep 10:27, "the buyable ladder delivers $500k only if coupons are reinvested at about 4.97% or more"); commit `f38fe68`; `keel/final_report/NUMBERS.md:76-103`; RUNLOG Mon 9 Nov 07:40.

### K-12: Six drafts in a day, then the order to slow down
- Date (Sydney): Mon 26 Oct, 07:56 to 23:27
- Origin: CAPLET (the two instructions); KEEL (the drafts and the reset)
- What happened: At 07:56 the team leader stopped our polishing of the fourth IPS version and asked for a rewrite from scratch. By 23:01 we had produced six drafts (at 13:48, 14:56, 15:11, 22:46, 22:54 and 23:01), the last labelled "near-final". Then came the next message: "The process of rewriting the IPS should not have been this fast ... THINK ... I don't want you to be hasty." At 23:27 we reset to a slow road: no drafting until Fri 30 Oct, a daily thinking log, research questions first.
- Stakes: Speed passing for thought, eleven days before the IPS deadline.
- Decision or response: Drafting stopped for four days; the research rounds that followed produced the findings in K-02, K-05 and K-10.
- What changed afterwards: No part of the office could ask for a draft or a date. The same rule later shaped the Final Report plan: no prose until Fri 27 Nov.
- Vivid detail: The sixth draft of the day, at 23:01, was saved as a "near-final candidate"; 26 minutes later: "reset to the slow road (no drafting until Fri 30 Oct)".
- Strand: learning and growth
- Evidence: commits `65b2a36` (07:56, "Stop polishing IPS v4 (Ray, 26 Oct): rewrite from scratch"), `2f9d0cd`, `015a986`, `f8817a0`, `3826a5d`, `15c7d3d`, `c19ccf3`, `17e348d`; `keel/INSTRUCTIONS.md` I41 ("D1, D1.2, D1.3, D2 and D3 were all written on 26 Oct"); CLAUDE.md (no Final Report prose until Fri 27 Nov).

### K-13: "Metaphors alone does not count as creativity"
- Date (Sydney): Thu 5 Nov, 19:09-19:10 (response 19:52-19:58, then overnight)
- Origin: CAPLET (the office's response was KEEL)
- What happened: The name Caplet XR began as one of three name packages our office tested on 24 Oct (an extended-release caplet; X for the ten payments, R later redefined as redemption). On 26 Oct the team locked it, calling it "the most genius name idea of any team". On the evening of 5 Nov, with the draft frozen, the team leader wrote: "metaphors alone does not count as creativity. We want intellectual creativity, yours just packaging." A minute later: the tablet image "feels like we're helping Laura for a rehab, but she doesn't need any rehab."
- Stakes: About a day and a half before the deadline, with the image running through the opening and the ending.
- Decision or response: Within the hour a new search for creativity in the reasoning, not the picture; the overnight rewrite kept the name but dropped the medicine and let the ten redemptions themselves carry the circle.
- What changed afterwards: A standing rule for the Final Report: creativity lives in what the plan does and why.
- Vivid detail: "she doesn't need any rehab."
- Strand: learning and growth
- Evidence: commit `3b71b9e` and `keel/rooms/lab/L-06_cp/packages.md:102` ("Package B: Caplet XR (our own name; the road nobody else can take)"); `keel/INSTRUCTIONS.md` I34, I84, I85; commits `92ce7ba` (19:52) and `0327626` (19:58, "four-idea rewrite with the tablets out"); `keel/ips_rewrite/final_night/README.md` (call 1).

### K-14: Her career is a share she can't sell: the idea that survived from the first day
- Date (Sydney): Sun 27 Sep (team notes reviewed); Sat 7 Nov (submitted); Sun 8 Nov, 20:01 (tested)
- Origin: CAPLET (the team's own idea); KEEL (kept it and tested it)
- What happened: Our first review of the team's own notes on Laura, on 27 Sep, kept one idea: her career already carries concentrated risk (publishing, speaking, licensing), so her portfolio should not add correlated risk. Six weeks later it opened the IPS we submitted. On 8 Nov we tested it with data: for US college graduates, shocks to lifetime pay move with the previous year's stock market (correlation about 0.52) and hardly at all with the same year; in 2009 shares rose 25.94% while US school book sales fell 13.8%, and schools buy her books. The same test found two lines in our own submitted IPS that need stating as risks: "the bottom will remain constant" holds only once the 2032 Treasury fund is bought in January 2028, and the reasons to change the plan name "a missed deposit" but not a smaller one.
- Stakes: The IPS's central idea, and whether it overpromised.
- Decision or response: The Final Report will name the textbook view (a career is steady like a bond, so a young worker should own more shares) and say why Laura differs: no pay cheque, and no money in or out before 2033 except the 2028 deposit. The two risks are stated, not hidden.
- What changed afterwards: The plan for 9 Nov started with these two hardest numbers.
- Vivid detail: The submitted pitch: "Laura's career is already a giant stock she can't sell."
- Strand: research and decision process
- Evidence: `keel/library/team_materials/review_why_laura_and_public_profile.md:12` ("her career already carries concentrated risk (publishing, speaking, licensing), so the portfolio should not add correlated risk"); `keel/final_report/FINAL_IPS_as_submitted.txt`; commit `332880b` (PR #159, merged `7076208` 20:02); `keel/final_report/research/cards/Q1_career_as_shares.md` rows 7, 28, 44 and section (b); `keel/episodes/2026-11-08_ep42.md` Record table.

### K-15: A vote five minutes after a message nobody read
- Date (Sydney): Fri 30 Oct, 18:15-18:34 (audit 26 Oct; rule made Sun 1 Nov)
- Origin: KEEL
- What happened: An audit on 26 Oct had found 13 of the team's 33 written instructions to us ignored or only partly applied. On 30 Oct a long message from the team arrived at 18:15 and cancelled the review planned for the next day; at 18:20 our daily meeting voted 5-1 on which draft to send to that review, and its minutes never mentioned the message. It was the second time in three days an instruction had been stored but not applied. The next day the team wrote that its messages were "just being blatantly ignored".
- Stakes: Work aimed at a plan the team had already cancelled, and the team's trust.
- Decision or response: From 1 Nov, before any vote opens, the meeting quotes the time of the team's newest message and says how the vote answers it. Every candidate draft also got a line-by-line check against every instruction (198 rows for one draft).
- What changed afterwards: "Storing an instruction is not applying it" became a ruled lesson; the vote gate was first used on 2 Nov.
- Vivid detail: Five minutes: the team's message at 18:15, the vote at 18:20, on a draft for a review the message had just cancelled.
- Strand: teamwork and communication
- Evidence: `keel/loop/LESSONS.md` LS-06 ("13 of 33 instructions ignored or partly applied"; "ruled (Sun 1 Nov: the vote gate)"); `keel/office/outbox/2026-10-30_rooftop_the-vote-after-the-message.md`; commit `ae292c1` (18:34); `keel/INSTRUCTIONS.md` I70; commit `f6a1020` ("IPS V45 (voice-first) with its 198-row Bible check").

### K-16: The night the ladder crossed $300,000
- Date (Sydney): Fri 23 Oct, 09:53 (US close of Thu 22 Oct)
- Origin: KEEL
- What happened: The morning the Trading Notes Analysis was due in the US, our daily repricing showed the ten payments' cost jump from $297,202 to $302,139, $2,139 over Laura's first deposit, after long yields fell about 0.15 points in one day. The trade rule we had set for October (move some world shares into the 2032 Treasury fund if the gap opened) did not fire: its window had closed on 20 Oct, when the cost was $297,411. Over 7-22 Oct the Treasuries in our simulator rose about $7,550 while Laura's real January purchase became $10,206 dearer.
- Stakes: The simulator showed a gain at the very moment the real plan got harder to afford.
- Decision or response: No trade (the rule had not fired); the IPS gave the 2028 deposit the job of topping up the payments first.
- What changed afterwards: The completion rule in the submitted IPS, and the habit of reporting the real plan's cost separately from the simulator's value.
- Vivid detail: "Our WInS bonds gained while Laura's real plan got dearer."
- Strand: response to challenges
- Evidence: commit `efbabf5` ("ladder cost crosses $300k; October rule did not fire"); `keel/library/assistant_review_2026-10/checks/RESULTS_16Oct2026.md` section 5 (table 16-22 Oct; "+$10,206"; "about $7,550 (+2.8%)").

### K-17: The cure we proposed used something WInS doesn't sell
- Date (Sydney): Tue 27 Oct, 19:21 to Wed 28 Oct, 10:45
- Origin: KEEL
- What happened: To fix the contradiction in K-02, our check proposed moving any gap "into Treasury bills" in January 2033, and the next draft wrote it in. A rival-scan meeting at 22:13 flagged the rule risk, and the morning rules check confirmed it: Wharton allows only Treasury bonds "available on WInS", WInS lists 43 Treasury bonds, and no bill had ever been seen there.
- Stakes: Recommending a security outside the permitted list, the same kind of error that cost last year's team (it traded outside the rules).
- Decision or response: Rewritten the same morning to move the money into "the next Treasury fund to mature".
- What changed afterwards: Every instrument a draft names is checked against the WInS list before the draft goes anywhere.
- Vivid detail: The draft: "any projected shortfall, plus a cushion, moves into Treasury bills".
- Strand: response to challenges
- Evidence: commit `c546f9b` and `keel/office/outbox/2026-10-27_archive_stocks-behind-the-cheques.md` ("move any visible gap ... into Treasury bills, once"); `keel/ips_rewrite/drafts/D6/ips.txt:11`; commit `dc9f748` (22:13, "brief to the rewrite (T-bills rule risk)"); `keel/office/checks/2026-10-28.md:8` ("WInS lists 43 US T-bonds and no bill has been seen there"); commit `ae30a4d` (10:43, "no T-bills on WInS"); CLAUDE.md "Team" (2025-26 lesson).

### K-18: Thirteen suggested edits rejected the night the Trading Notes were due
- Date (Sydney): Fri 23 Oct, about 21:00 to 21:10 (deadline 08:00 Sat)
- Origin: CAPLET
- What happened: Hours before the Trading Notes Analysis deadline, our office's final check of the rewritten reflections placed small edits as suggestions in the team's document (13 could be placed). Some addressed real issues, including two reflections at exactly 100 words and a phrase calling inflation risk "nonexistent" against the case's own line on inflation. The team leader rejected all 13 within minutes: clearer, but they softened the voice.
- Stakes: The first judged deliverable, and whose voice it carried.
- Decision or response: The same night a standing rule: the team prefers confident, assertive phrasing; checks flag only hard issues (limits, rule breaches, facts) and never soften.
- What changed afterwards: From then on the office's checks separated "false" from "bold"; three days later the team leader added that a strong true word is not a breach.
- Vivid detail: "Our team leader rejected all 13 (23 Oct 21:08 Sydney): clearer but softens the voice."
- Strand: teamwork and communication
- Evidence: commit `66d5403` (`keel/office/LEDGER.md` WO-0007 row); commit `0d1680b` ("Keel voice: confidence is the voice; checks flag hard issues only, never soften"); `keel/pm/RETROS.md:25`; `keel/INSTRUCTIONS.md` I35.

### K-19: A former judge said the draft couldn't make the semifinal
- Date (Sydney): Mon 19 Oct, 20:35
- Origin: CAPLET (the team brought the verdict); KEEL (the diagnosis)
- What happened: The team reported that a former Wharton judge had said our IPS draft could not reach the semifinals, without giving reasons. Reading the 14 Oct version against Wharton's criteria, our office found it passed the format checks, so the problem was substance: the case's one real choice (what to do with the 2028 $150,000) was played very safely and never argued for Laura, leaving shares at about 7-9% of her $450,000, and the draft claimed more certainty than coupon bonds and funds can give ("cannot miss the range").
- Stakes: The semifinal, two and a half weeks before the IPS deadline.
- Decision or response: The rewrite set out to argue the trade-off in Laura's terms and to cut every certainty claim back to what the holdings give.
- What changed afterwards: The later drafts' two jobs: say why this plan suits her, and answer the strongest rival plan (K-22).
- Vivid detail: Memo title: "the judge's 'no' is most likely about substance: the case's one real choice is played very safely and never argued for Laura".
- Strand: response to challenges
- Evidence: commit `39c37c3`; `keel/office/outbox/2026-10-19_WO-0002_judging_ips-v5-why-not-semifinal.md` (context line and Answer 1-2).

### K-20: Seed money: the donor study we had read backwards
- Date (Sydney): Tue 27 Oct, 08:51 (followed up Fri 30 Oct, 12:20)
- Origin: KEEL
- What happened: A client-side note said co-sponsors respond to a lead gift "existing, not its size", citing a field experiment. Checking the study at its source showed the opposite: raising seed money from 10% to 67% of a campaign's goal produced "a nearly sixfold increase in contributions". The size of a committed sum matters; the ratio of a match doesn't. It was marked false before any draft used it.
- Stakes: The 2031 range is what Laura offers co-sponsors, and its bottom works like seed money.
- Decision or response: The bottom of the range was treated as the part co-sponsors can book, and the top as an intention.
- What changed afterwards: The cost of a lower bottom is now measured in co-sponsors' gifts, not just in Laura's money.
- Vivid detail: "a nearly sixfold increase in contributions".
- Strand: research and decision process
- Evidence: commit `b08794b`; `keel/office/outbox/2026-10-27_window_7-5-and-three-checks.md:15` ("The cited study shows the opposite"); RUNLOG Tue 27 Oct 15:40 ("co-sponsors read the bottom as bookable, the top as an intention"); commit `855c18a` ("seed money read at the source (nearly sixfold, so the low side costs the co-sponsors' gifts)").

### K-21: The Wharton line Wharton never wrote
- Date (Sydney): Mon 2 Nov, 07:16
- Origin: KEEL
- What happened: Our reference file of Wharton's own words had been quoted for days as saying the three deliverables "are judged together on these five". Reading it back against the source showed the sentence sat outside the quote marks: it was our own summary. Wharton's real line, in the case, is harder: "Evaluators will consider the three deliverables together. Teams should use each deliverable for its intended purpose while maintaining a clear and consistent investment strategy across all three."
- Stakes: The real line makes the locked Trading Notes binding. The draft said "A Treasury held to maturity pays exactly what it promises" right after naming funds, which our submitted reflection says pay "a net asset value, as opposed to a promise of par".
- Decision or response: The case's sentence replaced our summary; the next research job checked all five funds' prospectuses against the draft's words.
- What changed afterwards: Every job now quotes the Wharton line it serves, read back by someone who didn't write the order; consistency with the submitted notes became the test every later draft faced.
- Vivid detail: "The Wharton line we keep quoting for 'judged together' is ours, not Wharton's."
- Strand: learning and growth
- Evidence: commit `e7aa7d0`; `keel/ips_rewrite/inbox/2026-11-02_noticeboard.md`; `keel/loop/LESSONS.md` LS-14; RUNLOG Mon 2 Nov 07:40.

### K-22: The strongest rival plan, priced three times in one day
- Date (Sydney): Sat 31 Oct, 12:20 to 19:21
- Origin: KEEL
- What happened: Two of six simulated judges asked the obvious question: why not buy the safe ladder and put everything else in shares? We built that rival at its strongest (same ladder, about 80% shares, the 2031 bottom moved into Treasuries only when named). It never breaks a payment either, so the honest difference is a price. The first answer quoted about $9,000 (the smallest cell of a table), a mock trial raised it to about $19,000, and a check on our own plan's design found $15,000: owning the bottom from 2028 costs Laura about $15,000 on average by 2042, but if 2028-30 markets are in their worst twentieth, the rival's named bottom is about $90,000 against our $140,000. Real institutions had faced the same choice: Harvard, Yale and Princeton paused buildings in 2009, and farmers forward-sell only the grain already in the bin.
- Stakes: The plan's main trade-off, which no draft had answered.
- Decision or response: One paragraph naming the price and what it buys, with $15,000.
- What changed afterwards: A rule that a number goes to a vote with its design written beside it ("in which plan?"); the rival became the Final Report's benchmark.
- Vivid detail: "$90k v $140k".
- Strand: research and decision process
- Evidence: `keel/office/outbox/2026-10-31_library_money-with-a-date.md` (commit `76a0081`); RUNLOG Sat 31 Oct 16:40 ("price ~$9k"), 19:40 ("its '$9,000' was the smallest cell, the price is a ~$19,000 mean"); commit `0c4f84c` and `keel/office/outbox/2026-10-31_archive_the-price-on-our-own-design.md` ("'$19,000' becomes '$15,000'"); `keel/loop/LESSONS.md` LS-13; `keel/ips_rewrite/rivals/A09.md`.

### K-23: Wharton's rule change made our first research run obsolete
- Date (Sydney): Tue 6 Oct (email); Wed 14 Oct, 21:16 and Tue 20 Oct, 10:37 (rebuild)
- Origin: KEEL (absorbing a Wharton rule change)
- What happened: Our first research run, an 831-page record, built Laura's real plan on Treasury STRIPS, zero-coupon bonds that pay an exact sum on an exact date. Wharton's 6 Oct email limited Laura's plan to WInS-listed stocks, ETFs and Treasury bonds, and on 20 Oct the public FAQ listed TIPS and STRIPS as not permitted "for BOTH contributions, the IPS and Final Report". We marked every STRIPS-based file superseded (18 files on 14 Oct, 66 more on 20 Oct) and rebuilt the numbers on what WInS actually lists: term Treasury funds and Treasury bonds, with the 2032 fund as the bottom.
- Stakes: The cleanest instrument for the job was gone; coupon bonds and funds bring reinvestment risk and payouts at net asset value.
- Decision or response: Rebuild on WInS instruments only.
- What changed afterwards: Reinvesting coupons became the plan's one named weakness (K-11), and the funds' net-asset-value payout became a precise word in every later draft.
- Vivid detail: "66 STRIPS-era markdown files ... the same superseded banner as the 18 files bannered on 14 Oct".
- Strand: response to challenges
- Evidence: commit `124e1d6` (28 Sep, 831-page record); CLAUDE.md ("6 Oct Wharton email ... STRIPS-based numbers ... superseded (banners added)"); commit `44f1296`; commit `f9adf01`; commit `85a10cc`; `competition/official/2026_27/smapply_public_2026-10-20/`.

### K-24: Our September software followed rules we had invented
- Date (Sydney): Wed 30 Sep (review written; filed Fri 16 Oct, 09:09); stale rules fixed Wed 14 Oct, 21:16
- Origin: KEEL
- What happened: Two days after trading opened, a review of everything in the repo found that the software the team started with in September enforced rules that weren't Wharton's: a "Wharton approved" list of 31 securities that rejected IEF, TLT, VT and IBTM (funds we were about to buy), a 25% sector cap, $100,000 starting cash and a 9% hurdle. It also produced made-up company financials labelled FY2025, and its audit commands could not fail.
- Stakes: Last year's team traded outside the rules; this year a tool's invented rules could have blocked legal holdings or approved illegal ones.
- Decision or response: The tool was set aside (nothing current imports it); the stale rules were fixed and one source-of-truth file of this year's rules was written.
- What changed afterwards: Every trade and every recommended instrument is checked against this year's official documents only.
- Vivid detail: "enforces an invented 'Wharton approved' 31-security list that rejects IEF, TLT, VT and IBTM".
- Strand: response to challenges
- Evidence: `keel/library/assistant_review_2026-10/03_Repo_Review_30Sep2026.md:302-307`; commit `cf43a9d`; commit `44f1296` ("Fixed stale rules ($300k, commissions, dates, no sector rule, no approved list)"); CLAUDE.md "Team" and "Open items".

### K-25: Plain English, and an honest count: fifty-five versions
- Date (Sydney): Tue 3 Nov, 20:48
- Origin: CAPLET (the team leader's note); KEEL (the response)
- What happened: Four days before the deadline the team leader named two problems: our writing read as corny and machine-made in tone and phrasing (not content), and the team couldn't tell what the office had achieved because it overcomplicated everything. Within hours the newest draft was rewritten in plain English with the same ideas and numbers, and a one-page status in plain words told the team where things stood, including an admission.
- Stakes: Communication between the team and its office, days before the IPS.
- Decision or response: Anything written for the team became one page of plain English with no internal labels; morning briefs were shortened and stripped of codes.
- What changed afterwards: A standing rule for every session; the Final Report plan's notes to the team follow it.
- Vivid detail: "55 versions is a sign we were polishing words, not improving the plan."
- Strand: teamwork and communication
- Evidence: commit `b9c492c` ("V55: V54 in plain English; one-page plain status for the team (Ray, 3 Nov)"); `caplet/STATUS_2026-11-03.md` (point 5); `keel/INSTRUCTIONS.md` I80; RUNLOG Wed 4 Nov 07:40 ("Brief (shorter, no codes, per I80)"); CLAUDE.md ("Talk to the students plainly").

### K-26: A draft rejected entirely: "half of your sentences just DON'T MAKE SENSE"
- Date (Sydney): Sun 1 Nov, 11:08 to 17:40
- Origin: CAPLET (the verdict); KEEL (the rebuild)
- What happened: As the team asked, we rebuilt the IPS sentence by sentence on the shapes of fifteen great writers, then revised it again by 11:29. A teammate rejected the result entirely: it opened with a rhetorical question ("the corniest and most cringeworthy thing I've ever seen"), said "our model" four times with no evidence, described our team's progress instead of the strategy ("We know this rival because we built it first"), and over-compressed until "half of your sentences just DON'T MAKE SENSE"; borrowing other writers' lines had made it worse. We rebuilt the IPS from scratch that afternoon, and a review already under way was withdrawn mid-run because the draft it was reviewing no longer existed.
- Stakes: Three days before the final draft was due to the team.
- Decision or response: A complete rebuild with new rules: no opening question, no model talk in the IPS, no team history, every sentence plain sense.
- What changed afterwards: The IPS became strategy only (the how and the why); models and evidence were sent to the Final Report.
- Vivid detail: The rejected draft's line: "We know this rival because we built it first."
- Strand: learning and growth
- Evidence: commits `d536e71` (11:08, "V48: IPS rebuilt sentence by sentence on great human sentences"), `84f1c4f` (11:29, V49), `fd4a575` (16:46, "V50: complete IPS rebuild after Book 11"); `keel/INSTRUCTIONS.md` I71-I78; RUNLOG Sun 1 Nov 17:45 ("W1 withdrawn at 17:40: Book 11 and V50 landed mid-run").

### K-27: The same ideas in two voices
- Date (Sydney): Sun 8 Nov, 11:26
- Origin: KEEL
- What happened: The day after the team set our drafts aside, we compared our last draft with the letter the team submitted, idea by idea. The plan was mostly the same; the writing was not. The letter starts from what Laura asked for, in her words, gives its reasons out loud with "because", concedes first ("You'd think that someone with your taste for thoughtful risk and 6 years to wait would usually own shares"), tells the story of changing its mind, and walks the cause one step per sentence. Ours stated rules without reasons and skipped middle steps: "writing for someone who already knows what we know."
- Stakes: The voice of the Final Report, judged on the same standard.
- Decision or response: Voice studies come before any Final Report prose; the letter is the benchmark for comprehension.
- What changed afterwards: The Final Report plan (no prose until Fri 27 Nov) starts every writing round from the letter's habits.
- Vivid detail: Our draft: "Our dose is Treasuries: before anyone relies on a sum Laura commits to, she owns the ones that will repay it." The letter: "barring a US default, none of your 10 operating payments will depend on a share price, or on anybody else's money, when they fall due."
- Strand: learning and growth
- Evidence: commit `7de06ac`; `keel/final_report/voice/STUDY1_two_voices.md` (sections A and B); `keel/episodes/2026-11-08_ep41.md` Record table (11:26).

### K-28: The model left out our own rule
- Date (Sydney): Wed 28 Oct, 18:33
- Origin: KEEL
- What happened: While testing two cures for the bond-interest gap, we found that the shared model every test used had never applied the draft's own rule that the promised half of the shares moves into Treasuries when Laura names her range in 2031. With the rule in, the top of the range was reached in about 86% of model paths, not the 73% we had been quoting.
- Stakes: A headline number had understated our own plan in drafts and memos.
- Decision or response: The model was corrected, and the meeting voted 4-1-1 to cover the gap on naming day ("bank it at the mark"); the one-sentence fix went into the draft.
- What changed afterwards: Model designs are written beside every number they produce.
- Vivid detail: "the shared model never locked the promised half (top 86% vs 73%)".
- Strand: research and decision process
- Evidence: commit `2ffca6e`; `keel/office/outbox/2026-10-28_long-room_bank-it-at-the-mark.md` ("We also caught the shared model leaving out the draft's own 2031 lock").

### K-29: The $85,000 break point came from an older plan
- Date (Sydney): Fri 30 Oct, 19:28
- Origin: KEEL
- What happened: The new draft answered "high degree of certainty" with a break point: a payment fails only if Laura's 2028 deposit comes in under about $85,000 after a two-point fall in rates. A word-for-word check against our submitted notes found the $85,000 came from an older version of the plan. Re-run on the current design, $85,000 failed a payment in 19.2% of model paths after such a fall; the real break was about $125,000. The next sentence, "her 2028 deposit never carries a cheque", contradicted two trade notes we had saved on 6-7 Oct.
- Stakes: Our key certainty claim was off by $40,000, and a second sentence contradicted the record judges already held.
- Decision or response: The figure was corrected to $125,000 and the sentence became "her 2028 deposit plugs any gap", which agrees with the notes.
- What changed afterwards: Numbers carried between drafts are re-run on the current design before use.
- Vivid detail: "$85k fails 19.2% of MODEL paths, $100k 5.0%, $125k 0.19%, $150k none."
- Strand: response to challenges
- Evidence: commits `fbf45f2`, `29e85c7`; `keel/office/outbox/2026-10-30_archive_the-deposit-carries-more.md`; `keel/rooms/archive_checks/A25_results.json`.

### K-30: The margin that vanished in a rewrite
- Date (Sydney): Mon 2 Nov, 14:02 to 14:07
- Origin: KEEL
- What happened: Between drafts, one paragraph lost the $7,500 cushion set aside on 28 Oct for the bond-interest gap. Re-testing the current draft found the cost: without the cushion only 76% of model futures paid all ten payments in full (47% if yields fall two points for good); with it, 99.8% and 99.7%. The cushion was back in the draft five minutes later, with the order of who bears a loss stated.
- Stakes: The payments' certainty, lost to an edit nobody meant as a change of plan.
- Decision or response: Restored; every idea in every version tracked in one ledger so it can't vanish between drafts.
- What changed afterwards: The team's earlier order ("Ideas vanished between versions") was applied as a check on each draft.
- Vivid detail: "no margin: 76% of base futures pay all ten cheques in full, 47% if yields fall 2pt; with it 99.8% / 99.7%".
- Strand: response to challenges
- Evidence: commit `8655ddc`; commit `1c5522f` ("the reinvestment cushion restored and the order of loss said"); RUNLOG Mon 2 Nov 13:40; `keel/office/outbox/2026-11-02_genius-lab_two-jobs-one-pocket.md`; `keel/INSTRUCTIONS.md` I65.

### K-31: Eleven days without a fresh Treasury curve, while one sat on a side branch
- Date (Sydney): Mon 26 Oct to Tue 3 Nov; Fri 6 Nov, 12:36
- Origin: KEEL
- What happened: From 27 Oct our daily markets check reported "no curve after 22 Oct", because the Treasury website refused our downloads. A 23 Oct curve had in fact been saved at 06:52 on 26 Oct, on a side branch the other work never read. Other work stranded the same way: a key model result sat on its own branch on 27 Oct, and on 31 Oct two parts of a round had been saved where the parts checking them never saw them. On 2 Nov all 21 leftover branches were merged into one; the next morning the ladder was repriced on 23 Oct prices ($297,636, $2,364 under $300,000). On 6 Nov a different download route reached the Treasury and brought prices up to 5 Nov: $302,163.
- Stakes: Decisions made on stale prices, and checks run on incomplete work.
- Decision or response: Merge everything; every room's work merged into the main copy daily.
- What changed afterwards: One main copy; the Final Report has a single numbers engine and register built on the 6 Nov close.
- Vivid detail: "no curve after 22 Oct (treasury.gov blocked)"; "curl is refused by the proxy".
- Strand: teamwork and communication
- Evidence: RUNLOG Tue 27 Oct 10:45 and rows to Sat 31 Oct; commit `0fdda97` (Mon 26 Oct 06:52, "file the coupon-shortfall scripts and the 23 Oct curve"); `keel/office/outbox/2026-10-27_archive_stocks-behind-the-cheques.md` ("L-10 was stranded on its own branch (PR #50)"); `keel/office/outbox/2026-10-31_archive_the-price-on-our-own-design.md` ("the Writing Room and the Courtroom never saw it"); commit `a8396c3` and RUNLOG Mon 2 Nov 19:30 ("All 21 leftover branches merged"); commit `d2e68f2`; commit `b69fa9f`; commit `f38fe68`.

### K-32: Our research corrected to the IPS the team actually submitted
- Date (Sydney): Sat 7 Nov, 11:38; Sun 8 Nov, 11:48
- Origin: KEEL
- What happened: The morning after the team submitted its own IPS, at its request we wrote Research tabs into its Final Report document: six by 11:38, then nine more, about 22,000 words. On Sunday we checked them against the letter that had actually been submitted and made 24 replacements. The tabs had described moving half the shares into Treasuries before 2031 as an option where the letter makes it a promise, and claimed the shares would cover the bond-interest risk where the letter says nothing of the kind.
- Stakes: The Final Report is judged together with the frozen IPS.
- Decision or response: 24 replacements, each checked as one change; the ladder repriced on the 6 Nov close ($301,544).
- What changed afterwards: Every Final Report figure now comes from one number register, and every claim is checked against a file of exact quotations from the submitted work.
- Vivid detail: "24 replacements".
- Strand: research and decision process
- Evidence: commit `f954c19`; commit `039bcbf`; RUNLOG Sun 8 Nov 11:48; `keel/episodes/2026-11-08_ep41.md` Record table; commit `f38fe68` (`keel/final_report/NUMBERS.md`, `keel/final_report/CANON.md`).

### K-33: Two blind readers found October's word on their own
- Date (Sydney): Wed 4 Nov, 19:26
- Origin: KEEL
- What happened: On the night the final draft went to the team, two outside readers given only our submitted Trading Notes record and the draft both found the same clash unprompted: in October we had told judges our bonds work "through duration-matching", and the new IPS explained that method as the one we don't use. One reader offered a quick fix ("which also matches timing"); re-running the check showed it false, since the ladder's average timing is about 7.6 years against the payments' 10.0.
- Stakes: Consistency across all three deliverables, with the October text locked.
- Decision or response: The IPS was left unchanged (the plan hadn't changed, only a word) and the clash was handed to the Final Report to explain; the reader's fix was refused.
- What changed afterwards: The Final Report owns explaining how October's word and November's plan fit.
- Vivid detail: "the judge's fix 'also matches timing' is false (... 7.61 v 9.99, MODEL)".
- Strand: research and decision process
- Evidence: commit `27d3132`; `keel/office/outbox/2026-11-04_archive_the-word-october-used.md`; RUNLOG Wed 4 Nov 19:26.

### K-34: One false sentence in the final draft, found at the sources
- Date (Sydney): Wed 4 Nov, 12:54-12:56
- Origin: KEEL
- What happened: The day the final draft was due to the team, we read its new investing lines against the sources the ideas first came from. Of twelve sentences, seven were true, four true only with a condition, and one false: the draft sized its safety margin "as if no more interest were reinvested", but the term Treasury funds end their lives holding cash, so a margin sized to those words would leave a payment short in some model futures.
- Stakes: The final draft's central certainty sentence.
- Decision or response: Rewritten as "as if every dollar waiting for a cheque earned nothing" and applied the same afternoon.
- What changed afterwards: A new check: every line is read against the people who first wrote the idea down, not only against its last editor.
- Vivid detail: "12 sentences, 7 TRUE, 4 TRUE IF, 1 FALSE".
- Strand: response to challenges
- Evidence: commits `ae31139`, `c82e1ee`; `keel/office/outbox/2026-11-04_library_checked-only-by-its-writers.md`; RUNLOG Wed 4 Nov 13:05.

### K-35: Our first test was wrong, and we said so
- Date (Sydney): Tue 3 Nov, 09:12
- Origin: KEEL
- What happened: Checking how the draft said the bond-interest gap is covered, we found the text described one check (in 2031) where the model relied on two (2031 and January 2033). Our first test of the difference said only 86.76% of futures paid every payment with one check; a second reviewer found a leak in that test, and it was withdrawn. The fair test gave 96.01% with one check and 99.87% with two (94.39% against 99.85% if yields fall two points for good). The hole was older than the current draft: drafts of 29-30 Oct had said "tops up once" and the second step had been parked as detail.
- Stakes: A promise in the draft that the plan only kept with a step the draft never mentioned.
- Decision or response: The parked idea was reopened; the next day's draft priced the gap as if nothing more were reinvested, which needs no second check.
- What changed afterwards: Withdrawn results are recorded as withdrawn, not quietly replaced.
- Vivid detail: 86.76% withdrawn; the fair test said 96.01% with one check against 99.87% with two.
- Strand: response to challenges
- Evidence: commit `8bd0819`; `keel/office/outbox/2026-11-03_window_the-second-look.md`; commit `059ffe0` (Wed 4 Nov 08:09, "reinvestment priced as if nothing more were reinvested").

### K-36: The $10,000 buffer was a lower quote with a name
- Date (Sydney): Sun 25 Oct, 18:25
- Origin: KEEL
- What happened: Our leaning was to hold a $10,000 Treasury buffer from the 2028 deposit as a third safety layer; an exhibit showed it cut the chance of the gift landing under its quoted bottom from 0.75% to 0.11%. A mock prosecution re-ran the model with the buffer paid from the same money that buys the bottom: simply quoting the bottom $10,000 lower, with no buffer, gave the identical 0.11%.
- Stakes: The team was about to vote on a layer that added complexity and no safety.
- Decision or response: The vote was split into two plain questions: how much to quote, and who owns the slack.
- What changed afterwards: Any proposed safety layer is tested against its plain twin before it is offered.
- Vivid detail: "Same safety. The exhibit's 0.75% -> 0.11% comes from the lower quote, not from the buffer."
- Strand: research and decision process
- Evidence: commit `a0488a4`; `keel/office/outbox/2026-10-25_courtroom_d1-buffer-is-a-lower-quote.md`; `keel/IDEAS.md` I-24.

### K-37: Seven of eleven catches were the same mistake, and the team leader said stop
- Date (Sydney): Mon 26 Oct, 20:24 (count); registered 22:42 (overrule)
- Origin: KEEL (the count); CAPLET (the overrule)
- What happened: Counting every catch that changed a line over two days, we found eleven, and seven were the same mistake: a word saying a holding is surer than it is ("exact" for a ladder whose coupons must be reinvested; a fixed sum "released" by funds that pay their net asset value). We proposed stating three kinds of "sure" in the IPS. The same evening the team leader overruled it: stop the certainty obsession; funds held to their December liquidation are "near-ironclad", and any bond-versus-fund distinction is one concise clause.
- Stakes: Precision against voice, eleven days before the IPS.
- Decision or response: The checks' rule changed: a false fact is a breach; a strong true word is not.
- What changed afterwards: The office stopped softening true lines and kept flagging false ones.
- Vivid detail: "seven were the same mistake: a word that says a holding is surer than it is."
- Strand: teamwork and communication
- Evidence: commit `641e796`; `keel/office/outbox/2026-10-26_rooftop_three-kinds-of-sure.md`; `keel/INSTRUCTIONS.md` I35 ("Overrules the Rooftop's 'three kinds of sure'"; "a false fact is a breach, a strong true word is not"); commit `d5db4e9` (22:42).

### K-38: Four of five fixes were our own dates, and one day's price three ways
- Date (Sydney): Sat 24 Oct, 20:23; Sun 25 Oct, 07:13
- Origin: KEEL
- What happened: Looking back over three days of fixes, we found four of the five were our own dates or forecast editions attached to a fact, and none had been caught by the part of the office that wrote it. The next morning a numbers audit found the papers for the team's vote carried the ladder's cost on the same day's close three ways ($298,861, $300,224 and $302,139, depending on the pricing basis) beside two J.P. Morgan editions (7.0% and 7.5%).
- Stakes: The team was about to vote on numbers that disagreed with each other.
- Decision or response: Every number in a working copy carries value, source, date or edition, basis and label (case fact, holding or model), struck before anything is pasted into a submission; the IPS text itself carried no model number.
- What changed afterwards: "One sheet, one edition", and later the Final Report's single number register.
- Vivid detail: "Four of five are a date or an edition attached to a fact; none was caught by the room that wrote it."
- Strand: learning and growth
- Evidence: commit `8d2fd9e`; `keel/office/outbox/2026-10-24_rooftop_our-own-dates.md`; commit `5e07534`; `keel/office/outbox/2026-10-25_SD-P02_numbers_one-basis-sheet.md` (table B); commit `fcec8f3` (holdings basis $302,199).

### K-39: Never quote the bottom as a number
- Date (Sydney): Tue 27 Oct, 18:29
- Origin: KEEL
- What happened: Drafts had quoted the bottom of Laura's 2031 range as $145,000. A mock trial of marking the bottom to market found that a fixed $145,000 would have been above the true bottom in 43.5% of model paths before any adjustment.
- Stakes: The case warns that overpromising damages credibility, and the bottom is the figure co-sponsors book.
- Decision or response: The IPS states the bottom as a rule (what Laura already owns in Treasuries), never as a dollar figure.
- What changed afterwards: The submitted IPS gives the bottom as the payout of "a Treasury fund maturing in late 2032", with no dollar figure.
- Vivid detail: "the IPS states the 2031 bottom as a rule, never $145k (below it in 43.5% of paths before any mark)".
- Strand: research and decision process
- Evidence: commit `693c3e5`; `keel/office/outbox/2026-10-27_courtroom_mark-to-market-on-trial.md`; `keel/final_report/FINAL_IPS_as_submitted.txt`.

### K-40: The draft never named the operating reserve
- Date (Sydney): Thu 29 Oct, 15:17
- Origin: KEEL
- What happened: Reading the current draft against every line of the case from Laura's side, we found it never named the operating reserve, which the case asks to be set aside at the start of 2033. The fix took 14 words: from 2033 the ten holdings are the reserve, one redemption per payment.
- Stakes: A required element of the case missing from the IPS.
- Decision or response: Added.
- What changed afterwards: The submitted IPS says it in one line: "From 2033 the Treasuries are the operating reserve."
- Vivid detail: "+14 words".
- Strand: research and decision process
- Evidence: commit `9dfd199`; RUNLOG Thu 29 Oct 15:45 ("V29 never names the operating reserve (case :94-97, Book 7), fix = from 2033 the ten holdings are the reserve, one redemption per cheque (+14 words)"); `keel/rooms/lauras_room/LR-06_four_doors_then_ten.md`; `keel/final_report/FINAL_IPS_as_submitted.txt`.

### K-41: Measuring the voice gap, then reading a thousand pieces in a night
- Date (Sydney): Tue 27 Oct, 19:57 to Thu 29 Oct, 06:48
- Origin: KEEL
- What happened: Told that our prose was flat and to read 500 to 1,000 pieces for voice, we first measured the gap: our drafts had 3-4% long sentences against 18% in a teammate's essays, five times his numbers per word and a quarter of his idea-words. We also found we had credited those essays to the wrong teammate for days. The reading log passed 1,000 pieces overnight (Montaigne, De Quincey, Wollstonecraft and Reserve Bank of Australia documents among them), saved in batches at 23:45, 01:06, 02:19, 03:29, 04:35 and 05:43.
- Stakes: The voice of the IPS.
- Decision or response: A voice guide judged by ear, with counts never used as a gate.
- What changed afterwards: Three days later the team still called the drafts "chronically incapable of writing like a human"; the first fix ("make it punchy") had been the wrong one.
- Vivid detail: "It lists what the plan owns and leaves out what it believes."
- Strand: learning and growth
- Evidence: commit `5413013`; `keel/office/outbox/2026-10-27_writing-room_voice-study.md:15-18`; `keel/INSTRUCTIONS.md` I36 ("said 'Ray's' until 27 Oct"), I69; commits `21911fc`, `435c432`, `4c8e45d`, `4cade3d`, `d9d1f01`, `8bf1b93`, `eb39665`; `keel/voice/reading/LOG.md`.

### K-42: Nineteen problems in our own research, one blocking
- Date (Sydney): Mon 28 Sep, 15:37
- Origin: KEEL
- What happened: Before the first research run went to the team, a final verification pass found 19 problems in it: 1 blocking, 7 important and 11 minor. Eighteen were fixed in place. The blocking one was privacy: a parked question quoted a line our own filter had excluded as personal and presented it as "Laura's identity-context advice".
- Stakes: Putting words in the real client's mouth, and personal material in a shared record.
- Decision or response: The quote was withheld; the entry points only to the ruling.
- What changed afterwards: No Laura quotes in the Trading Notes or IPS; every claim carries a status label (verified at source, from a repo file, assumption, or unverified paraphrase).
- Vivid detail: "I found 19 problems: 1 blocking, 7 important and 11 minor."
- Strand: research and decision process
- Evidence: commit `343b921`; `keel/library/insight_v1/phase_G/verification.md:5-6, 20`; `keel/library/insight_v1/README.md` (status labels); CLAUDE.md ("no Laura quotes in the Trading Notes or IPS").

### K-43: Four of our own mistakes found on one Sunday
- Date (Sydney): Sun 8 Nov, 12:05-12:12
- Origin: KEEL
- What happened: Building one ranked store of every idea from six weeks of research, a reviewer found the builder marking sources as fully checked when only some of their claims had been (scoring 5 instead of 3). Rereading Saturday's nine deep tabs found three more: a student's school email address copied into file paths in three tabs and an old script; the figure $306,663 used as "the cost if no interest is ever reinvested" when it means money sitting idle only between each payout and 1 January; and the TIPS and STRIPS ban dated to a later email when it was public on 20 Oct.
- Stakes: The Final Report's raw material, and a student's personal data.
- Decision or response: All four fixed the same hour; the store rebuilt from 1,131 to 1,317 ideas (507 in the top tier); the true no-reinvestment cost flagged as not yet worked out.
- What changed afterwards: The next morning's numbers engine computed it: $54,595 short if interest earns nothing.
- Vivid detail: "$306,663 ... means something narrower."
- Strand: response to challenges
- Evidence: commits `4b83f8f`, `47b30ed`; RUNLOG Sun 8 Nov 12:07 and 12:20; `keel/episodes/2026-11-08_ep41.md` Record table; `keel/final_report/NUMBERS.md` (design A, "Short if interest earns nothing $54,595").

### K-44: Eighteen questions and seven votes waiting
- Date (Sydney): Mon 26 Oct
- Origin: CAPLET (the instruction); KEEL (the change)
- What happened: By 26 Oct, 18 questions and 7 votes from our office were waiting on the six students. The team leader answered: "For all the decisions waiting on me just make your own call whichever you think work the best", keeping only danger-zone decisions (orders, submissions, money, accounts) for students. Every waiting item was decided the same day with a written reason; two were left, both WInS orders.
- Stakes: Work stalled behind busy students, twelve days before the IPS.
- Decision or response: A decision log in which each call is written with its reason and a default the office acts on.
- What changed afterwards: The office made and logged its own calls; the team kept the final word (and used it, see K-06).
- Vivid detail: "18 questions and 7 votes sat waiting on Caplet".
- Strand: teamwork and communication
- Evidence: `keel/INSTRUCTIONS.md` I40; `keel/pm/ASK_HUMANS.md`; CLAUDE.md ("Keel makes its own calls (Ray, 26 Oct)").

### K-45: The pre-mortem: "not standing out, not being wrong"
- Date (Sydney): Fri 16 Oct, 22:23
- Origin: KEEL
- What happened: A week before the Trading Notes were due, a pre-mortem asked why we might miss the semifinal. Its bottom line: the portfolio was fine, "The risks are all in the writing." That day's edit of the IPS had added about a dozen figures, several with no source, and dropped the diversification and annual-review clauses; the trade-note reflections had not been started with seven days left.
- Stakes: The first two judged deliverables.
- Decision or response: A blueprint so each reflection is tested, refined or supported; every figure in the IPS traced to a source.
- What changed afterwards: Standing out became an explicit goal alongside being right, the start of the search for one clear idea.
- Vivid detail: "If we miss the semis, the likeliest reason is not standing out, not being wrong."
- Strand: learning and growth
- Evidence: commit `a356283`; `keel/library/assistant_review_2026-10/05_Premortem_Review_16Oct2026.md` section 0.

### K-46: Nine stages of work for one sentence
- Date (Sydney): Wed 28 Oct, 20:55
- Origin: KEEL
- What happened: Our first full research round spent five of its stages and four model scripts choosing between two dates for a cushion of about $7,500. The draft moved by one sentence. The night before, a teammate had written that we seemed "too focused on making minute changes ... a small addition to the specific trades we're going to be making in a decade's time."
- Stakes: Days of the office's time, a week before the IPS.
- Decision or response: A rule: no IPS paragraph gets more than two stages in one round, and if the answer is a trade after 2030, its numbers go to the Final Report.
- What changed afterwards: Later rounds named the paragraph a stage could move before it started.
- Vivid detail: Five stages and four model scripts, to move the draft by one sentence.
- Strand: learning and growth
- Evidence: `keel/office/outbox/2026-10-28_rooftop_one-sentence-for-nine-beats.md`; `keel/loop/LESSONS.md` LS-10; `archive/bible_2026-11-08/BIBLE.md:276`.

### K-47: A username in a public repository
- Date (Sydney): Tue 20 Oct, 10:37; Fri 23 Oct, 09:22
- Origin: KEEL
- What happened: Our repository was public until 23 Oct. A fact sweep on 20 Oct found the team's WInS username written twice in the rules file and removed it; on 23 Oct another copy was found in a compliance audit written on 17 Oct and redacted. The repository was made private the same day.
- Stakes: The security of the trading account only one student may use.
- Decision or response: Removed and redacted; a standing rule never to commit personal data or credentials.
- What changed afterwards: The same rule caught a student's school email in file paths on 8 Nov (K-43).
- Vivid detail: "WInS username removed twice (public repo)".
- Strand: response to challenges
- Evidence: commit `f9adf01`; commit `d401ba2` ("Redact WInS username from the 17 Oct compliance audit"); CLAUDE.md ("Repo is private (made private by Ray on 23 Oct 2026; it was public before)").

### K-48: The checks passed, but the sheet we'd trade from was stale
- Date (Sydney): Wed 30 Sep, 15:12 and 16:18
- Origin: KEEL
- What happened: Two days before the first planned trades, our pre-trade gate passed 413 checks with zero failures. A new check comparing the team's live spreadsheet (the order tickets and notes the team would trade from) with the checked files found it stale: an old maximum price, 26 example notes, a retired ticket and 4 missing ones. The fourth run passed 490 checks and still found 31 stale rows in the live tabs.
- Stakes: Orders placed from the wrong price limits or notes, which cannot be edited once saved.
- Decision or response: Flagged "fix before Friday"; the live tabs became part of the gate.
- What changed afterwards: Checks cover the copy the team actually uses, not only the files the office keeps.
- Vivid detail: 413 checks and zero failures, while the team's live order tickets still carried an old maximum price of 97.940.
- Strand: research and decision process
- Evidence: commits `dd68e6e`, `33d7de9`; `archive/rab/gates/gate_C.md`.
