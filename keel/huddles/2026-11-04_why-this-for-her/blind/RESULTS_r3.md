# H-032 second blind read: results, key unsealed (Amara, cold judge, Wed 4 Nov 2026, round 3)

> Real test, AI readers: three fresh outside model calls (professor Opus 5.5, speed judge Sonnet 5.5, Year 11 Haiku 5.5),
> not Keel members. (Keel is a simulated team, AI-written.) Scored against my registration (`REGISTRATION.md`, written
> in round 1, not changed since), with the same two resolutions I declared in `RESULTS.md`, and the chair's rules for
> this read, registered at 18:50 before it ran (`../chair.md`, "Round 2 tally and round 3"). The answers are stamped
> about 18:55. Texts checked before scoring: each packet's five versions match the arm files word for word (sha256
> prefixes of the files: A_FINAL `b9368f5b5fa9ffc5`, the same file as round 1; E `5b54d923c71680be`; F
> `1a3bfe1009b73209`; G `3f66b903a9eb1815`; H `e2631c772dbc37b2`). Strict counts (`textcheck.py`, the larger): final
> 495, E 497, F 497, G 497, H 493. As in round 1, the packets hold only the texts; the questions and case summary went
> in the chair's prompt, which isn't filed, so I can't check those word for word against my registration.

## The key, unsealed
| Reader | Final | E (Jun, Felix) | F (Kai) | G (Tess) | H (Nora) |
|---|---|---|---|---|---|
| A2, professor | P | N | V | B | G |
| B2, speed judge | D | V | Y | L | J |
| C2, Year 11 | J | N | S | B | V |

All four change P3 only. Against the final, word by word:
- **E:** "which never needs rebalancing" becomes "so no cheque depends on what a bond sells for that January"; cuts "as rates move", "exactly" and "to us,". (10 words out, 12 in.)
- **F:** the same new clause; cuts "either", the "January" of "In January 2027", "exactly", and "So, to us," (the sentence now starts "High certainty"). (10 out, 12 in.)
- **G:** the same new clause; cuts "exactly", "whatever markets do" and "to us,". (10 out, 12 in.)
- **H:** cuts ", to us," and nothing else. (2 out.)

## How I scored: the two round-1 resolutions, and one new call
1. **Q2**, as in round 1: 3 = names nothing, 2 = names only lines outside P3. Every reader named the closing line in
   every version this time, so no cell scores 3.
2. **Q3 is scored on P3**, as in round 1. "Treasury funds with fixed end dates" is in P3 but word for word the same in
   all five, so its flag counts in every version and can't move a comparison. Flags on other paragraphs are listed
   at the end. I checked the other way too: scoring each version's worst flag across the whole text moves some cells
   (the professor's shared flags on P7 and P8 would pull G to 1; the speed judge's "takes a second read" on P7,
   written once under E, would pull E to 1), but no arm falls behind the final for any reader, so no line of the bar
   moves.
3. **New: readers who answered "same".** The speed judge wrote the reason out once (under E, read first), then wrote
   "The same plan:" for the final and "Same plan and same reasoning" for G, H and F, and said in Q4: "The versions
   barely differ on understanding." The Year 11 wrote "Same logic as J" (H, J being the final), "The same logic" (G)
   and "The same logic as S and B" (E). Where a reader says two versions share the same logic, I give them the same Q1
   score, at the fullest statement of it that reader wrote. That's round 1's rule (a back-reference inherits the
   answer it points to) applied to answers that point at all the others. The professor told the versions apart in so
   many words, so I score the professor cell by cell.
   **This call decides tonight, so I'm saying it out loud.** Read the speed judge cell by cell instead, with "same
   reasoning" pointing past the final back to that reader's answer under E, and G beats the final with the speed
   judge 3 v 2 and clears (a) and (d). I don't read it that way, because the same reading scores H, the final's own
   P3 but for ", to us,", 3 against the final's 2 for "Same plan, same reasoning". Read cell by cell with the nearest
   earlier answer, only E (read first) gains, and it still wins one reader. The other close calls (the professor's Q1
   for F, E and the final, the Year 11's for F) give no arm a second reader on Q1 whichever way I take them.

## Scores, per reader (0-3, against the registered key)

### A2, professor
The professor listed the problems shared by all five once, under V. The shared P3 one, "'Treasury funds with fixed
end dates' is unexplained jargon, and a fund's final payout is not fixed the way a bond's is", scores 2 in every
version: true, and the sentence doesn't claim a fixed payout.

| Version | Q | Score | Why, in the reader's words |
|---|---|---|---|
| Final (P) | Q1 | 2 | "As G": "The same plan, but the reason given for one bond per payment is the team's convenience ('never needs rebalancing'), not the benefit to Laura." Her fit only from the plan set out under V (her income "dries up in the same downturns that sink shares"), as in round 1. |
| Final (P) | Q2 | **0** | "'So, to us, high certainty means no payment depends on shares.' The 'to us' is throat-clearing before the line lands." |
| Final (P) | Q3 | **0** | "The same two problems as G: 'never needs rebalancing' is untrue, and 'exactly' overclaims for the funds." The "exactly" reason holds; the "never" reason doesn't (ruling below). |
| E (N) | Q1 | 2 | "The same plan. The paragraph ends 'So high certainty means...', which presents the definition as following from how a bond behaves." Points back to V. |
| E (N) | Q2 | 2 | "Only the shared closing line." |
| E (N) | Q3 | 1 | "Unclear: ... 'and rebalancing'. Rebalancing for what reason? Without 'as rates move', a reader can't see why that method needs constant upkeep. That upkeep is the whole reason to prefer one bond per payment." The words E cut to pay for its clause. |
| F (V) | Q1 | 2 | "so the payment never depends on what a bond sells for on the day, or on shares. This suits Laura because her own income (advances, speaking, licensing) dries up in the same downturns". Her facts, but the why is the new clause handed back nearly word for word, not set against the other method (as round 1's speed judge on Felix's: 2). |
| F (V) | Q2 | **0** | "In V only, 'High certainty means no payment depends on shares.' stands on its own without 'So', so it reads as a slogan rather than a conclusion." A sentence F changed, with a reason. |
| F (V) | Q3 | 1 | "'In 2027' is vaguer than 'January 2027', and that matters for a ladder built around January dates." |
| G (B) | Q1 | **3** | "it keeps the reason the other method needs rebalancing, and it states the benefit in Laura's terms: no cheque depends on a sale price that January." In Q4, in the reader's own words: "the exact risk being removed, which is having to sell at whatever price that January offers." |
| G (B) | Q2 | 2 | "Only the shared closing line." |
| G (B) | Q3 | 2 | "Nothing beyond the problems shared by all five. Dropping 'whatever markets do' costs nothing ... and the shorter claim is harder to attack." |
| H (G) | Q1 | 2 | "The same plan, but the reason given for one bond per payment is the team's convenience ('never needs rebalancing'), not the benefit to Laura." |
| H (G) | Q2 | 1 | "'We do the second, which never needs rebalancing.' It reads as a mic-drop." A P3 line called a punchline with no reason; my key needs one for 0. A 0 would move nothing: the final scores 0 with this reader, and it isn't the sentence H changed. |
| H (G) | Q3 | **0** | "Untrue: 'never needs rebalancing' ... Also an overclaim: 'pays exactly what it promised' is true of a single bond, but the ladder also holds funds whose end value is not promised." |

### B2, speed judge
| Version | Q | Score | Why, in the reader's words |
|---|---|---|---|
| Final (D) | Q1 | 3 | "The same plan: ten bonds, one per cheque, bought up front. It suits Laura because the cheques are fixed and her top-up money is unreliable in a crash." With "The versions barely differ on understanding", scored at the reasoning written out under E (note 3). |
| Final (D) | Q2 | 1 | "'So, to us, high certainty means…' also sounds a little staged." Mild, like round 1's "a bit like a stated definition". |
| Final (D) | Q3 | 1 | "'Pays exactly what it promised, whatever markets do' and 'which never needs rebalancing' are overclaims. The plan itself later admits it relies on reinvesting interest and can fall short. That makes 'exactly' and 'never' untrue as stated, or at least contradictory." "Untrue" fails the facts; "contradictory" stands as unclear (ruling below). |
| E (V) | Q1 | 3 | "Each of the ten cheques gets its own Treasury maturing just before its January, so nobody has to sell anything in a bad market. That suits Laura because the money is a fixed promise ... Her extra income ... is the part most likely to dry up in a downturn". |
| E (V) | Q2 | 2 | "'Like the tablet it is named after ...' This is the winding-up-for-a-punchline line." |
| E (V) | Q3 | 3 | "Nothing untrue." The reader's two notes are on P5 and P7. |
| F (Y) | Q1 | 3 | "Same plan, same reasoning." |
| F (Y) | Q2 | 2 | "The closing tablet line." |
| F (Y) | Q3 | 3 | "Nothing untrue. 'Whatever markets do' is a mild overclaim given the reinvestment caveat. 'In 2027' is vaguer than 'January 2027', but that doesn't matter to a skimmer." Quibbles; the overclaim's reason fails the facts (ruling below). |
| G (L) | Q1 | 3 | "Same plan and same reasoning." |
| G (L) | Q2 | 2 | "The closing tablet line." |
| G (L) | Q3 | 3 | "Nothing. This is the cleanest claim. 'Pays what it promised' has no 'exactly' and no 'whatever markets do'. The promise still sits a little awkwardly beside the later reinvestment admission, but it doesn't overclaim." |
| H (J) | Q1 | 3 | "Same plan, same reasoning." |
| H (J) | Q2 | 2 | "The closing tablet line." |
| H (J) | Q3 | 1 | "'Pays exactly what it promised, whatever markets do' and 'never needs rebalancing' overclaim, for the same reason as D. They contradict the later shortfall paragraph." |

### C2, Year 11
| Version | Q | Score | Why, in the reader's words |
|---|---|---|---|
| Final (J) | Q1 | **3** | "Each January cheque is matched by a Treasury that matures before it, so the cash is there on the day and nothing has to be sold. ... which suits Laura because a fixed bill cannot wait for a market recovery." A 3 from the Year 11 again, as in round 1. |
| Final (J) | Q2 | 2 | "'Like the tablet it is named after ...' This is a neat closing gag built on the tablet joke." |
| Final (J) | Q3 | 1 | "'Treasury funds with fixed end dates' is unclear and probably wrong: a fund does not mature the way a bond does." "Probably wrong" fails the facts (the funds redeem for cash in their final year); "unclear" stands. Also "'which never needs rebalancing' is unexplained, since I do not know what rebalancing is." |
| E (N) | Q1 | 3 | "The same logic as S and B." |
| E (N) | Q2 | 2 | "The same tablet closer." |
| E (N) | Q3 | 1 | "'rebalancing' now appears with no 'as rates move', so the first pension option is harder to follow. The fund-maturity problem is still there." |
| F (S) | Q1 | 3 | "the plan says why this matters: 'so no cheque depends on what a bond sells for that January.' The reader can see the risk being removed." On its own a 1 (the clause quoted, no fact of hers); the reader puts it in "the same logic" as the rest under B and N, so 3 (note 3). Either way F doesn't beat the final with this reader. |
| F (S) | Q2 | 2 | "The same tablet closer." |
| F (S) | Q3 | 1 | "The same 'Treasury funds with fixed end dates' and 'late 2032' fund problem." |
| G (B) | Q1 | 3 | "The same logic, and the clearest of the five. Both pension options are set out with 'either', 'as rates move' and the reason for choosing the second, so the reader can follow why Laura's cheques do not depend on prices." Level with the final: my key stops at 3. |
| G (B) | Q2 | 2 | "The same tablet closer." |
| G (B) | Q3 | 1 | "The same fund-maturity problem." |
| H (V) | Q1 | 3 | "Same logic as J: one Treasury per payment, held to maturity, so no sale is needed and shares sit behind the cheques." |
| H (V) | Q2 | 2 | "The same closing line about the tablet." |
| H (V) | Q3 | 1 | "The same problems as J ('Treasury funds with fixed end dates', 'never needs rebalancing')." On "exactly": "a stronger claim than the others, though still true for a Treasury held to maturity", a quibble. (The final has "exactly" too; the reader missed it there.) |

### Ruling on "never needs rebalancing" and "exactly" (only the final and H still carry them)
- **"never needs rebalancing": not 0, scored 1.** The professor: "The plan itself reinvests bond interest and, in
  2031, moves shares into Treasuries to cover the reinvestment gap. That is rebalancing." The speed judge: the plan
  "relies on reinvesting interest and can fall short". The sentence before defines the word: pension funds match
  "their bonds' average timing to the payments' and rebalanc[e] as rates move". That is the pension sense, re-matching
  the bonds' timing to the payments as time passes and rates change, and the ladder never does it. Reinvesting
  interest doesn't re-match anything, and the 2031 move happens once, on a fixed date, and buys Treasuries to cover a
  gap; it doesn't re-time the ladder. So the reason doesn't hold against the checked facts. The stumble is real,
  though: two readers tonight and the first professor ("'never' invites a challenge") read "never" against P7 and the
  2031 move. That's an ordinary reader's confusion, a 1. It moves no number: "exactly" already holds the professor at
  0 in both versions, and the speed judge's flag scores 1 either way.
- **"exactly": the professor's 0 stands; the speed judge's flag is a 1.** The professor's reason, "true of a single
  bond, but the ladder also holds funds whose end value is not promised", holds against iShares (the fund "does not
  seek to return any predetermined amount at maturity"), as in round 1. The speed judge's reason doesn't: a Treasury
  held to maturity does pay exactly its interest and face value, and what the reinvested interest earns is a separate
  risk, one P7 names. The "or at least contradictory" half scores as unclear.
- **Caplet's Book 4 (Ray, 26 Oct).** It lets Caplet keep "exactly": the iBonds are "as close to guaranteeing an exact
  amount at an exact date as it gets ... other than literal T-Bonds", and drawing the line is "up to you", "concise
  and direct". It doesn't make the professor wrong: its own words, "other than literal T-Bonds", say the funds aren't
  exact. My key asks only whether the reader's reason holds, so the 0 stands. Book 4 ranks above my key, though, so
  this is a finding for Caplet's card, not a veto. The professor gave it 0 in both reads, and no reader of a version
  without "exactly" called that sentence untrue.

### Q4 (most investing understanding applied to her) and Q5 (sleep in a bad year)
| Reader | Q4 pick | Q4 score | Q5 pick | Q5 score |
|---|---|---|---|---|
| A2, professor | G (B): "We do the second, so no cheque depends on what a bond sells for that January." "It then gives the reason in terms of the client." Then: "V is a close second and N third ... G and P come last, because their version of that sentence is the one that is untrue." | G 3, others 0 | F (V): "A Treasury bond held to maturity pays what it promised, whatever markets do. High certainty means no payment depends on shares." "Without the 'So', the second sentence reads as a flat promise." The line this reader called a slogan under Q2. On G: it "drops 'whatever markets do', which is the phrase that would actually reassure a client watching a downturn." On the final and H: they "sound even calmer ... but they would cost her trust in 2031". | F 3, others 0 |
| B2, speed judge | E and G, jointly (V, L): "I'd pick V or L as the best presentation, because their wording ('so no cheque depends on what a bond sells for that January') stays accurate." The reader had just said "The versions barely differ on understanding." | E 3, G 3 (joint and qualified, like round 1's pick of Nora's), others 0 | G (L): "It promises the least, with no 'exactly', 'whatever' or 'never needs rebalancing' ... 'A Treasury bond held to maturity pays what it promised.'" F "nearly as good". | G 3, others 0 |
| C2, Year 11 | G (B): "It names the risk Laura cares about, the price of a bond on the day a cheque is due, and it is the sentence that links the investing choice to her bills." | G 3, others 0 | G (B): "it says her January payments are not exposed to falling prices." | G 3, others 0 |

G took five of the six picks (one shared with E), F one, and the final and H none. My bar leaves Q4 and Q5 out, as in
round 1, and I'm not adding them now.

## The table
| Version | Professor Q1/Q2/Q3 | Speed judge Q1/Q2/Q3 | Year 11 Q1/Q2/Q3 | Q1 total | Q2 total | Q3 total | Q4 total | Q5 total |
|---|---|---|---|---|---|---|---|---|
| **Final** | 2 / **0** / **0** | 3 / 1 / 1 | 3 / 2 / 1 | 8 | 3 | 2 | 0 | 0 |
| **E** (Jun, Felix) | 2 / 2 / 1 | 3 / 2 / 3 | 3 / 2 / 1 | 8 | 6 | 5 | 3 | 0 |
| **F** (Kai) | 2 / **0** / 1 | 3 / 2 / 3 | 3 / 2 / 1 | 8 | 4 | 5 | 0 | 3 |
| **G** (Tess) | **3** / 2 / 2 | 3 / 2 / 3 | 3 / 2 / 1 | **9** | 6 | 6 | 9 | 6 |
| **H** (Nora) | 2 / 1 / **0** | 3 / 2 / 1 | 3 / 2 / 1 | 8 | 5 | 2 | 0 | 0 |

## The bar, line by line: E, F and G (my whole bar and tripwire)
| Line | E (Jun, Felix) | F (Kai) | G (Tess) |
|---|---|---|---|
| (a) wins Q1 with 2 of 3 readers (ties don't count) | **Fail**: none (2 v 2, 3 v 3, 3 v 3) | **Fail**: none (2 v 2, 3 v 3, 3 v 3) | **Fail**: the professor only (3 v 2); speed judge 3 v 3, Year 11 3 v 3 |
| (b) not behind the final on Q3 for any reader | Pass (1 v 0, 3 v 1, 1 v 1). Two readers said the cut "as rates move" left the other method harder to follow; E stays level only because the final's P3 scored lower for other reasons | Pass (1 v 0, 3 v 1, 1 v 1) | Pass (2 v 0, 3 v 1, 1 v 1) |
| (c) not behind on Q2 for any reader | Pass (2 v 0, 2 v 1, 2 v 2) | Pass (0 v 0, 2 v 1, 2 v 2) | Pass (2 v 0, 2 v 1, 2 v 2) |
| (d) Q1 total at least 2 above the final's | **Fail**: 8 v 8 | **Fail**: 8 v 8 | **Fail**: 9 v 8 |
| (e) inside 497 strict, Book 11 and I80 kept | Pass: 497. The clarity cost is counted under (b), as I counted Felix's in round 1 | Pass on count: 497. The professor's "slogan" is the habit I80 bans; I count it once, under the tripwire | Pass: 497; no reader flagged anything it changed |
| Tripwire (any reader: a sentence in the repaired paragraph at Q2 = 0 or Q3 = 0) | Clear | **Trips**: the professor's Q2 = 0 on "High certainty means no payment depends on shares.", a sentence F changed | Clear |
| **Beats the final?** | **No** (fails a, d) | **No** (fails a, d; trips) | **No** (fails a, d) |

**Tie-break:** not needed, since none of E, F and G clears. (Had I read the speed judge the other way, G alone would
clear, so it still wouldn't run.)

## H (Nora's cut of ", to us,"): (b), (c) and the tripwire only
| Line | H |
|---|---|
| (b) not behind the final on Q3 for any reader | Pass (0 v 0, 1 v 1, 1 v 1) |
| (c) not behind on Q2 for any reader | Pass (1 v 0, 2 v 1, 2 v 2). The final's "So, to us, high certainty means ..." drew "throat-clearing before the line lands" and "sounds a little staged"; H's version of it drew nothing |
| Tripwire, as the chair registered it for H at 18:50: no reader flags its last sentence | Clear: no reader named "So high certainty means no payment depends on shares." in H |
| **Result** | **Passes** |

As my tripwire is written (any P3 sentence at 0), H trips on the professor's 0 for the "exactly" sentence, which it
keeps word for word: the same 0 the final carries. In round 1 I said I'd meant the tripwire for lines a repair adds,
and the chair's test for H says the same thing, so I rule on that. The two words H cuts are also a habit on Ray's own
list of AI tells ("Stilted asides: 'That, to us, is what ...'", `keel/ips_rewrite/drafts/D35/README.md`); the chair
noted in round 1 that the line was added after the I80 check ran.

## Verdict
**Verdict.** None of the three merged lines beats the final under the bar I registered, so no new reason goes into P3
tonight. Each fails (a) and (d), the Q1 lines, because only one reader, the professor, heard a better why from any of
them. The Year 11 gave the final 3, as the first Year 11 did, so a repair needed both other readers, and the speed
judge wrote "The same plan" for the final, "Same plan, same reasoning" for three of the others, and "The versions
barely differ on understanding". G
(Tess's merge) came closest and is the readers' favourite: it is behind the final on nothing for any reader, it won the
professor's Q1 (3 v 2), it drew no corny flag and nothing untrue, and it took five of the six "most understanding" and
"sleep in a bad year" picks, where the final took none. But its Q1 total is 9 v 8, one short of the +2 my bar asks,
and a tie goes to the final. E (Jun and Felix) ties the final on Q1 with all three readers, and two readers said its
cut of "as rates move" left the other method harder to follow. F (Kai) also trips the tripwire: the professor read its
bare "High certainty means no payment depends on shares." "as a slogan rather than a conclusion". H (Nora's cut of ",
to us,") passes its test: no reader put it behind the final, and nobody flagged the sentence it changed, where the
final's version drew a flag from two readers of three. Under the chair's 18:50 rule, the room now chooses between (2)
and (4) on that result. One call decided this, and I've set it out above: I scored the speed judge's "same reasoning"
as a tie. Read the other way, G would clear, but the same reading would score H, the final's own words but for two,
above the final for the same reasoning. On the final itself, the professor scored "exactly" 0 again, for the first
professor's reason. That 0 stands under my key, but Caplet's Book 4 permits the word and ranks above us, so it's a
card finding, not a repair.

## The two reads together
Across both reads (six readers; the final, Felix's, Nora's and Tess's, then the final, E, F, G and H), the final won
none of the twelve "most understanding" and "sleep in a bad year" picks, and ten went to a version carrying Felix's
clause, "so no cheque depends on what a bond sells for that January". Yet no version beat the final on the why,
because both Year 11 readers found it in the final ("a bond that was always going to pay it"; "nothing has to be
sold"). The clause makes readers prefer and trust the paragraph more than it makes them understand it. And two of
three readers named the final's "So, to us, high certainty ..." in both reads; with "to us" cut and "So" kept, no
reader named it in fifteen reads (Felix's and Nora's, then E, G and H).

## Flagged by every reader in every version
- **The closing line**, "Like the tablet it is named after, the plan works as long as nobody crushes it.": the
  professor ("The closing line, which is in all five"), the speed judge ("the winding-up-for-a-punchline line") and the
  Year 11 ("a neat closing gag built on the tablet joke"; in a bad year it "would make her feel the plan is a clever
  line rather than a safe one, so it is the line I would least want"). That makes 27 answers out of 27 across the two
  reads. It is the only line every reader flagged in every version. It isn't on tonight's ballot; it is Caplet's choice.

Flagged in all five by at least one reader (no P3 change reached these):
- **"Treasury funds with fixed end dates"** (P3, unchanged in every arm): the professor ("unexplained jargon, and a
  fund's final payout is not fixed the way a bond's is", which is true) and the Year 11 ("a fund does not mature the way
  a bond does", which half fails the facts). A Year 11 has stumbled on it in both reads.
- **Why a held-to-maturity ladder needs reinvesting** (P7): the professor ("The text never says the bond interest
  arrives years before the cheques start, so a reader wonders why one-bond-per-payment needs any reinvesting"), the
  Year 11 under G ("confusing, since the bonds are said to be held to maturity") and the speed judge under E ("takes a
  second read"). Three readers, new tonight. It is the same gap the professor and the speed judge set against "never needs
  rebalancing", and the speed judge against "exactly".
- **"the money set aside"** (P8): the professor, "which money?"
- **The tablet set-up**: "'X for ten, R for redemption' is cute too" (professor); "The 'do not crush' paragraph earlier
  is a milder version of the same joke" (speed judge).
- **For the Year 11**: "time makes a loss rarer, not smaller" and "portfolio insurance" unexplained; the "late 2032"
  fund. The other two readers picked shared lines as the best in the piece: "time makes a loss rarer, not smaller, and
  a fixed cheque can't wait for a recovery" (professor, "The best investing sentence in the whole piece") and "so her
  portfolio shouldn't bet on shares twice" (speed judge).
