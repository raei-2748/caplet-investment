# D10 Compliance Officer: which book WInS shows (M005) and the IPS governance lines (M013)

Agent D10 (Compliance Officer), insight_v1 run. Written 2026-09-28 (the first official trading day). Scope follows brief
sections 16-17: this file serves **WInS trading now + the Trading Notes (TN, Oct 23)** and **the IPS (Nov 6)** only.
Final Report items are listed at the end as one-line "later" entries. Everything here is AI-generated research:
specifications, rule checks, numbers and checklists. **None of it is text to submit.** The team decides, and writes
every WInS note, reflection and IPS sentence in its own words (Wharton AI policy, quoted in section 4).

Status labels (brief section 3): VERIFIED-PRIMARY (VP), VERIFIED-REPO-FILE (VRF), SNIPPET-UNVERIFIED, ASSUMPTION,
INTERPRETATION (my reading of an official text, not a fact).

Scripts (run from the repo root):
- `.venv/bin/python research/insight_v1/scripts/D10_wins_book_compliance.py` (M005: the three candidate books under
  each possible position limit; volume rule; equity-share consistency; position-limit drift).
- `.venv/bin/python research/insight_v1/scripts/D10_ips_page_fit.py` (M013: does 50 + 500 words fit on two
  double-spaced Times New Roman pages; the word budget left for governance).

Terms used: **hedge / promise money** = the Treasury funds standing in for the ten fixed $50,000 payments (2033-2042).
**Growth money / sleeve** = everything the payments do not need. **Funded ratio** = money set aside for the promise
divided by the market price of the ten payments. **Position limit** = the most WInS lets the team hold in one security
(shown only in the logged-in Portfolio Summary > Session Rules). **Book** = the list of holdings at one date.

---

## Summary: top findings (ranked by impact on reaching the semifinals and on making the plan Laura's)

1. **The IPS page limit is the most likely way to lose a semifinal place, and 550 words barely fit** (tier 2, act
   now). At Times New Roman 12, double-spaced, 1-inch margins, the 50-word pitch plus a 500-word IPS fill about
   **92-105% of the two allowed pages on U.S. Letter** (script; ASSUMPTION-based layout model). Word's default 8pt
   space after each paragraph and more than about 7 paragraphs push it over. On A4 (an Australian default) it fits
   more easily (about 89-99%). A breach means "will not be considered for semifinal selection" (IPS guide L82-83,
   VRF). Checklist in M013.
2. **M005: no official rule decides which book WInS shows; the IPS sentence naming the date is required either way.**
   Both the post-2028 mix scaled to $300k (ticket option ii) and the literal January-2027 book (option iii) pass every
   WInS rule, whatever the position limit turns out to be (script). What the rules do require is **consistency**: the
   frozen Nov-6 portfolio must "reflect the strategy established in your IPS" (IPS guide L75, VRF), and the Investment
   Strategy criterion scores "consistency with the team's IPS" (SMApply, VRF). WInS equity differs from Laura's real
   January-2027 equity by **+20.5 points under (ii)** and **0 under (iii)** (script), so (ii) needs a longer
   explanation. **The "middle path" (about 3% growth slice) is mis-posed:** at today's prices the literal leftover is
   **$4.4k-6.6k (1.5-2.2% of WInS), so equity would be only 0.9-1.3%**, and it reverses the ticket's rule that the 2027
   leftover waits in T-bills. Drop it. D10 leans to (iii) at medium-low confidence; (ii) is equally compliant if the
   three-element sentence is in the IPS.
3. **The book must be chosen before the first order, because trade notes are permanent** (tier 1). Notes cannot be
   edited, only added to (Stock-Trak, via A4), and must be consistent with the later IPS (TN guide L30-31, VRF). A later
   switch between books is allowed (notes "do not need to correspond to investments that remain", TN L25-26, VRF) but
   must be a real, logged decision, not a same-day reversal ("Day Trading: This is not permitted", 2026-27 User Guide,
   VP via A4).
4. **M013: the IPS needs four governance elements in about 30-45 words beyond D8's four money rules.** They are:
   (a) who decides: the rules decide; Laura herself makes only the two choices the case gives her; **no "our portfolio
   manager/advisor approves" wording**, because the real rules say advisors "may not make decisions" (Rules page, VP
   2026-09-27); (b) review points at the case's own cash-flow dates plus a yearly check; (c) the event triggers **folded
   into one "promise first" priority rule** rather than listed; (d) one rebalancing sentence that also states the
   deliberate **no-rebalancing between promise money and growth money** (CFA: "If the policy is not to rebalance, this
   policy should be documented in the IPS", VP). Cut the org chart, firm name or size, fees, reporting terms, the
   residency-delay trigger and citations.
5. **Why governance is a compliance issue, not decoration:** after Nov 6 "you may not redesign your strategy after
   observing the results" but "planned adjustments as funding dates approach" are allowed (Guide p.5, VRF). Only
   adjustments the IPS pre-authorises can appear later without looking like a post-freeze revision. A named trigger
   costs about 5-10 words; a missing one can cost the whole scenario analysis its legitimacy.
6. **A funded-ratio trigger "below 100%" can never fire once the ladder is bought** (it is cash-flow matched, so the
   ratio stays at 100% barring a U.S. default). It can only matter **before** the January 2027 purchase or while part
   of the promise waits for the 2028 deposit (the ladder cost more than $300k on 173 of 185 trading days of 2026; about
   24% modelled odds on 2027-01-01, F-111/F-112). So the real trigger is a yes/no test: "is the promise fully bought?"
7. **Deliverables of this D10 task:** this working file; two scripts (`D10_wins_book_compliance.py`,
   `D10_ips_page_fit.py`); and the structured answers for M005 and M013 returned to the run. No submission text, no
   commits.

---

## 1. M005 (tier 1: WInS now + TN; the sentence is tier 2: IPS)

**Question (canonical, Phase C):** Should the WInS book (exactly Laura's $300k Year-1 deposit; the $150k is never
added) mirror her literal 2027 portfolio (about 97% Treasury ladder plus a small labelled surplus sleeve) rather than the
post-2028 ~65/35 target mix, and which one IPS sentence says which book WInS represents?

**Premise check.** Two corrections before answering:
- "65/35" is hedge/sleeve, not bonds/equity; the post-2028 book holds about **20.4% equity** (F-409, VRF; ticket
  section 2). Option (i) (35% equity) is already dropped.
- "About 3% surplus sleeve" overstates the leftover. The ten payments cost $292,264 (F-101) to $294,387 (STRIPS
  ladder, ticket). After 4-7 commissions ($25 each) and a $1,000 cash float (ASSUMPTION, ticket band), the leftover is
  **$4,438-6,636 = 1.5-2.2% of WInS**; at 60/40, **VT would be $2.7k-4.0k (0.9-1.3%)** (script section 2).

**One-sentence answer:** No official document decides which book WInS shows, and both the literal January-2027 book
and the scaled post-2028 mix pass every WInS rule, so the compliance requirement is only that the IPS names the date
WInS represents and that the frozen portfolio can be produced by the IPS rules at that date; the "middle path" is
mis-posed (about 1% equity, and it reverses the plan's 2027 leftover rule), and D10 leans to the literal January-2027
book because it is the only one that is true at a stated date without scaling.

### 1.1 What the official texts say (all re-read)
| # | Claim | Source | Status |
|---|---|---|---|
| E1 | "The WInS portfolio represents each team’s implementation of its investment strategy during the competition. It does not determine Laura’s actual portfolio value at the beginning of 2027." | Case p.4 (`Laura_Gao_2026_Client_Profile.txt` L129-130) | VRF |
| E2 | "The $300,000 is your team's WInS simulator balance. The additional $150,000 contribution described in the Client Case Study will not be added to WInS." | https://wghsinvcomp.smapply.us/res/p/trading/ (read 2026-09-27/28, helper `--grep` YES) | VP |
| E3 | "There is no required sector allocation or minimum number of sectors. However, diversification remains an important investment principle." ... "funding purposes. The goal is to build an intentional mix of investments appropriate for your strategy, not simply to own a large number of securities." | same page | VP |
| E4 | "Your portfolio and Final Report should reflect the strategy established in your IPS." | IPS guide L75; Guide p.2 L60-61 | VRF |
| E5 | Investment Strategy criterion: "uses appropriate diversification; and maintains consistency with the team's IPS." | `SMApply_Deliverables_Page_2026-09-27.md` L49 | VRF |
| E6 | "The analysis should be consistent with the strategic approach your team is developing and will later articulate in its IPS." / "The Trading Notes you select do not need to correspond to investments that remain in your portfolio at the end of the competition." | TN guide L25-31 | VRF |
| E7 | Trading Note should capture "its expected role in growth, liquidity, risk management, or future funding." / WInS "is not the competition scorecard" / "your portfolio provides evidence of the decisions your team made" | Guide p.3 L70-86 | VRF |
| E8 | "Collectively, the decisions should demonstrate how your team used individual investments as part of a cohesive portfolio strategy." | TN guide L14-15 | VRF |
| E9 | "Focus on the strategy and decision-making framework that guide your portfolio rather than describing individual investments" | IPS guide L51-52 | VRF |
| E10 | "Day Trading: This is not permitted." / "Position Limit: This is how much of your portfolio you can invest in one single stock." (a 2024 screenshot shows a separate bond "Position Limit (Single Position) 100%") | 2026-27 WInS User Guide p.6, via `phase_A/wins_week1_guardrails.md` | VP (via A4) |
| E11 | Stock-Trak default "position limit is 25%" | edu.stocktrak.com/wharton/portfolio-faq/ (generic, 2023) via A4 | VP (generic, not this season) |
| E12 | Trade notes: "students cannot edit or delete their trade notes ... they can add more notes" | Stock-Trak blog 2017 via A4 | VP (vendor, not season-specific) |
| E13 | No document states which date's book WInS should show | `phase_A/case_register.md` X-7, R-AN14 | VRF (A1's search) |
| E14 | "Take only investment actions that are consistent with the stated objectives and constraints of that portfolio" (B.5.a); disclosures must be "truthful, accurate, complete, and understandable" (F.2) | CFA Institute *Asset Manager Code*, 2nd ed., via `phase_A/stakeholder_map.md` SH-25 and D8; the Rules page tells teams to "operate by these standards" (re-read 2026-09-27, `--grep` YES) | VP |

### 1.2 Rule check of the three books (script sections 1 and 4)
All three use only ETFs and cash (permitted), no margin, no shorting, no derivatives. Every order is at most **0.2% of
the "twice the current daily volume" cap** for the funds whose issuers publish volume (IEF, TLH, SPTL); Vanguard funds
(VT, VGSH, VGIT, VGLT) publish no volume, so read it in WInS (ticket check 5). All securities remain **PENDING WInS
AVAILABILITY + POSITION-LIMIT CHECK**.

| Book | No limit | 35% limit | 25% limit | WInS equity |
|---|---|---|---|---|
| (ii) post-2028 mix scaled | IEF 23.6 / TLH 42.4 / VT 20.5 / VGSH 12.5 / cash 1; 4 trades, $100 | + SPTL 8.4 (TLH 34); 5 trades, $125; hedge ~10.2y | IEF 23.6 / TLH 24 / SPTL 18.4; 5 trades, $125; hedge ~10.5y | 20.5% |
| (iii) literal Jan-2027 | IEF 35 / TLH 63 / cash 2; 2 trades, $50 | IEF 34 / TLH 34 / SPTL 30; 3 trades, $75; hedge ~10.6y | IEF 24 / TLH 24 / SPTL 24 / VGIT 17.6 / VGLT 8.4; 5 trades, $125; hedge 9.9y | 0% |
| (mid) literal + growth slice | IEF 35.1 / TLH 63.1 / VT 0.9 / VGSH 0.6; 4 trades, $100 | 5 trades, $125 | 7 trades, $175 | 0.9% |

- **Continuous-limit risk** (ASSUMPTION that WInS re-checks the limit as prices move): under a 25% limit, a holding
  placed at 24% crosses 25% after rates fall about **101bp (ii, TLH)** or **118bp (iii, SPTL)**, or rise about **128bp
  (iii, IEF)** (first-order duration arithmetic, script section 4). The 10-year yield moved about 120bp from its
  February low to September in 2026 (F-003), so this is possible within six weeks but unlikely. If Session Rules
  show the limit is checked only when an order is placed, ignore it. Note (E10): the User Guide says the limit is per
  "single stock", and an older screenshot shows a separate 100% bond limit, so **read both lines** in Session Rules.
- None of the three breaks a rule. Rule compliance does not choose between them.

### 1.3 Consistency check (the binding requirement)
WInS equity minus the equity share of Laura's real portfolio at each plan date, in percentage points (script
section 3; real shares: 0% in January 2027 under the T-bill rule, 20.4% in 2028-2030 (F-409), about 4% after the 2031
floor (brief section 16), all ASSUMPTION-based):

| Book | Jan 2027 | 2028-2030 | After the 2031 floor |
|---|---|---|---|
| (ii) | **+20.5** | +0.1 | +16.5 |
| (iii) | **0.0** | -20.4 | -4.0 |
| (mid) | +0.9 (−0.1 if the growth-mix rule replaces the T-bill rule) | -19.5 | -3.1 |

Reading (INTERPRETATION): every book matches exactly one date, so **the IPS must say which date WInS shows under any
choice**. Under (iii) the date is the one Laura's real money first exists in the plan, so the explanation is short
("WInS is her first deposit on the day it is invested"). Under (ii), WInS holds about 20% stocks while the IPS's own
first-year allocation is about 0%, so the sentence needs the three elements already specified in the ticket (section
2): the post-2028 mix; scaled to $300,000; and that in January 2027 almost all of her real $300,000 buys the ladder.
Under Asset Manager Code F.2 (truthful, complete disclosure), a (ii) book should never be called "Laura's portfolio"
in a note or the IPS without that scaling caveat.

### 1.4 The trade-offs the rules leave open (for the team's vote, ticket gate box b)
| | (ii) | (iii) |
|---|---|---|
| Diversification criterion (E3, E5) | Three funding purposes visible in WInS (promise, growth, short Treasuries) | One funding purpose in WInS; diversification by purpose shown only in the IPS |
| TN variety (E7, E8) | Notes can show three roles: future funding, growth, liquidity | Notes show future funding / risk management only; the third note must come from a genuine later decision (duration refresh, position-limit response) |
| Consistency burden | Needs the three-element sentence (ASSUMPTION: ~30-40 words of 500) | Needs a short date sentence (ASSUMPTION: ~12-20 words) |
| What WInS says about Laura | "Her whole plan, in miniature" | "Promise first": what her real money does first; fits her verified concern about not letting down "people who were your earliest supporters" (D13a; use only as D13 allows, never in the TN or IPS) |
| Main risk | Reader sees ~20% stocks against a ~0% first-year plan and suspects inconsistency | Reader sees ~98% Treasuries for a client "willing to take thoughtful risks" and suspects timidity |

**D10 lean (medium-low confidence):** (iii). Reasons: it is the only book true at a stated date without scaling; it
needs the shortest reconciling sentence in a tight IPS (finding 1); it shows the plan's central priority in the WInS
holdings themselves. **(ii) is equally compliant** if the three-element sentence is in the IPS and no note calls the
holdings "Laura's portfolio". This is a team decision; record the vote and the reason in the decision log before the
first order.

**Drop the middle path.** A 0.9-1.3% VT position (about $2.7k-4.0k) would carry a $25 commission and a whole trading
note about a sliver that grows only in 2028. It also needs the ticket's 2027 leftover rule (T-bills; S4 finding 13)
changed to "growth mix from day one". It adds a rule change and a weak note for no compliance gain.

### 1.5 Implication
- **WInS-now (decision, before the first order):** vote (ii) or (iii) using the table above; screenshot Session Rules
  (both position-limit lines); pick the cap branch from the ticket/script. The middle path is off the table.
- **TN (sentence spec, not text):** whichever book, each note's reasoning must be true of that book on its trade date.
  Under (ii), a note on VT or VGSH must say the holding represents the growth money after the second deposit. Under
  (iii), no note may imply WInS holds growth assets.
- **IPS (one sentence, tier 2), must contain:** (1) the date WInS represents (January 2027 for (iii); "after both
  deposits, scaled to $300,000" for (ii)); (2) that WInS holds stand-in funds that move like her payments, not the
  ladder itself; (3) for (ii) only: that in January 2027 almost all of her real $300,000 buys the ladder. No tickers,
  no weights to decimals (E9).

**Numbers and where they come from:** leftover $4,438-6,636 (1.5-2.2%); VT 0.9-1.3%; equity gap +20.5 / 0.0 pts;
position counts 2-7; commissions $50-175; worst order 0.19% of the volume cap; limit-drift 101-128bp (all from
`D10_wins_book_compliance.py`, inputs VRF/VP as listed in its docstring).

**Deadline tier:** 1 (vote before the first order); the IPS sentence is tier 2.
**Confidence:** high that both books comply and that the date sentence is required; medium-low on the lean to (iii).
**Changes current strategy:** yes, slightly: it removes the middle path and moves the ticket's lean from (ii) to (iii);
the lock-early strategy itself is unchanged.
**Criterion served most:** Investment Strategy ("consistency with the team's IPS"; "appropriate diversification").
**What this teaches:** a simulator is a picture of a plan at one moment. A plan that changes over time can only be
photographed at one date, so say which date the photo shows.

---

## 2. M013 (tier 2: IPS)

**Question (canonical, Phase C):** Which governance elements must the 500-word IPS carry (who decides what among
automatic rules, the firm and Laura; dated reviews in 2028, 2031 and 2033; event triggers such as a funded ratio below
100%, a short or late deposit or a residency delay; one rebalancing rule), and which can be cut?

**Status of the question:** partly answered already. D8 (`phase_D/D8_practice.md`, M006/M235) set the four money
rules (promise first; growth mix; 2031 range; 2033 order of use) at about 110-155 words plus one governance line.
The "answered" skeptic killed M013 for that reason. What is new here: the compliance reasons (the advisor rule and the
freeze rule), folding the triggers into rule 1, the funded-ratio point, the cut list, and the page-fit test.

**One-sentence answer:** On top of D8's four money rules, the IPS needs about 30-45 words of governance: the rules
decide and Laura herself makes the two choices the case gives her (no "portfolio manager/advisor approves"); reviews at
the case's own cash-flow dates plus a yearly check, where rules change only if her circumstances change and never
because markets moved; event triggers folded into the "promise first" rule; and one rebalancing sentence that states
the no-rebalancing policy between promise and growth money. Everything else (org chart, firm details, fees,
reporting, residency-delay trigger, citations) is cut.

### 2.1 Evidence
| # | Claim | Source | Status |
|---|---|---|---|
| G1 | "Advisors may not make decisions on behalf of students or actively participate in team activities, trading decisions, or strategy development." | https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ (read 2026-09-27, `--grep` YES) | VP |
| G2 | "Your portfolio manager (your team’s teacher/advisor who makes the final investment decisions for your firm’s portfolio)" | Case p.1 L4-5 (R-C3) | VRF |
| G3 | The same line appears in the 2021-22 and 2022-23 cases, where the firm (WGAM) "currently manages a $100,000,000 portfolio": it refers to the firm's own book, inherited wording | `phase_B/B1a_case_anomalies.md` E1 (Wharton archive) | VP via B1a (not re-checked by D10) |
| G4 | "Laura must decide how much of the remaining portfolio she can responsibly contribute"; in 2031 "she will need to describe how much she expects to contribute"; "she wants to communicate a credible range" | Case p.3 L101-117 | VRF |
| G5 | "Investment Policy Statement. This formally establishes the strategy and the team’s decision-making framework." | Case p.4 L155-156 (R-C89) | VRF |
| G6 | "Once submitted, the IPS becomes the official record ... Your team may not revise its investment strategy after the submission deadline." | IPS guide L73-74 | VRF |
| G7 | "A long-term strategy may include planned adjustments as funding dates approach, but it should not be rewritten simply because markets move or hindsight reveals a different outcome." / "you may not redesign your strategy after observing the results" | Guide p.5 L156-159 | VRF |
| G8 | IPS should explain "planned changes in the portfolio as future funding needs approach" and "How your strategy will guide portfolio construction and investment decisions as the client’s needs change" | IPS guide L46-47, L61-62 | VRF |
| G9 | CFA *Elements of an IPS for Individual Investors* (2010): "2a. Specify who is responsible for determining investment policy, executing investment policy, and monitoring the results"; "It can reinforce the obligations of advisers to offer counsel and the obligations of principals to ultimately approve or disapprove of the policy." "2b. Describe the process for reviewing and updating the IPS." "A process for refreshing the IPS as investor circumstances and/or market conditions change should be clearly identified in advance." Example review "no less frequently than annually". "4c ... If the policy is not to rebalance, this policy should be documented in the IPS." "the IPS serves as a policy guide that can offer an objective course of action to be followed during periods of market disruption" | https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf (read 2026-09-28 with the helper) | VP |
| G10 | "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted." "Submissions that do not meet the requirements below will not be considered for semifinal selection." TNR 12, double-spaced, 1-inch margins, pages 2-3 "2-page maximum", pitch max 50 words, IPS max 500 words | IPS guide L82-123 | VRF |
| G11 | Ladder cost > $300k on 173 of 185 trading days of 2026; ~24% modelled chance on 2027-01-01 | F-111 (VP inputs), F-112 (ASSUMPTION) | as labelled |
| G12 | The case says the $150,000 "will" be contributed | Case p.2 L43-45 (R-AN35) | VRF; a short or late deposit is the team's own stress scenario and must be labelled so |
| G13 | Liberation Serif is metrically compatible with Times New Roman | https://en.wikipedia.org/wiki/Liberation_fonts (read 2026-09-28) | secondary source; used as ASSUMPTION |

### 2.2 Keep / cut (each element traced to a source)
| Element | Keep or cut | Why (source) | Word budget (ASSUMPTION) |
|---|---|---|---|
| **Who decides** | KEEP: the students' rules run the portfolio; Laura makes the two choices the case gives her (the 2031 range she announces, the 2033 facility amount), on the team's rule-based recommendation | G4 (the case gives those decisions to her); G9 2a (principal approves, adviser counsels); G1 | 10-15 |
| "Our portfolio manager / advisor approves" | **CUT** | G1: in the real rules the advisor may not decide; G2/G3: the fiction's PM decides the *firm's* book and is inherited wording. Zero benefit, some risk of a reader thinking the advisor made strategy decisions | 0 |
| **Review points** | KEEP: at the case's cash-flow dates (Jan 2028 deposit, 2031 announcement, Jan 2033 reserve) plus a yearly check; rules change only for a change in Laura's circumstances, never because markets moved | G7, G8, G9 2b; D8 governance line | 12-18 |
| **Event triggers** | KEEP, but **inside rule 1 (promise first)**, not as a separate list: whenever the promise is not fully bought (ladder cost above the cash on hand; 2028 deposit short or late), the next money completes it before any growth | G6/G7 (a response must be pre-authorised to count as "planned"); G11 (binds in about 1 in 4 modelled paths); G12 (label the deposit scenario as the team's own) | 0 extra (already in D8's rule 1) |
| "Funded ratio below 100%" as a trigger | **Replace** with the yes/no test "is the promise fully bought?" | Once the ladder is bought it is cash-flow matched, so the ratio stays at 100% barring default; the test only bites before the purchase or while the 2028 top-up is pending (G11) | 0 |
| Residency delay trigger | **CUT** | The case fixes 2033; a delay is outside the case (BS-07). A change in her circumstances is covered by the review line | 0 |
| **Rebalancing** | KEEP one sentence: the growth mix is reset to its target once a year (band as the team sets it); **promise money and growth money are never rebalanced against each other** | G9 4c (a no-rebalancing policy must be written down); ticket section 5; D8 rule 2 | 10-15 (part may overlap D8's rule 2) |
| Record-keeping / decision log | Implied only (FR material) | Code D.4 via SH-25; FR is out of scope now | 0 |
| Org chart, firm name or size, fees, reporting frequency | CUT from the IPS | Not asked by the IPS guide (L53-65); fees belong to the FR projections (BS-01) | 0 |
| Naming CFA / citing sources | CUT | G10: "formal citations are not permitted"; naming a code in running text is not a formal citation (INTERPRETATION), but it spends words for no gain | 0 |

**Total governance ≈ 30-45 words**, on top of D8's four money rules (110-155 words). That leaves about 300-360 words
for the thesis, the client-specific reasoning (why this is Laura's plan), risk/return, liquidity and diversification,
which the IPS guide asks for first (L53-65).

### 2.3 Page-fit test (script `D10_ips_page_fit.py`; ASSUMPTION-based layout model)
Liberation Serif widths (same as Times New Roman), Word-style "double" = 2 x single line (26.6pt; Word may use up to
27.6pt, which is tighter), word lengths sampled from Wharton's own guides, 400 random layouts per setting:

| Paper | Paragraphs in the IPS | Space after paragraph | Share of the two pages used (median; p95) | Word slack at the median |
|---|---|---|---|---|
| Letter | 5 | 0pt | 92%; 101% | ~52 |
| Letter | 7 | 0pt | 94%; 101% | ~38 |
| Letter | 7 | 8pt (Word default) | 99%; 105% | ~5 |
| Letter | 9 | 8pt | 105%; 111% | ~-31 (overflows) |
| A4 | 7 | 0pt | 91%; 97% | ~60 |
| A4 | 9 | 8pt | 99%; 107% | ~7 |

Compliance checklist for the IPS file (tier 2; start testing with the first rough draft, not on Nov 6):
- [ ] Pitch at most 50 words and IPS at most 500 words **by the team's own count**; keep a margin (ASSUMPTION: aim for
      about 480) because Word and Google Docs count "U.S.", "$50,000", hyphens and slashes differently.
- [ ] Space after paragraphs set to 0; at most about 7 IPS paragraphs; the two headings on one line each.
- [ ] Export to PDF and confirm the file is **exactly 3 pages** (title page + 2), at most 5 MB.
- [ ] Times New Roman 12 everywhere, including headings; double-spaced; 1-inch margins all sides.
- [ ] No tables, charts, images, links, footnotes, citations; no bullet graphics pasted as images.
- [ ] Title page: official team name exactly as on the roster; members as "First Name, Last Initial" exactly as on
      the roster; the **WInS username** (not the team name).
- [ ] Every sentence written by a student; AI use logged for the Works Cited later (section 4).

### 2.4 Implication
- **IPS (decision + word budget):** adopt the keep/cut table; spend about 30-45 words on governance; put the triggers
  inside the promise-first rule; state the no-rebalancing policy between promise and growth money in words.
- **IPS (format):** run the page-fit checklist on every draft; set paragraph spacing to 0 now.
- **TN:** none directly, except that no note should say "our portfolio manager decided" (A4 checklist item 13).

**Numbers and where they come from:** governance 30-45 words (ASSUMPTION budget); D8 rules 110-155 words (D8); page use
92-105% on Letter, 89-99% on A4 (script); rates-fall branch binds ~24% of modelled paths and 173/185 days of 2026
(F-111, F-112).

**Deadline tier:** 2. **Confidence:** high on the advisor/freeze reasoning and the cut list; medium on the page-fit
numbers (a model of Word's layout, not the team's real file). **Changes current strategy:** no (it formalises the
current rules; it only removes the funded-ratio and residency-delay triggers as separate items). **Criterion served
most:** Investment Strategy (a clear framework consistent across deliverables).
**What this teaches:** a policy is judged by what it says it will do before anything goes wrong. Rules written in
advance let you act later without anyone asking whether you changed your mind after seeing the results.

---

## 3. Other compliance flags seen while working (outside M005/M013; one line each)
- **Today is the first trading day (Sep 28).** Nothing requires trading today ("does not require frequent or same-day
  trading", SMApply, VP); the ticket's five-box gate comes first.
- **"Required trading activity"** exists on the FAQ and Rules pages but is defined on no public page (FAQ re-read
  2026-09-28, VP). Read the logged-in Trading Details page this week; the "first trade by Oct 10" claim is still
  UNVERIFIED (a 2023-24 rule per A4).
- **AI-use log:** "If you use AI to assist you in any way during the competition, how you use it must be recorded in
  your Works Cited pages" (https://globalyouth.wharton.upenn.edu/ai-policy/, re-read 2026-09-28, VP). Start a dated
  log now (tool, date, what it was used for); the Works Cited itself is FR work.

## 4. Later (after Nov 9; Final Report) - one line each
- FR: Works Cited must record how AI was used (from the AI-use log).
- FR: school documentation needs an owner and an October request (BS-11; "Do not wait until the last minute", SMApply).
- FR: if (ii) was chosen, the evaluation of WInS must repeat that it was a scaled post-2028 mix.

## Sources (access dates 2026-09-27/28)
- SMApply Trading Details: https://wghsinvcomp.smapply.us/res/p/trading/ (VP; `--grep` checks run 2026-09-27/28).
- SMApply FAQs: https://wghsinvcomp.smapply.us/res/p/faqs/ (VP).
- Wharton Rules & Roles: https://globalyouth.wharton.upenn.edu/competitions/investment-competition/rules-roles/ (VP).
- Wharton AI policy: https://globalyouth.wharton.upenn.edu/ai-policy/ (VP).
- CFA Institute, *Elements of an Investment Policy Statement for Individual Investors* (2010):
  https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
  (VP, read 2026-09-28).
- CFA Institute, *Asset Manager Code*, 2nd ed. (via `phase_A/stakeholder_map.md` SH-25 and `phase_D/D8_practice.md`, VP
  there).
- Wikipedia, "Liberation fonts": https://en.wikipedia.org/wiki/Liberation_fonts (secondary, read 2026-09-28).
- Repo (VRF): `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, `2026_WGY_Investment_Policy-FINAL.txt`,
  `2026_WGY_Trading_Notes_Analysis-FINAL.txt`, `2026_WGY_Investment_Competition_Guide.txt`,
  `SMApply_Deliverables_Page_2026-09-27.md`.
- Run files: `phase_A/case_register.md` (R-AN14, X-7, X-10, X-23), `phase_A/fact_register.md` (F-003, F-101, F-111,
  F-112, F-117, F-409), `phase_A/stakeholder_map.md` (BS-07, BS-08, BS-11, SH-25), `phase_A/wins_week1_guardrails.md`
  (A4), `wins_now/securities_and_allocation_v0.md`, `wins_now/S4_red_team.md` (finding 13), `phase_B/B1a_case_anomalies.md`,
  `phase_C/survivors.json` (M005, M013), `phase_D/D8_practice.md`, `phase_D/D13a_laura_quotes_verified.md`.
- Scripts: `research/insight_v1/scripts/D10_wins_book_compliance.py`, `research/insight_v1/scripts/D10_ips_page_fit.py`.

## What this teaches
1. **Rules first, then taste.** Check what the rules force before debating what looks best. Here the rules force only
   one thing (say which date WInS shows), and the rest is a real choice the team can make and defend.
2. **Check the premise with arithmetic.** "A 3% growth slice" sounded reasonable; the leftover is really 1.5-2.2%, so
   the stock position would be about 1%. A two-line calculation removed a whole option.
3. **A trigger that can never fire is not a safeguard.** Ask when each rule could actually bite. The funded ratio can
   only fall below 100% before the ladder is bought, so the real test is simply "is the promise fully bought?"
4. **Format is part of the strategy.** Two double-spaced pages hold about 550 words only if the layout is tight. Test
   the PDF early, because a page too many means the strategy is never read.
