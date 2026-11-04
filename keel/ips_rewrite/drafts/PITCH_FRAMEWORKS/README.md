# Pitch Frameworks — AI DRAFT (Claude, 4 Nov 2026)

Five frameworks for the 50-word elevator pitch, borrowed from Hollywood, trial law and NASA
rather than Wall Street. Each draft is ≤ 50 words. **All need rewriting in the team's own
words and GPTZero checking before use.**

Status: drafts for team review. None selected yet.

---

## 1. THE COLD OPEN — from screenwriting (recommended)

**Technique:** TV dramas open on the crisis, not the backstory. The audience is dropped into
the worst moment, then shown the characters survive. A judge reads "shares crash forty
percent" and switches from skimming to stress-testing. Then "every payment still arrives"
forces them to read the plan.

> Shares crash forty percent the year before Laura's first cheque. Every payment still
> arrives. Her first $300,000 buys ten Treasuries, one maturing before each January. Her
> 2028 deposit sets a minimum building gift, and only its interest goes into shares. The
> crash shrinks the gift, not the cheques. **(48 words)**

Strongest move: "The crash shrinks the gift, not the cheques." One sentence tells the judge
exactly what is protected and what is not.

Risk: the plan's real weakness is falling interest rates, not a share crash. The IPS body
must say so on the page; no one answers a judge's questions before the semifinal.

---

## 2. THE PRE-MORTEM — from NASA

**Technique:** Before every launch NASA runs a pre-mortem: assume the mission failed, work
backwards to the cause. The pitch names the failure mode, then shows the team eliminated it.
Signals the team stress-tested the plan, not just designed it.

> **Fact check (daily loop, 5 Nov):** not true as worded. A US default is not the only way to miss a payment: the FINAL says falling reinvestment rates can leave the ladder short, and the 2028 deposit may have to complete it (`../FINAL/ips.txt` P7; `../FINAL/LOOK_ALIKE_CARD.md` section D). This version also uses "cheque" and "minimum building gift", which Ray banned (I83).

> We asked what would have to go wrong for Laura to miss a cheque. Answer: the US Treasury
> defaults. Her first $300,000 buys ten Treasuries, each maturing before a January payment.
> No share needs to rise. Her 2028 deposit sets a minimum building gift; only its interest
> buys shares. **(49 words)**

Strongest move: "Answer: the US Treasury defaults." Five words that prove the payments are
as certain as anything in finance can be.

---

## 3. THE VERDICT — courtroom closing + reframe

**Technique:** A prosecutor opens with the verdict, then shows the evidence. "Laura already
has enough" is the verdict. Everything after is proof. The pair "No share needs to rise; no
market needs to recover" reframes the portfolio: it says what the plan does not need.

> Laura already has enough. At today's rates, her first $300,000 buys ten Treasuries, each
> paying one January cheque from 2033 through 2042. No share needs to rise; no market needs
> to recover. Her 2028 deposit sets a minimum building gift, and only the interest it would
> earn goes into shares. **(50 words)**

Strongest move: "Laura already has enough." Three words that reframe the whole competition
— the payments are not a growth problem, they are a preservation problem.

---

## 4. THE HEIST — from Ocean's Eleven

**Technique:** A heist film explains the plan by giving each person one job. "You drive. You
crack the safe." Each part is one sentence, complete on its own. The audience remembers the
plan because it is three things, not one complicated thing.

> Laura's money has three jobs and each dollar does exactly one. Her first $300,000 buys ten
> Treasuries, one per January cheque. Her 2028 deposit buys a Treasury floor for the
> building gift. Only that floor's interest goes into shares: the upside comes free and a
> crash can't reach the rest. **(50 words)**

Strongest move: "Each dollar does exactly one." Judges penalize complexity; this line
promises the opposite.

---

## 5. THE CROSS-EXAMINATION — from trial law

**Technique:** A trial lawyer builds the closing on questions the jury already answered yes
to. Each is so obvious the jury nods. The conclusion feels inevitable. (Irving Younger's
"Ten Commandments of Cross-Examination," 1975.)

> Can the US Treasury pay its debts? Then Laura's cheques arrive: her first $300,000 buys
> one Treasury per payment. Will her 2028 deposit buy a Treasury? Then her minimum building
> gift is set. Could shares fall? Yes, but only the floor's interest is exposed, so only the
> upside shrinks. **(49 words)**

Strongest move: three questions, three obvious answers, three parts of the plan proven.

Risk: most stylistically unusual. A judge who dislikes the tone may find it gimmicky; a
judge who likes it will remember this team out of hundreds.

---

## Ranking

| Rank | Framework   | Opens with        | Strength                                          |
|------|-------------|-------------------|---------------------------------------------------|
| 1    | Cold Open   | The crisis        | Judge can't skim; plan proves itself under fire    |
| 2    | Pre-mortem  | The failure mode  | Signals stress-testing, not just design            |
| 3    | Verdict     | The conclusion    | "Already has enough" reframes the whole competition|
| 4    | Heist       | The structure     | Clearest, easiest to remember, most conventional   |
| 5    | Cross-exam  | Three questions   | Most memorable if liked, most risky if not         |

## Notes

- Frameworks are modular: the Cold Open's first two sentences work with the Heist's
  three-job body, or the Verdict's opening with the Pre-mortem's failure mode.
- Book 10 bans "every team will …". None of these drafts names other teams.
- The current IPS pitch (V57) should be compared against these before choosing.
- The pitch and the IPS body must tell the same story; changing the pitch may require
  small adjustments to the IPS's opening paragraph.

---

## Insight-led pitch (Ray, 4 Nov: "open with our most original insight, build on it")

AI DRAFT (Claude, 4 Nov 2026). The insight: Laura's 2028 money comes from "publishing advances,
speaking engagements, licensing, and other entrepreneurial ventures" (case, p.1), income that
tends to fall when shares fall. The case lists the sources; the link to markets is our
reasoning. Everything else in the plan follows from it: no promise (cheque, or the 2031 range)
may depend on shares or on her career.

**Lead (50 words)**
> When shares fall, Laura's book advances and speaking fees tend to fall with them, so we never
> let a promise depend on either. Her first $300,000 buys ten Treasuries, one per January cheque
> from 2033. Her 2028 deposit buys a minimum building gift, and only its interest goes into shares.

**Alt A (49 words)**
> Laura's book, speaking and licensing income can dry up in the same downturns that sink shares,
> so her portfolio never needs both to recover. Her first $300,000 buys ten Treasuries, one per
> January cheque. Her 2028 deposit buys a minimum building gift, and only its interest goes into shares.

**Alt B (50 words)**
> Laura's career already rides on good times: book advances, speaking fees and licensing shrink
> when markets fall. So no cheque depends on shares. Her first $300,000 buys ten Treasuries, one
> maturing before each January payment. Her 2028 deposit buys a minimum building gift, and only
> its interest goes into shares.

Checks: word counts by `split()`; not yet checked in GPTZero; team rewrites in its own words.
"Tend to" stays because the case lists the income sources but does not say they fall with
markets; the claim has to hold on the page alone (INSTRUCTIONS I82).
