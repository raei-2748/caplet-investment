# Research round 2: the brief every worker reads first (Mon 16 Nov 2026, Sydney)

Caplet, Mon 16 Nov: "I don't see you doing anywhere near the volume of research and analysis I want to see from you
... GO INTO OVERDRIVE". So from today every Final Report run sends many research workers at once, each on one hole in
the store (`store/DIGEST_2026-11-15.md` sections 3-4), and every find lands in the store as card rows. The day's
volume is counted in `VOLUME.md`. This file is the shared brief; each worker's own question is in its prompt.

## What the work is for

Team Caplet (six Sydney high-school students) is writing the Final Report for the Wharton Global High School
Investment Competition 2026-27, due Sat 5 Dec 2026. The client is Laura Gao (official case:
`competition/official/2026_27/Laura_Gao_2026_Client_Profile.pdf`): $300,000 at the start of 2027, $150,000 at the
start of 2028, ten fixed $50,000 payments each January 2033-2042 for an arts residency's operations in Taiwan, an
operating reserve from 2033, a facility contribution with flexibility, and in 2031 a dollar range with a confidence
level for co-sponsors. No report prose is written before Fri 27 Nov: workers write research notes, never report text.

## Read first, in full (about 15 minutes)

1. `keel/final_report/FINAL_IPS_as_submitted.txt` (Caplet's own IPS, submitted 7 Nov; frozen; the report must agree
   with it). Plan in one breath: ten Treasuries (T-bonds or iShares iBonds Term Treasury ETFs) bought Jan 2027, each
   maturing just before its payment; the 2028 deposit first completes the ladder if yields fell, then most of the rest
   buys a Treasury fund maturing late 2032 (the floor, IBTM), the remainder VT (world shares, the ceiling); half the
   shares are promised to no one (her flexibility); the other half moves into Treasuries before the 2031 co-sponsor
   meetings; only two reasons to change the plan: a missed deposit or a Treasury default.
2. `keel/drafts/writing_room_2026-11-03/tna_as_submitted.txt` (the locked Trading Notes Analysis).
3. The parts of `keel/final_report/NUMBERS.md` your topic touches (grep it). NUMBERS is the only source of figures
   about the plan: never compute a plan figure of your own and present it as the plan's; your own arithmetic on a
   source's figures is labelled "Keel arithmetic".
4. The existing cards your prompt names, so you add and never repeat. Grep the store too:
   `grep -ci "<term>" keel/final_report/research/store/insights.jsonl`.

## Rules that bind every row (Caplet's books; `keel/EXPECTATIONS.md` holds them all)

- If a search tool says its credits or free tier are used up (Firecrawl, Parallel), switch to WebSearch and WebFetch and carry
  on; list in Gaps anything you could not reach.
- Real sources only, read at source (the page, paper, statute or dataset itself, not a summary of it), with URL and
  the date you read it. Quote short exact phrases when a row rests on wording. Anything you could not read at source is
  marked UNVERIFIED and says why. Never fill a gap from memory or "typical" practice.
- Prefer primary sources, papers, theses, official data and practitioners' own documents; read widely and from any
  field. Wharton's own pages are never a reference (context only).
- Treasuries may be called guaranteed, locked, set in stone or risk-free; do not add "barring a US default" (Books 3, 5,
  19). A false fact stays out; a strong true word stays in.
- Never: "optimal"; "a natural hedge"; CPPI, "portfolio insurance" or "capital-protected" for this plan (it is
  buy-and-hold); "full funding" for the facility; "endowment" for the operating reserve; "prudent" for the range rule
  (a statute's name may be quoted as a name); TIPS or STRIPS as anything Laura could hold (banned by Wharton this year);
  "Taiwan's government cut arts money in a recession" (it rose 29.1% in 2009); VT as a Taiwan-dollar hedge;
  "fail-safe" for the whole plan; an iBond fund's payout as fixed; J.P. Morgan's 7.5% as "the top" or "the consensus"
  (it is above the middle of published forecasts, with no median figure in the report: about 6.5% of fifteen houses, 6.9% of seventeen with Goldman Sachs's 7.7% and Fidelity International's 7.6%; Tue 17 Nov evening, card Q117 row 8; Wed 18 Nov evening, card Q146); "the largest share" for the founder (in Taiwan the founder pays
  first); "cash cannot go below zero"; "ended on schedule" for the iBond funds (IBTA ended 15 days early); a stated
  contribution above the stated top.
- Flag any clash with the IPS or the TNA in the clash column (for example: paying a payment from shares; selling the
  bonds as rates move; a fixed $150,000 minimum; later bonds' interest paying earlier payments).
- No invented people, events or quotes. No student surnames, emails or other personal data. Never use or read WInS or
  SMApply; never contact Laura Gao or anyone else; never post anything anywhere.
- No AI-use or integrity notes, and no AI-detector anything.
- Plain English in every cell: a smart 16-year-old should follow it.

## What to write

One new card, `keel/final_report/research/cards/<your card id>_<short_name>.md`, in the form of the recent cards
(read `cards/Q45_selling_in_a_stress.md` for the shape):

1. Title line `# <id>. <the question in plain words>`, then bullets: Date (Sydney), Report parts it serves (SKELETON
   part numbers: 2.0-2.5, 3.0, 3a-3f, Tables 1-3), "Notes for the Final Report store, not report prose", Not repeated
   (the cards and store ids you checked), Claims tested (2-5 claims a judge might make or the report might lean on,
   each to keep, kill or change), Problem class and the field that solved it first.
2. `## Verdicts in one screen`: each claim's verdict with the numbers and sources, and a one-line "Judge's note" where a
   finding could give a Wharton judge an "aha" (a place where a smart reader had it backwards).
3. `## Rows for the store`: the harvest table, header exactly

   `| # | Idea (plain words, one line) | Source(s) as cited in the file | Tags | Niche? | Analogy/use for Laura | Critique/disanalogy already recorded | Verified? | Clash with FINAL or TNA? | Where it was found |`

   then `|---|---|---|---|---|---|---|---|---|---|` and one row per distinct idea, numbered `| 1 |`, `| 2 |` ...
   Aim for 25-45 strong rows; never pad. Tags from: CAREER, CERTAINTY, LADDER, COMPLETE2028, FLOOR, CEILING, HALFKEPT,
   MOVE2031, RESERVE2033, TWOREASONS, COSPONSOR, FUNDRAISING, RESIDENCY, INFLATION_TWD, REINVEST, LAURA, PROCESS,
   PRESENTATION, OTHER (several allowed, most important first). Niche? is TEXTBOOK, KNOWN or NICHE. Verified? is
   "VERIFIED (read at source, <date>)", "UNVERIFIED (why)" or "CONFLICTING (what)". Where it was found: "This run:
   <site or dataset>".
4. `## Best five for the report`: the five rows most likely to give a judge an aha or do a job Wharton asks a part to
   do, each with the part it serves and one line on why.
5. `## Gaps`: what you looked for and could not find, so the next round can.
6. `## Sources`: APA 7th entries for every source read, with URL and "Retrieved <date>".

Pipes inside a cell break the table: write "/" instead. Keep each row to one line.

## Files

- Write only your own card (and, if your prompt says so, a data file under `keel/final_report/research/cards/data/`).
  Do not edit any other file: the lead merges, rates and registers.
- Do not commit or push; the lead does.
- `/mnt/project-files/` is a shared network folder: do not search it, and do not write to it.
- Report back in under 200 words: the card path, the number of rows, the number of sources read at source, and the
  three strongest finds in one line each.
