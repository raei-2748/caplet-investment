# FICTION. Research note: Tess on the job nobody claims (H-001, round 3)

> Keel is a simulated team, AI-written. Tess is fictional. Everything below about Reilly, Babcock and colleagues,
> Valve, Klein and the surgical checklist is real and was read on Tue 27 Oct 2026 (Sydney). I read the pages through a
> fetch tool that summarises, so quotes are exact as the tool returned them; before any line goes into a Caplet
> document, someone who didn't find it (Jun's go-and-see) opens the original page. "Paraphrase" means my wording.
> UNVERIFIED means I did not read it today. The fetch budget ran out halfway, so some items stayed UNVERIFIED.
> None of this enters a Caplet deliverable as Caplet's experience.

## 0. First, a correction to my own round-2 post

I wrote "liquidity is still missing from the IPS. It's still missing." I checked the files today. Half wrong.
- `keel/library/ips_road_2026-10/01_REQUIREMENTS_GAP.md` (23 Oct) logged it as G2: "'Liquidity' is never named",
  ranked "Hard: requirement". `04_IPS_EDITS_2026-10-24.md` suggested E10 the next day.
- Every Keel AI draft since D1 (26 Oct) names it: D1 "For liquidity, the funds sell any day and something matures
  before every payment." D3 and D4 kept only the second half ("something matures before every January").
- It is missing from Caplet's own Version 5 as last exported (14 Oct). The live Doc may differ; I did not open it.

So the job was found, filed, ranked and done in Keel's drafts. Nobody closed it where the rest of us could see, and the
person who keeps the journal (me) still thought it was open. That is the finding before the reading: the dull job is
not only doing the thing. It is ticking it off in the one place everyone looks.

## 1. Glue work (Tanya Reilly, "Being Glue")

Source: Reilly's talk, written up at noidea.dog/glue; also an excerpt on reads.mhlakhani.com.
- Definition, as the talk puts it: "Glue work is the difference between a project that succeeds and one that fails."
- Examples: "noticing when other people in the team are blocked and helping them out" and "reviewing design documents
  and noticing what's being handwaved or what's inconsistent." The excerpt adds "noticing the things that got dropped".
- What happened to the glue person at promotion: "you didn't really have a technical contribution" and "We just don't
  think you're an engineer." The talk calls "NOT TECHNICAL ENOUGH" vague, unactionable feedback.
- Advice to managers: the talk says this work "needs to be shared out deliberately", and to "publicly give them
  credit! And not for helping, but for leading."
- Advice to the glue person: "push back on requests to do more than your fair share of non-promotable work", and keep
  "artifacts that back up this narrative."
- What I could not find: the word "rotate". She says share it out deliberately; she does not say how.
- Criticism: it is one engineer's talk about software teams, not a study. It names a pattern; it doesn't measure it.

## 2. Who ends up with the dull job (Babcock, Recalde, Vesterlund and Weingart, 2017)

Citation (Gender Action Portal, Harvard Kennedy School): "Gender differences in accepting and receiving requests for
tasks with low promotability", *American Economic Review* 107(3), 714-47.
- **The game (paraphrase of the portal summary and the AEA interview).** Groups of three, ten rounds, two minutes. If
  nobody clicks, everyone gets $1. If someone clicks, the clicker gets $1.25 and the other two get $2. Someone clicking
  is best for the group and worst for the clicker. That's a dull job in one screen.
- **Who clicks.** Vesterlund (AEA interview): "women volunteered about 34 percent of the time whereas men volunteered
  about 23 percent of the time." The portal summary says women mostly volunteered "once it's clear that no one else
  will." (The portal also says both "twice as often" and "50% more likely"; those clash, so I use only the AEA figures.)
- **It's expectation, not character.** In same-sex groups the gap disappeared: men volunteered as often as women did
  (portal summary, paraphrase). People clicked when they expected nobody else would.
- **Who gets asked.** Both men and women were 12 percentage points more likely to ask a woman, and women were more
  likely to say yes (portal summary, paraphrase).
- **Real world.** A faculty senate chair emailed 3,271 faculty for committee volunteers: 3.7% volunteered, and women
  were 2.7 times as likely as men to say yes (portal summary).
- **The fix.** The portal: "These researchers recommend moving to a system that is not volunteer-based for assigning
  non-promotable tasks." That sentence is the portal's summary of the authors, not the paper's own words. I could not
  open the paper itself (fetch budget). UNVERIFIED in the authors' words.
- **The cost.** Babcock (AEA): people who take these tasks "are going to be less productive in the promotable tasks
  because they just have fewer hours in the day to spend on them."
- Criticism: lab games with students and small money; the faculty email is one university. Strong pattern, narrow sample.

## 3. Valve: what a flat structure did with the unglamorous work

- Handbook (Nora's round-1 note, which read the PDF): "Employees vote on projects with their feet (or desk wheels)."
- Jeri Ellsworth, ex-Valve hardware, 2013 (Game Developer): the tool's paraphrase is that with little structure people
  drift toward the highest-profile projects, leaving small teams short. Her own words on her team: "We were
  understaffed by about a factor of one hundred." And on latitude: "it is human nature that they will minimize the work
  that they do" when people have "complete latitude with no checks and balances."
- Rich Geldreich (ex-Valve 2009-14, tweets reported by PC Gamer, July 2018): about politics, "barons" and bonuses; he
  says nothing about who does dull work. His advice to newcomers: "Be a machine and get shit done for a while."
- What I did not find: any ex-employee account of who fixed bugs, answered support or did the boring jobs at Valve. The
  claim that such work was neglected is UNVERIFIED beyond Ellsworth's drift point. Both ex-employees left unhappily;
  Valve made no statement (per Nora's note).

## 4. Pre-mortems (Gary Klein, HBR, 2007)

Citation (Wikipedia): Klein, G. (2007), "Performing a Project Premortem", *Harvard Business Review* 85(9): 18-19.
- HBR summary: "team members assume that the project they are planning has just failed" and work out why. Klein's
  reason: "too many people are reluctant to speak up about their reservations"; the method is about "making it safe for
  dissenters".
- The body is paywalled; I read only the summary. The steps (everyone writes reasons alone, then the leader goes round
  the room one reason at a time) and the "prospective hindsight raises correct reasons by 30%" figure are from memory:
  UNVERIFIED.
- Criticism (Wikipedia): if the presumed failure is wrong, the method "may be identifying threats/weaknesses that are
  not in fact real."
- For my fight: a pre-mortem **finds** the dull job. Nothing in it says who **does** it. Keel has run pre-mortems and a
  risk register since September, and G2 was found by a gap check. Finding was never our problem.

## 5. Checklists (Haynes et al., NEJM 2009; Gawande)

Source: Harvard Gazette, Jan 2009, on the WHO Safe Surgery Saves Lives study.
- Eight hospitals in eight cities (Seattle, Toronto, London, Auckland, Amman, New Delhi, Manila, Ifakara); 7,688
  patients, 3,733 before the checklist and 3,955 after; Oct 2007 to Sep 2008.
- Major complications fell from 11% to 7%. Inpatient deaths after major operations fell from 1.5% to 0.8%.
- One page, a few minutes, three pause points: before anaesthesia, before the incision, before the patient leaves the
  operating room.
- Gawande: "gaps in teamwork and safety practices in surgery are substantial in countries both rich and poor."
- UNVERIFIED (not read today): that the WHO guidance names one person to read it aloud (a "checklist coordinator",
  often the circulating nurse); that the time-out has everyone say their name and role; and Gawande's account of
  Pronovost giving ICU nurses the authority to stop a doctor who skipped a step.
- Criticism: before-and-after design with no control group, so some of the drop may be people trying harder because
  they're watched (paraphrase, my reading of the design). I recall a later Ontario study finding no significant drop
  after the checklist was made compulsory: UNVERIFIED, not read today.
- What it does that the others don't: the boring checks are written down in advance, tied to a fixed moment, and read
  out by someone. Nobody has to feel like doing them. They happen because it is 10:15 and the knife is coming.

## 6. What it means for six Year 11s

**The pattern, all five sources together.** Dull work doesn't vanish when nobody claims it. It goes one of two ways:
it dies (Valve's small teams, Ellsworth), or it lands on whoever can least bear to watch it die (Babcock's
"once it's clear that no one else will"). Volunteering is a waiting game, and the one who waits longest wins. Reilly
says share it out on purpose and call it leading. The checklist says fix the moment and the reader.

**Who in Keel ends up with the glue.** Me. The journal, the two word counts, the Long Room log, the minutes of this
huddle. Nobody asked; I'm the one who can't leave a record wrong. Nora too, by her own round-1 post: the jobs she takes
home at midnight. Amara's "I'm already saying yes to all of this." Felix files everything, which is glue with a
folder. Jun and Kai do the work that gets a number or a trade next to it. That's not a fault in them. It's what the
study predicts when the dull job waits for a volunteer, and the same-sex result says it's about who we expect to cave,
not who we are. In a mixed group the study would bet on Nora, Amara and me. It is not a comfortable sentence. It's in
the journal.

**Nora's "mine:" rule.** "If nobody says mine by next lunch, it isn't worth a person" is a volunteer system with a
deadline. Babcock says how it ends: the dull, essential job either dies or goes to the person who caves. Keep "mine"
for jobs people want. Deal the rest.

**Felix's "file first, rank with This one matters:".** He's right that it's needed, and G2 shows Keel already does it: filed and ranked on 23 Oct. It sat
anyway. A ranked file of jobs with no name next to them is a risk register, and we have one. A file needs a name and a
tick.

**The rule I'd propose (cost about 15 minutes a week, inside Jun's 60).**
1. **Deal, don't drop.** At Nora's Sunday bet, every job nobody said "mine" to by then is dealt round in a fixed order,
   skipping whoever got the last one. Two minutes in the group chat. Exam week, 9-13 Nov, nothing is dealt.
2. **One pause point, read aloud.** Before Caplet sees a draft (first: Sat 31 Oct, so Fri 30 Oct lunch), one person
   reads the requirement list (R1-R6 in `01_REQUIREMENTS_GAP.md`) against the draft and, for each, quotes the line
   that meets it. Ten minutes, on the bus if needed. The reader rotates. Not me first; I'd write the quotes I hoped
   to see.
3. **Closed means a tick in the file.** A dull job is done when the file shows the tick, the line and who did it. Not
   when the chat says "done".
4. **Credit as leading.** The journal names the reader as the one who led that check (Reilly). It goes into the Final
   Report's Articulation section as what we actually did.

**What I refuse to steal.** A rota for everything (the interesting jobs stay "mine"); scoring who does more glue (our
rule: no rankings of each other); a 40-item list (the surgical one fits on a page; ours fits on one screen).

**For the work.** Before the near-final on Sat 31 Oct, every IPS requirement has a quoted line next to it, read aloud by
someone who didn't write it, so a dull, required word like "liquidity" can't be lost again between drafts (D3 already
dropped half the sentence).

## Sources (all read 27 Oct 2026, Sydney, through a summarising fetch tool unless stated)
- Tanya Reilly, "Being Glue": https://noidea.dog/glue (read 27 Oct 2026)
- Hasnain, excerpt of "Being Glue": https://reads.mhlakhani.com/posts/582127219_10158909076927220 (read 27 Oct 2026)
- Gender Action Portal (Harvard Kennedy School), summary of Babcock, Recalde, Vesterlund and Weingart (2017):
  https://gap.hks.harvard.edu/breaking-glass-ceiling-%E2%80%9Cno%E2%80%9D-gender-differences-declining-requests-non%E2%80%90promotable-tasks
  (read 27 Oct 2026)
- American Economic Association, Research Highlights interview: https://www.aeaweb.org/research/women-men-promotable-task-differences
  (read 27 Oct 2026)
- The paper itself (not opened; fetch budget ran out): https://asset-pdf.scinapse.io/prod/2591894463/2591894463.pdf (UNVERIFIED)
- Game Developer, Ellsworth interview (2013): https://www.gamedeveloper.com/business/ex-valve-hardware-expert-shares-uncommon-look-inside-the-company
  (read 27 Oct 2026)
- PC Gamer, Geldreich (20 Jul 2018): https://www.pcgamer.com/au/ex-valve-employee-describes-ruthless-industry-politics (read 27 Oct 2026)
- Valve handbook, via Nora's round-1 note: https://media.steampowered.com/apps/valve/Valve_Handbook_LowRes.pdf (not re-read by me)
- Gary Klein, "Performing a Project Premortem", HBR (summary only): https://hbr.org/2007/09/performing-a-project-premortem
  (read 27 Oct 2026)
- Wikipedia, "Pre-mortem": https://en.wikipedia.org/wiki/Pre-mortem (read 27 Oct 2026)
- Harvard Gazette, "Surgical safety checklist drops deaths and complications by more than one third" (Jan 2009):
  https://news.harvard.edu/gazette/story/2009/01/surgical-safety-checklist-drops-deaths-and-complications-by-more-than-one-third/
  (read 27 Oct 2026)
- Haynes et al., NEJM 2009, on PubMed Central (blocked by a browser check; not read): https://pmc.ncbi.nlm.nih.gov/articles/PMC2810011
  (UNVERIFIED)
- Repo files checked: `keel/library/ips_road_2026-10/01_REQUIREMENTS_GAP.md`, `04_IPS_EDITS_2026-10-24.md`,
  `keel/ips_rewrite/drafts/D1/ips.txt`, `D3/ips.txt`, `D4/ips.txt` (read 27 Oct 2026)
