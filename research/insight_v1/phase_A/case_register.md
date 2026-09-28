# A1 Case Register: every requirement, number, definition, permission, prohibition and word choice

Agent: A1 (Case Lawyer), insight_v1 run, written 2026-09-27. Authority order: case > guides > criteria page > public
web pages (brief section 1). This file makes no strategy decisions and contains no text meant for submission.

## 0. Summary (read this first)

1. **This year's WInS trading rules are public, and the team has not yet recorded them.** Two SMApply resource pages
   open without logging in: "Trading Details" (https://wghsinvcomp.smapply.us/res/p/trading/) and "FAQs"
   (https://wghsinvcomp.smapply.us/res/p/faqs/). Both were read 2026-09-27 at about 11:40 UTC and are
   VERIFIED-PRIMARY. They state:
   - **$300,000** starting virtual cash (R-W56, R-W85). This equals Laura's 2027 deposit. The $150,000 "will not be
     added to WInS" (R-W59).
   - Trading runs Sept 28 to Nov 6, 2026 (R-W58).
   - **Up to 200 trades** (R-W65), and no single trade larger than twice a security's daily volume (R-W66).
   - Allowed: stocks priced at $5 or more, **any ETF available on WInS**, and **Treasury bonds** (U.S., U.K., Germany,
     France, Italy, the Netherlands) (R-W67 to R-W69, R-W89).
   - **Not allowed**: margin, short selling, stock-secured debt, crypto, derivatives (R-W90).
   - **No required sector allocation or minimum number of sectors** (R-W70). This contradicts the third-party claim
     "sector minimum = team size" recorded in the brief and CLAUDE.md.
   - Commission: $25 per stock trade, $10 per Treasury-bond trade (R-W92).
   - Bond prices update once a day (R-W91).

   **I found no fixed "approved ETF list"; the rule is "any ETF available on WInS".** The team must still check that
   each instrument is actually available in WInS, and confirm with Wharton anything ambiguous (R-AN15, R-AN49).
   Confirm against this year's WInS list and rules before trading.
2. **The repo's official PDFs match the live official files byte for byte.** I downloaded the three Box links shown on
   the public SMApply pages today. Their SHA-256 hashes equal the repo files and `manifest.yaml` (VERIFIED-PRIMARY).
   The repo `.txt` extractions are faithful word for word. The only differences are whitespace, bullet control
   characters, one soft hyphen and two letter-spacing artefacts in pypdf output (section 1.2). The two photos in the
   case contain a little text that the text file does not have (R-C22).
3. **Official sources disagree on what decides the semifinals.** The Rules page says the Top 50 are picked "based on the
   strength of their Investment Policy Statement (IPS) and Final Reports" (R-W24). The SMApply page says the Trading
   Notes Analysis, IPS and Final Report "are evaluated" (R-S9). The case says "Evaluators will consider the three
   deliverables together" (R-C91). See X-8.
4. **Source-citation duties are split across deliverables.** The IPS forbids "formal citations" (R-I55). The Code of
   Conduct requires teams to "properly cite any sources used" (R-W30). The AI policy page says AI use "must be recorded
   in your Works Cited pages" (R-W46). The only compatible reading (INTERPRETATION): the sources, and a record of how AI
   was used, go in the Final Report.
5. **Contacting the client means disqualification** (R-W16, R-W55). Wharton also says "While the client is real, the
   financial scenario is developed specifically for the competition" (R-W4). Laura's real finances and real plans are
   not case facts.
6. **Notable case-design facts** (details in section 7):
   - Contributions total $450,000, less than the $500,000 of nominal payments (R-AN13).
   - The co-sponsor confidence statement is about the contribution falling **within** a range, which has two ends
     (R-AN9).
   - The case never names a currency (R-AN10).
   - The first payment falls on the same date the reserve is set aside (R-AN2).
   - An SMApply FAQ lists permitted investments "for BOTH contributions" (R-AN15).
7. **Field size, 2025-26** (Wharton news page, VERIFIED-PRIMARY): "more than 6,300 registered teams"; "some 2,300 teams
   from 79 countries submitted final reports" (R-W97 to R-W99). The main page counter gives 2,339 teams (R-W10). Last
   year's WInS cash was $500,000; this year it is $300,000.

Entry count: 324 register entries (C 97, I 61, T 36, S 30, W 100), plus 60 anomalies and 24 cross-document items.

### Legend
- Status labels:
  - `VERIFIED-REPO-FILE`: quoted from the official file in `competition/official/2026_27/`.
  - `VERIFIED-PRIMARY`: quoted from the public Wharton or SMApply page, read by me on 2026-09-27 (URL given).
  - `INTERPRETATION`: my reading; never a fact.
  - `DERIVED`: arithmetic on quoted numbers.
- Location: page (p.) and line (L) in the repo `.txt` file. For the SMApply `.md` file, the md line number. For web
  pages, the page section.
- Types: requirement, number, definition, permission, prohibition, format, evaluation, framing, word-choice.
- Quotes keep the source's curly apostrophes (’) where the source uses them.

---

## 1. Method and source checks

### 1.1 Files and hashes
- Official PDFs, repo SHA-256:
  - Client_Profile `bfb653cb…e1fead7`
  - IPS guide `d4aeaca7…06df6a`
  - Trading Notes guide `72bbc4a9…d05d52`

  These match `manifest.yaml`. VERIFIED-REPO-FILE.
- Live downloads, 2026-09-27, `https://upenn.box.com/shared/static/<id>.pdf`:
  - Client case id `i4t4b2n4ycjkev7p78mhyjsvypombkxo`, linked from https://wghsinvcomp.smapply.us/res/p/client/
  - IPS id `0iib496jhswp30c12zhn6b2fret8dl30`
  - Trading Notes id `3pxn798a1lnlifkikj4g56srmg2ijuo6`

  The last two are linked from https://wghsinvcomp.smapply.us/res/p/deliverables/. All three hashes are **identical**
  to the repo files. VERIFIED-PRIMARY.
- PDF metadata (pypdf):
  - Case: created 2026-09-10 15:19 (-04:00), Adobe InDesign 21.4, 4 pages.
  - IPS guide: created 2026-09-09 17:01 (-04:00), 6 pages.
  - Trading Notes guide: created 2026-09-10 15:21 (-04:00), 2 pages.

  All are US Letter (612x792 pt) with no hyperlink annotations. VERIFIED-REPO-FILE.
- The SMApply Deliverables page is **publicly readable** at https://wghsinvcomp.smapply.us/res/p/deliverables/ (read
  2026-09-27). Its text matches the repo transcription `SMApply_Deliverables_Page_2026-09-27.md`. The only differences:
  the live page uses curly apostrophes, and its "Click Here" links point to the Box URLs above. VERIFIED-PRIMARY. The
  repo file's header calls it a "registered-team portal" page, but it opens without logging in.

### 1.2 Text-extraction check (case, IPS guide, Trading Notes guide)
I ran a word-level diff between the repo `.txt` files and a fresh pypdf extraction
(`/home/user/caplet-investment/.venv/bin/python`, pypdf). No word is added, dropped or changed in meaning.
VERIFIED-REPO-FILE. The differences:

| File | Repo .txt | Fresh pypdf | Meaning changed? |
|---|---|---|---|
| Case p.1 L4 | "teacher/advisor" | "teacher/ advisor" (line-wrap space) | No |
| Case p.1 L18 | "per­" (soft hyphen U+00AD) + "sonal" | "per-" + "sonal" | No (the word is "personal") |
| Case p.4, IPS p.1-2 bullets | Some bullets start with a BEL control character (U+0007) before the word | Plain bullet | No; a search for "\x07" hits these |
| IPS p.4 L128 | "ONLY" | "ONL Y" (letter-spacing artefact) | No |
| Trading Notes p.1 L3, L32 | "Team’s", "ANALYSIS" | "T eam’s", "ANAL YSIS" (kerning artefacts) | No |
| All | Blank lines between bullets | Bullets on consecutive lines | No |

**The images carry text that is not in the text files** (checked by viewing the two embedded JPEGs):
- Case p.1 has a portrait photo with no text.
- Case p.2 has a photo of Laura at a book display. It shows the *Messy Roots* cover with the subtitle "A Graphic Memoir
  of a Wuhanese American" and a conference badge marked "SPEAKER".
- The pull quote on p.1 (R-C21) sits in the "MEET LAURA GAO" sidebar. The text layer gives it no attribution line.

---

## 2. Case: `Laura_Gao_2026_Client_Profile.txt` (R-C)

All entries VERIFIED-REPO-FILE unless marked.

### Page 1: framing and biography
- **R-C1** · p.1-4 L2/35/82/122 · format · "Investment Competition Guide" — Every page of the case has this header,
  the same header as the Trading Notes guide. The IPS guide uses a different one.
- **R-C2** · p.1 L3 · framing · "You are a team of young analysts working at an asset management company." — The
  role-play frame: we are professionals at a firm.
- **R-C3** · p.1 L4-5 · framing · "Your portfolio manager (your team’s teacher/advisor who makes the final investment
  decisions for your firm’s portfolio)" — In the fiction, the advisor decides. The real rules forbid this (R-W19,
  R-W87; see R-AN4).
- **R-C4** · p.1 L5 · word-choice · "recently met with a potential client, Laura Gao" — "Potential": she has not
  hired the firm yet.
- **R-C5** · p.1 L5-6 · definition · "a bestselling author, illustrator, entrepreneur, and educator, who is planning
  the next chapter of her career" — Her roles as the case lists them. "Next chapter" is a book metaphor.
- **R-C6** · p.1 L6-7 · framing · "Laura has built a successful creative business by turning ideas into
  opportunities" — Her business is creative and built on ideas.
- **R-C7** · p.1 L7-8 · framing · "she is now seeking thoughtful financial planning to help her achieve her long-term
  goals." — "Thoughtful" is the first of three uses in the case (R-C24, R-C37).
- **R-C8** · p.1 L9-10 · framing · "Your team hopes to develop the investment strategy that Laura ultimately chooses
  as she works toward achieving her future vision." — She will compare strategies and choose one. Ours must win her
  choice.
- **R-C9** · p.1 L12 · framing · "Laura Gao believes stories have the power to change how people see the world." —
  The first thing the case says about her is a belief, not a fact about money.
- **R-C10** · p.1 L13-14 · definition · "Born in Wuhan, China, and raised in Texas, Laura is a bestselling graphic
  novelist, illustrator, entrepreneur, and educator whose work explores identity, belonging, and the power of
  storytelling." — Official bio and themes of her public work. The brief allows the themes; never use them to pick
  investments.
- **R-C11** · p.1 L14-15 · framing · "While studying at the Wharton School, she combined her passion for creativity
  with an entrepreneurial mindset and launched a small business." — She was an entrepreneur while still a student.
- **R-C12** · p.1 L16-17 · number/definition · "She graduated in 2018 with a degree in Statistics & Information
  Decisions Management before beginning her career as a product manager in the technology industry." — 2018; a
  quantitative degree; a tech product manager.
- **R-C13** · p.1 L18-19 · number · "In 2020, Laura published The Wuhan I Know, a comic inspired by her per­sonal
  experiences during the COVID-19 pandemic." — 2020, her first public work named in the case. The line is broken by a
  soft hyphen.
- **R-C14** · p.1 L19-20 · framing · "Originally intended as a response to misinformation and anti-Asian racism" —
  The comic was made to correct misinformation.
- **R-C15** · p.1 L20-22 · framing · "the comic resonated with readers worldwide and ultimately inspired her
  bestselling graphic memoir, Messy Roots." — A small project grew into a larger one.
- **R-C16** · p.1 L22-23 · framing · "Today, her books are read in classrooms around the world and have sparked
  conversations about identity, belonging, and community." — Education reach. "Community" appears again at R-C40.
- **R-C17** · p.1 L24-25 · framing · "Although Laura’s career began in business and technology, she has always
  approached creativity with an entrepreneurial mindset." — Business and creativity together.
- **R-C18** · p.1 L25-26 · framing · "she has combined artistic passion with strategic thinking and a willingness to
  pursue unconventional opportunities." — Willing to take unconventional paths.
- **R-C19** · p.1 L27 · framing · "That philosophy continues to guide Laura as she considers what comes next." — Her
  approach to career choices guides what comes next, but R-C37/R-C38 add a limit.
- **R-C20** · p.1 L28-30 · framing · "MEET LAURA GAO / Storyteller, Entrepreneur, and Creative Visionary" — Sidebar
  headline. "Storyteller" comes first.
- **R-C21** · p.1 L31-33 · framing · "The only person who needs to believe in something is yourself." — Pull quote in
  the sidebar, with no attribution line in the text layer (see R-AN30).
- **R-C22** · p.1-2 images · framing · Image text (not in the .txt): "A Graphic Memoir of a Wuhanese American" (the
  *Messy Roots* cover subtitle) and a "SPEAKER" badge — Shows the public roles of author and speaker. VERIFIED-REPO-FILE
  (viewed the embedded JPEGs).

### Page 2: goals and money
- **R-C23** · p.2 L36-37 · framing · "Looking Ahead" / "Laura has no shortage of ideas for the future." — Many ideas;
  the portfolio serves the chosen ones.
- **R-C24** · p.2 L37-39 · framing · "she recognizes that achieving ambitious goals requires more than creativity
  alone. Thoughtful financial planning and long-term investing will play an important role in turning those ideas
  into reality." — She sees finance as the thing that turns her ideas into reality.
- **R-C25** · p.2 L39-41 · framing · "Working with your portfolio manager, Laura has identified several long-term
  financial objectives that reflect both her entrepreneurial mindset and her passion for innovation." — The goals are
  already set with the portfolio manager (PM). Teams do not choose her goals.
- **R-C26** · p.2 L43 · number · "At the beginning of 2027, Laura plans to invest $300,000 with an asset management
  firm." — $300,000 on 1 Jan 2027. "An" firm, not "your" firm.
- **R-C27** · p.2 L43-45 · number · "She will contribute an additional $150,000 at the beginning of 2028, using
  earnings from publishing advances, speaking engagements, licensing, and other entrepreneurial ventures." —
  $150,000 on 1 Jan 2028. The case says "will", not "may". All the named income sources come from her own work.
- **R-C28** · p.2 L46-47 · definition · "For purposes of the competition, teams should use the following timeline.
  Year 0 is 2026, the present, before any money has been invested." — Year 0 = 2026 = now.
- **R-C29** · p.2 L49-57 · number · "2026 is Year 0." "2027 is Year 1." "2028 is Year 2." "2031 is Year 5." "2033 is
  Year 7." — Only the event years are listed.
- **R-C30** · p.2 L58 · definition · "Any year not listed follows the same pattern: subtract 2026 from the calendar
  year to get its year number." — So 2042 = Year 16 (DERIVED).
- **R-C31** · p.2 L59 · definition · "All contributions and withdrawals occur at the beginning of the applicable year."
  — Every cash flow happens on 1 January.
- **R-C32** · p.2 L59-60 · word-choice · "The ten operating payments are therefore spaced exactly one year apart." —
  Mentions the payments before the case has introduced them (R-AN12).
- **R-C33** · p.2 L61-63 · definition · "Laura’s living expenses and short-term financial needs will be covered by
  income and financial resources outside the portfolio." — No living-cost withdrawals. She has other resources.
- **R-C34** · p.2 L63-65 · prohibition · "Apart from the two contributions described above, she will neither add to
  nor withdraw from the portfolio before 2033." — No other money moves in or out before 2033.
- **R-C35** · p.2 L66-67 · requirement · "The portfolio should therefore be managed to support the goals described
  below." — The portfolio exists for the goals that follow.
- **R-C36** · p.2 L68-69 · framing · "Laura understands that investing involves uncertainty and periods of market
  volatility." — She accepts that markets move.
- **R-C37** · p.2 L69-71 · word-choice · "Although she has been willing to take thoughtful risks throughout her
  entrepreneurial career" — "Although" contrasts her career risk-taking with what she wants now (R-AN16).
- **R-C38** · p.2 L71-74 · requirement · "she wants her investment team to recommend an appropriate balance between
  pursuing growth and protecting the capital required for her goals." — The team recommends the balance. What is
  protected is the capital "required for her goals".
- **R-C39** · p.2 L76 · number · "In 2033, Laura plans to establish a collaborative creative residency in Taiwan." —
  2033; Taiwan; "plans".
- **R-C40** · p.2 L76-80 · definition · "She envisions a small, community-oriented space where artists, writers,
  designers, entrepreneurs, and educators can temporarily live, work, teach, and collaborate." — Small and
  community-oriented; stays are temporary.

### Page 3: the commitment, the reserve, the facility, co-sponsors
- **R-C41** · p.3 L83 · definition · "Establishing the residency will require funding for the facility as well as
  reliable support for its early operations." — Two needs: the facility, and operations. The ten years are called
  "early operations".
- **R-C42** · p.3 L84 · requirement · "The investment portfolio must fund the operating commitment described below"
  — The portfolio must fund it.
- **R-C43** · p.3 L84-85 · permission · "and may also cover part of the facility’s cost." — The facility is optional
  and partial ("part").
- **R-C44** · p.3 L85-86 · permission · "Any remaining facility cost, and any operating support beyond Laura’s
  commitment, may come from co-sponsors, grants, collaborators, program fees, continued business income, or other
  sources." — Outside money is allowed for the rest of the facility and for extra operating support. The list includes
  "continued business income".
- **R-C45** · p.3 L88-89 · number · "Laura will make ten annual payments of $50,000 toward the residency’s operating
  expenses, one at the beginning of each year from 2033 through 2042." — 10 × $50,000, on 1 Jan 2033 to 1 Jan 2042.
- **R-C46** · p.3 L90 · definition · "For purposes of the competition, each payment is a fixed $50,000 and is not
  adjusted for inflation." — Payments are fixed in nominal dollars (not raised for inflation).
- **R-C47** · p.3 L91 · requirement · "All ten payments must be funded by the investment portfolio with a high degree
  of certainty." — The core requirement. "High degree of certainty" is not defined (R-AN1).
- **R-C48** · p.3 L91-92 · prohibition · "Teams may not rely on co-sponsors, grants, program fees, or other outside
  funding to meet this requirement." — No outside money for the ten payments.
- **R-C49** · p.3 L92-93 · definition · "Funding the residency beyond the final payment in 2042 is outside the scope of
  the competition." — Nothing after 2042.
- **R-C50** · p.3 L94-95 · requirement · "At the beginning of 2033, before making the first operating payment or
  contributing to the facility, Laura will set aside a portion of the portfolio to fund the ten payments." — Order on
  1 Jan 2033: reserve first, then the payment and the facility (R-AN2).
- **R-C51** · p.3 L95 · definition · "This set-aside is called the operating reserve." — The official term.
- **R-C52** · p.3 L95-96 · requirement · "Teams must recommend its size and initial asset composition" — Two
  deliverable items: how big, and what it holds at first.
- **R-C53** · p.3 L96-97 · requirement · "and explain how its composition should change, if at all, as the annual
  payments approach and are made." — "If at all": a reserve that never changes is allowed (R-AN27).
- **R-C54** · p.3 L97-98 · requirement · "They should also define what they consider a high degree of funding
  certainty" — The team writes the definition. Note "funding certainty" here versus "certainty" at L91.
- **R-C55** · p.3 L98 · requirement · "explain how they evaluated that level of certainty" — The method must be shown.
- **R-C56** · p.3 L98-99 · requirement · "and identify the assumptions supporting their recommendation." — Assumptions
  must be listed.
- **R-C57** · p.3 L101-102 · requirement · "After establishing the operating reserve in 2033, Laura must decide how much
  of the remaining portfolio she can responsibly contribute toward the cost of establishing the residency facility." —
  The facility money comes only from what is left after the reserve. Laura decides.
- **R-C58** · p.3 L102-103 · framing · "She recognizes that committing all remaining assets could limit her financial
  flexibility as the project develops." — Flexibility is about the project's future needs.
- **R-C59** · p.3 L104 · definition · "There is no predetermined facility contribution." — No target amount is given.
- **R-C60** · p.3 L104-106 · requirement · "Teams must recommend and justify the extent to which Laura can responsibly
  contribute, based on their investment strategy, projected portfolio outcomes, assumptions, and understanding of her
  goals." — The recommendation must rest on four bases. "Extent" could be a share or a rule, not only a dollar amount
  (R-AN20).
- **R-C61** · p.3 L106-107 · permission · "Teams are not expected to determine the size or investment composition of a
  separate contingency fund or endowment." — Not required. It is not forbidden either.
- **R-C62** · p.3 L109 · number · "Laura plans to begin approaching potential co-sponsors in 2031, two years before
  the residency is established." — 2031 = Year 5 = two years before 2033.
- **R-C63** · p.3 L110 · requirement · "At that time, she will need to describe how much she expects to contribute
  toward the facility in 2033." — A 2031 statement about 2033.
- **R-C64** · p.3 L110-112 · framing · "A meaningful personal contribution may signal that the residency is
  financially viable, demonstrate Laura’s commitment to the project, and make potential co-sponsors more willing to
  contribute." — Three reasons a contribution helps. "May" is hedged.
- **R-C65** · p.3 L112-113 · framing · "In 2031, however, the value of her portfolio in 2033 remains uncertain." —
  The case states the uncertainty outright.
- **R-C66** · p.3 L114-115 · framing · "If Laura promises more than she can ultimately contribute, she could damage her
  credibility and lose the confidence or participation of co-sponsors." — Overpromising is the named risk.
- **R-C67** · p.3 L115-116 · requirement · "Rather than promising one exact amount, she wants to communicate a credible
  range for her potential contribution." — A range, not a single number.
- **R-C68** · p.3 L117 · requirement · "Teams must recommend the dollar range Laura should communicate" — Expressed in
  dollars.
- **R-C69** · p.3 L117-118 · requirement · "and state how confident they are that her 2033 contribution will fall
  within that range." — A confidence level for landing "within" the range, which has two ends (R-AN9).
- **R-C70** · p.3 L118-119 · requirement · "They should explain how favorable and unfavorable market outcomes could
  affect the amount she can provide." — Good and bad scenarios.
- **R-C71** · p.3 L119-120 · requirement · "The proposed range must also protect the portfolio’s ability to fund the
  ten-year operating commitment." — The promised range cannot put the payments at risk.

### Page 4: strategy rules, deliverables, scope
- **R-C72** · p.4 L123-124 · requirement · "Each team must also draft part of Laura’s fundraising materials describing
  this potential contribution for prospective co-sponsors." — Students write "part" of her fundraising material (a
  Final Report item; students write it themselves, per R-W26).
- **R-C73** · p.4 L126 · framing · "There is no single correct strategy for achieving Laura’s goals." — Many valid
  answers.
- **R-C74** · p.4 L126-128 · permission · "Teams may reach different conclusions about risk, asset allocation,
  liquidity, return expectations, funding confidence, the facility contribution, and the financial flexibility Laura
  should preserve." — Seven dimensions where answers may differ.
- **R-C75** · p.4 L129 · definition · "The WInS portfolio represents each team’s implementation of its investment
  strategy during the competition." — WInS = putting the strategy into practice.
- **R-C76** · p.4 L130 · definition · "It does not determine Laura’s actual portfolio value at the beginning of 2027."
  — WInS results never become her starting value.
- **R-C77** · p.4 L130-132 · requirement · "For long-term projections, teams should begin with Laura’s $300,000
  investment in 2027, add the $150,000 contribution in 2028, and use reasonable return assumptions consistent with
  their strategy." — The projection recipe.
- **R-C78** · p.4 L132-133 · prohibition · "Gains or losses generated during the WInS trading period should not be
  added to or subtracted from Laura’s portfolio projections." — Keep WInS profit and loss (P&L) out of projections.
- **R-C79** · p.4 L134 · requirement · "Each team must develop and justify an investment strategy that:" — Five tests
  follow.
- **R-C80** · p.4 L136 · requirement · "Supports the ten-year operating commitment with a high degree of certainty." —
  Test 1.
- **R-C81** · p.4 L138 · requirement · "Determines a responsible facility contribution for the residency." — Test 2.
- **R-C82** · p.4 L140-141 · requirement · "Addresses how investment uncertainty could affect both the operating
  commitment and the facility contribution." — Test 3: uncertainty for both goals.
- **R-C83** · p.4 L143 · requirement · "Communicates Laura’s potential facility contribution to co-sponsors clearly and
  credibly." — Test 4. Almost the same words as the Creativity criterion (R-S28).
- **R-C84** · p.4 L145 · requirement · "Preserves appropriate financial flexibility when determining the facility
  contribution." — Test 5.
- **R-C85** · p.4 L146-148 · requirement · "Teams should identify and explain their assumptions about investment
  performance, the timing of cash flows, outside funding, the effect of inflation on portfolio projections and facility
  costs, and the financial flexibility Laura should preserve." — Five assumption areas, including inflation's effect
  on facility costs (R-AN8).
- **R-C86** · p.4 L148-149 · requirement · "They should also consider how favorable and unfavorable investment outcomes
  would affect their recommendations." — Scenario analysis.
- **R-C87** · p.4 L150 · definition · "Teams will demonstrate their work through three connected deliverables:" —
  "Connected".
- **R-C88** · p.4 L152-153 · definition · "Trading Notes Analysis. This shows how selected investment decisions
  reflected, tested, or refined the team’s developing strategy." — The strategy may be "developing" at this stage.
- **R-C89** · p.4 L155-156 · definition · "Investment Policy Statement. This formally establishes the strategy and the
  team’s decision-making framework." — "Formally establishes" and a "decision-making framework".
- **R-C90** · p.4 L158-160 · definition · "Final Report. This evaluates how that strategy was implemented and presents
  the team’s analysis and recommendations for Laura’s operating commitment, facility contribution, financial
  flexibility, and communication with co-sponsors." — The Final Report carries the numbers.
- **R-C91** · p.4 L161 · evaluation · "Evaluators will consider the three deliverables together." — The deliverables
  are judged as one package (compare R-W24).
- **R-C92** · p.4 L161-162 · requirement · "Teams should use each deliverable for its intended purpose while
  maintaining a clear and consistent investment strategy across all three." — One strategy across all three.
- **R-C93** · p.4 L162-163 · number · "Detailed Final Report requirements will be released at the beginning of Week 7."
  — Week 7 = 9 Nov (R-S19).
- **R-C94** · p.4 L164 · definition · "The total cost of the facility has not been determined." — Facility cost is
  unknown by design.
- **R-C95** · p.4 L164-166 · permission · "Teams are not expected to estimate that cost, prepare a construction budget,
  determine the project’s total funding gap, or develop a detailed business plan for the residency." — Four things
  that are out of scope.
- **R-C96** · p.4 L166-167 · requirement · "Their primary focus should remain on the investment strategy and how much
  the portfolio can responsibly provide toward Laura’s goals." — Stay on investing.
- **R-C97** · p.4 L168-169 · permission · "For purposes of the competition, teams do not need to account for personal
  income taxes, capital gains taxes, or the legal and regulatory requirements of establishing a residency in Taiwan." —
  Taxes and Taiwan law are out of scope. Currency is not mentioned (R-AN10).

### Derived arithmetic from case numbers (DERIVED; no assumptions)
- 10 × $50,000 = **$500,000** in nominal payments. Contributions total $300,000 + $150,000 = **$450,000**. The gap is
  $50,000 before any facility contribution.
- Payment dates: Years 7 to 16 (2033 to 2042). The last payment is 9 years after the first.
- From deposit to first payment: 6 years for the $300,000 (Year 1 to Year 7) and 5 years for the $150,000 (Year 2 to
  Year 7).
- 2031 to 2033 = 2 years (Year 5 to Year 7).
- Competition "Year 0" (2026) is when WInS trading happens.

---

## 3. IPS guide: `2026_WGY_Investment_Policy-FINAL.txt` (R-I)

All entries VERIFIED-REPO-FILE.

### Page 1: purpose and prompts
- **R-I1** · p.1-6 header · format · "Investment Policy Statement (IPS)" — The page header, which differs from the case
  and Trading Notes guide.
- **R-I2** · p.1 L3-4 · definition · "An Investment Policy Statement (IPS) outlines an investor’s financial goals, risk
  tolerance, and guidelines for managing a portfolio." — The official definition includes "risk tolerance" and
  "guidelines".
- **R-I3** · p.1 L4-5 · definition · "It helps investors stay focused on long-term objectives and make disciplined
  decisions during changing market conditions." — An IPS is a tool for behaving well in bad markets.
- **R-I4** · p.1 L6-7 · framing · "Your investment strategy is the cornerstone of the Wharton Global High School
  Investment Competition, and your IPS is where you clearly articulate that strategy." — "Cornerstone". Repeated on the
  SMApply page (R-S16).
- **R-I5** · p.1 L8-9 · requirement · "Your strategy should explain how you will invest your client’s money to support
  their financial goals and future cash flow needs while managing risk and uncertainty." — Goals, cash flows, risk.
- **R-I6** · p.1 L9-10 · requirement · "It should reflect your client’s goals, time horizons, liquidity needs, desired
  degree of funding certainty, and need for financial flexibility." — Five items to reflect. "Desired degree of funding
  certainty" belongs in the IPS itself.
- **R-I7** · p.1 L12 · word-choice · "There is no single “correct” investment strategy for your client." — "Correct"
  is in quotation marks.
- **R-I8** · p.1 L12-13 · requirement · "Your team should use research and analysis to develop an approach that
  reflects your client’s financial goals, funding needs, and changing time horizons." — "Changing" time horizons.
- **R-I9** · p.1 L16 · requirement · "What is the central idea behind your investment strategy?" — Prompt 1: one
  central idea.
- **R-I10** · p.1 L18 · requirement · "What principles will guide your investment decisions?" — Prompt 2: principles.
- **R-I11** · p.1 L20 · requirement · "How does your strategy balance growth, risk, liquidity, funding reliability, and
  financial flexibility?" — Prompt 3: five things to balance.
- **R-I12** · p.1 L22-23 · requirement · "How will the portfolio’s asset allocation and composition change as future
  funding needs approach and payments are made?" — Prompt 4 assumes the allocation changes over time (a glide path;
  compare the case's "if at all", R-C53).
- **R-I13** · p.1 L25-26 · requirement · "How will your strategy protect the operating commitment while preserving
  flexibility for a responsible facility contribution?" — Prompt 5: protection versus flexibility.
- **R-I14** · p.1 L27-28 · requirement · "Always remember who your strategy is designed to serve. Your client’s profile
  and financial goals should remain at the center of your investment decisions." — Client first.
- **R-I15** · p.1 L30 · format · "Your IPS submission has two parts." — Pitch + IPS (the title page is extra).
- **R-I16** · p.1 L31-33 · format · "Investment Strategy Elevator Pitch" / "Maximum 50 words" — Hard limit: 50 words.
- **R-I17** · p.1 L35-36 · requirement · "Quickly summarize your team’s investment strategy. Clearly communicate the
  central idea behind your approach and how it is designed to support your client’s financial goals and future
  funding needs." — The pitch must carry the central idea plus how it serves her goals.
- **R-I18** · p.1 L37-39 · format · "Investment Policy Statement" / "Maximum 500 words" — Hard limit: 500 words.
- **R-I19** · p.1 L41 · requirement · "Clearly explain your team’s investment strategy and the reasoning behind it." —
  Strategy plus reasons.

### Page 2: content expectations and the freeze
- **R-I20** · p.2 L45-46 · requirement · "Your IPS should demonstrate how your strategy is tailored to your client’s
  financial goals, time horizons, and needs." — Tailoring.
- **R-I21** · p.2 L46-47 · requirement · "Explain how your team will approach risk and return, liquidity, portfolio
  construction and diversification, and planned changes in the portfolio as future funding needs approach." — Four
  topics, including "planned changes".
- **R-I22** · p.2 L48-50 · requirement · "Your IPS should also establish your strategic approach to preparing for the
  operating commitment, managing the operating reserve’s asset composition over time, determining a responsible
  facility contribution, and preserving appropriate financial flexibility." — The approach to the reserve and the
  facility belongs in the IPS. The numbers do not (R-I31).
- **R-I23** · p.2 L51-52 · requirement · "Focus on the strategy and decision-making framework that guide your
  portfolio rather than describing individual investments or presenting detailed financial calculations." — Rules and
  framework, not tickers or maths.
- **R-I24** · p.2 L53-55 · requirement · "Your IPS should make it clear:" / "What your team is trying to accomplish for
  the client" — Clarity item 1.
- **R-I25** · p.2 L57 · requirement · "Why your strategy is appropriate for the client and their financial goals" —
  Item 2.
- **R-I26** · p.2 L59 · requirement · "How your strategy balances growth, liquidity, funding reliability, risk, and
  financial flexibility" — Item 3. Same five words as R-I11, in a different order.
- **R-I27** · p.2 L61-62 · requirement · "How your strategy will guide portfolio construction and investment decisions
  as the client’s needs change" — Item 4: rules that guide future decisions.
- **R-I28** · p.2 L64-65 · requirement · "How your approach will protect the required operating payments while
  supporting a responsible facility contribution" — Item 5. "Required" payments.
- **R-I29** · p.2 L66 · permission · "You do not need to address these points separately." — No checklist structure is
  needed.
- **R-I30** · p.2 L66-67 · evaluation · "Your goal is to present a clear, cohesive, and well-supported investment
  strategy." — Three quality words.
- **R-I31** · p.2 L68-69 · permission · "The IPS is not expected to include final operating-reserve calculations,
  detailed portfolio projections, a final facility-contribution range, or the draft communication to co-sponsors." —
  Four items that stay out of the IPS.
- **R-I32** · p.2 L69-70 · requirement · "These elements will be developed and supported in the Final Report using the
  strategy established in the IPS." — The Final Report numbers must follow from the IPS strategy.
- **R-I33** · p.2 L72 · evaluation · "Your IPS is the foundation of your Final Report and will be evaluated." — The
  IPS is scored.
- **R-I34** · p.2 L73 · definition · "Once submitted, the IPS becomes the official record of your team’s investment
  strategy." — The IPS is the official record.
- **R-I35** · p.2 L73-74 · prohibition · "Your team may not revise its investment strategy after the submission
  deadline." — The strategy freezes on 6 Nov.
- **R-I36** · p.2 L75 · requirement · "Your portfolio and Final Report should reflect the strategy established in your
  IPS." — The WInS portfolio and the Final Report must match the IPS.
- **R-I37** · p.2 L75-78 · definition · "In the Final Report, your team will evaluate how effectively it implemented
  that strategy and present its analysis and recommendations for the operating commitment, facility contribution,
  financial flexibility, and communication with co-sponsors under varying investment outcomes." — The Final Report is
  self-evaluation plus recommendations under different scenarios.

### Page 3: format rules (the disqualification rules)
- **R-I38** · p.3 L82 · requirement · "Please follow these directions carefully." — Emphatic.
- **R-I39** · p.3 L82-83 · prohibition · "Submissions that do not meet the requirements below will not be considered
  for semifinal selection." — Breaking a format rule rules the team out of the semifinals.
- **R-I40** · p.3 L84-85 · format · "Page 1: Title Page" / "1 page maximum" — One page.
- **R-I41** · p.3 L86-90 · format · "Official team name" / "This should be the same as what you submitted with your
  official team roster." — Must match the roster.
- **R-I42** · p.3 L92-94 · format · "Finalized team member names" / "These should be the same as what was submitted
  with your official roster." — Must match the roster.
- **R-I43** · p.3 L96 · format · "Format: First Name, Last Initial" — e.g. "Jordan A." (R-I59).
- **R-I44** · p.3 L98-100 · format · "WInS username" / "This is the team’s username for logging into the WInS
  platform." — The username, not the team name (R-W86).
- **R-I45** · p.3 L101 · permission · "Formatting choices not specified below are left to the team’s discretion." —
  Appears after the title-page list, and it is unclear whether it covers the title page or the whole file (R-AN37).
- **R-I46** · p.3 L101-102 · requirement · "Keep the presentation simple and focus on communicating the investment
  strategy clearly." — Simplicity is asked for directly.
- **R-I47** · p.3 L103-104 · format · "Pages 2 and 3: Investment Strategy" / "2-page maximum" — The pitch and the IPS
  together fit in 2 pages.
- **R-I48** · p.3 L105-109 · format · "Investment Strategy Elevator Pitch, maximum 50 words" / "Investment Policy
  Statement, maximum 500 words" — Limits restated.
- **R-I49** · p.3 L112 · format · "Font: Times New Roman" — Required font.
- **R-I50** · p.3 L114 · format · "Size: 12-point" — Required size.
- **R-I51** · p.3 L116 · format · "Spacing: Double-spaced" — Required spacing.
- **R-I52** · p.3 L118 · format · "Margins: 1 inch on all sides" — Required margins.
- **R-I53** · p.3 L120 · format · "Submit as a PDF through SurveyMonkey Apply." — PDF only.
- **R-I54** · p.3 L122 · number · "Maximum file size: 5 MB." — 5 MB cap.
- **R-I55** · p.3 L123 · prohibition · "Graphics, charts, images, attachments, external links, footnotes, and formal
  citations are not permitted." — Seven banned elements.
- **R-I56** · p.3 L124 · permission · "Teams should use research and analysis to develop their strategy, but sources do
  not need to be cited in the IPS." — Research is expected but not cited in the IPS.
- **R-I57** · p.3 L125 · requirement · "Relevant sources and supporting evidence must be included in the Final
  Report." — Citations move to the Final Report.

### Pages 4-6: sample layout
- **R-I58** · p.4 L128 · format · "ILLUSTRATIVE FORMAT EXAMPLE | PLACEHOLDER CONTENT ONLY" — The sample is for layout
  only.
- **R-I59** · p.4 L129-131 · format · "SAMPLE TEAM NAME" / "Jordan A. | Taylor B. | Casey C. | Morgan D." / "WInS
  Username: sample_team-1234567" — Sample title page: names separated by pipes, with the label "WInS Username:".
- **R-I60** · p.5 L135/L139 · format · Section headings "Investment Strategy Elevator Pitch" and "Investment Policy
  Statement" — The sample puts the pitch and the IPS on the same page under two headings.
- **R-I61** · p.5-6 L136-174 · number · Placeholder lengths: pitch 41 words; IPS placeholder about 394 words running
  onto p.6; 13-15 words per line. DERIVED (word count of the placeholder). This gives a rough guide to how many words
  fit per line (R-AN39).

---

## 4. Trading Notes guide: `2026_WGY_Trading_Notes_Analysis-FINAL.txt` (R-T)

All entries VERIFIED-REPO-FILE.

- **R-T1** · p.1-2 header · format · "Investment Competition Guide" — Same header as the case.
- **R-T2** · p.1 L3 · framing · "What Was Your Team’s Decision-Making Process?" — The deliverable's title question is
  about process.
- **R-T3** · p.1 L4-6 · definition · "The purpose of this deliverable is to demonstrate how your team’s investment
  decisions reflected the strategy it developed for the client, including its approach to growth, risk, liquidity,
  funding reliability, financial flexibility, and future cash-flow needs." — Purpose, plus six topics.
- **R-T4** · p.1 L7 · framing · "Successful investing is not simply about selecting individual stocks." — A warning
  against stock picking for its own sake.
- **R-T5** · p.1 L7-8 · framing · "It requires making disciplined decisions that consistently support an overall
  investment strategy." — Discipline and consistency.
- **R-T6** · p.1 L8-9 · requirement · "Throughout the competition, your Trading Notes should document the research,
  analysis, and reasoning behind your investment decisions." — Every note should record research and reasoning.
- **R-T7** · p.1 L9-10 · evaluation · "Collectively, they provide evidence of how your team has put its strategy into
  practice." — The notes are evidence.
- **R-T8** · p.1 L11 · requirement · "For this analysis, select three investment decisions that best illustrate your
  team’s strategic thinking." — Three decisions, chosen by the team.
- **R-T9** · p.1 L11-13 · requirement · "Explain the reasoning behind each decision, how it aligned with, tested, or
  refined your overall investment strategy, and how it supported the client’s goals, funding needs, or risk
  considerations." — Three things to explain.
- **R-T10** · p.1 L14-15 · requirement · "Collectively, the decisions should demonstrate how your team used individual
  investments as part of a cohesive portfolio strategy." — The three together should show one portfolio logic.
- **R-T11** · p.1 L15-16 · evaluation · "The focus should be on the quality of your reasoning and the intended role of
  each decision, not simply whether an investment gained or lost value during the competition." — Reasoning over
  profit and loss.
- **R-T12** · p.1 L17 · number · "Your team will formally present its investment strategy in the Investment Policy
  Statement (IPS) in Week 6." — IPS = Week 6 (6 Nov).
- **R-T13** · p.1 L18-19 · permission/requirement · "Although your strategy may continue to evolve as you conduct
  additional research and evaluate new information, you should already be using a clear strategic approach to guide
  your investment decisions." — Change is allowed before the IPS, but a clear approach is expected already.
- **R-T14** · p.1 L20-22 · permission · "At this stage, your team is not expected to calculate the final size of the
  operating reserve, complete long-term portfolio projections, determine Laura’s facility contribution, or draft her
  communication to co-sponsors." — Four items not expected.
- **R-T15** · p.1 L22 · definition · "These recommendations will be developed in the Final Report." — Where they go.
- **R-T16** · p.1 L22-23 · requirement · "The Trading Notes Analysis should focus on your investment decisions and
  their relationship with your developing strategy." — Focus.
- **R-T17** · p.1 L24-26 · permission · "Important" / "The Trading Notes you select do not need to correspond to
  investments that remain in your portfolio at the end of the competition." — The note trades may be sold later.
- **R-T18** · p.1 L26-27 · permission · "A decision can still demonstrate thoughtful analysis and strategic thinking
  even if your team later sells the investment or changes its approach." — Changing course is not penalised.
- **R-T19** · p.1 L28 · evaluation · "What matters is that each Trading Note provides evidence of your team’s
  decision-making process." — The note is evidence of process.
- **R-T20** · p.1 L29-30 · requirement · "Your reflections should clearly explain how each decision supported, tested,
  or refined your overall investment strategy." — Supported / tested / refined.
- **R-T21** · p.1 L30-31 · requirement · "The analysis should be consistent with the strategic approach your team is
  developing and will later articulate in its IPS." — The notes must be consistent with the future IPS.
- **R-T22** · p.2 L35 · format · "Trading Note Example" — An official sample.
- **R-T23** · p.2 L36-37 · framing · "We are purchasing shares of an intermediate-term U.S. Treasury bond ETF to reduce
  portfolio volatility and begin preparing for Laura’s future operating commitment." — Wharton's own example: a
  Treasury bond fund for the payments.
- **R-T24** · p.2 L37-38 · framing · "The position provides income and greater stability than equities, although
  interest-rate changes may affect its value." — The example names a risk of its own trade.
- **R-T25** · p.2 L38-39 · framing · "This trade supports our plan to balance continued growth with reliable future
  cash flows as the residency funding date approaches." — The example describes shifting towards safer assets as the
  date nears.
- **R-T26** · p.2 L36-39 · number · The example note is 59 words, about 415 characters. DERIVED. Gives a length scale
  for a WInS note. No WInS character limit is stated.
- **R-T27** · p.2 L42 · requirement · "Select three (3) Trading Notes from trades your team executed in WInS." — Exactly
  three, from executed trades.
- **R-T28** · p.2 L44 · requirement · "Include each Trading Note exactly as it appears in WInS." — Copy it word for word,
  with no edits.
- **R-T29** · p.2 L46 · format · "For EACH Trading Note, write a reflection of 100 words or fewer explaining:" — 100
  words or fewer per reflection.
- **R-T30** · p.2 L48 · requirement · "Why your team made the investment decision." — Reflection item 1.
- **R-T31** · p.2 L50 · requirement · "How the decision aligned with your overall investment strategy." — Item 2.
- **R-T32** · p.2 L52 · requirement · "How the decision supported the client’s goals, funding needs, or risk
  considerations." — Item 3.
- **R-T33** · p.2 L53 · requirement · "The Trading Notes must correspond to trades executed in WInS." — Must match real
  WInS trades.
- **R-T34** · p.2 L53 · word-choice · "Yes, we will verify this." — Unusually emphatic (R-AN42).
- **R-T35** · p.2 L54 · format · "Your team will submit their trading notes via the SurveyMonkey Apply form." — A form,
  not a file upload.
- **R-T36** · whole guide · format (omission) · The guide sets no font, file type, page limit or citation rule, and
  says nothing on whether the note text counts toward the 100 words. VERIFIED-REPO-FILE (absence). The form may add
  rules. Check the SMApply form before 23 Oct.

---

## 5. SMApply Deliverables page: `SMApply_Deliverables_Page_2026-09-27.md` (R-S)

VERIFIED-REPO-FILE. Also checked live at https://wghsinvcomp.smapply.us/res/p/deliverables/ on 2026-09-27
(VERIFIED-PRIMARY, identical text).

- **R-S1** · L3 · framing · "registered-team portal; text pasted by Team Leader Ray" — The repo note. The page is in
  fact public (section 1.1).
- **R-S2** · L6 · word-choice · "The 2026-2027 has four REQUIRED Deliverables:" — The noun after "2026-2027" is
  missing. "REQUIRED" is in capitals.
- **R-S3** · L8 · number · "Team Roster (Due: October 9; no later than 5:00 p.m. ET)" — 9 Oct, 5 pm Eastern Time.
- **R-S4** · L9 · number · "Trading Notes Analysis (Due: October 23; no later than 5:00 p.m. ET)" — 23 Oct.
- **R-S5** · L10 · number · "Investment Policy Statement (Due: November 6; no later than 5:00 p.m. ET)" — 6 Nov.
- **R-S6** · L11 · requirement · "IMPORTANT: Trading ends and your portfolio is locked." — The portfolio locks on the
  IPS due date.
- **R-S7** · L12 · number · "Final Report & Official School Documentation (Due: December 4; no later than 5:00 p.m.
  ET)" — 4 Dec.
- **R-S8** · L14 · requirement · "Team must submit all the deliverables, and meet their necessary requirements, in
  order to receive a digital credential." — Needed for the digital credential.
- **R-S9** · L15 · evaluation · "Your Trading Notes Analysis, Investment Policy Statement and Final Report are
  evaluated." — Three deliverables are scored. The roster is not.
- **R-S10** · L16 · requirement · "All deliverables must be submitted via your team's SurveyMonkey Apply account." —
  The submission channel.
- **R-S11** · L17 · prohibition · "We will not grant any deadline extensions." — No extensions.
- **R-S12** · L22 · prohibition · "Once your official team roster is submitted, teams may not change their members." —
  Members are locked after 9 Oct.
- **R-S13** · L23-32 · requirement · Roster fields: "Full Name – Every Student", "Email – Every Student (NOTE: A unique
  email must be provided for each student.)", "Birthday (Month, Day, Year) - Every Student", "Anticipated Graduation
  Year – Every Student", "Official Team Name", "School Country", "School State (U.S. school only)", "School City",
  "Official School Website (URL)" — Personal data. It must never go in the repo (brief privacy rule).
- **R-S14** · L35 · definition · "The purpose of this deliverable is to demonstrate how your team's investment
  decisions reflected the strategy it developed for the client." — Same as the guide, shortened.
- **R-S15** · L36 · format · Trading Notes instructions = Box link `3pxn798a…` — The same file as the repo PDF (hash
  match).
- **R-S16** · L39 · framing · "Your investment strategy is the cornerstone of the Wharton Global High School
  Investment Competition, and your Investment Policy Statement is where you clearly articulate that strategy." — Same
  as R-I4.
- **R-S17** · L40 · format · IPS instructions = Box link `0iib496j…` — Same file (hash match).
- **R-S18** · L43 · definition · "In your Final Report, your team will evaluate how it implemented its investment
  strategy and present its analysis and recommendations for achieving Laura's goals." — The Final Report's purpose.
- **R-S19** · L44 · number · "Detailed Final Report instructions and requirements will be shared on November 9." —
  9 Nov = Week 7.
- **R-S20** · L45 · requirement · "We require official documentation from your school to ensure your team is in
  compliance with the Competition Rules." — School documentation is required.
- **R-S21** · L45 · requirement · "Do not wait until the last minute to request documentation." — Ask the school
  early.
- **R-S22** · L45 · format · "This will be submitted along with your Final Report as a separate file." — A separate
  file.
- **R-S23** · L46 · word-choice · "Sample Documentation: Coming soon" — Not yet published.
- **R-S24** · L49 · evaluation · "Investment Strategy: Presents a clear and creative investment thesis; demonstrates
  disciplined planning across Laura's changing time horizons and cash-flow needs; uses appropriate diversification;
  and maintains consistency with the team's IPS." — Criterion 1 has four parts. "Creative" and "appropriate
  diversification" are both named.
- **R-S25** · L51 · evaluation · "Client Knowledge and Objectives: Tailors the strategy to Laura's circumstances,
  priorities, risk considerations, and residency goals; demonstrates a thoughtful understanding of the client; and
  presents recommendations that can earn her confidence." — Criterion 2. "Earn her confidence" matches the case's
  "ultimately chooses" (R-C8).
- **R-S26** · L53 · evaluation · "Portfolio Analysis: Demonstrates understanding and effective use of investment
  concepts and tools; integrates quantitative and qualitative analysis; and uses reasonable assumptions and
  projections to evaluate funding reliability, the facility contribution, and financial flexibility under varying
  market outcomes." — Criterion 3: numbers and words, and scenarios.
- **R-S27** · L55 · evaluation · "Articulation of Competition Experience: Demonstrates teamwork, communication, and
  learning; clearly explains the team's research and decision-making process; and reflects meaningfully on the team's
  growth and response to challenges." — Criterion 4: process and growth.
- **R-S28** · L57 · evaluation · "Creativity and Presentation: Presents a compelling, well-organized narrative in an
  authentic team voice; uses data effectively to support conclusions; demonstrates original thinking and meaningful
  reflection; and communicates Laura's potential facility contribution and investment uncertainty clearly and credibly
  to prospective co-sponsors." — Criterion 5. The co-sponsor message is scored here.
- **R-S29** · L48-57 · evaluation (omission) · No weights, no scoring scale, and no note on which criterion applies to
  which deliverable. VERIFIED-REPO-FILE (absence).
- **R-S30** · L6-17 · word-choice · The page lists four "REQUIRED" deliverables (including the roster and school
  documentation). The case speaks of "three connected deliverables" (R-C87). Both hold: three are evaluated, four are
  required.

---

## 6. Public Wharton and SMApply web pages (R-W)

All entries VERIFIED-PRIMARY, read 2026-09-27 between 11:38 and 11:45 UTC with curl through the session proxy. The
text was extracted from the HTML. Quotes are exact apart from spacing around bold tags.

Page keys:
- [MAIN] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ (also reached from
  /investment-competition/ and /investment-competition/rules/ by redirect)
- [RULES] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/
- [FAQ] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/
- [REG] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/register-now/
- [AI] https://globalyouth.wharton.upenn.edu/ai-policy/
- [NEWS] https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
  (listed on MAIN as January 27, 2026)
- [ARCH] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/archive/
- [S-HOME] https://wghsinvcomp.smapply.us/
- [S-CLIENT] https://wghsinvcomp.smapply.us/res/p/client/
- [S-TRADE] https://wghsinvcomp.smapply.us/res/p/trading/ (page title "Trading Details")
- [S-WINS] https://wghsinvcomp.smapply.us/res/p/wins/
- [S-FAQ] https://wghsinvcomp.smapply.us/res/p/faqs/
- [S-DELIV] https://wghsinvcomp.smapply.us/res/p/deliverables/

These slugs returned 404: trading-rules, case-study, resources, approved-securities, key-dates.

### Main page [MAIN]
- **R-W1** · [MAIN] top · framing · "Registration for the 2026-2027 Competition is closed." — Registration is closed.
- **R-W2** · [MAIN] intro · definition · "a free, experiential investment challenge for high school students (9th to
  12th grade) and teachers. Students work in teams of four to six, guided by a teacher from their school as their
  advisor, and have access to an online stock market simulator." — Basic format.
- **R-W3** · [MAIN] Important Dates · number · "September 28 Competition begins; first day of trading" … "October 9
  Deliverable: Official team roster" … "October 23 Deliverable: Trading Notes Analysis" … "November 6 Deliverable:
  Investment Policy Statement (IPS)" … "December 4 Deliverable: Final report and school documentation" … "TBD
  Semifinalists (top 50 teams) announced" … "TBD Virtual Semifinals" … "April 29 & 30 Learning Day & Global Finale" —
  Same dates as SMApply. Semifinal dates are TBD (to be decided).
- **R-W4** · [MAIN] About · definition · "Each year, teams are introduced to a new case study featuring a Wharton School
  alum. While the client is real, the financial scenario is developed specifically for the competition." — The
  scenario is invented. Do not treat Laura's real-life plans or finances as case facts.
- **R-W5** · [MAIN] About · requirement · "Using the client’s background, financial goals, and their own research,
  teams develop a long-term investment strategy designed to help the client achieve their objectives." — Background,
  goals, and outside research are all expected.
- **R-W6** · [MAIN] About · definition · "Teams also use the Wharton Investment Simulator (WInS) to implement their
  investment strategy by building and managing a portfolio using virtual cash to buy and sell approved securities." —
  WInS = implementation.
- **R-W7** · [MAIN] About · evaluation · "Unlike other investment competitions, success is not determined by portfolio
  performance. Teams are evaluated on the quality of their investment strategy, how well it aligns with their client’s
  objectives, the strength of their research and analysis, and their ability to clearly communicate and defend their
  recommendations." — Four judging themes. "Defend" points to the semifinal Q&A.
- **R-W8** · [MAIN] About · evaluation · "Following the submission of final reports, a panel of judges selects 50
  semifinalist teams. Those teams are invited to present their investment strategies during the virtual Semifinals.
  The top 10 teams advance to the Global Finale" — Top 50 are chosen after 4 Dec. Top 10 go to the finale.
- **R-W9** · [MAIN] · framing · "Academic Director: Professor Michael Roberts" (a finance professor; his research
  listed there includes "the effect of interest rates on bank lending") — Context on who designs the competition. The
  page does not say he judges.
- **R-W10** · [MAIN] counters · number · "* 2025-2026 Participation Completion Numbers": Teams 2,339; Countries 79;
  Students 12,145; Advisors 1,625 — Read from the `data-counter-value` attributes in the HTML, because the page's
  display shows "0" until JavaScript runs. Last year about 2,300 teams completed.

### Rules & Roles [RULES]
- **R-W11** · [RULES] Student Eligibility · requirement · "Each team must designate one student team leader who is at
  least 16 years old at the start of the Competition. No exceptions will be granted." — Team leader must be 16 or
  older.
- **R-W12** · [RULES] Student Eligibility · requirement · "Teams must be composed of current students from the same
  high school." — Same school.
- **R-W13** · [RULES] Teams · requirement · "Each team must consist of four to six students, including the student
  team leader, throughout the Competition." — 4 to 6 members at all times.
- **R-W14** · [RULES] Teams · definition · "Each team will share one WInS account." — One shared account.
- **R-W15** · [RULES] Teams · requirement · "All team members are responsible for: Developing and implementing the
  team’s investment strategy; conducting research and analysis; collaborating with teammates and placing trades
  through the team’s shared WInS account; and remaining actively engaged throughout the Competition and meeting all
  deadlines." — Students own the strategy and the trades.
- **R-W16** · [RULES] Teams · prohibition · "Teams may not contact the Competition client. Teams that violate this rule
  will be disqualified." — Never contact Laura.
- **R-W17** · [RULES] Teams · prohibition · "After the official team roster is submitted, teams may not add members."
  … "Teams that fall below four members or exceed six members at any time during the Competition will be
  disqualified." — Roster lock; size rule.
- **R-W18** · [RULES] Advisors · requirement · "Each team must have one Advisor, who must be a teacher or educator at
  the high school attended by the team members." — Advisor must be from the school.
- **R-W19** · [RULES] Advisors · prohibition · "The Advisor’s role is to provide guidance, encouragement, and
  educational support throughout the Competition. Advisors may not make decisions on behalf of students or actively
  participate in team activities, trading decisions, or strategy development." — Directly contradicts the case's
  fictional portfolio manager (R-C3; R-AN4).
- **R-W20** · [RULES] Advisors · definition · "Monitoring team engagement and portfolio activity." / "Serving as a
  sounding board without completing work on behalf of students." — What advisors do.
- **R-W21** · [RULES] Advisors · prohibition/permission · "Teams may seek guidance from a parent, industry
  professional, or other adult serving as a secondary advisor, provided the team also has a primary teacher Advisor.
  However, the use of paid advisors, education consultants, or other agents is prohibited. Similarly, no participant
  or team may enroll in any non-Wharton extracurricular course (online or in person) that claims to teach the
  Investment Competition." — Unpaid secondary advisors are allowed. Paid help and outside "competition courses" are
  not.
- **R-W22** · [RULES] Deliverables & Requirements · definition · "Trading Notes Analysis: Document your team’s
  decision-making process." / "Investment Policy Statement (IPS): Define your client’s investment objectives, risk
  tolerance, and overall investment strategy." / "Comprehensive Final Report: Present and justify your team’s
  investment strategy, portfolio recommendations, and analysis." — The IPS description names "risk tolerance".
- **R-W23** · [RULES] Trading Requirements · requirement · "Teams must meet the required trading activity and
  portfolio management guidelines throughout the competition." — The public pages give no minimum amount of trading
  (R-AN36; X-18).
- **R-W24** · [RULES] Semifinals & Global Finale · evaluation · "The top 50 teams will be selected as semifinalists
  based on the strength of their Investment Policy Statement (IPS) and Final Reports." — Trading Notes are not named
  (X-8).
- **R-W25** · [RULES] Semifinals · requirement · "Semifinalists must also submit documentation on official school
  letterhead confirming that: The team has permission to participate in the Competition. All students and the advisor
  are affiliated with the school." — Letterhead confirmation.
- **R-W26** · [RULES] Use of Generative AI · permission/prohibition · "Teams may use generative AI tools (such as
  ChatGPT) for brainstorming and idea generation." … "AI-generated work may not be submitted as your own." … "Any
  AI-generated material included in your report must be properly cited, just like any other reference source." —
  Brainstorming with AI is allowed. AI text may not be submitted as the team's own, and any AI use must be cited.
- **R-W27** · [RULES] AI Policy · prohibition · "Beware that use may also stifle your own independent thinking and
  creativity. You may not submit any work generated by an AI program as your own." — Restated.
- **R-W28** · [RULES] Ethics · prohibition · "We trust that you will not lie about your investment decisions and
  outcomes, fabricate analyses, invent teamwork and experiential stories, compensate advisors, education consultants,
  or other agents, enroll in non-Wharton extracurricular courses that claim to “teach” the competition, or plagiarize
  existing strategies." — The reflections and the Articulation section must be true.
- **R-W29** · [RULES] Ethics · requirement · "All teams should review the CFA Institute’s Asset Manager Code and
  operate by these standards. We expect you to read these rules and apply them to all you do on behalf of your
  potential client throughout the competition." — Names a professional ethics code. "Potential client" again.
- **R-W30** · [RULES] Code of Conduct · requirement · "Each team is required to properly cite any sources used and
  acknowledge ownership of all images and other media that it submits as part of a deliverable or a presentation that
  it (or a team member) does not own or did not solely develop." — A general citation duty (X-9).
- **R-W31** · [RULES] Code of Conduct · permission · "each team (and/or the students on such team) retains ownership
  of their own work." — Teams own their work.
- **R-W32** · [RULES] Recording Policy · prohibition · "Video recording, audio recording, photography, screenshots, or
  posting presentations or participants online during the Semifinals or Global Finale is strictly prohibited." —
  Applies at the semifinals and finale.
- **R-W33** · [RULES] Prizes & Recognition · number · "All students on teams that submit the required competition
  deliverables and meet the minimum competition requirements will receive a Digital Credential (participation badge)
  in February 2027." — The credential needs the "minimum competition requirements", which are not defined publicly.
- **R-W34** · [RULES] Participation & Travel · definition · "The Semifinals will be conducted virtually." / finalists
  "may participate either in person or virtually" — Format.

### FAQ [FAQ]
- **R-W35** · [FAQ] Basics · number · "Registered teams will be able to practice on the Wharton Investment Simulator
  (WInS) from September 15 – 25, 2026 (4:00 p.m. ET). All practice portfolios will be removed at that time." —
  Practice period is over.
- **R-W36** · [FAQ] Basics · number · "The competition will officially begin on September 28, 2026 and end on December
  4, 2026." — 28 Sep to 4 Dec.
- **R-W37** · [FAQ] Eligibility · framing · "so they can achieve our ultimate goal with this game, which is learning
  the nuances of investing." — Learning is the stated goal. "Game".
- **R-W38** · [FAQ] Team size · requirement · "All team members must play a contributing role." — Everyone contributes.
- **R-W39** · [FAQ] Time · number · "The competition is 10 weeks in length" — Week 1 starts 28 Sep. Week 6 ends
  6 Nov, Week 7 starts 9 Nov and Week 10 ends 4 Dec. This matches R-T12 and R-C93 (DERIVED).
- **R-W40** · [FAQ] Judging · evaluation · "No. Teams will not receive individual feedback." — No feedback.
- **R-W41** · [FAQ] Judging · evaluation · "We are looking for teams that score exceptionally well on all five
  components of the criteria, and that embrace all aspects of the competition with passion and creativity, which is
  then reflected in various ways in their final reports." — All five criteria matter. The Final Report is the showcase.
- **R-W42** · [FAQ] Judging · evaluation · "your team’s standings on WInS have little to do with the final outcome.
  Winners are selected on the strength and articulation of their overall investment strategies and competition
  experiences, not on the percentage growth of their portfolios" — Returns do not decide the winner.
- **R-W43** · [FAQ] Judging · evaluation · "There is no single winning investment strategy. Strong teams understand the
  client, work effectively together, conduct thoughtful research and analysis, and develop a clear and creative
  strategy designed around the client’s goals. Their investment decisions reflect that strategy, and their
  deliverables connect into a cohesive, well-supported submission. Just as importantly, successful teams communicate
  their reasoning, assumptions, tradeoffs, and competition experience clearly and authentically." — Wharton's own
  description of a winning team. "Tradeoffs" and "authentically" are named.
- **R-W44** · [FAQ] Semifinals · requirement · "Your team will be expected to create and deliver a short presentation
  (via video conference for the Semifinals and live or via video conference for the Global Finale) about your team’s
  strategy, analysis and experience over the past 10 weeks to a live panel of judges. All team members must
  participate." — Every member presents.

### Register page [REG]
- **R-W45** · [REG] · definition · "Accounts are created per team, not per student. Each team shares one Wharton
  Investment Simulator (WInS) account." — Consistent with R-W14.

### AI policy page [AI]
- **R-W46** · [AI] Investment Competition › AI Policy · requirement · "If you use AI to assist you in any way during the
  competition, how you use it must be recorded in your Works Cited pages." — Any AI use must be recorded in a Works
  Cited list. This is stricter than the Rules page version. It implies the Final Report has a Works Cited section.
- **R-W47** · [AI] · requirement · "All material referenced or generated by AI should be cited like any other reference
  material (with due consideration for the quality of the reference, which may be poor)." — Cite AI, and treat it as a
  weak source.
- **R-W48** · [AI] Investment Competition › Ethics · prohibition · "…enroll in non-Wharton extracurricular courses that
  claim to “teach” the competition, pass AI generated writing or work off as your own, or plagiarize existing
  strategies." — This version of the Ethics text adds the AI clause, which the Rules page version lacks.
- **R-W49** · [AI] Statement of AI Use · requirement · "When students express themselves in the Wharton Global Youth
  Program, they must use their voice and words." / "AI-generated work should be cited like any other reference
  material, including how and where students used AI-generated information." — Students write in their own words.
- **R-W50** · [AI] Pre-baccalaureate section · prohibition (scope: the pre-bacc program) · "Don’t use AI for personal
  reflection or opinion-based tasks." — Written for another program. Still a strong signal for the Trading Notes
  reflections and the Articulation criterion (INTERPRETATION).
- **R-W51** · [AI] Checklist Questions · requirement · "Did I come to my current conclusion before or after using
  generative AI tools?" / "Did I double check the numbers and information are most up-to-date?" — A self-check list.

### 2025-26 season news and archive [NEWS], [ARCH]
- **R-W52** · [ARCH] · framing · Clients 2021-22 to 2025-26: "Nichole Jordan, WG’08"; "Peter Wang Hjemdahl, W’19";
  "Hilary Ash, W’13"; "Ladi Ayoola, WG’22"; "Connor Barwin, WG’23" — Laura (a 2018 Wharton graduate per the case, so "W’18"
  in this notation, DERIVED) is the next alum client. The archive does not list her yet.
- **R-W97** · [NEWS] · number · "the competition welcomed more than 6,300 registered teams from around the world, an
  increase of 1,300+ from the previous year." — 2025-26 registered teams.
- **R-W98** · [NEWS] · number · "students were crafting compelling investment strategies and building investment
  portfolios with $500,000 in virtual cash, up from $100,000." — Last year's WInS cash was $500,000. This year's is
  $300,000 (R-W56).
- **R-W99** · [NEWS] · number · "On December 12, some 2,300 teams from 79 countries submitted final reports, an
  increase of nearly 30% over last year’s competition." — The real field is teams that finish: about 2,300.

### SMApply public resource pages
- **R-W53** · [S-HOME] · word-choice · "An investment in knowledge pays the best interest." — Unattributed tagline on
  the portal.
- **R-W54** · [S-CLIENT] · definition · "Get to the know the client. The Client Case Study is the starting point for the
  competition." / "It introduces the client, her background, financial circumstances, and long-term goals. Teams
  should use this information to understand who they are investing for and to develop a thoughtful investment
  strategy tailored to her needs. The case study provides the foundation for the team’s portfolio decisions,
  Investment Policy Statement, Trading Notes Analysis, and Final Report." — Includes the typo "to the know". The case is
  the foundation of all deliverables.
- **R-W55** · [S-CLIENT] · prohibition · "IMPORTANT: Teams are not permitted to contact Laura Gao." — Restated for this
  client by name.
- **R-W56** · [S-TRADE] Account and Trading Period · number · "Your team will begin the official trading period with
  $300,000 in virtual cash." — **Starting cash is $300,000.**
- **R-W57** · [S-TRADE] · definition · "Each team shares one WInS account. All team members will use the same username
  and password." — Shared login.
- **R-W58** · [S-TRADE] · number · "Official trading begins on September 28, 2026, and ends on November 6, 2026. When
  trading ends, your portfolio will be frozen, and your team may no longer trade or change its holdings." — Trading
  window and freeze.
- **R-W59** · [S-TRADE] Important · definition · "The $300,000 is your team’s WInS simulator balance. The additional
  $150,000 contribution described in the Client Case Study will not be added to WInS." — WInS never receives the
  $150,000.
- **R-W60** · [S-TRADE] Important · prohibition · "WInS gains and losses should not be added to or subtracted from the
  client’s long-term portfolio projections. Those projections should use the cash flows provided in the Client Case
  Study and reasonable return assumptions consistent with your strategy." — Consistent with R-C77/R-C78.
- **R-W61** · [S-TRADE] How Trades Are Executed · permission · "You may enter buy and sell orders at any time during
  the official trading period. The timing of execution depends on the security, its market, and whether that market is
  open." — Orders are accepted at any hour.
- **R-W62** · [S-TRADE] U.S. Securities · definition · "Orders placed while the market is open are executed using
  real-time prices." / "Orders placed while the market is closed are filled at the security’s opening price when the
  market reopens." / "Prices displayed for open positions may be delayed by 10 to 15 minutes." — How fills work.
  Relevant for a team in Australia trading overnight.
- **R-W63** · [S-TRADE] International Securities · definition · "International equity orders may experience a longer
  delay and are processed at the end of the applicable trading day." — Non-U.S. orders fill at the end of the day.
- **R-W64** · [S-TRADE] · definition · "WInS automatically completes foreign-currency conversions. You do not need to
  exchange currency yourself, but exchange-rate movements may affect the value of your holdings." — Currency
  (foreign-exchange, FX) risk exists in WInS.
- **R-W65** · [S-TRADE] Trading Limits · number · "Your team may make up to 200 trades during the competition." —
  **200-trade cap confirmed.**
- **R-W66** · [S-TRADE] Trading Limits · number · "Your team may trade an amount equal to no more than twice a
  security’s current daily trading volume." — Size cap per trade, tied to trading volume.
- **R-W67** · [S-TRADE] Approved Securities · permission · "Stocks: Any stock available on WInS priced at $5 or more,
  or the equivalent of $5 in its local currency." — Stocks priced at $5 or more.
- **R-W68** · [S-TRADE] Approved Securities · permission · "Exchange-Traded Funds: Any ETF available on WInS." — **Any
  ETF available on WInS.** There is no separate list.
- **R-W69** · [S-TRADE] Approved Securities · permission · "Treasury Bonds: Bonds available on WInS. The list includes
  Treasury bonds from the United States, United Kingdom, Germany, France, Italy, and the Netherlands." — **Individual
  government bonds can be bought.**
- **R-W70** · [S-TRADE] Diversification · permission · "There is no required sector allocation or minimum number of
  sectors. However, diversification remains an important investment principle." — **No sector minimum.** This
  replaces the unverified "sector minimum = team size" claim.
- **R-W71** · [S-TRADE] Diversification · framing · "Your team may consider diversification across asset classes,
  sectors, industries, market capitalizations, geographic regions, risk characteristics, and funding purposes. The
  goal is to build an intentional mix of investments appropriate for your strategy, not simply to own a large number of
  securities." — "Funding purposes" counts as a kind of diversification (R-AN45).
- **R-W72** · [S-TRADE] Trading Outside the U.S. · permission · "You are not expected to stay awake during the night to
  trade. Orders may be entered while the U.S. market is closed and will be filled when the market reopens." — Written
  with non-U.S. teams in mind.
- **R-W73** · [S-TRADE] · evaluation · "The competition does not require frequent or same-day trading. Make thoughtful,
  well-researched decisions and record the reasoning behind them in your Trading Notes." — Fewer, better trades.
- **R-W74** · [S-WINS] · definition · "WInS is a tool for implementing your investment strategy." — WInS = a tool.
- **R-W75** · [S-WINS] · evaluation · "You are not being evaluated based on: Your portfolio ranking / How many trades
  you make / Whether you outperform other teams / Whether your portfolio makes money during the competition" — Four
  things that are not judged.
- **R-W76** · [S-WINS] · evaluation · "A long-term investment strategy cannot be judged solely by what happens in the
  market over a few weeks. Instead, your portfolio provides evidence of the decisions your team made and how you put
  your strategy into practice." — The portfolio is evidence.
- **R-W77** · [S-WINS] · definition · "All account activity will be cleared after the practice session. Practice
  trades, portfolio activity, gains and losses, and account balances will be reset before official trading begins on
  September 28." — Practice trades cannot be used as notes.
- **R-W78** · [S-WINS] · number · "Official trading will end on November 6, when your Investment Policy Statement is
  due. At that time, your WInS portfolio will be frozen" — Freeze date.
- **R-W79** · [S-WINS] · framing · "Test ideas and evaluate how different investments may contribute to growth,
  liquidity, funding reliability, financial flexibility, or risk management." — The same vocabulary again (X-16).
- **R-W80** · [S-WINS] · requirement · "Your portfolio should reflect a cohesive strategy designed around the client’s
  goals. Each investment decision should have a clear purpose within that strategy." — Every holding needs a purpose.
- **R-W81** · [S-WINS] · evaluation · "Gains and losses generated in WInS do not determine how your team is evaluated."
  — Restated.
- **R-W82** · [S-WINS] Remember Your Trading Notes · requirement · "Complete a Trading Note when your team makes an
  investment decision. Your Trading Notes should record the reasoning, research, and intended strategic role of each
  decision at the time it is made." — Write every note at the time of the trade.
- **R-W83** · [S-WINS] · evaluation · "The goal is not simply to achieve the highest return, but to demonstrate what
  your team has learned and how effectively you applied that learning throughout the competition." — Learning is
  judged.
- **R-W84** · [S-WINS] · definition · "Access WInS: https://edu.stocktrak.com/wharton/" — The platform is run by
  Stock-Trak (R-W85).
- **R-W85** · [S-FAQ] · number · "Your team will be responsible for managing a portfolio of $300,000 in virtual cash." /
  "Wharton Global Youth Program has contracted with Stock-Trak®" — $300,000 confirmed a second time.
- **R-W86** · [S-FAQ] · definition · "Your team username is NOT the same as your team name." — The title page needs
  both (R-I41, R-I44).
- **R-W87** · [S-FAQ] Who can place trades · prohibition · "Students should place trades on WInS, NOT the advisor. A
  key component of the Investment Competition is teamwork and communication. It should be a team decision. We strongly
  encourage teams to identify different roles for each team member." — Advisor does not trade. Assigning roles is
  encouraged.
- **R-W88** · [S-FAQ] Placing trades · framing · "you should not be doing a lot of buying and selling of the stocks
  designated for the long-term portion of your portfolio … you are not trying to prove the worthiness of your long-term
  strategy through how your portfolio performs over 10 weeks of trading." — Low turnover. "Long-term portion" implies
  other portions exist.
- **R-W89** · [S-FAQ] · permission · "DOES THE COMPETITION ALLOW ALL SECURITIES? No." / "Investments permitted (for
  BOTH contributions): Cash / Any stock from any exchange available on WInS priced at $5 (or the equivalent of $5 in the
  local currency) or higher. / Any Exchange-Traded Funds (ETFs) available on WInS. / Any Government/Treasury Bonds from
  any exchange available on WInS." — The permitted list, with the phrase "for BOTH contributions" (R-AN15).
- **R-W90** · [S-FAQ] · prohibition · "The following are NOT permitted: Margin trading / Short selling / Stock-secured
  debt / Crypto / Derivatives (options, futures, swaps, etc.) / Anything other than the approved investments listed
  above." — **Prohibited list.**
- **R-W91** · [S-FAQ] · definition · "The bond prices are updated once daily at U.S. market open, and pay out every six
  months." … "When the competition ends, any bonds held will have their value factored into the teams final portfolio
  value." — Bond prices are stale within the day. Coupons are paid twice a year.
- **R-W92** · [S-FAQ] · number · "Each stock transaction is charged a flat $25 commission and treasury bonds are charged
  $10. Commission is charged only on a trade that clears." — Trading costs.
- **R-W93** · [S-FAQ] · definition · "WInS provides real-world corporate actions such as dividends, stock splits, bond
  coupons, and so on." — Income is credited.
- **R-W94** · [S-FAQ] · framing · "You can only cancel open orders." … "If you make an error, we encourage you to run
  with it and not scramble to “fix” it. Trading errors are part of the learning process." — Errors are learning
  material (and a possible Articulation story, if true).
- **R-W95** · [S-FAQ] Judging · evaluation · "Gains and losses generated in WInS are not used to select winning teams
  and are not applied to the client’s long-term portfolio projections. … Teams are evaluated on how thoughtfully they
  develop, implement, evaluate, and communicate a cohesive investment strategy designed around the client’s goals." —
  Four verbs: develop, implement, evaluate, communicate. These match the three deliverables.
- **R-W96** · [S-DELIV] · framing · The public page text is identical to the repo transcription (section 1.1). The Box
  downloads' SHA-256 values match the repo PDFs. — The repo copy is current as of 2026-09-27.
- **R-W100** · [S-FAQ] typo · word-choice · "DOES THE COMPETITION ALLOW MARGING TRADING OR SHORT SELLING? No." / "We
  will not provide your with information" — Editing slips on the FAQ (see R-AN47).

---

## 7. Notable word choices and anomalies (R-AN)

Every "possible purpose" below is INTERPRETATION: a neutral guess at why the designers wrote it this way. None is a
fact. Quotes are VERIFIED-REPO-FILE or VERIFIED-PRIMARY as referenced.

- **R-AN1 "High degree of certainty" is never defined.**
  - Case p.3 L91: "All ten payments must be funded by the investment portfolio with a high degree of certainty."
    L97-98: "define what they consider a high degree of funding certainty".
  - Two wordings are used ("certainty" and "funding certainty"). No percentage or method is given.
  - Possible purpose: tests whether teams can turn a client's plain-language wish into a definition that can be
    tested, and explain how they checked it. This fits a client with a statistics degree (R-C12).
- **R-AN2 The reserve comes before everything, on the same day as the first payment.**
  - Case p.3 L94-95: "At the beginning of 2033, before making the first operating payment or contributing to the
    facility, Laura will set aside a portion of the portfolio to fund the ten payments."
  - DERIVED: the first payment is also due "at the beginning of 2033" (L88-89). The set-aside must therefore cover
    ten payments, one of them paid immediately.
  - Possible purpose: sets a priority order (the promise first, the facility second) and checks whether teams notice
    that the first payment is due at once.
- **R-AN3 "Not adjusted for inflation" is stated outright.**
  - Case p.3 L90: "each payment is a fixed $50,000 and is not adjusted for inflation."
  - Possible purpose: removes a common source of confusion and makes the commitment a fixed-dollar liability that
    bonds can match. The loss of real value (what $50,000 can buy) is shifted elsewhere: "any operating support beyond
    Laura’s commitment, may come from co-sponsors…" (L85-86). Inflation still enters through the facility (R-AN8).
- **R-AN4 The fiction says the advisor decides; the rules say the opposite.**
  - Case p.1 L4: "your team’s teacher/advisor who makes the final investment decisions for your firm’s portfolio".
  - [RULES]: "Advisors may not make decisions on behalf of students or actively participate in team activities,
    trading decisions, or strategy development."
  - [S-FAQ]: "Students should place trades on WInS, NOT the advisor."
  - Possible purpose: role-play of a firm's hierarchy (analysts recommend; a portfolio manager signs off), without
    changing who does the work.
  - Consequence (INTERPRETATION): the IPS "decision-making framework" (R-C89) must be the students' own. Any mention
    of the advisor must match the real rules.
- **R-AN5 A competitive pitch to a client who has not yet committed.**
  - Case p.1 L9-10: "the investment strategy that Laura ultimately chooses". L5: "a potential client". p.2 L43: "with
    an asset management firm". [RULES] Ethics: "your potential client".
  - Possible purpose: the task is persuasion as well as analysis. The judge acts as the client choosing among firms.
    The criterion "recommendations that can earn her confidence" (R-S25) points the same way.
- **R-AN6 Outside money may fund the facility but not her commitment.**
  - Case p.3 L85-86: "Any remaining facility cost, and any operating support beyond Laura’s commitment, may come from
    co-sponsors…". L91-92: "Teams may not rely on co-sponsors, grants, program fees, or other outside funding to meet
    this requirement."
  - Possible purpose: makes the facility the flexible amount and the payments the fixed one. Her personal promise has
    to rest on her own money, while shared costs can be shared.
- **R-AN7 2031 is exactly two years before 2033 and gets its own timeline line.**
  - Case p.2 L55: "2031 is Year 5." p.3 L109: "in 2031, two years before the residency is established."
  - Possible purpose: creates a forecasting problem with a fixed, short horizon. A two-year gap is short enough for
    part of the promise to be secured with a matching two-year instrument. Two-year U.S. Treasury notes are a standard
    maturity; that is general market knowledge, not something the case states.
- **R-AN8 Inflation's effect on facility costs must be explained, but the facility cost need not be estimated.**
  - Case p.4 L146-147: "the effect of inflation on portfolio projections and facility costs". L164-165: "The total
    cost of the facility has not been determined. Teams are not expected to estimate that cost".
  - Possible purpose: asks for an assumption about how rising prices shrink what a fixed-dollar contribution buys (and
    the real value of projections), without a construction budget. Relevant to how the 2031 range is explained to
    co-sponsors.
- **R-AN9 The confidence statement is two-sided.**
  - Case p.3 L117-118: "state how confident they are that her 2033 contribution will fall within that range."
  - A contribution above the top of the range is literally "outside" it.
  - Possible purpose: a range that is wide enough to be safe becomes useless to co-sponsors, and one narrow enough to
    be useful becomes risky. The wording forces the team to size both ends. The credibility sentence (L114) shows the
    low end matters most.
- **R-AN10 The case never names a currency.**
  - "$300,000", "$150,000", "$50,000", "dollar range" (L117). No "U.S. dollar" or "USD"; no mention of the New Taiwan
    dollar or exchange rates. Yet the residency is "in Taiwan" (L76).
  - [S-TRADE]: "WInS automatically completes foreign-currency conversions … exchange-rate movements may affect the
    value of your holdings."
  - Possible purpose: a simplification (the U.S. dollar is implied for a U.S. competition) that leaves room for teams
    to notice currency risk in a Taiwan project. Whether to raise it is a team judgement. Taxes and Taiwan law are
    explicitly excluded, but currency is not mentioned at all.
- **R-AN11 The timeline lists only the event years.**
  - Case p.2 L49-57: 2026, 2027, 2028, 2031, 2033. 2029, 2030 and 2032 are missing, and so is 2042 (Year 16, the last
    payment).
  - Possible purpose: draws attention to the decision dates. The pattern rule (L58) covers the rest.
- **R-AN12 The payments are mentioned before they are introduced.**
  - Case p.2 L59-60: "The ten operating payments are therefore spaced exactly one year apart." This appears a page
    before "Operating Commitment" (p.3 L87).
  - Possible purpose: the timing convention exists to make the maths exact: yearly discounting, with no mid-year
    question.
- **R-AN13 The money put in is less than the money promised.**
  - DERIVED: $300,000 + $150,000 = $450,000, while 10 × $50,000 = $500,000 in nominal payments.
  - The portfolio must grow before any facility money exists. At the 2026-09-25 Treasury curve, the payments' value on
    1 Jan 2027 is $292,264 (VERIFIED-REPO-FILE: `research/verified_2026-09-27/official_curve_pv.py`, per the brief),
    so the present-day cost is below $300,000 even though the nominal total is above $450,000.
  - Possible purpose: makes time and interest rates central, and asks whether the promise can be secured early.
- **R-AN14 WInS starting cash equals Laura's first deposit exactly.**
  - [S-TRADE]: "$300,000 in virtual cash" and "The additional $150,000 contribution … will not be added to WInS."
  - [NEWS]: last year "$500,000 in virtual cash, up from $100,000."
  - Possible purpose: this year's simulator is sized to be Laura's Year-1 portfolio. That bears on the open question in
    the brief of whether WInS should mirror the 2027 book or the post-2028 target. Neither document settles it.
    (Seed question 3's "$500k = WInS cash" link does not hold this season.)
- **R-AN15 "Investments permitted (for BOTH contributions)".**
  - [S-FAQ]. Possible purpose, reading 1: the permitted-investment list also limits the long-term strategy for both
    Laura's $300,000 and her $150,000. Instruments outside it, such as derivatives, would then be off-limits even in
    the plan.
  - Reading 2: the wording is left over from an earlier year's case that had two contributions.
  - Treat reading 1 as the safe assumption. Confirm with Wharton via the Contact Us form if the plan relies on
    anything not on the list.
- **R-AN16 "Although … thoughtful risks" and "the capital required for her goals".**
  - Case p.2 L69-74.
  - Possible purpose: signals that her career risk-taking does not simply carry over to the portfolio. What must be
    protected is the capital her goals require, not every dollar. "Thoughtful" appears three times in the case (L7,
    L38, L70). The risk wording is qualitative on purpose.
- **R-AN17 The case never states a risk tolerance, return target, benchmark or asset mix.**
  - Absent from the case: "risk tolerance", "benchmark", "rebalanc(e)", "return target". Word check, VERIFIED-REPO-FILE.
  - Yet the IPS definition includes "risk tolerance" (R-I2), and so does the Rules page IPS description (R-W22).
  - Possible purpose: teams must infer and justify her risk tolerance from the case, including the difference between
    how much risk she is willing to take and how much she can afford to take.
- **R-AN18 "Responsibly" and "responsible" are key words that are never defined.**
  - Case: "responsibly contribute" (L102, L105), "responsibly provide" (L167), "a responsible facility contribution"
    (L138). IPS guide: "responsible facility contribution" (3 times).
  - Possible purpose: the team must say what makes a contribution responsible: it protects the reserve and preserves
    flexibility (R-C84).
- **R-AN19 Flexibility "as the project develops", yet no contingency fund is required.**
  - Case p.3 L102-103 and L106-107.
  - Possible purpose: flexibility belongs to the residency project, not to her personal spending (living costs are
    outside the portfolio, L61-63). Teams must express it without sizing a separate fund, for example as a rule or a
    share (INTERPRETATION).
- **R-AN20 "The extent to which" and "no predetermined facility contribution".**
  - Case p.3 L104-105.
  - Possible purpose: permits a rule-based answer (a share of the surplus, a floor plus a share) and even a small
    amount. The dollar requirement applies to the 2031 range (L117), not to the 2033 contribution itself.
- **R-AN21 "Draft part of Laura’s fundraising materials".**
  - Case p.4 L123. Only "part"; the audience is prospective co-sponsors. The IPS guide (R-I31) and the Trading Notes
    guide (R-T14) both exclude it, so it belongs in the Final Report. Criterion 5 scores it (R-S28).
  - Possible purpose: tests whether teams can explain uncertainty to people who are not investors. Under the AI policy
    it must be the students' own writing (R-W26, R-W49).
- **R-AN22 Year 0 is "before any money has been invested", yet WInS trading happens in Year 0.**
  - Case p.2 L47. p.4 L130: "It does not determine Laura’s actual portfolio value at the beginning of 2027."
  - Possible purpose: separates the practice run (WInS, in 2026) from the plan (money from 2027).
- **R-AN23 The portfolio "may also cover part of the facility’s cost".**
  - Case p.3 L84-85. "Part" signals no expectation that her portfolio pays for the whole facility.
  - Possible purpose: sets the expectation of a partial, credible contribution.
- **R-AN24 "Continued business income" is listed as a possible outside source.**
  - Case p.3 L86 lists it among sources for the facility and extra support. For the commitment, teams "may not rely on
    … other outside funding" (L91-92).
  - Possible purpose: her future earnings may help the project but cannot back the promise. Whether it counts as
    "outside funding" is the team's reading; the stricter reading is safer.
- **R-AN25 The ten years are called "early operations".**
  - Case p.3 L83: "reliable support for its early operations". L92-93: after 2042 is out of scope.
  - Possible purpose: frames the commitment as start-up support. It explains why there is no need to fund the
    residency forever.
- **R-AN26 "A portion of the portfolio" and "the remaining portfolio".**
  - Case p.3 L95, L101.
  - Possible purpose: the reserve is one part of the portfolio. The remainder is for the facility and flexibility,
    which is the two-part structure the case expects.
- **R-AN27 "If at all": a reserve that never changes is allowed.**
  - Case p.3 L96. Contrast IPS p.1 L22: "How will the portfolio’s asset allocation and composition change as future
    funding needs approach and payments are made?"
  - Possible purpose: the case allows a reserve that pays itself out as bonds mature, with no trading. The IPS prompt
    still expects the portfolio as a whole to change over time (X-2).
- **R-AN28 "Laura will set aside" in 2033, but nothing forbids earlier funding.**
  - Case p.3 L94-95 defines the reserve at 2033. It does not say how the money is invested before then.
  - Possible purpose: tests whether teams see that the set-aside is a label at a date, while the investing decision
    starts in 2027. The team must decide how to describe this reading; the case gives no ruling (open item in the
    brief).
- **R-AN29 The case's "must" versus "should" pattern.**
  - "Must" appears 9 times in the case. It covers:
    - the portfolio funding the commitment;
    - the size and composition of the reserve;
    - the facility recommendation;
    - the range and the confidence statement;
    - the range protecting the payments;
    - the fundraising draft;
    - the strategy tests.
  - "Should" covers the certainty definition (L97 "They should also define"), the assumptions and the scenarios.
  - Possible purpose: signals what is a hard requirement. In practice every "should" item is also scored under
    Portfolio Analysis.
- **R-AN30 The pull quote versus the co-sponsor task.**
  - Case p.1 L31-33: "The only person who needs to believe in something is yourself." Versus p.3 L114-115: overpromising
    could "damage her credibility and lose the confidence or participation of co-sponsors."
  - Possible purpose: her self-belief meets a 2031 task where others must believe her. The case may be testing whether
    teams can turn conviction into evidence. INTERPRETATION only. The quote has no attribution line in the text layer;
    B8/D13 should check it against a primary source before anyone presents it as her words.
- **R-AN31 Her roles are listed differently in each place, and all her income sources come from her own work.**
  - "bestselling author, illustrator, entrepreneur, and educator" (L5-6); "bestselling graphic novelist…" (L13);
    "author, illustrator, educator, and public speaker" (L25); "Storyteller, Entrepreneur, and Creative Visionary"
    (L29-30). The 2028 sources: "publishing advances, speaking engagements, licensing, and other entrepreneurial
    ventures" (L44-45).
  - Possible purpose: shows a varied creative career whose income depends on her personal brand. The case states the
    $150,000 as certain ("will"). Stress-testing it is a team choice, which the Portfolio Analysis criterion allows
    ("varying market outcomes").
- **R-AN32 A statistics degree.**
  - Case p.1 L16: "Statistics & Information Decisions Management".
  - Possible purpose: a client who can judge a probability statement. Loose phrases such as "95% safe" with no stated
    method would be exposed (INTERPRETATION).
- **R-AN33 Her first named work answered misinformation.**
  - Case p.1 L19-20: "Originally intended as a response to misinformation".
  - Possible purpose: fits a case whose central communication task is credibility and not overpromising. Use only as a
    link to her stated public work, never as decoration (INTERPRETATION).
- **R-AN34 What is conspicuously NOT asked or stated** (VERIFIED-REPO-FILE word checks across the four official
  documents unless noted):
  - No values-based or impact preference: 0 hits each for "ESG", "values", "impact", "sustainab" (compare last season's
    impact-led case, per the brief).
  - No benchmark, rebalancing rule, fee rule, return target, risk-tolerance number or confidence level (for example
    95%).
  - No currency and no exchange-rate mention (R-AN10). No estate or legacy. No retirement.
  - No cash needs before 2033.
  - No instruction for what happens if the residency cannot open or moves.
  - No requirement to use WInS holdings in projections; this is forbidden, in fact (R-C78).
  - No facility cost and no contingency fund (both explicitly not expected).
  - No word on what happens to leftover money after 2042.
  - The case does not mention technology or AI risk to her income.
  - The case does not say whether the $150,000 could be smaller.
  - The public web pages give no minimum trading activity.

  Possible purpose: keeps the case focused on one liability, one uncertain surplus and one communication problem.
  Anything a team adds from this list must earn its place (brief design principle).
- **R-AN35 "She will contribute an additional $150,000".**
  - Case p.2 L43-45. The case uses "will", not "expects to".
  - Possible purpose: removes deposit risk from the base case. Teams who stress-test it go beyond the case and must
    label that as their own scenario.
- **R-AN36 Trading freezes in Week 6, but the competition runs 10 weeks.**
  - [S-TRADE]/[S-WINS]: trading ends 6 Nov. [FAQ]: the competition ends 4 Dec, "10 weeks".
  - Possible purpose: the Final Report is written about a frozen portfolio and must judge its implementation
    ("evaluates how that strategy was implemented", R-C90). The Rules page's "required trading activity" (R-W23) is not
    quantified anywhere public.
- **R-AN37 Scope of "Formatting choices not specified below".**
  - IPS p.3 L101: the sentence sits at the end of the title-page block but says "below".
  - Possible purpose: probably means that anything not listed (headings, alignment, page numbers) is the team's
    choice. Safe reading: follow the sample layout (R-I59, R-I60) and add nothing banned (R-I55).
- **R-AN38 No citations in the IPS versus citing everything.**
  - IPS p.3 L123-125: "formal citations are not permitted" and "sources do not need to be cited in the IPS". [RULES]
    Code of Conduct: "required to properly cite any sources used". [AI]: "must be recorded in your Works Cited pages".
  - Possible purpose: keeps the IPS a clean, persuasive 500 words and moves the evidence to the Final Report (IPS
    L125).
- **R-AN39 Two pages double-spaced for 550 words is tight but workable.**
  - IPS p.3 L103-118. The official placeholder averages 13-15 words per line (R-I61).
  - ASSUMPTION (estimate from the sample, not a measurement of a real document): 9 inches of usable height at double
    spacing gives about 23 lines per page, so about 46 lines. 550 words plus two headings needs roughly 42-44 lines.
  - Possible purpose: the page limit and the word limit together punish padding. Test-print the real PDF.
- **R-AN40 The Trading Notes come before the IPS.**
  - Case p.4 L150-160 order: Trading Notes → IPS → Final Report. TN guide L17-21: the strategy "may continue to evolve"
    but notes must be "consistent with the strategic approach your team is developing and will later articulate in its
    IPS."
  - Possible purpose: rewards teams that have a strategy before trading. The notes show how it was "reflected, tested,
    or refined".
- **R-AN41 Official sources disagree on what selects the semifinalists.**
  - [RULES]: "based on the strength of their Investment Policy Statement (IPS) and Final Reports". [S-DELIV]: "Your
    Trading Notes Analysis, Investment Policy Statement and Final Report are evaluated." Case L161: "Evaluators will
    consider the three deliverables together."
  - Possible purpose: none; probably different pages were updated at different times. Safe reading: treat all three as
    scored.
- **R-AN42 "Yes, we will verify this."**
  - TN p.2 L53. An unusually informal, emphatic sentence in a formal guide.
  - Possible purpose: a warning, likely prompted by teams inventing or editing notes. It pairs with "exactly as it
    appears in WInS" (L44).
- **R-AN43 Notes are locked when written.**
  - TN L44: "Include each Trading Note exactly as it appears in WInS." [S-WINS]: "record the reasoning, research, and
    intended strategic role of each decision at the time it is made."
  - Possible purpose: the note shows thinking at the time of the trade. The reflection (100 words or fewer) is the only
    place to add hindsight. Every note written from now on is a potential deliverable.
- **R-AN44 Wharton's own example note is a bond fund for the payments.**
  - TN p.2 L36-39: "an intermediate-term U.S. Treasury bond ETF to reduce portfolio volatility and begin preparing for
    Laura’s future operating commitment".
  - Possible purpose: shows the expected quality of a note: a purpose, a link to Laura, and a named risk ("although
    interest-rate changes may affect its value"). It also hints that preparing for the liability is a legitimate
    trading theme. Many teams will copy it, so matching it does not make a team stand out (INTERPRETATION).
- **R-AN45 "Funding purposes" counts as a kind of diversification.**
  - [S-TRADE]: "diversification across asset classes, sectors, industries, market capitalizations, geographic regions,
    risk characteristics, and funding purposes."
  - Possible purpose: lets a portfolio split by goal (for example, money for the payments versus money for growth)
    count as diversification. Relevant to criterion 1, "uses appropriate diversification" (R-S24).
- **R-AN46 "The long-term portion of your portfolio".**
  - [S-FAQ]. Implies the designers expect portfolios to have more than one portion.
  - Possible purpose: may be older FAQ wording, but it fits a split portfolio.
- **R-AN47 Editing slips on the web pages.**
  - "The 2026-2027 has four REQUIRED Deliverables" (R-S2); "Get to the know the client" (R-W54); "MARGING TRADING" and
    "provide your with information" (R-W100); "the teams final portfolio value" (R-W91).
  - Possible purpose: none. These pages are lightly edited, so avoid reading hidden meaning into single words there.
    The PDFs are the carefully edited documents.
- **R-AN48 The bond lists differ slightly.**
  - [S-TRADE]: Treasury bonds from six named countries. [S-FAQ]: "Any Government/Treasury Bonds from any exchange
    available on WInS."
  - Possible purpose: none. In practice, what WInS lists is what is allowed. Check in WInS before trading.
- **R-AN49 "Any ETF" versus "no derivatives".**
  - [S-TRADE] "Any ETF available on WInS" and [S-FAQ] "Derivatives (options, futures, swaps, etc.)" are "NOT
    permitted". Leveraged and inverse ETFs use derivatives internally.
  - Possible purpose: unclear. The safe course is to avoid leveraged, inverse or options-based ETFs unless Wharton
    confirms them. Confirm against this year's WInS list and rules before trading.
- **R-AN50 The $5 stock rule has no stated timing.**
  - [S-TRADE]: "priced at $5 or more". It does not say whether this applies only at purchase.
  - Possible purpose: blocks penny stocks. Likely irrelevant to a fund-and-bond strategy.
- **R-AN51 A 200-trade cap with flat commissions.**
  - [S-TRADE] and [S-FAQ]: $25 per stock trade, $10 per bond trade.
  - Possible purpose: discourages frequent trading. With $300,000 the cost is small (DERIVED: 20 trades cost at most
    $500). The trade count matters more than the cost.
- **R-AN52 Bond prices update once a day and coupons are paid every six months.**
  - [S-FAQ].
  - Possible purpose: explains why WInS bond values look stale within the day. Individual bonds behave like real
    Treasuries, coupons included, which matters for matching the payment dates.
- **R-AN53 The goals are already fixed.**
  - Case p.2 L39-41: "Working with your portfolio manager, Laura has identified several long-term financial
    objectives".
  - Possible purpose: teams build the strategy; they do not renegotiate the goals.
- **R-AN54 Three deliverables are evaluated; four are required; school documentation is extra.**
  - [S-DELIV] and case L150.
  - Possible purpose: administrative items (roster, school documentation) are pass/fail gates, not scored.
- **R-AN55 Week language versus dates.**
  - Case L163 "beginning of Week 7". TN L17 "Week 6". SMApply gives dates.
  - Possible purpose: the guides may be reused across years. The dates line up this year (R-W39).
- **R-AN56 "While the client is real, the financial scenario is developed specifically for the competition."**
  - [MAIN].
  - Possible purpose: tells teams that public facts about the person can inform understanding, but the money story is
    fiction. Do not import her real finances or real plans.
- **R-AN57 A no-contact rule, with disqualification.**
  - [RULES] and [S-CLIENT].
  - Possible purpose: fairness, and the client's privacy. Consistent with the brief's privacy rule.
- **R-AN58 Who receives the payments is left vague.**
  - Case p.3 L88: "payments of $50,000 toward the residency’s operating expenses". It does not say whether an entity or
    a bank account receives them.
  - Possible purpose: keeps legal structure out of scope (compare L168-169).
- **R-AN59 Nothing after 2042.**
  - Case L92-93. It says nothing about money left over after the last payment.
  - Possible purpose: bounds the problem. Leftover money is covered only by "flexibility" (R-C84).
- **R-AN60 Last season's field was much smaller than the headline registration number.**
  - [NEWS]: "more than 6,300 registered teams" versus "some 2,300 teams … submitted final reports". [MAIN] counter:
    2,339 teams.
  - Possible purpose: none. For the team, the realistic rival field is the teams that finish (about 2,300 last year),
    not everyone who registers. The North Star's "6,000 others" fits the registered count, not the finishing count.

---

## 8. Cross-document consistency (X)

Each item: what the IPS guide, Trading Notes guide or web pages say, and how it constrains or pulls against the case.

- **X-1 Horizons.** IPS L10 "time horizons" and L13 "changing time horizons"; criterion 1 "Laura's changing time
  horizons" (R-S24). The case has five dated points: 2027, 2028, 2031, 2033 and 2033-2042. Consistent. The team should
  name them explicitly.
- **X-2 Changing allocation versus "if at all".** IPS L22-23 (prompt 4) and L47 ("planned changes in the portfolio as
  future funding needs approach") versus case L96 ("if at all"). Mild tension. The case allows a static reserve; the
  IPS expects the overall portfolio's plan to change over time.
- **X-3 Where the numbers go.**
  - The IPS guide (L68-70) and the Trading Notes guide (L20-22) both exclude the final reserve calculations,
    projections, the final range and the co-sponsor draft. The case requires all of these, so they are Final Report
    items.
  - The IPS must still carry the approach to the reserve (L48-50) and the "desired degree of funding certainty" (L10).
    So the *definition* of certainty plausibly belongs in the IPS while the *calculation* does not (INTERPRETATION).
- **X-4 Individual investments.**
  - The IPS says describe the framework "rather than describing individual investments" (L51-52).
  - The Trading Notes are about individual decisions, but "as part of a cohesive portfolio strategy" (TN L14-15).
  - A clean division: the notes carry the specifics and the IPS carries the rules.
- **X-5 The freeze chain.** TN L18-19 (strategy may evolve) → IPS L73-74 ("may not revise its investment strategy after
  the submission deadline") → Final Report "evaluates how that strategy was implemented" (case L158). Criterion 1
  requires "consistency with the team's IPS". Any strategy change must happen before 6 Nov and be explained in the
  Final Report.
- **X-6 The WInS freeze date is the IPS date.** [S-DELIV], [S-TRADE], [S-WINS]: the portfolio is frozen on 6 Nov. IPS
  L75: "Your portfolio and Final Report should reflect the strategy established in your IPS." The WInS holdings on 6
  Nov will be read against the IPS.
- **X-7 WInS $300,000 versus a two-deposit plan.**
  - Case L129-133: WInS = implementation; its results stay out of projections. [S-TRADE]: the $150,000 "will not be
    added to WInS".
  - No document says whether WInS should show the Year-1 portfolio or the long-run target. This is a team choice to
    state and defend (open item in the brief).
- **X-8 Semifinal selection basis.** [RULES] says the IPS and Final Reports. [S-DELIV] says all three evaluated. Case
  L161 says the three together. The FAQ says "all five components of the criteria". Treat all three as scored.
- **X-9 Citations.** IPS L123-125 (no formal citations in the IPS; sources in the Final Report). [RULES] Code of
  Conduct (cite all sources). [RULES] and [AI] (cite AI; record AI use in "Works Cited pages"). Consistent only if the
  Final Report has a Works Cited section that includes how AI was used. The IPS has no citations but must not contain
  AI-written text (R-W26).
- **X-10 Advisor.** Case framing (the advisor decides) versus [RULES] and [S-FAQ] (the advisor may not decide or trade).
  The real rules govern conduct. The case framing governs only the story.
- **X-11 Risk tolerance.** IPS definition (L3) and the [RULES] IPS description ("risk tolerance") versus the case
  ("thoughtful risks", "appropriate balance"; no number). The IPS must state a risk tolerance that the team derives
  from the case.
- **X-12 Diversification.**
  - Criterion 1: "uses appropriate diversification". IPS L46-47: "portfolio construction and diversification".
    [S-TRADE]: no sector minimum; diversification by "funding purposes" counts.
  - Consistent: diversification is expected but defined broadly.
  - This removes the unverified "sector minimum" constraint from the brief (section 6).
- **X-13 Instruments.** The TN example uses a Treasury bond ETF. [S-TRADE] and [S-FAQ] also allow individual
  government bonds. Derivatives are banned. Both bond routes are open in WInS in principle. Confirm what is actually
  listed in WInS before trading.
- **X-14 Communicating with co-sponsors.** Case L143: "Communicates Laura’s potential facility contribution to
  co-sponsors clearly and credibly." Criterion 5: "communicates Laura's potential facility contribution and investment
  uncertainty clearly and credibly to prospective co-sponsors." Nearly the same words. The criterion adds "investment
  uncertainty".
- **X-15 Reasonable assumptions.** Case L132 "reasonable return assumptions consistent with their strategy";
  criterion 3 "reasonable assumptions and projections"; [S-TRADE] and [S-WINS] repeat it. Consistent. Returns must be
  defensible, and consistent with the chosen strategy.
- **X-16 A shared vocabulary.** The same five words recur across documents: growth, risk, liquidity, funding
  reliability, financial flexibility (IPS L20 and L59; TN L5; [S-WINS]). The case uses "financial flexibility" and
  "funding confidence" (L127). These are the graders' own terms (INTERPRETATION).
- **X-17 Voice.** Criterion 5 "an authentic team voice"; [AI] "they must use their voice and words"; [RULES] Ethics "invent teamwork and experiential stories" is banned; [FAQ] "clearly and authentically". Consistent. The reflections and the Articulation section must be the students' own and true.
- **X-18 Trading activity.**
  - [RULES]: "must meet the required trading activity". [S-WINS]: not judged on "How many trades you make". [S-FAQ]:
    avoid "a lot of buying and selling". [S-TRADE]: cap of 200 trades.
  - The public pages set no minimum number. Some minimum may exist in the logged-in portal or in WInS weekly emails.
    Check.
- **X-19 Where the judging weight falls.** Case L161 says the deliverables are judged together. [FAQ] says criteria are
  "reflected in various ways in their final reports". The Final Report is the main showcase, but the IPS is the anchor.
- **X-20 Dates.** Case "beginning of Week 7" = [S-DELIV] "November 9". TN "Week 6" = IPS due 6 Nov. [FAQ] 10 weeks, 28
  Sep to 4 Dec. Consistent.
- **X-21 Names.** IPS title page "First Name, Last Initial" versus the roster, which requires full names, emails and
  birthdays (R-S13). The repo keeps first names only (brief privacy rule).
- **X-22 Year 0 versus WInS.** Case Year 0 = 2026, "before any money has been invested", while WInS trades real market
  prices in 2026. Consistent with R-C76. WInS is a demonstration of the strategy, not Laura's money.
- **X-23 An IPS as a rulebook.** IPS L3-5 (guidelines; disciplined decisions in changing markets) and L61-62 ("guide
  portfolio construction and investment decisions as the client’s needs change"), together with the case's "favorable
  and unfavorable" scenarios (L118, L148). The IPS should contain the decision rules the Final Report later tests
  (INTERPRETATION).
- **X-24 Corrections to the brief and CLAUDE.md** (VERIFIED-PRIMARY, pages cited above):
  - "Approved list, starting cash and WInS rules are UNKNOWN": now largely known. Starting cash $300,000. Allowed:
    stocks at $5 or more, any ETF on WInS, government bonds on WInS, cash. Banned: margin, shorting, stock-secured debt,
    crypto, derivatives. Cap of 200 trades. Volume cap of twice the daily volume. Commissions $25 per stock trade and
    $10 per bond trade.
  - "sector minimum = team size": contradicted ("no required sector allocation or minimum number of sectors").
  - "200-trade cap": confirmed.
  - "first trade by Oct 10": not found on any public page; still unverified.
  - "2025-26 starting cash $500k": confirmed by [NEWS]. This season is $300,000.
  - The historical 2025-26 ETF list is not needed this year, since any ETF on WInS is allowed.
  - Still to check inside WInS: which specific ETFs and bonds are actually listed, and whether any minimum trading
    activity rule exists.

---

## 9. Sources (all accessed 2026-09-27)

- Repo official files (VERIFIED-REPO-FILE):
  - `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt` and `.pdf`
  - `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt` and `.pdf`
  - `competition/official/2026_27/2026_WGY_Trading_Notes_Analysis-FINAL.txt` and `.pdf`
  - `competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md`
  - `competition/official/2026_27/manifest.yaml`
- Box official PDFs (VERIFIED-PRIMARY, hash-matched):
  - https://upenn.box.com/shared/static/i4t4b2n4ycjkev7p78mhyjsvypombkxo.pdf
  - https://upenn.box.com/shared/static/0iib496jhswp30c12zhn6b2fret8dl30.pdf
  - https://upenn.box.com/shared/static/3pxn798a1lnlifkikj4g56srmg2ijuo6.pdf
- Wharton pages (VERIFIED-PRIMARY), keys as in section 6:
  - https://globalyouth.wharton.upenn.edu/competitions/investment-competition/
  - …/rules-roles/
  - …/faq/
  - …/register-now/
  - …/archive/
  - https://globalyouth.wharton.upenn.edu/ai-policy/
  - https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- SMApply public pages (VERIFIED-PRIMARY):
  - https://wghsinvcomp.smapply.us/
  - https://wghsinvcomp.smapply.us/res/p/client/
  - https://wghsinvcomp.smapply.us/res/p/trading/
  - https://wghsinvcomp.smapply.us/res/p/wins/
  - https://wghsinvcomp.smapply.us/res/p/faqs/
  - https://wghsinvcomp.smapply.us/res/p/deliverables/
- Not reached: https://edu.stocktrak.com/wharton/ (WInS itself; needs the team login, not attempted). The logged-in
  SMApply pages (weekly updates, forms) are not public.

---

## What this teaches

1. Read a contract (and a case is a kind of contract) three ways:
   - Pull out the **hard rules** ("must", "may not").
   - Pull out the **undefined words** ("high degree of certainty", "responsibly", "credible"). The team has to define
     these itself, and that is where teams win or lose marks.
   - Note what is **left out**. Currency, a risk-tolerance number and a confidence level are all missing, so any
     choice there must be explained.
2. Always check whether the official source says more than you were told. Here, the "unknown" trading rules were
   sitting on public pages. Knowing them (no sector minimum, individual Treasury bonds allowed, 200 trades, no
   derivatives) changes what the team can safely do.
3. When official sources disagree (which deliverables pick the semifinalists; citations or none), do not pick the
   convenient one. Adopt the reading that keeps you compliant with all of them, and write down why.
