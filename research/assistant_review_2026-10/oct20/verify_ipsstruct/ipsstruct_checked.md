# How professional IPSs are structured, and what that means for a 500-word student IPS (Tue 20 Oct 2026, Sydney)

> **CHECKED COPY (20 Oct 2026, Sydney) of `oct20/ipsstruct/ipsstruct.md`: all 21 fixes E1-E21 from section 3 of `oct20/verify_ipsstruct/verify_ipsstruct.md` were checked against the cited evidence and applied (E1/E14/E15 only CalPERS TAP, not MOSERS, has a liability-matched segment and its cash reserve sits inside it; E2 IPS:123 does not name tables; E3 residency link in A2/B2/C2; E4 G3+G4 in B7; E5/E7/E8 §0 wording; E6 C5+C6 no longer pre-decides D4 or the floor's asset class; E12 values screens were an assistant flag, not a team rejection; E9-E11, E13, E16-E21 dates, line citations and names), with two small evidence-based adjustments (E10, E11) listed under "Fixes not applied" at the end, and each changed spot marked [fixed 20 Oct, E#].**

**AI-generated research by Claude Code for Team Caplet. Evidence only, not text to submit.** It contains **no IPS, pitch or
title-page sentences**. Section 5 gives orderings as lists of element *names*, with word budgets. Students choose a structure and
write every word themselves, with this file, V5, the exemplars and any AI chat closed. If the team uses this file, log it
in the AI-use record now and in the Final Report's Works Cited later. Wharton's AI policy says: "If you use AI to assist you in
any way during the competition, how you use it must be recorded in your Works Cited pages"
(https://globalyouth.wharton.upenn.edu/ai-policy/, as cited in `oct20/verify_ipsfix/ips_fix_list_checked.md:5`).

**Path short forms.** `oct19/` and `oct20/` = `/tmp/claude-0/-home-user-caplet-investment/9a6d3111-0f82-5d56-a545-e37650a2edcf/scratchpad/oct19/` and `.../oct20/`.
- **IPS:n** = `/home/user/caplet-investment/competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`.
- **case:n** = `.../2026_27/Laura_Gao_2026_Client_Profile.txt`.
- **deliv:n**, **FAQ:n**, **trading:n** = `.../2026_27/smapply_public_2026-10-14/{deliverables,faqs,trading}.txt`. These are 14 Oct snapshots. The live FAQ changed on 16-19 Oct; see the compliance matrix `oct20/compliance/compliance_matrix.md` rows Δ1 and Δ3, lines 74 and 76.
- **V5:n** = `oct19/drive/ips_report_live.md`, lines 23-30. **(A)** is the accepted text, the second wording on each line. **(P)** is the pending suggestion, the first wording.
- **FIX** = `oct20/verify_ipsfix/ips_fix_list_checked.md`, the checked copy, with its row IDs (X1, O3, S3 and so on). **KIT** = `oct19/ipskit/ips_writing_kit.md`.
- **Notes:n**, **CR:n**, **UPD** = as defined in FIX (FIX:21, 29-30). [fixed 20 Oct, E20]

**Source copies.** Every web source was fetched on **Tue 20 Oct 2026, about 10:00 Sydney (19 Oct about 23:00 UTC)**. Copies
are in `oct20/ipsstruct/dl/<id>.raw`, with text in `<id>.txt`. Line numbers below refer to those `.txt` files.
- Fetch command: plain curl with a cache-busting query (`oct20/ipsstruct/tools/get.sh`).
- investor.gov refused curl's default user agent (403), so it was fetched with the generic UA "Mozilla/5.0".
- sec.gov refused both (403, "Request Rate Threshold Exceeded"). morningstar.com returned 403, so the Morningstar Australia copy was used (Christine Benz, 12 Oct 2021, `mstar_au.txt:167-168`; whether it is identical to the US page is **UNVERIFIED**). [fixed 20 Oct, E11]
- Every quote is 30 words or fewer.

---

## 0. Summary (five lines)

1. The IPS-type sources (CFA-I/N, the CFA reading, CCF, MOSERS) follow one pattern: **objectives (return and risk) -> constraints (time horizon, liquidity, tax, legal, unique) -> allocation and the role of each asset -> rebalancing -> monitoring, review and governance**; the investor-education and regulatory pages (Vanguard, FINRA, SEC) cover parts of it. [fixed 20 Oct, E5] One pension example, CalPERS TAP, adds a separate **liability-matched (immunized) segment, with a two-year cash reserve held inside it, then a segment for the excess invested like the main fund** ("growth segment" is our label, not TAP's). [fixed 20 Oct, E1, E14] That last structure closely resembles Laura's design (TAP has no facility-floor segment, and its reserve is cash). [fixed 20 Oct, E15]
2. Wharton's IPS brief keeps the objectives/constraints core. It **overrides professional norms** in seven places (six from the brief, one from the case) [fixed 20 Oct, E7]: no citations, no charts, graphics or appendices (charts and graphics are banned at IPS:123; tables are not named, so whether a table counts as a "chart" or "graphic" is **UNVERIFIED**; write in prose to be safe) [fixed 20 Oct, E2], framework instead of detailed calculations (IPS:51-52) [fixed 20 Oct, E8], no final range or projections, 500 words, a strategy frozen after 6 Nov instead of a "living document", and, from the case, taxes and Taiwan legal requirements out of scope (case:168-169). [fixed 20 Oct, E7]
3. Against those elements, V5 is strong on the liability match and the return need. It **misses** flexibility, "responsible", liquidity, a certainty standard, the permitted-investment line and a review measure; FIX already lists all of these. It **over-covers** model numbers and slogans. All of this agrees with FIX; nothing here contradicts it.
4. Three additions from the professional lens (two are new to FIX; the segment framing extends FIX S6):
   - **Keep a stated no-rebalancing rule.** CFA says it should be written down [fixed 20 Oct, E17]; it is in (A) line 27 and dropped by (P). It also needs a post-2033 rule.
   - **Describe the allocation as purpose segments, not percentage ranges.** That is how CalPERS TAP and the CCF "Roles of Investments" section do it.
   - **The 2033 equity sale is itself a liquidity event**, and it could fall in a market downturn.
5. Section 5 gives the kit order plus three alternative orderings (A: CFA constraints order; B: timeline/glide path; C: money in priority order, LDI style). Each is a list of element names with word budgets, held under the kit's 470-word strict cap, and each element is tied to the case line it serves.

---

## 1. Sources found (all fetched 20 Oct 2026, Sydney)

| ID | Source | URL | What it is | Status |
|---|---|---|---|---|
| CFA-I | CFA Institute, *Elements of an Investment Policy Statement for Individual Investors*, May 2010, ISBN 978-0-938367-31-4 | https://rpc.cfainstitute.org/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf (landing page https://rpc.cfainstitute.org/policy/positions/elements-of-an-investment-policy-statement-for-individual-investors) | The standard professional checklist: 4 parts, 16 numbered elements (1a-4c), each with fictitious example wording | Read in full |
| CFA-N | CFA Institute, *Elements of an Investment Policy Statement for Institutional Investors*, May 2010, ISBN 978-0-938367-32-1 | https://rpc.cfainstitute.org/-/media/documents/article/position-paper/investment-policy-statement-institutional-investors.pdf | The institutional twin. It adds "roles and responsibilities of boards and staff" and liability-based risk tolerance | Contents and key sections read |
| CFA-C | Maginn, Tuttle, McLeavey, Pinto, "The Portfolio Management Process and the Investment Policy Statement", CFA refresher reading 2018, Level II (from *Managing Investment Portfolios*, 3rd ed., 2006) | https://www.cfainstitute.org/-/media/documents/article/refresher-readings-free/rr-2018-l2v6r47.pdf | The curriculum's objectives (risk, return) and constraints (liquidity, time horizon, tax, legal/regulatory, unique circumstances) framework | Sections 5-6 read. The PDF is marked "MEMBER USE ONLY" but was served publicly. Quotes are short |
| MS | Christine Benz (Morningstar), "How to create an investment policy statement", 12 Oct 2021 | https://www.morningstar.com.au/personal-finance/how-to-create-an-investment-policy-statement (US copy https://www.morningstar.com/personal-finance/how-create-an-investment-policy-statement returned 403; whether the AU copy is identical to it is **UNVERIFIED** [fixed 20 Oct, E11]) | Investor-education IPS in 6 steps | Read |
| VG | Vanguard, *Vanguard's Principles for Investing Success* (© 2023 edition, form ISGPRINC 112023, `vg_pis_us.txt:1450, 1453`; PDF file dated 6 Mar 2025; charts use data to 2022-2023, `vg_pis_us.txt:1424`) [fixed 20 Oct, E9] | https://corporate.vanguard.com/content/dam/corp/research/pdf/vanguards_principles_for_investing_success.pdf | Investor education on goals, balance, cost and discipline. Vanguard publishes no public IPS template (search on 20 Oct found none) | Goals chapter read |
| FINRA | FINRA Rule 2111 (Suitability), and FINRA investor page "Asset Allocation and Diversification" | https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111 ; https://www.finra.org/investors/investing/investing-basics/asset-allocation-diversification | The regulator's list of what an "investment profile" contains, and goal-by-goal allocation | Read |
| SEC | SEC Office of Investor Education and Assistance [fixed 20 Oct, E21], "Beginners' Guide to Asset Allocation, Diversification, and Rebalancing" (investor.gov) | https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset | Time horizon, risk tolerance, rebalancing | Read |
| CCF | California Community Foundation, *Investment Policy Statement for the Endowment Pool*, adopted 6 May 2026 | https://www.calfund.org/wp-content/uploads/CCF-IPS-Endowment-Pool-5-6-2026-Final.pdf | A public community-foundation IPS: objectives, risk, spending rule with a floor and a ceiling, "roles of investments", ranges, liquidity, rebalancing, review | Read in full |
| MOS | Missouri State Employees' Retirement System (MOSERS), *Investment Policy Statement*, effective 20 Nov 2025 | https://mosers.org/docs/default-source/leadership/investment-policy-statement.pdf | A state-pension IPS: objectives, philosophy, asset/liability study, targets with min/max ranges, mandatory rebalancing, annual review | Sections I-VIII and XVIII read |
| TAP | CalPERS Investment Committee, Agenda Item 5f, "Terminated Agency Pool Rebalance", 16 Mar 2026 | https://www.calpers.ca.gov/documents/202603-invest-agenda-item05f-00-a-mar16/download | A public pension's **LDI / cash-flow-matching** pool: an immunized portfolio (matched securities plus a two-year cash reserve) and a non-immunized segment invested like the main fund (PERF; "growth segment" is our label, not TAP's), annual adequacy test [fixed 20 Oct, E14] | Read in full. This is a board report about the pool, not the policy document itself. The CalPERS *Total Fund Investment Policy* was not fetched (**UNVERIFIED** beyond `tap26.txt:110-120`) |

Not used: Russell Investments' "13 elements" page (404 with and without the cache-buster) and the Vanguard nonprofit page (no IPS content).

---

## 2. What professional IPSs contain, and how each source states it

### 2a. The professional element list (the master list used in §3-§4)

The CFA papers give the canonical skeleton:
- (1) Scope and Purpose;
- (2) Governance;
- (3) Investment, Return, and Risk Objectives;
- (4) Risk Management (CFA-I contents, `cfa_ind.txt:29-58`; CFA-N `cfa_inst.txt:30-60`).

The curriculum's one-line definition: an IPS "sets out a client's return objectives and risk tolerance over that client's relevant time horizon, along with applicable constraints such as liquidity needs, tax considerations, regulatory requirements, and unique circumstances" (CFA-C `cfa_rr.txt:47-50`, 30 words).

| # | Element | CFA source of the element | Short quote |
|---|---|---|---|
| P1 | Context and client description | CFA-I 1a-1b | "A preamble is often useful to relate information about the investor and/or the source of wealth" (`cfa_ind.txt:107-108`) |
| P2 | Governance: who sets, carries out and monitors the policy; how the IPS is reviewed | CFA-I 2a-2b; CFA-N 2d adds boards and staff | "A process for refreshing the IPS as investor circumstances and/or market conditions change should be clearly identified in advance" (`cfa_ind.txt:205-206`) |
| P3 | Overall investment objective (purpose of the money) | CFA-I 3a | "The IPS should relate the purpose of the assets being invested to one or more broad investment objectives" (`cfa_ind.txt:264-265`) |
| P4 | Return requirement (required return, spending arithmetic) | CFA-I 3b | "descriptions of general funding needs and the relationships of those needs to key factors (e.g., inflation, a spending rate)" (`cfa_ind.txt:273-274`) |
| P5 | Risk tolerance = willingness + ability; risk tied to liabilities and to goals | CFA-I 3c; CFA-C 6.1.1 | "any assessment of risk tolerance must consider both an investor's willingness and that investor's ability to take risk" (`cfa_rr.txt:553-554`); "the IPS should account for known liabilities" (`cfa_ind.txt:346`) |
| P6 | Constraints: time horizon, liquidity, taxes, legal/regulatory, unique circumstances | CFA-C 6.2; CFA-I 3d | "liquidity, time horizon, tax concerns, legal and regulatory factors, and unique circumstances" (`cfa_rr.txt:745-746`) |
| P7 | Investment philosophy / beliefs | CFA-I 3e | "The IPS should document the investor's philosophical approach to investing" (`cfa_ind.txt:439-440`) |
| P8 | Permissible asset classes and the role of each | CFA-I 3b; CCF D | "The IPS should set forth all permissible asset classes in which the portfolio may be invested" (`cfa_ind.txt:279-280`) |
| P9 | Policy portfolio: target allocations with ranges | CFA-I 3b | "An asset allocation policy should designate target allocations to each asset class, with allowable ranges around the targets" (`cfa_ind.txt:312-313`) |
| P10 | Rebalancing policy (including a decision **not** to rebalance) | CFA-I 4c | "If the policy is not to rebalance, this policy should be documented in the IPS" (`cfa_ind.txt:531`) |
| P11 | Performance measurement, benchmarks, reporting | CFA-I 4a | "The IPS should establish an objective, reliable mechanism for reporting investment performance" (`cfa_ind.txt:500-501`) |
| P12 | Risk metrics and evaluation | CFA-I 4b | "Consistent use of metrics to assess and evaluate the risk profile ... is important" (`cfa_ind.txt:511-512`) |
| P13 | Other policies: leverage, foreign securities, **currency**, proxy voting, securities lending, ESG screens | CFA-I 3d-3e | "If relevant, specify a policy on foreign currency management" (`cfa_ind.txt:426`) |
| P14 | Spending / distribution rule (endowments, pensions) | CFA-I 3b; CCF C | "Distributions may be characterized as a percentage of portfolio market value or as a specific cash value" (`cfa_ind.txt:304-305`) |
| P15 | Liability-matched segment and cash reserve (LDI) | TAP (MOSERS IV.B states shortfall as the key risk, but holds no matched segment) [fixed 20 Oct, E1] | "liabilities must influence the asset structure" (TAP `tap26.txt:26-27`) |

Two warnings from CFA itself matter for a 500-word IPS:
- "Not every element will be appropriate for every investor or every situation" (`cfa_ind.txt:86-87`).
- "Templates that purport to offer convenience ... almost inevitably sacrifice consideration of factors that are highly relevant to the investor" (`cfa_ind.txt:80-81`).

Both give professional backing for choosing elements, not filling a template.

Why an IPS exists: it "can offer an objective course of action to be followed during periods of market disruption" (`cfa_ind.txt:75-77`). Wharton's own definition says the same thing: an IPS "helps investors stay focused on long-term objectives and make disciplined decisions during changing market conditions" (IPS:4-5).

### 2b. How each source states the six things the task asked about

| Source | Objectives | Risk tolerance | Allocation ranges | Rebalancing | Monitoring / review | Governance |
|---|---|---|---|---|---|---|
| **CFA-I / CFA-N** (template) | Purpose of the assets plus a required return linked to funding needs (`cfa_ind.txt:264-277`) | Willingness and emotional tolerance; liabilities give "some quantitative basis"; "multiple levels of risk associated with ... meeting a specific future financial goal" (`cfa_ind.txt:346-352`). Institutions relate returns to "a liability profile" (`cfa_inst.txt:360-361`) | Targets with "allowable ranges"; the plan may sit in an appendix "which can be revised without requiring approval of an entirely new IPS" (`cfa_ind.txt:230-231`) | Document the boundaries, or document that there is no rebalancing (`cfa_ind.txt:527-531`) | Review the IPS "no less frequently than annually" (example, `cfa_ind.txt:210`); an evaluation horizon (`cfa_ind.txt:373-376`) | Name who approves, who advises, who monitors; "Document acceptance of the IPS" (`cfa_ind.txt:182`) |
| **CFA-C** (curriculum) | Return objective "consistent with the risk objective" (`cfa_rr.txt:609`) | Willingness vs ability grid; where they differ, "Resolution needed" (`cfa_rr.txt:605-606`). "An investor with an above-average ability to assume risk may have legitimate reasons for choosing a lower risk strategy" (`cfa_rr.txt:564-565`) | Strategic asset allocation follows from the IPS plus capital-market expectations | "guidelines for rebalancing the portfolio based on feedback" (`cfa_rr.txt:284`) | "the schedule for review of investment performance as well as the IPS itself" (`cfa_rr.txt:279`) | "duties and investment responsibilities of parties involved" (`cfa_rr.txt:274-275`) |
| **MS** (Benz) | "Step 1: Document your goals" (`mstar_au.txt`, step list). One IPS per goal: "create a separate one for each goal" (`mstar_au.txt:180`) | Implicit in the target mix | Ranges, not points: "express your target allocations to each asset class as a range rather than a specific target" (`mstar_au.txt:208`) | Rebalance at 5 or 10 points from target (`mstar_au.txt:208, 222`) | Check frequency ("Less is more"), what to check first: "whether the portfolio is on track to meet its goals" | None (personal) |
| **VG** | "Create clear, appropriate investment goals." (`vg_pis_us.txt:67`). Goals include "growing wealth to ensure future flexibility" (`vg_pis_us.txt:81-82`) [fixed 20 Oct, E10] | A constraint: "their level of risk tolerance" | (Balance chapter, not read in detail) | (Discipline chapter, not read in detail) | — | — |
| **FINRA** | "investment objectives" is one item of the 2111(a) investment profile (`finra2111.txt:225`) | Profile items include "investment time horizon, liquidity needs, risk tolerance" (`finra2111.txt:225`) | "a different target asset allocation for different accounts" by goal (`finra_aa.txt:256`) | Consider "once a year as part of an annual review" (`finra_aa.txt:265`) | Annual review | — |
| **SEC** | The best allocation "will depend largely on your time horizon and your ability to tolerate risk" (`sec_aa.txt:197`) | "ability and willingness to lose some or all of your original investment" (`sec_aa.txt:205`) | — | Calendar or threshold; "rebalancing tends to work best when done on a relatively infrequent basis" (`sec_aa.txt:303`) | Change the allocation "as you get closer to your investment goal" (`sec_aa.txt:273`) | — |
| **CCF** (community foundation) | Two ranked goals: "(1) to support the current and future operations of the Foundation and (2) to preserve and enhance the real ... purchasing power" (`ccf.txt:104-105`); a 5.7% real return target | "prioritizes capital preservation but accepts prudent market risk" (`ccf.txt:109`); volatility near a 75/25 blend | Table of current / target / range per class (`ccf.txt` p.5) plus a **"Roles of Investments"** paragraph for each class (`ccf.txt:175-201`) | Deviations outside ranges "addressed through rebalancing or acknowledgment of a valid reason" (`ccf.txt:280-282`) | IPS "reviewed annually ... and be either reaffirmed or amended" (`ccf.txt:60-61`); meetings at least 4 a year | Investment Committee / OCIO / staff duties listed (`ccf.txt` A) |
| **MOS** (state pension) | Purpose: benefits "at a reasonable and predictable cost"; a real return objective (`mosers.txt` IV) | Philosophy: "A key risk to the Plan is asset shortfall where assets are insufficient to meet promised benefit obligations" (`mosers.txt:164-165`); "willing to take measured risks" (`mosers.txt:167`) | Figure 1: policy / min / max per class, e.g. Treasuries 20% (15-25%) (`mosers.txt:436`) | "Rebalancing must occur immediately whenever an individual range limit is exceeded" (`mosers.txt:489-490`) | Asset/liability study at least every five years, using "stress tests and scenario analyses" (`mosers.txt:412, 420`) [fixed 20 Oct, E13]; IPS reviewed "at least annually" (`mosers.txt:806`) | Board, committees, CIO, consultants (section V) |
| **TAP** (CalPERS LDI pool) | "the primary performance objective of the TAP portfolio is to minimize funding risk" (`tap26.txt:31`) | Set by the liabilities: an immunized segment "designed to minimize the likelihood of underfunding" (`tap26.txt:34-35`) | **Segments, not percentages:** an immunized portfolio that also holds "two years of projected benefit payments in a cash reserve", plus a non-immunized segment of "assets in excess of those required", invested like the main fund (PERF) (`tap26.txt:38-47`) [fixed 20 Oct, E14] | Annual rebalance that re-checks the hedge and extends maturities (`tap26.txt` p.3) | "Annual updates on current market value ... and an analysis of the adequacy" of assets against liabilities (`tap26.txt:115-116`); tested "growing up to a 6% inflation rate" (`tap26.txt:69`); named residual risks (`tap26.txt:88-97`) | Policy requirements plus separate compliance monitoring (`tap26.txt:110-113`) |

**The closest professional analogue to Laura is TAP**: liability-matched Treasuries with a short cash reserve held inside that segment, a non-immunized segment for the excess invested like the main fund ("growth sleeve" is our label, not TAP's) [fixed 20 Oct, E14], an annual adequacy test, and a plain list of remaining risks. **Caution:** TAP's matched segment uses TIPS and STRIPS, and both are now "NOT permitted" for Laura's plan (live FAQ change Δ3, `oct20/compliance/compliance_matrix.md:76`). Copy the *structure*, never the instruments. TAP's inflation-scenario test also does not transfer directly: Laura's payments are fixed nominal amounts (case:90). The matching test axis for Laura is reinvestment rates (FIX K2).

**The closest analogue to the 2031/2033 contribution rule is CCF's spending rule**: a formula with a floor (4%) and a ceiling (7%) (`ccf.txt:150-151`). It shows that professional IPSs *can* state distributions as **a rule with bounds** (CCF), and CFA-I allows a percentage rule or a fixed cash amount (`cfa_ind.txt:304-305`). [fixed 20 Oct, E19] This supports FIX G2/G7 (bottom and top set by rules), but it is an analogy, not evidence about co-sponsors.

---

## 3. Mapping 1: Wharton's 2026-27 IPS instructions against the professional elements

### 3a. What Wharton requires (exact words)

- Scope of the strategy: "explain how you will invest your client's money to support their financial goals and future cash flow needs while managing risk and uncertainty" (IPS:8-9). "It should reflect your client's goals, time horizons, liquidity needs, desired degree of funding certainty, and need for financial flexibility" (IPS:9-10).
- Five questions to consider (IPS:16-26): the "central idea"; "What principles will guide your investment decisions?"; the balance of "growth, risk, liquidity, funding reliability, and financial flexibility"; how "asset allocation and composition change as future funding needs approach and payments are made"; how the strategy will "protect the operating commitment while preserving flexibility for a responsible facility contribution".
- The IPS must cover: "risk and return, liquidity, portfolio construction and diversification, and planned changes in the portfolio as future funding needs approach" (IPS:46-47). It must also establish the approach to "preparing for the operating commitment, managing the operating reserve's asset composition over time, determining a responsible facility contribution, and preserving appropriate financial flexibility" (IPS:48-50).
- Five "make it clear" points (IPS:53-65): what, why, the balance, how construction and decisions follow "as the client's needs change", and how the approach protects the payments "while supporting a responsible facility contribution".
- Focus: "Focus on the strategy and decision-making framework that guide your portfolio rather than describing individual investments or presenting detailed financial calculations" (IPS:51-52).
- Form: "You do not need to address these points separately. Your goal is to present a clear, cohesive, and well-supported investment strategy" (IPS:66-67).
- **Not expected:** "final operating-reserve calculations, detailed portfolio projections, a final facility-contribution range, or the draft communication to co-sponsors" (IPS:68-69). These "will be developed and supported in the Final Report" (IPS:69-70).
- Freeze: "Your team may not revise its investment strategy after the submission deadline" (IPS:73-74).
- Bans: "Graphics, charts, images, attachments, external links, footnotes, and formal citations are not permitted" (IPS:123). "sources do not need to be cited in the IPS" (IPS:124).
- Gate: "Submissions that do not meet the requirements below will not be considered for semifinal selection" (IPS:82-83).

### 3b. Element-by-element map

Status key:
- **REQ** = Wharton asks for it in words.
- **IMPL** = implied by the brief or case.
- **NOT EXP** = Wharton says it is not expected in the IPS.
- **BANNED / OUT** = not permitted, or outside the case's scope.
- **OPTIONAL** = harmless, but costs words.

| Professional element | Wharton status | Wharton / case words | What it means for a 500-word IPS |
|---|---|---|---|
| P1 Context, client description | IMPL, keep short | "tailored to your client's financial goals, time horizons, and needs" (IPS:45). Past Wharton guidance: "Don't use precious space repeating known facts about your client" (`oct16/research/KB_what_wins.md:202`) | Case facts only as reasons for a choice (FIX O8) |
| P2 Governance, review process | Not asked. The review cadence is IMPL through "as the client's needs change" (IPS:61-62) | Fiction: the PM is "your team's teacher/advisor who makes the final investment decisions" (case:4). Real rule: "Students should place trades on WInS, NOT the advisor ... It should be a team decision" (FAQ:34) | At most one clause: when the plan is reviewed with Laura, and what is checked. Leave who-does-what to the FR's Articulation section (see §6, O7) |
| P3 Overall objective | **REQ** | "What your team is trying to accomplish for the client" (IPS:55); the three objective bullets (case:136, 138, 145) of the five at case:136-145 [fixed 20 Oct, E16] | Three objectives in the case's order (FIX O6) |
| P4 Return requirement | **REQ** ("risk and return", IPS:46) | "reasonable return assumptions consistent with their strategy" (case:132) | A return need in words, plus the growth assumption in words (FIX R6, S7) |
| P5 Risk tolerance, willingness + ability | **REQ** | "thoughtful risks"; "an appropriate balance between pursuing growth and protecting the capital required for her goals" (case:70-74); living costs are covered outside the portfolio (case:61-63) | Willingness and ability **by goal**, with the mismatch resolved (FIX R2; CFA-C grid) |
| P6a Time horizon (multistage) | **REQ** ("time horizons", IPS:10, 45) | Year map (case:46-60); payments 2033-2042 (case:88-89) | Name the stages once (FIX R6) |
| P6b Liquidity | **REQ** (IPS:10, 46, 59) | Operating reserve set aside "before making the first operating payment or contributing to the facility" (case:94) | When each payment's money is ready and where it waits (FIX S3, H1). Also how the 2033 contribution is turned into cash (§7, N3) |
| P6c Taxes | **OUT** | "teams do not need to account for personal income taxes, capital gains taxes" (case:168) | Zero words |
| P6d Legal / regulatory | IMPL, as the competition's permitted list | "Investments permitted (for BOTH contributions, the IPS and Final Report)" (live FAQ, Δ1); Taiwan legal requirements are out of scope (case:168-169) | One line: only WInS-listed stocks, ETFs and Treasury bonds (FIX S4) |
| P6e Unique circumstances | IMPL | The residency and its "early operations" (case:83); the 2028 deposit comes from creative income (case:44-45); co-sponsor credibility (case:114-116) | The residency link (FIX R5); the timing reason for the 2028 rule (FIX R3) |
| P7 Philosophy / principles | **REQ** | "What principles will guide your investment decisions?" (IPS:18) | Principles stated as plain reasoning, not slogans (FIX X6) |
| P8 Permissible assets + role of each | **REQ** ("portfolio construction and diversification", IPS:46) | Diversification may be "across ... risk characteristics, and funding purposes" (trading:49) | The role of each kind of holding by funding purpose (FIX S5; §7, N2) |
| P9 Target allocation with ranges | Not asked; charts and graphics are banned (IPS:123); tables are not named, so whether a table counts as a "chart" or "graphic" is **UNVERIFIED**; write in prose to be safe [fixed 20 Oct, E2]; detail discouraged (IPS:51-52) | — | No percentage ranges. Any shares labelled as Laura's plan (FIX S6) |
| P10 Rebalancing policy | IMPL (IPS:22-23 "how ... composition change") | — | State the hold / no-rebalancing rule to 2033 and what happens after (§7, N1) |
| P11 Benchmarks, performance reporting | Not asked; "detailed financial calculations" discouraged (IPS:51-52) | — | No index benchmarks. The measure is whether each payment is funded (FIX H4) |
| P12 Risk metrics / stress tests | **REQ** through the case: define "high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions" (case:97-99) | "funding reliability" (IPS:20, 59) | The standard, the method type and the assumptions in words. Results are NOT EXP (IPS:68-69) (FIX O3, G1) |
| P13 Currency policy | IMPL through "the effect of inflation on ... facility costs" (case:146-147); currency itself is not in the case (FIX C10) | — | Currency as a labelled assumption, saying who bears it (FIX K5, G8) |
| P13 ESG, proxy voting, securities lending, leverage | **OUT / BANNED**: margin and derivatives are banned (FAQ:46-52); values screens were flagged as unsupported by the case in the 27 Sep assistant review (`research/team_materials/review_why_laura_and_public_profile.md:27`; the case names no values preference) [fixed 20 Oct, E12] | — | Zero words; the permitted-list line covers leverage |
| P14 Distribution / spending rule | **REQ**: "determining a responsible facility contribution" (IPS:49); the payments themselves | Range and confidence: "Teams must recommend the dollar range" (case:117), but the final range is NOT EXP in the IPS (IPS:68-69) | The contribution rule and 2031 principles, no dollars (FIX G1-G8) |
| P15 Liability-matched segment + reserve | **REQ**: "managing the operating reserve's asset composition over time" (IPS:48-49); size, initial composition and change "if at all" (case:95-97) | — | The reserve principle; sizes go to the FR (FIX H5) |
| (Wharton only) Elevator pitch | **REQ**, maximum 50 words (IPS:31-36) | — | No professional equivalent. The closest are Benz's "The idea is to be succinct" (`mstar_au.txt:194`) and MOSERS's mission statement |
| (Wharton only) Link to the WInS portfolio | IMPL: "Your portfolio and Final Report should reflect the strategy established in your IPS" (IPS:75-76) | — | One clause, or a logged decision to leave it to the FR (FIX S8, D7) |

---

## 4. Mapping 2: what Laura's case demands, and what V5 covers, misses or over-covers

Columns: element; case demand (line); V5 (A) and (P) evidence (line); verdict; FIX row(s). The verdicts were re-checked against FIX and agree with it. Term counts were re-run on 20 Oct over `oct19/ips/work/v5_accepted.txt` and `v5_pending.txt`. "liquidity" is 0 in (A) and 1 in (P). "flexib" is 0 and 2. "responsib" is 0 and 0. "rebalanc" is 1 and 0. "horizon", "willing", "monitor", "meaningful", "credib" and "currency" are 0 in both. This matches FIX O6 and FIX §0 item 7.

| Element | Case demand | V5 evidence | Verdict | FIX |
|---|---|---|---|---|
| Overall objectives | Payments "with a high degree of certainty" (case:91, 136); "responsible facility contribution" (case:138); "appropriate financial flexibility" (case:145) | (A) 25: primary + secondary objective only; "flexibility" and "responsible" absent. (P) 25 adds "preserving her financial flexibility" | **Misses** the third objective in (A) and "responsible" in both | O5, O6 |
| Central idea up front | "What is the central idea" (IPS:16) | (A) 25 opens with case facts; the idea first appears in 27 ("Buy the payments, then the floor, then growth") | **Partly covers, late** | O8, X5 |
| Return requirement | "reasonable return assumptions" (case:132) | (A) 26 "require a 5.1% annual return on the 2027 deposit"; (A) 27 "assumed to return 7% a year before inflation" | **Covers** (keep the 5.1% idea; state the convention) | R1 (keep note), R6, S7 |
| Risk tolerance by goal | "thoughtful risks" / "appropriate balance" (case:70-74) | (A) 26 capacity only ("capacity for risk is high"); (P) 26 adds willingness ("takes thoughtful risks but seeks a balance"), but not goal by goal | **Misses** willingness in (A); **partial** in (P) | R2 |
| Liability matching | Ten fixed $50k payments, portfolio only (case:88-92) | (A) 27 ladder for all ten payments | **Covers**: the design's core strength (the professional LDI pattern, TAP) | S1, S2 (reasons and order) |
| Certainty standard + how tested + assumptions | case:97-99 | (A) 25 a mechanism ("covered by Treasuries"), no level and no test; (A) 29 a model percentage | **Misses** the standard; **over-covers** results | O3, G1, K2 |
| Multistage time horizon | case:46-60 | Dates scattered (25, 27, 29); no horizon statement; "horizon" 0 | **Partial** | R6 |
| Liquidity | IPS:10, 46, 59; case:94 | (A) 28 "Maturing bonds, not sales, supply every payment" is false for 2038/2039 (Notes:16-17); "liquidity" 0 in (A) | **Misses / false** | S3, H1, O4 |
| Legal / permitted investments | live FAQ Δ1, Δ3 | No line | **Misses** | S4 |
| Taxes | Out of scope (case:168) | Silent | **Correct**: do not add | — |
| Unique circumstances: residency purpose | "reliable support for its early operations" (case:83) | "residency" once in (A) (25); no link from design to purpose | **Misses** | R5, O7, Pi4 |
| Unique circumstances: 2028 deposit income | case:43-45 | (A) 26 "depends on publishing and speaking income" | **Covers the rule**, but the reason reads as doubt | R3, R4 |
| Principles / philosophy | IPS:18 | (A) uses slogan sentences as principles: "Hold to maturity." (28), "Promise only what is owned." (29), "Name the residual risks." (30) | **Covered in a weak register**; one is misleading | X6, G3, K1 |
| Role of each holding / diversification | IPS:46; trading:49 | (A) 27 "Concentration in one issuer is deliberate"; one diversified global fund | **Covers** (keep the idea; drop the absolute claim) | S5 |
| Allocation shares | (none required) | (A) 27 "two-thirds ... one quarter ... under one tenth" | **Covers as outcome shares**; must be labelled as Laura's plan | S6 |
| Rebalancing | IPS:22-23 | (A) 27 "left unrebalanced until 2033"; (P) drops it; nothing after 2033 | **Covers to 2033 in (A) only**; **misses** the post-2033 rule | §7, N1 (new); H2, D2 |
| Monitoring / review | IPS:61-62 | (A) 28 "At each January review with Laura"; no measure or trigger | **Partial** | H4 |
| Operating reserve composition over time | case:94-97; IPS:48-49 | (A) 28 "these Treasuries become the operating reserve, running off as each matures" | **Partial** (no set-aside principle, no waiting-money home) | H5, S3 |
| Shortfall order to 2042 | case:91-92 (portfolio only), case:119-120 | (A) 25 "covered by her other assets, with the floor used last" (ambiguous, and fails after 2033); (A) 28 equity backstop | **Misses / conflicts** | O1, O2, H2, D5 |
| Contribution rule (distribution) | case:101-107 | (A) 29 "the floor plus half the fund, capped at the upper bound" | **Covers the rule**; **misses** "responsible" and the reason for "half" | G5, O6 |
| 2031 range principles | case:109-120 | (A) 29 bottom and top rules; no valuation date, re-quote rule, currency or "meaningful" | **Partial** | G2, G7, G8 |
| Range dollars / odds / stress figures | NOT EXP (IPS:68-69) | (A) 29 "three of four simulated paths", "$169,000 to $162,000"; (A) 30 "$21,000"; (P) 30 adds $136,000 and 12% | **Over-covers** | X3, G1, G4, K2, K6 |
| Good vs bad markets in words | case:118-119, 148-149 | Only as figures in (A) 29 | **Covered only as numbers** | G4 |
| Residual risks + what absorbs each | case:140-141 | (A) 30 opens with "Beyond a US default"; inflation/FX named without a policy | **Partial** | K3, K4, K5 |
| Currency | (not in the case) | (A) 30 "a stronger Taiwan dollar raise costs" | **Partial**: a labelled assumption is needed | K5, G8, C10 |
| Benchmarks, ESG, proxy, leverage, fees, governance roles | (not in the case) | Silent | **Correct**: do not add | — |
| WInS link | IPS:75-76 | No V5 sentence (the WInS line is in V4: `ips_report_live.md:45`, V4 tab) [fixed 20 Oct, E20] | **Misses** (or log a D7 decision) | S8, C12 |
| Elevator pitch | IPS:31-36 | (P) 23 is 49 strict / 53 with heading; (A) lists purchases without the why | **Gate risk + misses the why** | Pi1-Pi4 |

**Net picture.**
- V5 already has the two elements most professional IPSs treat as central to a liability-driven client: the liability match and the return requirement.
- What it lacks are the *constraint* and *policy* elements: liquidity, legal, horizon, review measures, the post-2033 rule and the certainty standard. It also lacks two of the case's three objective words.
- It spends its words on the elements Wharton says are not expected: final figures, odds and stress results. This agrees with FIX §0 items 4, 6, 7 and 8.

---

## 5. Orderings for a 500-word student IPS (element names only; no sentences)

**Rules that apply to every ordering.** These come from FIX §3a and KIT §3 and are not changed here.
- Strict-counter totals: pitch body 41 or fewer (45 or fewer with its heading); IPS 470 or fewer including headings (Wharton's caps are 50 and 500).
- Seven body paragraphs or fewer help the two-page fit.
- Sub-headings are optional ("You do not need to address these points separately", IPS:66), and any sub-heading counts inside its paragraph's budget.
- Numbers only from FIX §3b.
- Every element below depends on the D-decisions in FIX §0 / UPD §7. A skeleton is a container, not a decision.

**The pitch is the same for every ordering:** central idea; why it suits Laura (portfolio-only payments, case:91-92); the order of use; what co-sponsors can rely on. Body target 35-41, cap 41 (FIX Pi1-Pi2; IPS:35-36).

### Baseline 0: the kit order (already in KIT §3; shown for comparison only)

P1 objectives (50/60) · P2 Laura and risk by goal (60/70) · P3 certainty standard (60/70) · P4 building the portfolio
2027-28 (80/90) · P5 changes over time and the operating reserve (60/70) · P6 facility contribution and 2031 (60/70) · P7
trade-off and WInS (30/37). Targets total about 400 and caps 467, plus a 3-word heading (KIT:394-541; FIX §3a).

### Ordering A: "CFA order" (objectives -> client risk -> constraints -> portfolio -> policy over time -> facility)

Closest to professional practice (CFA-I §3-4; CFA-C §6). It differs from the kit by giving the **constraints** (horizon,
liquidity, permitted investments) their own short block, ahead of construction.

| # | Element names (no wording) | Target / cap (words) | Case line(s) served | Wharton line(s) | FIX rows |
|---|---|---|---|---|---|
| A1 | Strategy name + central idea; three objectives in priority order (payments; responsible contribution; flexibility) | 50 / 55 | case:91, 101-103, 136-145 | IPS:16, 55 | O5, O6, O8 |
| A2 | Return need (case-derived); willingness vs ability by goal + how resolved; reason for the 2027 sizing rule (timing); residency link: payments-first to the residency's early operations (case:83) [fixed 20 Oct, E3] | 55 / 62 | case:43-45, 61-74, 83, 132 | IPS:46, 57 | R1-R6 [fixed 20 Oct, E3] |
| A3 | Constraints: multistage horizon (stage names); liquidity events (each 1 January, the 2033 set-aside and contribution); permitted-investment line; (taxes: zero words) | 40 / 48 | case:46-60, 94, 168-169; live FAQ Δ1/Δ3 | IPS:10, 46, 59 | S3, S4, R6 |
| A4 | Certainty standard; how evaluated (method type, scenario kinds); key assumptions; residual risks + what absorbs each | 55 / 62 | case:96-99, 140-141, 146-149 | IPS:20, 59, 64-65 | O3, K2-K5 |
| A5 | Portfolio by funding purpose: payment segment, facility-minimum segment, growth segment (roles, diversification); 2027 build rule + overrun rule; 2028 order of use; return assumption | 70 / 80 | case:88-92, 132 | IPS:46, 61-62; trading:49 | S1, S2, S5-S7 |
| A6 | Policy over time: hold to maturity; no-rebalancing rule (to 2033 and after); January review measure + triggers (ladder over $300k; late or small 2028 deposit); waiting-money home; operating reserve set-aside, composition, run-off; shortfall order to 2042 | 60 / 65 | case:91-97, 119-120 | IPS:22-23, 48-49 | H1-H5, O1, O2 |
| A7 | Facility contribution rule; "responsible" principle + reason for the share; flexibility kept; 2031 range principles (bottom rule, top rule, valuation date, re-quote, currency, "meaningful"/"credible"); good vs bad markets in words | 60 / 65 | case:101-120 | IPS:25-26, 49-50, 64-65 | G1-G8 |
| A8 | The one trade-off accepted; WInS clause | 25 / 30 | case:72-74 | IPS:20, 75-76 | K7, S8 |
| | **Totals** (+3-word heading) | **415 / 467** | | | |

- Strength: every CFA constraint has a visible home, which matches Client Knowledge's "risk considerations" (deliv:56).
- Weakness: eight paragraphs, one over the seven-paragraph guide. Fix this by merging A3 into A2 or A8 into A7.
- Weakness: liquidity appears twice (A3 names it; A6 handles it). Keep A3 to the stage and event names only.

### Ordering B: "Timeline / glide path" (stages in date order)

Answers IPS:22-23 most directly ("How will the portfolio's asset allocation and composition change as future funding needs
approach and payments are made?"), and Investment Strategy's "disciplined planning across Laura's changing time horizons
and cash-flow needs" (deliv:55). The SEC guide's logic is the same: change the allocation "as you get closer to your
investment goal" (`sec_aa.txt:273`).

| # | Element names (no wording) | Target / cap | Case line(s) | Wharton line(s) | FIX rows |
|---|---|---|---|---|---|
| B1 | Strategy name + central idea; three objectives | 50 / 55 | case:91, 101-103, 136-145 | IPS:16, 55 | O5, O6, O8 |
| B2 | Laura: return need; risk by goal; why only the 2027 deposit is sized for the payments; residency link: payments-first to the residency's early operations (case:83) [fixed 20 Oct, E3] | 55 / 62 | case:43-45, 61-74, 83 | IPS:45-46, 57 | R1-R6 [fixed 20 Oct, E3] |
| B3 | Certainty standard; how tested; assumptions; residual risks + absorbers | 55 / 62 | case:96-99, 140-141 | IPS:59, 64-65 | O3, K2-K5 |
| B4+B5 | **Stage Jan 2027**: first deposit buys the payments; overrun rule; why buy on arrival. **Stage Jan 2028**: order of use of the second deposit; diversification by purpose; permitted-investment line (one paragraph) | 95 / 108 | case:43-45, 88-92; live FAQ Δ1/Δ3 | IPS:46, 61-62 | S1-S8 |
| B6 | **Stage 2028-2032**: hold; no rebalancing; January review measure + triggers; waiting-money home | 45 / 50 | case:64-65 | IPS:22-23, 59 | H1, H3, H4, S3 |
| B7 | **Stage 2031**: range principles (bottom rule, top rule, valuation date, re-quote, currency); credibility vs "meaningful"; good vs bad markets in words; what sets the bottom and the top (true mechanism) [fixed 20 Oct, E4] | 45 / 50 | case:109-120 | IPS:25-26, 64-65 | G2-G4, G7, G8 [fixed 20 Oct, E4] |
| B8 | **Stage 2033-2042**: operating reserve set-aside, composition, run-off; contribution rule + "responsible" principle + reason for the share; kept money's job and home; shortfall order; the trade-off; WInS clause | 75 / 80 | case:94-107, 119-120 | IPS:48-50, 75-76 | H2, H5, G1, G5, G6, O1, O2, K7, S8 |
| | **Totals** (+3 heading) | **420 / 467** | | | |

- Strength: a cold reader can follow the money through time, and the two dated events (2031 and 2033) stay separate (FIX O5).
- Weakness: "responsible" and "flexibility" are spread across B7 and B8, so they risk being implied rather than stated. Name each once (FIX O6).
- Weakness: B8 is crowded. If it overruns, move the WInS clause to B4+B5.
- Weakness: dates invite numbers. Keep to case-derived figures only (FIX §3b).

### Ordering C: "Money in priority order" (LDI segments, the professional pension pattern)

Mirrors CalPERS TAP's immunized segment + reserve + "assets in excess" segment (`tap26.txt:34-41`) and CCF's "Roles of
Investments" (`ccf.txt:175-201`). This is the structure the case's own priority implies: payments first, then a
contribution that "must also protect" them (case:119-120).

| # | Element names (no wording) | Target / cap | Case line(s) | Wharton line(s) | FIX rows |
|---|---|---|---|---|---|
| C1 | Strategy name + central idea; objectives in priority order; the out-vs-in gap ($500k vs $450k) as the problem solved | 50 / 55 | case:43-45, 88-92, 136-145 | IPS:16, 55 | O6, O8 |
| C2 | Laura: return need; risk by goal (low ability for the payment money, high beyond it, and why); horizon stages; residency link: payments-first to the residency's early operations (case:83) [fixed 20 Oct, E3] | 55 / 62 | case:46-74, 83 | IPS:45-46, 57 | R1-R6 |
| C3 | **Payment money**: what it holds (permitted-investment line); 2027 build rule + overrun rule; liquidity and waiting-money home; hold to maturity; becomes the operating reserve in 2033 + run-off | 80 / 90 | case:88-97; live FAQ Δ1/Δ3 | IPS:46-49, 59 | S1, S3, S4, H1, H3, H5 |
| C4 | **Certainty standard for the payment money**: definition; how tested; assumptions; residual risks + which money absorbs each (shortfall order to 2042) | 60 / 65 | case:91-92, 96-99, 140-141 | IPS:20, 59, 64-65 | O1-O3, K2-K5, D5 |
| C5+C6 | **Money beyond the payments** (one paragraph): facility-minimum segment (source per the S2 order of use and D4; definition rule; rounding rule; its asset class and why) [fixed 20 Oct, E6]; growth segment (one broad fund; return assumption; no rebalancing; its jobs in priority order; where it sits after 2033) | 85 / 95 | case:101-107, 132 | IPS:46, 50; trading:49 | S2, S5-S7, G7, H2, D2, D4 |
| C7 | **The rules that connect them**: 2033 contribution rule + "responsible" principle + reason for the share; flexibility kept; 2031 range principles (valuation date, re-quote, currency, "meaningful"); good vs bad markets in words; January review measure + triggers; trade-off; WInS clause | 85 / 100 | case:101-120, 148-149 | IPS:25-26, 49-50, 61-65, 75-76 | G1-G8, H4, K7, S8 |
| | **Totals** (+3 heading) | **415 / 467** | | | |

- Strength: the clearest "funding reliability" logic for Portfolio Analysis (deliv:57). Each dollar has one job, and the certainty standard sits next to the money it protects.
- Strength: it is the shape a fixed-income PM would expect.
- Weakness: C7 carries a lot. It is the riskiest paragraph for the 2031 principles.
- Weakness: "planned changes over time" (IPS:47) is spread across C3 and C5+C6. A cold reader may miss the timeline, so name the stages once in C2.
- Weakness: the segment framing must not read as "owned" money before it is bought (FIX G3).

### Which ordering fits which goal (AI opinion; the team chooses)

| If the team wants mainly... | Ordering | Why (criterion phrase) |
|---|---|---|
| The fewest changes from V5 and the kit | Baseline 0 or A | V5's paragraphs already roughly follow this order (V5:25-30) |
| To show "changing time horizons and cash-flow needs" | B | deliv:55; IPS:22-23 |
| To show "funding reliability" and a fixed-income logic | C | deliv:57; case:96-99; TAP pattern |
| The cleanest "client knowledge" story | A | Constraints and risk by goal sit up front (deliv:56) |

Whichever is chosen, run the KIT §3 coverage self-check after drafting. "liquidity", "diversification", "responsible", "flexibility", "operating reserve" and "high degree of certainty" should each appear at least once, in the case's meaning (KIT, end of §3; FIX §4 item 14).

---

## 6. Where Wharton's instructions override professional norms (flags)

| # | Professional norm | Wharton override | Consequence |
|---|---|---|---|
| O1 | Policies cite statutes and standards, e.g. MOSERS footnotes to RSMo (`mosers.txt` p.4-6), CCF cites UPMIFA (`ccf.txt` C, L) | "footnotes, and formal citations are not permitted" (IPS:123); "sources do not need to be cited in the IPS" (IPS:124) | Name assumptions in words with no source. Sources go to the FR (IPS:124-125). How to disclose AI use in the IPS is still **UNVERIFIED** (FIX §5) |
| O2 | Allocation tables and appendices: MOSERS Figure 1, CCF's table, CFA's "asset allocation policy statement as an appendix" (`cfa_ind.txt:230`) | "Graphics, charts, images, attachments" not permitted (IPS:123) | Allocation in words. Purpose segments (C) or rounded shares labelled as Laura's plan (FIX S6) |
| O3 | Quantified objectives: CCF 5.7% real; MOSERS ranges; CFA risk objectives such as "the loss in any one year is not to exceed x percent" (`cfa_rr.txt:585`) | "rather than ... presenting detailed financial calculations" (IPS:51-52); final reserve calculations, projections and range not expected (IPS:68-69) | Case-derived numbers plus at most one or two dated anchors (FIX §3b-3c) |
| O4 | A living document: "reviewed annually ... and be either reaffirmed or amended" (`ccf.txt:60-61`); MOSERS amended nine times since its 2018 adoption (`mosers.txt:806-810`); CFA-I 2b | "Your team may not revise its investment strategy after the submission deadline" (IPS:73-74) | Any future action the team wants must be **pre-committed now as a rule with a trigger** (FIX H4). A review clause must not read as "we will rethink the strategy later" |
| O5 | Professional IPSs run 10-25 pages (CFA-I 26 pp.; MOSERS 22 pp.; CCF 10+ pp.) | 500 words; two pages for pitch + IPS (IPS:104-109) | Choose elements. CFA itself says "Not every element will be appropriate" (`cfa_ind.txt:86-87`) |
| O6 | Tax and legal constraints are core (CFA-C 6.2.3-6.2.4) | Taxes and Taiwan legal requirements out of scope (case:168-169) | Zero words on tax. "Legal" becomes the competition's permitted-investment list |
| O7 | Governance sections assign roles (CFA-I 2a-2e; CCF A; MOSERS V) | Not asked; the case's PM fiction (case:4) differs from the real rule that students decide and trade (FAQ:34) | Keep roles out of the IPS. The team's decision process goes in the FR's Articulation section (deliv:58) |
| O8 | No headline pitch (closest: a mission statement, MOSERS II) | A 50-word elevator pitch is required (IPS:31-36) | Treat it as a separate deliverable inside the IPS, held to the same principles |
| O9 | CalPERS TAP matches with TIPS and STRIPS (`tap26.txt:36-38, 58`) [fixed 20 Oct, E15] | TIPS and STRIPS "NOT permitted" for both contributions (live FAQ Δ3) | Copy the segment structure only. Never name TIPS or STRIPS as an option (FIX S4) |
| O10 | Numbered, headed sections | "You do not need to address these points separately"; "clear, cohesive" (IPS:66-67) | Headings are optional and count as words. Paragraph order carries the structure |
| O11 | Benchmarks and performance attribution (CFA-I 4a; CCF F; MOSERS XI-XII) | Not asked; detail discouraged (IPS:51-52) | The only measure needed: whether each payment is funded (FIX H4; TAP's annual adequacy test is the professional analogue) |
| O12 | "Document acceptance of the IPS" with signatures (`cfa_ind.txt:182`) | The title page needs the official team name, member names and the WInS username (IPS:84-100) | Not applicable. Never commit the PDF with the username (FIX T3) |

---

## 7. What the professional lens adds that FIX does not already say (new; consistent with FIX)

A search on 20 Oct of FIX, KIT and `oct20/rubric/rubric_scoring.md` for "rebalanc" and "governance" found **no hits**. N1 (rebalancing), N3 (the 2033 contribution as a liquidity event) and N5 (review and governance) are therefore new. N2, N4 and N6 extend existing FIX rows without changing them.

- **N1. A stated rebalancing policy.**
  - CFA: "If the policy is not to rebalance, this policy should be documented in the IPS" (`cfa_ind.txt:531`; same in `cfa_inst.txt:568`).
  - (A) line 27 has "left unrebalanced until 2033". (P) line 27 drops it.
  - After 2033, no rule says whether the kept stock money is held, sold down or rebalanced. That links to FIX H2 / D2 (where the kept money sits 2033-2042).
  - What a fix must achieve: one principle-level statement of the no-rebalancing rule to 2033 and the rule after it, consistent with the job the VT note gives stocks (Notes:14), which is silent on rebalancing. [fixed 20 Oct, E18]
- **N2. Allocation as purpose segments, not percentage ranges.**
  - Professional percentage ranges (MOSERS Figure 1; Benz's "range rather than a specific target", `mstar_au.txt:208`) assume rebalancing back to targets. Laura's plan does not rebalance.
  - The professional form for a cash-flow-matched plan is TAP's segments ("assets in excess of those required", `tap26.txt:40-41`), plus CCF-style roles for each holding.
  - Do not add ranges. Shares, if used, are outcomes, labelled as in FIX S6.
- **N3. The 2033 contribution is a liquidity event too.**
  - CFA-C: "An example of a liquidity event is planned construction of a building" (`cfa_rr.txt:756-757`). Also: "If the timing of an investor's liquidity requirements is significantly correlated with market downturns ... in favor of less risky assets" (`cfa_rr.txt:771-773`, shortened).
  - The half-of-the-fund part of the contribution needs stock fund units sold at a 2033 price. FIX S3/H1 cover the payments' liquidity, not this.
  - What a fix must achieve: the liquidity principle covers how the contribution's stock part becomes cash, and what a 2033 downturn does to it. This is in words; the figure goes to the FR, consistent with FIX G4.
- **N4. The willingness-ability resolution, named.**
  - CFA-C's grid labels a mismatch "Resolution needed" (`cfa_rr.txt:605-606`). It also says an investor with high ability "may have legitimate reasons for choosing a lower risk strategy" (`cfa_rr.txt:564-565`). Its example is an entrepreneur who has built wealth and "may now simply not want to lose wealth" (`cfa_rr.txt:570-572`).
  - This is the professional vocabulary for FIX R2 (high capacity, yet about 92% Treasuries: CR:99's confusion).
  - Use it as a reasoning pattern only. The case does not say Laura fears losses, and FIX bans Laura quotes and invented traits (KIT E-list).
- **N5. A review clause and governance in one clause, not a section.**
  - Professional IPSs fix a review cadence (CFA-I "no less frequently than annually", `cfa_ind.txt:210`; CCF; MOSERS) and an adequacy test (`tap26.txt:115-116`) [fixed 20 Oct, E20]. V5 (A) 28 already has the January review with Laura.
  - Per O4 and O7: no roles, no teacher/PM, and no promise to revise the strategy. The review checks pre-set measures and fires pre-set triggers (FIX H4).
- **N6. Stress-range form for the certainty standard (supports D3, decides nothing).**
  - TAP evaluated cover "growing up to a 6% inflation rate" (`tap26.txt:69`) and then listed its remaining risks (`tap26.txt:88-97`).
  - That is the professional form of FIX O3's third D3 option ("met even if yields fall N points and stay down").
  - For Laura the axis is reinvestment rates, not inflation (case:90). The level and the result go to the FR (IPS:68-69).
- **N7. Things professional IPSs contain that the team should NOT add:** benchmarks, fees, manager selection, proxy voting, securities lending, ESG screens, conflicts of interest, signatures, tax policy. Each is either out of scope (case:168-169), banned (FAQ:46-52), flagged as unsupported by the case in the 27 Sep assistant review (`research/team_materials/review_why_laura_and_public_profile.md:27`; the case names no values preference) [fixed 20 Oct, E12] or not asked (IPS:51-52). V5 correctly has none.

---

## 8. Still UNVERIFIED / limits

- (Vanguard *Principles* edition date removed from this list: it is dated © 2023, form ISGPRINC 112023; see the §1 VG row.) [fixed 20 Oct, E9]
- The CalPERS *Total Fund Investment Policy* text itself; TAP is cited only through the 16 Mar 2026 board item.
- SEC.gov pages (403); the investor.gov copy was used.
- Whether Wharton counts headings toward the 500 words (FIX §5); whether WInS-listed ETFs built on TIPS or STRIPS are banned (FIX S4).
- All "fit" and "strength / weakness" judgments in §5 are AI opinion. The professional sources describe institutions and generic individuals, not Laura; they are structure evidence, not evidence about the case.
- Word budgets are planning targets on the kit's strict counter (`office/tools/textcheck.py`), not measured drafts. Two-page fit is **UNVERIFIED** until a student draft is exported (FIX T4).

---

## Fixes not applied (checked copy, 20 Oct)

None of E1-E21 was rejected. Two were applied with a small adjustment because the evidence differs slightly from the fix text:
- **E10.** The fix says to cite `:81` for "growing wealth to ensure future flexibility". In `vg_pis_us.txt` that phrase runs across lines 81-82 ("simply growing" ends :81; "wealth to ensure future flexibility" is :82), so the second quote keeps `:81-82`. The first quote now cites `:67`, as the fix says.
- **E11.** The fix's wording says the AU copy has the "same title, author and date" as the US page. The US page returned 403 to both fetches, so its title, author and date cannot be compared either. The checked copy gives the AU copy's author and date with its line cite (`mstar_au.txt:167-168`) and marks identity with the US page **UNVERIFIED**.
