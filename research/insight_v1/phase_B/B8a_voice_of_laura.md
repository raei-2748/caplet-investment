# B8a Voice of Laura (lens: her own words; starting angle: long-form conversations)

Agent B8a, insight_v1 run, Phase B. Written 2026-09-27. AI-generated research for Team Caplet, not submission text.
It collects Laura Gao's own public, professional words. It maps them to her values, how she decides and how she handles
risk, and it turns them into questions that could change a decision, a number or a sentence. The team writes every
deliverable in its own words. Quotes are for the team's understanding. Before quoting any of them in a deliverable,
check the Works Cited and AI rules (R-W30, R-W46).

Privacy rule applied: I read pages that also contain personal and family material. I left all of it out: family
members, partner, birth name, health, relationships and coming-out stories. Only her public professional statements
and facts about her work are recorded here.

---

## 0. Summary (read this first)

1. **The case pull quote may not be her words.** "The only person who needs to believe in something is yourself."
   (R-C21) did not appear in any of the 25 public sources I opened (interviews, podcast transcript, her website, her
   speaking guide, her resume). An exact-phrase web search found only generic self-help pages. **Status:
   UNATTRIBUTED.** Treat it as the case's words ("the case profile highlights…"), never as "Laura says…" (Q01).
2. **Her real risk pattern: she lined up a funded base first, then leapt.** She calls the move "such a drastic move
   from an outside perspective" and says "you should always take the jump". But the reporting shows that she had "made
   a tentative plan" before the comic went viral, and she "gave Twitter her notice" only "when she got the book deal
   with HarperCollins" (Inverse, 2022, VERIFIED-PRIMARY). She also named the cost plainly: giving up a "cushy, paying
   job with health insurance to be self-employed, with unstable income" (Overachiever, 2021). **Our lock-early design
   (buy the promise first, take risk only with the surplus) matches this pattern.** This is the strongest Laura-rooted
   argument for it, and it is also an argument against "she likes risk, so give her more equity" (Q02).
3. **She rejects gimmicks and over-engineering in her own work.** She wrote "I scrapped three completely different
   drafts" and "So, I scrapped everything and went back to my roots. No more gimmicks." (Nerd Daily, 2025). This is
   last year's lesson ("complexity must earn its place") in her own voice. Every branded framework, thematic tilt or
   book-title pun has to pass this test (Q03, Q22).
4. **She writes a purpose statement for her work and treats the medium as replaceable.** "I can't think of many art
   pieces that I didn't also write some kind of purpose statement for." "I've always said that my main purpose is to
   tell a story" (Pulse Spikes, 2021). The mapping to an IPS is direct: purpose first, instruments as swappable
   "media" (primary pick plus alternates) (Q04).
5. **Her 2028 income is exposed to politics and timing more than to the stock market.**
   - Her books have been published late twice. *Messy Roots* was "planned for summer 2021" (Publishers Weekly, July
     2020) and went on sale 8 March 2022. *Kirby* was hoped for "2024" (Inverse, 2022) and came out in 2025.
   - In March 2025 she said she was "taking a short break from writing".
   - Her past speaking clients include corporate DEI/ERG events at Asana, Adobe and a Google LGBTQ+ group.
   - A Montana school board banned *Messy Roots* in January 2024 (Book Riot).
   - Implication: the 2028 deposit is more likely to be *late* or cut by a *political/budget* shock than to move with
     equities. That changes how we write about human-capital and wrong-way risk (Q08, Q09).
6. **She has built community institutions in stages, kept them free, and given out small grants.**
   - Pride in Panels: "way beyond our initial passion project"; "We definitely hope to offer more as the festival
     grows"; the event is free and gives mini-grants to 20 creators (Local News Matters, Feb 2026).
   - She finds community through co-living and co-working spaces (Maverick Show, 2022).
   - This supports three things: the case's operations-first order, a flexibility buffer, and a range that can grow
     as support is proven (Q12, Q13, Q23).
7. **Taiwan appears in her own words.**
   - "Taiwan is like one of my top places to live in and to travel to all time."
   - Among her favourite places she names Yilan, noting "some art residencies at the top of the mountains there"
     (Maverick Show transcript, June 2022).
   - The case scenario is fictional (R-W4), so never present this as her plan. It still tells us that a Taiwan
     residency is plausible for her, and a rural setting would change which cost index is relevant (Q10).
8. **Her first public act was correcting a one-sided risk story about a place.** "It's disheartening to know that
   all they know are the bad parts of it" (NPR, 2020). "focus on the full human story" (HuffPost, 2020). So a Taiwan
   section that reduces Taiwan to "Strait war risk" is exactly the framing she fought. Name the risk precisely and
   completely, once (Q11).
9. **She has shown both sides of finance: the trading floor and consumer protection.** She was a Trading Intern at
   Belvedere Trading and a Policy Analyst Intern at the CFPB. She also taught "financial literacy to high school
   students in West Philadelphia" (Poets&Quants 2018). A high-school team is writing for a former financial-literacy
   teacher of high-schoolers. That raises the bar on fee disclosure, plain words and honesty (Q06, Q07).
10. **Her working style matches the Trading Notes design.** "Always start small and post that work, no matter how
    crappy it looks!" "I give myself a deadline for when I must post the art, finished or not." (Honey Pop, 2022).
    She kept a daily "comics diary". She co-founded an "Anti-Resume Project" to "normalize failure". Implications: an
    early small first trade, notes written as an experiment log, and a candid Articulation section (Q15-Q17).

Counts: **25 questions** (section 5). **48 numbered quotes** in the quotes table (section 2), all VERIFIED-PRIMARY (#4, #5 and #18 are reporter text), plus a few
reported facts. 68 phrases in total were confirmed verbatim (list in section 7).

---

## 1. Method and source access (what I opened, how quotes were verified)

- Access date for every page: **2026-09-27** (between about 14:00 and 15:30 UTC), from this run's container.
- Verification: each quote was checked with `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL --grep
  "phrase"` and returned `PHRASE FOUND VERBATIM: YES`.
- **One exception (Poets&Quants page), handled as follows:**
  - The helper's Chrome user agent got HTTP 403 from poetsandquantsforundergrads.com. Plain curl (default user
    agent) returned 200, so I saved that response into the helper's cache.
  - The helper's HTML parser then printed almost no text. It drops the page body on this WordPress page.
  - I verified these quotes with a scratchpad variant, `ft2.py`. It uses the helper's own `fetch()` and `norm()`
    functions and only swaps the tag stripper for a regex. It also returned `PHRASE FOUND VERBATIM: YES`.
  - The fix for others: add a fallback extractor to `fetch_text.py` (see Leads).
- **The Maverick Show transcript is AI-generated.** The page says "We produce our transcripts using Outcast AI". So
  its wording is a machine transcription of speech, not text she edited. The quotes are verbatim to the transcript, not
  necessarily to her speech. They are labelled VERIFIED-PRIMARY (transcript) with this caveat.
- **Anomaly:** the show's "Read the Transcript" link for Ep 190 (Laura) serves the transcript of Ep 189 (another
  guest). The correct PDF is `…/uploads/2025/10/190_Laura_Gao_Transcript.pdf`. I found it by URL pattern, and it
  opens with her introduction.

**Blocked or not useful:**

| Source | Result |
|---|---|
| legacy.diversebooks.org Q&A | Captcha page (HTTP 202, sgcaptcha); **not read** |
| ampersand-mag.com/laura-gao (2021 profile) | TLS error; **not read** |
| nuvoices.com/2022/03/17/… | 404; the alternate URL /podcast/nuvoices-podcast-72-… opened, but it is show notes only, with no transcript. Topics are mostly personal, so nothing was used |
| Wainao (Taiwan-based Chinese-language outlet) | Video only, with no transcript |
| YouTube "Laura Gao on Messy Roots book ban" | Title seen in search only; video not watched (SNIPPET) |
| lauragao.com/s/Interactive-School-Visits-Guide-Laura-Gao.pdf | Returned almost no text |

---

## 2. Quotes table (her own words; all VERIFIED-PRIMARY unless marked)

Columns: # · exact text (copied character-for-character, original punctuation) · source (URL, piece date) · context ·
value it shows · implication. Access date for all: 2026-09-27.

**Sources (short names used below):**
- **PQ** = Poets&Quants for Undergrads, "2018 Best & Brightest: Laura Gao, Wharton School", 2018-03-30,
  https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/
- **WM** = Wharton Magazine, "A Wharton Grad From Wuhan's Exploration of Identity", 2022-04-06,
  https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/
- **OA** = Overachiever Magazine, "Interview with Laura Gao", 2021-03-15,
  https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid
- **IN** = Input/Inverse, "How a viral tweet turned into a queer coming-of-age graphic novel", 2022-03-07,
  https://nc.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel
- **PS** = Pulse Spikes, "Laura Gao: A Comic Artist Tackling Misconceptions…", 2021-06-18,
  https://pulsespikes.org/story/laura-gao
- **MV** = The Maverick Show Ep 190 transcript (AI transcription), episode 2022-06-23,
  https://www.themaverickshow.com/wp-content/uploads/2025/10/190_Laura_Gao_Transcript.pdf
- **HP** = The Honey Pop, "Exclusive Interview: Laura Gao on Messy Roots…", 2022-06-02,
  https://thehoneypop.com/2022/06/02/exclusive-interview-laura-gao-on-messy-roots-lgbtq-representation-and-more/
- **ND** = The Nerd Daily, "Q&A: Laura Gao, Creator of 'Kirby's Lessons for Falling (In Love)'", 2025-03-08,
  https://thenerddaily.com/laura-gao-kirbys-lessons-for-falling-in-love-interview/
- **BW** = BookWeb (ABA), "An Indies Introduce Q&A With Laura Gao", 2022-02-07,
  https://www.bookweb.org/news/indies-introduce-qa-laura-gao-1627512
- **NPR** = NPR Goats and Soda, "'The Wuhan I Know': A Comic About The City Behind The Coronavirus Headlines",
  2020-04-04,
  https://www.npr.org/sections/goatsandsoda/2020/04/04/823825436/the-wuhan-i-know-a-comic-about-the-city-behind-the-coronavirus-headlines
- **HUF** = HuffPost, "Artist Illustrates What Her Hometown Of Wuhan Is Really Like", 2020-04-30,
  https://www.huffpost.com/entry/chinese-american-illustrator-life-in-wuhan_n_5ea9c739c5b63115cec2be5a
- **LNM** = Local News Matters (Bay City News), "SF queer comics fest expands, stays free in second year", 2026-02-12,
  https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/
- **DP16** = The Daily Pennsylvanian, "Student Spotlight Q&A: Laptop decal designer and Wharton sophomore Laura
  Gao", 2016-01-28, https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a
- **SG** = her "Messy Roots Publicity & Speaking Guide" PDF (undated; it says Kirby "will be released in 2025", so it
  was written in 2024 or earlier), https://lauragao.com/s/Publicity-and-Speaking-Guide-Laura-Gao-e5n7.pdf
- **RES** = her resume PDF (undated, current), https://lauragao.com/s/Laura-Gao-Resume.pdf
- **HEY** = https://lauragao.com/hey/ (current)

### 2a. Risk, leaving tech, jumping

| # | Exact text | Src | Context | Value | Implication |
|---|---|---|---|---|---|
| 1 | "It’s not an easy thing to say, “let me give up my incredibly cushy, paying job with health insurance to be self-employed, with unstable income.”" | OA | On leaving Twitter for full-time comics | She is aware of the downside and says the cost out loud | She calls her own income "unstable". That supports the case's split: career risk sits outside, and the promise is protected inside the portfolio (R-C37/R-C38) |
| 2 | "But I always tell myself, you should always take the jump because you’re always going to regret not doing it." | OA | Same answer | Regret-minimising courage | She respects bold moves. Our "bold" part is the growth sleeve and the residency itself, not gambling the payments |
| 3 | "I feel like I’ve been jumping almost my whole life." | OA | On switching careers | Serial pivots | Her identity is someone who jumps. The portfolio's job is to be the platform that makes jumping safe |
| 4 | "Even before her comic went viral on Twitter, she’d made a tentative plan to travel around the world, teach art part-time, and focus on her own creative endeavors." | IN (reporter, not her words) | Reporter's account | She planned before she leapt | Evidence for the pattern "plan, then leap" |
| 5 | "So when she got the book deal with HarperCollins, she gave Twitter her notice." | IN (reporter) | Reporter's account | She leapt once a contract was signed | This is the key: **a secured base, then risk.** It is the same logic as lock-early |
| 6 | "So, I can't say no to this opportunity" | MV (AI transcript) | After her agent approached her | Acts decisively when a real opportunity arrives | Supports a pre-set decision rule (e.g. buying the ladder when the money arrives) over waiting for a perfect moment |
| 7 | "I was a bit hesitant. I was like, I know this is kind of a sensitive topic. I don't know what I'll get from it" | NPR | On posting "The Wuhan I Know" | She takes risk under uncertainty, with purpose | "Thoughtful risk" = uncertain outcome, clear purpose, downside she can bear |
| 8 | "When I first posted the comic, I expected a way worse reaction" | OA | On online abuse | Plans for the worst case | A pre-mortem mindset. Show the bad-case numbers first |
| 9 | "This is who you’re trying to help, and this is the positive effect you actually have." | OA | How she steadied herself after hostile comments (a saved note) | Pre-commitment to purpose | A drawdown rule anchored in purpose (the ten payments are already bought) is her own coping style |
| 10 | "However, this lack of structure and certainty can be off-putting for students who are easily influenced by those around them or are risk-adverse." | PQ | Advice on studying business | She names risk aversion without contempt | She understands that some people need structure. "Certainty" and "structure" are her words for the protected part |

### 2b. Building things, creating what is missing

| # | Exact text | Src | Context | Value | Implication |
|---|---|---|---|---|---|
| 11 | "If what you want doesn’t exist, create it yourself." | PQ | "Biggest lesson" from studying business | Founder mindset | The residency is this principle again. A strategy built around *her* problem, not a template, fits it |
| 12 | "However, I realized transferring was nothing more than running away from the problem." | PQ | On nearly leaving Wharton | Stays and fixes rather than exits | Stay-the-course rule. Fix a problem (e.g. rates fall before Jan 2027) with a rule, not an exit |
| 13 | "Well, if people aren’t gonna give it to us, I’ll just make one." | OA | On her second book | Build what is missing | Same as #11 |
| 14 | "but why wasn’t there any single event where we could celebrate that community and bring everyone together?" | LNM | Origin of Pride in Panels (2026 article) | Community infrastructure builder | She has already founded a community institution with partners. Co-sponsors are her normal way of working |
| 15 | "All of it is way beyond our initial passion project." | LNM | Festival growth | She grows things in stages | Staged ambition: floor first, upside later (range design) |
| 16 | "We definitely hope to offer more as the festival grows." | LNM | On mini-grants to creators | Scale after support is proven | A contribution that can grow with results, not a single fixed bet |
| 17 | "Our No. 1 priority is to get as many diverse voices and stories in the room as possible, no matter the grounds that they start off on" | LNM | On grants | Access for all | Program fees may be low, so the operating money matters more (interpretation) |
| 18 | "remaining free for exhibitors and attendees" | LNM (reporter) | The festival stays free | Free access | Same. Evidence for a low-fee model (interpretation, not a case fact) |
| 19 | "Was a simple, 10-panel comic enough to accomplish such a feat?" | WM | When asked to write more | Starts small and doubts scale | Small things can grow. It also mirrors a small reserve decision growing into ten years of operations |

### 2c. Craft, simplicity, purpose, evidence

| # | Exact text | Src | Context | Value | Implication |
|---|---|---|---|---|---|
| 20 | "I scrapped three completely different drafts before landing on this one." | ND | Writing Kirby | She will discard work that is not right | Discard ideas that do not earn their place |
| 21 | "So, I scrapped everything and went back to my roots. No more gimmicks." | ND | Same | **Anti-gimmick** | The complexity test. Drop tilts, branded names and puns that do not add value |
| 22 | "I can’t think of many art pieces that I didn’t also write some kind of purpose statement for." | PS | On writing and art | Purpose first | An IPS is a purpose statement. Lead with what the money is for |
| 23 | "I’ve always said that my main purpose is to tell a story" | PS | Across her media | Purpose fixed, medium flexible | Instruments are the "medium": primary pick plus alternates, same purpose |
| 24 | "That [story] was something I could prove better with data" | PS | Her "Rewriting Herstory" data project | Evidence-backed storytelling | Final Report: one chart that proves one point. The IPS must prove it in words alone (R-I55) |
| 25 | "I've always been an artist, and I believe that comics are a great way to marry imagery with the power of words to express a story" | NPR | On comics | Words plus pictures | The Final Report charts should carry the story, not decorate it |
| 26 | "Always start small and post that work, no matter how crappy it looks!" | HP | Advice to young artists | Ship early, iterate | WInS: a small first trade early in the window. The notes show a developing strategy (R-C88) |
| 27 | "I give myself a deadline for when I must post the art, finished or not." | HP | Same | Self-imposed deadlines | Internal deadlines ahead of Oct 23 and Nov 6 |
| 28 | "Ultimately my goal is to tell a story; I don’t need to be perfect to be impactful." | HP | Same | Impact over perfection | Plain and correct beats polished and complex |
| 29 | "don't put too much pressure on getting everything perfect" | MV (AI transcript) | On her creative process | Same | Same |
| 30 | "Soon enough, I had a comics diary that I could not only decompress into, but also take pride in how far I’d come when I reread it." | WM | Nightly comic habit while at Twitter | A process record | Keep a dated decision diary; the Final Report shows growth from it |
| 31 | "My biggest advice is to be OK with the fact that your significant projects will never be finished." | DP16 | As a 19-year-old founder | Iterate forever | Tension with "the IPS freezes the strategy" (R-I35): freeze the principles and rules, and let execution iterate inside them |
| 32 | "how long will this novelty factor last?" | DP16 | On her own launch hype | Sceptical of hype | She would question an AI or thematic hype trade |
| 33 | "I wish I wrote about these nuances and tradeoffs made in an author’s note at the end. But at the same time, I wish I didn’t always have to explain myself." | BW | On translation choices in Messy Roots | Values disclosed trade-offs, and brevity | One compact "trade-offs and assumptions" note, not pages of caveats |

### 2d. Money, freedom, flexibility, success

| # | Exact text | Src | Context | Value | Implication |
|---|---|---|---|---|---|
| 34 | "Now I get to fit work around life instead of the other way around, which is such a game-changer" | IN | On full-time art | Autonomy | Flexibility is a core value, not just a case requirement (R-C58) |
| 35 | "knowing that I don't have to own anything or be tied to any material possessions" | MV (AI transcript) | Impact of travel | Travels light, stays flexible | She prefers optionality to ownership. It argues against committing "all remaining assets" to a building |
| 36 | "My advice is to avoid siloing yourself into an end-all-be-all career situation." | PQ | Advice on studying business | Keep options open | Same. It is diversification in life language |
| 37 | "I did 50 things, and maybe I didn’t like fully excel at each, but I got to try all of them" | OA | How she wants to look back at 80 | Breadth over one bet | Diversification is her own life philosophy. A broad index sleeve, not concentrated picks |
| 38 | "mainly because I’m so interested in them and I don’t want to pigeon-hole myself into one thing." | PS | On many projects | Same | Same |
| 39 | "it’s great having thousands of likes, but at the end of the day, it’s just a number." | OA | On online feedback | Meaning over metrics | Express results in what they secure (years of operations funded), not only dollars |
| 40 | "each has juggled passion against practicality, social pressure against personal identity, and countless bouts of career pivoting" | PQ | About the alumni The Sign.al profiled | Passion vs practicality balance | The case's "balance between pursuing growth and protecting the capital" (R-C38) in her own words |
| 41 | "Every character is grappling with how to balance society’s expectations with their own desires." | ND | Kirby's theme | Balance | Same. Balance as a stated rule, not a vibe |

### 2e. Taiwan, community, how she lives and works (professional-relevant only)

| # | Exact text | Src | Context | Value | Implication |
|---|---|---|---|---|---|
| 42 | "Taiwan is like one of my top places to live in and to travel to all time" | MV (AI transcript) | She lived mostly in Taipei while writing the second half of Messy Roots | Real connection to Taiwan | The residency location is plausible for her. The scenario is still fiction (R-W4); do not state her real plans |
| 43 | "Or there's also a little like some art residencies at the top of the mountains there." | MV (AI transcript) | Recommending Yilan, Taiwan | She knows Taiwanese art residencies | Rural vs city matters for which cost index (construction vs Taipei property) is relevant |
| 44 | "join a co living space even just for like a week or a month" | MV (AI transcript) | Her travel tip | Community through shared spaces | The residency model ("temporarily live, work, teach, and collaborate", R-C40) is how she herself finds community |
| 45 | "I visited and started making community there." | MV (AI transcript) | Co-living and co-working in Lisbon | Community | Same |
| 46 | "It's disheartening to know that all they know are the bad parts of it" | NPR | On headlines about Wuhan | Against one-sided risk stories | Taiwan risk must be framed completely, not as a flashpoint caricature |
| 47 | "focus on the full human story" | HUF | On how to discuss Wuhan | Complete picture | Same |
| 48 | "There wasn’t much that was incorrect as much as there just wasn’t any news about the overall picture of Wuhan outside of the coronavirus" | HUF | Same | She objects to *incomplete* framing more than errors | A section can be accurate and still fail her by being incomplete |

### 2f. Facts about her professional record (her own documents; VERIFIED-PRIMARY)

- "Trading Intern at Belvedere Trading in Chicago". She was also a "Policy Analyst Intern at Consumer Financial
  Protection Bureau". She was a "Mentor for Tech It Out Philly and MoneyThink, two organizations in which I taught web
  development and financial literacy to high school students in West Philadelphia." (PQ)
- "Bachelor of Science in Statistics and Information Decisions, Concentration in Product Design" (RES). Her own
  words in WM: "a degree in business analytics". PQ 2018: "Major: Economics with a concentration in Business
  Analytics". These are consistent with a Wharton BS in Economics with concentrations (ASSUMPTION; see Q05).
- "Experimented and shipped 10 features that resulted in +4.5M DAU" (RES, Twitter PM). She is an experimenter
  (A/B testing, SQL, R, Tableau).
- Speaking guide (SG):
  - "Rates will differ based on travel, length of event, and books purchased." "Pro-bono visits can be offered on
    need-basis."
  - "Previous talks: APAPI Author Talk with Asana, Doodle Therapy with Adobe, Drawing Your Life Workshop with Google
    LGBTQ+ Group".
  - Listed topic question: "What motivated you to quit a secure job to become an artist-writer in the middle of a
    pandemic?"
- HEY: she uses "she/her and they/them pronouns" (the SG says "she/they"). She signs off with "Let’s make something
  together."
- Her Kirby page (publisher copy on her site): "Once dubbed the Queen of Balance".
- "I’m taking a short break from writing to focus on teaching my Writing Comics course at California College of the
  Arts!" (ND, March 2025).
- DP 2019-03-17 (reporter): "her anti-resume includes receiving 33 job rejections". PS (reporter): "To destigmatize
  alternate career paths and normalize failure, Laura helped launch the Anti-Resume Project".

### 2g. Publishing timing evidence (VERIFIED-PRIMARY on the pages named)

| Book | Planned date | Source | Actual date | Source |
|---|---|---|---|---|
| *Messy Roots* | "Publication for the first book is planned for summer 2021" | Publishers Weekly Rights Report, week of July 20, 2020 | "On Sale: 3/8/2022" | BookWeb, 2022 |
| *Kirby* | "She’s hoping to finish in time for a 2024 release." | Inverse, 2022 | Published in 2025 | SG says "will be released in 2025"; search snippets give 4 March 2025 (SNIPPET-UNVERIFIED for the day) |

- The first book deal was "acquired, at auction" (PW).
- Book Riot (2024-01-12): "Laurel Public Schools (MT) school board just banned six books", *Messy Roots* among them
  (VERIFIED-PRIMARY for Book Riot's report). This closes the stakeholder map's open item SH-23 ("I have not verified
  whether any of Laura's titles were challenged"): one ban is now reported.

### 2h. Unverified or unattributed

| Text | Status | Note |
|---|---|---|
| "The only person who needs to believe in something is yourself." | **UNATTRIBUTED** | Case pull quote (R-C21). Not found in any source above. An exact-phrase WebSearch returned only generic motivational pages (SNIPPET). It could come from her books or a talk I could not read. Until found, it is the case's wording |
| "Laura Gao cares so passionately about making a difference…" | VERIFIED-PRIMARY | This is a Wharton staff member's recommendation on the PQ page, not her words. Do not attribute it to her |
| Belvedere Trading is an options market-making firm | ASSUMPTION (general knowledge) | Not checked on a primary page |

---

## 3. What her words say about her (values, decisions, risk)

**Values**, ranked by how often they recur across sources (my judgement; the quote numbers are the evidence):
1. **Build what is missing, with others** (#11, #13, #14, #44). She founds things: a club, a startup project, a
   festival, and in the case a residency.
2. **Purpose first; the medium is replaceable** (#22, #23, #39).
3. **Authenticity, no gimmicks** (#20, #21, #28; PQ "the Laura Gao I knew loved building apps, not excel models").
4. **Optionality and freedom** (#34-#38). She keeps options open and does not like being tied down.
5. **Honesty about failure and trade-offs** (#33; the anti-resume; "33 job rejections").
6. **Complete, fair stories about places and people** (#46-#48).
7. **Access and community** (#17, #18; pro-bono "on need-basis").

**How she decides (evidence-based pattern, INTERPRETATION):**
- She plans quietly first (#4).
- She commits when a concrete, funded opportunity appears (#5, #6).
- She starts small, ships to a deadline and iterates (#19, #26, #27, #31).
- She will scrap work that is not right (#20, #21).
- She uses data as proof inside a story (#24).
- She is an experimenter (A/B tests at Twitter).

**How she handles risk (INTERPRETATION):**
- High willingness, but she names the cost first (#1).
- She prepares for the worst case (#8).
- She anchors herself to purpose when things go badly (#9).
- Her "jumps" were cushioned by a signed contract and a community (MV: "with enough trust in people around me").
- This is "thoughtful risk" (R-C37) in her own life: **risk on top of a secured base**, not risk to the base.

**What she would find inauthentic (seed 34), from her own contrasts:**
- The "ideal Whartonite" voice she rejected: "excel models", "corporate coffee chats", peers asking "why aren't you
  going for McKinsey or Goldman Sachs" (PS, reporter quoting her).
- Hype ("novelty factor", #32).
- Gimmicks (#21).
- One-sided risk stories (#46).
- Numbers without human meaning (#39).
- Using her identity or book titles as decoration. This is the brief's tokenism rule, and it also fits #21.

**What would earn her trust (seed 32):**
- A purpose statement she could have written.
- Risk taken only where it cannot hurt the promise.
- Trade-offs disclosed briefly.
- Evidence shown, not asserted.
- An honest failure log.
- Room left for the project to grow.

**Which of her ideas our strategy already echoes (seed 33):**
- Lock-early = "secured base, then leap" (#4, #5).
- The growth sleeve = "take the jump" with money the promise does not need (#2).
- The broad index sleeve = "50 things" (#37).
- Flexibility after 2033 = "fit work around life" and not being tied down (#34, #35).
- The 2031 floor-plus-upside range = staged growth (#15, #16).

---

## 4. Questions already answered elsewhere (not re-asked)
Brief section 8 items 1-19 are not re-asked. Q02 adds **new evidence** for item 1 (lock-early). The new evidence is
her own decision pattern, not a model result. Q09 adds new evidence to the open wrong-way-risk item (brief section
9).

---

## 5. Questions (25), with reasoning

Format: question · anchor · hypothesis (a GUESS unless marked) · what changes · deliverables · domain · seed.

**Q01. Is the case pull quote Laura's own words, and how may the team use it?**
- Anchor: R-C21, R-AN30: "The only person who needs to believe in something is yourself." (no attribution line in
  the text layer).
- Hypothesis (guess): it is Wharton's framing, or a line from her books or a talk. It is not in 25 of her public
  sources (UNATTRIBUTED).
- Why it matters: if it is hers, the co-sponsor task reads as her own conviction being turned into public proof. If
  it is Wharton's, it is the case designer's theme.
- Her record in fact shows reliance on others: "with enough trust in people around me" (MV) and co-organised,
  partner-funded projects. So the quote may over-state her solo self-belief.
- Changes: every deliverable sentence that uses it says "the case profile highlights…", not "Laura says…". Remove any
  pitch that hangs on the quote.
- Deliverables: IPS, FR · D7 · seed 15.

**Q02. Does Laura's own leap (a tentative plan first, notice given only after the book deal was signed) show that her
"thoughtful risk" means risk on top of a secured base? And should the IPS describe her risk tolerance that way instead
of "high risk appetite, so more equity"?**
- Anchor: R-C37 ("willing to take thoughtful risks"), R-C38; quotes #1, #4, #5.
- Hypothesis (guess, strong): yes.
  - This is new evidence for brief section 8.1 (lock-early). It is Laura's revealed behaviour, not a simulation.
  - It also argues for the lower end of the open 50/60/70% sleeve-equity choice. Her risk appetite is spent on her
    career and the residency, and the median barely changes (F-4xx: $205k/$207k/$209k).
- Changes (sentence): the IPS risk sentence frames willingness vs capacity with this pattern.
- Changes (decision): the sleeve equity weight. Also one TN reflection could name the "secure first, then grow"
  logic.
- Deliverables: IPS, TN, FR · D6 · seed 33.

**Q03. Which parts of our plan would she call "gimmicks"?**
- Candidates: EWT/Taiwan tilt, "two-clock sleeve" labels, 200k-path Monte Carlo in the main text, thematic ETFs.
- Anchor: R-S24 ("clear and creative investment thesis"); quote #21 "No more gimmicks."
- Hypothesis (guess): a Taiwan equity tilt and any branded framework names fail her test. Plain names (the promise
  portfolio and the growth portfolio) pass.
- Changes (decision): keep or drop EWT (brief section 9) and branded labels, applied now in WInS. Also the complexity
  budget of the FR.
- Deliverables: WInS-now, IPS, FR · D9 · seed 34.

**Q04. Should the IPS open with a one-sentence purpose statement, and treat each security as a replaceable "medium"
(primary pick plus alternates) serving a fixed purpose?**
- Anchor: R-I9 ("What is the central idea behind your investment strategy?"), R-I14; quotes #22, #23.
- Hypothesis (guess): yes. It mirrors her craft habit and the IPS guide's focus on "strategy and decision-making
  framework … rather than describing individual investments" (R-I23).
- Changes (sentence order): the IPS opening. TN reflections name the purpose each trade serves.
- Deliverables: IPS, TN · D9 · seed 32.

**Q05. What is the right way to describe her quantitative background?**
- The sources differ: case/resume "Statistics & Information Decisions", her 2022 words "a degree in business
  analytics", PQ 2018 "Economics with a concentration in Business Analytics".
- Anchor: R-C12.
- Hypothesis (guess): all are consistent with a Wharton BS in Economics with concentrations. Use the case wording.
- The deeper point: she is a data *practitioner* (SQL, R, Tableau, A/B tests, "+4.5M DAU"). She will value testable
  claims and experiment-style evidence more than theory.
- Changes (sentence): "as a statistics graduate, Laura…" framing in the FR. Avoid over-claiming what her degree
  means.
- Deliverables: FR · D7 · seed null.

**Q06. What would a former financial-literacy teacher of high-schoolers (MoneyThink), consumer-protection intern (CFPB)
and trading intern (Belvedere) check first in a student plan?**
- Anchor: R-S25 ("presents recommendations that can earn her confidence"); R-W29 (CFA Asset Manager Code); BS-01
  (no fee assumption); PQ facts.
- Hypothesis (guess): fees and costs, conflicts, and whether a 16-year-old could explain every sentence.
- Changes (decision): add an explicit fee assumption (about $17k lower median surplus at 0.5%/yr, per BS-01) and a
  jargon ban list. Changes (number): the projections net of fees.
- Deliverables: IPS, FR · D8 · seed null.

**Q07. Which common student-pitch phrases sound like the "ideal Whartonite" voice she rejected, and should the team
ban them?**
- Examples: "maximise returns", "alpha", "conviction picks", "beat the market", "aggressive growth".
- Anchor: R-S28 ("an authentic team voice"); PQ "loved building apps, not excel models"; PS on "McKinsey or Goldman
  Sachs".
- Hypothesis (guess): yes. A short banned-phrases checklist for TN reflections and the pitch costs nothing and
  removes the most common authenticity failure.
- Changes (sentence): style checklist for all three deliverables.
- Deliverables: TN, IPS, FR · D9 · seed 34.

**Q08. Given two publication slips (about 9 and 12 months) and a 2025 "short break from writing", should the stress
tests include a 2028 deposit that arrives late (for example in 2029)? And what does lock-early do in that case?**
- Anchor: R-C27 ("She will contribute an additional $150,000 at the beginning of 2028, using earnings from
  publishing advances…"); BS-13; section 2g.
- Hypothesis (guess): the case says "will", so it is a sensitivity, not the base case.
  - Under lock-early, lateness only delays and shrinks the growth sleeve.
  - Exception: if rates fall before January 2027 and the ladder is topped up from the 2028 deposit, a late deposit
    leaves the top-up unfunded for a year. This is the brief section 9 joint-tail item.
- Changes (number): add a "deposit 12 months late" scenario. Changes (sentence): "timing of cash flows" assumption
  in the IPS/FR.
- Deliverables: IPS, FR · D3 · seed 16.

**Q09. Is Laura's 2028 income more exposed to political and budget cycles than to the stock market?**
- Evidence: corporate DEI/ERG talks at Asana, Adobe and Google; school visits; a 2024 school-board ban of *Messy
  Roots*.
- Anchor: R-C27; brief section 9 (wrong-way risk); SG "Previous talks…"; Book Riot 2024-01-12.
- Hypothesis (guess): partly. Her channels are sensitive to DEI rollbacks (2025 corporate cuts: SNIPPET-UNVERIFIED)
  and book challenges, which correlate only loosely with equities.
  - So an equity "media/publishing underweight" hedges little.
  - The real hedge is what we already do: the promise is independent of her income after January 2027.
- Changes (decision): drop the human-capital sector underweight as a trade (less complexity). Changes (sentence): the
  FR's human-capital paragraph names political/budget risk to the deposit.
- Deliverables: FR, IPS · D6 · seed 16.

**Q10. If the residency is rural (she recommends Yilan and its mountain art residencies), which inflation index should
the FR use for facility costs?**
- Anchor: R-C39 ("In 2033, Laura plans to establish a collaborative creative residency in Taiwan."); case p.4
  "effect of inflation on … facility costs"; F-508 (Taiwan construction cost index); quotes #42, #43.
- Hypothesis (guess): the national construction cost index (about 3.5%/yr since 2021, F-508) is the defensible
  choice, with a stated caveat.
  - The case does not give a location.
  - Her public words make a non-Taipei setting plausible, but R-W4 says the scenario is fictional. So the FR must
    not say where she will build.
- Changes (sentence): the facility-cost inflation assumption and its caveat.
- Deliverables: FR · D4 · seed 19.

**Q11. How should the FR and the co-sponsor draft describe Taiwan geopolitical risk?**
- The problem: her founding public work was a protest against reducing a place to its worst headline.
- Anchor: R-C72 (fundraising draft), R-S28 ("clearly and credibly"); quotes #46-#48.
- Hypothesis (guess): name the risks once and precisely: currency, construction costs, operational continuity. Say
  what the plan does about each, and keep the "full picture" (why Taiwan is a strong location).
  - A dramatic "invasion scenario" paragraph would read to her as the framing she fought.
  - Staying silent would fail "credibly".
- Changes (sentence): the Taiwan risk section's framing and length.
- Deliverables: FR · D4 · seed 19.

**Q12. Her institutions grow in stages after support is proven (Pride in Panels). Does that support describing the
2031 range as a bought floor plus an upside that grows with results?**
- Anchor: R-C68 ("Teams must recommend the dollar range Laura should communicate"), R-C71; quotes #15, #16.
- Hypothesis (guess): yes for the floor-plus-upside framing. But the case fixes the decision at "the beginning of
  2033" (R-C57), so any staging beyond 2033 is an FR suggestion only.
- Changes (sentence): the co-sponsor draft uses "a committed floor now; more as results come in", which is her own
  festival logic. Possible decision: whether to recommend part-payment of the facility contribution.
- Deliverables: FR · D5 · seed null.

**Q13. If the residency follows her free-access ethos (free festival; pro-bono visits "on need-basis"), program fees
will be small. Does that make the operating commitment and the post-2033 flexibility buffer more important?**
- Anchor: R-C44 ("Any remaining facility cost, and any operating support beyond Laura’s commitment, may come from
  co-sponsors, grants, collaborators, program fees…"); BS-17; quotes #17, #18.
- Hypothesis (guess, interpretation): yes. Operating money is the hardest to raise (BS-17), and a low-fee model
  reduces one listed source. That is one more reason to keep a real flexibility share.
- Changes (sentence): the flexibility purpose sentence. Changes (number): possibly the share of surplus kept (see
  Q14).
- Deliverables: FR · D5 · seed null.

**Q14. Her most consistent stated value is keeping options open. Should the recommended flexibility share of the
post-reserve surplus be higher than a typical team's, and by how much?**
- Evidence: "avoid siloing yourself", "don't have to own anything", "fit work around life".
- Anchor: R-C58 ("committing all remaining assets could limit her financial flexibility as the project develops"),
  R-C84; quotes #34-#36.
- Hypothesis (guess): keep roughly 25-40% of the post-reserve surplus uncommitted. The exact number should come from
  the contribution-rule simulation (B1a lead: gift = min(top, floor + s × (residual − floor))). Her values support a
  lower s (e.g. 0.6-0.7 rather than 1.0).
- Changes (number): the facility share parameter s and the kept-flexibility dollars.
- Deliverables: FR · D3 · seed 33.

**Q15. Should the team place a small first trade early and treat the Trading Notes as a dated experiment log
(hypothesis, test, refine)?**
- Her method: "start small and post", deadlines "finished or not", A/B testing.
- Anchor: R-C88 ("reflected, tested, or refined the team’s developing strategy"), R-T9, R-W82 ("at the time it is
  made"); quotes #26, #27.
- Hypothesis (guess): yes. The first ladder/duration trade early (after checking the position limit) gives a real
  note to refine later. Waiting for a perfect plan wastes the window (Sep 28-Nov 6).
- Changes (decision): timing and sizing of the first WInS trades. The note template gets a "what we are testing"
  line.
- Deliverables: WInS-now, TN · D10 · seed null.

**Q16. Would a candid "anti-resume" in the Articulation section earn more of her respect than a smooth success
story?**
- Content: last year's rule breach, rejected ideas, WInS mistakes.
- Anchor: R-S27 ("reflects meaningfully on the team's growth and response to challenges"), R-W83; DP 2019 ("33 job
  rejections"); PS on the Anti-Resume Project.
- Hypothesis (guess): yes, provided it is specific and shows what changed. She co-built a project to "normalize
  failure".
- Changes (sentence/decision): the FR Articulation structure. Possibly one TN reflection on a trade that did not work
  as intended.
- Deliverables: FR, TN · D7 · seed null.

**Q17. Should the team keep a dated decision diary from day 1 (trade notes plus a weekly log), as she kept a daily
comics diary, so the FR can show growth from primary records?**
- Why now: WInS notes cannot be edited.
- Anchor: R-T28 ("Include each Trading Note exactly as it appears in WInS."), R-W82; quote #30.
- Hypothesis (guess): yes. It is low cost and feeds Articulation (R-S27) with evidence rather than memory.
- Changes (decision): a process rule this week.
- Deliverables: WInS-now, TN, FR · D10 · seed null.

**Q18. Should the FR express results in what they secure (for example "all ten years of operating payments already
bought") next to dollars?**
- Anchor: R-S28 ("communicates Laura's potential facility contribution and investment uncertainty clearly and
  credibly"); BS-09; quote #39 "it's just a number".
- Hypothesis (guess): yes, as long as it stays inside the case. No residency budget or resident counts, because
  teams "are not expected to … develop a detailed business plan".
- Changes (sentence): headline metrics in the FR and the co-sponsor draft ("years of operations funded", funded
  ratio).
- Deliverables: FR · D9 · seed 32.

**Q19. How big should the trade-offs and assumptions disclosure be?**
- She wanted an author's note on trade-offs but also "wish I didn't always have to explain myself".
- Anchor: case p.4 ("Teams should identify and explain their assumptions…"), R-I31; quote #33.
- Hypothesis (guess): one compact, clearly labelled trade-offs box in the FR, and one sentence in the IPS. No pages
  of caveats.
- Changes (sentence/decision): FR structure and word budget.
- Deliverables: FR, IPS · D9 · seed null.

**Q20. She doubted her own launch hype at 19. Should the team state the growth sleeve's AI and mega-cap concentration
plainly and leave the choice to her, rather than tilt toward or away from AI?**
- Anchor: R-S24 ("appropriate diversification"); quote #32 "how long will this novelty factor last?"; seed 20.
- Hypothesis (guess): yes. Broad index, a plain disclosure of the concentration share, and no thematic AI fund.
- Changes (decision): no AI thematic ETF in WInS. Changes (sentence): one disclosure line in the FR.
- Deliverables: WInS-now, IPS, FR · D2 · seed 20.

**Q21. Which pronoun should the deliverables use?**
- Facts: her site lists "she/her and they/them"; the case uses "she".
- Anchor: R-C10 (case biography uses "she"); HEY page.
- Hypothesis (guess): use "she", consistently. It matches the case and one of her stated pronouns. Never mix within a
  document.
- Changes (sentence): the style-guide line. It is a small thing that careless teams get wrong.
- Deliverables: TN, IPS, FR · D9 · seed null.

**Q22. Would using her book titles as metaphors read as authentic or as decoration?**
- Examples: "strong foundations for messy roots", "lessons for falling".
- Anchor: R-S28 ("authentic team voice"); brief section 4 (tokenism rule); quote #21.
- Hypothesis (guess): decoration.
  - The prior team review suggested such frames. Her own "No more gimmicks" and the tokenism rule argue against
    puns in the pitch.
  - Echo her *principles* in plain words instead (secure first, then leap; start small).
- Changes (decision): drop book-title puns from the elevator pitch and headings.
- Deliverables: IPS, FR · D9 · seed 17.

**Q23. Does her own way of finding community (co-living and co-working spaces) support stating the case's
reserve-first order as a people-first design?**
- Anchor: R-C40 ("temporarily live, work, teach, and collaborate"), R-C50/R-C57 order; quotes #44, #45.
- Hypothesis (guess): yes. The operating money pays for the community; the building is the container. That makes
  the operations-first order read as hers, not only as a rule.
- Changes (sentence): the IPS protection principle.
- Deliverables: IPS, FR · D5 · seed 17.

**Q24. Should the IPS include one pre-committed "bad-year rule" tied to purpose, instead of generic "stay the course"
language?**
- Her coping habit: she kept a supporter's note "saved for every time I felt bad".
- Example rule: "if equities fall X%, we do nothing to the promise portfolio; we rebalance the sleeve at the next
  review".
- Anchor: R-I3 ("make disciplined decisions"), R-I13; quotes #8, #9.
- Hypothesis (guess): yes. One rule, one number, one reminder that the ten payments are already bought. That is her
  own pre-commitment style.
- Changes (sentence): the IPS decision rule. Changes (number): the rebalancing band (brief section 9 open item).
- Deliverables: IPS, FR · D6 · seed 27.

**Q25. How should the team handle conflicts between secondary sources about her?**
- Examples:
  - Kirkus places the comic after a March 2021 event, although the comic was posted in March 2020.
  - Some bios say she moved at four, Inverse says three.
  - The Maverick transcript link serves another episode.
  - A Wharton staff quote on the PQ page is easy to mistake for hers.
- Anchor: R-S25 ("demonstrates a thoughtful understanding of the client"); R-W30 (cite sources).
- Hypothesis (guess): cite only her own words or primary pages, and flag conflicts rather than pick silently. Client
  Knowledge is scored, and errors about the client are the cheapest way to lose her confidence.
- Changes (sentence): the FR's client section cites primary sources only.
- Deliverables: FR · D10 · seed null.

**Parked** (fail the "would change something" filter now):
- Her favourite books and travel lists.
- Her identity themes as investment screens (the tokenism rule; the case names no screens, brief section 8.19).
- Her real-life residence (privacy).
- Finale Q&A (out of scope).

---

## 6. Leads for the specialists (sources and facts to use)

- **D6 (client psychology):**
  - OA 2021 (#1-#3, #8, #9, #13, #37, #39) and IN 2022 (#4, #5, #34) are the core risk-pattern sources.
  - The MV transcript PDF (AI transcription) covers the leap decision, Taiwan and community.
  - Use these for Q02 and Q24. Behavioural terms to research: "regret minimisation", "pre-commitment devices",
    "mental accounting / goals-based buckets".
- **D3 (quant):**
  - Q08: add a "2028 deposit 12 months late" scenario and the joint tail "rates fall before Jan 2027 + late
    deposit".
  - Q14: run the contribution-rule s = 0.5/0.7/1.0 from B1a and report the kept-flexibility dollars.
  - Publication-slip evidence is in section 2g.
- **D5 (philanthropy):**
  - The Pride in Panels model: free event, library partner (SFPL Hormel Center), mini-grants to 20 creators,
    biennial, and expanded in 2026 (LNM 2026-02-12, VERIFIED-PRIMARY; 48hills.org 2026-02, same facts).
  - Use it for Q12, Q13 and Q23. Also research how small artist residencies fund operations with low fees.
- **D4 (Taiwan):**
  - MV transcript: she lived mostly in Taipei while writing, rode the northern and eastern Huandao, and recommends
    Yilan and its mountain art residencies.
  - Keep to cost and currency facts (F-508, F-510). Never state her real plans (R-W4).
  - Framing guidance for Q11: NPR 2020 and HuffPost 2020 quotes #46-#48.
- **D2 (equity):** Q20 hype scepticism (DP16 #32). Q09 says the human-capital sector underweight hedges little. Check
  the broad index's top-10 weight for the disclosure line.
- **D7 (Wharton intent):**
  - Q01: try to locate the pull quote in *Messy Roots* or *Kirby* text (library preview or Google Books search), or
    in a Wharton talk.
  - Wharton Magazine tag page https://magazine.wharton.upenn.edu/tag/laura-gao/ lists two items (2022-04-06
    interview; "Alumni Book Roundup: Spring 2022", 2022-05-03).
- **D8 (practice):** Q06. She has trading-floor, consumer-protection (CFPB) and financial-literacy teaching experience
  (PQ). Pair with the CFA Asset Manager Code F.2/F.4.d disclosures (stakeholder map W-1).
- **D9 (plain English):** Q07 banned-phrase list; Q21 pronoun; Q22 no book-title puns; Q19 one trade-offs box; Q04
  purpose-first opening.
- **D10 (compliance and process):**
  - Q15 early small first trade (after reading the Session Rules position limit); Q17 decision diary; Q25 source
    discipline.
  - Tooling: `fetch_text.py` returns 403 on poetsandquantsforundergrads.com with its Chrome user agent, and its
    HTMLParser drops the body text on that page. Suggested fix: retry with curl's default user agent, and fall back
    to regex tag stripping when the output is under ~20 lines.
- **Not read (retry if access widens):**
  - Diverse Books Q&A (captcha).
  - Ampersand Magazine 2021 profile (TLS error).
  - YouTube interview on the book ban (video).
  - Wainao video (Taiwan outlet).

---

## 7. Sources (all accessed 2026-09-27; status)

| Source | URL | Piece date | Status |
|---|---|---|---|
| Poets&Quants for Undergrads, 2018 Best & Brightest | https://poetsandquantsforundergrads.com/students/2018-best-brightest-laura-gao-wharton-school/ | 2018-03-30 | VERIFIED-PRIMARY (via ft2 fallback; see section 1) |
| Wharton Magazine interview | https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/ | 2022-04-06 | VERIFIED-PRIMARY |
| Overachiever Magazine interview | https://www.overachievermagazine.com/conversations/gskjklclyh93jwbb2809150ne9iyid | 2021-03-15 | VERIFIED-PRIMARY |
| Input/Inverse feature | https://nc.inverse.com/input/culture/laura-gao-messy-roots-viral-tweet-comic-graphic-novel | 2022-03-07 | VERIFIED-PRIMARY |
| Pulse Spikes profile | https://pulsespikes.org/story/laura-gao | 2021-06-18 | VERIFIED-PRIMARY |
| Maverick Show Ep 190 show notes | https://www.themaverickshow.com/podcast/190-messy-roots-queer-identity-the-beauty-of-wuhan-and-writing-a-graphic-memoir-while-traveling-the-world-with-laura-gao/ | 2022-06-23 | VERIFIED-PRIMARY |
| Maverick Show Ep 190 transcript (AI) | https://www.themaverickshow.com/wp-content/uploads/2025/10/190_Laura_Gao_Transcript.pdf | episode 2022-06-23 | VERIFIED-PRIMARY (machine transcript) |
| The Honey Pop interview | https://thehoneypop.com/2022/06/02/exclusive-interview-laura-gao-on-messy-roots-lgbtq-representation-and-more/ | 2022-06-02 | VERIFIED-PRIMARY |
| The Nerd Daily Q&A | https://thenerddaily.com/laura-gao-kirbys-lessons-for-falling-in-love-interview/ | 2025-03-08 | VERIFIED-PRIMARY |
| BookWeb Indies Introduce Q&A | https://www.bookweb.org/news/indies-introduce-qa-laura-gao-1627512 | 2022-02-07 | VERIFIED-PRIMARY |
| NPR "The Wuhan I Know" | https://www.npr.org/sections/goatsandsoda/2020/04/04/823825436/the-wuhan-i-know-a-comic-about-the-city-behind-the-coronavirus-headlines | 2020-04-04 | VERIFIED-PRIMARY |
| HuffPost | https://www.huffpost.com/entry/chinese-american-illustrator-life-in-wuhan_n_5ea9c739c5b63115cec2be5a | 2020-04-30 | VERIFIED-PRIMARY |
| Kirkus interview | https://www.kirkusreviews.com/news-and-features/articles/laura-gao-messy-roots-interview/ | 2022-03-06 (per Wikipedia citation; SNIPPET for the date) | VERIFIED-PRIMARY (read; mostly personal, not quoted) |
| Local News Matters, Pride in Panels 2026 | https://localnewsmatters.org/2026/02/12/sf-queer-comics-fest-expands-stays-free-in-second-year/ | 2026-02-12 | VERIFIED-PRIMARY |
| 48 Hills, Pride in Panels 2026 | https://48hills.org/2026/02/pride-in-panels-fest-inks-in-queer-comics-brilliance/ | 2026-02 | VERIFIED-PRIMARY (context only) |
| Daily Pennsylvanian Q&A (Draw Street Journal) | https://www.thedp.com/article/2016/01/draw-street-journal-q-and-a | 2016-01-28 | VERIFIED-PRIMARY |
| Daily Pennsylvanian, anti-resumes | https://www.thedp.com/article/2019/03/penn-anti-resume-ocr-recruiting-failure-signal | 2019-03-17 | VERIFIED-PRIMARY |
| 34th Street, The Signal | https://www.34st.com/article/2018/04/the-signal-penn-club-squirrels-without-morality-cards-against-humanity-pre-professional | 2018-04 | VERIFIED-PRIMARY (no Laura quote) |
| Publishers Weekly Rights Report | https://www.publishersweekly.com/pw/by-topic/childrens/childrens-book-news/article/83911-rights-report-week-of-july-20-2020.html | 2020-07-21 | VERIFIED-PRIMARY |
| Book Riot, book bans | https://bookriot.com/book-banning-will-not-stop-at-schools/ | 2024-01-12 | VERIFIED-PRIMARY (Book Riot's report) |
| lauragao.com: hey, projects, data-journalism, speaking-events, messyroots, kirby, editorial | https://lauragao.com/hey/ etc. | current | VERIFIED-PRIMARY |
| Publicity & Speaking Guide PDF | https://lauragao.com/s/Publicity-and-Speaking-Guide-Laura-Gao-e5n7.pdf | ~2024 (undated) | VERIFIED-PRIMARY |
| Resume PDF | https://lauragao.com/s/Laura-Gao-Resume.pdf | current (undated) | VERIFIED-PRIMARY |
| Wikipedia, Laura Gao | https://en.wikipedia.org/wiki/Laura_Gao | edited 2026-08-31 | Read; secondary; used only for citation dates |
| NüVoices #72 page | https://nuvoices.com/podcast/nuvoices-podcast-72-messy-roots-a-conversation-with-laura-gao | 2022-03-17 | Show notes only |
| Corporate DEI cuts 2025 (HR Dive, Forbes, etc.) | search results only | 2025 | SNIPPET-UNVERIFIED |
| Pull-quote exact-phrase search | WebSearch | - | SNIPPET: no match to Laura |
| Diverse Books Q&A | https://legacy.diversebooks.org/qa-with-laura-gao-messy-roots-a-graphic-memoir-of-a-wuhanese-american/ | - | BLOCKED (captcha) |
| Ampersand Magazine profile | https://ampersand-mag.com/laura-gao | 2021-03-04 (per Wikipedia) | BLOCKED (TLS) |

Verbatim checks: 68 phrases were checked; all returned `PHRASE FOUND VERBATIM: YES`. The list is in the scratchpad
file `B8a_quotes.tsv` (not in the repo). Section 2 holds every phrase used.

---

## What this teaches

A client's own words are data, but only if you check them. Three lessons came out of this lens:
- The most famous line in the case could not be traced to her, so it must be quoted as the case's words.
- A person's *story* ("she took a big risk") can hide their *behaviour* ("she took it after the contract was
  signed"). Behaviour is the better guide to what she will trust.
- The strongest client insight here is not a clever metaphor. It is noticing that the plan already works the way she
  has lived: secure the base, then leap; start small; keep options open; and tell the full story, including the
  trade-offs.
