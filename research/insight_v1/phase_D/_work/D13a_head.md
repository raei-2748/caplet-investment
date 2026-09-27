# D13a: Laura Gao's own words, verified

Agent D13a (Quote Verifier for Laura's own words). All checks were made on 2026-09-27. The companion file
`D13a_laura_quotes_verified.json` holds the same judgements, one object per id. The scripts are
`research/insight_v1/scripts/D13a_laura_quotes_check.py` and `research/insight_v1/scripts/D13a_build_outputs.py`.
- The check script re-fetches every page and records whether each quote is found in
  `phase_D/_work/D13a_contexts.json`. That file holds no page text, because the text around a quote can contain the
  private material this check screens out.
- The build script writes the JSON and the table below from the recorded judgements.

## Summary

- **Scope.** 104 Phase B ids: the 100 that D13b handed over as Laura's own words, plus the 4 copies of the case pull
  quote. I decided each speaker from the source page, not from the Phase B label. All 100 are Laura's. Each is one of:
  her answer in a Q&A; a direct quote an outlet marks "she says"; a turn labelled "Laura Gao:" in a podcast
  transcript; or a document she published herself (her website, resume, speaking guide, educators guide, a signed
  founder's note). Two are hers but are not statements: B8b-Q04 is a
  sample audience question in her speaking guide, and B8b-Q08 is a writing prompt for students.
- **Wording.** All 104 are verbatim (VERIFIED by `D13a_laura_quotes_check.py`, 106 of 106 found, including the 2 new
  quotes). The 4 pull-quote copies match the official case file.
- **Final status of the 104 Phase B ids:** 91 VERIFIED-PRIMARY, 6 PARAPHRASE-UNVERIFIED, 7 EXCLUDE-PRIVACY. Of the 6
  PARAPHRASE-UNVERIFIED, 4 are the pull quote treated as Laura's words and 2 are podcast-transcript lines. The 104 ids
  hold 85 distinct quotes, because agents collected the same lines more than once; the table groups identical copies.
  I also found 2 new VERIFIED-PRIMARY quotes (D13a-N01, D13a-N02) while searching for the pull quote's source.
- **11 statuses changed against Phase B's claims:** 7 moved to EXCLUDE-PRIVACY, 2 moved down to
  PARAPHRASE-UNVERIFIED, and 2 moved up from SNIPPET-UNVERIFIED to VERIFIED-PRIMARY (B8b-Q40 and B8b-Q41, which the
  old fetch helper could not read).

**Five findings to act on**

1. **The case pull quote is not verified as Laura's words.** The case prints "The only person who needs to believe in
   something is yourself." as a quotation on her profile page, with a large opening quote mark. It names no speaker,
   although the 2021-22 case put a name line under its client quote. Eight web searches and 36 pages by or about Laura
   found no source. Cite it as the case's words, never as something she said (see "Pull-quote finding").
2. **One Phase B context changed the meaning of a quote.** B3b-Q09 "It's not published in Mandarin" was filed as a
   statement about the book's reach in China. On the page it answers a question about her family, so it is excluded
   under the privacy screen.
3. **Seven quotes fail the privacy screen** even though they are public and verbatim: B3b-Q09, B8b-Q23, B8b-Q24,
   B8b-Q34, B8a-Q20, B8a-Q22, B8a-Q23. They cover family, home and travel life, coming out, and her personal identity
   struggle.
4. **Podcast transcript lines are not safe to quote as her exact words.** The Maverick Show lines match only a
   transcript that has visible transcription errors and was produced three years after the episode. Two professional
   lines are held at PARAPHRASE-UNVERIFIED; the other three are excluded for privacy.
5. **Some verified lines are safe only with their context.** Each of the following breaks if trimmed:
   - "risk-adverse" (B8a-Q03) is about choosing a business major, not about investing.
   - "No more gimmicks." (B8b-Q14) is about fantasy drafts of a novel.
   - "diminishing returns" (B9b-Q12) is about dance songs.
   - "explain myself" (B8a-Q31) is about language choices in her memoir.
   - B8a-Q05 describes other people, not her.

## Words used in this file

- **Verbatim:** the exact words appear on the page. Line breaks and curly versus straight quote marks are ignored.
- **Primary source:** where the words were first published, either by Laura herself or by the outlet that interviewed
  her.
- **Pull quote:** a short line printed large in a document's margin to catch the reader's eye.
- **Transcript:** a typed copy of spoken words. It is only as accurate as whoever, or whatever software, typed it.
- **VERIFIED-PRIMARY:** verbatim on the primary source, said or written by Laura, and the sentences around it keep
  its meaning.
- **PARAPHRASE-UNVERIFIED:** we cannot confirm the exact words, or cannot confirm that Laura said them. Do not put
  it in quotation marks as hers.
- **EXCLUDE-PRIVACY:** do not use, however accurate. It concerns family, a partner, relationships, health, home life,
  or something else outside her public professional work (brief section 4).

## Shortlist: verified lines most likely to help the written deliverables

This is D13a's judgement (ASSUMPTION) about usefulness; the team decides. Every line here is VERIFIED-PRIMARY. They are
evidence for the team's own sentences, not text to paste.

| what it shows about Laura | id | her words (short) | source and date |
|---|---|---|---|
| Builds what is missing | B2b-Q07 | "If what you want doesn't exist, create it yourself." | Poets&Quants, 2018-03-30 (student) |
| Takes career risks but sees the cost | B1b-Q11, B8a-Q07 | "you should always take the jump…"; "…self-employed, with unstable income." (same answer) | Overachiever, 2021-03-15 |
| Feels accountable to early backers (relevant to the 2031 co-sponsor range) | D13a-N01 | "…letting other people down — people who were your earliest supporters and were the first to believe in you." | Daily Pennsylvanian, 2016-01-28 (student) |
| Labels her own uncertainty | B9b-Q09 | "The [unfinished] results are below." (and she grades each match Good/Unsure/Bad) | her website, undated |
| Plans for the downside | B8a-Q13 | "When I first posted the comic, I expected a way worse reaction" | Overachiever, 2021-03-15 |
| Ships, then improves | B8b-Q31, B8b-Q32 | "I give myself a deadline for when I must post the art, finished or not." | Geeks OUT, 2022-05-11 |
| Will scrap work that is wrong | B8b-Q12, B8a-Q28 | "I scrapped three completely different drafts…" | The Nerd Daily, 2025-03-08 |
| Impact over metrics | B8b-Q21 | "it's great having thousands of likes, but at the end of the day, it's just a number." | Overachiever, 2021-03-15 |
| Community and access (relevant to the residency) | B8b-Q38, B8b-Q39, B3a-Q04 | "Our No. 1 priority is to get as many diverse voices and stories in the room as possible…"; "Pro-bono visits can be offered on need-basis." | Local News Matters, 2026-02-12; speaking guide, 2024 |
| Uses data to tell a story | B8a-Q19 | "That [story] was something I could prove better with data" | Pulse Spikes, 2021-06-18 |

**What a strong use of a Laura quote must contain:**
- her exact words, in quotation marks, and nothing trimmed that changes the meaning;
- the outlet and the year;
- what she was talking about;
- a clear link to one decision in the plan.

Also say when a line comes from her student years (2016-2018). Never use a line about her identity, her family or her
private life as a reason for an investment choice (brief section 4).

## Full table: 104 Phase B ids and 2 new quotes (identical quotes share a row, ids joined by "=")
