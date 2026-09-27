## Pull-quote finding: "The only person who needs to believe in something is yourself."

**What the case shows** (VERIFIED-REPO-FILE: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
lines 31-33, and the PDF page 1 rendered and viewed on 2026-09-27):
- The line sits in a pull-quote box in the right margin of page 1, beside the paragraph about The Wuhan I Know. The
  page is titled "MEET LAURA GAO / Storyteller, Entrepreneur, and Creative Visionary".
- It is set in large grey italics under a big gold opening quote mark. That mark is drawn as a graphic, which is why
  the text file does not show it. There is no closing mark and no name line.
- The only picture on the page is her headshot, which contains no text. Pages 2-4 have no pull quote.
- So the case presents the line as a quotation on Laura's page, and a reader will assume it is hers. But the case
  never says who said it.
- **Past cases named the speaker.** The 2021-22 case ends its client quote with "— Nichole Jordan" (VERIFIED-PRIMARY,
  https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/, read
  2026-09-27). D13b reports a name line under Connor Barwin's quote in the 2025-26 case. The 2026-27 case has none.

**Search for a primary source where Laura says it: none found** (2026-09-27).
- **Web searches (8).** None found the line in Laura's words:
  - the exact phrase (only generic self-help pages on Medium, Pinterest, Facebook and blogs, none about Laura);
  - "Laura Gao" with "believe in something";
  - "Laura Gao" with "needs to believe";
  - "only person who needs to believe" with Gao;
  - the case's subtitle "Storyteller, Entrepreneur, and Creative Visionary" (no page but the case uses it);
  - Wharton Global Youth with Laura Gao 2026 (no public Wharton article on her yet);
  - Laura Gao talks with "believe in yourself";
  - her book titles with "believe in".
- **Pages read and searched for "believ" (36 distinct pages or files with content):**
  - her website: 10 pages;
  - her resume, speaking guide and educators guide;
  - The Sign.al founder's page;
  - 15 interviews, profiles and news reports from 2016 to 2026 (all listed under Sources);
  - the podcast transcript and episode page;
  - the Playbook "Imagination Fund" spotlight, her CCA directory entry, the Commons Comics review, Wikipedia and
    Goodreads' quotes page;
  - the public SMApply client page, which only links to the same case PDF.

  The phrase appears nowhere. The only place where she uses "believe" about other people's support is D13a-N01 (2016).
- **Could not check:**
  - archive.org answered "429 Too Many Requests" and reset connections;
  - thesign.al returned empty pages;
  - two lauragao.com addresses returned 404;
  - HarperCollins and bookseller pages refused access (403);
  - her posts on X and Instagram need a login and were not searched;
  - the full text of her books is not available.

  The line could still come from a private conversation with Wharton, a talk, a social post or a book page.

**Verdict**
- **As Laura's words: PARAPHRASE-UNVERIFIED** (all 4 ids: B2a-Q13, B2b-Q11, B8b-Q01, B8a-Q39). As the case's words the
  wording is VERIFIED-REPO-FILE.
- **How to cite it:** as the case's framing of her outlook, for example "the case's profile of Laura highlights the
  line ..." (Client Profile, p.1). Do not write "Laura said", "in an interview" or "her motto".
- **Why this matters for the deliverables** (guidance, not text to submit). The case uses the line as her
  philosophy. Brief section 14 notes the tension with 2031, when co-sponsors must believe her dollar range and
  "overpromising" damages credibility. Her own verified words hold both sides of that tension:
  - D13a-N02 (2016) says other people's doubts matter less than launching. That is the closest verified match to the
    pull quote.
  - D13a-N01 (2016) says letting down "people who were your earliest supporters and were the first to believe in you"
    is worse than letting yourself down.

  A strong use pairs the case's line, cited as the case, with one of her own dated lines, and ties them to a promise
  she can keep, such as a floor already bought. Both 2016 lines are from her student years; say so.
- **A similar-sounding line to avoid:** B8b-Q24 ("…it's not for anyone else to judge"). It is verbatim and hers, but
  it is about her personal identity journey and is excluded under the privacy screen.

## Laura-related quotes that are NOT her words (D13b's scope; listed so nobody quotes them as hers)

| id(s) | text (short) | real speaker | D13a note |
|---|---|---|---|
| B2b-Q06 = B8b-Q27 = B8a-Q16 = B10a-Q03 | "So when she got the book deal with HarperCollins, she gave Twitter her notice." | Input reporter Annie Graham, 2022-03-07 | The "So" follows personal material in the paragraph before, so it is not evidence of a contract-first financial plan. |
| B8b-Q28 | "She's hoping to finish in time for a 2024 release." | same reporter | The book came out in 2025 (Nerd Daily Q&A, 2025-03-08). |
| B2b-Q09 | "Gao asked city officials what problem areas…" | Wharton Magazine writer Sara Albert, 2017-10-30 | The same page has a direct Laura quote on that project: "They wanted to get an insider feel for what they should do to optimize the proposal," (VERIFIED-PRIMARY, https://magazine.wharton.upenn.edu/digital/whartons-pitch-to-amazon/, read 2026-09-27). |
| B3a-Q01 = B3b-Q01, B3b-Q02, B8b-Q29 | Rights Report lines on her HarperCollins deal | Publishers Weekly, July 2020 (trade press) | Not her voice. |
| B3b-Q12 | "When her dynamic move at the Texas Youth Fall Invitational goes awry" | Publishers Weekly reviewer, 2024-12-12 | About the fictional heroine. |
| B9b-Q15 | "Once dubbed the Queen of Balance…" | third-person book description on her site (publisher-style copy; bookseller copies returned 403, so the publisher origin is not confirmed) | About the fictional heroine; not her voice. |

## Method

1. Loaded `phase_B/quotes_raw.json` (271 quotes) and `phase_D/D13_mechanical_check.json`. My scope was the 100 ids
   that D13b classed as Laura's own words, plus the 4 pull-quote ids.
2. Read every source page in full, not just the matching sentence. For each quote I checked the speaker, the piece
   date and the question being answered, and whether trimming changed the meaning. Dates come from page metadata
   where it exists (article dates; PDF creation dates for her resume and guides).
3. `D13a_laura_quotes_check.py` re-fetched every page with the current fetch helper and saved 350 characters on
   each side of every quote. All 106 were found verbatim (104 Phase B ids and 2 new).
4. Applied the privacy screen (brief section 4 and this task) to every quote. Family, partner, relationships, health,
   home life and anything outside her public professional work were excluded even when public.
5. Pull quote: rendered case page 1 to see the layout. PyMuPDF was installed in the session scratchpad only, not in
   the project environment. I also ran 8 web searches and searched 36 pages by or about Laura (see above).
6. `D13a_build_outputs.py` records every judgement and writes the JSON and the table. It checks that grouped
   duplicates carry one judgement.

## Sources (all accessed 2026-09-27)

Laura's words:
- Overachiever Magazine, 2021-03-15: https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid
- Wharton Magazine, 2022-04-06: https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/
- Poets&Quants, 2018-03-30: https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/
- The Nerd Daily, 2025-03-08: https://thenerddaily.com/laura-gao-kirbys-lessons-for-falling-in-love-interview/
- ABA Bookweb, 2022-02-07: https://www.bookweb.org/news/indies-introduce-qa-laura-gao-1627512
- Input/Inverse, 2022-03-07: https://www.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel
  (the Phase B links www.inputmag.com/... and nc.inverse.com/... serve the same text)
- Geeks OUT, 2022-05-11: https://www.geeksout.org/2022/05/11/interview-with-creator-laura-gao/
- The Honey POP, 2022-06-02: https://thehoneypop.com/2022/06/02/exclusive-interview-laura-gao-on-messy-roots-lgbtq-representation-and-more/
- Pulse Spikes, 2021-06-18: https://pulsespikes.org/story/laura-gao
- Local News Matters, 2026-02-12: https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/
- The Maverick Show ep. 190, 2022-06-23: https://www.themaverickshow.com/podcast/190-messy-roots-queer-identity-the-beauty-of-wuhan-and-writing-a-graphic-memoir-while-traveling-the-world-with-laura-gao/
  and its transcript https://www.themaverickshow.com/wp-content/uploads/2025/10/190_Laura_Gao_Transcript.pdf
- NPR, 2020-04-04: https://www.npr.org/sections/goatsandsoda/2020/04/04/823825436/the-wuhan-i-know-a-comic-about-the-city-behind-the-coronavirus-headlines
- NPR, 2022-04-24: https://www.npr.org/sections/goatsandsoda/2022/04/24/1093992912/the-pandemic-inspired-a-cartoonist-to-explore-their-wuhanese-roots-and-queer-ide
- HuffPost, 2020-04-29: https://www.huffpost.com/entry/chinese-american-illustrator-life-in-wuhan_n_5ea9c739c5b63115cec2be5a
- The Daily Pennsylvanian, 2016-01-28: https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a
- Her site and documents: https://lauragao.com/hey/, https://lauragao.com/editorial,
  https://lauragao.com/s/Laura-Gao-Resume.pdf, https://lauragao.com/s/Publicity-and-Speaking-Guide-Laura-Gao-e5n7.pdf,
  https://lauragao.com/s/Educators-Book-Clubs-Guide-Messy-Roots-klc2.pdf, https://lauragao.com/rewriting-herstory,
  https://lauragao.com/the-evolution-of-dance-music, https://lauragao.com/philly-happy-hours, https://signaltemp.github.io/

Also read for the pull-quote search:
- Laura's site: https://lauragao.com/, https://lauragao.com/comics-and-stories/, https://lauragao.com/projects,
  https://lauragao.com/speaking-events, https://lauragao.com/kirbys-lessons-for-falling-in-love
- Other pages about her: https://www.playbook.com/blog/laura-gao-imagination-fund-recipient-spotlight/,
  https://portal.cca.edu/people/lauragao/, https://www.commonscomics.com/2022/messy-roots-by-laura-gao/,
  https://en.wikipedia.org/wiki/Laura_Gao, https://www.goodreads.com/author/quotes/20531180.Laura_Gao,
  https://magazine.wharton.upenn.edu/digital/whartons-pitch-to-amazon/
- Competition pages: https://wghsinvcomp.smapply.us/res/p/client/,
  https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/
- Official case: `competition/official/2026_27/Laura_Gao_2026_Client_Profile.{txt,pdf}` (repo; SHA-256 in
  `manifest.yaml`).

## What this teaches

- **A quote is three facts, not one:** the words, who said them, and what question they answered. The script got the
  words right for all 104 ids. Reading the page around them changed the status of 11 ids and the safe use of about a
  dozen more.
- **Short fragments are where meaning slips.** "risk-adverse", "No more gimmicks." and "It's not published in
  Mandarin" all mean something different once you read the sentence they came from.
- **A pull quote with no name is not a quote from the person.** Cite the document that printed it (the case), and
  look for the person's own words to stand beside it.
- **Public does not mean usable.** An interview can be published and accurate and still be about someone's family or
  private life. Writing about a real client means using only her professional record.
- **A transcript is a copy of speech, not the speech.** When the copy has obvious errors, treat its exact wording as
  unconfirmed until someone checks the audio.
- **Dates matter.** Several of her most quotable lines come from her student years (2016-2018). Saying so is more
  honest, and more convincing, than presenting them as what she thinks today.
