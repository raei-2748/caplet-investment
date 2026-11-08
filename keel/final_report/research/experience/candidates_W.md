# Candidate experience events, W series: the project record

Mined Mon 9 Nov 2026 (Sydney) from the project record (students' journal and notes, decision queue, instructions log,
change log, run log, office memos, WInS snapshot, commits), 27 Sep to 9 Nov 2026, plus last year's lessons. Notes for
the blind pool (`blind.py`), not report prose. Ranked most compelling first. Every card's facts are confirmed in the
files named under Evidence; times are Sydney unless marked ET. The eighteen events of `../EXPERIENCE_RECORD.md` are all
here: W-01, W-02, W-03, W-05, W-07, W-13, W-14, W-15 (16 Oct and the 6 Nov close), W-16, W-19, W-35, W-36, W-38,
W-39, W-44, W-45, W-46.

### W-01: The model that sank our own first plan
- Date (Sydney): Sun 27 Sep
- Origin: CAPLET
- What happened: Our first plan put about three-quarters of Laura's money in shares and trusted growth to cover her ten $50,000 payments. The day before trading opened we ran it through 200,000 simulated markets. It missed a payment in 3.2% of them, in 13.7% if her 2028 deposit came in at $75,000 instead of $150,000, and in 40.8% if that deposit never came, while a plan that bought the ten payments in Treasuries first never missed one.
- Stakes: The case asks for the payments to be met "with a high degree of certainty"; a plan that fails one time in thirty, or two times in five if a deposit slips, fails the case's first test.
- Decision or response: We dropped our own plan before placing a single trade and rebuilt it around buying the payments first, with only money no payment depends on going into shares.
- What changed afterwards: Payments first became the spine of everything we submitted, and we learned that the share weight we had argued over (50, 60 or 70% of the growth money) moved the median result by only about $2,000 either way.
- Vivid detail: 40.8%: how often our first plan missed a payment if the 2028 deposit never arrived.
- Strand: learning and growth
- Evidence: `keel/library/verified_2026-09-27/strategy_mc.py` (PATHS = 200_000, SEED 20260927); CLAUDE.md open items: "Growth-first: 3.2% miss; ... 13.7% miss if 2028 deposit is $75k, 40.8% if $0" and "Equity weight 50/60/70% in the sleeve: median $205k/$207k/$209k (barely matters)"; `keel/library/council_2026-09-27/team_notes_2026-09-27.md` (the team's ~75% equity notes); `keel/final_report/research/EXPERIENCE_RECORD.md` row Sun 27 Sep; students' timeline `keel/library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/01_experience_with_caplet_edits.txt`

### W-02: 00:30 in Sydney, and the click that cancelled the wrong order
- Date (Sydney): Wed 7 Oct (first order 10:55) to Thu 8 Oct (US open 00:30)
- Origin: CAPLET
- What happened: We placed our orders from Sydney while the US market was shut, starting at 10:55 on Wed 7 Oct, so they would fill at New York's open, which fell at 00:30 our time. During the session an automated browser click landed on the wrong row because the page had scrolled, and WInS cancelled our May 2038 Treasury order on the spot, with no confirmation step; we re-placed it at 15:22. That night one of us fell asleep waiting for the open.
- Stakes: WInS cancels instantly and trade notes cannot be edited, so one wrong click could strip a rung from Laura's ladder or leave a mistaken order and note on the record judges read.
- Decision or response: We made a rule the same day: only our team leader places or cancels WInS orders.
- What changed afterwards: Every order still open filled by 8 Oct (US time), and the rule held until trading froze on 7 Nov.
- Vivid detail: Our own journal, that night: "our time is freaking 12:30 AM that the market would open".
- Strand: response to challenges
- Evidence: `competition/COMPETITION.md` l.231-232: "on 7 Oct an AI browser click cancelled the wrong order (May-2038) because the page had scrolled. Rule since then: only Ray places or cancels WInS orders."; same file s4 table: "WInS cancels instantly with no confirmation"; `competition/wins/2026-10-23_snapshot.md` l.51: "T-bond May-2038 | 10/7 12:22:11 AM | ... | 10/6 8:13:31 PM (identical text)" (ET, = 15:22 and 11:13 Sydney; first order Nov-2041 10/06 7:55:45 PM ET = 10:55 Sydney); `caplet/google_drive/final_report.md` l.27 (Eric's line)

### W-03: The "copout" objection, and the test we had written before the numbers
- Date (Sydney): Mon 5 Oct (the fund test ran Wed 30 Sep)
- Origin: CAPLET
- What happened: One of us argued that putting the growth money in one world share fund was a "copout" and that we should pick stocks and ETFs like a normal team; a Taiwan fund (EWT) and gold (GLD) were raised too. For the gold idea we already had a test, written down before any number was run: leave the world fund (VT) only if an alternative lifted Laura's bad-case gift by $2,000 or narrowed its spread by 10%, on every run of the model. Gold plus property trusts came closest, with a spread ratio of 0.8991 against a bar of 0.90, but it passed on only 80-85% of runs and partly by trimming Laura's good outcomes.
- Stakes: The growth money is Laura's only upside for the facility gift and her flexibility; a weak answer would have left the plan's simplest part looking lazy to judges.
- Decision or response: We kept the one world fund; a Taiwan fund had already been ruled out on 28 Sep as tokenism and concentration in one small market.
- What changed afterwards: Our VT trade note turned the argument into a principle: "VT is where we allow ourselves to be wrong", because it is the only holding not standing between Laura and a payment date.
- Vivid detail: 0.8991 against a bar of 0.90: gold and property passed by 0.001, then failed the every-run rule.
- Strand: teamwork/communication
- Evidence: `caplet/google_drive/final_report.md` l.23: "5 Oct: Darren argued the world fund is a 'copout' and proposed normal stock and ETF picking; Taiwan (EWT) and gold (GLD) were also raised"; `archive/rab/decisions/D_fund_choice.md` (WS3, 30 Sep): "Decision: keep VT"; "Rule, written before any number was run"; "its spread ratio is 0.8991 ... 0.001 under the 0.90 bar ... passes on 80-85% of seeds ... so it fails the every-seed clause"; `keel/library/insight_v1/strategy_changes.md` l.44 ("EWT, AI or thematic tilts: tokenism and concentration"); `keel/rooms/archive.md` l.50 (submitted VT reflection)

### W-04: Our own trade note's warning came true
- Date (Sydney): Thu 22 Oct (US close), found Fri 23 Oct about 15:20
- Origin: KEEL
- What happened: When we bought IBTR on 7 Oct, its trade note set a test in writing: on that day's curve Laura's first $300,000 bought all ten payments, but if yields fell more than about 0.2 percentage points by January, the 2028 deposit would have to top up the ladder. On the 22 Oct close the 10-year yield was 0.31 points below 6 Oct and the cost of the ten crossed $300,000 for the first time, at $302,863. By then the team had already chosen three other notes for the Trading Notes Analysis it submitted that night, so the one prediction that came true was not among the three judged.
- Stakes: Judges read only three notes; the clearest proof that we understood our own main risk sat in a note they would not see.
- Decision or response: We kept the three chosen notes and carried the test into the IPS as a rule: if the ladder costs more than $300,000, the 2028 deposit completes it.
- What changed afterwards: The rule turned out to be needed, not hypothetical: at the 6 Nov close, the last before the freeze, the ten cost $301,544.
- Vivid detail: The 7 Oct note: "If yields fall more than about 0.2 percentage points by January, the 2028 deposit would top up the ladder"; on 22 Oct yields had fallen 0.31.
- Strand: learning and growth
- Evidence: `caplet/google_drive/ips_report/05_trading_note_reflection_wins_trading_notes.md` l.15 (IBTR note, 10/07/2026 04:42:53 AM ET, quoted); `keel/library/assistant_review_2026-10/oct23/tna_status.md` l.8 ("Picks changed: IBTR is out of the top table"), l.22 ("The test has now crossed on the 22 Oct close ... so the strongest evidence is now unused"), l.64 ("22 Oct | $302,863 | -$2,863 (crossed) | -0.31"); commit efbabf5 (Fri 23 Oct 09:53 Sydney) "ladder cost crosses $300k"; `keel/final_report/FINAL_IPS_as_submitted.txt` ("we'll simply complete it with the 2028 deposit"); `keel/final_report/NUMBERS.md` s1 ($301,544)

### W-05: We set the drafts aside and wrote our own IPS as a letter
- Date (Sydney): Fri 6 Nov to Sat 7 Nov, in before the 09:00 deadline
- Origin: CAPLET
- What happened: After weeks of drafts prepared for us, we decided none of them sounded like people talking to a client, and on the last day we rebuilt the IPS ourselves through our own rewriting process. We wrote it as a letter, "Dear Laura", in plain sentences around one investing idea: her writing career already behaves like a large holding of shares she cannot sell, so her portfolio should balance it, not add to it. It went in before trading froze at 09:00 on Sat 7 Nov.
- Stakes: The IPS is one of the three pieces the Top 50 is chosen on, and it freezes the strategy: whatever we sent was final.
- Decision or response: We kept the plan we had held since late September and rebuilt only how it was explained: payments in Treasuries, only unpromised money in shares, half the shares promised to no one, the other half moved into Treasuries before 2031.
- What changed afterwards: Our own IPS became the spine of the Final Report; every later figure and claim is checked against it, and nothing in it is redesigned.
- Vivid detail: The letter's last lines: "You take risks on the page. Fair enough; that's your job. With these promises, ours is to take none."
- Strand: learning and growth
- Evidence: `keel/final_report/FINAL_IPS_as_submitted.txt` ("Dear Laura,"; "In effect your career is a large holding of shares, and one you cannot sell"; closing lines quoted); `archive/bible_2026-11-08/BIBLE.md` l.792 (Book 16, Sat 7 Nov 01:54): "through a comprehensive rewriting process ... it sounds HUMAN. Even more importantly, it's COMPREHENSIBLE to humans"; `keel/INSTRUCTIONS.md` I92; `keel/ips_rewrite/VERSIONS.md` (57 numbered versions before it); `keel/final_report/ARGUMENT_LOG.md` (Sun 8 Nov row)

### W-06: The 7.5% we kept
- Date (Sydney): Wed 21 Oct to Tue 27 Oct
- Origin: CAPLET
- What happened: Before stating a return for the world fund, our team leader asked for every published long-run forecast. The newest, J.P. Morgan's release of 19 Oct, put global equities at 7.5% a year, up from the 7.0% our draft IPS cited, so our VT reflection said "about 7.5% a year (as per JPMorgan)". On submission day one check flagged the number as false, reading the older edition's table, where 7.5% belonged to another market; the reflection went in with 7.5%, and four days later the correction was withdrawn on the release's own words.
- Stakes: A submitted reflection cannot be edited, so a wrong number would have stood in front of judges; "correcting" a right number into a wrong one would have been just as bad.
- Decision or response: We kept the figure from the newest edition that our own question had turned up, rather than the older table or the checker.
- What changed afterwards: Every forecast we quote now names its edition and date, and the standing rule became: if a return is quoted, it is 7.5%.
- Vivid detail: J.P. Morgan, 19 Oct 2026: "Global equities are projected to return 7.5% (USD), increasing from 7.0%".
- Strand: research and decision process
- Evidence: `keel/office/outbox/2026-10-21_WO-0003*.md`: "Asked by: team lead (Ray), 21 Oct 2026"; "J.P. Morgan 2027 LTCMA, press release 19 Oct 2026 ... Global equities 7.5% (up from 7.0% in the 2026 edition the IPS cites)"; `keel/rooms/archive.md` l.69 ("a forecast return of about 7.5% a year (as per JPMorgan)"); `keel/library/assistant_review_2026-10/oct23/tna_status.md` l.46 ("FALSE: VT 'about 7.5% a year per JPMorgan'"); `keel/pm/CHANGES.md` (Tue 27 Oct): "Withdrawn ... 'Global equities are projected to return 7.5% (USD), increasing from 7.0%' ... if a return is quoted, it is 7.5%"

### W-07: The stale prices
- Date (Sydney): Tue 29 Sep to Wed 30 Sep
- Origin: CAPLET
- What happened: Before placing any order, we priced every Treasury bond WInS offered against the official Treasury yield curve. Two prices, for the February 2036 and February 2038 bonds, were stale: about a full percentage point of yield away from the curve. Our independent pricing checks of the ladder agreed to the cent, which is how we knew the fault was in the simulator's prices, not in our sums.
- Stakes: Buying at a stale price would have meant paying for a yield that did not exist and building a rung of Laura's ladder on a wrong number.
- Decision or response: We wrote a rule the same day, check each bond's yield against the curve, within 0.25 points, before ordering, and swapped the February 2038 bond for the May 2038 one.
- What changed afterwards: Every bond in the book passed the check before it was bought, and the rule stayed in our trading checklist.
- Vivid detail: The February 2036 price sat 111 basis points off the curve; the February 2038 price, 92.
- Strand: research and decision process
- Evidence: `caplet/google_drive/final_report.md` l.19: "two WInS bond prices were stale, about 1 percentage point of yield off the curve. New rule: yield-check every bond (within 25bp) before ordering. Swapped the Feb-2038 bond for the May-2038."; `archive/rab/STATUS.md` l.92 ("2 stale prices (-111bp/-92bp) confirmed; in-book bonds within 25bp"), l.93 ("all 3 pricers agree to the cent"), l.95 ("stale Feb-2036/Feb-2038 prices confirmed -111/-92bp"); `competition/COMPETITION.md` l.114

### W-08: Thirteen edits that softened our voice, all turned down
- Date (Sydney): Fri 23 Oct, 19:12 to 21:08
- Origin: CAPLET
- What happened: On the evening the Trading Notes Analysis was due, a teammate's rewrite of our three reflections arrived at 19:12 and went through a final check, which proposed 13 edits to make the wording safer and clearer. At 21:08 our team leader rejected all thirteen: clearer, he judged, but they softened the voice. We submitted that night with our own confident phrasing, including calling the bonds a "near-ironclad guarantee".
- Stakes: The reflections lock on submission; hedging every claim would have made the team sound unsure of a plan it believed in, while keeping bold words meant every one had to be defensible.
- Decision or response: We kept our assertive voice and made it a standing rule: checks flag only hard problems such as limits, rule breaches and factual errors, not tone.
- What changed afterwards: Confident, assertive phrasing became the team's stated preference for every later draft.
- Vivid detail: 13 suggested edits, all rejected at 21:08 on deadline night.
- Strand: teamwork/communication
- Evidence: commit 66d5403 (Fri 23 Oct 21:09 Sydney), `keel/office/LEDGER.md` WO-0007: "'Rewritten' TNA (Ahaan edit, 7:12 pm Sydney)"; "Ray rejected all 13 (23 Oct 21:08 Sydney): clearer but softens the voice. STANDING RULE: Caplet prefers confident, assertive phrasing; Keel checks flag only hard issues (limits, rule breaches, factual errors"; commit 44bf900 (Fri 23 Oct 23:52 Sydney) "Mark the TNA submitted"; `keel/rooms/archive.md` (submitted reflection 1)

### W-09: "Metaphors alone does not count as creativity"
- Date (Sydney): Thu 5 Nov, 19:09 to 21:09
- Origin: CAPLET
- What happened: Two days before the deadline, our team leader read the near-final IPS draft, built around the image of an extended-release tablet, and rejected its idea of creativity: "metaphors alone does not count as creativity. We want intellectual creativity, yours just packaging." A minute later he added that the medicine image made Laura sound like a patient. At 21:05 he pushed further: "What is the biggest strength our strategy?"
- Stakes: Creativity is one of Wharton's five criteria; a draft whose only originality was a picture would have been scored as decoration.
- Decision or response: We dropped the medicine imagery and asked what was actually new in the strategy itself; the answer was that both ends of Laura's 2031 range are owned before she names them.
- What changed afterwards: Creativity is now judged in the reasoning, not the wording; the IPS we submitted carries no extended metaphor and opens on one investing idea.
- Vivid detail: One minute later, at 19:10: "she doesn't need any rehab."
- Strand: learning and growth
- Evidence: `keel/INSTRUCTIONS.md` I84 ("Ray, 19:09 Sydney: 'metaphors alone does not count as creativity. We want intellectual creativity, yours just packaging.'"), I85 ("19:10 ... 'she doesn't need any rehab'"), I86 ("21:05 and 21:09 ... 'What is the biggest strength our strategy?'"; answer: "the 2031 range owned at both ends before it is said"); `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-10: A former Wharton judge says the IPS cannot make it
- Date (Sydney): by Mon 19 Oct
- Origin: CAPLET
- What happened: A former Wharton judge told the team that our IPS, as it stood in mid-October, could not reach the semifinals. The judge's reasons were not passed on, so we read the draft again against Wharton's official criteria to work out why. The likeliest answers: it played the case's one real choice very safely without arguing it for Laura, it claimed more certainty than the holdings gave, and Laura was barely in it.
- Stakes: Three weeks before the deadline, an experienced outside reader said our main written deliverable was not good enough.
- Decision or response: We treated the verdict as a diagnosis to make, not a judgement to argue with, and checked the draft line by line against the case and the judging criteria.
- What changed afterwards: Within a week our team leader ordered the IPS rewritten from scratch, slowly and with deep research.
- Vivid detail: The diagnosis in one line: "Laura is barely in it."
- Strand: response to challenges
- Evidence: `keel/office/outbox/2026-10-19_WO-0002_judging_ips-v5-why-not-semifinal.md` l.5: "Context (team report ...): a former Wharton judge told the team that the IPS cannot reach the semifinals. The judge's reasons were not passed on"; findings 1-3 ("played very safely, and V5 never argues the trade-off for Laura"; "It claims more certainty than the holdings give"; "Laura is barely in it"); CLAUDE.md (26 Oct: "IPS rewritten from scratch"; Ray's order "rewrite from scratch, slowly, with deep research and thought")

### W-11: Laura's career is a stock she cannot sell: six weeks to find the words
- Date (Sydney): Sun 27 Sep to Sat 7 Nov
- Origin: CAPLET
- What happened: In our first client notes, before trading opened, we wrote that Laura's career already carries concentrated risk from publishing, speaking and licensing, so her portfolio should not add more of the same. The idea sat in the background through weeks of drafts. By 5 Nov our handwritten pitch called it "Laura's human capital that fluctuates with stocks", and in the IPS we submitted it became the opening line.
- Stakes: Every team gets the same numbers; a reason rooted in who Laura is was our best chance to show client knowledge another team would not have.
- Decision or response: We made it the reason for the whole structure: her fixed payments go into Treasuries because her income already behaves like shares.
- What changed afterwards: It turned "payments first" from a textbook rule into an argument about this client; a scan of 36 simulated rival plans found none that used it.
- Vivid detail: The submitted pitch: "Laura's career is already a giant stock she can't sell. So we hedge it!"
- Strand: learning and growth
- Evidence: `keel/library/team_materials/review_why_laura_and_public_profile.md` (team documents reviewed 27 Sep): "her career already carries concentrated risk (publishing, speaking, licensing), so the portfolio should not add correlated risk"; `keel/ips_rewrite/caplet_doc/2026-11-05_one_check.md` l.13 ("'Laura's human capital that fluctuates with stocks' (Handwritten)"); `keel/final_report/FINAL_IPS_as_submitted.txt` (pitch); `keel/pm/CHANGES.md` (Tue 27 Oct night: "0 of 36 have human capital or a two-cost range")

### W-12: Promise only what is already owned
- Date (Sydney): Wed 28 Oct
- Origin: KEEL
- What happened: We tested five ideas in the model for how Laura should state her 2031 range to co-sponsors. One stood out: when she names her range, the half of her shares promised to the gift moves into Treasuries, so the top of the range is money she owns, not a share price. In the model the top was then reached about 93% of the time instead of about 77%, at a cost of about $1,600.
- Stakes: Co-sponsors plan around the range Laura names; a top that markets could take back after she named it would cost her the credibility the case says overpromising damages.
- Decision or response: We adopted it as a rule in plain words: no number Laura names rests on a share price; each is owned in Treasuries by the day she names it.
- What changed afterwards: The team's own IPS kept it, so both ends of the range are money Laura owns before she speaks.
- Vivid detail: The submitted IPS: "Before you meet co-sponsors in 2031, the other half will move into Treasuries, so whatever figure you choose is money you already own."
- Strand: research and decision process
- Evidence: `keel/pm/CHANGES.md` (Wed 28 Oct overnight): "'lock what you announce' (in 2031 the promised half of the stocks moves into Treasuries, so the top is reached ~93% vs ~77% for ~$1.6k)"; (Wed 28 Oct): "No number Laura names rests on a share price: each is owned in Treasuries by the day she names it."; `keel/final_report/FINAL_IPS_as_submitted.txt` l.15 (quoted)

### W-13: Wharton's 6 Oct email takes away our floor
- Date (Sydney): Tue 6 Oct
- Origin: CAPLET
- What happened: On the same day, in New York time, as our first orders, Wharton emailed that Laura's real plan, not just the simulator, could use only stocks, ETFs and Treasury bonds listed in WInS. Our floor for the 2031 facility gift rested on zero-coupon Treasury STRIPS, which WInS does not list. We moved the floor to IBTM, an iShares fund holding Treasuries that mature in December 2032, and marked every STRIPS-based number in our files as superseded.
- Stakes: A floor built on an instrument the rules had just ruled out would have made the core of Laura's 2031 promise non-compliant, the same kind of mistake as last year's trades outside the rules.
- Decision or response: We rebuilt the floor and re-ran the numbers on instruments WInS actually lists.
- What changed afterwards: When Wharton's FAQ banned TIPS and STRIPS outright on 20 Oct, nothing in our plan had to change; the submitted IPS calls the floor "a Treasury fund maturing in late 2032".
- Vivid detail: One email turned every STRIPS figure in our files into history; the banners on those files still say "superseded".
- Strand: response to challenges
- Evidence: CLAUDE.md: "6 Oct Wharton email: Laura's real plan may use only WInS-listed stocks, ETFs and Treasury bonds. STRIPS-based numbers ... are superseded (banners added). The floor is IBTM."; `archive/rab/decisions/D_fund_choice.md` l.1 ("STRIPS/zero-coupon references are superseded"); `competition/wins/2026-10-23_snapshot.md` (first order 10/06 7:55:45 PM ET); `competition/COMPETITION.md` s4; `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-14: Last year's lessons
- Date (Sydney): 2025-26 season, carried into Sun 27 Sep
- Origin: CAPLET
- What happened: Four of this year's six were on last year's team, which picked 12 themed stocks aiming at an 11-12% return, traded assets outside the rules, and never heard back from the judges. One position, FMC, fell 54% on a $10,000 allocation, a $5,400 loss. That year's report said "clarity beats complexity" and then wrapped a simple idea in heavy packaging.
- Stakes: Repeating any of those mistakes would have cost us the semifinal before a judge read a word of strategy.
- Decision or response: We began this year with three rules: check every trade against this year's rules and permitted list before placing it; complexity must earn its place; client first.
- What changed afterwards: All eleven of this year's trades stayed inside the permitted list, and the plan holds no individual stock picks: the growth money sits in one world fund.
- Vivid detail: Last year's report: "Our FMC position fell 54 percent on a $10,000 allocation, resulting in a $5,400 loss".
- Strand: learning and growth
- Evidence: `caplet/google_drive/2025_knox_wharton.md` (quoted line); `keel/library/assistant_review_2026-10/04_North_Star_Memo_16Oct2026.md` (four of six names on last year's team; 11-12% target; 12 themed stocks; "clarity beats complexity"); CLAUDE.md "Team" (Ray: "strategy packaging was over-complex for the insight; the team traded assets outside the trading rules. So: complexity must earn its place; check every trade ...; client first"); `competition/wins/2026-10-23_snapshot.md`

### W-15: From $1,913 of room to $1,544 over the line
- Date (Sydney): Fri 16 Oct to the 6 Nov close (US), the last before the freeze
- Origin: KEEL
- What happened: As US yields fell through October, the cost of Laura's ten payments crept up toward her $300,000 first deposit. On the 16 Oct curve the ten cost $298,087, leaving $1,913 of room, about 0.07 percentage points of yield. At the 6 Nov close, the last before trading froze, they would cost $301,544 on 1 Jan 2027: just over the deposit.
- Stakes: A little more fall in yields and the first deposit could no longer buy all ten, and our draft IPS of mid-October did not say in plain words what would happen then.
- Decision or response: We stopped treating "under $300,000" as a fact and wrote a rule for when it fails: the 2028 deposit completes the ladder first, before any money goes to the facility.
- What changed afterwards: The rule went into the IPS ("we'll simply complete it with the 2028 deposit") and, on the day the portfolio locked, it was needed rather than hypothetical.
- Vivid detail: $1,913 of room on 16 Oct; $1,544 over on 6 Nov.
- Strand: response to challenges
- Evidence: CLAUDE.md: "Ladder headroom fell to $1,913 (7bp) on the 16 Oct curve (cost $298,087)"; `keel/final_report/research/EXPERIENCE_RECORD.md` (Fri 16 Oct: "Why the IPS says the 2028 deposit completes the ladder if yields fall"); `keel/final_report/FINAL_IPS_as_submitted.txt`; `keel/final_report/NUMBERS.md` s1 ($301,544, 6 Nov close)

### W-16: Fifty-seven versions
- Date (Sydney): Mon 26 Oct to Wed 4 Nov (status note Tue 3 Nov)
- Origin: KEEL
- What happened: On 26 Oct our team leader ordered a slow rewrite of the IPS ("THINK ... I don't want you to be hasty"), and five drafts were written that same day. By 4 Nov there were 57 versions, many ranked by panels of simulated judges. On 3 Nov our own status note to the team admitted the problem: the ideas had been settled by about 28 Oct, and most of the 40 versions after that were rewording.
- Stakes: Every hour spent polishing sentences was an hour not spent improving the plan or making it clear to the six of us who had to submit it.
- Decision or response: We wrote the team a one-page plain-English status and stopped measuring progress by version count.
- What changed afterwards: For the Final Report the order is reversed: no prose until Fri 27 Nov, research and thinking first.
- Vivid detail: The 3 Nov status note: "55 versions is a sign we were polishing words, not improving the plan."
- Strand: learning and growth
- Evidence: `keel/ips_rewrite/VERSIONS.md` (57 numbered rows; row 57 dated Wed 4 Nov); `caplet/STATUS_2026-11-03.md` l.23 (quoted); students' timeline `.../01_experience_with_caplet_edits.txt` l.34 ("The ideas were settled by about 28 Oct. Most of the next 40 versions were rewording."); `keel/INSTRUCTIONS.md` I41 ("THINK ... I don't want you to be hasty"; "D1, D1.2, D1.3, D2 and D3 were all written on 26 Oct"), I89-I91

### W-17: Testing our own central claim against 2009 and 2020
- Date (Sydney): Sun 8 Nov
- Origin: KEEL
- What happened: After the IPS was in, we tested its central claim, that a writer's income comes "later and smaller" in a recession, against publishing data from three downturns. 2001 was flat. The 2008-09 recession supported it: advances were cut, acquisitions frozen, speaking budgets cut and licensing royalties down 8.7%. 2020 did not: print book sales rose 8.2%, graphic novels rose 29%, and Laura's own comic went viral in the crash year.
- Stakes: If the claim at the heart of the IPS fell to a judge's first counter-example, the client argument would fall with it.
- Decision or response: We kept the claim but recorded it as only partly supported, with the counter-evidence written down, because the plan is frozen and the Final Report must be honest about where the comparison breaks.
- What changed afterwards: Our notes now describe her career as a single, hit-driven stock whose danger is the bad years, not as a plain index fund that rises and falls with the market.
- Vivid detail: Graphic novels sold 29% more in 2020, the year of the COVID crash and the year Laura's comic went viral.
- Strand: research and decision process
- Evidence: `keel/final_report/research/cards/Q1_career_as_shares.md` (Sun 8 Nov) row 32 ("print units +8.2% ... graphic novels +29%"), row 45, row 46 ("Her career is not a plain index holding: its best year so far came when markets crashed. It is a single, hit-driven stock whose danger is the left tail"); `keel/final_report/CANON.md` l.115 (B4 "PARTLY"; "licensing royalties down 8.7% in 2009"); `caplet/google_drive/notes_and_discussions.md` l.236 ("The only market crash in her career was her best year")

### W-18: Three simulated Lauras called us "too timid", so we tested a smaller floor
- Date (Sydney): Mon 28 Sep to Tue 29 Sep
- Origin: KEEL
- What happened: In a blind test, three simulated readers playing Laura each ranked six anonymous plans; all three put ours first, and all three called it too timid, with only about 9% in shares. We took the criticism seriously and tested smaller floors for the 2028 deposit, from $150,000 down to $50,000, with the rest in the world share fund. Each $25,000 less floor added only about $2,000-3,000 to the middle outcome but cost about $9,000-10,000 in a bad market and about $15,000 in the worst historical case.
- Stakes: If the critics were right, the plan was leaving Laura's money on the table; if they were wrong, more shares would weaken her 2031 promise for little gain.
- Decision or response: We kept the $150,000 floor and answered "timid" with the price of certainty instead of adding shares.
- What changed afterwards: The 1 Oct model check backed the same floor and the strategy was locked; "timid" became a trade-off we could state in numbers.
- Vivid detail: Cutting the floor from $150,000 to $100,000 would cut the share of her likely gift Laura already owns from 86% to 68%.
- Strand: research and decision process
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.101 ("three pretend Lauras ... all three ranked yours first. All three also said it looks too timid, with only about 9% in stocks"), Strategy Log 29 Sep l.280-301 ("Smaller-floor test"; "Each $25k less floor adds only about $2-3k to the middle outcome, but costs about $9-10k in a bad market and about $15k in the worst historical case"; "With $150k she already owns 86% of the likely gift ... with $100k it's 68%"); `caplet/google_drive/final_report.md` l.21 (1 Oct)

### W-19: The rival's plan beat our designer's
- Date (Sydney): Sun 27 Sep to Mon 28 Sep
- Origin: KEEL
- What happened: In our first deep research run, 472 questions were cut to 48 that survived skeptical filters, and a designer drew up a plan that was then attacked by a simulated judge, a simulated Laura and a simulated rival team. The rival team's plan beat our own designer's, so the rival's plan became our recommendation: buy the payments with the first deposit, then a Treasury floor and one world fund with the second.
- Stakes: Recommending our design because it was ours would have meant a worse bad case for Laura.
- Decision or response: We switched to the better plan and kept the earlier idea, locking growth in 2031, only as the alternative to compare against.
- What changed afterwards: Against that alternative, the new plan's bad case was better: about $182,000 against $168,000 at the 5th percentile, and $169,000 against $120,000 in the worst six-year window of history.
- Vivid detail: 472 questions in, 48 survived; the plan that won was the one built to beat ours.
- Strand: research and decision process
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.87-100 ("472 questions -> 48 survived"; "The pretend rival team's plan beat your own designer agent's plan, so it became the final recommendation"); CLAUDE.md insight_v1 section (REC vs ALT "the earlier 2031 lock": "p5/p50/p95 $182k/$207k/$250k vs $168k/$210k/$266k; worst historical 6-year window $169k vs $120k")

### W-20: The cheapest the payments had been since 2002
- Date (Sydney): Mon 28 Sep
- Origin: KEEL
- What happened: We priced Laura's ten payments on every Treasury yield curve since 2000, 6,688 trading days, each time with the payments the same distance ahead. In August 2020 they would have cost $470,249, more than all the money Laura will ever deposit; on 28 Sep 2026 they cost $289,119, the cheapest since May 2002. On only 11% of days since 2000 would $300,000 have bought all ten, and before this September on no day since 2008.
- Stakes: The chance could vanish before January: the model gave about a 1 in 4 chance that the ten would cost more than $300,000 by then.
- Decision or response: It became the reason for the plan's order: buy every payment with the first deposit while certainty is cheap, and grow only what is left.
- What changed afterwards: It explained choices that otherwise looked timid, such as holding no shares in the first $300,000.
- Vivid detail: $470,249 in August 2020; $289,119 on 28 Sep 2026.
- Strand: research and decision process
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.309-322 ("$289,119, the cheapest since May 2002"; "Only 11% of days since 2000 would $300k have bought all ten payments, and no day between 2008 and today would have"; "about a 1 in 4 chance the ladder costs more than $300k by January"; "Why no stocks in the first $300k? Because this rare chance buys all ten promises")

### W-21: Our notes priced the payments at 4%; the real curve said otherwise
- Date (Sydney): Sun 27 Sep
- Origin: CAPLET
- What happened: Our first strategy notes rightly treated the case as a pension-funding problem, but priced it with a flat 4% rate in one place and a 10-year yield of about 5.1% in another, and listed that clash among their own known contradictions. At 4% the payments were worth about $333,000 in 2027, more than Laura's first deposit. A search summary also claimed the 10-year yield was 4.22%; the official Treasury table for 25 Sep said 5.17%.
- Stakes: At 4% buying all ten payments with the first deposit looks impossible; with the wrong yield, the strategy would have been built on a number that did not exist.
- Decision or response: We retired both rates and priced each payment off one verified Treasury curve on one date.
- What changed afterwards: On the official curve the ten cost $292,264, under the deposit, which made payments first possible; since then every rate we use comes from a primary file with its date.
- Vivid detail: 4.22% from a search summary against 5.17% in the Treasury's own table.
- Strand: research and decision process
- Evidence: `keel/library/council_2026-09-27/team_notes_2026-09-27.md` (student-authored, 27 Sep) l.34 ("Reserve PV in 2027 = L2033/1.04^6 ~ $333k (> first $300k deposit)"), l.52-55 ("KNOWN INTERNAL CONTRADICTIONS"; "4% in one place, 5.1% in another"); `keel/library/council_2026-09-27/01_chair_memo.md` s2 ("retire both the flat 4% and '10y 5.1%'"); CLAUDE.md ("10y 5.17 ... (A search summary claiming 10y 4.22% was wrong.)"; "Ten payments valued at 2027-01-01 from that curve: $292,264")

### W-22: The name we kept changing
- Date (Sydney): Thu 1 Oct to Sat 7 Nov
- Origin: CAPLET
- What happened: Our strategy was Roots First, then Root-and-Branch on 1 Oct. On 24 Oct our team leader dropped the roots name and motif, and on 26 Oct a teammate locked in a new name ending in XR, the pharmacy label for extended release, praising X for the ten payments as "the most genius name idea of any team". By 5 Nov all three of our own draft pitches said "Steady Roots", the medicine imagery behind XR had been rejected, and the IPS we submitted used no name at all.
- Stakes: A name is the first thing a judge reads; a clever one that needs explaining eats into a 50-word pitch and a 500-word limit.
- Decision or response: In the end we let the plan speak for itself and spent the words on Laura rather than on a label.
- What changed afterwards: We learned that a name has to carry an idea about the client or it is decoration, the same test we later applied to every metaphor.
- Vivid detail: A teammate, asking for a better R: "'10 releases' is quite frankly just a weird name for an investing strategy".
- Strand: learning and growth
- Evidence: `caplet/google_drive/final_report.md` l.21 ("Strategy name settled as Root-and-Branch (earlier 'Roots First')"); `keel/rooms/archive.md` l.77 ("Ray, 24 Oct: name and roots motif out"); `archive/bible_2026-11-08/BIBLE.md` Book 5 (Mon 26 Oct; quoted lines; author Ahaan per `keel/INSTRUCTIONS.md` I48); `keel/ips_rewrite/caplet_doc/2026-11-05_one_check.md` l.40 ("All three pitches say Steady Roots"); `keel/INSTRUCTIONS.md` I85; `keel/final_report/FINAL_IPS_as_submitted.txt` (no strategy name)

### W-23: Fifteen famous writers, and a draft that made no sense
- Date (Sydney): Sun 1 Nov (verdict 16:26)
- Origin: KEEL
- What happened: Asked to learn from the best human writing, we rebuilt the IPS sentence by sentence on the shapes of fifteen writers, from Feynman and Orwell to Buffett and Munger, with a source logged for every sentence, and a second version the same day added five more. That afternoon a teammate rejected it entirely: it opened on a rhetorical question he called "the corniest and most cringeworthy thing I've ever seen", and "half of your sentences just DON'T MAKE SENSE".
- Stakes: Three days before the final IPS was due for the team's review, the drafts were getting cleverer and harder to read.
- Decision or response: We threw the version away and rebuilt from scratch the same day: no opening question, no model results in a strategy document, no story of our own progress.
- What changed afterwards: Later drafts were written to be understood by a person on one reading, cutting whole ideas rather than squeezing sentences; the same teammate named the obsession with brevity as what made the writing sound unnatural.
- Vivid detail: The verdict, 1 Nov: "half of your sentences just DON'T MAKE SENSE".
- Strand: response to challenges
- Evidence: `keel/ips_rewrite/VERSIONS.md` rows 48-50 ("every sentence modelled on a real sentence by one of 15 writers (Feynman, Didion, Orwell, E. B. White, Buffett, Marks, Munger ..."; "eight sentences rewritten on new sources (Baldwin, Dillard, Keynes, Taleb, Damodaran"; "Ahaan's Book 11 rejected V49 entirely. Rebuilt from scratch"); `archive/bible_2026-11-08/BIBLE.md` l.318 (Book 11, Sun 1 Nov 16:26); `keel/INSTRUCTIONS.md` I71-I74; students' timeline `.../01_experience_with_caplet_edits.txt` l.35

### W-24: The one-stock-per-sector rule that was not a rule
- Date (Sydney): Mon 5 Oct
- Origin: CAPLET
- What happened: A teammate found a rule saying each team member must hold one stock per sector. We traced where it came from: a third-party website mislabelled as 2026-27, Wharton's guidebook from 2015-16, and a teacher's blog from 2021. This year's official Trading Details page has no sector minimum at all.
- Stakes: Obeying a dead rule would have forced six unwanted stock picks into a plan built on Treasuries and one world fund; ignoring a real one would have repeated last year's rule breach.
- Decision or response: We followed the primary source and kept the plan as it was.
- What changed afterwards: We wrote the lesson into our own journal: check the primary source.
- Vivid detail: The rule's trail ended in a 2015-16 guidebook and a 2021 blog; our journal's verdict: "Lesson: check the primary source."
- Strand: research and decision process
- Evidence: `caplet/google_drive/final_report.md` l.22 ("We traced it to a third-party site mislabelled 2026-27 (wghs.org.cn), the official 2015-16 guidebook and a 2021 teacher blog; this year's official Trading Details says there is no sector minimum. Lesson: check the primary source."); CLAUDE.md ("NO sector minimum (the 'sector minimum = team size' claim is false)")

### W-25: The best line in the draft was false
- Date (Sydney): Fri 30 Oct, 09:40
- Origin: KEEL
- What happened: The strongest line in our Saturday draft read: "wipe out every share she owns and no cheque is worse off". A check against our own model found it false: with the shares wiped out, a payment came out worse in about 1 path in 500, by up to $2,812, because money banked from the shares in 2031 also stood behind the payments. The true statement ran the other way: the shares can help a payment, never hurt one.
- Stakes: A dramatic claim contradicted by our own numbers is exactly what a bond professional on the panel would test first.
- Decision or response: We replaced it with the true, shorter line, "The shares can help a cheque, never hurt one", which held in 600,000 of 600,000 modelled paths.
- What changed afterwards: The wipe-out thought experiment moved to the Final Report, where it can be told with its true ending.
- Vivid detail: 364 of 200,000 paths: the line's own test, read backwards.
- Strand: research and decision process
- Evidence: `keel/office/outbox/2026-10-30_window_the-wipe-out-line.md` ("is false in our own model: the shares never hurt a cheque, but wiping them out does leave one worse off in about 1 path in 500"; "364 / 354 / 412 of 200,000 paths ... by up to $2,812"); `keel/pm/ASK_HUMANS.md` l.48 ("'The shares can help a cheque, never hurt one.' Reason: true in 600,000 of 600,000 MODEL paths"); `keel/pm/RUNLOG.md` l.90

### W-26: $85,000 was really $125,000
- Date (Sydney): Fri 30 Oct (night)
- Origin: KEEL
- What happened: A draft said Laura's 2028 deposit could fall to about $85,000 after a two-point fall in yields before her payments were at risk. Rechecking the plan as written, we found the true figure was about $125,000: the plan had $40,000 less room for bad luck than we were about to claim.
- Stakes: Overstating the safety margin is the most damaging error a payments-first plan can make.
- Decision or response: We corrected the figure before it went anywhere and named instead the only two things that could break a payment.
- What changed afterwards: The submitted IPS uses the same frame: "There are only 2 possible reasons we would change our plan", a missed deposit or a Treasury default.
- Vivid detail: $85,000 claimed, $125,000 true.
- Strand: research and decision process
- Evidence: `keel/pm/CHANGES.md` l.33 (Fri 30 Oct night: "on this plan the 2028 deposit can fall to about $125,000 (not $85,000) after a two-point yield drop"; "V39 says only two things break a cheque"); `keel/final_report/FINAL_IPS_as_submitted.txt` (quoted)

### W-27: One word in our locked notes: "duration-matching"
- Date (Sydney): Wed 4 Nov
- Origin: KEEL
- What happened: Two outside readers, given only our submitted trade notes and the final IPS draft, separately noticed the same thing: our first reflection said the bonds remove uncertainty "through duration-matching", while the IPS described matching the bonds' average timing as the method we do not use. One reader's suggested fix was itself false: on average our holdings pay back after about 7.6 years, against about 10 years for the payments.
- Stakes: The trade notes were submitted and could not change; a visible contradiction between two judged pieces would undercut the coherence judges reward.
- Decision or response: We treated it as a change of word, not of plan: say "each payment has its own bond", never deny the earlier phrase.
- What changed afterwards: Agreement with everything already submitted became a standing check on every new piece of writing.
- Vivid detail: 7.6 years against 10: the "matched" holdings pay back early.
- Strand: learning and growth
- Evidence: `keel/pm/ASK_HUMANS.md` l.28 (Wed 4 Nov: "Two outside readers ... both noticed, separately, that your first reflection says the bonds remove uncertainty 'through duration-matching' ... It's a change of word, not of plan. One reader's fix ... is false: the ladder comes back early on average, about 7.6 years against the payments' 10.0"; "Rewrite P3 as 'each payment has its own bond', never 'we don't duration-match'"); `keel/rooms/archive.md` (submitted reflection 1); CLAUDE.md ("extreme coherence with everything submitted (frozen)")

### W-28: Hold or trade: "u sure"
- Date (Sydney): Mon 26 Oct to Wed 28 Oct
- Origin: CAPLET
- What happened: Our research support recommended keeping the WInS portfolio exactly as it was until the freeze, rather than making about ten trades to re-size the ladder for a modelled gain of about $1,500. Our team leader, the only one allowed to trade, pushed back with two words: "u sure". A second proposal on 28 Oct, swapping two bonds for low-coupon versions for about $2,000 of protection if rates fell for good, got the same answer.
- Stakes: Ten trades would have meant new notes on a record already judged; not trading meant leaving a small modelled gain on the table.
- Decision or response: The case for holding was sent the same day, our team leader kept the decision as his, and the book was not traded again before the freeze.
- What changed afterwards: The low-coupon idea went to the Final Report instead of into a trade.
- Vivid detail: The whole reply to the recommendation to hold: "u sure".
- Strand: teamwork/communication
- Evidence: `keel/pm/ASK_HUMANS.md` l.71 (Mon 26 Oct: "Keep the WInS book exactly as it is ... ten trades for a ~$1.5k model gain"; "u sure"; "Keel's case for holding sent in the thread the same day; still Ray's call until the freeze"), l.56 (Wed 28 Oct: "thin-coupon twins ... four extra trades and two new trade notes for ~$2k of protection ... the idea goes to the Final Report"); `competition/wins/2026-10-23_snapshot.md` (no trade since 8 Oct)

### W-29: The October trade we never made
- Date (Sydney): Wed 14 Oct to Fri 23 Oct (09:53)
- Origin: KEEL
- What happened: We wrote down in advance the triggers that would make us trade in October, and that if none fired there would be no trade. Through October we re-ran the checks on each new Treasury curve. On 23 Oct, with the ladder's cost now over $300,000, the rule still did not fire, so we held.
- Stakes: A trade made to look active would have cost commissions, added a trade note to explain and moved a portfolio designed to be held.
- Decision or response: We recorded each result and did not trade.
- What changed afterwards: Holding became part of the evidence of discipline: 11 trades out of 200, none after 8 Oct.
- Vivid detail: Our own rule: "If no trigger fires there is no trade, and that is a valid result. We never add a trade to reach a count."
- Strand: research and decision process
- Evidence: `archive/rab/trades/october_trade.md` l.14 (quoted), l.47 ("Write 'checked 14 Oct: the rules said hold'"); commit efbabf5 (Fri 23 Oct 09:53 Sydney) "Update rate checks to 22 Oct: ladder cost crosses $300k; October rule did not fire"; `competition/wins/2026-10-23_snapshot.md`

### W-30: Handing over the decisions, and losing sight of the work
- Date (Sydney): Mon 26 Oct
- Origin: CAPLET
- What happened: With questions piling up for him, our team leader changed how we worked with our research support: "just make your own call whichever you think work the best, do not have danger zone decisoins made for me". Trades, orders, submissions, money and anything sent outside stayed with the six of us. The same day he wrote that he had no idea what was happening in our research work.
- Stakes: Six of us with school commitments could not vote on every modelling choice, but handing decisions over risked a plan we could no longer follow or defend.
- Decision or response: Every delegated call was logged with a one-line reason we could overturn, and one dashboard showed what had been done each day.
- What changed afterwards: Decisions sped up but understanding lagged: on 3 Nov our team leader said we could not follow what had been achieved, which led to one-page plain-English summaries.
- Vivid detail: "do not have danger zone decisoins made for me" (26 Oct, typo and all).
- Strand: teamwork/communication
- Evidence: `keel/pm/ASK_HUMANS.md` l.3-6 (Ray, Mon 26 Oct, quoted; "Only danger-zone decisions wait for a student: anything irreversible or outward-facing, i.e. a WInS trade or order"); `keel/INSTRUCTIONS.md` I19 (26 Oct, quoted; fix: dashboard), I80 (3 Nov: "The team doesn't know what Keel has achieved; Keel overcomplicates things and is hard to follow"); `caplet/STATUS_2026-11-03.md`

### W-31: Why the case file was dated 10 September
- Date (Sydney): Mon 28 Sep
- Origin: KEEL
- What happened: Checking the case document, we found Wharton's PDF had been created on 10 Sep 2026. That was the first day in 2026 on which Laura's ten payments could be bought for less than $300,000; on 173 of the year's first 185 trading days they had cost more.
- Stakes: If the timing was deliberate, the case was built so the first deposit buys the promise and the second funds the building; a team that missed this could split the money the wrong way.
- Decision or response: We read the case as giving Laura's money two jobs, one per deposit, and built on that reading while treating the designers' intent as an interpretation, not a fact.
- What changed afterwards: "Her money has two jobs, one per deposit" became the plainest way to explain the plan's structure.
- Vivid detail: Above $300,000 on 173 of 185 trading days; the case file created on the first day below it.
- Strand: research and decision process
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.173 ("The case PDF was created on 10 Sep 2026. That's the first day in 2026 the ten-payment ladder cost dropped under $300k; it was above $300k on 173 of 185 trading days. Interpretation: ... Her money has two jobs, one per deposit."); CLAUDE.md ("it fits under $300k only since Sep 10")

### W-32: The perfect story we dropped
- Date (Sydney): Sun 27 Sep to Mon 28 Sep
- Origin: KEEL
- What happened: Early research turned up a line that Laura "only leapt once the book deal secured a floor", a perfect story for a plan built on buying a floor first. Checking its source, we found it was a reporter's sentence, not Laura's words. The case's own pull quote did not appear in any of the 25 sources we checked either.
- Stakes: Putting words in a client's mouth is a factual error a judge can catch, and the most tempting story is the one most worth checking.
- Decision or response: We dropped the story and agreed never to quote Laura directly in the trade notes or the IPS.
- What changed afterwards: Every client fact we use is cited as the case's words or a verified source, never "as Laura says".
- Vivid detail: Our note to ourselves: "the most tempting story about a client is often the unverified one".
- Strand: learning and growth
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.242 ("didn't appear in any of 25 sources checked ... A team that writes 'As Laura says...' is making a factual error"), l.244 ("came from a reporter's sentence, not her own words, so it was dropped"; quoted line); CLAUDE.md ("no Laura quotes in the Trading Notes or IPS")

### W-33: The $9,000 bug
- Date (Sydney): Sun 27 Sep to Mon 28 Sep
- Origin: KEEL
- What happened: Our first model priced the bonds at about 5.08% but let spare bond money earn only 4%. That one inconsistency made the all-Treasury option look about $9,000 worse than it really was.
- Stakes: A model tilted against the safest option would have pushed Laura toward more risk for a reason that was only an error, one a statistician on the panel would spot.
- Decision or response: We found it, corrected it and re-ran the comparison.
- What changed afterwards: The all-Treasury plan stayed in later comparisons as the honest benchmark every other plan had to beat.
- Vivid detail: 5.08% in, 4% out: a $9,000 tilt against the safest plan.
- Strand: research and decision process
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.256 ("The original model priced the bonds at about 5.08% but let spare bond money earn only 4%. That made the all-bond option look about $9k worse than it really is. It was found and corrected."), l.296 (all-Treasuries row in the 29 Sep test); `keel/final_report/NUMBERS.md` l.168 (all-Treasury benchmark)

### W-34: Which portfolio should WInS show?
- Date (Sydney): Tue 29 Sep to Thu 1 Oct
- Origin: CAPLET
- What happened: One of us pointed out that WInS gives us $300,000, exactly Laura's first deposit, and never shows her second one. We had to choose: hold her first $300,000 dollar for dollar, which would be all bonds, or hold her whole plan after both deposits, scaled down to $300,000, with about 8.7% in the world fund and the floor inside IBTM. Before the vote, a memo set out the strongest case for each side.
- Stakes: Judges see the WInS portfolio before they read our strategy; an all-bond book would show only one of Laura's three goals, while a scaled book needs explaining.
- Decision or response: We chose the scaled book, so that the payments, the floor and the growth fund all appear in WInS.
- What changed afterwards: Every dollar figure in our notes had to be read as "in Laura's plan, scaled", a cost we accepted; the book stayed unchanged from 8 Oct to the freeze.
- Vivid detail: The option we turned down needed no explaining and left about $2,000 more cash.
- Strand: teamwork/communication
- Evidence: `caplet/google_drive/notes_and_discussions.md` l.303-305 ("Wharton never showed the second deposit (150K later), which means we need to reconsider what the 300K mean"; "Current plan (ii)R ... scaled down to $300k. That's why it includes 8.7% in VT"); `archive/rab/decisions/D7_wins_book.md` ("for the 1 Oct vote"; "Written because the red team ... found no memo that set out both sides before the vote"; "Scale words needed: yes"); `competition/wins/2026-10-23_snapshot.md` (VT 167 held; no trade since 8 Oct)

### W-35: Eleven orders, eleven fills
- Date (Sydney): Wed 7 Oct to Fri 9 Oct (fills 7-8 Oct, US time)
- Origin: CAPLET
- What happened: All eleven orders filled: five iBond Treasury funds, five Treasury bonds and 167 shares of the world fund VT, leaving $3,514 in cash. The plan had been to trade on Fri 2 Oct; in the end every order went in while the US market was closed, between 6 and 7 Oct New York time. We used 11 of our 200 permitted trades, paid $200 in commissions, and the largest order was 1.3% of that day's volume, far inside the limit of twice a security's daily volume.
- Stakes: A single trade outside the rules or the volume limit would have repeated last year's mistake on the first judged record.
- Decision or response: Once filled, we held: the plan was to buy and keep to maturity.
- What changed afterwards: Our own review found one slip, 167 VT shares bought against 164 planned (about $476 over) with no recorded reason; its advice was to keep the position and record why.
- Vivid detail: Fifteen trade notes on eleven trades: four sit on cancelled orders, so two IBTR notes exist, one saying 0.3 points and the filled one "about 0.2".
- Strand: research and decision process
- Evidence: `competition/wins/2026-10-23_snapshot.md`; CLAUDE.md ("11/200 trades, cash $3,514"; "15 trade notes on 11 trades (4 on cancelled orders)"); `keel/library/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md` l.120 ("The cancelled one says '0.3'; the filled one ... says 'about 0.2'"), l.279-288 ("Every order went in while the US market was closed (6 Oct 7:55 PM to 7 Oct 8:27 PM ET). The plan had been Fri 2 Oct"; "largest order was 1.3% of that day's volume (IBTM)"; "commissions were $200"; "VT: 167 shares bought against 164 planned (+$476 ...)")

### W-36: No bond for the missing years, and a ticker that was not ours
- Date (Sydney): Tue 29 Sep
- Origin: CAPLET
- What happened: Searching WInS for a bond to fund each payment, we found no Treasury bond maturing between February 2031 and February 2036, so five of Laura's ten years had nothing to buy. We used iShares iBonds Treasury ETFs, funds that hold Treasuries maturing in one set year and then close, for the 2033-2037 payments. We also caught that "IBTN" in WInS was an unrelated company, not the iBond fund its ticker suggested.
- Stakes: Without a dated instrument for those years the payments could not be matched, and buying IBTN by its ticker would have put an unknown company inside a Treasury ladder.
- Decision or response: We turned the gap into a design: iBond funds (IBTM to IBTR) for 2033-2037 and Treasury bonds for 2038-2042.
- What changed afterwards: The ladder became a mix of two instruments, and we learned the difference that matters: an iBond fund pays out its net asset value at the end, not a promised par value, which our IBTM trade note says in so many words.
- Vivid detail: "IBTN" turned out to be INSCORP Inc.
- Strand: response to challenges
- Evidence: `caplet/google_drive/final_report.md` l.18 ("WInS lists no Treasury bond maturing Feb 2031 to Feb 2036, so we used iBonds Treasury ETFs (IBTM to IBTR) for the 2033-2037 payments. Also caught that 'IBTN' in WInS is an unrelated company"); `competition/COMPETITION.md` l.113 ("IBTN on WInS is INSCORP Inc, not an iBond"); `keel/rooms/archive.md` (IBTM reflection: "a net asset value, as opposed to a promise of par")

### W-37: $3, not $5; 300 characters, not 413
- Date (Sydney): Tue 29 Sep
- Origin: CAPLET
- What happened: The first time we logged into WInS we read its own session rules instead of trusting the public guide. The minimum share price was $3, not the guide's $5, and the trade-note box held only 300 characters, shorter than the 413-character example Wharton itself had published.
- Stakes: Trade notes cannot be edited once placed and three of them would be judged; a note written to Wharton's example length would have been cut off mid-sentence.
- Decision or response: We wrote every note to fit 300 characters and treated the simulator's own rules, not the public guide, as the ones that bind.
- What changed afterwards: Every note fitted; the longest we checked ran to 288 characters.
- Vivid detail: A 300-character box, against Wharton's own 413-character example.
- Strand: learning and growth
- Evidence: `caplet/google_drive/final_report.md` l.17 ("minimum price $3 (guide says $5), and the trade note box holds 300 characters, shorter than Wharton's own 413-character example"); `competition/wins/2026-10-23_snapshot.md` l.49 ("288 chars")

### W-38: Wide spreads after hours, and an order ticket that broke
- Date (Sydney): Wed 30 Sep
- Origin: CAPLET
- What happened: When we set up the iBond orders, IBTR's order ticket returned an error and the after-hours price spreads on the iBond funds were very wide. We also learned that Treasury bond orders are entered in units of $1,000 face value, not dollars.
- Stakes: A market order into a wide spread, placed from Sydney with nobody awake at the open, could fill at a bad price on a ladder where every dollar counts.
- Decision or response: We planned limit orders and a retry in market hours rather than forcing the trade.
- What changed afterwards: Execution became part of the strategy; when the orders went in, the funds filled about $800-900 below the previous closes, which our own review put down to luck, and every bond within about 9 basis points of the curve.
- Vivid detail: Our review of the fills: "That was luck."
- Strand: response to challenges
- Evidence: `caplet/google_drive/final_report.md` l.20 ("IBTR's order ticket errored and after-hours iBond spreads were very wide, so we plan limit orders and a retry in market hours. Also learned Treasury orders are entered in $1,000-face units."); `keel/library/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md` l.277 ("below the 7 Oct closes, by about $0.8-0.9k in total. That was luck."), l.278 ("The bonds filled within about 9bp of the curve")

### W-39: Locking the core strategy
- Date (Sydney): Thu 1 Oct
- Origin: CAPLET
- What happened: Four days into the trading window, a final model check backed the two calls still open: a $150,000 Treasury floor bought with the 2028 deposit, and splitting the world fund 50/50 between the facility gift and Laura's own flexibility. We locked the IPS content and named the strategy.
- Stakes: Trade notes cannot be edited, so orders placed before the plan settled would have locked an unsettled plan into the judged record.
- Decision or response: We locked the plan and scheduled the orders for Fri 2 Oct.
- What changed afterwards: The core, payments first in Treasuries, a bought floor and one world fund, held all the way to the submitted IPS; later work added rules on top, such as moving the promised shares into Treasuries before 2031.
- Vivid detail: The 50/50 split: half the world fund for the facility gift, half kept as Laura's flexibility.
- Strand: research and decision process
- Evidence: `caplet/google_drive/final_report.md` l.21 ("1 Oct: model check backed the $150k floor and 50/50 split; IPS content locked."); `archive/rab/decisions/D7_wins_book.md` ("for the 1 Oct vote"; "10 on Fri 2 Oct"); `keel/final_report/FINAL_IPS_as_submitted.txt` ("half of the value of the shares will be promised to no one")

### W-40: The floor hiding inside the reserve
- Date (Sydney): Mon 5 Oct
- Origin: CAPLET
- What happened: Rereading our IPS draft, we realised the facility floor was being counted inside the operating reserve, so the same money was doing two jobs on paper. We fixed four phrases so the payment money and the facility money were kept apart.
- Stakes: Counting one dollar twice would have overstated what Laura could promise co-sponsors, the kind of overpromise the case warns damages credibility.
- Decision or response: We fixed the four phrases and kept one strong line on purpose: the gift never falls below the floor.
- What changed afterwards: The separation held in every later version down to the submitted IPS, where "only money you haven't promised yet goes into shares".
- Vivid detail: Four phrases changed; one, "never below the floor", kept on purpose.
- Strand: learning and growth
- Evidence: `caplet/google_drive/final_report.md` l.24 ("we realised the facility floor counted inside the operating reserve. We fixed four phrases and kept 'never below the floor' on purpose"); `keel/final_report/FINAL_IPS_as_submitted.txt` (quoted)

### W-41: "Every claim must hold on the page"
- Date (Sydney): Wed 4 Nov
- Origin: CAPLET
- What happened: Our preparation notes for the IPS kept leaning on what we would say "if a judge asks". Our team leader banned that kind of thinking: nobody gets to answer a judge before the semifinal, and the Top 50 is picked on the written work alone. The same day he banned invented terms such as "floor", telling us to use the case's own words or plain English.
- Stakes: A plan that only made sense with a spoken explanation would lose to one that made sense on paper, and coined labels make a reader learn our vocabulary before our idea.
- Decision or response: Every claim had to stand on the page alone, or be fixed or cut, and labels like "cheques" and "building gift" gave way to the case's words.
- What changed afterwards: The submitted IPS speaks the case's language (operating commitments, operating reserve, facility contribution) and uses "floor" once, in the pitch.
- Vivid detail: The instruction, 4 Nov: "do not invent terms, like floor".
- Strand: learning and growth
- Evidence: `keel/INSTRUCTIONS.md` I82 ("Nobody gets to answer a judge before the semifinal; the Top 50 is picked on the written work alone. Every claim must hold on the page, or be fixed or cut."), I83 (quoted; "no coined labels ('floor', 'building gift', 'cheques', 'promises')"); `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-42: A teammate's case for the iBond funds
- Date (Sydney): Mon 26 Oct
- Origin: CAPLET
- What happened: When our drafts kept hedging every claim about the iBond funds, a teammate wrote a long argument for why they deserve to be called near-ironclad. A normal Treasury fund never matures, so its price can be deep in the red when the cash is needed; an iBond fund's bonds all mature in one year, so its price is pulled toward its final value as that year approaches, and when the fund closes holders receive the cash inside.
- Stakes: Too many hedges make a safe plan sound unsafe; too few leave a claim a bond professional can knock down.
- Decision or response: His argument backed what our submitted notes had already said, "near-ironclad", alongside the exact caveat that the funds pay a net asset value, not a promise of par.
- What changed afterwards: Our drafts stopped hedging claims that were factually sound, while still stating exactly what each instrument pays.
- Vivid detail: His advice on our fear of sounding too sure: "Just calm down a bit, take a deep breath, and think through it properly".
- Strand: learning and growth
- Evidence: `archive/bible_2026-11-08/BIBLE.md` Book 5 (Mon 26 Oct; "the fund's price automatically locks into its final value as that year approaches ('pull-to-par')"; "the iBonds can also be described as 'near-ironclad'"; quoted line); `keel/INSTRUCTIONS.md` I48 (the books are Ahaan's); `keel/rooms/archive.md` (submitted reflections: "near-ironclad guarantee"; "a net asset value, as opposed to a promise of par"); `keel/pm/CHANGES.md` (Mon 26 Oct: "iBonds near-ironclad")

### W-43: Three pitches on the morning before
- Date (Sydney): Thu 5 Nov (document read 09:39)
- Origin: CAPLET
- What happened: On the morning of 5 Nov our IPS document held three pitches the team had written itself: a handwritten one at 50 words, our team leader's at 44 and a third at 56, over the form's 50-word limit. All three called the plan "Steady Roots", and the handwritten one introduced Laura's "human capital that fluctuates with stocks".
- Stakes: The pitch is the first 50 words a judge reads, and one word over the limit and the form would not take it.
- Decision or response: Each pitch was counted strictly and checked against the case's own words; the strongest idea, her career as a holding of shares, carried into the final pitch.
- What changed afterwards: The submitted pitch is the team's own, built on the handwritten version's idea: "Laura's career is already a giant stock she can't sell."
- Vivid detail: One pitch: 56 words for a 50-word box.
- Strand: teamwork/communication
- Evidence: `keel/ips_rewrite/caplet_doc/2026-11-05_one_check.md` l.11-13, l.40, l.52-54 ("Pitch, Handwritten | 50 / 51"; "Pitch, Ray's ... | 44 / 45"; "Pitch, Darren's ... | 56 / 57"; "All three pitches say Steady Roots"); `keel/pm/ASK_HUMANS.md` l.26; `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-44: TIPS and STRIPS banned, three weeks in
- Date (Sydney): Tue 20 Oct
- Origin: KEEL
- What happened: Wharton's public FAQ, live on 20 Oct, listed TIPS and STRIPS as not permitted, for both the IPS and the Final Report, and the $5 minimum share price vanished from the public page. Because we had already moved off STRIPS after the 6 Oct email, nothing in the plan had to change.
- Stakes: Inflation-protected and zero-coupon Treasuries are the textbook tools for fixed future payments; a plan relying on them would have had to be rebuilt with two weeks to go.
- Decision or response: We checked every holding and every draft against the new list and kept every recommendation inside it.
- What changed afterwards: The rule confirmed our basis: the submitted IPS uses only Treasury bonds, iBond Treasury funds and one world fund.
- Vivid detail: The two instruments built for exactly this kind of promise, ruled out three weeks into trading.
- Strand: response to challenges
- Evidence: CLAUDE.md ("Public SMApply FAQ, live 20 Oct: TIPS and STRIPS are now listed as NOT permitted, the permitted list is 'for BOTH contributions, the IPS and Final Report', and the public $5 stock floor is gone"); `competition/COMPETITION.md` s4; `competition/official/2026_27/smapply_public_2026-10-20/`; `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-45: The IPS becomes a form
- Date (Sydney): Thu 22 Oct
- Origin: CAPLET
- What happened: Wharton's week 4 email turned the IPS from a document into an online form: a 50-word pitch and 500 words, with no title page, charts, links or citations. Our drafts had been carrying a dozen or so figures.
- Stakes: With two weeks to go, everything a chart or table had shown at a glance had to be carried by sentences inside 500 words.
- Decision or response: We moved the numbers and models toward the Final Report and kept the IPS to the strategy: what we do, and why.
- What changed afterwards: The submitted IPS carries almost no figures; a teammate later put the rule plainly: models and evidence belong in the Final Report, the IPS explains the strategy.
- Vivid detail: 50 words for the pitch, 500 for the strategy, no charts, no links.
- Strand: response to challenges
- Evidence: `competition/official/2026_27/wharton_email_week4_2026-10.md`; CLAUDE.md ("IPS is now an SMApply FORM, not a PDF"; 16 Oct pre-mortem: "the live V5 ... added ~a dozen figures"); `keel/INSTRUCTIONS.md` I73 (Book 11: "Models, citations, evidence for the Final Report"); `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-46: Trading Notes Analysis submitted
- Date (Sydney): Fri 23 Oct (marked submitted 23:52)
- Origin: CAPLET
- What happened: We submitted our first judged deliverable: three trade notes quoted exactly from executed WInS trades, each with a reflection of 100 words or fewer. We chose a long Treasury bond (February 2037), the iBond fund IBTM and the world fund VT. That day WInS valued the portfolio at $305,557.66, up 1.85%.
- Stakes: The notes are judged with the IPS and the Final Report to pick the Top 50, and they cannot be changed once submitted.
- Decision or response: A final check matched each note exactly to its filled WInS order before the team submitted.
- What changed afterwards: The reflections became fixed points every later draft had to agree with; where a later text described the method differently, the later text had to bend.
- Vivid detail: WInS value on the day: $305,557.66 (+1.85%).
- Strand: research and decision process
- Evidence: commit 44bf900 (Fri 23 Oct 23:52 Sydney) "Mark the TNA submitted (T01 done, 23 Oct)"; `keel/office/LEDGER.md` WO-0007 ("Notes 1-3 (Feb-2037 12:24 AM, IBTM, VT) match filled orders exactly"); `keel/rooms/archive.md` (submitted text); `competition/wins/2026-10-23_snapshot.md`; `keel/pm/ASK_HUMANS.md` l.28 (4 Nov, the "duration-matching" case)

### W-47: The simulator called our bonds "Long Equities"
- Date (Sydney): Fri 23 Oct
- Origin: KEEL
- What happened: Reading the WInS snapshot on submission day, we found that the simulator's pie chart labelled our iBond Treasury funds "Long Equities", showing 61.6% of the portfolio in shares when the true mix was about 91% Treasuries. Two WInS screens also disagreed about the account's value by $1,310.
- Stakes: A judge glancing at the chart could conclude that a Treasury plan was mostly shares.
- Decision or response: We worked out the true mix from the holdings themselves, traced the $1,310 gap (accrued interest and cash explain the headline value), and chose to quote the portfolio value and return rather than the conflicting positions line.
- What changed afterwards: The mislabel became a point the Final Report has to explain, and the figure we quote for 23 Oct is the portfolio value, $305,557.66.
- Vivid detail: "Long Equities: 61.6%", for a portfolio about 91% in Treasuries.
- Strand: research and decision process
- Evidence: `competition/COMPETITION.md` l.117 ("The WInS pie chart labels the iBond ETFs 'Long Equities' (61.6%). The true mix is about 91% Treasuries."); `competition/wins/2026-10-23_snapshot.md` l.63-65 ("WInS's own figures disagree by $1,310"; "Portfolio value ($305,557.66) = cash + positions ($300,757.88) + accrued interest"; "Quote portfolio value and return, not the long-positions line"); `competition/COMPETITION.md` l.117-118 ("Explain this in the Final Report.")

### W-48: A wrong coupon in our own records
- Date (Sydney): Wed 21 Oct, 16:11
- Origin: KEEL
- What happened: Two days before the trade notes were due, a check against the WInS security code found that our own master file gave the February 2037 bond's coupon as 5.000%. The bond we owned paid 4.750%, and its note was one of the three we planned to submit.
- Stakes: A wrong coupon in a submitted reflection would have been a factual error about our own holding, in front of judges, in a text that cannot be edited.
- Decision or response: We fixed the record from the primary source, the security code shown in WInS.
- What changed afterwards: The submitted note on the February 2037 bond was checked against its filled order and matched exactly.
- Vivid detail: 5.000% in our file; 4.750% on the bond.
- Strand: research and decision process
- Evidence: commit 78fc1df (Wed 21 Oct 16:11 Sydney) "Fix Feb-2037 bond coupon in COMPETITION.md (4.750%, per WInS security code); log WO-0004 TNA final check"; `keel/library/assistant_review_2026-10/01_Caplet_Team_Brief_15Oct2026.md` l.287 ("WInS shows B-T-4.750-15022037 ... competition/COMPETITION.md:181 says 5.000%"); `keel/office/LEDGER.md` WO-0007

### W-49: Thirty-six rival plans
- Date (Sydney): Tue 27 Oct (night) to Wed 28 Oct
- Origin: KEEL
- What happened: To see what we were up against, we mapped 36 simulated rival IPSs, twelve of them generated straight from the case with no research behind them. All twelve of those reached the same answer, "ladder first, then stocks", and nine of twelve rival plans already locked shares into Treasuries around 2031. None of the 36 used Laura's career as a reason, or set her 2031 range by the cost of missing each end.
- Stakes: If our plan was the obvious answer, judges would read it many times over; what set us apart had to be found and put at the centre.
- Decision or response: We kept the ladder and the 2031 lock, which were common, and led with what no rival had: the career reason and the two-cost range.
- What changed afterwards: Laura's career as an unsellable holding of shares moved toward the centre of the argument, where the team's own IPS finally put it.
- Vivid detail: 0 of 36 rival plans used Laura's career as a reason.
- Strand: research and decision process
- Evidence: `keel/pm/CHANGES.md` l.47 (Tue 27 Oct night: "36 simulated rival IPSs mapped (all 12 raw-AI rivals reach 'ladder first, then stocks'; 0 of 36 have human capital or a two-cost range)"), l.44 (Wed 28 Oct: "9 of 12 rival plans already lock stocks into Treasuries around 2031 ... Human capital and the two-cost range kept (no rival has them)"); `keel/final_report/FINAL_IPS_as_submitted.txt`

### W-50: "i want more COMPUTER MODELS"
- Date (Sydney): Tue 27 Oct (22:20)
- Origin: KEEL
- What happened: Our team leader asked for more computer models. Until then we had tested the plan in one simulated world, with bell-curve share returns and random-walk yields, and against no rival plans. That night we built four worlds, including fat-tailed market regimes and every month of US history since 1871, and five rival plans: ours broke a payment promise in 0-1.6% of worlds against 22-36% for the rivals.
- Stakes: A plan tested only in a gentle model could fail in the crashes real history contains.
- Decision or response: Every assumption was logged and each finding reduced to one plain number.
- What changed afterwards: The history run produced the fact that frames the plan's timing: since 1871 $300,000 would have bought all ten payments in only about one month in four, and in none from mid-2007 until this year.
- Vivid detail: The request, word for word: "i want more COMPUTER MODELS".
- Strand: research and decision process
- Evidence: `keel/INSTRUCTIONS.md` I52 ("i want more COMPUTER MODELS"; "The lab ran one world (bell-curve stocks, random-walk yields) and no rival plans"); `keel/pm/RUNLOG.md` l.112 (Tue 27 Oct 22:20: "four worlds, five rival plans, 7 charts; the champion breaks a promise in 0-1.6% of worlds vs 22-36% for rival plans; new fact: $300k buys the ten cheques in 1 month in 4 since 1871, none from mid-2007 to now")

### W-51: The interest that has to be reinvested
- Date (Sydney): Mon 9 Nov, 07:00
- Origin: KEEL
- What happened: The ten Treasuries reach $50,000 each only if the interest they pay along the way is reinvested at future rates nobody knows today. Testing the ladder as written against every 16-year stretch of US rates since 1962, we found it fell short somewhere in 55.6% of them: usually by a little (median $1,592), but by $34,555 one time in 20 and by $45,266 in the worst case, the stretch starting July 2007.
- Stakes: The case asks for the payments with a high degree of certainty; a gap that appears in more than half of historical periods cannot go unsaid in the Final Report.
- Decision or response: We decided the 2028 deposit's first dollars complete the ladder with a margin of $21,149, enough to pay all ten in 94% of historical stretches, at a cost of about $20,000 off the bottom of the 2031 range.
- What changed afterwards: Our notes stopped claiming that the shares cover this gap; the margin follows the IPS's own promise to complete the ladder from the 2028 deposit.
- Vivid detail: Worst case: $45,266 short, for the sixteen years starting July 2007.
- Strand: response to challenges
- Evidence: `keel/final_report/NUMBERS.md` l.81 ("$302,287 | ... | 55.6% | $1,592 / $34,555 / $45,266 (start Jul 2007)"); `keel/pm/ASK_HUMANS.md` l.18 (Mon 9 Nov 07:00: "Margin $21,149 ... all ten paid in 94% of historical stretches, worst $12,117 short of $500,000. It costs about $20,000 off the bottom of the range"); `keel/pm/CHANGES.md` (Sun 8 Nov: "the reinvestment risk is no longer said to be covered from the shares")

### W-52: "The world fund makes the gift bigger": a claim we killed
- Date (Sydney): Mon 9 Nov
- Origin: KEEL
- What happened: We compared the top of the facility range in our plan with a plan that put everything in Treasuries. The top of our range was below the all-Treasury benchmark in 98% of modelled paths, because half of the world fund is held back on purpose as Laura's flexibility.
- Stakes: Telling judges the share fund makes the gift bigger, when our own model says the opposite, would be an overclaim at the heart of the Final Report.
- Decision or response: We dropped the claim and restated what the world fund buys: a share of world growth for the top of the range and for the half Laura keeps, at the cost of a lower certain bottom.
- What changed afterwards: The case for shares in the Final Report rests on flexibility for Laura, not on a bigger gift.
- Vivid detail: 98%: how often the all-Treasury plan beat the top of our range.
- Strand: research and decision process
- Evidence: `keel/final_report/NUMBERS.md` l.168-170 ("The FINAL's gift top is below that benchmark in 98% of house paths. Half of VT is held back from the gift on purpose, as flexibility"; "What VT adds is a share of world growth for the top and for the kept half, at the cost of a lower certain bottom"); `keel/final_report/ARGUMENT_LOG.md` (Mon 9 Nov, killed: "VT makes the gift bigger")

### W-53: One cost, four engines, four answers
- Date (Sydney): Sun 8 Nov to Mon 9 Nov
- Origin: KEEL
- What happened: Looking back over the IPS work, we found the same cost had come out at $4,000, $9,000, $15,000 and $19,000 on four different models. Each was right on its own assumptions, but nobody on the team could tell which one to trust.
- Stakes: A Final Report quoting figures from different engines would contradict itself, and the six of us could not defend numbers we could not trace.
- Decision or response: We built one number register on one dated curve with one engine behind it, and every figure in the Final Report must come from it.
- What changed afterwards: Each figure now carries its date, its source and the script that made it, including the plan's own headline numbers such as $301,544 at the 6 Nov close.
- Vivid detail: $4,000, $9,000, $15,000 and $19,000: one cost, four engines.
- Strand: learning and growth
- Evidence: students' timeline `keel/library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/01_experience_with_caplet_edits.txt` l.38 ("The same cost came out at $4,000, $9,000, $15,000 and $19,000 on four different engines. The Final Report must use one engine on one dated curve."); `keel/final_report/NUMBERS.md` (9 Nov; engine `keel/final_report/numbers/`); CLAUDE.md ("Every figure comes from the number register")

### W-54: No Final Report prose until 27 November
- Date (Sydney): Sun 8 Nov, 11:06 to 11:26
- Origin: CAPLET
- What happened: With the IPS in, the team set the plan for the Final Report: no prose at all until Fri 27 Nov. Until then, deep research and thinking on every part of the case, not only the investing, and one ranked store of every insight so nothing found is lost; then a single 24-hour writing session with at least twelve rounds of drafting, review and rewriting, and a final draft to the team on Sat 28 Nov.
- Stakes: The IPS had shown what happens when writing starts before thinking ends: dozens of versions polishing words, not the plan.
- Decision or response: Research first, writing last, all of it measured against Wharton's own criteria.
- What changed afterwards: The Final Report work runs from a schedule, a daily test against Wharton's criteria and a ranked insight store, not from drafts.
- Vivid detail: At least twelve draft-review-rewrite rounds in one 24-hour session, starting Fri 27 Nov.
- Strand: learning and growth
- Evidence: `archive/bible_2026-11-08/BIBLE.md` l.730 (Book 13, Sun 8 Nov 11:06), l.755 (Book 14, 11:21: "No writing until the day before; notes on every expectation; one ranked store of every insight"), l.778 (Book 15, 11:26); `keel/INSTRUCTIONS.md` I89-I91; `keel/final_report/README.md`; CLAUDE.md ("Fri 27 Nov: one 24-hour session, at least twelve draft-review-rewrite rounds ... final draft to Caplet Sat 28 Nov")

### W-55: "Judges are shark tanks"
- Date (Sydney): Tue 27 Oct
- Origin: CAPLET
- What happened: Our team leader told us our writing was "just telling facts ... like eating plastic", and that "judges are not examiners ... judges are shark tanks". He asked us to read widely, from great essays to investor theses and bank research, "to practice writing, not start writing", and for three days no IPS prose was written at all.
- Stakes: A strategy argued like an exam answer could tick every box and still fail to win a reader's conviction.
- Decision or response: We paused drafting, studied how strong writers argue, and aimed for an investor's conviction: a hook, real stakes, a reason to care about Laura's residency, and confidence.
- What changed afterwards: Persuasion, not just correctness, became part of how we judged a draft.
- Vivid detail: His verdict on our prose: "like eating plastic".
- Strand: learning and growth
- Evidence: `keel/INSTRUCTIONS.md` I47 ("is just telling facts ... like eating plastic"; "to practice writing, not start writing"), I50 ("you gotta have emotional appeal man. Judges are not examiners ... judges are shark tanks"; "a hook, real stakes, a reason to care about Laura's residency, and confidence in us"); `keel/pm/ASK_HUMANS.md` l.61 (Tue 27 Oct: Ray: "stop writing for now"; "Paused 27-29 Oct")
