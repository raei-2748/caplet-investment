# B3b Laura's World & Human Capital (starting angle: her books, her public values, and the income behind the 2028 deposit)

Agent B3b, insight_v1 run, Phase B. Written 2026-09-27. This is AI-generated research for Team Caplet and is not text
for submission. It generates questions. It does not answer them for the team, and it drafts no deliverable prose.

Privacy rule applied: this file uses only Laura Gao's public professional record: her books, publisher and review
copy, her website's professional pages, her résumé's work history, and press about her work. Several sources I opened
also contain family, relationship, name-history, contact and hobby details. I left all of them out on purpose. Nothing
here suggests contacting her (R-W55).

Relation to other Phase B files: B8a and B8b (Voice of Laura) already collected her own words on risk, gimmicks,
purpose statements, staged institution-building, late books and the unattributed pull quote. I do **not** re-ask
those questions. Where one of my questions touches theirs, I say what new evidence I bring. My lens starts from the
**books themselves** (what the publisher, reviewers and she say they are about) and from the **economics of the
income** that is meant to fund the $150,000 deposit in January 2028 (publishing contracts, advances, the classroom
and library channel, speaking, licensing, generative AI, and US-China tension).

---

## 0. Summary (read this first)

1. **The one market crash of her career coincided with her career's biggest boost.** "The Wuhan I Know" went viral in
   late March/April 2020 (NPR, 2020-04-04). The S&P 500 fell 33.9% from 19 Feb to 23 Mar 2020 (FRED, VERIFIED-PRIMARY).
   HarperCollins bought her first two books "at auction" in the week of 20 July 2020 (Publishers Weekly,
   VERIFIED-PRIMARY). North American comics and graphic-novel sales then rose from $1.1bn (2019) to $2.01bn (2022)
   (ICv2, VERIFIED-PRIMARY). So the simple story ("a crash also shrinks her advances") has one real counter-example.
   Her income is driven by events, publishing contracts and policy more than by the stock market. This bears directly
   on the open "wrong-way risk" item in brief section 9 (Q04).
2. **The 2020 two-book contract appears to be used up, so any "publishing advance" in January 2028 must come from a
   contract that is not public yet.** Publishers Weekly (2020) records "world English rights to debut YA graphic memoir
   The Wuhan I Know, plus a second graphic work … The second graphic work is about a queer girl's many loves". That
   description matches *Kirby's Lessons for Falling (in Love)* (HarperAlley, March 2025). Her résumé says she "wrote
   and illustrated two award-winning graphic novels" for HarperCollins. The Authors Guild's typical six-part advance
   schedule ends "12 months after publication", which for Kirby would be about March 2026 (ASSUMPTION: a generic
   schedule, not her contract). Implication: the deposit is **contract-cycle risk**, and the case's "will" (R-AN35)
   carries more hidden work than teams will notice (Q03). This adds new evidence to B8b Q13.
3. **The deposit sits in the right tail of author incomes.** $150,000 in one year is 6.0 times the 2022 median
   *combined* author income of full-time graphic novelists ($25,000; Authors Guild 2023 survey, VERIFIED-PRIMARY). The
   team must not doubt the client (the case says "will"). But it should know that any part of the *promise* that rests
   on the deposit rests on right-tail career success. That happens in exactly one place: the rule for "rates fall
   before January 2027 and the ladder costs more than $300k" (Q02).
4. **Her human capital has a tech leg, which is labour flexibility in the Bodie-Merton-Samuelson sense.** Her résumé
   lists "LG Studios | Freelance Product Designer, Author & Illustrator 2020 - Present". It also lists earlier work as
   a Twitter product manager and an Amazon data analyst. A client who can switch back to paid product work has more
   capacity to take risk with money the promise does not need (BMS 1992, VERIFIED-PRIMARY abstract). This is a
   Laura-specific input to the open sleeve equity weight (50/60/70%) (Q05).
5. **On AI she is not a simple "artist versus AI" story.** Her own studio's clients include "Retainit, AI-powered online
   learning software" (résumé, VERIFIED-PRIMARY). HarperCollins, her publisher, offers authors an opt-in AI-training
   licence of $5,000 per title, split 50-50 (Authors Guild, VERIFIED-PRIMARY). I found no public statement by her on
   generative AI. So any "AI hedge" story in the portfolio would be invented. AI exposure should be disclosed and left
   as her choice (Q09). A separate point teams will miss: **a client who is a professional illustrator should get a
   Final Report with no AI-generated images and no imitation of comic art** (Q10, Q11).
6. **Her classroom and library channel faces policy risk, and that risk is now documented on primary pages.** In 2025
   Executive Order 14238 directed the elimination of the Institute of Museum and Library Services (IMLS); a court
   reversed this in November 2025 (ALA, VERIFIED-PRIMARY). In June 2026 the FCC advanced a proposal asking whether
   E-Rate "should be terminated or limited to only rural areas" (ALA, VERIFIED-PRIMARY). A Montana school board banned
   *Messy Roots* in January 2024 (Book Riot, VERIFIED-PRIMARY). Both books are rated "Ages 14–up" (Publishers Weekly).
   These are risks to her income, **not** reasons to tilt any investment (Q06, Q20).
7. **Factual traps that most teams will fall into.**
   - (a) Linking her Wuhan birth to Taiwan ("returning to her roots"). The case never does this, and it is wrong (Q08).
   - (b) Inflating her accolades. Her own résumé gives the exact claims: "Debuted on #9 on Indies Bestsellers List"
     and "Finalist for Harvey Award, Goodreads Choice Awards, and California Booksellers Award" (Q14).
   - (c) Using 2026 news about her real career, such as her college "will close permanently in 2027" (The Art
     Newspaper), even though R-W4 says the scenario is fictional (Q15).
8. **What she would recognise as hers is a benefit, not a metaphor.** For a client who calls her own income "unstable"
   (Overachiever 2021, verified by B8a), the most personal thing our plan can offer is plain: **once the ladder is
   bought, her promise to the residency no longer depends on her next book deal, speaking season or licence** (Q01).
   Book-title puns and plot metaphors are optional at best (Q13).

Counts: 21 questions (section 3); 24 evidence items (section 2); 9 items parked as duplicates (section 4).

---

## 1. Method and source access

- Every web page was read with `.venv/bin/python research/insight_v1/scripts/fetch_text.py URL`. Quotes were checked
  with `--grep "phrase"` and returned `PHRASE FOUND VERBATIM: YES`. Access date for every source: **2026-09-27**
  (about 15:30-16:30 UTC).
- WebSearch was used three times and then hit the session's search budget (200 calls used by the run). After that I
  reached pages by known URLs, by links on pages already opened, and through the run's shared fetch cache
  (`/tmp/insight_v1_fetch_cache/`, pages other agents had already fetched).
- **Blocked or not found:**
  - search.books.com.tw and readmoo.com (Taiwan bookstores): HTTP 403. I could not check whether a Traditional
    Chinese (Taiwan) edition of her books exists.
  - Open Library lists English editions only for both books (a check, not proof).
  - Google Books API: no result.
  - No 2024-2026 ICv2 market-size page was reachable without search. The latest verified figure is for 2023.
  - Corporate DEI and heritage-month speaking cuts in 2025: no primary page read (SNIPPET-UNVERIFIED lead only).
  - PEN America's ban index: not reached (search budget).
  - No public statement by Laura about generative AI was found in the ~40 cached pages about her. Absence of evidence
    is not evidence.
- **Anomaly:** Wikipedia's *Messy Roots* article says she made the comic "In 2021 … as a response to … the 2021
  Atlanta spa shootings". The case (R-C13: "In 2020") and NPR (2020-04-04) date the comic to 2020. The Wikipedia
  sentence is wrong on the year. Do not cite Wikipedia for dates.

---

## 2. Evidence found (E-ids used in the questions)

Status: VP = VERIFIED-PRIMARY (read on the page, phrase verified); VRF = VERIFIED-REPO-FILE; SU = SNIPPET-UNVERIFIED;
ASM = ASSUMPTION; DER = derived arithmetic.

### 2a. The books (what they are, who they are for)

| E | Fact (exact words where quoted) | Source | Status |
|---|---|---|---|
| E01 | *Messy Roots: A Graphic Memoir of a Wuhanese American*, "HarperCollins/Balzer + Bray, $22.99 (272p)"; "Ages 14–up"; review opens "In this fresh, frank, and tender debut"; closes "A multidimensional, thoroughly entertaining account of growing into queer Asian American identity." Reviewed 2022-01-06 | publishersweekly.com/9780063067769 | VP |
| E02 | *Kirby's Lessons for Falling (in Love)*: "Laura Gao. HarperAlley, $26.99 (304p) … $18.99 paper"; "Ages 14–up"; plot: a competitive climber whose "dynamic move at the Texas Youth Fall Invitational goes awry", who must do another activity while her arm heals so she can still reach a university climbing team; the review praises Gao for "delicately balancing the pros and cons of Kirby's close-knit Christian immigrant community". Reviewed 2024-12-12; published March 2025 | publishersweekly.com/9780063067806 | VP |
| E03 | Her site's Kirby page: "Once dubbed the Queen of Balance as her school's top rock climber, Kirby Tan suffers an injury that sidelines her for the rest of the season." Kirkus line on the page: "A refreshingly raw and vulnerable exploration of grief and hope." | lauragao.com/kirbys-lessons-for-falling-in-love | VP (publisher and review copy, not her voice) |
| E04 | *Messy Roots* page: "3 starred reviews · 12+ awards & honors"; SLJ: "lifts the story of Wuhan beyond COVID". Her Educators guide lists accolades including "GOLDEN POPPY AWARD WINNER", "CYBIL AWARD WINNER", "HARVEY AWARDS FINALIST", "GOODREADS CHOICE AWARDS FINALIST", "NYPL BEST BOOKS OF 2022" | lauragao.com/messyroots/ ; lauragao.com/s/Educators-Book-Clubs-Guide-Messy-Roots-klc2.pdf | VP |
| E05 | Her résumé: "Debuted on #9 on Indies Bestsellers List, and featured on NPR and New York Times"; "Finalist for Harvey Award, Goodreads Choice Awards, and California Booksellers Award". Her /hey page: "A Harvey and Goodreads Choice Award honoree" | lauragao.com/s/Laura-Gao-Resume.pdf ; lauragao.com/hey | VP |
| E06 | Her Educators guide (her note): the activities "exercise students’ creativity in less daunting ways than traditional essay writing" | Educators guide PDF | VP |
| E07 | Horn Book (as quoted by Wikipedia): "Gao personalizes her experiences with insight and humor"; "candid depiction of the universal search for one’s place in the world" | en.wikipedia.org/wiki/Messy_Roots | Wikipedia page VP; Horn Book original SU |
| E08 | "It's not published in Mandarin" (her answer, NPR 2022-04-24, on whether the book reached China; she adds she is unsure it ever will be, because of censorship rules on LGBTQ content: paraphrase of the same answer) | npr.org/sections/goatsandsoda/2022/04/24/1093992912/… | VP (first sentence); rest PARAPHRASE of a VP page |

### 2b. The contract and income economics

| E | Fact | Source | Status |
|---|---|---|---|
| E09 | "Donna Bray at HarperCollins/Balzer + Bray has acquired, at auction, world English rights to debut YA graphic memoir The Wuhan I Know, plus a second graphic work, by Laura Gao." "The second graphic work is about a queer girl's many loves." (Rights Report, week of 20 July 2020) | publishersweekly.com/…/83911-rights-report-week-of-july-20-2020.html | VP |
| E10 | Résumé: "HarperCollins, wrote and illustrated two award-winning graphic novels" | Résumé PDF | VP |
| E11 | Authors Guild (2021-07-20): advances are paid "in three, and even up to six, installments"; a common six-part payout is "on signing the contract, three to six months after contract signing, on delivery of the manuscript, on acceptance of the manuscript, upon publication date, and one part 12 months after publication" | authorsguild.org/blog/everything-you-need-to-know-about-book-advances/ | VP |
| E12 | Authors Guild 2023 survey (2022 incomes, full-time authors): "Graphic novelists ranked second, earning a median book income of $15,000 and a combined income of $25,000 when including other author-related income." Also: "most authors are earning half of their writing-related income from sources other than their books." | authorsguild.org/news/key-takeaways-from-2023-author-income-survey/ | VP |
| E13 | $150,000 ÷ $25,000 = **6.0x** the median combined income of a full-time graphic novelist | E12 + case R-C27 | DER |
| E14 | ICv2 (2024-07-15): U.S./Canada comics and graphic-novel sales "around $1.87 billion in 2023, down 7% from $2.01 billion in 2022"; 2019 "when sales were $1.1 billion". The Covid surge "crested in 2022" | icv2.com/print/article/57351 | VP |
| E15 | S&P 500: 3,386.15 (2020-02-19) → 2,237.40 (2020-03-23) = **-33.9%**; 3,257.30 on 2020-07-21 (the week of her deal), -3.8% from the peak | fred.stlouisfed.org SP500 CSV | VP (DER for the %) |
| E16 | Résumé: "LG Studios | Freelance Product Designer, Author & Illustrator 2020 - Present"; "Founded professional studio for product design and illustration work"; "Clients include: Retainit, AI-powered online learning software". Earlier: Twitter product manager 2018-2020; Amazon data analyst 2017 | Résumé PDF | VP |
| E17 | Her /projects page lists game, CRM and UI/UX work (e.g. "UI/UX work for a retail media adtech company"); her site sells prints and has a "Visual Data Stories" section | lauragao.com/projects ; lauragao.com | VP |
| E18 | Bodie, Merton & Samuelson (1992): "The ability to vary labor supply ex post induces the individual to assume greater risks in his investment portfolio ex ante." | nber.org/papers/w3954 | VP (abstract) |
| E19 | CFA Institute Research Foundation, *Lifetime Financial Advice: Human Capital, Asset Allocation, and Insurance* (2007): individuals "must take into account human capital" when setting asset allocation | rpc.cfainstitute.org/research/foundation/2007/lifetime-financial-advice-human-capital-asset-allocation-and-insurance | VP (summary page) |

### 2c. Channel and policy risks (to income, never to investment choice)

| E | Fact | Source | Status |
|---|---|---|---|
| E20 | ALA (Dec 2025): "On March 14, President Trump issued Executive Order 14238, which directed the elimination of the agency" (IMLS). Grants were reinstated after a 21 Nov 2025 court ruling. ALA news list, 2026-06-25: the FCC advanced a proposal that "asks whether the E-Rate program should be terminated or limited to only rural areas" | ala.org/news/2025/12/ala-welcomes-reinstatement-all-federal-imls-grants-libraries | VP |
| E21 | Book Riot (2024-01-12): "Laurel Public Schools (MT) school board just banned six books", including *Messy Roots* | bookriot.com/book-banning-will-not-stop-at-schools/ | VP (Book Riot's report) |
| E22 | ALA: 4,235 unique titles challenged in 2025 (via stakeholder map SH-23) | A3 stakeholder map, W-9 | VP (by A3) |
| E23 | Authors Guild (2024-11-19): "The HarperCollins licensing deal provides for a $5,000 fee per title, which will be split 50-50 between an author who chooses to participate and HarperCollins." It covers nonfiction titles and is opt-in | authorsguild.org/news/harpercollins-ai-licensing-deal/ | VP |
| E24 | The Art Newspaper (2026-01-13): California College of the Arts "will close permanently in 2027"; her /hey page says she is "a Professor of Comics at California College of the Arts" | theartnewspaper.com/2026/01/13/california-college-arts-closing-vanderbilt-university-takeover ; lauragao.com/hey | VP. **For team awareness only. See Q15: do not use in deliverables.** |

Already verified by B8a/B8b and relied on here: "unstable income" (Overachiever 2021); "No more gimmicks." (Nerd
Daily 2025); "I’m taking a short break from writing" (Nerd Daily 2025); Messy Roots planned for "summer 2021" but
published 8 March 2022; past talks at corporate heritage and employee-group events (her speaking guide).

---

## 3. Questions (21), with reasoning

Format: question · anchors · anchor quote · hypothesis (a GUESS unless it cites evidence) · what would change ·
deliverables · domain · seed · north star. Ranked by deadline tier, then impact.

### Tier 1 and 2 (WInS now, Trading Notes, IPS)

**Q01. Should the IPS name, as the client benefit, that from the Treasury purchase onward her ten-year promise stops
depending on her own future earnings (book deals, speaking, licensing)?**
- Anchors: R-C27, R-C33, R-C38, R-S25, SH-01, BS-03.
- Anchor quote: "she wants her investment team to recommend an appropriate balance between pursuing growth and
  protecting the capital required for her goals" (case p.2).
- Hypothesis (guess):
  - Yes. It is the most Laura-specific benefit available, and it needs no metaphor.
  - Her income is event-driven and contract-driven (E09-E14). She has called it "unstable" (B8a #1).
  - Most teams will describe safety as "low volatility". Ours can describe it as **independence from her career's ups
    and downs**.
  - That independence is complete in January 2027 if the ladder costs ≤ $300k. It is complete in January 2028 if a
    top-up is needed (see Q02).
- Would change: a sentence. It sets what the pitch and the IPS's opening must contain (the team writes it).
- Deliverables: IPS, FR, TN (the first Treasury note's "why"). Domain: D9. Seed: 33.
- North star: she chooses the firm whose plan makes her dream stop depending on her next good year.

**Q02. If rates fall before January 2027 and the ladder costs more than $300k, how much of the promise may rest on the
2028 deposit? Should the IPS rule say so in one line?**
- Anchors: R-C27, R-C47 (portfolio-funded "with a high degree of certainty"), R-AN35, brief section 9 (joint tail),
  F-111.
- Anchor quote: "All ten payments must be funded by the investment portfolio with a high degree of certainty."
- New evidence: the deposit is right-tail income (E13: 6.0x the median) and depends on a contract that is not yet
  public (E09-E11).
- Hypothesis (guess, DER from brief section 6):
  - At -50bp the gap is $7,135 (4.8% of the deposit). At -100bp it is $22,864 (15.2%). P(cost > $300k) is about 24%
    (Phase A, ASSUMPTION model).
  - Relying on a deposit the case says "will" arrive is allowed.
  - A statistics-trained client would still want the dependency named: "up to $X of the promise waits for the 2028
    deposit; if it is late, [rule]".
  - Candidate rules for D1/D3 to compare:
    - (a) long rungs first; the gap sits in the 2033 rung, the least rate-sensitive, and the deposit fills it;
    - (b) also hold the gap as a T-bill "pending" line;
    - (c) accept it and state it.
- Would change: a decision (the January 2027 rule) and a number (maximum dependence in $ and %).
- Deliverables: IPS, FR. Domain: D1. Seed: 16.
- North star: we say exactly how much of her promise rests on her own career, and for how long. That is usually zero,
  and never unstated.

**Q03. Is the HarperCollins two-book contract of 2020 fully delivered and paid? If so, should the team's labelled
stress case treat the "publishing advances" part of the 2028 deposit as uncontracted, and size a "late" case and a
"smaller" case on that basis?**
- Anchors: R-C27, R-AN35, BS-13, SH-21.
- Anchor quote: "She will contribute an additional $150,000 at the beginning of 2028, using earnings from publishing
  advances, speaking engagements, licensing, and other entrepreneurial ventures."
- New evidence beyond B8b Q13:
  - The 2020 deal was for "The Wuhan I Know, plus a second graphic work … about a queer girl's many loves" (E09).
  - Her résumé counts "two" HarperCollins novels (E10). Kirby came out March 2025 (E02).
  - A typical last instalment is "12 months after publication" (E11), i.e. about March 2026 (ASM).
- Hypothesis (guess):
  - Yes, as a *labelled* scenario only. The case base ($150k, Jan 2028) is unchanged.
  - A new deal signed in 2026-27 would pay only its signing instalment(s) by January 2028. Those are small shares of
    a six-part advance.
  - So "late" (12 months) and "smaller" ($75k) are equally reasonable, and both are already in the model.
  - This evidence justifies them in the FR without guessing at her private finances.
- Would change: a sentence (the FR's justification for the stress cases). Possibly a number (the weight given to the
  "late" case).
- Deliverables: FR. Domain: D6. Seed: 16.
- North star: our stress tests come from how her industry pays, not from generic shocks.

**Q04. Given that her career's biggest boost came during the 2020 crash, what correlation between the 2028 deposit
and 2027 equity returns should the model assume? Should the FR state it as an explicit assumption?**
- Anchors: R-C85 ("timing of cash flows, outside funding"), R-C86, brief sections 9 and 11 ("2028 deposit independent
  of markets").
- Anchor quote: "They should also consider how favorable and unfavorable investment outcomes would affect their
  recommendations."
- New evidence:
  - E15 (-33.9% crash, Feb-Mar 2020) came at the same time as the viral comic and the July 2020 auction deal (E09).
  - The comics market grew +83% from 2019 to 2022 (E14, DER).
  - Books are low-price goods ($18.99-$26.99, E01/E02).
  - Advances are paid on contract milestones (E11), and school and library budgets are set by policy (E20).
- Hypothesis (guess):
  - The correlation is close to zero, and the sign is uncertain.
  - The real joint tail is a *policy or contract-cycle* shock (a missing deal, cuts to school and library budgets,
    fewer corporate heritage-month events), not a 2027 equity crash.
  - Keep zero as the base, with a +0.3 stress (ASM) to show the plan survives it. Under lock-early it does, by
    construction, once the ladder is bought.
  - This probably closes the open "wrong-way risk" item with one sentence and no extra model.
- Would change: a number (the correlation input in D3's model) and a sentence (FR assumptions list).
- Deliverables: FR, IPS (assumptions line). Domain: D6 (with D3). Seed: 16.
- North star: we tested the risk that is actually hers, not a textbook one.

**Q05. Does her human capital argue for the low or the high end of the growth-sleeve equity weight (50/60/70%)?**
- Anchors: brief section 9 (sleeve weight open), R-C37, R-C38, R-AN16, R-S25 ("risk considerations").
- Anchor quote: "Although she has been willing to take thoughtful risks throughout her entrepreneurial career".
- Evidence: two forces pull in opposite directions.
  - Towards **more** equity: labour flexibility (E18). She has a working product-design studio and a PM/data-analyst
    record (E16, E17).
  - Towards **less** equity: lumpy, contract-driven creative income (E11-E14). Human capital belongs in asset
    allocation (E19).
- Hypothesis (guess):
  - The promise is locked and living costs sit outside the portfolio (R-C33). So the sleeve is "surplus" money, and
    labour flexibility dominates.
  - That supports 60% or a little higher, never lower for human-capital reasons.
  - The sleeve weight barely moves the median (brief 8.5), so this is a *reasoning* gain more than a number gain.
- Would change: a decision (the weight, or at least the reason the IPS gives for it).
- Deliverables: IPS, FR. Domain: D6 (D8 to benchmark). Seed: 16.
- North star: the risk level is set by who she is professionally (a flexible, multi-skilled founder), not by an age or
  a quiz.

**Q06. Should the WInS portfolio carry any tilt meant to "hedge" her human capital (e.g. underweighting media and
publishing stocks such as HarperCollins's parent, News Corp)? Or should that idea be dropped now?**
- Anchors: brief section 9 ("human-capital underweight of publishing/media"), R-S24 ("appropriate diversification"),
  G-ids in the WInS guardrails (compliance first).
- Anchor quote: "uses appropriate diversification; and maintains consistency with the team's IPS" (SMApply
  criterion 1).
- Hypothesis (guess): drop it.
  - Her income drivers are contracts, policy (E20-E22), and events such as corporate heritage-month bookings (SU).
    None of these is well tracked by any listed stock.
  - Publishing is a tiny share of broad indices. HarperCollins is only one division of News Corp (general knowledge,
    ASM).
  - A tilt adds a trade, a commission ($25, F-607) and an explanation, and it hedges almost nothing. That fails
    "complexity must earn its place".
  - The hedge that works is structural: the promise is locked (Q01).
- Would change: a decision (no human-capital sector tilt in WInS; one FR line explaining why).
- Deliverables: WInS-now, IPS, FR. Domain: D2. Seed: 16.
- North star: we considered her career risk and chose the simplest hedge that actually works.

**Q07. Is a US-China/Taiwan crisis the one scenario that hits her promise, facility, residency and income at the same
time? Should the FR name it as the single "correlated" scenario, while keeping the direction of the income effect
honest?**
- Anchors: R-C39, R-C58, R-C86, brief section 9, seed 24.
- Anchor quote: "In 2033, Laura plans to establish a collaborative creative residency in Taiwan."
- Evidence:
  - Her books are English-only: "It's not published in Mandarin" (E08). World English rights only (E09).
  - Her subject matter is China, Wuhan and the diaspora (E01).
  - The residency is in Taiwan (case).
  - Broad U.S. equity indices depend on Taiwan-made chips (D2 to verify).
  - Her 2020 surge came *during* a spike in anti-Asian sentiment (R-C14), so her income may **rise**, not fall, in a
    crisis.
- Hypothesis (guess):
  - Yes. One named scenario: equities fall, the TWD moves, residency operations are disrupted, and the facility range
    is cut.
  - The Treasury-locked promise is unaffected (it is in USD, paid by the U.S. Treasury).
  - Her income effect is "uncertain in sign" (E15 precedent).
  - One scenario beats five generic shocks.
- Would change: a sentence (FR scenario list and co-sponsor draft content spec). Possibly a decision (whether the
  facility range carries a "location contingency" clause).
- Deliverables: FR. Domain: D4. Seed: 19.
- North star: we found the one risk that links all her goals and showed the promise survives it.

**Q08. How do we make sure no deliverable links her Wuhan birth to the Taiwan location (e.g. "returning to her
roots"), which would be a factual error and politically loaded?**
- Anchors: R-C10, R-C39, brief 8.19 (residency ≠ her home), R-S28 ("clearly and credibly").
- Anchor quote: "Born in Wuhan, China, and raised in Texas" (case p.1).
- Hypothesis (guess):
  - This is a high-frequency error among rival teams (ASM).
  - The case gives no reason for Taiwan. Her public professional link is only that she has lived and worked there
    (B8a #42, AI transcript).
  - Treat "China ≠ Taiwan; Wuhan ≠ Taiwan" as a checklist item, and never explain the location choice on her behalf.
- Would change: a sentence (checklist rule for all deliverables).
- Deliverables: TN, IPS, FR. Domain: D9 (D4 to confirm wording). Seed: 19.
- North star: the client who fought a one-sided story about her hometown will notice a careless one about Taiwan.

**Q09. Should the team reject any "AI hedge" argument (holding AI-heavy stocks to offset AI's threat to her career),
disclose the index's AI concentration plainly, and leave any AI tilt as her choice?**
- Anchors: seed 20, R-S24, R-C18, B8a Q20 (disclosure).
- Anchor quote: "she has combined artistic passion with strategic thinking and a willingness to pursue unconventional
  opportunities" (case p.1).
- New evidence beyond B8a Q20:
  - She designs *for* an AI-powered learning company (E16).
  - Her publisher offers an opt-in AI-training licence, author's share $2,500 per nonfiction title (E23). *Kirby* is
    fiction; whether *Messy Roots* qualifies is unknown and none of our business.
  - Her main income channels (in-person speaking, school visits, teaching, festivals, human-authored books) are
    among the least AI-substitutable (ASM).
  - No public statement by her on generative AI was found.
- Hypothesis (guess):
  - Yes, reject the hedge story. It would attribute a view to her that she has not stated, and it is weak economics.
  - Keep the broad index. State the concentration once. No thematic AI fund in WInS.
- Would change: a decision (no AI tilt either way; no "AI hedge" wording) and a sentence (FR disclosure).
- Deliverables: WInS-now, IPS, FR. Domain: D2. Seed: 20.
- North star: we did not put words in her mouth about AI. We showed the facts and left the choice with her.

**Q10. Given that she is a professional illustrator and her industry body calls unlicensed AI training "flagrant
theft", should the team commit to no AI-generated images in any deliverable, and to a specific AI-use log in the
Works Cited?**
- Anchors: R-W46, R-W47, R-S27, R-S28 ("authentic team voice"), E23.
- Anchor quote: "If you use AI to assist you in any way during the competition, how you use it must be recorded in
  your Works Cited pages."
- Evidence: the Authors Guild page (E23, VP) says "AI companies’ ongoing, flagrant theft of books and journalism".
  The comics community is openly hostile to generative AI art (Broken Frontier series title, SU).
- Hypothesis (guess):
  - Yes. Many teams will decorate a Final Report with an AI "residency in Taiwan" image or a cartoon of Laura. For
    this client that is the single most self-defeating visual choice.
  - The AI log should say what AI did (research help, fact-checking) and did not do (no text, no images).
- Would change: a decision (a no-AI-images rule for the FR, and the content spec of the AI log).
- Deliverables: FR (TN and IPS have no images). Domain: D10. Seed: 20.
- North star: we respected her craft in how we made the report, not only in what it says.

**Q11. Should the Final Report avoid imitating comic style (panels, speech bubbles, drawn characters) and instead meet
the standard of her own "Visual Data Stories": a few clean, honest charts?**
- Anchors: R-S28 ("uses data effectively"), R-C12, SH-04, E17.
- Anchor quote: "Presents a compelling, well-organized narrative in an authentic team voice; uses data effectively to
  support conclusions" (SMApply criterion 5).
- Hypothesis (guess):
  - Yes. Comic-style layouts imitate her professional craft (a tokenism and quality risk). Her data-journalism
    section and statistics degree set the relevant bar.
  - Two or three charts, each proving one claim (payments covered; the 2031 range with both tails; the flexibility
    buffer).
- Would change: a decision (the FR's visual style) and chart specs.
- Deliverables: FR. Domain: D9. Seed: 34.
- North star: we meet her as a data storyteller, not as a cartoon.

### Tier 3 (Final Report and co-sponsor materials), plus team-wide writing rules

**Q12. Should the team adopt a written "swap test" for every Laura-specific sentence? The test: keep it only if it
depends on her professional record (statistics degree, event-driven income, institution-building, public credibility);
cut it if it works only because of her ethnicity, sexuality or birthplace.**
- Anchors: brief section 4 (tokenism), R-C10, R-S25 ("thoughtful understanding of the client").
- Anchor quote: "whose work explores identity, belonging, and the power of storytelling" (case p.1).
- Hypothesis (guess):
  - Yes. It is a one-line, checkable rule that turns "no tokenism" into practice.
  - Most personalisation that survives is about **how she earns, decides and communicates**, not who she is.
- Would change: a decision (a checklist item applied to TN, IPS and FR drafts).
- Deliverables: TN, IPS, FR. Domain: D9 (D6). Seed: 34.
- North star: personal without being tokenistic. That line decides whether she feels understood or used.

**Q13. Is there one principle drawn from her books' *plots* (not their titles) that maps onto a real mechanism in our
plan? If there is, where, if anywhere, may it appear?**
- Anchors: seed 17, R-C9 ("stories have the power…"), B8a Q22 and B8b Q17 (titles and identity quotes as metaphors).
- Anchor quote: "Laura Gao believes stories have the power to change how people see the world."
- New evidence (plot level, E02/E03):
  - Kirby, dubbed the "Queen of Balance", falls, is sidelined, and keeps her goal by taking a different route while
    she heals.
  - *Messy Roots* "lifts the story of Wuhan beyond COVID" (E04): the full story rather than the headline.
- Hypothesis (guess):
  - "Keep the goal, change the route after a fall" matches our pre-committed contingency rules (rates fall before
    2027; a late deposit; a bad sleeve year).
  - At most one mention, in the FR's Articulation section. Never in the IPS.
  - Probably better left out entirely. She scrapped drafts for being gimmicky (B8b). The plan should *be*
    goal-fixed/route-flexible, not *say* so.
- Would change: a decision (use or drop the metaphor).
- Deliverables: FR. Domain: D9. Seed: 17.
- North star: if she recognises her book in our plan, it should be because of how the plan behaves, not a pun.

**Q14. Which exact words may the deliverables use about her books and honours, so that nothing is overstated?**
- Anchors: R-C10, R-C15 ("bestselling"), R-W28 (no lying), CFA Code F.2 (SH-25), SH-03.
- Anchor quote: "a bestselling graphic novelist, illustrator, entrepreneur, and educator" (case p.1).
- Evidence: E04/E05.
  - Her own résumé says "#9 on Indies Bestsellers List" (not the New York Times list).
  - She was a *finalist* for the Harvey and Goodreads Choice awards. "Award-winning" is supported by the Golden Poppy
    and Cybils wins.
- Hypothesis (guess): use the case's words ("bestselling") and at most her own verified phrasings. Never write "New
  York Times bestselling" or "Harvey Award winner".
- Would change: a sentence (bio line in the FR and co-sponsor draft).
- Deliverables: FR. Domain: D9 (D10). Seed: 33.
- North star: accuracy about her is the first test of whether our numbers can be trusted.

**Q15. How much real 2025-26 news about her career may the FR use, given that "the financial scenario is developed
specifically for the competition"? Examples: no announced next book; a 2025 writing break; her college closing in
2027.**
- Anchors: R-W4, R-W5 ("their own research"), R-AN35, brief privacy rule.
- Anchor quote: "While the client is real, the financial scenario is developed specifically for the competition."
- Hypothesis (guess):
  - Use such facts only to *motivate* labelled, generic stress cases ("publishing timelines slip; author income is
    lumpy"), citing industry sources (E11-E14).
  - Never state or imply anything about her current employment or finances. So E24 (her college's closure) should
    not appear in any deliverable.
  - Rewarded research is research into her public work and industry, not into her circumstances.
- Would change: a decision (the boundary rule) and sentences (how the stress cases are justified).
- Deliverables: FR. Domain: D10. Seed: null.
- North star: deep research that never becomes intrusive, which is what a real adviser would do.

**Q16. Should the co-sponsor draft carry one line on what the range is NOT (not a pledge of the top figure, not an
estimate of facility cost, not a promise in NT$)? This applies her founding principle of pre-empting misreading.**
- Anchors: R-C14 ("a response to misinformation"), R-C66, R-C72, R-S28, BS-04.
- Anchor quote: "If Laura promises more than she can ultimately contribute, she could damage her credibility".
- Hypothesis (guess):
  - Yes, one line. Her first public work was built to correct a misreading. The main credibility risk in 2031 is
    that a co-sponsor reads the top of the range as a pledge.
  - Pre-empting that protects both the fundraising and her reputation, and her reputation is her income (BS-03).
- Would change: a sentence (content spec for the fundraising draft).
- Deliverables: FR. Domain: D5 (D9). Seed: 33.
- North star: her credibility is protected in the exact way she protected her hometown's story.

**Q17. What readability level should the IPS and FR target, given that her books are rated "Ages 14–up" and she
designs teaching material to be "less daunting" than essays?**
- Anchors: R-C16 ("read in classrooms around the world"), R-S28, E01, E02, E06.
- Anchor quote: "Today, her books are read in classrooms around the world".
- Hypothesis (guess):
  - Aim for about a 14-16-year-old reader (roughly U.S. grade 9-10) for narrative text, with each technical term
    defined once.
  - The team is her books' own readership. Writing so a classmate could follow is authentic, and it is her standard.
  - D9 to pick a measurable target, e.g. a Flesch-Kincaid grade ≤ 10 for non-technical paragraphs (ASM).
- Would change: a number (the readability target) and a checklist item.
- Deliverables: TN, IPS, FR. Domain: D9. Seed: 34.
- North star: she writes for teenagers. A plan a teenager can follow is a plan she can trust.

**Q18. Should the FR avoid naming her "continued business income" as the backstop for facility overruns, and size
the flexibility buffer without counting on it?**
- Anchors: R-C44, R-AN24, R-C58, SH-26.
- Anchor quote: "Any remaining facility cost, and any operating support beyond Laura’s commitment, may come from
  co-sponsors, grants, collaborators, program fees, continued business income, or other sources."
- Hypothesis (guess):
  - Yes. Her income is event-driven (E09-E15), and her time after 2033 goes to running the residency (SH-26, ASM).
  - Counting on her earnings would rebuild, for the facility, the dependence we removed from the promise.
  - The buffer is sized from portfolio money only. Her income is upside.
- Would change: a sentence, and possibly a number (the uncommitted share after the facility contribution).
- Deliverables: FR. Domain: D6 (D5). Seed: 16.
- North star: the same independence principle is applied to her dream as to her promise.

**Q19. Is "licensing" in the case partly translation and foreign rights? Could a Taiwanese partner that funds comics
translation or residencies be a natural co-sponsor type for the fundraising draft?**
- Anchors: R-C27 ("licensing"), R-C44, R-C72, SH-07.
- Anchor quote: "using earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial
  ventures".
- Evidence: the 2020 deal was for "world English rights" (E09), so other-language rights stay with the author. As of
  2022, "It's not published in Mandarin" (E08). No Traditional Chinese edition was found; the Taiwan bookstores were
  blocked.
- Hypothesis (guess):
  - Possibly. Taiwan's cultural-content agencies fund translation and international comics (UNVERIFIED, D5 to check).
  - Low priority: this changes at most the list of co-sponsor *types* the draft addresses. Never name an
    organisation as committed.
- Would change: a sentence (co-sponsor audience in the draft).
- Deliverables: FR. Domain: D5. Seed: 19.
- North star: the fundraising draft speaks to partners who plausibly exist in her world.

**Q20. How should the FR describe the policy risks to her classroom and library channel? Should it cite the verified
2025-26 events in one clause, or stay generic?**
- Anchors: R-C16, R-C27, SH-23.
- Anchor quote: "her books are read in classrooms around the world and have sparked conversations about identity,
  belonging, and community."
- New evidence beyond B8a Q09: EO 14238 and its reversal; the June 2026 FCC E-Rate proposal; ALA's 4,235 challenged
  titles; the Laurel ban (E20-E22).
- Hypothesis (guess):
  - One generic clause ("school and library budgets and book challenges can affect an author's speaking and sales")
    in the human-capital paragraph.
  - Do not name her banned book in a document written for her. It adds nothing to the decision and could read as
    unkind.
  - Evidence goes in the team's notes, not the report.
- Would change: a sentence (length and specificity).
- Deliverables: FR. Domain: D6. Seed: 16.
- North star: we understand her industry's risks without dramatising her own experience.

**Q21. Reviewers repeatedly praise her work as frank, candid, humorous and tender (E01, E07). Should the FR's
"authentic team voice" allow one or two moments of warmth or humour, as long as the numbers stay exact?**
- Anchors: R-S28 ("authentic team voice"), seed 34, B8b Q28 (voice).
- Anchor quote: "Presents a compelling, well-organized narrative in an authentic team voice".
- Hypothesis (guess):
  - Yes, sparingly, and never about her or her identity: e.g. honest humour about the team's own mistakes in the
    Articulation section.
  - Candour about uncertainty is the professional form of "frank".
- Would change: a decision (tone guidance for the FR).
- Deliverables: FR. Domain: D9. Seed: 34.
- North star: a report that sounds like people she would want to work with, not a finance brochure.

---

## 4. Parked or not re-asked (already covered elsewhere)

| Item | Where covered | Why not re-asked |
|---|---|---|
| Is the pull quote hers? | B8a Q01, B8b Q1 | Settled as UNATTRIBUTED; nothing new found |
| "Secured base, then leap" as the risk pattern | B8a Q02, B8b Q3 | Q01 here uses it as a *benefit statement*, not as evidence |
| Late-deposit size (9-12 months) | B8a Q08, B8b Q12 | Q03 adds contract-completion evidence only |
| Gimmicks / finance-bro language | B8a Q03, Q07; B8b Q15, Q16 | Covered |
| Purpose statement / holding "jobs" | B8a Q04; B8b Q18 | Covered |
| "Both, not either-or" | B8b Q21 (same quote, E06-adjacent) | Covered |
| Taiwan risk framing (full story) | B8a Q11 | Q07 adds the "one correlated scenario" angle only |
| Rural vs city inflation index | B8a Q10 | Not my lens |
| Pronouns | B8a Q21 | Covered (she/her and they/them on her /hey page, VP) |

---

## 5. Leads for the specialists

- **D1 (rates):** Q02. Use the brief's shock table ($299,596 / $307,135 / $322,864 at -25/-50/-100bp). Express the
  top-up as a share of the $150k deposit (DER: 0% / 4.8% / 15.2%). Compare the rules (a)-(c).
- **D3 (quant):** Q04. Add a deposit-equity correlation parameter (base 0, stress +0.3; ASM) and a "late 12 months"
  switch. FRED SP500 2020 (E15) is the one real-life data point from her career; do not fit a model to it.
- **D6 (client psychology):**
  - Q03-Q05, Q18, Q20.
  - Primary sources: Authors Guild advances page (E11) and 2023 income survey (E12); BMS 1992 abstract (E18);
    CFA RF *Lifetime Financial Advice* (E19); her résumé's LG Studios line (E16).
  - Fuller survey data: the Guild's PDF (linked from E12, not opened).
- **D2 (equity/AI):** Q06, Q09. Verify the share of Taiwan-made chips in the index's largest holdings for Q07 (not
  researched here). Check whether News Corp is in the broad index and its weight (tiny, ASM).
- **D4 (Taiwan/geopolitics):** Q07, Q08. Also check whether a Traditional Chinese edition of *Messy Roots* exists.
  books.com.tw and readmoo.com gave 403 from this container; try a publisher catalogue or the National Central
  Library ISBN search.
- **D5 (co-sponsors):** Q16, Q19. Check Taiwan's cultural-content agency (TAICCA) programmes for comics translation
  and residencies (UNVERIFIED; not opened).
- **D9 (communication):** Q01, Q08, Q11-Q14, Q17, Q21. Exact accolade wording is in E04/E05. Book ages: "Ages 14–up"
  (E01/E02).
- **D10 (compliance):** Q10, Q15. The AI policy wording is in `phase_A/wins_week1_guardrails.md` section (d).
- **Still unverified (do not use as fact):**
  - 2025 corporate DEI and heritage-month event cuts (affecting her past talk types).
  - 2024-2026 comics market size (ICv2 publishes yearly; only 2023 was reached).
  - PEN America's ban index entries for her titles.
  - Whether U.S. tariffs affect China-printed full-colour graphic novels. This is a possible US-China channel into
    publishing costs, and so into advances: a lead only, no evidence read.
- **Fetch-cache tip:** other agents' pages are in `/tmp/insight_v1_fetch_cache/`. Grep them for `og:url` or
  `canonical` to find what is already there before spending searches.

---

## 6. Sources (all accessed 2026-09-27)

| Source | URL | Piece date | Status |
|---|---|---|---|
| Publishers Weekly review, *Messy Roots* | https://www.publishersweekly.com/9780063067769 | 2022-01-06 | VP |
| Publishers Weekly review, *Kirby's Lessons for Falling (in Love)* | https://www.publishersweekly.com/9780063067806 | 2024-12-12 | VP |
| Publishers Weekly Rights Report, week of 20 July 2020 | https://www.publishersweekly.com/pw/by-topic/childrens/childrens-book-news/article/83911-rights-report-week-of-july-20-2020.html | 2020-07 | VP |
| Laura Gao, Kirby page | https://www.lauragao.com/kirbys-lessons-for-falling-in-love | current | VP |
| Laura Gao, Messy Roots page | https://lauragao.com/messyroots/ | current | VP |
| Laura Gao, /hey, /projects, /speaking-events | https://lauragao.com/hey ; https://lauragao.com/projects ; https://lauragao.com/speaking-events | current | VP |
| Laura Gao, résumé PDF (professional lines only used) | https://lauragao.com/s/Laura-Gao-Resume.pdf | undated, current | VP |
| Messy Roots Educators & Book Clubs Guide | https://lauragao.com/s/Educators-Book-Clubs-Guide-Messy-Roots-klc2.pdf | c.2024 (says Kirby "will be released in 2025") | VP |
| NPR, "The pandemic inspired a cartoonist…" | https://www.npr.org/sections/goatsandsoda/2022/04/24/1093992912/the-pandemic-inspired-a-cartoonist-to-explore-their-wuhanese-roots-and-queer-ide | 2022-04-24 | VP (professional line only) |
| Wikipedia, *Messy Roots* and *Laura Gao* | https://en.wikipedia.org/wiki/Messy_Roots ; https://en.wikipedia.org/wiki/Laura_Gao | current | VP for the page; secondary; one date error noted |
| Authors Guild, book advances | https://authorsguild.org/blog/everything-you-need-to-know-about-book-advances/ | 2021-07-20 | VP |
| Authors Guild, 2023 income survey | https://authorsguild.org/news/key-takeaways-from-2023-author-income-survey/ | 2023-09-27 (upd. 2023-10-25) | VP |
| Authors Guild, HarperCollins AI licensing | https://authorsguild.org/news/harpercollins-ai-licensing-deal/ | 2024-11-19 | VP |
| ICv2 market size 2023 | https://icv2.com/print/article/57351 | 2024-07-15 | VP |
| FRED SP500 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500 | data to 2020-07-24 used | VP |
| NBER w3954 (Bodie, Merton, Samuelson) | https://www.nber.org/papers/w3954 | 1992 | VP (abstract) |
| CFA Institute RF, *Lifetime Financial Advice* | https://rpc.cfainstitute.org/research/foundation/2007/lifetime-financial-advice-human-capital-asset-allocation-and-insurance | 2007 | VP (summary) |
| ALA on IMLS reinstatement (and news list) | https://www.ala.org/news/2025/12/ala-welcomes-reinstatement-all-federal-imls-grants-libraries | 2025-12 | VP |
| Book Riot, Book Censorship News | https://bookriot.com/book-banning-will-not-stop-at-schools/ | 2024-01-12 | VP |
| The Art Newspaper, CCA closing | https://www.theartnewspaper.com/2026/01/13/california-college-arts-closing-vanderbilt-university-takeover | 2026-01-13 | VP (team awareness only; Q15) |
| Broken Frontier, comics and generative AI (title only) | https://www.brokenfrontier.com/raging-against-the-machine-comics-and-generative-ai-art-part-1/ | unknown | SU (search result title) |
| Blocked | search.books.com.tw, readmoo.com (403); Google Books API (no result) | - | not read |

---

## What this teaches

A person's job is an asset too. Economists call it **human capital**: the value of what you will earn in the future.
When we plan Laura's money we have to ask how her *income* behaves, not just her portfolio. Hers comes in lumps, from
contracts, book releases, speaking seasons and school budgets. It does not move in step with the stock market. In 2020
her career took off while stocks crashed. That changes the advice. The best protection for her residency promise is
not a clever trade that "hedges" publishing stocks. It is buying the payments in Treasuries so that the promise stops
depending on her next good year at all. The other lesson is about respect. Understanding a client means getting her
facts exactly right (which list, which award, which city). It means using her professional record rather than her
identity, and presenting the work in a way that honours her craft: no AI images for an illustrator, and clear charts
for a statistics graduate.
