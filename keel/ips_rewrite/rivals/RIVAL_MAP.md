# The rival map: what 36 simulated rival IPSs say, so Caplet XR can say what they don't

> **Read `../../BIBLE.md` first.** This page feeds the rewrite. It drafts no IPS prose.

AI-generated (Claude Code), Tue 27 Oct 2026, night (Sydney), thread "Out-think every rival team for semis". The rival
texts are simulations, not real teams. They are here so Caplet can avoid the crowd, never to copy from.

## Result
**The strategy V25 runs on is the field's default answer.** All twelve rivals written by a fresh AI from nothing but
the case, the instructions and the permitted list (four each from Haiku, Sonnet and Opus, with four kinds of student
prompt) reached the same plan: a Treasury ladder matched to the ten payments, bought first and held to maturity, with
everything else in diversified stocks for the facility. Eleven of the twelve then step the stocks down toward 2031-2033.
Eight say the only risk left is a US government default. Five of the twelve names contain "Promise". One of them
(A09, Opus, from a one-line prompt: "We want to win") reproduces V25's contribution rule almost exactly: the floor
locked in Treasuries maturing before 2033, plus at most half the stocks, capped at the top of the range, with the rest
kept as Laura's flexibility. The simulated near-twin (H19: iBond ladder + VT + promised minimum) says most of V25's
substance in a cleaner, more impersonal voice.

So **structure is table stakes, not an edge.** Hundreds of real entries will open with some version of "secure the
promise, then grow the surplus". What only Caplet has, after reading all 36:

1. **Human capital as a reason for the order of purchase:** her 2028 money shrinks in the same slump that makes bonds
   dearer. 0 of 36 rivals say it. The nearest is "her income is irregular" (A11).
2. **The range set by weighing two costs** (over-promising judged about three times worse than under-promising, so the
   top sits where it is reached about three times in four). 0 of 36. The rivals set a "bad market" bottom and a
   "median/strong market" top, or a percentile, without saying why there.
3. **Certainty defined by where it breaks.** The rivals' "only a default can stop it" is false for a coupon ladder.
   See s3 and R06 D6.
4. **The stock share rises as the payments are made, with no trade.** 25 of 36 do the opposite, on purpose (H03:
   "Risk falls as her ten $50,000 payments approach, and keeps falling as they are paid"). See R06 D1.
5. **One test on fixed dates as the decision framework.** Only H23 has a funding ratio, and it uses bond funds and
   yearly rebalancing. See R06 D2.
6. **XR.** No rival has a pharmacology motif or a name that is also the team's name.

**What V25 shares with the crowd** (and so cannot rely on): debts vs hope (A12: "a hope"; H09: "a debt with a date on
it"), pay the payments first, the 2028 deposit fills the gap, inflation hurts the facility and not the fixed payments
(18 of 36), keep part for flexibility (22 of 36), ladder held to maturity (23 of 36). Each can stay as a fact, but none
can be the hook.

## 1. Method and its limits
- **A01-A12, raw AI:** fresh agents told to read only `kit` copies of the case, the updated IPS instructions and the
  permitted list (Book 6), and to ignore any project context. Prompts in four styles, the same four for each model:
  "write it, we want to win"; "give it a creative name, stand out"; "act as a CFA charterholder"; "use an extended
  metaphor, sound human, not AI". Models: Haiku 5.5 (A01-04), Sonnet 5.5 (A05-08), Opus 5.5 (A09-12).
- **H01-H24, human archetypes:** three Opus agents, each writing eight strong teams from a brief (bucket, CFA template,
  glide path, endowment, core-satellite, values, quant, barbell, pure matcher, dividends, two pots, graphic novel,
  inflation, risk parity, safe withdrawal rate, momentum, bridge, anchor-and-sail, the iBond near-twin, CPPI,
  lead gift, Messy Roots garden, LDI immunisation, staged commitment), with realistic slips noted at the bottom of each
  file.
- **Limits.** (a) Simulated, not real: the archetypes are our guess at the field. The raw-AI set is the stronger
  evidence, because AI-assisted teams will literally get these answers. (b) The agents ran inside this repo, whose
  project file mentions Caplet's plan. They were told to ignore it, but some leakage can't be ruled out (A09's
  closeness is the one to doubt). Even so, the same structure appears across all three models and all prompt styles,
  which looks like a real attractor. (c) `tally.py` counts keywords, so it is a floor. The rows that matter most were
  re-read by hand: for the raw-AI set, "only default" is 8/12 (the keyword count finds 5), and stepping the stocks down
  is 12/12 by hand (11 by keyword; A12 says "ink the pencil gradually").

## 2. What everyone says (36 rivals; `tally.json`, by keyword; hand counts in brackets)
| Move | All 36 | Raw AI (12) | Human (24) |
|---|---|---|---|
| A Treasury ladder matched to the payments | 26 | 12 | 14 |
| Held to maturity | 23 | 11 | 12 |
| Stocks stepped DOWN toward 2031-2033 (glide, reef, harvest, lock gains) | 25 | 11 (12 by hand) | 14 |
| Keep part of the surplus for flexibility | 22 | 9 | 13 |
| Inflation hits the facility, not the fixed payments | 18 | 7 | 11 |
| Laura's credibility with co-sponsors | 15 | 9 | 6 |
| The 2028 deposit completes the ladder first | 14 | 10 | 4 |
| Certainty = "only a US default could stop it" | 9 (13+ by hand) | 5 (8 by hand) | 4 (5+) |
| A metaphor frames the plan | 17 | 7 | 10 |
| "Promise" in the name or pitch | 12 | 8 | 4 |
| Range bottom = an amount already locked | 11 | 3 | 8 |
| Coupon reinvestment named at all | 10 | 6 | 4 |
| A probability for the payments (95% etc.) | 8 | 0 | 8 |
| Annual review or rebalancing | 31 | 10 | 21 |
| **Contribution capped at the top of the range** | 4 | 1 | 3 |
| **Longest-dated payments bought first** | 3 | 1 | 2 |
| **Defined-maturity iBond funds** | 2 | 0 | 2 |
| **Sequence-of-returns risk** | 1 | 0 | 1 (H15, as a reason for a bond tent in a 60/40) |
| **Funding ratio** | 1 | 0 | 1 (H23) |
| **Her income moves with markets (human capital)** | 0 | 0 | 0 |
| **Over- vs under-promising weighed as two costs** | 0 | 0 | 0 |

## 3. How the rivals define "high certainty"
Three families, and V25 should beat all three in one clause:
- **"Only a US default"** (A01, A05-A09, A11, A12, H05, H11, H12, H19, H24 and others): every payment has a Treasury
  maturing before it, held to maturity. This is false as stated: coupons are reinvested at unknown rates, and the
  ladder may cost more than the first deposit (K2: 47% of model paths). Most rivals don't mention coupons at all.
- **A probability** (H07 "at least 95% of 10,000 simulations", H18 95%, H21 97%, H15 a 95% backtest): honest, but it
  admits a 1-in-20 or 1-in-30 broken promise, and Book 7 doesn't want the calculations in the IPS.
- **A funding ratio** (H23, at least 105% each January): the most professional, but it is held in bond funds and
  rebalanced, so it leaks.
- **V25:** where it breaks (yields more than 2pp lower before the build AND the 2028 deposit more than halved), plus
  one named soft spot (coupons, fixed in January 2033). That is the only definition in the field that tells the judge
  something they didn't know.

## 4. Names and motifs (Book 2's groupthink fear, measured)
- **Names:** Promise First (A05, H19), Promise First, Growth Second (A07), Promise First, Then Grow (A09), Fund the
  Promise, Then Grow (A03), Protect the Promise, Grow the Vision (A11), Three Acts, One Promise (A06), Lock the Ladder,
  Grow the Surplus (A01), Match First (H09), Lock & Launch (H05), Foundation First, Then the Garden (A08). "X first,
  then Y" is the house style.
- **Motifs:** sailing (A04 Ballast and Sail, H18 Anchor and Sail), building (A08 house and garden, H17 bridge),
  **roots** (A10 Roots & Wings, from a raw Opus prompt; H06 Rooted & Rising; H22 Deep Roots), **graphic novel ink and
  pencil** (A12 Pencil and Ink, H12 Ink Before Colour, found independently), buckets and pots (H01, H11), lanterns
  (A02), theatre acts (A06), seasons (H14), startup runway (H24).
- **So:** Ahaan's warning about roots (Book 2) is confirmed: 3 of 36, one of them unprompted. The graphic-novel motif
  is the obvious "Laura" motif and two rivals found it. **R must not be "runway"** (H24 uses it for the payments; it
  was the Sonnet rung's runner-up, `../../loop/CHAMPIONS.md` C2). No rival has anything medical, pharmacological or
  named after the team. XR is clear.

## 5. How the rivals set the 2031 range
- Bottom = an amount moved into short Treasuries in 2031 (A02, A05, A08, A09, A11, A12, H21, H24); top = what the stocks
  might add, "strong market" or "median". **Selling stocks in 2031 to make the bottom is the crowd's move.** V25 buys
  its floor in January 2028, before a single share, so its bottom doesn't depend on 2028-2031 markets.
- A percentile of simulated outcomes (H07, H14, H23: a 90% lower end). The floor is then a probability, not an
  amount owned.
- **None says why the top sits where it does.** V25's two-cost reasoning (a top reached about three times in four
  because over-promising is about three times worse) is the only argued range in the field.
- **Co-sponsor framing:** H21 (a firm lead gift plus a matching pledge) is the strongest rival idea on co-sponsors, and
  belongs to the Final Report. Note that R05 #17 warns that a conditional pledge can count as "conditional" under US
  nonprofit accounting. H21 walks straight into it.

## 6. The most dangerous rivals
| Rival | Why it is dangerous | Where V25 still beats it |
|---|---|---|
| A09 (raw Opus) | Same contribution rule as V25 (locked floor + at most half the stocks, capped) | It sells stocks in 2031 to make the floor; "only default" certainty; no human capital; no reason for the range |
| H19 (near-twin) | iBond ladder + VT + promised minimum, very clean | Says the ladder costs "a little under $300,000" (a coin flip); no coupons; no range logic; impersonal |
| A12 / H12 (ink and pencil) | The motif judges will find charming, tied to Laura's own craft | Decoration over a crowd plan; both glide down |
| H23 (LDI) | Real pension vocabulary: PV, duration, funding ratio | Bond funds leak (convexity, twists); a 90% lower end makes the bottom a probability |
| H21 (lead gift) | The best co-sponsor idea in the field | A conditional match is legally "conditional"; IEF reserve has rate risk until 2031 |
| H24 (staged) | Fresh real-options frame, startup voice | Tranches after 2033 stretch the case; "runway" |

## 7. Ranked moves for the rewrite (strategy and emphasis only; prose stays with the rewrite thread)
1. **Don't let the hook be the crowd's sentence.** "Debts paid with debts / promise vs hope / buy the cheques first"
   is what every one of the 12 AI pitches leads with, in some form ("secure the payments first, then grow"). Keep the idea; lead with something only Caplet can say. Candidates,
   strongest first: (a) **everyone else de-risks at the end; Caplet XR de-risks at the start, and then risk rises by
   itself** (R06 D1); (b) certainty defined by where it breaks, against a field that says "only a default"; (c) the
   range as a choice between two costs.
2. **Make the framework one rule a judge can point to** (R06 D2): one test, three Januaries. It answers Book 7's W4,
   and only one rival has anything like it.
3. **Promote human capital.** 0 of 36 rivals have it, and it is V25's best client-knowledge line.
4. **Say the cap and why** (R06 D5). 4 of 36 cap the contribution; none explains that above the cap every dollar is
   Laura's flexibility.
5. **Say the floor was bought in 2028, not harvested in 2031.** That is the real difference from A09 and from the
   rivals' "bottom = what we lock in 2031". It is also the static form of contingent immunisation (R02 reading list).
6. **Spend no kicker on inflation.** The idea is in 18 of 36; only V25's wording is distinctive.
7. **Name the residency's people.** Only 2 of 36 rivals name artists or writers. The Shark Tank stakes beat is open
   ground (`../reviews/V25_shark_tank.md`).
8. **Motif guardrails:** no ink or pencil, nothing roots, no buckets or pots, no anchor or sail, R never "runway".
9. **No probability for the payments.** 8 of 36 quote 95%. V25 is right to avoid it.
10. **Statistics at Wharton:** two rivals (H07, H23) use Laura's degree as a hook. If Caplet uses it, it must do more
    than flatter.

Files: `A01.md`-`A12.md` (raw AI), `H01.md`-`H24.md` (human archetypes, with simulator notes), `tally.py` /
`tally.json` (counts), `../reviews/2026-10-27_rival_panel.md` (V25 judged blind in this field).
