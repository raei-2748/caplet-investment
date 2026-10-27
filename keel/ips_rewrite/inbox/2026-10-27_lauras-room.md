# Laura's Room -> the rewrite, Tue 27 Oct 2026: WO-R7 and the price of a margin

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Full page:
`../../rooms/lauras_room/LR-04_price_of_a_margin.md`; numbers `LR-04_results.json` (MODEL, 22 Oct curve, 7.5% world
stocks, 200,000 paths; also with R05_joint's correlated shock). Simulated readers are tests, never quotes.

1. **LR-03 corrected.** The size of a committed lead moves giving (seed 10% -> 67% of goal: nearly sixfold, List &
   Lucking-Reiley 2002); the match ratio doesn't (Karlan & List 2007); announcing a lead gift beats matching (Huck &
   Rasul 2011; Rondeau & List 2008). So shaving the bottom has a price.
2. **Co-sponsors read a range the newsvendor way (WO-R7: yes).** The bottom is the only number their finance teams can
   count (ASU 2018-08: an "intention to give" is not recognised; CASE counts documented pledges); the top is an
   intention that moves no money. Make the bottom as big as it can honestly be; keep the top a rule.
3. **Don't pad the bottom today; mark it to market in 2031.** A fixed $10k margin (D1b) still breaks 0.11% of paths
   and taxes the signal by ~6.8% in every path (seed-study elasticity, heroic). Cutting the bottom in 2031 only by the
   coupon gap already visible then (net of the leftover and Laura's half) breaks **0 of 200,000** paths and cuts in
   8% of them, by $809 on average. Clearing houses call these initial and variation margin. The 2031 and 2033 gaps
   move together (corr 0.95). **Survives the joint run** (R05_joint's shock, rho 0.5, 6.5% stocks): 7 of 200,000
   breaks vs 0.23% for a fixed $10k. Keel's call: D1b becomes this rule (ASK_HUMANS, 27 Oct).
4. **Confidence to quote:** the chance of reaching the top, 69.9% (76.7% within $1k); implied over/under cost ratio 2.3.
5. Candidate line (AI DRAFT (Claude, 27 Oct 2026)): "In 2031 Laura names a bottom she already owns, less any gap the
   bond market has already shown her, and a top that is the floor plus half her stock fund. The bottom isn't a
   forecast; the top is reached about seven years in ten."

---

## Earlier note the same day (rewrite thread, 14:00ish; the web was blocked for it), kept as written
The 15:10 room run re-read its open items at source: List & Lucking-Reiley's abstract (sixfold), Karlan & List
(ratio), ASU 2018-08's text (barrier + right of return; "intention to give" not recognised) and CASE counting are now
VERIFIED (sources in `../../rooms/lauras_room/LR-04_price_of_a_margin.md` s2). Its wording caution stands: in the
fundraising text, say "we expect to add up to" plus the rule, never "only if stocks hold".

AI-generated (Claude Code), Laura's Room WO-R7 + newsvendor check, 27 Oct 2026

# Laura's Room (Amara): would co-sponsors read the range as intended? And the newsvendor check

**Honest status first.** WebFetch is blocked and the curl script returned 403 from the proxy for every site I tried
(catalog.upenn.edu, oid.wharton.upenn.edu, mheducation.com, a CPA-firm ASU summary, econpapers). WebSearch returned
page titles and URLs only, no text. So almost nothing below is confirmed from page text. I mark each claim:
CONFIRMED-BY-TITLE (the search result's title/URL shows it exists), or UNVERIFIED (my background knowledge, not
re-read today). A student should open the links before anything goes in the Final Report.

## Q1. Would the range be read as "bottom = commitment, top = conditional stretch"?

**(a) Accounting (ASU 2018-08 / ASC 958-605).** Sources exist (search hits, 27 Oct 2026):
https://bnncpa.com/resources/accounting-standards-update-2018-08-accounting-for-contributions ,
https://www.ksmcpa.com/blog/fasb-clarifies-scope-and-accounting-guidance-for-contributions-received-and-contributions-made ,
https://www.jrcpa.com/?p=21959 . From memory (UNVERIFIED today): a promise is *conditional* only if the donor's
agreement includes both a barrier the recipient must overcome (a measurable performance term, a limited discretion,
or a stipulation related to the purpose) AND a right of return of assets or right of release of the donor's
obligation. Unconditional promises are booked as revenue when made (at present value if long-dated); conditional
ones are not booked until the barrier is met. Applied to Laura: a bottom she already owns and commits is
unconditional. A top that rises only if stocks hold has no barrier the *recipient* must clear and no right of
return; it is a variable amount, not a condition in the ASU sense. Likely effect (UNVERIFIED, my reading, not a
professional opinion): the bottom is bookable; the market-linked top would be disclosed as a possible further gift
and not booked. That matches the plan's intent. Wording risk: if the fundraising text says "if stocks hold,
the facility will receive more", a lawyer could argue a stated condition; say "we expect to add up to" plus the
rule, and avoid "only if".

**(b) Capital-campaign practice.** I found no source I could read. UNVERIFIED general practice: campaigns announce
leadership gifts as a pledge total, often paid over 3-5 years; pledges are discounted for expected non-payment in
the books; a range or "up to" is common in early quiet-phase conversations, and a donor-stated floor is treated as
the countable amount. No contradiction with the plan found, but this is memory, not evidence.

**(c) Donor response to size.** CONFIRMED-BY-TITLE: List and Lucking-Reiley, "The Effects of Seed Money and Refunds
on Charitable Giving: Experimental Evidence from a University Capital Campaign", Journal of Political Economy
110(1), 215-233 (2002): https://econpapers.repec.org/article/ucpjpolec/v_3a110_3ay_3a2002_3ai_3a1_3ap_3a215-233.htm
and https://ir.vanderbilt.edu/items/350f62bd-7961-400b-becc-63ca8c9408f5 . The "10% to 67% of goal, nearly sixfold"
figure in the THINKING_LOG comes from The Window's note; I could not re-read it, so keep it UNVERIFIED until a
student reads the abstract. Important caveat (UNVERIFIED): that was a field experiment on *announced seed money as a
share of the goal*, with a computer-lab campaign, not on ranges. It supports "a larger announced committed amount
raises giving" and so supports not quoting the bottom too low. It says nothing about whether donors discount a
conditional top. Andreoni and Karlan-List (2007, match ratios) I did not search; I recall that larger match ratios
did not raise giving beyond a 1:1 match (UNVERIFIED), which, if true, cuts against "bigger announced numbers always
help" and gently supports a modest top.

**Does anything break the reading? Nothing found, but two cautions.** (1) The evidence is thin on *ranges*:
no study I located tests how donors weight the bottom against the top. A co-sponsor may simply anchor on the top.
The plan's defence is to lead with the bottom and state the top's rule in one clause. (2) The case itself says
over-promising "could damage her credibility" (Client Profile, "Communicating with Co-Sponsors"), so the case's
own readers weigh the downside; a lead sentence on what is owned matches that.

## Q2. Newsvendor and Laura's degree

- **Cachon and Terwiesch book.** CONFIRMED-BY-TITLE: "Matching Supply with Demand: An Introduction to Operations
  Management", Gérard Cachon, Christian Terwiesch, McGraw-Hill, now 5th edition
  (https://www.mheducation.com/highered/product/Matching-Supply-with-Demand-An-Introduction-to-Operations-Management-Cachon).
  UNVERIFIED: that both authors are Wharton faculty (my memory: yes, OID department) and that the book has a
  newsvendor chapter (my memory: yes, a standard chapter on it). Open the McGraw-Hill table of contents to confirm.
- **OIDD 6110 / OIDD 101 teaches newsvendor.** NOT VERIFIED. My search found no syllabus. Do not write "Wharton's
  core course teaches newsvendor" until a syllabus or course page is read.
- **OID as a Wharton department and concentration.** CONFIRMED-BY-TITLE: Penn catalog lists "Operations,
  Information & Decisions, BS: General Track" (https://catalog.upenn.edu/undergraduate/programs/operations-information-decisions-general-track-bs),
  and the department site is https://oid.wharton.upenn.edu/ ; Wharton's own pages list "Operations, Information &
  Decisions" (https://globalyouth.wharton.upenn.edu/?p=6720). So OID exists as a Wharton department/concentration.
- **"Statistics & Information Decisions Management" degree name.** The case says it (Client Profile line 16), but I
  could not find that exact name in any Wharton or Penn page. UNVERIFIED: it is not a Penn degree title I can
  confirm; it may be the case's blend of "Statistics" and "Operations, Information and Decisions". Do not claim OID
  is "the department behind" her degree; say only that the case names the field and OID is a real Wharton department
  whose name contains "Information" and "Decisions".

## Recommendation
Keep the range as designed. In the IPS use plain words ("the bottom is what she owns; the top is a rule we state").
Keep "newsvendor" to at most one clause, and not as a claim about what Wharton teaches, until a student verifies the
course. Before the Final Report: someone reads the ASU 2018-08 text (barrier + right of return), the List and
Lucking-Reiley abstract, and an OIDD syllabus.
