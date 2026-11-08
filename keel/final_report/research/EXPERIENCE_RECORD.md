# What Caplet actually did: the record behind "Articulation of Competition Experience"

Started Mon 9 Nov 2026 (Sydney); section 5 holds the blind ranking of the whole pool. Notes, not report text. This is the material for the experience section: real,
dated events of Caplet's competition, each with its source. The section is built from these and told vividly; a
scenario that helps the argument is told as an illustration ("suppose ...", "imagine ..."), never as something that
happened. Since I102 (Mon 9 Nov) the pool also holds Keel's real work events, and the whole pool is judged blind of
which team produced each event (`experience/`); the invented people and scenes in Keel's diary are not events and are
not used.

The spine is Caplet's own timeline in the Final Report doc's Experience tab, as Caplet edited it
(`keel/library/research_tabs_2026-11-07/doc_snapshot_2026-11-08/01_experience_with_caplet_edits.txt`, "the tab" below).

## 1. The timeline (Sydney dates)

| Date | What happened | What it shows (decision, cause, cost) | Source |
|---|---|---|---|
| 2025-26 | Last year's team traded assets outside the trading rules, packaged a strategy more complex than its insight, and heard nothing back | Why this year's rules: check every trade against this year's list; complexity must earn its place; client first | CLAUDE.md "Team" (Ray) |
| Sun 27 Sep | First model of the original plan (about three-quarters shares) missed a payment in 3.2% of paths, 13.7% if the 2028 deposit came in at $75,000 and 40.8% if it never came. Buying the payments first never missed one | The team dropped its own first plan on evidence | the tab; `keel/library/verified_2026-09-27/strategy_mc.py` |
| Mon 28 Sep | Trading opened; the new plan was chosen: the first deposit buys the ten payments, the second buys a Treasury floor plus one world share fund | Better outcomes in bad years outweighed a higher median | the tab |
| Tue 29 Sep | WInS listed no Treasury bond maturing between Feb 2031 and Feb 2036, so the team used iShares iBonds Term Treasury ETFs (IBTM-IBTR) for the 2033-2037 payments | A constraint turned into a design choice | the tab |
| 29-30 Sep | Two WInS bond prices were stale, about one percentage point of yield off the Treasury curve. New rule: check every bond's yield against the curve, within 0.25 points, before ordering | Caught before any money moved | the tab; `competition/COMPETITION.md` |
| Wed 30 Sep | After-hours iBond spreads were wide, so the team planned limit orders and trades in market hours | Execution as part of the strategy | the tab |
| Thu 1 Oct | Core strategy locked | | the tab |
| Mon 5 Oct | Darren argued the world fund was a "copout" and proposed picking stocks and ETFs; a Taiwan fund (EWT) and gold (GLD) were raised. The team kept the one world fund (VT) | A real disagreement, settled on reasons | the tab |
| Tue 6 Oct | Wharton's email: Laura's real plan may use only WInS-listed stocks, ETFs and Treasury bonds. Earlier numbers built on STRIPS were dropped; the building floor became IBTM | Adapting to a rule change mid-competition | CLAUDE.md; `competition/official/2026_27/` |
| Wed 7 Oct | A mis-click led to the rule that only Ray places or cancels orders. Market open was 00:30 Sydney time; Eric fell asleep before it | Trading from Sydney; a control born from an error | the tab; CLAUDE.md |
| 7-8 Oct | All eleven orders filled: five iBond ETFs, five Treasury bonds and VT (167 shares). 11 of 200 trades used; cash $3,514 | The plan, executed | the tab; `competition/wins/2026-10-23_snapshot.md` |
| Fri 16 Oct | Rates fell and the ladder's room under $300,000 shrank to about $1,900 | Why the IPS says the 2028 deposit completes the ladder if yields fall | the tab; CLAUDE.md |
| Tue 20 Oct | Wharton's public FAQ listed TIPS and STRIPS as not permitted, for both contributions | Rules confirmed the WInS-only basis | `competition/COMPETITION.md` section 4 |
| Thu 22 Oct | Wharton's week 4 email: the IPS became an online form (a 50-word pitch and 500 words, no charts or links) | Every chart and table had to become sentences | `competition/official/2026_27/wharton_email_week4_2026-10.md` |
| Fri 23 Oct (ET) | Trading Notes Analysis submitted: three notes quoted from executed trades, each with a reflection of 100 words or fewer. WInS value that day $305,557.66 (+1.85%) | The first judged deliverable | `keel/pm/ASK_HUMANS.md` (24 Oct); the WInS snapshot |
| 26 Oct-6 Nov | The IPS was rewritten from scratch many times | What a rewrite fixes and what it cannot | `keel/INSTRUCTIONS.md` I41-I92 |
| Fri 6-Sat 7 Nov | The team set every earlier draft aside and wrote its own IPS as a letter to Laura, in plain sentences, with one investing idea at its centre (her career behaves like shares she can't sell). It was in before 09:00 Sat Sydney, when trading froze and the portfolio locked | The plan stayed; the explanation was rebuilt | `keel/final_report/FINAL_IPS_as_submitted.txt`; `keel/INSTRUCTIONS.md` I92 |
| 6 Nov close | The ten Treasuries would cost $301,544 on 1 Jan 2027, just over the $300,000 deposit | The IPS's completion rule is needed, not hypothetical | `keel/final_report/NUMBERS.md` section 1 |

## 2. The five strongest moments, and what makes each vivid

1. **The model that killed the team's own plan (27 Sep).** The numbers are the drama: 3.2%, then 40.8% if Laura's
   2028 money never came. The team changed course on day one of trading. Growth: evidence over attachment.
2. **00:30 in Sydney (7 Oct).** The US market opened after midnight; one teammate fell asleep before it; a mis-click
   ended with one person placing every order. Concrete, human, and it shows a control coming from a mistake.
3. **Darren's "copout" (5 Oct).** A teammate attacked the plan's simplest part; Taiwan and gold were on the table;
   the team kept one world fund and can say why. Shows disagreement handled on reasons.
4. **The stale prices (29-30 Sep).** Two bond prices a full point of yield off the curve, caught before any order,
   and a rule written the same day. Shows checking.
5. **The night of 6 Nov.** Weeks of rewrites, then the team wrote its own IPS as a letter to Laura and sent it
   before the morning deadline. The plan held from late September; only the way of saying it changed.

Also usable: the $1,900 margin on 16 Oct (the plan's tightest point, and the reason for the completion rule); the
mid-competition rule changes (6 Oct, 20 Oct, 22 Oct) and how each was absorbed; last year's lesson as the opening of
the team's growth story.

## 3. Illustrations the report may use (told as illustrations)

- Suppose Laura's 2028 deposit came in at half, or not at all: what the plan does (NUMBERS.md section 5).
- Imagine yields fall two points before January 2027: the ten would cost $369,710 and the 2028 deposit completes
  them (NUMBERS.md section 1).
- Picture a co-sponsor meeting in 2031: what Laura can promise and why (NUMBERS.md section 4).

## 4. What the record does not hold

Feelings, who said what in meetings beyond the tab, and moments after 7 Nov. If Caplet adds any, they go straight
into the table above with the date.

## 5. The blind ranking (Mon 9 Nov, Caplet's order I102)

**How.** Two researchers gathered every real event of the competition that the files confirm: 40 from Caplet's own
record and 63 from Keel's work (`experience/candidates_W.md`, `candidates_K.md`; each with its evidence). The pool was
stripped of who produced each event, given random ids and shuffled (`experience/blind.py`, `BLIND_POOL.md`). Three
independent readers who saw nothing else scored all 103 on Wharton's Articulation wording, vividness, credibility and
the link to the strategy (`judge_1-3.md` and `.csv`: a Wharton finance professor, a reader of student essays, a
fixed-income portfolio manager). Origins were revealed only after (`experience/aggregate.py`, `RANKING.md`). The best
events split evenly: Caplet 6 and Keel 4 in the top 10, 15 each in the top 30.

**The top 15** (mean of three readers, out of 40; all three put the first nine in their own top 15):

| Rank | Event | Score | Origin |
|---|---|---|---|
| 1 | The model that sank our own first plan (27 Sep) | 34.0 | Caplet |
| 2 | Our own trade note's warning came true (7 Oct note; the completion rule) | 32.3 | Keel |
| 3 | Last year's lessons (FMC down 54%, trades outside the rules, no feedback; three rules for this year) | 32.0 | Caplet |
| 4 | A bond fund never matures (why one dated holding per payment) | 31.0 | Keel |
| 5 | No bond for the missing years, and a ticker that was not ours (IBTN was INSCORP Inc.) | 31.0 | Caplet |
| 6 | The "copout" objection, settled by a test written before the numbers (5 Oct) | 31.0 | Caplet |
| 7 | Laura's career is a stock she cannot sell: six weeks to find the words | 30.7 | Caplet |
| 8 | The cheapest the payments had been in years (28 Sep) | 30.3 | Keel |
| 9 | A former Wharton judge says the IPS cannot make it ("Laura is barely in it") | 30.0 | Caplet |
| 10 | The night the ladder crossed $300,000 | 30.0 | Keel |
| 11 | Her career is a share she can't sell: the idea that survived from the first day | 30.0 | Caplet |
| 12 | We set the drafts aside and wrote our own IPS as a letter | 30.0 | Caplet |
| 13 | $300,000 could buy the ten payments in only about one month in four since 1871 | 29.7 | Keel |
| 14 | From $1,913 of room to $1,544 over the line | 29.3 | Keel |
| 15 | Wharton's 6 Oct email takes away our floor | 29.0 | Caplet |

**The arc all three readers built** (each proposed one; they share five steps): last year's lessons -> the model that
sank our own plan -> learning how Treasuries really behave (no bond for the missing years; a bond fund never matures)
-> the "copout" objection -> the trade note's warning came true -> a former judge: "Laura is barely in it" -> our own
IPS as a letter -> the central idea tested honestly after submission (2009 supports it, 2020 does not). It runs from a
team that lost last year, through decisions made on evidence, to a team that found its client and its own voice.

**What the readers said to leave out**, with their reasons: a thousand essays read in one night (no reader believes
students did it, and it makes the true events look doubtful); drafts scored by machine judges and an office that
ignored the team's messages (reads as a team that did not own its work); the team leader handing decisions to someone
else (Wharton says the decisions are the students'); thirteen edits rejected on deadline night (points the judges at a
weak line in a reflection they already hold).

**Numbers to reconcile before any event is told.** Event cards quote the record as it stood that day; the report uses
NUMBERS.md only. (a) "Only 12 of 185 days" came from an earlier ladder model: the register says 37 of 214 closes
(section 8b). (b) "$302,863 on 22 Oct" and "crossed $300,000 for the first time" came from an older calculation: on
the register's engine the ten cost $298,861 on 22 Oct and first went back over $300,000 on 2 Nov ($300,233), $301,544
at the freeze; the 10-year yield on 22 Oct was 0.31 points below 6 Oct, as the card says. (c) "Cheapest since May
2002" and "one month in four since 1871" are not yet in the register; re-derive them on this engine before use.
(d) The 7 Oct mis-click is told as Caplet's own tab tells it ("a mis-click incident led to the rule that only Ray
places or cancels orders").
