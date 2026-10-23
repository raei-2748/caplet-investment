## What set Wharton winners apart (2023–2026 seasons): lessons for Team Caplet (fact-checked)

**How this was sourced.** The network proxy blocked every official page. I confirmed this again today: WebFetch of globalyouth.wharton.upenn.edu/…/faq/ returned EGRESS_BLOCKED on 2026-09-27. The original author also reported these sites blocked: wharton.upenn.edu, talos.stuy.edu, delbarton.org, medium.com, newsbreak.com, hwchronicle.com and web.archive.org. Everything below comes from WebSearch result summaries retrieved 2026-09-27, plus the team's local official files. Summaries are paraphrases, so any "quote" should be checked against the original page. Publication dates are UNVERIFIED unless stated.

### What the sources say

**Results and cases by season**

| Season | Client and case (from search summaries) | 1st / 2nd / 3rd |
|---|---|---|
| 2022-23 | Peter Hjemdahl (W'19), social entrepreneur. About 1,400 final reports from 53 countries [S1]. Not re-checked. | DMV's Finest (Thomas Jefferson HS, VA) / Amity 7 Chakras (CT) / NovyPorg_1 (Prague) [S1]. Not re-checked. |
| 2023-24 | Hilary Ash. Finale April 20 in Philadelphia [S2]. Not re-checked. | Spark Investments (Bergen County Academies, NJ). 2nd and 3rd UNVERIFIED [S2] |
| 2024-25 | Ladi Ayoola (WG'22). Goals centred on impact for Nigerian youth [S3][S4]. **Re-verified:** 5,000 registered teams, 1,800 final reports submitted in December, Top 50 chosen in January [S3]. | **Re-verified:** BAM Investing (Deerfield Academy) won 1st [S3]. 2nd and 3rd (Finance from France; FA Quakers) not re-checked [S3]. |
| 2025-26 | Connor Barwin (WG'23), Make The World Better (MTWB). **Re-verified:** grow $500k to at least $1.5M by 2036; the focus was revitalising public spaces and community engagement in Philadelphia [S6]. "Facility construction" appears only in the original report and is UNVERIFIED. **Re-verified:** more than 6,300 teams registered at the start of trading on 2025-09-29 [S7]; the winners article says "nearly 6,000 teams competed" [S5]. **Re-verified:** virtual cash went from $100k to $500k, the first change since 2012 [S7]. | **Re-verified:** FigCapital (Stuyvesant) / HHA Investments (Colégio Marista de Brasília) / Riverhawk (Farmington HS, CT) [S5][S6]. The name appears as "Traders" in one summary and "Trades" in another, so the exact name is UNVERIFIED. The finale was April 25–26 [S5]. |

**How judging works**
- **Returns don't decide the winner.** Re-verified: "success is not determined by portfolio performance." Teams are judged on the quality of their strategy, how well it fits the client, the strength of their research, and how well they communicate and defend it [S9].
- **The IPS and Final Report decide the Top 50.** Re-verified: the Top 50 are chosen "based on the strength of their Investment Policy Statement (IPS) and Final Reports" [S7]. The original report cited [S8], the FAQ page; its wording was UNVERIFIED this pass.
- **Finale format.** A 10-minute pitch plus 5 minutes of Q&A before four judges [S4]. Not re-verified: my search found no timing details, so treat the format as UNVERIFIED for 2027.
- **2026 judges.** The original report placed them at Aberdeen, King Street, Zen Capital and WRDS [S5]. This was not re-checked and is UNVERIFIED.

**Advisors, judges and past teams** (all paraphrased by the search summaries, none re-checked)
- Teacher advisor Alex Lamon (2023): build the strategy first and pick stocks second. Check each stock against your thesis. "Winning isn't about portfolio gains. It is about having a coherent strategy." [S10]
- Wharton's strategy guidance: understand the client and make educated assumptions where details are missing. Develop a strategy and stick with it. Gains without a clearly stated strategy give "no shot at winning." [S11]
- Judge Melissa Ko Hahn: warns against "hiding behind fancy terms and formulas" and says "the best solutions are made up of simple, elegant ideas." [S12][S13] The year is UNVERIFIED.
- "Less is more / cut slides, cut words, cut minutes." Who said it is UNVERIFIED: one summary names judge Andrea Vittorelli [S12], another names Brian Z of DMV's Finest [S14].
- Judge Virgilio Aquino: "maintain the discipline of your investment process and be flexible when things don't work out." [S12] The year is UNVERIFIED.
- A third-party prep guide, not official, lists likely judge questions [S13].

**UNVERIFIED:** I found nothing on the winning teams' allocations, report contents or judge feedback on them.

**Local official 2026-27 files (checked against the files today)**
- **Five scoring areas [L1], all confirmed:**
  - Investment Strategy
  - Client Knowledge and Objectives
  - Portfolio Analysis, which covers "funding reliability, the facility contribution, and financial flexibility under varying market outcomes"
  - Articulation of Competition Experience
  - Creativity and Presentation, which covers communicating "to prospective co-sponsors clearly and credibly"
- **What the case requires [L2], all confirmed:**
  - Define "high degree of funding certainty" and explain how it was evaluated.
  - Size the operating reserve and say how its composition changes over time.
  - Give a dollar range for the facility contribution, with a stated confidence level.
  - Draft part of the co-sponsor fundraising materials.
  - Leave WInS gains and losses out of the projections.
  - "Evaluators will consider the three deliverables together."
  - Taxes and Taiwan's legal and regulatory rules are out of scope.
  - Teams do not estimate the facility cost.
- **Deadlines [L1]:**
  - Roster: October 9
  - Trading Notes: October 23
  - IPS: November 6 (trading locks)
  - Final Report: December 4 (all at 5:00 p.m. ET)
  - Final Report instructions come out November 9.

### Inference: 10 lessons for a liability-funding case

1. **Lead with the liability, not the stock picks** [S9][S10]. Show the timeline first: $300k at the start of 2027, $150k at the start of 2028, the reserve set aside at the start of 2033, then ten $50k payments from 2033 to 2042 [L2].
2. **Put a number on "high certainty"** [L2]. Something like "≥95% Monte Carlo probability plus a deterministic floor" works. The 95% is our choice, not a rule.
3. **Size the reserve from a present value.** Value the ten payments at the start of 2033, with the first payment made right away (an annuity-due), because the profile says the reserve is set before the first payment [L2]. I recomputed this in Python:
   - $439,305 at 3%
   - $421,767 at 4%
   - $405,391 at 5%

   These match the original figures. The discount rates are illustrative, not current market yields: actual Treasury yields are UNVERIFIED.
4. **Use the 2026 case as a precedent.** It was a mission-driven, target-growth case [S6]. This year's case adds an explicit reliability analysis, so a pitch that only maximises returns is probably not enough.
5. **Keep it simple** [S12]. Use three buckets:
   - growth to 2031
   - a glide path from 2031 to 2033
   - the reserve from 2033 to 2042
6. **Make the co-sponsor range a centrepiece** [L1][L2]. Tie the range to percentiles, add a sensitivity table, and write a draft paragraph in Laura's voice.
7. **Keep the Trading Notes, IPS and Final Report consistent.** They are evaluated together [L2], and the IPS feeds the Top-50 selection [S7].
8. **Rehearse client-specific Q&A** on rate shocks and inflation. The format is UNVERIFIED. The payments are fixed nominal dollars [L2], so any TWD/USD point should be framed as a flexibility issue, not a funding risk.
9. **Tell Laura's story.** Link her themes of identity and belonging to the purpose of the residency [L2].
10. **Set de-risking triggers in advance**, following Aquino's advice on discipline and flexibility [S12].

### Verification notes
- **Re-searched on 2026-09-27:**
  - 2026 podium, team and finale dates: confirmed.
  - BAM win and the 5,000 / 1,800 counts: confirmed.
  - "Not determined by portfolio performance": confirmed on [S9].
  - Top-50 selection on IPS and Final Reports: confirmed, now cited to [S7].
  - MTWB $500k→$1.5M by 2036 and 6,300+ registered: confirmed.
  - $100k→$500k virtual cash: confirmed.
- **Changed:**
  - Added that the winners article says "nearly 6,000 teams competed" alongside the 6,300+ registered.
  - Marked Riverhawk's exact team name as UNVERIFIED.
  - Marked "facility construction" in the MTWB case as UNVERIFIED.
  - Marked the finale format and the 2026 judges' firms as not re-verified.
  - Added the local deadlines and the scope exclusions.
  - Explained that the PV figures assume the first payment is made immediately, and marked the discount rates as illustrative.
- **Python check:** the start-of-2033 PV (first payment immediate) matches the original. If the first payment were one year later, the values would be $426,510 / $405,545 / $386,087.
- **Blocked:** a WebFetch of globalyouth.wharton.upenn.edu returned EGRESS_BLOCKED.

### Sources
Retrieved 2026-09-27 via WebSearch summaries (page bodies blocked):
- [S1] https://globalyouth.wharton.upenn.edu/news/the-2023-investment-competition-global-finale-ends-in-sweet-victory-for-dmvs-finest/
- [S2] https://globalyouth.wharton.upenn.edu/news/spark-investments-bergen-county-academies-new-jersey-bring-the-heat-to-the-2024-investment-competition-global-finale/
- [S3] https://globalyouth.wharton.upenn.edu/news/bam-investing-from-deerfield-academy-massachusetts-wins-the-2025-wharton-global-high-school-investment-competition/
- [S4] https://globalyouth.wharton.upenn.edu/investment-competition/previous-winners/case-study-for-2024-2025/
- [S5] https://globalyouth.wharton.upenn.edu/news/2026-investment-competition-global-champions/
- [S6] https://www.scribd.com/document/965855349/Case-Study-Wharton-Global-Youth-Program
- [S7] https://globalyouth.wharton.upenn.edu/news/a-winning-season-thousands-of-teams-bigger-stakes-and-the-top-50-2026-investment-competition-teams-revealed/
- [S8] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/ (WebFetch blocked)
- [S9] https://globalyouth.wharton.upenn.edu/competitions/investment-competition/
- [S10] https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/
- [S11] https://globalyouth.wharton.upenn.edu/developing-strategy/
- [S12] https://globalyouth.wharton.upenn.edu/news/top-teams-sail-to-success-in-the-2022-wharton-investment-competition-global-finale/ (which page each quote comes from is UNVERIFIED)
- [S13] https://en.wghs.org.cn/news/100.html (third-party)
- [S14] https://globalyouth.wharton.upenn.edu/news/wharton-investment-competition-tales-from-the-2023-teams/

Local files:
- [L1] /home/user/caplet-investment/competition/official/2026_27/SMApply_Deliverables_Page_2026-09-27.md
- [L2] /home/user/caplet-investment/competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt