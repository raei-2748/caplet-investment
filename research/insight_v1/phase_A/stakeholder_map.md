# A3 Stakeholder map and blind spots

Agent: A3 (Blind-spot Mapper), insight_v1 run, written 2026-09-27. This is AI-generated research (Claude Code) for Team
Caplet, for brainstorming only. It holds **no submission-ready prose**. Where it says what a sentence "must contain",
that is a checklist. The six students write every word. It names **no securities**.

Scope: semifinals only (brief section 4). Finale judges get one line (SH-17) and are then parked.

---

## 0. Summary (read this first)

1. **Twenty-six stakeholders, one test.** Every stakeholder below reaches the deliverables through one of three
   readers: **Laura** (who chooses a firm), the **co-sponsors** (who read the fundraising draft) and the **semifinal
   readers** (who score all three deliverables together). The case turns each of them into a scored requirement:
   - "recommendations that can earn her confidence" (criterion 2, R-S25);
   - "communicates Laura's potential facility contribution and investment uncertainty clearly and credibly to
     prospective co-sponsors" (criterion 5, R-S28);
   - "Evaluators will consider the three deliverables together" (case p.4 L161, R-C91).

   All three are VERIFIED-REPO-FILE.
2. **The rules name a professional ethics code, and no research file uses it (BS-02).** The Rules page tells teams
   to "review the CFA Institute's Asset Manager Code and operate by these standards" (R-W29, VERIFIED-PRIMARY via A1).
   I read the Code itself (VERIFIED-PRIMARY, CFA Institute PDF, 2nd ed., ©2009, 2010). Its provisions line up almost
   one for one with the IPS guide:
   - know the client (B.6.a);
   - act only within the stated mandate (B.5.a);
   - make disclosures that are "truthful, accurate, complete, and understandable" (F.2);
   - disclose fees (F.4.d);
   - keep records (D.4).

   This hands the fictional "firm" a ready-made governance backbone, and it costs almost no words.
3. **Nobody has modelled the firm's own fee (BS-01).** The case has Laura invest "with an asset management firm"
   (p.2 L43), and the Code requires fee disclosure (F.4.d). No file in `research/` mentions a management fee
   (grep, 2026-09-27), and the verified model runs with no fees (brief section 11).

   Rough arithmetic (ASSUMPTION: a yearly fee on all assets, paid from the growth sleeve; ladder +5.1% a year, sleeve
   +5.9% a year): a 0.5% fee cuts the median 2033 surplus by about **$17k** and a 1.0% fee by about **$34k** (roughly
   8% and 16%). The ten payments are unaffected, but only as long as the fee is paid from the sleeve.
4. **Credibility is one of Laura's income assets, not only a fundraising asset (BS-03).** The whole 2028 deposit comes
   from reputation-driven work: "publishing advances, speaking engagements, licensing, and other entrepreneurial
   ventures" (p.2 L44-45, VERIFIED-REPO-FILE). If she misses a range she announced in public, the harm reaches her
   earning power as well as the co-sponsors. This is a second, Laura-specific reason the 2031 floor must be bought,
   not forecast. Existing files discuss credibility only with co-sponsors.
5. **Funders are reluctant to pay running costs, and Laura's promise is exactly that money (BS-17).** Gregory & Howard
   (SSIR, Fall 2009, VERIFIED-PRIMARY) describe funders' "unrealistic expectations about how much it costs to run a
   nonprofit". The case's split fits this: co-sponsors may fund the building, but Laura alone funds ten years of
   operations (R-AN6). For a co-sponsor, "running costs for the first ten years are already set aside" answers the
   question a building funder worries about most. No research file makes this link. It belongs in the Final Report
   fundraising draft.
6. **"Dollar range" is ambiguous to a Taiwanese reader (BS-04).** The case never names a currency (R-AN10), and
   Taiwan's currency is also a "dollar" (the New Taiwan dollar, NT$). Existing work covers exchange-rate *risk*, not
   this *labelling* risk. The fundraising draft should write "US$" every time, and give the NT$ figure as a dated
   reference.
7. **Pledge wording matters to co-sponsors (BS-05).**
   - The case says Laura will "describe how much she *expects* to contribute" and calls it her "potential
     contribution" (p.3 L110, L116; VERIFIED-REPO-FILE).
   - Fundraisers routinely discount pledges. One search snippet says 10-30% are never collected (SNIPPET-UNVERIFIED).
   - Whether a charitable pledge is legally binding varies by U.S. state (California Bar memo, 2010,
     VERIFIED-PRIMARY). That is not the team's question to answer.

   The team's question is which verb goes with which tier: "set aside" for the bought floor, "expects" or "aims" for
   the stretch.
8. **Operators and participants feel the case's two simplifications most:** fixed nominal payments (R-C46) and
   nothing after 2042 (R-C49). Both are known open items (brief section 9). This map adds only who carries the cost:
   the staff's real budget shrinks each year, and by the case's own list the gap falls to "co-sponsors, grants,
   collaborators, program fees, continued business income" (p.3 L85-86).
9. **Rival teams may reach the same architecture (BS-10).** The council's claim that "most strong teams will write
   safe bucket + growth bucket" is untested (ASSUMPTION). Many teams will use AI tools, which readily suggest
   liability matching. Caplet's edge should therefore rest on Laura-specific reasoning and real process evidence, not
   on "lock early" being rare.
10. **One administrative gate has no owner: the school documentation (BS-11).** Its official wording: "Do not wait until
    the last minute to request documentation" (R-S21, VERIFIED-REPO-FILE). The semifinal letterhead confirmation
    (R-W25) has the same problem. Neither appears as an action in any research file.

Entry count: 26 stakeholder entries (SH-01 to SH-26), 20 blind spots (BS-01 to BS-20), 8 cross-stakeholder tensions
(T-1 to T-8) and 14 candidate questions for Phase B (Q-A3-01 to Q-A3-14).

---

## 1. How to read this file

**Status labels** (brief section 3). I abbreviate them inside dense blocks:
- **VRF** = VERIFIED-REPO-FILE
- **VP** = VERIFIED-PRIMARY
- **SNIP** = SNIPPET-UNVERIFIED
- **ASM** = ASSUMPTION (a modelling input or a judgement; "ASM/judgement" marks interpretation)
- **PARA** = PARAPHRASE-UNVERIFIED

**References.**
- R-C / R-I / R-T / R-S / R-W / R-AN / X- are entries in A1's `phase_A/case_register.md`. Each carries its quote,
  its location and its status.
- F-xxx are entries in A2's `phase_A/fact_register.md`.
- W-n are web sources (section 8).
- Case locations are page (p.) and line (L) in `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`.

**Deliverable tags.**
- **TN** = Trading Notes Analysis, Oct 23 (tier 1)
- **IPS** = Investment Policy Statement, Nov 6 (tier 2)
- **FR** = Final Report, Dec 4 (tier 3)
- **ADMIN** = a pass/fail gate that is not scored

**Terms used below.**
- **Co-sponsor**: an organisation or person who funds part of the residency alongside Laura.
- **Lead gift**: the largest early gift in a fundraising campaign.
- **Pledge**: a promise to give in the future.
- **Mark-to-market**: valuing a holding at today's market price, not at what it will pay at maturity.
- **Human capital**: the value of a person's future earnings.
- **Funded ratio**: assets divided by the Treasury price of the promised payments.
- **AUM fee**: a yearly fee charged as a percentage of "assets under management".

---

## 2. Overview table

"Reaches us via": L = Laura, C = co-sponsors, J = semifinal readers, T = the team itself.

| ID | Stakeholder | Reaches us via | Most important thing to them | Deliverable most affected |
|---|---|---|---|---|
| SH-01 | Laura as investor (choosing a firm) | L | The promise is safe, and her risk appetite is used where it cannot hurt it | IPS, FR |
| SH-02 | Laura as founder of the residency | L, C | A facility contribution she can stand behind, with flexibility left | FR |
| SH-03 | Laura as author, educator and public voice | L | Nothing she announces publicly turns out untrue | FR |
| SH-04 | Laura as statistics graduate | L, J | Every probability names its model, and "certainty" is testable | FR, IPS |
| SH-05 | Private and family foundations | C | A floor that is real, and a plan for shortfalls and overruns | FR |
| SH-06 | Public arts bodies (US and Taiwan) | C | Eligibility, local-currency budgets, public accountability | FR |
| SH-07 | Taiwanese partners (host institutions) | C | NT$ figures; their share of cost and risk | FR |
| SH-08 | Corporate sponsors | C | Timing, visibility, reputational safety | FR |
| SH-09 | Individual donors | C | A visible personal commitment (seed-money signal) | FR |
| SH-10 | Wharton/Penn alumni networks | C, J | Rigor they recognise, and an alumna's credibility | FR |
| SH-11 | Residency participants | (C) | The programme exists and continues | FR |
| SH-12 | Future staff and operators | (C) | A predictable operating budget; who covers erosion; 2043 | FR |
| SH-13 | Taiwan host community | (C) | A good neighbour; local benefit | FR (one line at most) |
| SH-14 | Portfolio manager (case fiction) | J | A defensible, rule-based framework the firm can sign | IPS |
| SH-15 | Real teacher advisor (admin only) | T | Rule compliance; documentation; engagement | ADMIN, FR |
| SH-16 | Semifinal readers | J | Five criteria, consistency across deliverables, an authentic voice | TN, IPS, FR |
| SH-17 | Finale judges | (parked) | Out of scope for this run | none |
| SH-18 | Rival teams | J (comparison) | Their median submission sets the bar | all |
| SH-19 | Wharton Global Youth (organiser) | J | Learning, ethics, AI honesty, respect for a real alumna | all |
| SH-20 | The six students | T | Learning, fairness of workload, no repeat of last year's rule break | all |
| SH-21 | Laura's publishers and literary agent | (L) | Source of the 2028 deposit | FR |
| SH-22 | Speaking hosts and licensees | (L) | Also a source of the 2028 deposit | FR |
| SH-23 | Readers of her books, and classrooms | (L) | Her public voice; her books' classroom and library channel | FR (income risk) |
| SH-24 | The team's school | T | Permission, letterhead documentation, reputation | ADMIN |
| SH-25 | The "firm" and its ethics code | J | CFA Asset Manager Code (named in the Rules) | IPS, FR |
| SH-26 | Laura after 2033 (running the residency) | L | Flexibility when her earnings may be lower | FR |

---

## 3. Stakeholder entries

Each entry lists:
- **Interests**: what they care about.
- **Fears**: what they worry about.
- **Needs to see**: what would earn their trust.
- **Loses trust if**: what would lose it.
- **Anchor**: the official requirement that connects them (quote, location and status).
- **Implication**: a decision, number or sentence, tied to a deliverable.

### Laura (four roles)

**SH-01 Laura as investor (the client choosing among firms)**
- **Interests:** she chooses one strategy out of many. The case says "the investment strategy that Laura ultimately
  chooses" (p.1 L9-10, R-C8, VRF). She wants "an appropriate balance between pursuing growth and protecting the
  capital required for her goals" (p.2 L71-74, R-C38, VRF).
- **Fears** (ASM/judgement, drawn from the case wording): a plan so cautious that it ignores "thoughtful risks"
  (p.2 L70, VRF). Or a plan that risks the promise. Or statements that show her balance falling while the payments
  are in fact safe (see BS-09).
- **Needs to see:**
  - Risk taken only with money the promise does not need.
  - One clear principle.
  - Her own goals in her own order: the reserve first, then the facility, then flexibility (p.3 L94-103, R-C50,
    R-C57, VRF).
- **Loses trust if:**
  - The plan is generic, e.g. an unexplained 60/40.
  - It is a return forecast dressed up as certainty.
  - The fees are hidden (BS-01).
- **Anchor:** criterion 2, "presents recommendations that can earn her confidence" (SMApply L51, R-S25, VRF). IPS
  guide: "Always remember who your strategy is designed to serve" (IPS p.1 L27, R-I14, VRF).
- **Implication:**
  - IPS: the central idea must be stated as *her* trade-off, growth versus the capital her goals require, not as a
    finance label.
  - FR: report "payments covered" (the funded ratio) next to the market value (BS-09).
  - Decision still open: the sleeve's equity weight, 50/60/70% (brief section 9).

**SH-02 Laura as founder of the residency**
- **Interests:** a "small, community-oriented space" in Taiwan (p.2 L76-80, R-C40, VRF). She wants the largest
  contribution she can *responsibly* make (p.3 L101-106, R-C57, R-C60, VRF), and she wants to keep flexibility "as
  the project develops" (p.3 L102-103, R-C58, VRF).
- **Public record of building institutions (VP, lauragao.com/hey, read 2026-09-27):** she "co-organizes San
  Francisco's LGBTQ+ comics festival, Pride in Panels". This is cited only as evidence that she has built community
  institutions before. It is never a reason for any investment choice.
- **Fears:**
  - Over-committing in 2033 and having nothing left when costs overrun.
  - A co-sponsor walking away after a missed range (p.3 L114-115, R-C66, VRF).
- **Needs to see:**
  - A contribution rule that leaves a stated buffer.
  - What happens in good and bad markets (p.3 L118-119, R-C70, VRF).
  - What happens if the project is delayed or changes (BS-07).
- **Loses trust if:** the team commits "all remaining assets". The case warns against exactly this: "committing all
  remaining assets could limit her financial flexibility" (p.3 L102-103, VRF).
- **Anchor:** case test 5, "Preserves appropriate financial flexibility when determining the facility contribution"
  (p.4 L145, R-C84, VRF).
- **Implication (FR):**
  - Decide the share of the post-reserve surplus that is *not* contributed, and say why. The council's view is to
    keep it "mainly as project flexibility" (CLAUDE.md interview item 3; ASM).
  - A strong sentence names the buffer's purpose: project overruns and changes, not her living costs, which sit
    outside the portfolio (p.2 L61-63, VRF).

**SH-03 Laura as author, educator and public voice**
- **Interests:** her public credibility. The case says her books "are read in classrooms around the world" (p.1
  L22-23, R-C16, VRF). Her first named work was "a response to misinformation" (p.1 L19-20, R-C14, VRF).
- **Public record (VP, lauragao.com/hey, 2026-09-27):**
  - She lists "Speaking engagements".
  - She is described as shaping "the next generation of creators as a Professor of Comics at California College of
    the Arts".
  - The case lists her as "educator" (p.1 L6, VRF).
  - Teaching income is not one of the case's 2028 sources (brief section 8.19).
- **Fears** (ASM/judgement): a promise she has made in public breaks; the plan contains a claim she could not repeat
  in front of a class.
- **Needs to see:** plain language, honest ranges, and no hype.
- **Loses trust if:**
  - "Guaranteed" or "100%" appears without its qualifiers.
  - Her identity is used as decoration (brief section 4, tokenism rule).
- **Anchor:** criterion 5, "an authentic team voice" and "clearly and credibly" (SMApply L57, R-S28, VRF).
- **Implication:**
  - FR: every uncertainty statement must be one she could say out loud without a footnote.
  - BS-03: her credibility is part of her income.

**SH-04 Laura as statistics graduate**
- **Interests:** a degree in "Statistics & Information Decisions Management" (p.1 L16, R-C12, VRF). Her site has a
  "Visual Data Stories" section (VP, lauragao.com, 2026-09-27).
- **Fears** (ASM/judgement): a "95%" with no model behind it; confusion between the median and the mean; a
  confidence statement that is really one-sided.
- **Needs to see:**
  - "Certainty" defined in a way she can check herself: market-priced full funding, cash flows matched, residual
    risks named (brief section 8.6).
  - Every probability with its model and at most two significant figures.
  - The two-sided "within that range" wording handled properly (p.3 L117-118, R-AN9, VRF).
- **Loses trust if:** false precision; one model presented as the truth; a range whose confidence counts only the
  low end.
- **Anchors:**
  - "define what they consider a high degree of funding certainty, explain how they evaluated that level of
    certainty" (p.3 L97-98, R-C54, R-C55, VRF).
  - Criterion 3, "uses reasonable assumptions and projections" (SMApply L53, R-S26, VRF).
- **Implication:**
  - FR: state the confidence for *both* ends of the 2031 range: P(below floor) and P(above top).
  - IPS: one plain sentence defining certainty, with no numbers needed (R-I31).

### Prospective co-sponsors (kept generic; the case names none)

Common anchors for all co-sponsor entries, all VRF:
- "A meaningful personal contribution may signal that the residency is financially viable, demonstrate Laura's
  commitment to the project, and make potential co-sponsors more willing to contribute" (p.3 L110-112, R-C64).
- "If Laura promises more than she can ultimately contribute, she could damage her credibility and lose the
  confidence or participation of co-sponsors" (p.3 L114-115, R-C66).
- "Each team must also draft part of Laura's fundraising materials" (p.4 L123-124, R-C72).

**SH-05 Private and family foundations**
- **Interests:** due diligence. One foundation-practice bulletin (PKF O'Connor Davies, July 2019, VP, W-6) says a
  funder should check "whether the sources of potential revenue are reliable", and should "have a clear understanding
  of how the grantee would respond to any unexpected revenue shortfalls or cost overruns".
- **Fears:**
  - A founder's pledge that later shrinks.
  - Being asked for running costs indefinitely. Funders' "unrealistic expectations about how much it costs to run a
    nonprofit" are the first step of the "starvation cycle" (Gregory & Howard, SSIR, Fall 2009, VP, W-3).
- **Needs to see:**
  - A floor already set aside, not a forecast.
  - An explicit answer to "what if markets are bad", which is also a case requirement (R-C70).
  - What happens to her contribution if building costs overrun. Brief section 9 lists a "scope clause" as open.
- **Loses trust if:** the range is so wide that it is useless, or so narrow that it is risky (R-AN9); or the
  "certainty" turns out to cover only nominal USD and nobody said so.
- **Implication (FR fundraising draft):** a strong passage contains:
  1. what is already set aside (the floor) and in what form;
  2. the stretch figure with its stated probability and model;
  3. that ten years of operating payments are funded separately, from her portfolio alone (R-C48);
  4. what she will do if outcomes are unfavourable (a smaller contribution, never a raid on the operating reserve).

**SH-06 Public arts bodies (U.S. arts councils; Taiwan's national and local culture agencies)**
- **Interests:** public accountability, eligibility rules, local-currency budgets.
- **Evidence:**
  - Taiwan's Ministry of Culture funds artist villages and international residency exchange, and runs an "Arts
    Residency Network Taiwan" platform (SNIP, W-12; the site `artres.moc.gov.tw` returned HTTP 403 to curl on
    2026-09-27).
  - Most U.S. state arts councils have grants for individual artists (Artist Communities Alliance page, VP, W-4).
- **Fears** (ASM/judgement): figures in a foreign currency; a private founder's commitment that depends on markets.
- **Needs to see:** figures in their own currency with a date and an exchange rate; a clear statement of which costs
  Laura's money covers.
- **Loses trust if:** "dollar" is left ambiguous (BS-04).
- **Anchor:** "Any remaining facility cost, and any operating support beyond Laura's commitment, may come from
  co-sponsors, grants, collaborators, program fees, continued business income, or other sources" (p.3 L85-86, R-C44,
  VRF).
- **Implication (FR):** quote US$ as the binding figure, with an NT$ reference at a stated date and rate. A2 has the
  numbers: USD/TWD 31.82 on 2026-09-18 and 10-year volatility 4.69% (F-510, F-512, VP).

**SH-07 Taiwanese partners (host institutions, universities, cultural organisations)**
- **Interests:** local costs are paid in NT$, and construction costs are rising much faster than consumer prices.
  Taiwan's construction cost index was +6.53% y/y in August 2026 against CPI of +2.04% (F-508, F-501, VP).
- **Fears** (ASM/judgement): absorbing currency and building-cost risk that the founder's USD promise passes on to
  them.
- **Needs to see:**
  - The contribution in NT$ under strong-TWD and weak-TWD cases.
  - Who carries cost overruns.
  - That a USD promise is "certain in nominal USD", not in NT$.
- **Loses trust if:** the materials call a USD figure "certain" without that qualifier.
- **Anchor:** "the effect of inflation on portfolio projections and facility costs" (p.4 L146-147, R-C85, R-AN8, VRF).
- **Implication (FR):** a sentence on cost inflation must use a building-cost assumption, not CPI (brief section
  8.15). F-508 warns that the 6.5% figure is a 2026 jump; the 2021-2026 average is about 3.5% a year (VP).

**SH-08 Corporate sponsors**
- **Interests:** brand visibility, fit with their budget calendar, reputational safety.
- **Fears** (ASM/judgement): public association with a project that stalls.
- **Needs to see:** a firm commitment date (2033) and a founder commitment that is not contingent on markets.
- **Loses trust if:** the figures keep moving between 2031 and 2033 with no explanation.
- **Anchor:** R-C66 (credibility).
- **Implication (FR):** low priority. The floor-plus-stretch structure already serves them. No extra content is
  needed. Say so to keep complexity down.

**SH-09 Individual donors (including readers and community supporters)**
- **Interests:** a visible personal commitment. In List & Lucking-Reiley (2002), higher announced seed money raised
  small-donor giving. The brief treats this as a mechanism, not a prediction for institutions (brief section 8.17;
  council citation, SNIP-level for the details).
- **Fears:** giving to a project that never opens.
- **Needs to see:** a simple statement of what Laura herself puts in and when.
- **Loses trust if:** the numbers are too technical to repeat.
- **Implication (FR):** the fundraising draft should work for a non-specialist in one reading (criterion 5). Put
  technical detail in an appendix.

**SH-10 Wharton/Penn alumni networks (as potential co-sponsors or connectors)**
- **Interests:** Laura is a 2018 Wharton graduate (p.1 L16, VRF). Alumni readers will recognise, and test, finance
  rigour.
- **Fears** (ASM/judgement): a sloppy method attached to a Wharton name.
- **Needs to see:** a method they would accept: market pricing of the promise, stated models, sensitivity to rates.
- **Loses trust if:** they find the jargon without the substance.
- **Implication:** the same as SH-04. No separate content. (Recorded so that Phase F does not flag it as missed.)

### The residency's people and place

**SH-11 Residency participants (artists, writers, designers, entrepreneurs, educators)**
- **Interests:** the case lists them and says they will "temporarily live, work, teach, and collaborate" (p.2
  L78-80, R-C40, VRF).
  - The Artist Communities Alliance (VP, W-4) says: "Most artists ask: 'Where can I go that's free?' The short
    answer is, nothing is free." It also says residencies often subsidise fees through work-exchange, "teaching a
    workshop" among the examples.
  - Program fees are one of the case's permitted outside sources (p.3 L86, VRF).
- **Fears** (ASM/judgement): a programme that shrinks or closes mid-way; fees that rise because the operating budget
  erodes.
- **Needs to see:** that the programme's base funding does not depend on annual fundraising for its first ten
  years.
- **Anchor:** "reliable support for its early operations" (p.3 L83, R-C41, VRF).
- **Implication (FR):** participants never read our deliverables. Their interest reaches us through co-sponsors
  (SH-05). One clause in the fundraising draft ("operations funded for ten years, independent of co-sponsors") serves
  them. Do not write a programme or business plan; the case says so explicitly (p.4 L164-166, R-C95, VRF).

**SH-12 Future staff and operators, who depend on the $50k a year**
- **Interests:** a predictable budget. The ten payments are fixed at $50,000 and arrive "at the beginning of each
  year" (p.3 L88-90, R-C45, R-C46, VRF). A lump sum on 1 January is good for cash planning.
  - An arts-funding commentator (Emil J Kang, Substack, 13 July 2026, VP, opinion piece, W-5): "None of this runs
    for free. A residency covers room and board, studio space, the staff who hold it together".
  - One funder at a 2007 Grantmakers in the Arts roundtable (VP, W-7): "When we look at proposals for staff support,
    we ask organizations if they have sustainable payroll and benefit packages, governed by the board." This is one
    speaker, and old.
- **Fears:**
  - **Real erosion.** At an assumed 2% a year, the fixed $50k is worth about $43.5k in 2026 money by 2033 and about
    $36.4k by 2042 (council arithmetic; ASM inflation rate). Taiwan wages in construction rose +8.12% y/y (F-508,
    VP), although that is not a residency wage index.
  - **Currency.** Payments in USD, wages in NT$.
  - **The 2043 cliff.** Nothing is funded after 2042 (p.3 L92-93, R-C49, VRF).
- **Needs to see:** that someone has named who covers the erosion and what happens in 2043.
- **Loses trust if:** the plan calls the operating budget "secure" without saying "in nominal USD".
- **Anchor:** "each payment is a fixed $50,000 and is not adjusted for inflation" (p.3 L90, R-C46, VRF). The
  "operating support beyond Laura's commitment" may come from other sources (p.3 L85-86, VRF).
- **Implication (FR):** one sentence that must contain:
  1. the payments are fixed in nominal USD, as the case specifies;
  2. their real value falls at an assumed rate;
  3. by the case's own terms the top-up belongs to co-sponsors, program fees and other sources;
  4. funding after 2042 is outside the plan (R-C49).

  This is a known unanswered item (brief section 9, "real erosion... must be said aloud"). This map adds the
  operators as the people who bear it.

**SH-13 Taiwan host community (neighbours, local creative scene, local government)**
- **Interests** (ASM/judgement): local benefit, access to programmes, good-neighbour behaviour. The case calls the
  space "community-oriented" (p.2 L77, VRF). An Artist Communities Alliance research project on residencies as "a
  platform for engaging communities" is SNIP only; ACA says its reports are members-only (W-4 search result).
- **Fears / needs:** out of scope for an investment strategy. Taiwan's legal and regulatory requirements are
  explicitly excluded (p.4 L168-169, R-C97, VRF).
- **Implication:** none for TN or IPS. At most one clause in FR, if it helps the fundraising draft. Listed so that
  its omission is a deliberate choice (design principle: complexity must earn its place).

### Competition stakeholders

**SH-14 The portfolio manager (case fiction: "your team's teacher/advisor who makes the final investment decisions")**
- **Interests:** the case sets up a firm with analysts and a PM who signs off (p.1 L3-5, R-C2, R-C3, VRF). A PM wants
  a policy that any member of the firm could apply the same way, and that the firm can defend.
- **Fears** (ASM/judgement): analysts proposing trades that break the mandate; recommendations with no stated
  basis.
- **Needs to see:** a written decision framework with rules: the lock rule, the rule if rates fall, the 2031 floor
  rule and the rebalancing bands.
- **Anchor:**
  - "This formally establishes the strategy and the team's decision-making framework" (p.4 L155-156, R-C89, VRF).
  - Asset Manager Code B.5.a, "Take only investment actions that are consistent with the stated objectives and
    constraints" (VP, W-1).
- **Implication (IPS):** write the framework as pre-set rules, which also reads well to judges. Do *not* write that
  "our PM decided". The real rules forbid advisor decisions (SH-15, R-AN4).

**SH-15 The real teacher advisor (administrative role only)**
- **Interests:** the role is "to provide guidance, encouragement, and educational support". Advisors "may not make
  decisions on behalf of students or actively participate in team activities, trading decisions, or strategy
  development" (Rules page, R-W19, VP via A1). "Students should place trades on WInS, NOT the advisor" (R-W87, VP).
  The advisor also monitors "team engagement and portfolio activity" (R-W20).
- **Fears** (ASM/judgement): a rule breach that disqualifies the team; missing school documentation.
- **Needs to see:** the team making and logging its own decisions, and the paperwork done early (SH-24).
- **Implication:**
  - FR, Articulation: one true sentence on the advisor's administrative role (CLAUDE.md "Team"; R-W28 bans invented
    teamwork stories).
  - ADMIN: the advisor is the natural route to the school letterhead (BS-11).

**SH-16 Semifinal readers (who pick the Top 50 from the written deliverables)**
- **Interests:** the five criteria (SMApply L49-57, R-S24 to R-S28, VRF). They check consistency: "maintaining a clear
  and consistent investment strategy across all three" (p.4 L161-162, R-C92, VRF). They check the trade record: "Yes,
  we will verify this" (TN p.2 L53, R-T34, VRF). Returns do not count: "your team's standings on WInS have little to
  do with the final outcome" (R-W42, VP).
- **Fears** (ASM/judgement):
  - AI-written text. "AI-generated work may not be submitted as your own" (R-W26, VP).
  - Jargon.
  - Mismatches between the notes, the IPS and the WInS portfolio.
  - Format breaches in the IPS, which are disqualifying (IPS p.3 L82-83, R-I39, VRF).
- **Needs to see:**
  - Laura-specific tailoring.
  - Reasoning over results: "The focus should be on the quality of your reasoning and the intended role of each
    decision" (TN p.1 L15-16, R-T11, VRF).
  - An authentic voice.
  - One strategy told the same way three times.
- **Loses trust if:**
  - A trading note's wording differs from WInS.
  - A reflection justifies a trade by its gain.
  - The IPS mirror (~65/35) contradicts the plan's ~17-24% total equity (F-409, derived).
- **Implication:**
  - TN: each reflection names which of Laura's needs the trade serves.
  - IPS: at most one rounded number.
  - FR: sources and a record of AI use in a Works Cited list (R-W46, VP).

**SH-17 Finale judges.** Out of scope for this run (brief section 4: semifinals only). No finale content is produced.
The only carry-over: nothing in the written deliverables should be impossible to defend aloud (R-W7, "communicate and
defend", VP). Parked.

**SH-18 Rival teams**
- **Scale:**
  - 2025-26 had "more than 6,300 registered teams". "Some 2,300 teams from 79 countries submitted final reports"
    (R-W97, R-W99, VP).
  - The realistic field is teams that finish, about 2,300 last year (R-AN60).
- **What they will likely submit** (ASM/judgement): "safe bucket + growth bucket" with a Monte Carlo "95%" (council
  judge panel view; untested). With AI tools common, a liability-matched Treasury ladder may also be common (BS-10).
- **What they fear:** the same things we do. Their median quality sets the bar.
- **Implication (all deliverables):** distinctiveness should come from:
  1. reasons specific to Laura (lumpy reputation-driven income, BS-03; the statistics degree, SH-04; the co-sponsor
     audience, SH-05 to SH-07);
  2. true process evidence (decision log, the trades that tested the plan);
  3. clarity.

  It should not come from the architecture alone. The ethics rule bans plagiarising "existing strategies" (R-W28,
  VP).

**SH-19 Wharton Global Youth (the organiser) and what it is teaching**
- **Interests (VP, main competition page, read with curl 2026-09-27):**
  - Students "learn about strategy-building, teamwork, communication, risk, diversification, company and industry
    analysis, and many other aspects of investing."
  - The page promises "finance skills that will last a lifetime".
  - "Unlike other investment competitions, success is not determined by portfolio performance."
  - The FAQ says the "ultimate goal with this game... is learning the nuances of investing" (R-W37, VP), and the
    WInS page says "demonstrate what your team has learned" (R-W83, VP).
  - It points teams to a professional code (R-W29, VP; see SH-25).
  - It protects a real alumna: "While the client is real, the financial scenario is developed specifically for the
    competition" (R-W4, VP), and contacting her is forbidden (R-W16, R-W55, VP).
- **What this year's case seems designed to teach** (ASM/judgement; A1's R-AN entries give the evidence):
  1. separate a fixed promise from an uncertain surplus;
  2. turn a vague wish ("high degree of certainty") into a testable definition;
  3. communicate uncertainty honestly to people who are not investors.
- **Fears** (ASM/judgement): AI plagiarism, privacy breaches involving a real alumna, rule breaches.
- **Implication (FR, Articulation):** show what the team learned (e.g. why "lock early" beat "growth first", brief
  section 8.1). Credit AI use. Respect the privacy rule.

**SH-20 The six students (learning goals)**
- **Interests:**
  - Ray's stated goal is to learn markets and client analysis (CLAUDE.md, VRF).
  - The team's goal is the Top 50.
  - All members must contribute: "All team members must play a contributing role" (R-W38, VP).
  - Last year's lessons: over-complex packaging, and a trade outside the rules (v4 Part 2, VRF).
- **Fears:** repeating last year's rule break; an AI-written feel; uneven workload. Roles are still unassigned
  (CLAUDE.md open item).
- **Needs:** a strategy each of the six can explain in plain words; a decision log kept at trade time (R-W82, VP).
- **Implication:**
  - TN (tier 1): assign a trader and a note-writer before the next trade.
  - FR: the Articulation evidence must be real. Ethics bans invented "teamwork and experiential stories" (R-W28, VP).

### Stakeholders the prompt missed

**SH-21 Laura's publishers and literary agent (source of much of the 2028 deposit)**
- **Evidence:**
  - Her site links a Publishers Weekly item titled "My book deal with HarperCollins" (VP, lauragao.com/hey,
    2026-09-27). It also says she is represented by a literary agency (VP; named on the page, not needed here).
  - How advances are paid (Authors Guild, 20 July 2021, VP, W-8): "paying them out in three, and even up to six,
    installments". "Royalties are not paid to the author until the publisher has fully recouped the full amount of
    the advance." "The sales numbers of one book can affect the ability to sell the next project."
- **Interests** (ASM/judgement): the author's next books, delivered on schedule. A residency project competes for
  her time.
- **Why this matters:** the case says she "will contribute an additional $150,000 at the beginning of 2028, using
  earnings from publishing advances…" (p.2 L43-45, R-C27, R-AN35, VRF). Instalment timing makes *late* as plausible
  as *smaller* (BS-13).
- **Implication (FR):** stress tests should label a "late 2028 deposit" case as well as a "smaller" one. Under the
  lock-early rule, lateness only delays the growth sleeve. The team's own scenario must be labelled as beyond the
  case (R-AN35).

**SH-22 Speaking hosts, schools that book visits, and licensees**
- **Interests:** the case lists "speaking engagements, licensing" as deposit sources (p.2 L44-45, VRF). School and
  library budgets and event demand drive them (ASM/judgement).
- **Implication (FR):** these sit in the same "human capital" bucket as SH-21. They matter only through the 2028
  deposit and the wrong-way-risk question (brief section 9). No separate content.

**SH-23 Readers of her books, and the classroom and library channel**
- **Evidence:**
  - The case: "her books are read in classrooms around the world" (p.1 L22, VRF).
  - ALA (release April 2026, VP, W-9): "ALA's Office for Intellectual Freedom (OIF) tracked 4,235 unique titles
    challenged in 2025, the second highest ever documented by ALA." Also: "Of the unique titles challenged in 2025,
    1,671 (40%) represent the lived experiences of LGBTQIA+ people and people of color."
  - **I have not verified whether any of Laura's titles were challenged. Do not claim they were.**
- **Why it matters:** the school and library channel for books on identity themes faces a documented challenge
  climate. That is a sector risk to the publishing income behind the 2028 deposit. It is **not** a reason to pick or
  avoid any investment (tokenism rule).
- **Implication (FR):** at most one clause in the human-capital discussion, framed as a risk to an income channel.
  Owner: B3/D6.

**SH-24 The team's school**
- **Interests:** its name is on the submission. It must provide "official documentation from your school" (SMApply
  L45, R-S20, VRF). Semifinalists must also supply letterhead confirming "The team has permission to participate"
  and that all students and the advisor "are affiliated with the school" (R-W25, VP).
- **Fears:** a last-minute request; an administrative miss.
- **Implication (ADMIN):** request the documentation in October ("Do not wait until the last minute", R-S21, VRF).
  "Sample Documentation: Coming soon" (R-S23, VRF), so check SMApply again for the sample. See BS-11.

**SH-25 The "firm" (case fiction) and its ethics code**
- **Evidence (Asset Manager Code, CFA Institute, 2nd ed., ©2009, 2010; PDF downloaded and read 2026-09-27, VP,
  W-1):**
  - Principle 5: "Communicate with clients in a timely and accurate manner."
  - B.4: "Have a reasonable and adequate basis for investment decisions."
  - B.6.a: "Evaluate and understand the client's investment objectives, tolerance for risk, time horizon, liquidity
    needs, financial constraints, any unique circumstances…"
  - D.4: "Maintain records for an appropriate period of time in an easily accessible format."
  - E.1: "Managers must not misrepresent the performance of individual portfolios or of their firm."
  - F.2: "Ensure that disclosures are truthful, accurate, complete, and understandable and are presented in a format
    that communicates the information effectively."
  - F.4.d: "Management fees and other investment costs charged to investors…"
- **Anchor:** the Rules page, "All teams should review the CFA Institute's Asset Manager Code and operate by these
  standards" (R-W29, VP via A1).
- **Implication:** see BS-01 and BS-02.

**SH-26 Laura after 2033, while she runs the residency**
- **Interests** (ASM/judgement): once she runs a residency, her own earnings may change. The case lists "continued
  business income" among possible *outside* sources for the project (p.3 L86, R-AN24, VRF), and says nothing about
  her earnings after 2033.
- **Why it matters:** this is a Laura-specific reason for the flexibility the case asks for (R-C58, R-C84), besides
  building-cost overruns. It is an interpretation, not a case fact.
- **Implication (FR):** a flexibility sentence may give two purposes: project overruns and changes, and the
  founder's own reduced capacity to top up. Living costs stay outside the portfolio (p.2 L61-63, VRF). Owner: B3/D6.

---

## 4. Cross-stakeholder tensions (where pleasing one reader can cost another)

| ID | Tension | Anchors (VRF unless marked) | How the current strategy resolves it | What is still open |
|---|---|---|---|---|
| T-1 | Laura's "thoughtful risks" (SH-01) vs co-sponsors' need for a floor (SH-05) | p.2 L70; p.3 L114-115 | Risk is taken only in the surplus sleeve; the floor is bought in 2031 (brief section 7) | Sleeve equity weight; the share of the sleeve locked as the floor (brief section 9) |
| T-2 | The statistician's wish for method (SH-04) vs the IPS ban on calculations and charts (SH-16) | R-C55; IPS p.2 L51-52 and p.3 L123 | Principle in the IPS, method in the FR | Which single number, if any, goes in the IPS |
| T-3 | Operators' real budget (SH-12) vs fixed nominal payments (case) | R-C46; R-C44 | Treasuries match the nominal promise (brief section 8.10) | The sentence on who bears erosion (brief section 9) |
| T-4 | Taiwanese partners' NT$ (SH-07) vs a USD promise | R-AN10; R-C85 | Disclose; quote in two currencies (brief section 8.15) | Whether to convert part of the 2031 floor to NT$ (brief section 9) |
| T-5 | Founder's wish for a big gift (SH-02) vs flexibility (SH-26) | R-C57; R-C58 | Leftover money kept mainly as flexibility (CLAUDE.md) | How much to hold back, as a rule or a share |
| T-6 | The organiser's learning and AI honesty (SH-19) vs the team's wish to win (SH-20) | R-W26; R-W49 | AI output is research only; students write | Works Cited AI record (R-W46) not yet drafted |
| T-7 | Being distinctive against rivals (SH-18) vs the simplicity principle | R-S24 "creative"; v4 Part 2 | Distinctiveness through client insight, not complexity | BS-10 |
| T-8 | The fictional PM decides (SH-14) vs the real rules, where students decide (SH-15) | R-C3; R-W19 | Write the IPS as the team's rules; the advisor is admin only | Wording in the Articulation section |

---

## 5. Blind spots: considerations that no current document in `research/` addresses

**Method.**
- On 2026-09-27 I searched every `.md` file under `research/` (excluding `_context/` and the case register's own
  quotes) for each topic's key words with grep. Examples: "management fee|advisory fee", "Asset Manager Code|CFA
  Institute", "enforceab|legally binding", "alumni", "staff|salar|payroll", "key person|successor",
  "custod|counterparty", "host community", "grant cycle|lead time".
- "Not addressed" means no strategy or research file treats the point. A topic that appears only as an unanswered
  seed question or an A1 anomaly entry counts as *not addressed*, and is marked "(seed only)".

Each blind spot gives: what it is; why it matters (status); the implication and deliverable; and the phase or agent
best placed to answer it.

**BS-01 The firm's own fee and fund costs are missing from every projection.**
- The case says Laura will invest "with an asset management firm" (p.2 L43, VRF). The Code requires disclosure of
  "Management fees and other investment costs" (F.4.d, VP). The verified model has "no fees" (brief section 11).
- Rough effect, from my arithmetic:
  - Inputs (ASM): the fee is charged yearly on all assets and paid from the sleeve. The ladder grows at 5.1% a year
    from $292,264. The sleeve starts at $7,736, adds $150k in 2028 and grows at 5.9% a year.
  - With no fee, the 2033 surplus is ~$211k. At 0.25%, 0.5% and 1.0% it is ~$202k, ~$193k and ~$177k.
  - A fee therefore lowers the facility contribution, not the payments, because the ladder is untouched.
- **Implication:** FR projections must state a fee assumption (zero, fund expenses only, or an explicit rate) and
  its effect on the 2031 range. IPS: "low-cost" as a principle is consistent with Laura's likely preference
  (team review, ASM). Owner: D3 (model fees properly) and D8 (what fee is realistic for a portfolio this size;
  needs a source).

**BS-02 The CFA Asset Manager Code is named in the rules but used nowhere.**
- R-W29 (VP) tells teams to "operate by these standards". The Code's text (VP, W-1) maps onto the deliverables:
  - B.6.a "Evaluate and understand the client's investment objectives, tolerance for risk, time horizon, liquidity
    needs…" matches the IPS guide's list (IPS p.1 L9-10, VRF).
  - B.5.a "consistent with the stated objectives and constraints" matches the IPS freeze ("may not revise its
    investment strategy", R-I35).
  - F.2 matches criterion 5's clarity.
  - E.1 (do not misrepresent performance) matches the TN focus on reasoning over gains.
  - D.4 (records) matches the decision log.
- **Implication:** IPS, one clause: the framework follows a professional code's duties (know the client, act within
  the mandate, disclose plainly). FR: cite the Code in the Articulation or governance part. Do not over-quote it.
  This is a low-complexity credibility gain. Owner: D10 (compliance) and D8.

**BS-03 Credibility is part of Laura's human capital.**
- Her 2028 income sources are reputation-driven (p.2 L44-45, VRF). A missed public range damages co-sponsor
  confidence (R-C66, VRF) and, by inference, future advances, speaking and licensing (ASM/judgement). Existing files
  treat credibility only as a fundraising issue.
- **Implication:** FR, a second, Laura-specific reason the 2031 floor must be bought: breaking a public promise costs
  her twice. Also strengthens the wrong-way-risk discussion (brief section 9). Owner: B3/D6.

**BS-04 "Dollar range" is ambiguous in Taiwan.**
- The case uses "$" and "dollar range" and never names a currency (R-AN10, VRF). NT$ is the "New Taiwan dollar"
  (general knowledge; ASM that readers could confuse the two). Existing files cover exchange-rate *risk* (brief
  section 8.15, F-510), not the ambiguity of the label.
- **Implication:** FR fundraising draft: "US$" on every figure; the NT$ reference with a date and rate; one line
  saying which currency is binding. Owner: D5/D9.

**BS-05 The words of the promise: "expects" versus "pledges".**
- The case: "describe how much she expects to contribute" and "her potential contribution" (p.3 L110, L116, VRF).
- Fundraisers discount pledges. The "10-30% never collected" figure comes from vendor blogs (SNIP, W-11; primary
  pages refused with HTTP 403).
- Enforceability of charitable pledges differs by jurisdiction. Restatement (Second) of Contracts §90(2) makes
  charitable subscriptions binding without consideration in some places, while "charitable pledges are not
  enforceable in California unless the pledgor receives consideration" (California Bar Business Law Section memo,
  2010, VP, W-10; law may have changed since; legal questions are not the team's to settle).
- **Implication:** FR draft: pick the verbs deliberately. The bought floor can be stated as set aside. The stretch is
  an expectation with a probability. No legal claims. Owner: D5/D9.

**BS-06 Co-sponsors will read Laura's figure as a share of a total that nobody has estimated.**
- Fundraising norms put a lead gift at roughly 15-30% of a campaign goal, and expect leaders to give first (SNIP,
  W-13; AFP and NonProfit PRO pages refused or redirected).
- But "Teams are not expected to estimate that cost… or determine the project's total funding gap" (p.4 L164-166,
  R-C95, VRF).
- **Implication:** FR: state that the contribution is sized from her portfolio, not as a share of a budget. Do not
  compute a campaign goal (that would breach the scope and add complexity). Owner: D5.

**BS-07 What the plan does if the residency is delayed, moved or cancelled.**
- The case gives no instruction (R-AN34, VRF). Seed question 24 asks about Taiwan Strait risk (seed only). No file
  answers it.
- Relevant fact: Treasury holdings can be sold at market price. The ladder's value moves about $289 per 0.01% of
  rates (F-101 area, brief section 6), so a change of plan is possible at a market price, with no penalty beyond
  that.
- **Implication:** FR flexibility section, one sentence: the reserve sits in highly liquid government bonds, so a
  change of plan costs only the market move. Do not add scenarios beyond one line (scope). Owner: D1/D4.

**BS-08 Governance continuity: can anyone apply the rules?**
- The case fixes dates (2031, 2033). Nobody has specified who carries out the 2031 floor purchase and the 2033
  designation, or with what records.
- Code D.4 (records) and D.3 ("accurate and complete" client information, with independent third-party review)
  apply (VP).
- **Implication:** IPS: write each rule so that any PM could apply it (trigger, action, record). This is also
  SH-14's need. Keep it generic. No personal speculation about Laura (privacy rule). Owner: D8.

**BS-09 What Laura sees on her statements between 2027 and 2032.**
- The locked ladder is marked to market. With a duration of 9.90 years (brief section 6), a +100bp rise lowers its
  value by roughly 9-10% even though every payment is still covered. At 2027-01-01 that is $292,264 falling to
  $264,890 (brief section 6, VRF script output). The council noted that this is "hard to explain
  to co-sponsors" (council `03_proposals_and_crossexam.md` L259). No file sets a reporting rule.
- **Implication:**
  - FR: set a reporting metric ("payments covered: yes/no; funded ratio"), with the market value shown second.
  - TN: if a WInS Treasury fund falls, the reflection explains why that does not matter for a held-to-maturity
    promise, and notes that WInS funds are a duration proxy, not a held ladder (brief section 8.13).

  Owner: D6.

**BS-10 Rivals using the same AI tools may reach the same architecture.**
- The distinctiveness claims in the council files are untested (ASM). No file considers that liability-driven
  investing (LDI) may be a common AI-suggested answer this season.
- **Implication (all deliverables):** measure distinctiveness by Laura-specific reasoning (BS-03, SH-04, SH-05 to
  SH-07) and by genuine process evidence. Owner: B7/E4.

**BS-11 School documentation and the semifinal letterhead have no owner or date.**
- Requirements: R-S20, R-S21, R-S23 (VRF) and R-W25 (VP). CLAUDE.md lists the Dec 4 due date only.
- **Implication (ADMIN):** assign an owner (with the advisor) and request the documentation in October. Owner: the
  team and D10.

**BS-12 Taiwanese co-sponsors may need materials in their own language and currency.** (Seed only: judge-panel
translation remarks concern jargon, not language.)
- No file asks whether the fundraising draft's audience includes Mandarin-reading institutions.
- **Implication:** FR: at most, note that figures are given in US$ with an NT$ reference. Translation is out of scope
  and should not be attempted (complexity). Owner: D5.

**BS-13 The 2028 deposit can be late, not only smaller.**
- Advances are paid in instalments tied to milestones (Authors Guild, VP, W-8). The case fixes "beginning of 2028"
  (R-C27, VRF). Existing stress tests vary the size (brief section 6), not the timing.
- **Implication:** FR: one scenario label, "late (mid-2028)", alongside "smaller" and "missing". Its effect under
  lock-early is small: sleeve growth only. Owner: D3.

**BS-14 The classroom and library channel risk to publishing income** (SH-23).
- The ALA 2025 data are VP (W-9). The team's own documents raised book challenges as a risk (unverified), but no
  research file quantifies them.
- **Implication:** FR: one clause in the human-capital discussion; no investment consequence (tokenism rule).
  Owner: B3.

**BS-15 Which co-sponsor types exist in Taiwan.**
- Evidence is SNIP only: the Ministry of Culture funds artist villages and residency exchange (W-12, site refused
  curl with HTTP 403).
- **Implication:** FR: keep the co-sponsor audience generic ("foundations, public cultural agencies, local
  partners"). Name no organisation. Owner: D5 (only if it earns its place).

**BS-16 Funders ask how a grantee responds to shortfalls and overruns** (PKF 2019, VP, W-6).
- This matches the case's "favorable and unfavorable" requirement (R-C70) and the open "scope clause" (brief section
  9).
- Partly known; what is new is the external evidence that this is a standard funder question.
- **Implication:** FR: the fundraising draft must answer "what if costs overrun" in one line: her contribution does
  not rise beyond the stated range; the scope adjusts. Owner: D5.

**BS-17 Operating money is the money funders least like to give** (SSIR 2009, VP, W-3; Kang 2026, VP opinion, W-5:
"Funders can give unrestricted operating money to the residencies carrying the earliest risk").
- This explains the case's split (R-AN6) and turns Laura's ten-year operating commitment into a fundraising asset.
- **Implication:** FR fundraising draft must contain the fact that the first ten years of operating payments are
  funded from her portfolio alone, so co-sponsor money can go to the building. IPS: supports "promise first" as the
  central idea. Owner: D5.

**BS-18 Operational risk in "certain barring U.S. default" is unspecified.**
- The certainty definition names "operational error" as residual (council chair memo section 4). No file says which
  operational steps could fail (buying wrong maturities, missed reinvestment, custody) or how they are controlled.
- **Implication:** FR: one line naming the control (records and independent checks, per Code D.3 and D.4). This
  makes the certainty definition complete for a statistician (SH-04). Owner: D1/D10.

**BS-19 Laura's capacity to top up after 2033** (SH-26). Not addressed. Interpretation only.
- **Implication:** FR flexibility rationale. Owner: B3/D6.

**BS-20 The organiser protects a real alumna.**
- The case scenario is fiction, but the person is real (R-W4, R-AN56). No file sets a rule for how the team *writes
  about* her identity and life in the FR. The privacy rule exists for research (brief section 4) but not as a
  writing checklist.
- **Implication:** FR: add a pre-submission check. Public professional record only; no speculation about her real
  finances; identity themes cited only as her public work and never as an investment reason. Owner: D10/D9.

**Known open items this map touches but does not re-open** (brief section 9): real erosion of the $50k (SH-12); the
joint tail of falling rates and a missing 2028 deposit (SH-21); wrong-way risk (SH-21, SH-22); the currency of the
2031 floor (SH-07); the scope clause (BS-16); post-2033 flexibility size (SH-02, SH-26).

---

## 6. Candidate questions for Phase B (each anchored; A3 does not answer them)

| ID | Question | Anchor | Would change |
|---|---|---|---|
| Q-A3-01 | What fee assumption should projections carry, and how much does it move the 2031 range? | Code F.4.d (VP); p.2 L43 | FR numbers |
| Q-A3-02 | Which provisions of the Asset Manager Code does our IPS framework already meet, and which one clause would show it? | R-W29 | IPS sentence |
| Q-A3-03 | Does a missed public range hurt Laura's income, and should that be part of the reason the floor is bought? | p.2 L44-45; R-C66 | FR sentence |
| Q-A3-04 | How should the fundraising draft label currency so that no reader confuses US$ and NT$? | R-AN10; p.3 L117 | FR draft |
| Q-A3-05 | Which verb goes with the bought floor and which with the stretch? | p.3 L110, L116 | FR draft |
| Q-A3-06 | How do we stop co-sponsors reading the contribution as a share of an unestimated total? | R-C95 | FR draft |
| Q-A3-07 | What does the plan do if the residency is delayed by one to two years? | R-AN34 | FR flexibility sentence |
| Q-A3-08 | What metric do we report to Laura each year so that bond price falls do not look like broken promises? | R-S25; R-C38 | FR; TN reflection |
| Q-A3-09 | Is lock-early actually rare among AI-assisted rivals, and if not, what is our real edge? | R-S24 "creative"; R-W28 | all |
| Q-A3-10 | Who requests the school documentation and letterhead, and by when? | R-S21; R-W25 | ADMIN |
| Q-A3-11 | Should stress tests include a late 2028 deposit as well as a smaller one? | R-C27; R-AN35 | FR scenarios |
| Q-A3-12 | What single line answers a funder's "what if costs overrun"? | R-C70; PKF (VP) | FR draft |
| Q-A3-13 | Does "operations funded for ten years" belong at the top of the fundraising draft? | R-AN6; R-C64 | FR draft |
| Q-A3-14 | Which operational controls complete the certainty definition? | R-C54 to R-C56 | FR |

---

## 7. Implications ranked by deadline

- **Tier 1 (TN, Oct 23; WInS now):**
  - Assign a trader and a note-writer (SH-20).
  - Each reflection names Laura's need and does not justify by gain (SH-16, BS-09).
  - Keep the WInS mirror consistent with the plan (SH-16, F-409).
  - Request the school documentation (BS-11, ADMIN).
- **Tier 2 (IPS, Nov 6):**
  - The framework as pre-set rules any PM could apply (SH-14, BS-08).
  - One clause on professional duties (BS-02).
  - "Promise first" as the central idea, with the operating-money rationale (BS-17).
  - A plain certainty definition (SH-04).
  - "Low cost" as a principle (BS-01).
- **Tier 3 (FR, Dec 4):**
  - A fee assumption in projections (BS-01).
  - Two-sided confidence for the range (SH-04).
  - The fundraising-draft checklist: floor set aside; stretch with its model; operations funded for ten years; US$
    labelled with an NT$ reference; the overrun answer; no share-of-total (SH-05 to SH-07, BS-04 to BS-06, BS-16,
    BS-17).
  - The erosion sentence (SH-12).
  - The human-capital clause (BS-03, BS-13, BS-14).
  - The flexibility rationale (SH-02, SH-26, BS-07).
  - The reporting metric (BS-09).
  - The privacy check (BS-20).
  - Works Cited with the AI record (SH-16, R-W46).

---

## 8. Sources

All web sources were accessed 2026-09-27 from this run's container.

**Official and repo files (VRF):**
- `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
- `2026_WGY_Investment_Policy-FINAL.txt`
- `2026_WGY_Trading_Notes_Analysis-FINAL.txt`
- `SMApply_Deliverables_Page_2026-09-27.md`
- `research/insight_v1/phase_A/case_register.md` (A1; its R-W entries are VP)
- `research/insight_v1/phase_A/fact_register.md` (A2)
- `research/council_2026-09-27/*.md` (prior AI brainstorming, lower authority)
- `research/team_materials/review_why_laura_and_public_profile.md`
- `CLAUDE.md`

The team's two client documents (outside the repo) were read as leads only. Nothing was copied from them. No personal
details from them are used here.

**Web sources:**

| ID | Source | Status |
|---|---|---|
| W-1 | CFA Institute, *Asset Manager Code*, 2nd ed., ©2009, 2010. PDF https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/amc/asset-manager-code-and-guidance-2nd-ed.pdf (downloaded with curl, text extracted) and web page https://rpc.cfainstitute.org/codes-and-standards/asset-manager-code | VP |
| W-2 | Laura Gao, "Hey" page, https://lauragao.com/hey/ (public professional facts only) | VP |
| W-3 | Ann Goggins Gregory & Don Howard, "The Nonprofit Starvation Cycle", Stanford Social Innovation Review, Fall 2009, https://ssir.org/articles/entry/the_nonprofit_starvation_cycle | VP (read with curl) |
| W-4 | Artist Communities Alliance, "Fees, stipends, and funding for residencies", https://artistcommunities.org/fees-stipends-and-funding-residencies (no date shown) | VP |
| W-5 | Emil J Kang, "Artist Residencies Are Arts Infrastructure", Substack, 13 July 2026, https://emilkang.substack.com/p/artist-residencies-are-arts-infrastructure (opinion) | VP |
| W-6 | PKF O'Connor Davies, "Best Practices: Due Diligence on Grantees", Private Foundations Bulletin, July 2019, https://www.pkfod.com/wp-content/uploads/2019/07/Best-Practices-Due-Diligence-on-Grantees-v4.pdf | VP |
| W-7 | Grantmakers in the Arts, "Do Foundation Sustainability Strategies Work?", October 2007, https://www.giarts.org/article/do-foundation-sustainability-strategies-work (roundtable notes; old) | VP |
| W-8 | The Authors Guild, "Everything You Need to Know About Book Advances", 20 July 2021, https://authorsguild.org/blog/everything-you-need-to-know-about-book-advances/ | VP |
| W-9 | American Library Association, "American Library Association releases 2025 Most Challenged Books List…", April 2026, https://www.ala.org/news/2026/04/american-library-association-releases-2025-most-challenged-books-list-national-library | VP |
| W-10 | State Bar of California, Business Law Section, "Charitable Pledges" legislative proposal memo (file BLS-2010-03), https://www.calbar.ca.gov/sites/default/files/portals/0/documents/legislation/BLS-2010-03-charitable_pledges.pdf | VP for the memo's text; current law not checked |
| W-11 | Pledge non-collection "10 to 30 percent" (vendor blogs, e.g. https://www.bonterratech.com/blog/unfulfilled-pledges, which returned 403) | SNIP |
| W-12 | Taiwan Ministry of Culture residency support, https://artres.moc.gov.tw/en/about/index (HTTP 403 with curl) | SNIP |
| W-13 | Capital-campaign lead-gift and board-giving norms: https://afpglobal.org/4-persistent-capital-campaign-myths-dispelled-data (403), https://www.nonprofitpro.com/post/find-right-board-giving-goal-capital-campaign/ (307 redirect, not followed), https://www.donorsearch.net/resources/gift-range-chart-guide/ | SNIP |
| W-14 | Wharton Global Youth, competition main page, https://globalyouth.wharton.upenn.edu/competitions/investment-competition/ | VP (read with curl) |

**Access notes:**
- WebFetch was refused ("EGRESS_BLOCKED") for every host I tried, including hosts the brief lists as reachable
  (lauragao.com, globalyouth.wharton.upenn.edu).
- Plain curl through the proxy worked for most hosts. It returned 403 for afpglobal.org, bonterratech.com,
  littlegreenlight.com, help.candid.org and artres.moc.gov.tw.
- I report these rather than guess what they say.

---

## What this teaches

A client never stands alone. Laura's money serves a building, a staff, visiting artists, co-funders in another country,
and her own reputation, and each of these reads the plan with a different fear. Mapping them does not mean pleasing
everyone. It shows which promise matters to whom: operators need the nominal $50k, co-sponsors need a floor that
exists, and Laura needs her word to hold. It also shows where a single sentence, such as "US$", "set aside" or "funded
for ten years", does more work than another model. The blind spots here are mostly small and cheap to fix, and that is
the point. Judges and statisticians tend to find weak spots in the details nobody owned: fees, labels, paperwork and
wording.
