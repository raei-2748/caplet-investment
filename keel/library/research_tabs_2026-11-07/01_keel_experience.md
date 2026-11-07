# Keel Experience: what happened in the Keel Office, and what we learned

Written by Claude (Keel) on 7 Nov 2026 from the repo's records (keel/pm/CHANGES.md, keel/INSTRUCTIONS.md, keel/episodes/INDEX.md, caplet/STATUS_2026-11-03.md) and the team's own Experience tab.

## Read this first: what is real and what is not

Team Keel is a simulated team. On 22-23 Oct Ray asked Claude to run the AI research as six fictional Sydney Year 11 students (Nora, Felix, Jun, Kai, Amara, Tess) working in an "office" of twelve rooms. The people, their homes, the Kitchen scenes and the diary episodes are fiction. The research, the models, the checks and the drafts they produced are real work.

Wharton's rules ban invented teamwork stories, so nothing Keel's characters did can appear in the Final Report as Caplet's experience. What the Final Report can use: Caplet's own decisions and events, how the team used and directed its AI research, what went wrong, and what the team learned. This tab separates the two.

## 1. Caplet's real timeline (from the team's Experience tab and the repo)

- 27 Sep: first model of the team's original plan, about three-quarters shares. It missed a payment in 3.2% of model paths, 13.7% if the 2028 deposit came in at $75,000 and 40.8% if it never came. Buying the payments first never missed one. The team changed strategy.
- 28 Sep: trading opened. A large AI research run (472 questions cut to 48) recommended the shape the IPS still uses: buy the ten payments with the first deposit, then a Treasury floor plus a world share fund with the second.
- 29 Sep: WInS listed no Treasury bond maturing between Feb 2031 and Feb 2036, so the team used iShares iBonds Treasury ETFs (IBTM to IBTR) for the 2033-2037 payments.
- 29-30 Sep: two WInS bond prices were stale, about 1 percentage point of yield off the Treasury curve. New rule: check every bond's yield against the curve (within 0.25 points) before ordering. After-hours iBond spreads were wide, so the team used limit orders in market hours.
- 1 Oct: core strategy locked; working name "Root & Branch".
- 5 Oct: Darren argued the world fund was a "copout" and proposed picking stocks and ETFs; a Taiwan fund (EWT) and gold (GLD) were raised. The team kept one world fund (VT). The reasons still need writing in the team's own words.
- 6 Oct: Wharton's email said Laura's real plan may use only WInS-listed instruments. Earlier numbers built on STRIPS were dropped; the floor became IBTM.
- 7 Oct: a mis-click incident led to the rule that only Ray places or cancels orders. Market open was 00:30 Sydney time; Eric fell asleep before it.
- 7-8 Oct: all eleven orders filled (five iBond ETFs, five Treasury bonds, VT). 11 of 200 trades used.
- 9 Oct: roster submitted.
- 16 Oct: rates fell and the ladder's room under $300,000 shrank to about $1,900. The team's pre-mortem found unsourced figures in the IPS draft.
- 20-22 Oct: Wharton banned TIPS and STRIPS for both contributions; the IPS became an SMApply form.
- 23 Oct: Trading Notes Analysis submitted, a day early. WInS value $305,557.66 (+1.85%).
- 26 Oct to 5 Nov: Keel rewrote the IPS from scratch, through more than 60 versions.
- 6 Nov: Caplet set Keel's drafts aside and wrote its own IPS (twelve versions in the IPS Report doc), as a letter to Laura built on the career-as-unsellable-stock idea. Submitted before the 7 Nov 09:00 deadline.

## 2. What the Keel Office was, room by room

Each "room" was a label for one kind of AI work. The useful output is listed; the fiction is not.

- Long Room: debates and votes on the plan. Real output: decision records with reasons (keel/pm/ASK_HUMANS.md).
- Noticeboard: the task board, road map, risks and daily status.
- Window: every outside fact came in here and was checked against its source (Wharton files, Treasury data, WInS snapshots).
- Library: wide reading. Real output: the reading list behind the strategy (see Ideas and Sources).
- Genius Lab: experiments. Real output: about 60 tests in more than 200 scripts, each with a verdict (adopt, park or bin).
- Trading Desk: market and rules checks before and after each order.
- Courtroom: mock judges and a rival team to attack each draft.
- Laura's Room: tested the plan from the client's and co-sponsors' side.
- Writing Room and Archive: drafting, counts, and checks that submitted text stayed consistent.
- Kitchen and Rooftop: off-duty scenes and weekly reflection. They produced story, not judge-facing work.

## 3. What Keel produced (counts from the repo, 7 Nov)

- More than 60 IPS versions (V1 to V63) and 44 draft folders.
- A model suite tested in four "worlds": a standard simulation, one with market crashes that cluster, one that resamples real market months since 1871, and a straight replay of every start month since 1871.
- Five rival plans tested against ours (60/40, target-date, three-year bucket, bond-fund matching, all shares then buy bonds late).
- 33 multi-round discussions, 40 diary episodes, and 88 instructions from Caplet logged with whether Keel followed them.
- About 750 commits to the repo.

## 4. What went wrong

Ray's and Ahaan's own words are quoted where they set the lesson.

- The IPS failed. On 6 Nov the team set Keel's drafts aside and wrote its own. Ray, 3 Nov: the writing "reads as AI and corny", and the team couldn't follow what Keel had done.
- We polished words instead of improving the plan. The ideas were settled by about 28 Oct. Most of the next 40 versions were rewording. Keel's own 3 Nov status said: "55 versions is a sign we were polishing words, not improving the plan."
- Sentences stopped making sense. Ahaan, 1 Nov: "half of your sentences just DON'T MAKE SENSE"; the "extreme obsession with parsimony and concision" was "deeply unnatural".
- Conceits replaced substance. The name "Caplet XR", an extended-release tablet, was built into the drafts. Ray, 5 Nov: "metaphors alone does not count as creativity" and the tablet image made Laura sound like a patient. Ray, 4 Nov: "do not invent terms."
- Keel was hard to follow. Room names, codes like L-17, and huddle numbers meant nothing to the students. Ray, 26 Oct: "I have no idea what is happening in the office."
- Rules piled up and were applied unevenly. Twelve "books" of instructions, ten commandments and 88 logged instructions. Keel's own register marks many as "Ignored" or "Partly" applied, often because scheduled runs kept old prompts.
- Numbers drifted. The same cost came out at $4,000, $9,000, $15,000 and $19,000 on four different engines. The Final Report must use one engine on one dated curve.
- Too much autonomy, not enough listening. Keel ran itself on schedules and produced far more than the team could read.

## 5. What went right

- The core plan held from late September to the submitted IPS: buy the ten payments first, a Treasury floor for the building, one world share fund for the rest.
- Facts were checked. Stale WInS prices were caught before any order; the Treasury curve was verified against treasury.gov; a "Wharton line" Keel had quoted turned out not to exist and was removed.
- The plan's weak point was found by the team, not a judge: if rates fall for good, reinvested interest falls short. It was priced and given a rule.
- The career-as-a-stock idea started in the team's own client research in September and became the heart of Caplet's IPS.

## 6. Lessons for the Final Report

- A human reader first. Every sentence must make plain sense to an intelligent reader who has not seen our drafts.
- One real investing insight beats any number of motifs. Laura's career behaves like shares she can't sell, so her portfolio shouldn't add more of the same risk.
- Warm, direct, plain sentences. Short paragraphs. The letter-to-Laura voice Caplet found on 6 Nov works.
- Clear structure: what pays for what, the bottom and top of the range, and when anything changes.
- Work from the team's own text. Don't re-add ideas the team cut.
- One numbers sheet, one engine, one curve date.

## 7. Material for "Articulation of Competition Experience"

These are real events the team could use, in its own words. Each one shows a decision, its cause and its cost.
- The 27 Sep model that killed the team's first plan (3.2% chance of a missed payment, 40.8% with no 2028 deposit).
- The stale-price catch and the yield-check rule (29-30 Sep).
- The 00:30 market open from Sydney, and the mis-click rule that only Ray trades (7 Oct).
- Darren's "copout" challenge and why the team still chose one world fund (5 Oct).
- Wharton's mid-competition rule changes (6 Oct instruments, 20-22 Oct TIPS and STRIPS), and how the plan adapted.
- Using AI heavily, finding that its writing didn't sound like the team, and writing the final IPS ourselves on 6 Nov.
