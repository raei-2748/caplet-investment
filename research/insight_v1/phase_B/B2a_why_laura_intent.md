# B2a Why Laura / Case-Designer Intent: questions from six seasons of client history

Agent B2a, insight_v1 run, Phase B (question generation), written 2026-09-27. Lens: "Why Laura / Case-Designer
Intent". Starting angle: the client history 2021-2027 (Jordan, Hjemdahl, Ash, Ayoola, Barwin, Gao). I read each past
case and each season's winner and finalist news on globalyouth.wharton.upenn.edu, built one table of case shapes, and
asked which trend Laura's case continues or breaks and what that implies the semifinal readers will reward.

This file is AI-generated research for Team Caplet, for brainstorming only. It holds questions, evidence and
checklists. It contains no text meant for submission. The six students decide and write every deliverable in their
own words, and any AI use must be recorded in the Final Report's Works Cited (R-W46). Laura is covered only through
the case and her public professional record. Past clients are covered only through Wharton's own case pages and news
items; I left out their personal and family details on purpose.

Status labels (brief section 3): VERIFIED-PRIMARY (I read it on the primary page, URL + 2026-09-27),
VERIFIED-REPO-FILE, SNIPPET-UNVERIFIED, ASSUMPTION, PARAPHRASE-UNVERIFIED. INTERPRETATION marks my reading, never a
fact. A "hypothesis" in a question is a guess.

---

## 0. Summary (read this first)

1. **Laura's promise problem has been asked before, in a zero-rate world.** The 2021-22 case (Nichole Jordan) asked
   teams to fund a $5,000 scholarship "for at least 10 years" and wrote: "Should she keep $50,000 in cash? Should
   she invest in stocks that pay dividends? Another option?" (VERIFIED-PRIMARY). On the day that season began, the
   10-year Treasury yielded 1.48% (FRED, VERIFIED-PRIMARY). Buying the ten payments in advance would then have cost
   about 95% of their face value. Today the same kind of promise costs about 58% ($292,264 for $500,000, brief
   section 6). INTERPRETATION: the designers have brought back an old question at a time when interest rates change
   the answer. At 2021 rates, Laura's ten payments would cost about $429,000, almost all of her $450,000 (ASSUMPTION:
   flat 1.48%). (Q3)
2. **The $300,000 first deposit is almost exactly the price of the promise.** At a flat rate, $300,000 buys the ten
   payments at 5.09% (DERIVED). Through most of 2026 it did not quite reach: the same ladder cost more than $300k on
   173 of 185 trading days (F-111). The case PDF was created on 2026-09-10 (case_register 1.1), the first day the
   ladder cost fell under $300k. INTERPRETATION: the designers probably meant the first deposit to cover roughly the
   promise, and the second deposit to fund the facility and flexibility. That argues for (a) a lock rule written to
   depend on rates, not "it fits inside $300k", and (b) a two-deposits, two-jobs story (Q4, Q5).
3. **The committed outflow grew from half the client's money to more than all of it.** Jordan's payments were 50% of
   her $100,000. Laura's $500,000 of payments is 111% of her $450,000 (DERIVED). This is the first case with no
   return target and the first to use the word "certainty" (0 hits before, 6 this year; my word count, below). "Stock"
   drops from 2-4 hits per case to 0. "Co-sponsor" has 9 hits, "flexib" 5, "credib" 3, "uncertain" 3, where every
   past case had 0. INTERPRETATION: the scoring weight has moved from picking investments to reliability,
   flexibility and credibility (Q6, Q7).
4. **This is the first case with no personal-life hooks at all.** Every past case described hobbies (Peloton, yoga,
   scuba, Muay Thai, modelling; volleyball for Ash, per Wharton news). Teams turned those hobbies into stock picks
   (for Ash, "Nike ... caters to Ms. Ash’s love of sports", Teen Ink 2023-24 report, SNIPPET-UNVERIFIED). Laura's case
   has 0 hits for "enjoy", "love", "free time", "family", "lives" and "partner" (VERIFIED-REPO-FILE word check). Only
   her professional mindset and her goals remain. INTERPRETATION: "tailoring" this year has to run through her cash
   flows, constraints and way of thinking, not through her tastes (Q2).
5. **Clients and judges have said the same things for five years (all VERIFIED-PRIMARY).**
   - Clients reward feeling understood. Jordan (2022): she "had never felt more “seen” in her life". Ayoola (2025):
     "not just about the numbers, but about understanding and connecting with people".
   - Judges reward restraint and clear reasoning: "Cut slides, cut words, cut minutes" (2022); "a lot of depth and
     accuracy" (2024); "clear thoughtfulness and reasoning behind all the decisions" (2025).
   - Judges have also named two gaps that most teams leave open: "consider behavioral finance and their clients’
     emotions during a market downturn" and "take a look at this person holistically" (2024, the second from an
     Aberdeen fixed-income manager).

   Our plan does not yet cover these two gaps explicitly (Q1, Q10, Q11).
6. **Two facts correct the team's "Why Wharton chose Laura" document.**
   - Laura is not the youngest recent client. The 2022-23 case states "Peter, who is 25 years old" (VERIFIED-PRIMARY).
   - "Unstable income is new" needs one correction. Her living costs are outside the portfolio, so the instability
     matters only through the 2028 deposit. What is genuinely new is that this is the first case in six seasons with
     a scheduled second contribution, and that contribution depends on creative income (Q11).
7. **19 questions follow (section 3)**, ranked by deadline tier within groups. The five I rate highest for "99% of
   teams will miss": Q4 (the $300k calibration and a rate-conditional lock rule), Q3 (why locking is right *now*: the
   2021 comparison), Q2 (no hobby hooks, so no identity-themed securities), Q10 (the two gaps judges keep naming),
   Q5 (two deposits, two jobs).

---

## 1. Method

- Read Wharton's archive page and every linked news item for the finals and semifinals 2022-2026. Read the three
  past case pages that are still live (2021-22, 2022-23, 2024-25). Read the 2025-26 case from a Scribd copy of the
  retired Wharton page. For 2023-24 I found no case page, so the case shape comes from a team report on Teen Ink.
  URLs are in section 6.
- Word-counted the same key words in each case text (Python regex, lower case). The 2025-26 count uses the Scribd
  copy, which is partly truncated. The 2024-25 page may end before any boilerplate. So the counts are indicative, not
  exact.
- Took season-start 10-year yields from FRED DGS10. Priced the 2021-22 scholarship at the 2021-09-27 FRED curve
  (ASSUMPTION: par yields used as zero rates, payments at mid-year). Solved for the flat rate at which $300,000 buys
  Laura's ten payments. All inline Python is in section 5.
- Checked 19 key quotes word for word with `fetch_text.py --grep` (all "FOUND VERBATIM: YES").
- Checked Phase A (R, F, SH ids) and the four Phase B files already written (B1a, B1b, B7a, B7b) so I would not re-ask
  their questions. Where I overlap, I say what is new.

---

## 2. Client history table (2021-2027)

| Season | Client (Wharton) | Money in | What the case asked | Shape of the liability | WInS cash | Words that framed success | Winners | Finished reports |
|---|---|---|---|---|---|---|---|---|
| 2021-22 | Nichole Jordan, WG'08 (SVP at Via, TransitTech) | $100,000 | $5,000/yr scholarship from 2022 "for at least 10 years"; build generational wealth and fund education for young relatives | 10+ fixed annual payments = 50% of assets, starting at once; "Should she keep $50,000 in cash? ... dividends? Another option?" | $100,000 | "long-term and a small amount of mid-term profitability"; "WInS can only accurately assess ... short-term" | Sailing to Success (AZ); Sky Investments (Bergen County Academies); M&R (Marvin Ridge) | ~1,300 |
| 2022-23 | Peter Wang Hjemdahl, W'19 (rePurpose Global) | $100,000 | $20,000 now to grow ≥$10,000 in 5 years, then yearly $5-10k gifts to start-ups "use the interest"; wellness centre in Miami within 15 years | Return target plus a perpetual-style gift paid from income | $100,000 | "compelling and clever pitch to convince Peter"; "trying to land the same client" | DMV's Finest (Thomas Jefferson HS); Amity 7 Chakras; NovyPorg_1 (Prague) | ~1,400 |
| 2023-24 | Hilary Ash, W'13 (LA28 Olympic and Paralympic Games) | not found (case page retired) | Per a team report (SNIPPET-UNVERIFIED): renovate a property in South America within 5 years; launch a sports consulting firm within 15 years | Two dated goals, return-driven | not found | Volleyball, "a passion highlighted in Hilary Ash’s client profile", inspired team creativity (Wharton news) | Spark Investments (Bergen County Academies); Wreckers (Staples HS); DMV's Finest | >1,600 |
| 2024-25 | Ladi Ayoola, WG'22 (Visa; co-founder of Plugtent) | "$100,000 investment a baseline" | Phase 1: ≥5 housing units by 2030 at "about $10,000 USD per housing unit"; Phase 2 (2040): storefront + youth centre ≥$50,000, plus one year of operations ≥ a quarter of $100k; Phase 3 later | Dated cost targets; first mention of operating costs | $100,000 | "generate a return"; "impact" (2 hits) | BAM Investing (Deerfield); Finance from France (Chicago); FA Quakers | ~1,800 |
| 2025-26 | Connor Barwin, WG'23 (Make the World Better foundation) | $500,000 | Grow to ≥$1.5m by 2036 for a capital project; community contributions from "the end of year three (2029)" of ~$10k that "can rise" | Growth target + small rising grants | $500,000 | "Every dollar invested reflects MTWB’s values"; "win Connor’s business"; Wharton: "think beyond financial returns" | FigCapital (Stuyvesant); HHA (Brasília); Riverhawk (Farmington) | ~2,300 |
| **2026-27** | **Laura Gao, W'18** (author, illustrator, entrepreneur, educator) | **$300,000 (2027) + $150,000 (2028)** | **Ten fixed $50,000 payments 2033-2042 "with a high degree of certainty"; operating reserve set aside in 2033; a "responsible" facility contribution; a 2031 dollar range + confidence for co-sponsors; a fundraising draft** | **Fixed nominal liability = 111% of contributions; deferred 6 years; no return target** | **$300,000 (= first deposit)** | **"earn her confidence"; "authentic team voice"; "certainty" x6; "co-sponsor" x9** | TBD | TBD |

Sources: 2021-22, 2022-23 and 2024-25 case pages, VERIFIED-PRIMARY. 2023-24 goals from the Teen Ink team report,
SNIPPET-UNVERIFIED as to the case wording. 2025-26 from the Scribd copy, SNIPPET-UNVERIFIED. Winners and report counts
from the archive and finale/semifinal articles, VERIFIED-PRIMARY. 2026-27 from the repo case, VERIFIED-REPO-FILE.

Word counts across the case texts (my count; indicative only, see Method):

| Case | return | profit | risk | certainty* | thoughtful | impact | values | stock | inflation | uncertain | credib | flexib | co-sponsor | pitch/convince/"win " |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021-22 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2022-23 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 4 |
| 2024-25 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2025-26 (copy) | 1 | 2 | 1 | 0 | 0 | 3 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 8 |
| 2026-27 | 2 | 0 | 2 | 6 | 3 | 0 | 0 | 0 | 2 | 3 | 3 | 5 | 9 | 0 |

*In 2021-22 and 2022-23 the regex hit "certain factors", which is not the concept, so those cells are set to 0.
"Volatil" appears only in 2026-27 ("Laura understands that investing involves uncertainty and periods of market
volatility", VERIFIED-REPO-FILE p.2).

Season-start 10-year Treasury yield (FRED DGS10, VERIFIED-PRIMARY; 2026 from the repo Treasury CSV, F-001):

| Season start | 2021-09-27 | 2022-09-26 | 2023-09-25 | 2024-09-23 | 2025-09-29 | 2026-09-25 |
|---|---|---|---|---|---|---|
| 10y yield | 1.48% | 3.88% | 4.55% | 3.75% | 4.15% | 5.17% |

What the table shows (INTERPRETATION):
- **Trends that continue.**
  - Every client is a Wharton alum paying something forward to others. Jordan: "opening doors or creating
    opportunities for others like me". Hjemdahl: "pay forward the gratitude". Ayoola: "it truly takes a village".
    Barwin: community spaces. Laura: a residency for "artists, writers, designers, entrepreneurs, and educators",
    the same roles the case gives her.
  - Three cases in a row fund a physical, community-facing place: Ayoola, Barwin, Gao.
  - Horizons stay long (10-16 years).
  - The "portfolio manager ... makes the final investment decisions" line is boilerplate from 2021 onward.
- **Trends that break.**
  - The return target disappears.
  - Certainty, flexibility, credibility and a third-party audience (co-sponsors) appear.
  - Hobbies and values language vanish.
  - The liability grows from 50% to 111% of the client's money.
  - Cash cannot fund the promise, because $450k is less than $500k.
  - The timing is exact ("Year 0 is 2026"). Earlier cases were loose: "starting in 2022", "the end of year three".
  - WInS cash equals the first deposit.
  - The instruments open up to any ETF and any government bond.
- **What that implies readers will reward.** An answer to a *promise* problem that is reliable, plainly explained
  and honest about uncertainty to outsiders. That fits every judge remark since 2022 (restraint, accuracy, reasoning,
  the client's emotions, the whole person). A stock-screening showcase does not fit it. Past finales celebrated
  "stock-filtering algorithms", "endless Environmental, Social & Governance considerations" (2023) and "customized
  algorithms, AI innovations, portfolio optimizations" (2025).

---

## 3. The questions

Each gives: the question; its anchor; the hypothesis (a GUESS) with evidence; what it would change and where; the
deliverables; the domain; the seed; the North Star link.

### Tier 1: WInS now and Trading Notes (Oct 23)

**Q4. Was the $300,000 first deposit sized to be roughly the price of the ten payments at 2026 rates, so the IPS lock
rule should say "buy as much of the ladder as the 2027 deposit affords and complete it from the 2028 deposit" rather
than rely on today's "it fits inside $300k"?**
- Anchor: F-111 ("Above $300k on 173 of 185 trading days"), R-AN13, R-AN14, R-C26/R-C27. Case PDF created
  2026-09-10 (case_register 1.1).
- Hypothesis (GUESS): yes. At a flat rate, $300k buys the promise at 5.09% (DERIVED). At 4.0-4.5%, the rates most
  people would call "reasonable" in 2025-26, the promise costs $317-333k. At those rates the first deposit falls just
  short and the two deposits together cover it easily. The designers probably wrote the case when the ladder cost
  $302-325k (Jan-Sep 2026, F-111). Our "fits inside $300k with $7.7k to spare" depends on a September 2026 rate peak.
  The 10y is at its highest close since 2007 (F-004).
- Would change (decision + sentence):
  - The IPS rule wording must depend on rates and name the 2028 deposit as the planned completion source.
  - The WInS promise book should be sized as "what $300k buys today" (about 97%), with the gap stated.
  - One Trading Note reflection could say the rule was tested by rates.
- Deliverables: WInS-now, TN, IPS. Domain: D1. Seed: none (extends brief section 9, "Rule if rates fall").
- North Star: Laura sees a plan that works in the world the case was written for, not one that needed lucky rates.

**Q5. Should our narrative spine be "the first deposit secures the promise; the second deposit and growth fund the
facility and flexibility", the one idea a reader remembers, as Wharton's WInS cash ($300k = deposit 1) seems to
invite?**
- Anchor: R-AN14; R-W59 ("The additional $150,000 ... will not be added to WInS"); R-C8 ("the investment strategy
  that Laura ultimately chooses"). Judge, 2022 finale (VERIFIED-PRIMARY): "Cut slides, cut words, cut minutes".
- Hypothesis (GUESS): yes, as long as it is stated with Q4's rate condition. It gives the 50-word pitch a structure
  that is easy to remember. It explains the WInS book as the Year-1 promise book, which settles the open question
  (Year-1 book vs post-2028 target, brief section 9) in favour of Year 1, with a small growth sleeve. It maps onto the
  case's order: reserve first, facility second (R-C50).
- New versus B1b Q5: the case history shows WInS cash was never before tied to a client deposit ($100k × 13 seasons,
  then $500k). Q4's calibration shows the tie is also economic.
- Would change: decision (WInS allocation mirrors the Year-1 book) + the sentence spec for the pitch.
- Deliverables: WInS-now, TN, IPS. Domain: D9. Seed: 1.
- North Star: the simplest true story of her money; each deposit has a job she can repeat to a co-sponsor.

**Q2. Laura's case is the first in six seasons with no hobbies, family or city. Did Wharton remove the "hobby hooks"
that past teams turned into stock picks, and should we therefore rule out every identity- or interest-themed security
(Taiwan tilt, publishing, "creator economy", Asian-American themes)?**
- Anchor: R-AN34 (no values or impact language), R-C10 (her themes are her public work), brief section 4 (tokenism).
  Word check (VERIFIED-REPO-FILE): 0 hits for enjoy, love, free time, family, lives, partner, San Francisco.
- Evidence:
  - The 2021-22 case listed Peloton, yoga, wine tasting. The 2022-23 case listed scuba, Muay Thai, yoga. Both
    VERIFIED-PRIMARY.
  - 2023-24: "volleyball, a passion highlighted in Hilary Ash’s client profile that inspired great creativity"
    (VERIFIED-PRIMARY). A team bought Nike because it "caters to Ms. Ash’s love of sports" (Teen Ink,
    SNIPPET-UNVERIFIED).
  - The Top 50 lists are full of client-themed team names: "Serve and Set Finances" (2024); "End Zone Equity",
    "Lumen Field Investments" (2026) (VERIFIED-PRIMARY).
- Hypothesis (GUESS): yes, the removal is deliberate. Tailoring must run through cash flows, constraints and her
  professional mindset. The EWT/Taiwan tilt (open, brief section 9) should be dropped unless a cash-flow reason
  exists; I see none, because the promise is in USD.
- Would change: decision (drop themed positions from WInS now) + a sentence in the IPS saying how we tailored.
- Deliverables: WInS-now, TN, IPS. Domain: D7. Seed: 12.
- North Star: she is a person with a plan, not a theme; a firm that tailors to her goals shows it listened.

**Q18. The case is the first to say the client "understands that investing involves uncertainty and periods of market
volatility". Should our risk-tolerance statement, and one Trading Note, use that line to set a stated sleeve drawdown
she accepts, while the payments carry no market risk?**
- Anchor: case p.2 L68-74 (R-C37/R-C38 area; VERIFIED-REPO-FILE): "Laura understands that investing involves
  uncertainty and periods of market volatility. Although she has been willing to take thoughtful risks ...". "Volatil"
  has 0 hits in the four earlier case texts (my check).
- Hypothesis (GUESS): yes. Willingness is stated in the case, and ability is set by the promise. A number such as
  "the growth sleeve could fall about a third in a bad year; the ten payments would not change" turns an adjective
  into something she can hold us to. Wharton's example trading note (R-AN44) speaks of reducing volatility; our note
  should say why volatility in the promise hedge is not risk to her.
- Would change: a number (the stated sleeve drawdown, for D3 to size) + a sentence in the IPS risk section + one TN
  reflection.
- Deliverables: TN, IPS, FR. Domain: D6. Seed: 18.
- North Star: it answers her own stated understanding of risk, not a generic risk questionnaire.

**Q11. Laura is the first client in six seasons with a scheduled second contribution, and it depends on
reputation-driven creative income. Is a "human-capital" underweight (publishing, media, consumer names) large enough
to matter in a broad-index sleeve, or should we only state the link and do nothing (complexity must earn its place)?**
- Anchor: R-C27 ("publishing advances, speaking engagements, licensing, and other entrepreneurial ventures"), R-AN31,
  SH-03/BS-03 (credibility is income). Earlier clients: "both with steady jobs and incomes" (2024-25); retirement
  already covered (2021-22, 2022-23) (VERIFIED-PRIMARY). 2024 judge: "take a look at this person holistically"
  (VERIFIED-PRIMARY).
- Hypothesis (GUESS): publishing and media are well under 2% of a U.S. broad index (to verify). An underweight would
  add trades and explanation for almost no protection. The real link to her income is the equity market as a whole
  (a 2027 crash also hits advances and speaking), and that is the wrong-way deposit risk already open in brief
  section 9. So: state it, do not trade it.
- New versus brief section 9 ("human-capital underweight" open): the history shows this is the first case where the
  client's future income feeds the portfolio. That is why readers will look for the "holistic" point.
- Would change: decision (keep or drop the underweight idea) + a number (sector weight).
- Deliverables: WInS-now, IPS, FR. Domain: D2. Seed: none.
- North Star: shows we see her whole financial life without adding complexity she has to pay for.

### Tier 2: IPS (Nov 6)

**Q3. Wharton asked a ten-payment question before, in 2021 at a 1.48% 10-year yield, when pre-funding cost about 95%
of face. Should our IPS and FR say why locking the promise is right for Laura *now* (it costs about 58% of face at 2026
rates), so readers see a choice made for this rate world and not a reflex for safety?**
- Anchor: R-AN13 ($450k in vs $500k out). 2021-22 case (VERIFIED-PRIMARY): "wants to be able to offer the scholarship
  for at least 10 years. Should she keep $50,000 in cash? Should she invest in stocks that pay dividends? Another
  option?"
- Evidence (ASSUMPTION arithmetic, section 5):
  - Jordan's ten $5,000 payments at the 2021-09-27 curve were worth about $47.3k (0.946 of face).
  - Laura's ten payments at the 2026-09-25 curve are worth $292,264 (0.585 of face).
  - At a flat 1.48%, Laura's promise would cost about $429k.
- Hypothesis (GUESS): yes. In 2021, "keep cash" and "buy bonds" were almost the same thing. In 2026, locking earns
  about $208k of interest for her, so the case works only in a high-rate world. The designers made cash impossible
  ($450k < $500k) and interest rates the main variable. Saying so in one clause shows judgement, not caution.
- Would change: an IPS sentence (why now) and an FR chart (cost of the promise against the yield, marking 2021 and
  2026).
- Deliverables: IPS, FR. Domain: D1. Seed: none.
- North Star: Laura sees that we understood why her promise is affordable today, not only that it is safe.

**Q10. Judges and clients have named the same two gaps since 2024: the client's emotions in a downturn, and the whole
person. Which pre-commitment rule in the IPS answers the first, and which sentence answers the second?**
- Anchor: criterion "Client Knowledge and Objectives" (R-S25, "recommendations that can earn her confidence"). 2024
  finale (VERIFIED-PRIMARY):
  - "urging them (as investment advisors) to consider behavioral finance and their clients’ emotions during a market
    downturn";
  - "When analyzing someone’s investments, take a look at this person holistically".
  Guide p.5 (via B7a/B1b, VERIFIED-PRIMARY): "you may not redesign your strategy after observing the results".
- Hypothesis (GUESS):
  - (a) A one-line rule: "a fall in the growth sleeve never changes the promise book; we rebalance the sleeve inside
    bands and do not sell into a fall". The IPS must pre-commit it, because it cannot be added later.
  - (b) One sentence that joins her income (the 2028 deposit), her credibility and the portfolio.

  Neither is in the current strategy text (brief section 7).
- Would change: an IPS rule and sentence; an FR scenario ("what Laura sees in a 2029 bear market").
- Deliverables: IPS, FR. Domain: D6. Seed: none (connects to seed 27, which belongs to another lens).
- North Star: she chooses the firm that has already planned how she will feel on a bad day.

**Q8. Laura has a statistics degree, and the competition's academic director has an M.A. in Statistics and runs the
Wharton Financial Analytics Initiative. What would a statistically trained reader reject on sight in our "high degree
of certainty" definition and our 2031 confidence statement?**
- Anchor: R-C12, R-C54/R-C55, R-AN32, R-AN9. Main page (VERIFIED-PRIMARY): "his M.A. in Statistics and Ph.D. in
  Economics from the University of California at Berkeley"; "founded and heads the Wharton Financial Analytics
  Initiative".
- Also: Laura describes her degree as "a degree in business analytics" (Wharton Magazine, 6 Apr 2022,
  VERIFIED-PRIMARY). The case chose the word "Statistics".
- Hypothesis (GUESS): the reader would reject:
  - a bare "95%" with no model named;
  - calling a model probability a "confidence" without saying what is random;
  - a two-ended range whose top end was never tested;
  - independent lognormal returns presented as reality;
  - no sample size or seed.

  The fix is a four-line "model card" in the FR (model, inputs with dates, what is not modelled, what the number
  means), plus the market-priced definition of certainty already chosen.
- New versus brief section 8 item 6: the reader profile (academic director) is new evidence that raises the bar on
  method disclosure, not on the definition.
- Would change: an FR sentence/box; the IPS certainty sentence must name its test.
- Deliverables: IPS, FR. Domain: D3. Seed: 18.
- North Star: a statistics graduate trusts a firm whose numbers say what they are and are not.

**Q6. The committed outflow has grown from 50% of the client's money (Jordan) to 111% (Laura), and this is the first
case with no return target. Should the Final Report spend most of its analysis on funding reliability, the facility
rule and the co-sponsor range, and much less on security selection?**
- Anchor: R-C79-R-C84 (the five tests: none is about returns), R-S26 ("evaluate funding reliability, the facility
  contribution, and financial flexibility under varying market outcomes"), R-AN34. History table (section 2).
- Hypothesis (GUESS): yes. A rough split: about two-thirds on the promise, the facility and the co-sponsors, and
  about one-third on implementation and security rationale. Past finales celebrated stock screens (2023, 2025), so
  most repeat-school teams will over-weight security selection.
- Would change: decision (page allocation in the FR) + the IPS order of topics.
- Deliverables: IPS, FR. Domain: D7. Seed: none.
- North Star: her problem is a promise; the firm that spends its pages on her problem is the one she picks.

**Q7. The case's vocabulary moved: "certainty" (0 → 6 hits), "co-sponsor" (0 → 9), "flexib" (0 → 5), "credib" and
"uncertain" (0 → 3), while "stock" (2-4 → 0) and "pitch/convince/win" (up to 8 → 0) vanished. Should we adopt the
new words as our own terms and ban the old ones, and use the word table in the FR's Articulation section as evidence
of how we read the case?**
- Anchor: R-S27 ("clearly explains the team's research and decision-making process"), R-S28 ("authentic team voice").
  Word table in section 2 (my count).
- Hypothesis (GUESS): yes to the vocabulary. Words like "beat the market", "alpha", "pitch" or "win her business"
  read like last season's template. The word table is an honest process artefact for the Articulation criterion, and
  it takes one sentence or one small chart.
- New versus B1b Q9 (tone): this adds counts and makes them a reusable checklist.
- Would change: a vocabulary checklist for all three deliverables; a possible FR chart.
- Deliverables: TN, IPS, FR. Domain: D9. Seed: 12.
- North Star: we speak the language of her case (certainty, flexibility, credibility), which is the language she
  chose.

**Q14. The 2026-27 Guide opens by defining the whole competition as helping a client "achieve specific financial goals
and meet future cash-flow needs", which the public main page does not say. Is Wharton re-centring the competition on
cash-flow planning, and should our first exhibit (and every Trading Note) name the dated cash flow it serves?**
- Anchor: R-new. Guide p.1 (VERIFIED-PRIMARY): "designed to help a client achieve specific financial goals and meet
  future cash-flow needs". Main page R-W5: "designed to help the client achieve their objectives". Criterion 1
  (R-S24): "disciplined planning across Laura's changing time horizons and cash-flow needs".
- Hypothesis (GUESS): yes. The Guide is written generically ("a client") and so is likely to stay for future seasons.
  A one-row-per-year table (2027 to 2042: deposits, payments, reserve date, range date) is the cheapest way to score
  on "disciplined planning".
- New versus B1b Q2: the Guide's opening sentence is new evidence that this is the competition's frame, not only
  this case's.
- Would change: FR exhibit 1; a TN habit (each note names its date); IPS wording "cash-flow needs".
- Deliverables: TN, IPS, FR. Domain: D7. Seed: none.
- North Star: Laura's plan is a calendar of promises; showing the calendar shows we understood her.

**Q1. Past clients said what won them over: feeling "seen" (Jordan, 2022) and plans "not just about the numbers"
(Ayoola, 2025). With no personal hooks in Laura's case, which case-stated facts about how she thinks should each
recommendation visibly mirror, so she would feel understood rather than analysed?**
- Anchor: R-S25; R-C6, R-C12, R-C18, R-C24 ("Thoughtful financial planning ... turning those ideas into reality"),
  R-C37/R-C38; seed 32. Quotes VERIFIED-PRIMARY: "she had never felt more “seen” in her life"; "not just about the
  numbers, but about understanding and connecting with people".
- Hypothesis (GUESS), five mirrors, all from the case:
  - (1) Ideas become reality through planning: the plan makes the residency fundable.
  - (2) Statistics: certainty is defined and tested.
  - (3) "Thoughtful risks": risk only where the promise is safe.
  - (4) A product manager: dated milestones (2027, 2028, 2031, 2033) with decision rules.
  - (5) A public voice whose credibility is an asset: nothing overpromised.

  Every "tailored" claim should cite one of these. Any claim that cites none is decoration.
- Would change: a checklist for the IPS client paragraph and for each TN reflection's "how it serves Laura" line.
- Deliverables: TN, IPS, FR. Domain: D6. Seed: 32.
- North Star: this is the direct answer: she recognises her own way of thinking in our plan.

### Tier 3: Final Report (Dec 4)

**Q9. The pull quote "The only person who needs to believe in something is yourself." is unattributed, while every
past case quoted the client in the first person. Last year's client framed success as "confidence ... and humility to
know that you don't have all the answers". Is the case built on turning private conviction into public credibility,
and how should the fundraising draft use the quote, if at all?**
- Anchor: R-C21, R-AN30, R-C66. Past quotes (VERIFIED-PRIMARY):
  - Jordan: "What drives me is opening doors or creating opportunities for others like me."
  - Barwin (2026): "approach every problem with confidence that you can figure it out, and humility to know that you
    don’t have all the answers".

  My search found no source for the pull quote. It is not on the Wharton Magazine, Overachiever, Mochi or Wikipedia
  pages (fetch_text --grep: NO); Goodreads timed out. PARAPHRASE-UNVERIFIED as her words.
- Hypothesis (GUESS): yes to the theme. Her self-belief is what starts the project, and co-sponsors need evidence.
  The draft should not quote the line as hers unless it is verified. Instead it can show conviction as money already
  committed ("ten years of operations are already funded"), and humility as a range with a stated floor.
- Would change: a decision (quote or not); the structure of the FR fundraising draft.
- Deliverables: FR. Domain: D6. Seed: 15.
- North Star: we turn what she believes into what others can check, which is exactly what she needs in 2031.

**Q12. Laura's case-stated career includes product manager. Would framing the 2031 range as "committed (already bought)
plus stretch (with a stated probability)" feel like her own professional language, and more credible to co-sponsors,
than "p10-p90"?**
- Anchor: R-C12 ("product manager in the technology industry"), R-C67-R-C71, R-AN9.
- Hypothesis (GUESS): yes for the co-sponsor audience. Committed-versus-stretch is plain English, and it matches the
  floor-plus-upside design (brief section 8 item 7). It is professional, not identity, so it passes the tokenism rule.
  Percentile language belongs in the FR's method box (Q8).
- Would change: a sentence and structure spec for the FR fundraising draft.
- Deliverables: FR. Domain: D9. Seed: 32.
- North Star: she reads her range in words she already uses to promise things.

**Q13. All six clients pay something forward, and Laura's residency is for "artists, writers, designers, entrepreneurs,
and educators", her own roles. Are the residents, not only Laura, the people who rely on the ten payments, and does
that raise the bar for "high degree of certainty" and for how we describe it to co-sponsors?**
- Anchor: R-C40 (the residency), R-C41 ("reliable support for its early operations"), R-C47. Rules page R-W29 (CFA
  Asset Manager Code). History (VERIFIED-PRIMARY): "others like me" (Jordan), "pay forward" (Hjemdahl), "it truly
  takes a village" (Ayoola).
- Hypothesis (GUESS): yes. Residents will plan their lives around a residency place, so a broken operating promise
  harms third parties, not just Laura. That is a Laura-specific reason (beyond the case's "must") for market-priced
  certainty. It is also the strongest co-sponsor line: funders fear running costs (stakeholder map BS-17), and here
  running costs are already secured.
- Would change: a sentence in the IPS objective ("why certainty"); the FR fundraising lead.
- Deliverables: IPS, FR. Domain: D5. Seed: 15.
- North Star: we protect the people her residency serves, which is why she is building it.

**Q19. The case's first line about Laura is a belief, "stories have the power to change how people see the world", and
her first named work answered misinformation. Should the co-sponsor draft be built as a short story backed by numbers
(problem, promise, proof, range) rather than a table-first term sheet?**
- Anchor: R-C9, R-C14, R-AN33, R-S28 ("compelling, well-organized narrative"; "clearly and credibly to prospective
  co-sponsors").
- Hypothesis (GUESS): yes, with care. Use a four-beat story, each beat carrying one verified number. The tokenism
  risk is low because this is her case-stated belief about communication, not her identity. The failure mode is
  puns on her book titles, which the field will overuse (B7b).
- Would change: the structure of the FR fundraising draft; one Creativity-criterion decision.
- Deliverables: FR. Domain: D9. Seed: 15.
- North Star: she will recognise a firm that tells the truth as a story, the way she does.

**Q17. Semifinal lists show many client-themed team names and "creative" themes, and a 2024 semifinal judge said the
client-hobby creativity "resonated". Under this year's "authentic team voice" criterion, which creative element is
authentic for us, and which is decoration?**
- Anchor: R-S28. 2024 semifinal judge (VERIFIED-PRIMARY): "The one thing that stood out to me was the ability to
  connect the client’s objectives to an investment strategy." Top 50 names, 2024 and 2026 (VERIFIED-PRIMARY).
- Hypothesis (GUESS): creativity that carries analysis is authentic. Examples: the 2021-vs-2026 cost-of-the-promise
  chart (Q3), or one line on how Australia's Future Fund or superannuation handle long promises, if it earns its place
  (v4 Part 2 lesson 4). Book-title themes are decoration. Note the judge's own words: "connect the client’s
  objectives", not hobbies.
- Would change: decision on the FR's creative device.
- Deliverables: FR. Domain: D7. Seed: none.
- North Star: our creativity is about her problem, so it reads as ours and as hers.

**Q16. How did the 2021-22 finalists fund Jordan's ten scholarship payments (cash, dividend stocks, bonds)? Does that
show readers accept an answer suited to its rate regime, so a Treasury match in 2026 will not look "too simple"?**
- Anchor: 2021-22 case (VERIFIED-PRIMARY, quoted in Q3). 2022 finale (VERIFIED-PRIMARY): teams showed "client-focused
  talk of dividends and growth stocks, ESG and risk management".
- Hypothesis (GUESS): the finalists mostly used dividend stocks and growth stocks. Nobody locked Treasuries, because
  at 0-1.5% there was little to lock. If so, our FR can include a short "alternatives we rejected" line: cash (cannot
  reach $500k from $450k); dividend stocks (dividends were cut in 2008 and 2020, a fact to verify); growth-first
  (brief section 8).
- Would change: an FR "alternatives considered" sentence; confidence in the simple core.
- Deliverables: IPS, FR. Domain: D7. Seed: none.
- North Star: shows Laura we tested the obvious answers and chose the one that fits her year.

**Q15. The 2024-25 case, for a Nigerian project, wrote "$10,000 USD per housing unit". The 2026-27 case, for a Taiwan
project, never names a currency. Does that make currency a deliberate simplification (one disclosure line) rather than
a hidden test (a modelled TWD scenario)?**
- Anchor: R-AN10, BS-04. 2024-25 case (VERIFIED-PRIMARY): "Ladi believes it will cost about $10,000 USD per housing
  unit; however, material costs and market dynamics are always changing."
- Hypothesis (GUESS): simplification. Last year the designers named USD because they gave costs. This year they give
  no costs ("not expected to estimate that cost"). So the currency's job is only in the co-sponsor labelling (write
  US$) and one sentence on NT$ purchasing power. Brief section 8 item 15 already says "disclose, quote in two
  currencies". What is new is the prior-case contrast, which argues for keeping it to about one sentence.
- Would change: the number of FR words on TWD (a cap); no TWD positions in WInS.
- Deliverables: FR. Domain: D4. Seed: none.
- North Star: we handle the Taiwan detail with care but keep her plan simple.

---

## 4. Evidence found in this pass (with status)

| # | Fact | Source | Status |
|---|---|---|---|
| E1 | 2021-22 case: "Starting in 2022, Nichole would like to provide a small scholarship of $5,000 per year ... for at least 10 years. Should she keep $50,000 in cash? Should she invest in stocks that pay dividends? Another option?"; "$100,000"; "$100,000 in virtual cash"; lists hobbies | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/ | VERIFIED-PRIMARY |
| E2 | 2022-23 case: "Peter, who is 25 years old"; $20,000 fund, "at least a $10,000 return", "use the interest"; wellness centre "in the next 15 years"; "compelling and clever pitch" | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2022-2023/ | VERIFIED-PRIMARY |
| E3 | 2023-24 goals: South American property within 5 years; sports consulting firm within 15 years; a Nike pick justified by her love of sports; a mid-term report existed | https://www.teenink.com/opinion/all/article/1215809/ (team report) | SNIPPET-UNVERIFIED (secondary, team text) |
| E4 | 2024-25 case: "$10,000 USD per housing unit"; Phase 2 in 2040 "at least $50,000"; one year of operations "at least a quarter of your original $100,000" | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/ | VERIFIED-PRIMARY |
| E5 | 2025-26 case: grow $500,000 to at least $1.5 million by 2036; community contributions from "the end of year three (2029)"; "win Connor’s business" | https://www.scribd.com/document/965855349/Case-Study-Wharton-Global-Youth-Program | SNIPPET-UNVERIFIED (copy of the retired Wharton page) |
| E6 | 2022 finale: Jordan "had never felt more “seen” in her life"; judge: "Cut slides, cut words, cut minutes"; teams' "dividends and growth stocks, ESG and risk management"; ~1,300 final reports | https://globalyouth.wharton.upenn.edu/news/top-teams-sail-to-success-in-the-2022-wharton-investment-competition-global-finale/ (28 Apr 2022) | VERIFIED-PRIMARY |
| E7 | 2023 finale: "stock-filtering algorithms ... endless Environmental, Social & Governance considerations"; "we will build on the success of the Investment Competition with changes and new competitive experiences" | https://globalyouth.wharton.upenn.edu/news/the-2023-investment-competition-global-finale-ends-in-sweet-victory-for-dmvs-finest/ (26 Apr 2023) | VERIFIED-PRIMARY |
| E8 | 2024 finale judges: "a lot of depth and accuracy"; "consider behavioral finance and their clients’ emotions during a market downturn"; "take a look at this person holistically" (Zoe McCormick, abrdn North American fixed income); "doing some reimagining of our signature competition" | https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/ (23 Apr 2024) | VERIFIED-PRIMARY |
| E9 | 2024 semifinals: "volleyball, a passion highlighted in Hilary Ash’s client profile"; judge: "the ability to connect the client’s objectives to an investment strategy" | https://globalyouth.wharton.upenn.edu/news/wharton-global-youth-hosts-five-virtual-events-to-announce-the-2024-investment-competition-finalists/ (25 Mar 2024) | VERIFIED-PRIMARY |
| E10 | 2025 finale: Ayoola: "not just about the numbers, but about understanding and connecting with people"; judge (Aberdeen credit): "clear thoughtfulness and reasoning behind all the decisions"; teams used "customized algorithms, AI innovations, portfolio optimizations" | https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/ (1 May 2025) | VERIFIED-PRIMARY |
| E11 | 2026 finalists: Barwin's "confidence ... and humility" quote; his case "encouraged students to think beyond financial returns" | https://globalyouth.wharton.upenn.edu/news/11-teams-advance-to-the-2026-wharton-global-high-school-investment-competition-global-finale/ (20 Mar 2026) | VERIFIED-PRIMARY |
| E12 | Academic Director: Prof. Michael Roberts; "M.A. in Statistics"; heads the Wharton Financial Analytics Initiative; research includes "the effect of interest rates on bank lending" | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ | VERIFIED-PRIMARY |
| E13 | Guide p.1: "achieve specific financial goals and meet future cash-flow needs" | https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf | VERIFIED-PRIMARY |
| E14 | Season-start 10y: 1.48 / 3.88 / 4.55 / 3.75 / 4.15 (2021-2025); 2021-09-27 curve 1y 0.09, 2y 0.31, 3y 0.56, 5y 0.98, 7y 1.30, 10y 1.48 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 (and DGS1/2/3/5/7) | VERIFIED-PRIMARY |
| E15 | Jordan payments ≈ $47.3k at the 2021 curve (0.946 of face); Laura $292,264 (0.585); flat break-even for $300k = 5.087%; promise cost at flat 1.48% ≈ $428.9k, at 4% $333.3k, at 4.5% $317.5k, at 5% $302.5k | inline Python, section 5 | ASSUMPTION (par-as-zero, flat rates) |
| E16 | Laura: "After I graduated from Penn in 2018 with a degree in business analytics, I worked in tech as a product manager." | https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/ (6 Apr 2022) | VERIFIED-PRIMARY (professional line only; the page also has personal material, which I did not record) |
| E17 | Pull quote not found on Wharton Magazine, Overachiever, Mochi or Wikipedia pages | fetch_text --grep "believe": NO on each; Goodreads timed out | Search result: unattributed |
| E18 | Case word checks: "volatil" 1 (2026-27) vs 0 in four past cases; hobbies/family words 0 | repo case .txt + past case texts | VERIFIED-REPO-FILE / my count |

---

## 5. Reproduce the numbers (repo root)

```
.venv/bin/python -c "
import numpy as np; from scipy.optimize import brentq
m=[1,2,3,5,7,10]; y=[0.09,0.31,0.56,0.98,1.30,1.48]   # FRED 2021-09-27
pv=sum(5000/(1+np.interp(t,m,y)/100)**t for t in np.arange(10)+0.5); print(round(pv), round(pv/50000,3))
f=lambda r: sum(50000/(1+r)**(6+k) for k in range(10))
print(round(brentq(lambda r: f(r)-300000,0.001,0.2)*100,3), [round(f(r)) for r in (0.0148,0.04,0.045,0.05)])"
```
Output: 47297 0.946 / 5.087 [428906, 333328, 317478, 302509].

---

## 6. Sources (all accessed 2026-09-27)

| Source | URL / path | Status |
|---|---|---|
| Wharton archive (clients and winners 2021-2026) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/ | VERIFIED-PRIMARY |
| Case 2021-22, 2022-23, 2024-25 | https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2021-2022/ (and -2022-2023/, -2024-2025/) | VERIFIED-PRIMARY |
| Case 2023-24, 2025-26 on the same URL pattern | same pattern | 404 (retired) |
| Case 2025-26 copy | https://www.scribd.com/document/965855349/Case-Study-Wharton-Global-Youth-Program | SNIPPET-UNVERIFIED |
| 2023-24 team report | https://www.teenink.com/opinion/all/article/1215809/Profiteering-Peninsula-Panthers-2023-2024-Wharton-Global-High-School-Investment-Competition-Final-Report | SNIPPET-UNVERIFIED |
| Finale articles 2022-2026 | the five /news/ URLs in E6-E11, plus https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/ | VERIFIED-PRIMARY |
| Semifinal/finalist articles 2022-2026 | /news/announcing-the-top-10-teams-advancing-to-our-2022-investment-competition-grand-finale/; /news/celebrating-the-top-10-teams-in-the-2022-2023-wharton-global-high-school-investment-competition/; /news/wharton-global-youth-hosts-five-virtual-events-to-announce-the-2024-investment-competition-finalists/; /news/lets-go-announcing-the-top-10-teams-advancing-to-the-wharton-investment-competitions-2025-global-finale/; the four Top-50 announcement pages (2022-2026) | VERIFIED-PRIMARY |
| Competition main page (academic director) | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ | VERIFIED-PRIMARY |
| 2026-27 Competition Guide | https://upenn.box.com/shared/static/b9kh53xila9czkyznk1xv5yegl3snlc1.pdf | VERIFIED-PRIMARY |
| FRED DGS1-DGS10 | https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10 | VERIFIED-PRIMARY |
| Wharton Magazine interview (2022) | https://magazine.wharton.upenn.edu/digital/a-wharton-grad-from-wuhans-exploration-of-identity/ | VERIFIED-PRIMARY (professional lines only) |
| Global Youth "case study" page | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/case-study/ ("More information coming soon.") | VERIFIED-PRIMARY |
| Global Youth RSS feed (no Laura article yet; latest item 30 Apr 2026) | https://globalyouth.wharton.upenn.edu/feed/ | VERIFIED-PRIMARY |
| Blocked or failed | poetsandquantsforundergrads.com (Cloudflare challenge page today, although Phase A listed it as reachable); Goodreads quotes (timeout); Wayback (not tried; blocked per B1a) | — |
| Repo | `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`; Phase A registers; B1a, B1b, B7a, B7b | VERIFIED-REPO-FILE / prior agents |

---

## 7. Leads for the specialists

- **D1 (rates):**
  - Q4: price the ladder on every 2025 curve too (Treasury CSV). This shows whether $300k was ever enough while the
    case was likely being drafted (2025-26).
  - Q3: build the FR chart "cost of Laura's promise vs flat yield 1%-6%", marking 1.48% (2021) and 5.17% (2026).
  - Write the rate-conditional lock rule and its fallback (long rungs first, per brief section 7).
- **D2 (equity):** Q11. Weight of publishing, media and entertainment names in IVV/VTI (iShares/Vanguard holdings
  files, reachable), to decide whether a human-capital underweight is material.
- **D3 (quant):**
  - Q8: draft a four-line "model card" spec (model, inputs with dates, what is not modelled, how to read the number).
  - Q18: size a plain sleeve-drawdown number for the IPS: the historical worst 12-month fall for a 60/40 sleeve, or
    the p5 one-year sleeve return from strategy_mc.py.
- **D4 (Taiwan/FX):** Q15. Keep TWD to one disclosure sentence plus a US$ label. The 2024-25 "USD" contrast is the
  evidence.
- **D5 (co-sponsors):** Q13. Find evidence that funders value pre-funded operations (BS-17), and wording on who relies
  on a residency's operating budget (residents, partner institutions).
- **D6 (client):**
  - Q1: turn the five case-stated mirrors into a checklist.
  - Q10: pre-commitment language used by private banks.
  - Q9: keep the pull quote unattributed unless a primary source is found. The other B2 agent should keep searching
    her public talks and pages.
- **D7 (Wharton intent):**
  - Q16: find any 2021-22 semifinalist report (Scribd, Teen Ink, school news) showing how the scholarship was funded.
  - Q17: check 2025-26 Top-50 report styles for themes.
  - Recover the 2023-24 Ash case text (Scribd search "Hilary Ash case study") to fill the table's missing row.
- **D9 (plain English):**
  - Q7: turn the word table into a ban list and a use list.
  - Q12: committed/stretch wording.
  - Q19: a four-beat story template (problem, promise, proof, range) with one number per beat.
- **D10 (compliance):** Q2. If the Taiwan tilt is dropped, make sure any existing WInS position in it is sold before
  the notes are chosen, with its own note explaining why (the notes cannot be edited later, R-AN43).
- **Correction for the team's "Why Wharton chose Laura" document:**
  - "Youngest client in recent years" is wrong; the 2022-23 client was stated as 25 (E2).
  - "Three clients in a row fund community infrastructure" holds only for 2024-25, 2025-26 and 2026-27. The 2023-24
    goals were a property renovation and her own firm (E3, SNIPPET-UNVERIFIED).

---

## What this teaches

- **Compare the case with its own history.** Six seasons side by side show what the designers kept, what they
  removed and what they added. What they removed (return targets, hobbies, values words, stock language) tells you
  which old habits no longer score. What they added (certainty, co-sponsors, flexibility) tells you what now does.
- **The same question can have a different right answer in a different year.** A ten-payment promise cost about 95%
  of its face value in 2021 and about 58% in 2026. Interest rates, not cleverness, changed the answer. Good advisers
  say *why now*.
- **Listen to what clients and judges repeat.** Across five finales they asked for the same things: feel understood,
  cut the clutter, reason clearly, plan for the client's emotions in a downturn, see the whole person. A pattern that
  repeats across years is stronger evidence than any single quote.
- **Tailoring is not decoration.** When a case removes personal details, the way to tailor is through the client's
  goals, cash flows and way of thinking. Buying something because the client likes it was never the point.
