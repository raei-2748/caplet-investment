# L02: Client knowledge forensic (Laura Gao case vs everything Caplet has written)

Prepared Fri 16 Oct 2026 (Sydney) by an AI reviewer for Team Caplet. **Research and checks only, not submission text.** Nothing here is drafted deliverable prose. Record this review in the team's AI-use log.

Sources read in full: the case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`, 169 lines; `client_case_laura_gao_2026.pdf` is byte-identical, checked with `cmp`), the IPS brief (`2026_WGY_Investment_Policy-FINAL.txt`), the TNA brief, the Guide, the SMApply client and deliverables pages (14 Oct snapshot), IPS V5 (`team/google_drive/ips_report/01_version_5.md`), Tab 15, the 11 filled WInS notes (`05_trading_note_reflection_wins_trading_notes.md`), `COMPETITION.md`, `config/client_mandate.yaml`, `team/google_drive/notes_and_discussions.md`, `strategy_notes.md`, `client_portrait.md`, `final_report.md`, `deliverables/*`, the RAB decision memos (`rab/decisions/D6_cap_share.md`, `D_range_confidence_2031.md`, `D_certainty_definition.md`), `research/insight_v1/ips_spec.md`, `phase_A/case_register.md`. Line numbers below are file line numbers. "Case:N" = `Laura_Gao_2026_Client_Profile.txt` line N.

MODEL = a computed estimate from the repo, not a fact. Most repo model figures are on the 28 Sep STRIPS basis, which the 6 Oct email superseded; re-run before quoting.

---

## 1. The ten things that matter most

1. **The IPS draft has lost the case's own words.** "Flexibility" appears 5 times in the case and 6 times in the IPS brief, and 0 times in V5. "Responsibly" appears 4 and 3 times, and 0 in V5. "Liquidity" 1 and 4, 0 in V5. V1 to V3 had both a certainty definition and "a responsible facility contribution that leaves Laura flexibility". V5 dropped them (CLIENT-01).
2. **"The half Laura keeps" has three jobs and three different investments**, depending on which file you read. In a bad market it is about $16k (MODEL), below the team's own cited reserve benchmark of $25k (CLIENT-02).
3. **The operating-reserve ask has six parts.** V5 answers about one and a half of them (CLIENT-03).
4. **The case demands a stated confidence for the 2031 range, and a dollar range.** Caplet has a formula and the phrase "cannot miss" (CLIENT-04).
5. **The "Laura ultimately chooses" framing and her growth cues are under-read.** About 9% of the money is in stocks, and V5 never explains that choice in client terms (CLIENT-06).
6. **The fundraising draft has no current prep.** The only file is stale and contradicts the team's own research (CLIENT-12).
7. **None of the 11 filled WInS notes mentions flexibility, liquidity or the residency itself.** The TNA reflections must carry the client link (CLIENT-17).
8. **The fixed $50k loses about 20% of its buying power from 2033 to 2042** (2.5% inflation, MODEL). The case quietly hands that gap to co-sponsors. It is a co-sponsor message nobody has written down (CLIENT-09).
9. **"Meaningful" is the other half of the case's co-sponsor test.** Caplet argues only "credible" (CLIENT-11).
10. **Over-reads in the team's client research:** unstable income, human-capital risk, "not a typical artist", and "her quote". These could leak into the Final Report (CLIENT-15).

---

## 2. Line-by-line table: case element -> where Caplet addresses it -> verdict

Verdict key: **OK** = addressed correctly. **THIN** = mentioned, not answered. **GAP** = not addressed. **OVER** = Caplet claims more than the case says. **UNDER** = the case stresses it and Caplet barely mentions it. **MIS** = misread.

| # | Case element (exact words, Case:line) | Type | Where Caplet addresses it | Verdict |
|---|---|---|---|---|
| 1 | "Your portfolio manager (your team's teacher/advisor who makes the final investment decisions …)" (4) | framing | Not addressed. CLAUDE.md says the advisor does admin only. Rules: advisors may not make decisions (case_register.md R-AN4); "Students should place trades on WInS, NOT the advisor" (smapply faqs.txt:34) | GAP (low): the Final Report must describe the real process (CLIENT-21) |
| 2 | "a potential client … planning the next chapter of her career" (5-6) | framing | notes_and_discussions.md:76 ("Why would Laura choose our firm's plan") | OK in notes; absent from V5 |
| 3 | "seeking thoughtful financial planning" (8); "Thoughtful financial planning" (38); "thoughtful risks" (70) | value cue ×3 | V5:22 "measured risk" | THIN |
| 4 | "the investment strategy that Laura ultimately chooses" (9) | framing / ask | case_register.md R-AN5 flags it. No deliverable gives Laura a choice | UNDER (CLIENT-06) |
| 5 | "believes stories have the power to change how people see the world" (12); identity, belonging, storytelling (14) | values | notes:375-389 (client portrait text in notes); V5 none | UNDER in V5 (fine to keep light) |
| 6 | Born Wuhan, raised Texas; Wharton 2018 "Statistics & Information Decisions Management"; product manager in tech (13-17) | facts | V5:22 "statistics graduate"; notes:35 | OK; but V5 uses the degree as risk evidence (OVER, CLIENT-07) |
| 7 | Books "read in classrooms around the world"; "community" (22-23) | values | notes:375 | UNDER in V5 (zero "community", CLIENT-16) |
| 8 | "strategic thinking and a willingness to pursue unconventional opportunities" (26) | personality | notes:377 | OK in notes |
| 9 | Pull quote "The only person who needs to believe in something is yourself." (31-33) | cue | notes:242 warns it is the case's words, not hers; notes:344 and :377 then call it "Her quote" | MIS inside the team's own doc (known; CLIENT-15) |
| 10 | "objectives that reflect both her entrepreneurial mindset and her passion for innovation" (40-41) | cue | Not addressed anywhere in V5 or the notes | UNDER (CLIENT-06) |
| 11 | $300,000 at the beginning of 2027 "with an asset management firm" (43) | number | V5:20; COMPETITION.md:51 | OK |
| 12 | "She will contribute an additional $150,000 at the beginning of 2028, using earnings from publishing advances, speaking engagements, licensing …" (43-45) | number / fact | V5:20, :24; notes:47 "depends on her career going OK"; notes:405, :495 "least stable" income | OK in V5; OVER in notes (CLIENT-15) |
| 13 | Year 0 = 2026 … 2033 = Year 7 (46-58) | convention | COMPETITION.md:61 | OK |
| 14 | "All contributions and withdrawals occur at the beginning of the applicable year. … spaced exactly one year apart." (59-60) | timing | WInS notes use "1 Jan" (05_…md:16-24); D_certainty_definition.md:57 assumption 6 | OK (state the 1 Jan assumption once in the Final Report) |
| 15 | Living expenses "covered by income and financial resources outside the portfolio" (61-63) | capacity | V5:22 "other income covers her living costs" | THIN: drops "financial resources", which is evidence of more risk capacity |
| 16 | No adds or withdrawals before 2033 apart from the two deposits (63-65) | constraint | V5:22 | OK |
| 17 | "understands that investing involves uncertainty and periods of market volatility" (68-69) | risk | Not addressed | UNDER |
| 18 | "willing to take thoughtful risks … recommend an appropriate balance between pursuing growth and protecting the capital required for her goals" (69-74) | risk / explicit ask | V5:22 ("willingness depends on the objective"); about 9% stocks (COMPETITION.md:156-157) | THIN (CLIENT-06, CLIENT-07) |
| 19 | 2033 "collaborative creative residency in Taiwan … small, community-oriented space where artists, writers, designers, entrepreneurs, and educators can temporarily live, work, teach, and collaborate" (75-80) | goal | V5:20 "the Taiwan creative residency she opens in 2033"; V5:22 "the artists" | THIN: V5 never says what the residency is (CLIENT-16) |
| 20 | "funding for the facility as well as reliable support for its early operations" (83) | goal | case_register.md R-AN25 flags "early operations". Not in any deliverable draft | UNDER (CLIENT-09, CLIENT-20) |
| 21 | Portfolio "must fund the operating commitment … and may also cover part of the facility's cost" (84-85) | priority | V5:20 (first and second objectives) | OK |
| 22 | "Any remaining facility cost, and any operating support beyond Laura's commitment, may come from co-sponsors, grants, collaborators, program fees, continued business income, or other sources." (85-86) | permission | Pitch V5:16 says co-sponsors "rarely pay to run it" (unsupported; known). strategy_notes.md:16 says the case "calls them co-sponsors" | MIS (CLIENT-08, CLIENT-16) |
| 23 | Ten $50,000 payments, start of each year 2033-2042 (88-89) | number | V5:20; WInS ladder | OK |
| 24 | "fixed $50,000 and is not adjusted for inflation" (90) | number | ips_merge (15 Oct) and REPORT.md:245 note the real-value loss; V5 none | UNDER for co-sponsor messaging (CLIENT-09) |
| 25 | "funded by the investment portfolio with a high degree of certainty. Teams may not rely on co-sponsors, grants, program fees, or other outside funding" (91-92) | hard constraint | V5:20 "from these two deposits alone". But D6_cap_share.md:54 "she adds her own money"; V5:30 "stays with Laura" | OK in V5's goal, broken in the kit (CLIENT-13) |
| 26 | Beyond 2042 out of scope (92-93) | scope | Not mentioned | OK (but co-sponsors will ask; CLIENT-09) |
| 27 | Reserve set aside "At the beginning of 2033, before making the first operating payment or contributing to the facility" (94-96) | timing | V5:26 "In 2033 the payment Treasuries become the operating reserve" | OK on order; THIN on content |
| 28 | Teams "must recommend its size" (96) | explicit ask | Not in V5 (allowed: IPS-FINAL.txt:68). D_certainty_definition.md:63 says size = holdings + measured coupon gap, not ratified | GAP for the Final Report (CLIENT-03) |
| 29 | "… and initial asset composition" (96-97) | explicit ask | Not stated anywhere for 1 Jan 2033 | GAP (CLIENT-03) |
| 30 | "explain how its composition should change, if at all, as the annual payments approach and are made" (97) | explicit ask | V5:26 "shrinking as each payment is made". Where early-maturity cash waits: only Tab 15 (15_tab_15.md:35) | THIN (CLIENT-03) |
| 31 | "define what they consider a high degree of funding certainty" (98) | explicit ask | V3 had a definition (08_old_versions_v3.md:20); V5:20 has only a mechanism sentence | THIN (known; CLIENT-03) |
| 32 | "explain how they evaluated that level of certainty" (98-99) | explicit ask | rab/decisions/D_certainty_definition.md:23-40 (three tests, MODEL, unratified); none in V5 | GAP in drafts |
| 33 | "identify the assumptions supporting their recommendation" (99) | explicit ask | D_certainty_definition.md:47-57; V5 names one (US government pays) | THIN |
| 34 | "how much of the remaining portfolio she can responsibly contribute" (101-102) | explicit ask | V5:30 (floor + half fund, capped) | THIN: the rule is there, but no reason it is "responsible" (CLIENT-22) |
| 35 | "committing all remaining assets could limit her financial flexibility as the project develops" (102-103) | value cue | V5:30 "cushion if costs rise or co-sponsors fall short" | THIN (CLIENT-01, CLIENT-02) |
| 36 | "There is no predetermined facility contribution. Teams must recommend and justify …" (104-106) | explicit ask | V5:30 | THIN (CLIENT-22) |
| 37 | Not expected to size "a separate contingency fund or endowment" (106-107) | scope | 09_old_versions_v3_tab_7.md:37 uses a nonprofit reserve benchmark | OK if kept light |
| 38 | "begin approaching potential co-sponsors in 2031, two years before" (109) | timing | V5:30 "In 2031 Laura tells co-sponsors a range"; no date, no rule for 2032 conversations | THIN (CLIENT-05) |
| 39 | "describe how much she expects to contribute toward the facility in 2033" (110-111) | ask | V5:30 | OK |
| 40 | "A meaningful personal contribution may signal that the residency is financially viable, demonstrate Laura's commitment …" (111-112) | value cue | ips_spec.md:79 cites it; V5 none | UNDER (CLIENT-11) |
| 41 | "In 2031, however, the value of her portfolio in 2033 remains uncertain." (112-113) | uncertainty | V5:28-30 | OK |
| 42 | "If Laura promises more than she can ultimately contribute, she could damage her credibility …" (114-115) | emotional cue | V5:30 "missing a narrower one would harm her credibility more" | OK |
| 43 | "Rather than promising one exact amount, she wants to communicate a credible range" (115-116) | ask | V5:30 | OK |
| 44 | "recommend the dollar range Laura should communicate" (117) | explicit ask | Formula only (V5:30); projection MODEL in D_range_confidence_2031.md:35 | THIN (CLIENT-04) |
| 45 | "state how confident they are that her 2033 contribution will fall within that range" (117-118) | explicit ask | V5:30 "so she cannot miss the range"; D_range:7 "by construction, if five things hold" | GAP: no level stated (CLIENT-04) |
| 46 | "explain how favorable and unfavorable market outcomes could affect the amount she can provide" (118-119) | explicit ask | V5:28 (falls shrink the part above the floor); the cap's effect in good markets is not explained | THIN |
| 47 | "The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment." (119-120) | constraint | V5:30 "rounded down after any expected shortfall" | OK in idea; the wording can be read two ways (known) |
| 48 | "draft part of Laura's fundraising materials … for prospective co-sponsors" (123-124) | explicit ask | Only deliverables/cosponsor_talking_points.md (stale) | GAP (CLIENT-12) |
| 49 | "Teams may reach different conclusions about risk, asset allocation, liquidity, return expectations, funding confidence, the facility contribution, and the financial flexibility Laura should preserve." (126-128) | framing | Not used | UNDER (CLIENT-06) |
| 50 | WInS "does not determine Laura's actual portfolio value"; do not add WInS gains (129-133) | rule | COMPETITION.md:38-39; V5:26 "scaled down" | OK |
| 51 | Five strategy bullets: certainty, responsible contribution, uncertainty effect on both, communicate clearly and credibly, preserve flexibility (134-145) | explicit asks | V5 covers 1, 3 and 4 partly; 2 and 5 thinly | THIN (CLIENT-01) |
| 52 | Assumptions about "investment performance, the timing of cash flows, outside funding, the effect of inflation on portfolio projections and facility costs, and the financial flexibility Laura should preserve" (146-148) | explicit ask (5 items) | V5: cash-flow timing yes; outside funding yes; inflation on facility costs one clause (V5:28); performance none; inflation on projections none; flexibility none | THIN (CLIENT-03, CLIENT-09) |
| 53 | "consider how favorable and unfavorable investment outcomes would affect their recommendations" (148-149) | ask | V5:28 | THIN |
| 54 | Three connected deliverables; "Evaluators will consider the three deliverables together" (150-162) | rule | COMPETITION.md:34 | OK (consistency risk: CLIENT-02, CLIENT-12) |
| 55 | Final Report covers "operating commitment, facility contribution, financial flexibility, and communication with co-sponsors" (158-160) | structure | deliverables/final_report_outline.md (old plan) | THIN |
| 56 | Facility cost not determined; no budget, funding gap or business plan (164-167) | scope | CLAUDE.md lists a Taiwan construction-cost index as an inflation input, not a cost estimate | OK if kept to inflation |
| 57 | Taxes and Taiwan legal and regulatory requirements out of scope (168-169) | scope | COMPETITION.md:60 | OK |

**Count** (by each row's first tag): of 57 elements, 23 are OK, 17 THIN, 9 UNDER, 6 GAP and 2 MIS. Rows 6 and 12 also carry an OVER tag. The pattern: **Caplet nails the cash flows and the payment priority, but under-answers the case's "explain / define / state / justify" asks, and nearly ignores flexibility, "meaningful" and what the residency is.**

---

## 3. Findings

### CLIENT-01 · IPS V5 has dropped the case's key words and two earlier answers (high · IPS, Final Report · known-deeper)
- **Problem.** Word counts (my grep, 16 Oct):

  | Word | Case | IPS brief | V5 |
  |---|---|---|---|
  | flexib- | 5 | 6 | 0 |
  | responsib- | 4 | 3 | 0 |
  | liquid- | 1 | 4 | 0 |
  | confiden- | 3 | 0 | 0 |
  | assumption | 4 | 0 | 0 |
  | community | 2 | 0 | 0 |

  The IPS brief says the IPS must "establish your strategic approach to … determining a responsible facility contribution, and preserving appropriate financial flexibility" (IPS-FINAL.txt:48-50). It asks "How does your strategy balance growth, risk, liquidity, funding reliability, and financial flexibility?" (:20, again :59). Earlier drafts answered this. V1 (13_old_versions_v1.md:20), V2 (11_old_versions_v2.md:22) and V3 (08_old_versions_v3.md:20) all had "By high certainty we mean …" and "a responsible … facility contribution that leaves Laura (financial) flexibility". V5 replaced both with "a facility contribution with a floor Laura can promise co-sponsors and growth above it" (01_version_5.md:20). This is a regression. A judge scoring Client Knowledge reads for the case's own concepts. Words are not magic, but a missing concept is a missing answer.
- **Fix.** The students' fresh draft must answer, in their own words:
  - what "responsible" means for this gift (see CLIENT-22);
  - what flexibility Laura keeps, and for what;
  - how liquidity is handled (no withdrawals before 2033; each payment from its own maturing holding);
  - the certainty standard.

  Check it with the IPS-FINAL.txt:53-65 bullet list as a tick-box.

### CLIENT-02 · "The half Laura keeps" is booked three times and invested three different ways (high · IPS, Final Report, TNA · new)
- **Problem.**
  - **Three jobs in V5:**
    - (a) first cover for any payment shortfall after the 2027 leftover (V5:26);
    - (b) cushion "if costs rise or co-sponsors fall short" (V5:30);
    - (c) "the equity half Laura keeps is her defense" against inflation and a stronger Taiwan dollar (V5:28).
  - **Three investments across the repo:**
    - V5:28 says it is **equity**;
    - research/insight_v1/ips_spec.md:119 (R5) says it is "moved the same day to U.S. dollar Treasury bills";
    - rab/decisions/D6_cap_share.md:54 says "From the 2033 gift to the last payment she holds her half in **Treasuries**";
    - the stale deliverables/cosponsor_talking_points.md:9 says "Laura keeps **20%**".
  - **Size.** ips_spec.md:119 puts kept money at p5/p50/p95 **$16k/$32k/$66k** (MODEL, STRIPS basis). D6_cap_share.md:22 gives about **$15k-$17k in a 1-in-20 bad case** (MODEL). The team's own V3 notes cite a nonprofit reserve benchmark of 3-6 months of expenses, "about $25k minimum and $100k maximum" for a $50k operation (09_old_versions_v3_tab_7.md:37; benchmark not re-verified by me).
  - So in a bad market Laura's flexibility is below the team's own floor for "appropriate", and it is the first thing used up by a payment shortfall. Bad markets are also when co-sponsors are most likely to "fall short" (no source checked; reasoning only).
  - The RAB red team found the same conflict (rab/redteam/triage.md:39: "gives it three jobs … against the IPS cushion sentence and the case's flexibility ask") and marked it "fix-before-6-Nov". It never reached the 15 Oct brief or V5.
- **Fix.**
  - Vote set B must settle:
    - one priority order for the kept money's jobs;
    - one asset for it after 2033 (equity, T-bills or Treasuries; each answers V5:28 differently);
    - one stated principle for how much flexibility is "appropriate" (case 145; IPS-FINAL.txt:50).
  - If the kept money backs the payments, either count it inside the reserve (see CLIENT-03), or size a separate payment top-up in Jan 2033 and free the rest (triage D1's option).
  - Whatever is chosen, V5:28's "equity half … is her defense" must then be true.

### CLIENT-03 · The reserve and certainty asks have six explicit parts; the drafts answer about one and a half (high · IPS, Final Report · known-deeper)
- **Problem.** The case asks for (Case:96-99):
  1. the reserve's size;
  2. its initial composition;
  3. how the composition changes "if at all";
  4. a definition of high certainty;
  5. how it was evaluated;
  6. the assumptions.

  On top of that, the five assumption categories (Case:146-148). Here is where each stands:
  - **V5 answers (3) partly** ("shrinking as each payment is made", V5:26) **and (4) partly** (a mechanism, V5:20).
  - **Size (1) cannot be stated cleanly** while the payment backstop (the kept half, CLIENT-02) sits outside the reserve. D_certainty_definition.md:63 proposes "the ten holdings' value plus that measured amount", but it is unratified.
  - **Initial composition on 1 Jan 2033 (2) is written nowhere.** By then IBTM has paid out in Dec 2032 (cash for the first payment, which falls on the reserve date itself: case_register.md:48). The reserve also holds IBTO-IBTR (four funds), five coupon bonds and the reinvested coupon units.
  - **Where cash from the Feb-2037 and May-2038 bonds waits** for 10.5 and 7.5 months is only in the WInS notes (05_…md:16-17) and Tab 15 (15_tab_15.md:35). The real plan may use only WInS-listed securities (COMPETITION.md:87-90), and no WInS-listed short Treasury fund has been named (UNVERIFIED).
  - **"Mainly on the US government" (V5:20) hides the coupon-reinvestment part.** On the old basis the government owes "at least about $42,000 of every $50,000" (D_certainty_definition.md:19, :42; MODEL, superseded basis).
  - The 15 Oct brief flagged "certainty undefined" and "where early cash waits". It did not map the six-part ask, the reserve-size ambiguity or the missing 2033 composition.
- **Fix.**
  - IPS: one certainty standard plus the principle for the reserve's composition over time (the case allows "if at all": a static, run-off reserve is a legitimate answer, case_register.md:247).
  - Final Report: a reserve table for 1 Jan 2033 (holding, matures, funds which payment, value on the then-curve), the size rule, the three tests and the assumption list, each re-run on the WInS-listed basis.
  - Owner: rates analyst. Vote set B (Tue 27 Oct).

### CLIENT-04 · The 2031 range needs dollars and a stated confidence; Caplet has a formula and "cannot miss" (high · Final Report, IPS · new)
- **Problem.**
  - The case says teams "must recommend the dollar range" and "state how confident they are" (Case:117-118).
  - V5's answer is a rule: floor rounded down, up to floor plus half the fund's value then (V5:30). It closes with "so she cannot miss the range" (V5:30), which the IBTM note contradicts ("the final payout is not fixed", 05_…md:19; the absolute wording is a known issue).
  - The kit's chosen answer is "by construction, if five things hold" (rab/decisions/D_range_confidence_2031.md:7, :39-45). That is a conditional, not a confidence level.
  - Laura is a statistics graduate (Case:16). The team's own notes say she "can tell a real confidence interval from a made-up one" (notes:343). Co-sponsors read "likely" as about 50% unless a number is given (notes:224, research claim, not re-verified).
  - Also missing: what favourable markets after 2031 do. The cap means the gift does not rise, and the extra goes to Laura. The case asks for both directions (Case:118-119).
  - The kit already has the ingredients (MODEL, STRIPS basis, 28 Sep):
    - none of 1.6 million paths fell outside the range;
    - about 3 in 4 land at or near the top;
    - typical top about $175k, 90% of paths $165k-$190k (D_range_confidence_2031.md:25-35).
- **Fix.**
  - Final Report: a 2026 projection of the dollar range (bottom and the spread of tops), re-run on the WInS basis.
  - Give one stated confidence level and how it was measured, the named ways it can fail (iBond payout, coupon gap, cap rule), and where in the range the gift probably lands.
  - Explain what good and bad markets each do to the gift and to Laura's kept money.
  - IPS: no figures needed (IPS-FINAL.txt:68-69). The absolute words go.

### CLIENT-05 · 2031 is the start of a two-year campaign, not one meeting (medium · IPS, Final Report · new)
- **Problem.** The case says Laura will "begin approaching potential co-sponsors in 2031" (Case:109), so conversations run through 2031-2033. V5's top is "half the equity fund's value then" (V5:30), but:
  - there is no measurement date (1 Jan 2031? the first meeting?);
  - there is no rule for a co-sponsor met in 2032, after the fund has moved.

  If Laura quotes different tops to different co-sponsors, that hurts the credibility the plan exists to protect.
- **Fix.** The policy must fix one valuation date, and say whether the range is ever re-quoted (and in which direction) during the campaign. That rule must stay consistent with the 2033 cap. One sentence in the IPS if it fits; detail in the Final Report.

### CLIENT-06 · Growth cues and "Laura ultimately chooses" are under-read; about 9% stocks is never explained in client terms (high · IPS, Final Report, TNA · known-deeper)
- **Problem.**
  - The case gives three growth cues:
    - her objectives "reflect both her entrepreneurial mindset and her passion for innovation" (Case:40-41);
    - she has been "willing to take thoughtful risks" (Case:70);
    - she wants "an appropriate balance between pursuing growth and protecting the capital" (Case:72-74).
  - It also says "the investment strategy that Laura ultimately chooses" (Case:9), and that teams may reach different conclusions on "the financial flexibility Laura should preserve" (Case:126-128).
  - Caplet's plan has about 9% of all money in stocks after 2028 (COMPETITION.md:156-157). All three simulated Lauras called it "too timid" (notes:101; AI opinion). V5:22 says her tolerance above the floor is "above average", but V5 never says why the growth slice is small.
  - The team's own best answer sits in notes, unused:
    - the "price of certainty" table: each $25k less floor adds $2-3k to the middle outcome but costs $9-10k in a bad market (notes:286-302, MODEL, STRIPS basis);
    - "the leap is the residency itself" (notes:124).
  - The 15 Oct brief noted the "too timid" criticism as open (final.md:613). It did not tie it to Case:40-41 or Case:9.
- **Fix.**
  - IPS: one trade-off principle in client terms: what Laura gives up in the median for what she gains in a bad case, and why that fits a client whose career already carries risk.
  - Final Report: show Laura the dial (floor size against median and bad case, re-run on the WInS basis) with the team's recommendation. That respects "ultimately chooses" and answers "timid" with evidence.
  - TNA: the VT reflection should name the balance in the case's words.

### CLIENT-07 · V5's risk profile rests on an inference the case does not make (medium · IPS · new)
- **Problem.**
  - V5:22: "As a statistics graduate and entrepreneur she accepts measured risk". The case never links her degree to her risk appetite. Its risk evidence is Case:68-74 (understands volatility; thoughtful risks; wants a balance).
  - V5:22 also says "her tolerance for a missed payment is low, since the artists would bear the loss". The case lists artists, writers, designers, entrepreneurs and educators (Case:78-79), and describes the payments as support for "operating expenses" (Case:88). Who bears a missed payment is an inference.
  - Reading a degree as a risk trait can come across as stereotyping to a judge.
- **Fix.** Build the risk paragraph from the case's sentences:
  - capacity: living costs and "financial resources outside the portfolio", Case:61-63;
  - willingness: Case:68-74;
  - the hard constraint: Case:91-92.

  Label any inference as the team's judgement.

### CLIENT-08 · The pitch leads with co-sponsor behaviour, not Laura (medium · IPS · known-deeper)
- **Problem.**
  - The pitch's first clause, "Laura's co-sponsors who fund the building rarely pay to run it" (V5:16), is unsupported (known: final.md:435). The case allows co-sponsors to fund "operating support beyond Laura's commitment" (Case:85-86).
  - Deeper point: the IPS brief says the pitch must communicate the central idea and "how it is designed to support your client's financial goals" (IPS-FINAL.txt:35-36), and "Always remember who your strategy is designed to serve" (:27). V5's first 11 words are about third parties. Tab 15 kept the same structure with "may" (15_tab_15.md:7).
  - The case's own reason for funding payments first is the portfolio-only rule (Case:91-92).
- **Fix.** The pitch's opening idea should rest on a case fact about Laura's goals. 45 words or fewer.

### CLIENT-09 · The fixed $50k shrinks in real terms, and the case hands the gap to co-sponsors (medium · Final Report, IPS · known-deeper)
- **Problem.**
  - Payments are fixed and "not adjusted for inflation" (Case:90). At 2.5% a year (JPM LTCMA US inflation, CLAUDE.md key facts), the 2033 payment is worth about $42,100 in 2026 dollars and the 2042 payment about $33,700 (my calculation: 50,000/1.025^7 and /1.025^16).
  - Within the commitment, the 2042 payment buys about 20% less than the 2033 one (50,000/1.025^9 = $40,000). At Taiwan's +2.04% CPI (Aug 2026, research/insight_v1/phase_A/fact_register.md:23) the figures are $43,500 and $36,400.
  - The case says "operating support beyond Laura's commitment" may come from co-sponsors and program fees (Case:85-86). It calls the ten years "early operations" support (Case:83), and says funding after 2042 is out of scope (Case:92-93).
  - So the honest co-sponsor message includes three things nobody has written down: Laura's support is generous but fixed-dollar; it covers early operations only; and the residency's own income must grow.
  - V5's only inflation sentence is about facility costs (V5:28). The case also asks about "the effect of inflation on portfolio projections" (Case:147). The 30 Sep review noted the real-value loss (REPORT.md:245), but not as a co-sponsor or "early operations" point.
- **Fix.** Final Report: show the payments and the gift in nominal and real terms, with one stated inflation assumption. Say what the fixed-dollar design means for co-sponsors and for after 2042 (scope note only, no business plan). IPS: one clause in the assumptions.

### CLIENT-10 · The promise is in US dollars; co-sponsors in Taiwan may count in NT$ (medium · Final Report · known-deeper)
- **Problem.**
  - The case asks for a "dollar range" (Case:117). It never says what currency facility costs or co-sponsors use. V5:28 states "a stronger Taiwan dollar raises facility costs" as fact; it is an assumption.
  - If co-sponsors budget in NT$, a range that is certain in US$ moves in their eyes. USD/TWD 10-year volatility is 4.69% (fact_register.md:25, FRED). That is about ±6.6% over two years at one standard deviation, roughly ±$10,600 on a $160k gift (MODEL: random-walk scaling, 4.69% × √2).
  - ips_spec.md:119 (R5) already proposes no NT$ conversion or hedge before the facility decision (a forward is a derivative, banned). V5 does not say this.
  - The 30 Sep review said to "name who bears it" (REPORT.md:244). The co-sponsor-perception angle is new.
- **Fix.**
  - Label the currency assumption.
  - State that the range and gift are in US dollars.
  - Name who bears exchange-rate moves (the kept money, consistent with CLIENT-02).
  - Show one illustrative NT$ swing in the Final Report.
  - Do not dramatise Taiwan geopolitics (research/insight_v1/phase_B/B5a_macro_2026.md:561).

### CLIENT-11 · "Meaningful" is half of the co-sponsor test; Caplet argues only "credible" (medium · Final Report, IPS · new)
- **Problem.**
  - The case gives two reasons for the gift: "A meaningful personal contribution may signal that the residency is financially viable, demonstrate Laura's commitment …" (Case:110-112). It then warns against over-promising (Case:114-115). The tension between meaningful and credible is the core of this section.
  - V5 argues only credibility ("a range built to hold", V5:30). The strategy notes admit "a small floor is safe, but it may make a less impressive pitch" (strategy_notes.md:22).
  - Numbers the team has not used (MODEL, using the kit's $145k-$175k illustrative range, D_range_confidence_2031.md:8, :35):
    - the facility gift is about 32-39% of everything Laura deposits;
    - her total residency commitment (operations plus facility) is about $645k-$675k, or 143-150% of her $450k of deposits;
    - investment returns make that possible.

    That is a strong, simple "commitment" signal.
- **Fix.** Name the meaningful-vs-credible trade-off once in the IPS. In the Final Report's co-sponsor section, show the commitment signal with dated numbers re-run on the WInS basis. Avoid any claim about how much more co-sponsors give: no source measures it (strategy_notes.md:22).

### CLIENT-12 · No current prep for the fundraising draft; the only file is stale and contradicts the team's research (high · Final Report · known-deeper)
- **Problem.**
  - The case requires the team to "draft part of Laura's fundraising materials" (Case:123-124). The provisional Final Report outline tells students to "Use `cosponsor_talking_points.md`" (deliverables/final_report_outline.md:16).
  - That file (deliverables/cosponsor_talking_points.md, last changed in commit 2b9376c, 25-28 Sep) describes the old plan:
    - a minimum of "≈ $113k" (:5);
    - "about 80% confidence" (:6);
    - "A strong period can take it above the range" (:8), which contradicts V5's cap;
    - "never below it" (:8);
    - "Laura keeps 20%" (:9);
    - "matching or tiered sponsorship levels" (:11).
  - The team's own research says "don't offer to match" (notes:218).
  - The 15 Oct brief listed it among "old-plan numbers" (final.md:723) but did not flag the matching contradiction or the outline pointer.
  - Open questions no file answers:
    - whose voice the draft uses (it is "Laura's fundraising materials", and Laura is a real person, so no invented quotes from her);
    - who the audience is (non-finance co-sponsors, possibly in Taiwan);
    - what it must contain (range, confidence, meaningful signal, what good and bad markets do, the operating-commitment signal).
- **Fix.**
  - Put a "superseded, do not use" banner on both deliverables/ files (team action; this review cannot edit the repo).
  - Before 9 Nov: the client/co-sponsor lead builds a facts-only checklist (range in US$, stated confidence, the cap, who bears FX, "early operations", commitment numbers, no matching offer).
  - Students write the text after the 9 Nov instructions.

### CLIENT-13 · The shortfall chain must end inside the portfolio; the kit and V5's wording break that (medium · IPS, Final Report · new)
- **Problem.**
  - The case: payments "must be funded by the investment portfolio … Teams may not rely on … other outside funding" (Case:91-92).
  - rab/decisions/D6_cap_share.md:54: "From the 2033 gift to the last payment she holds her half in Treasuries; **beyond it, she adds her own money**." That is reliance on outside money. D_certainty_definition.md:62 says the opposite ("never 'her own money'").
  - V5:30 says the other half "stays with Laura", and COMPETITION.md:161 says "the rest stays with Laura". Both read as money leaving the portfolio. Yet V5:26 uses that same half to cover payment shortfalls. If it has left, the payments rely on Laura's outside money.
  - V5's chain also omits the floor as the last owner (known: final.md vote set A).
- **Fix.**
  - The policy must say the kept money stays invested in the portfolio until the last payment (or until the team's stated release rule).
  - The full shortfall chain must be listed, ending inside the portfolio.
  - Drop D6:54's clause from anything the team reuses.

### CLIENT-14 · The 2028 deposit: the case says "will", while team notes treat it as fragile (low · Final Report · new)
- **Problem.**
  - The case states the deposit as fact: "She will contribute an additional $150,000 at the beginning of 2028" (Case:43-44).
  - The notes say it "depends on her career going OK" (notes:47), call her income "the least stable of any recent client" (notes:405), and say "human-capital risk is central" (notes:495). The case calls her business "successful" (Case:6), and her living costs are met from "income and financial resources outside the portfolio" (Case:61-63).
  - A short sensitivity test (late or smaller deposit) is fine. A section on hedging her human capital (notes:527-530: underweight publishing, AI-dilemma screens) answers a question the case does not ask, and reads as doubting the client.
- **Fix.** Keep deposit risk to one labelled sensitivity line in the Final Report. Keep human-capital hedging out unless it changes a decision. It does not: the payments are in Treasuries.

### CLIENT-15 · Team language about Laura: "her quote", "not a typical artist", identity labels (medium · Final Report, Team · known-deeper)
- **Problem.**
  - The team doc warns the pull quote is the case's words, not hers (notes:242). Two paragraphs later it calls it "Her quote" (notes:344) and "Her quote in the case" (notes:377).
  - "She's not a typical artist" (notes:377) reads as a stereotype of artists.
  - "Laura is the furthest yet from traditional finance" (notes:492) contradicts the case's statistics and tech product background (Case:16-17) and the team's own notes:232 (internships).
  - The client-pattern table labels her "Immigrant, queer author-illustrator" (notes:487). Her public bio does describe "queer immigrant stories", a professorship and Pride in Panels (https://lauragao.com/hey/, accessed 16 Oct 2026). But the case deliberately gives no personal-life hooks (notes:166), and identity is not a portfolio input. The bio also says she uses "she/her and they/them pronouns". Using "she", as the case does, is fine and needs no comment.
  - Other phrases to watch: "the Dream" for the growth sleeve (notes:205); "money for a dream, not money for survival" (notes:379). These are fine in private notes; in a deliverable they risk sounding patronising.
- **Fix.**
  - In deliverables, describe Laura only through the case, plus at most one or two cited public facts that change a decision. Never use identity as a theme or allocation.
  - Never write "Laura says" for the pull quote.
  - Before the Final Report, run a "would Laura be comfortable reading this about herself?" pass.

### CLIENT-16 · Misreadings: co-sponsors, "building", and what the residency is (medium · IPS, Final Report · new)
- **Problem.**
  - strategy_notes.md:16 says the case "names grants, collaborators and others, and calls them co-sponsors". It does not: co-sponsors are listed alongside grants, collaborators, program fees and business income (Case:86).
  - The pitch says co-sponsors "fund the building" (V5:16). The kit sizes flexibility against "Taiwan building-cost rises" (D6_cap_share.md:28). The case says "facility" and "a small, community-oriented space" (Case:77-79). "Building" assumes construction, and the case only says teams need not "prepare a construction budget" (Case:165).
  - V5 never says what the residency is: a place where five kinds of people "temporarily live, work, teach, and collaborate" (Case:78-80). "Residency goals" is in the Client Knowledge criterion (smapply deliverables.txt:59). The team's own review correctly notes "residency" is a programme, not where she lives (research/team_materials/review_why_laura_and_public_profile.md:26). No file assumes Laura moves to Taiwan (grep 16 Oct: none).
- **Fix.** Use "facility", not "building". Show once that the team understands what the residency does, and why reliable early operating money matters to it. Correct the co-sponsor definition in the team's working notes.

### CLIENT-17 · The 11 filled WInS notes never mention flexibility, liquidity or the residency; the reflections must carry the client link (high · TNA · new)
- **Problem.**
  - The TNA brief opens with "growth, risk, liquidity, funding reliability, financial flexibility, and future cash-flow needs" (TNA-FINAL.txt:5-6). Each reflection must say "How the decision supported the client's goals, funding needs, or risk considerations" (:52).
  - A grep of the 11 filled notes (05_…md:14-24) finds none of: flexibility, liquidity, residency, community, confidence.
  - The client links that do exist:
    - IBTR: the payments-versus-facility trade-off (:15);
    - IBTM: the 2031 minimum for co-sponsors (:19);
    - VT: the range top (:14).

    The reflection tabs are empty (04_…md, 06_…md).
- **Fix.** A client-link checklist per suggested pick (labels only; students choose words):
  - **IBTR:** the case's certainty requirement and the portfolio-only rule (Case:91-92); the trade-off with the facility.
  - **IBTM:** credibility with co-sponsors and why over-promising hurts (Case:114-115).
  - **VT:** the balance between growth and protection (Case:72-74); the kept half as flexibility "as the project develops" (Case:102-103). Fix the "promised minimum" overclaim (known).

  Make sure the three together touch growth, risk, reliability and flexibility. Due before the Sat 24 Oct 08:00 Sydney deadline; the team's target is Thu 22 Oct.

### CLIENT-18 · The team's "single source of truth" summarises the client more thinly than the case (low · Team, IPS, Final Report · known-deeper)
- **Problem.**
  - COMPETITION.md §3 (lines 46-61) omits:
    - the six reserve and certainty asks;
    - the five assumption categories;
    - "explain favourable and unfavourable outcomes";
    - "meaningful";
    - "early operations";
    - "operating support beyond Laura's commitment".
  - It also still says "Laura is a fictional client" (:49; known).
  - The team's Client Portrait is a placeholder: "Placeholder for now" (client_portrait.md:14; known, final.md:614).
  - config/client_mandate.yaml is better (it lists the tensions, :219-222) but has `human_approved: false` (:231).
  - The items missing from the summary are the same ones missing from V5.
- **Fix.** The client lead turns the table in section 2 of this file into the team's own one-page case checklist (their words), linked from COMPETITION.md. Tick every row against each draft.

### CLIENT-19 · "Root-and-Branch" echoes Laura's own published words, but V5 never earns the name (low · IPS, Final Report · known-deeper)
- **Problem.**
  - Her official bio says "Laura's roots spread wide through California, Texas, and China" (https://lauragao.com/hey/, accessed 16 Oct 2026). Her memoir is *Messy Roots* (Case:22).
  - So the strategy name has a real, verifiable link to her vocabulary. But in her work "roots" means heritage and identity, and V5 uses it only for Treasuries (V5:16, :24) without explaining it. The open item is in COMPETITION.md:204.
  - A name that is never explained reads as a pun; one explained once reads as tailoring.
- **Fix.** Decide in vote set A whether the name earns its place. If kept, explain the link once and respectfully (the IPS allows no citations, so cite the bio in the Final Report). Never imply Laura endorsed the name.

### CLIENT-20 · The earliest payments rest on the least fixed instruments (low · Final Report · new)
- **Problem.**
  - The case stresses "reliable support for its early operations" (Case:83). A missed first-years payment would hurt a new residency most (reasoning).
  - Because WInS lists no Treasury maturing Feb 2031 to Feb 2036 (COMPETITION.md:93-94), payments 2033-2037 use iBond funds whose "payout is not fixed" (05_…md:19-22). Payments 2038-2042 use fixed bonds.
  - The modelled spread is small: on the old basis the floor holding "pays about $149,000 typically and at least about $146,000" per $150k, so roughly 2.5% at worst (D_range_confidence_2031.md:23-24, MODEL).
- **Fix.** The Final Report names this honestly as a WInS-listing constraint, states the measured worst case on the WInS basis, and names the cover (the 2027 leftover first). One or two sentences; it turns a weakness into evidence of care.

### CLIENT-21 · The case's "portfolio manager makes the final decisions" fiction versus the real rules (low · Final Report · new)
- **Problem.**
  - The case's framing says the advisor "makes the final investment decisions" (Case:4). It also says Laura identified her objectives "working with your portfolio manager" (Case:39-40).
  - The rules say advisors may not make decisions (case_register.md R-AN4), and "Students should place trades on WInS, NOT the advisor" (smapply faqs.txt:34).
  - The Articulation criterion asks the team to explain "the team's research and decision-making process" (deliverables.txt:61).
- **Fix.** In the Final Report, describe the real process: students decided, the advisor did admin. Do not borrow the case's role-play ("our PM approved").

### CLIENT-22 · "Responsible" has no stated test; "half" is a value judgement no client sentence supports yet (medium-high · IPS, Final Report · known-deeper)
- **Problem.**
  - The case asks teams to "recommend and justify the extent to which Laura can responsibly contribute" (Case:105). V5 gives the rule (floor plus half the fund, capped, V5:30) but no reason it is responsible.
  - The kit's reason is a pre-set test: Laura keeps at least 10% of her gift ("about three years of Taiwan building-cost rises") in 95% of paths, which picks about 0.47, rounded to half (D6_cap_share.md:27-32). The memo itself calls the test "a value judgement" (:60).
  - The 15 Oct brief asked for "one principle each for … the half split" (final.md objective 4). No client-based reason has been chosen.
- **Fix.** Vote set B: one sentence of principle linking the share to a case need. For example, what Laura must still be able to cover "as the project develops" (Case:102-103), after the payments are safe. The Final Report then shows the options table (D6:18-24, re-run on the WInS basis) as the evidence.

---

## 4. What Laura is NOT asking for (and where Caplet risks over-delivering)

| Not asked (case line) | Caplet risk | Verdict |
|---|---|---|
| A facility cost estimate, construction budget, funding gap or business plan (164-167) | The Taiwan construction-cost index (CLAUDE.md) is fine as an inflation input; never turn it into a cost | Low risk |
| Sizing a contingency fund or endowment (106-107) | The nonprofit reserve benchmark (09_…tab_7.md:37) is fine as a sanity check only | Low |
| Taxes, Taiwan legal or regulatory setup (168-169) | None found | OK |
| Funding after 2042 (92-93) | None; but say it once to co-sponsors (CLIENT-09) | OK |
| Inflation-adjusted payments (90) | None | OK |
| A return target or "beat the market" | None in V5; old outline had return assumptions only | OK |
| Values screens, ESG, themed or identity investing | notes:535-539 (values sleeve, EM/China "heritage" allocation) and :527-530 (human-capital, AI-dilemma screens) | Medium: keep out of deliverables (CLIENT-14, -15) |
| Stock picking | Darren's 5 Oct challenge (final_report.md:82) has no recorded outcome | Record the decision (known) |
| Using WInS gains in projections (132-133) | None | OK |
| Maximising the facility gift | V5 is correctly about "responsible" in substance, though not in words | OK in substance |
| Liquidity or income before 2033 (61-65) | Old "income-gap cash buffer" idea already rejected (review_why_laura…md:23) | OK |

---

## 5. Language audit: lines about Laura that could read as invented, generic or condescending

| Line | Issue | What the fix must achieve |
|---|---|---|
| V5:16 "co-sponsors who fund the building rarely pay to run it" | Unsupported generalisation; "building" (CLIENT-08, -16) | A case-based opening about Laura |
| V5:22 "As a statistics graduate and entrepreneur she accepts measured risk" | Degree as risk trait (CLIENT-07) | Case Case:68-74 evidence |
| V5:22 "since the artists would bear the loss" | Narrows five groups to one; inference | Label as judgement, or use case words |
| V5:28 "a stronger Taiwan dollar raises facility costs" | Assumption stated as fact (CLIENT-10) | Labelled assumption |
| V5:30 "so she cannot miss the range" | Absolute (known) | Conditional and true |
| V5:30 "The other half stays with Laura" | Implies withdrawal (CLIENT-13) | Stays invested in the portfolio |
| WInS VT note "her promised minimum" (05_…md:14) | Overclaim (known); notes cannot be edited | Explain in the reflection |
| COMPETITION.md:49 "Laura is a fictional client" | False (known) | "Real client, invented financial scenario" |
| notes:344, :377 "Her quote" | Contradicts notes:242 | Case's words only |
| notes:377 "She's not a typical artist" | Stereotype | Delete before any reuse |
| notes:487 "Immigrant, queer …" | Identity labels; not a portfolio input | Keep out of deliverables |
| notes:405, :495 "least stable income"; "human-capital risk is central" | Over-read (CLIENT-14) | One sensitivity line |
| strategy_notes.md:16 "calls them co-sponsors" | Misread (CLIENT-16) | Correct the definition |

---

## 6. What the best team in the world would notice that Caplet has not used

1. **The case hands the inflation gap to co-sponsors.** Fixed-dollar payments plus "operating support beyond Laura's commitment may come from co-sponsors" plus "early operations" means the residency must grow its own income over ten years. Saying so honestly makes the fundraising text more credible (CLIENT-09).
2. **Her total commitment exceeds her deposits.** About $645k-$675k committed from $450k deposited (MODEL) is a one-line "meaningful" signal (CLIENT-11).
3. **The 2031 message is a campaign, not a moment.** Fix the valuation date and the re-quote rule (CLIENT-05).
4. **Confidence as a number with named failure modes**, for a statistics-trained client (CLIENT-04).
5. **Give the client the dial.** Show the floor-size options with the team's pick, because the case says Laura "ultimately chooses" and that teams may differ on flexibility (CLIENT-06).
6. **One flexibility principle, one job order, one investment** for the money Laura keeps (CLIENT-02).
7. **The reserve on 1 Jan 2033 as a table:** what is cash, what is fund, what is bond, which payment each funds, and that "if at all" allows a run-off reserve (CLIENT-03).
8. **The currency in which co-sponsors judge credibility** (CLIENT-10).
9. **Her own published "roots" language**, used once, with respect and a citation (CLIENT-19).
10. **Honesty about the early-payment instruments:** a constraint turned into evidence of care (CLIENT-20).

None of this needs more complexity in the strategy. Every item is a sentence or a table that answers a case line already on the page.

---

## 7. Checklist (owners are suggestions; dates Sydney)

- [ ] Vote set A (Sun 18 Oct): name kept or dropped (CLIENT-19); banned absolute words incl. "cannot miss" and "stays with Laura" (CLIENT-13).
- [ ] TNA (submit by Thu 22 Oct; hard deadline Sat 24 Oct 08:00): client-link checklist per reflection (CLIENT-17).
- [ ] Vote set B (Tue 27 Oct):
  - [ ] kept money: jobs order, asset after 2033 and flexibility principle (CLIENT-02);
  - [ ] "responsible" principle (CLIENT-22);
  - [ ] certainty standard (CLIENT-03);
  - [ ] the 2031 valuation date and re-quote rule (CLIENT-05);
  - [ ] the growth trade-off sentence (CLIENT-06).
- [ ] IPS fresh draft: passes the IPS-FINAL.txt:53-65 bullets and uses the case's concepts (CLIENT-01). Risk paragraph from case words (CLIENT-07). Pitch about Laura (CLIENT-08). "Facility" not "building" (CLIENT-16).
- [ ] Client lead: one-page case checklist from section 2, in the team's words (CLIENT-18). Banner the two stale deliverables/ files (CLIENT-12).
- [ ] Final Report (after 9 Nov):
  - [ ] reserve table and size rule (CLIENT-03);
  - [ ] dollar range plus confidence (CLIENT-04);
  - [ ] the floor-size dial (CLIENT-06);
  - [ ] real-terms and early-operations note (CLIENT-09);
  - [ ] currency note (CLIENT-10);
  - [ ] commitment signal (CLIENT-11);
  - [ ] fundraising checklist then student text (CLIENT-12);
  - [ ] early-payment note (CLIENT-20);
  - [ ] real decision process (CLIENT-21);
  - [ ] "comfortable reading about herself" pass (CLIENT-15).
- [ ] Re-run every MODEL figure quoted here on the WInS-listed basis before use.

---

## 8. Verification log

- Case text read line by line; the PDFs `client_case_laura_gao_2026.pdf` and `Laura_Gao_2026_Client_Profile.pdf` are identical (`cmp`, 16 Oct).
- Word counts: `grep -o -i` over the case, IPS-FINAL.txt, V5 lines 14-30 and Tab 15 lines 6-20 (16 Oct).
- Real-value figures: my arithmetic (Python, 16 Oct). FX two-year figure: 4.69% × √2 (random-walk assumption) from fact_register.md:25.
- Public bio quotes ("Laura's roots spread wide through California, Texas, and China"; "queer immigrant stories"; "Professor of Comics at California College of the Arts"; "Pride in Panels"; "she/her and they/them pronouns"): https://lauragao.com/hey/, fetched 16 Oct 2026 with the scratchpad page tool.
- Not re-verified by me: the nonprofit reserve benchmark (09_…tab_7.md:37); the "likely ≈ 50%" research (notes:224); the List & Lucking-Reiley seed-money result (strategy_notes.md:22); every MODEL figure from rab/ and insight_v1/ (STRIPS basis, 28 Sep); whether a short Treasury ETF is listed on WInS (UNVERIFIED).
