# Team Keel: Caplet's mirror team

**FICTION, AI-generated (Claude Code), started 22 Oct 2026 at Ray's request.** Keel is an imaginary team of six
students in Sydney. They work on the same competition, the same client (Laura Gao), the same deadlines and the same
Wharton files as Caplet. They are written as a team we are confident would reach the semifinals or the finale.
Every day a new episode shows what they did: research, debates, mistakes, decisions.

A keel is the part of a boat that keeps it upright under sail. That is the team's idea of Laura's portfolio: the
payments are the keel, growth is the sail.

## Why it exists
- **A mirror.** Keel runs into the same problems as Caplet a day or two earlier and shows a strong way through.
  Each episode ends with **"What Caplet can take from today"**: concrete checks for our own work.
- **A voice.** Each Keel member has a personality and a way of arguing. Caplet's writing came out generic partly
  because no one in the AI record had a point of view. Keel members do.
- **Real research inside a story.** The story is invented; the research is not. Every fact, rule and number in an
  episode is real, dated and sourced, or is marked MODEL or UNVERIFIED.

## Hard rules for every episode
1. **Label.** Every file starts with "FICTION" in its first line. Keel is not a real team; its members are not
   based on Caplet members or anyone real. Never map a Keel member onto a Caplet student, and never rank Caplet
   students.
2. **Never copy Keel's story into Caplet's deliverables as Caplet's experience.** Wharton's ethics rule bans
   invented teamwork and experience stories. Keel's *research findings* may be used (re-check them first); Keel's
   *events* never are.
3. **Real research only.** Facts, rules and numbers come from:
   - Wharton's official files in `competition/official/2026_27/` (in the story this is the team's shared Google Drive
     folder "Wharton official"), quoted exactly with file and line;
   - public primary sources fetched that day (URL + date), e.g. treasury.gov, fund fact sheets, Taiwan DGBAS;
   - numbers computed by code that day (say MODEL and give the inputs).
   Keel does not read Caplet's private research files; it reaches its own conclusions.
4. **Same calendar as Caplet, Sydney time first.** TNA Sat 24 Oct 08:00; IPS + trading freeze Sat 7 Nov 09:00;
   Final Report instructions Tue 10 Nov 01:00; Final Report Sat 5 Dec 09:00 (all Sydney).
5. **Keel obeys the 2026-27 rules.** Only WInS-listed stocks, ETFs and Treasury bonds; no TIPS, STRIPS, margin,
   shorting, crypto or derivatives (Week 4 email). WInS profit is never added to Laura's projections.
6. **Characters stay in character** (see `personas/`), and they disagree for real. They are allowed to be wrong; the
   story shows how they find out.

## Daily episode recipe (for the scheduled session)
1. Read this README, `personas/*.md`, `STATE.md`, the last three episodes, `CLAUDE.md` and `COMPETITION.md`.
2. Work out today's date in Sydney and where the competition calendar is. Pick **one** event that a strong team
   would plausibly face today: a rule question, a research question, a draft review, a disagreement, a market move,
   a deadline task. Prefer what Caplet is about to face in the next few days.
3. Do the research for real: read the official file, fetch the page, run the numbers. Keep a source list.
4. Write `episodes/YYYY-MM-DD_epNN.md` as a diary episode, 600-1,000 words:
   - title, date (Sydney), whose point of view;
   - the story, with dialogue in each character's voice;
   - **Decisions** (decision, owner, date) and **Open threads**;
   - **What Caplet can take from today** (2-5 specific checks, each pointing at a Caplet file or deadline);
   - **Sources** (file:line, URL + access date, MODEL inputs).
5. Update `STATE.md` (plan, decisions log, open threads, relationships).
6. Commit and push. Episodes are fiction; the research inside them is logged as AI use for the Works Cited.

## Files
- `personas/` - the six members (`01_maya.md` ... `06_ines.md`)
- `STATE.md` - Keel's running plan, decision log, open threads
- `episodes/` - one file per day
