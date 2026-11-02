# FICTION (the room) + real work (the test). L-16: two jobs, one pocket

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Genius Lab, Mon 2 Nov
2026, 13:40 Sydney, round 6 beat 5 (Q14, the verify round: is everything V52 says about what Laura owns true at its
source?). Amara builds; Kai roasts and hunts flaws; Jun judges cold. Huddle H-016
(`../../huddles/2026-11-02_two-jobs-one-pocket/`; one round, three agent calls). Script
`L-16_two_jobs_one_pocket/run.py`; results `L-16_two_jobs_one_pocket/results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, world stocks 7.5% | 200,000 paths per world,
seed 20261016 | rho 0.5 unless S0 | V52's design = the Lab's L-13 -> L-14 chain (L-15's "same day" arm) | MODEL.**
Controls (asserted in the script): A0's gift mean and top reached equal L-14's XR row; A0 in S9 reproduces LR-09
(98.49% paid in full, median gap $5,032). Cross-check on a separate code path: L-11 D1 (Wed 28 Oct; a 2033 set-aside
with no 2031 mark) leaves a cheque short in 26.8% of S0 futures with no margin and 0.34% with $7,500, against L-16's
23.9% and 0.18%.

**For a judge, in plain words.** Our plan gives the stocks Laura keeps two jobs. They are her flexibility, and they are
the first money that covers the one weak point in her bond ladder: the interest it has to reinvest. We measured how
often the second job eats the first. In an ordinary future the ladder borrows from that pocket seven times in ten,
mostly a safety margin she gets back after the last cheque; one time in five it takes all of it (one in ten from the gap
alone); when rates fall hard and stay down, two times in three. The margin turned out to be the part the draft forgot to say. Priced at the day's yields
alone, the gap leaves a cheque short in about one future in four. With the margin, about one in 550. So the draft needs
its margin back, and it should say plainly what the design already does: her flexibility shrinks before her promise does.

**Why this, today.** Two open requests to the Lab, both on the same pocket. The Library (H-015, slip S-11 break 3): P6
calls the kept stocks "her flexibility" and P8 makes them the first payer of the reinvestment gap; in the bad cases, what
share does the gap take by January 2033, and how often is nothing left? Laura's Room (Kai, H-011): LR-09's world S9 bounces
a cheque in 1 in 66 futures, median $5,032; a rung never bought, or thin reinvestment after 2033, and do Laura's half kept
to 2042 or a bigger 2031 set-aside close it? Wharton's lines: "Preserves appropriate financial flexibility when determining
the facility contribution" (case :145); "committing all remaining assets could limit her financial flexibility as the
project develops" (:102-103); "define what they consider a high degree of funding certainty" (:97). A simulated judge
already wrote that "flexibility after 2033 is only about half a ~$30-40k stock pot. That is thin against the case's
warning" (`../../ips_rewrite/judges/panel_V42/judge3_scores.md`, a test, never a quote). IPS lines that can move: V52 P6
and P8; P3 for Kai's question.

## Pairings tried (beat 5)
- **N3 x Q14** (find x question): "under a tenth of her money" is the whole stock slice, so the kept half is under a
  twentieth, and it carries two jobs. The pocket is small; that is why the jobs collide. Tested (L-16).
- **F3 x T2** (find x find): the bond trader's floor is "guaranteed a minimum rate of interest" (HMRC CFM13340, the
  Library's F3), and IBTM "does not seek to return any predetermined amount". Laura can't buy a floor (Wharton bans
  derivatives), so the margin is a floor she writes to herself, and her flexibility is the premium. Final Report line.
- **F1 x a new stepping stone in a mined field** (find x stone): the caplet's leaflet ("may affect its sustained release
  properties", Panadol Osteo CMI) x the regulator's **overage**. ICH Q8(R2), section 2.2.2, fetched 2 Nov 2026
  (https://database.ich.org/sites/default/files/Q8%28R2%29%20Guideline.pdf, read through WebFetch, so the words came back
  in order, not a byte check): "In general, use of an overage of a drug substance to compensate for degradation during
  manufacture ... or to extend shelf life, is discouraged."; overages "should be justified"; give "1) amount of overage,
  2) reason for the overage ... and 3) justification for the amount of overage." The margin is an overage. Final Report
  image at most (see verdicts).

## Challengers and novelty check
Checked against IDEAS, the lab book's binned list, IDEA_LEDGER, IDEA_BANK, TERRITORY, R02 and the huddle INDEX.
| | Challenger | Novelty | Where it could land |
|---|---|---|---|
| C1 | **Add a margin**: P8 says the gap is priced "at the day's yields" and set aside; the model also sets aside $7,500 for yields that fall further | A restoration, not new: IDEA_LEDGER D6 had it IN ("with a cushion for the one thing they can't promise"); V52 dropped it | IPS, P8, +3 words |
| C2 | **Say the order**: "so her flexibility shrinks before her promise does" | New wording; the order is L-10's capital structure (FRB-2) applied to the kept half | IPS, P8, +8 with C1's 3 |
| C3 | **Gap first, then halve** (G): the gap comes out of all the stocks, then the rest is split half promised, half kept | New: no hit in the bank, ledger or lab book | Final Report, priced alternative |
| C4 | **The order line as a backstop** (B0): P9's "the cheques, then the floor, then everything above it", read literally after 2033 | Not new: L-11 D0 (Laura's half behind the cheques to 2042), rejected for the F2 clash | Final Report |
| C5 | **The margin as an overage** (pharmacology, ICH Q8(R2)) | New in this sense; "overage" so far meant the newsvendor's unsold papers (Library S-08, a different idea) | Final Report image at most |

## Hypotheses (one sentence each, can be wrong)
- **H1 (the Library's):** the kept half keeps most of its value in the bad cases, because the gap is small next to it, so
  P6's "her flexibility" survives P8.
- **H2 (Kai's, from H-011):** S9's gap is thin reinvestment after 2033, so Laura's half kept to 2042 closes it.

**Kai's roast.** Logged honestly as a deviation: the S9 arm ran first, to reproduce LR-09 before anything else was trusted,
and Kai's flaw-hunt (`../../huddles/2026-11-02_two-jobs-one-pocket/posts/r1_kai.md`) was written after all five worlds,
against the results file and the code. So this round has no sealed guess for him to lose; his post attacks the reading,
not the forecast. It cost the chair four corrections (CORDs, below), all made before anything left the room.

## Test
Six arms on V52's design, five worlds (S0 independent; S1 linked, rho 0.5; S2 the 2028 deposit halved; S6 yields fall 2
points just after the build, for good; S9 = S2 + yields a point lower before the build, LR-09's). A0 = V52 as modelled
(margin $7,500, LR-05's C; after January 2033 the kept stocks are never a source, Archive A19); A1 = V52 as written (no
margin; `CORD:` Kai, a generous reading: it keeps the January 2033 top-up from the kept stocks and the gift, which P8
never says, and drops the order line from February 2033; read live throughout it is B1, 92% / 59%, and no reading
without a margin gets near 99.8%); A2 = Kai's bigger set-aside ($15,000); B0 / B1 = A0 / A1 with the kept stocks paying any cheque gap after 2033
(valued in 2042, one lump: L-11 D0's approximation, generous in some paths); G = gap first, then halve. "Short" counts any
shortfall over 50 cents: the case's cheque is "a fixed $50,000" (:90). "Nothing left" = under $500 or 2% of the untouched
half. What would prove H1 wrong: the gap takes all of the kept half in more than 1 future in 10 in any bad world.

## Results (MODEL)
**Table 1. All ten cheques paid in full (median gap when short)**
| Arm | S0 | S1 | S2 | S6 | S9 |
|---|---|---|---|---|---|
| A0 V52 as modelled (margin $7.5k) | 99.82% ($359) | 99.81% ($362) | 99.74% ($408) | 99.68% ($364) | 98.49% ($5,032) |
| **A1 V52 as written (no margin)** | **76.09% ($3,076)** | 75.91% ($3,092) | 74.82% ($3,140) | **46.60% ($3,324)** | 64.31% ($2,709) |
| A2 bigger set-aside ($15k) | 100.00% | 100.00% | 100.00% | 100.00% | 98.58% ($5,433) |
| B0 A0 + kept stocks behind the cheques after 2033 | 99.94% ($397) | 99.94% ($388) | 99.82% ($388) | 99.79% ($346) | 98.49% ($5,052) |
| B1 A1 + the same | 92.23% ($3,161) | 90.74% ($3,183) | 83.74% ($3,229) | 59.11% ($3,343) | 71.22% ($2,728) |
| G gap first, then halve | 99.86% ($348) | 99.86% ($348) | 99.81% ($354) | 99.79% ($365) | 98.51% ($5,123) |

**Table 2. The kept half by January 2033: the gap takes some / half or more / all of it; median left of the untouched half**
| Arm | S0 | S1 | S2 | S6 | S9 |
|---|---|---|---|---|---|
| **A0 V52** | 71 / 38 / **19**%; $13.9k of $21.7k | 71 / 37 / **21**%; $14.5k of $21.7k | 72 / 61 / **42**%; $2.9k of $10.5k | 88 / 77 / **65**%; $0 of $13.3k | 99 / 98 / **86**%; $0 of $5.3k |
| A1 no margin | 36 / 19 / 10%; $19.4k | 36 / 20 / 11%; $20.0k | 37 / 28 / 22%; $9.3k | 77 / 64 / 52%; $0 | 54 / 46 / 41%; $2.6k |
| A2 $15k margin | 82 / 64 / 36%; $6.1k | 82 / 64 / 36%; $6.5k | 82 / 74 / 65%; $0 | 93 / 87 / 77%; $0 | 100 / 100 / 98%; $0 |
| G gap first, then halve | 71 / 20 / **7**%; $17.3k | 71 / 22 / 9%; $17.7k | 71 / 41 / 25%; $6.7k | 88 / 66 / **47**%; $1.6k | 99 / 84 / 60%; $0 |
Inside S0, in the worst tenth of naming-day gaps, A0 leaves nothing in 70% of futures, G in 39%. **Both rows matter**
(Kai): about half of A0's "takes some" is the margin alone; the gap by itself (A1's row) empties the pocket in 10 / 11 /
22 / 52 / 41%. In S9 the $7,500 margin is bigger than the median kept half on naming day ($4,637). The margin is not
lost, but it is not liquid either: whatever the cheques never need comes back to Laura after the last one, in 2042 (it is
inside "Laura 2042" below).

**Table 3. The range and the gift (range lowered on naming day / top reached / below the quoted bottom / median top
quoted / gift mean / Laura's 2042 money, mean)**
| Arm | S0 | S6 | S9 |
|---|---|---|---|
| A0 V52 | 17% / 97.9% / 0 / $165k / $159,957 / $49,270 | 63% / 96.0% / 0 / $145k / $141,771 / $23,725 | 83% / 95.9% / 0.01% / $40k / $37,464 / $13,409 |
| A1 no margin | 8% / 98.3% / 0 / $165k / $161,110 / $54,508 | 49% / 96.6% / 0 / $150k / $146,334 / $23,765 | 36% / 96.3% / 0.01% / $45k / $43,058 / $13,015 |
| A2 $15k margin | 34% / 97.4% / 0 / $165k / $157,671 / $45,936 | 75% / 95.6% / 0 / $140k / $136,299 / $26,916 | 98% / 96.1% / 0.01% / $30k / $30,166 / $20,072 |
| G gap first, then halve | 5% / 97.5% / **0.03%** / $160k / $157,588 / $55,542 | 43% / 94.5% / **0.15%** / $145k / $140,890 / $26,984 | 54% / 95.7% / **0.31%** / $40k / $37,092 / $15,322 |
S1 and S2 sit between (full rows in results.json). In January 2033 the gift also pays part of a cheque after naming in
16% of S0 futures (61% in S6), almost all of it out of the slack above the quoted top: the top is still reached 97.9%.

## Kai's question: where S9's gap comes from
Of S9's short dollars (A0): **35% a rung never bought** (at a point lower, the $300,000 bought less of the ladder, and the
halved deposit could not finish it), **49% the 2033 gap with nothing left to pay it** (the deposit went into the ladder,
so there is little floor and almost no stock; the kept half is gone in 86% of S9 futures), **15% after 2033**. `CORD:`
(Kai) the chair first wrote "the deposit, not reinvestment"; the sums are right (they add to 1.0000, no double count bar
a sliver under 1% of paths) but 49 + 15 = 64% of the dollars *are* reinvestment gaps. The halved deposit is why nothing
is left to pay them, not what they are. Neither cure closes it: kept stocks behind the cheques to 2042, 98.49% -> 98.50%; a $15,000
margin, 98.58%, and the gift's mean falls from $37,464 to $30,166. The only cure is money the plan doesn't have. **H2:
FALSE** (only 15% of the gap comes after 2033, and by then the pocket that would pay it is empty). In words a judge can check: P4 already says a smaller deposit shrinks the gift and spares "a cheque funded by a
Treasury already bought"; S9 is the cheque whose Treasury was never bought, which is why V47's "– or nearly" in P3 was
honest (the open item in D32's README).

## Verdicts
- **H1: FALSE in every bad world.** All of the kept half goes in 42% (deposit halved), 65% (yields 2 points lower for
  good) and 86% (S9) of futures; one in five even in the base world.
- **C1 add a margin: ADOPT** (to the rewrite thread). Without it the text describes a design that, in our model, leaves a
  cheque short about one future in four, and one in two if yields fall hard. Three words, no number (Book 11).
- **C2 say the order: ADOPT as an offer** if the words are paid by a whole idea: it tells the judge the first loss is
  Laura's own flexibility, by design, because "a number said aloud to co-sponsors cannot be quietly halved" (P7). Jun's
  blind read and Kai's flaw-hunt decide the wording (huddle, below).
- **C3 gap first, then halve: PARK** (Final Report, a priced alternative). It keeps her flexibility far more often
  (gone 7% v 19% in S0, 47% v 65% in S6) for about $2,400 off the mean gift and $5,000 off the median top, but it lets
  the gift fall below the quoted bottom (3 in 10,000 futures in S0, 20 in S2, 15 in S6, 31 in S9). `CORD:` (Kai) that
  breaks P7 (a number said aloud gets cut), not P6: the floor stays hers, the cheques eat into it as P9's order allows,
  and V52 itself does it once in 10,000 in S9. Keel's call (logged in ASK_HUMANS): keep V52's order.
- **C4 kept stocks behind the cheques after 2033: PARK** (Final Report). With the margin it adds little (99.82% ->
  99.94%) and ties "liquid any day" to the cheques again (L-11's F2 clash); without the margin it can't save the text
  (92%), because in the futures that need it the pocket is already empty.
- **A2 Kai's $15,000 margin: PARK** (Final Report). Every cheque in four worlds, but the pocket is empty in 36% of base
  futures, and it fails S9 anyway. $7,500 is the knee we tested; the exact size is Final Report work.
- **C5 the overage: BIN as an image** (Amara broke it, below); its three-part test (amount, reason, proof) goes to the
  Final Report with no pharmacy in it (bank #132).

## Offers to the IPS (AI DRAFT, Claude, 2 Nov 2026; GPTZero: not yet checked; strict counts by `textcheck.py`)
V52 (`../../ips_rewrite/drafts/D32/ips_V52.txt`) is 495 strict.
- **m1** (498): P8 "Before she names the range, we price that gap at that day's yields, add a margin, and set it aside
  from the stocks Laura keeps; whatever they can't cover lowers the whole range." One word over: pay with a whole idea.
- **m3j + cut** (498, `../../huddles/2026-11-02_two-jobs-one-pocket/offer_V52_m3j_cut.txt`; the huddle's pick): "Before
  she names the range, we price that gap at that day's yields, add a margin, and set it aside from the stocks Laura keeps,
  so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range."; paid by
  P3's mirror "We don't invest toward these payments. We buy them." (-9; the pitch keeps the line); one word still owed.

## The huddle (H-016, one round, three agents; posts in `../../huddles/2026-11-02_two-jobs-one-pocket/posts/`)
- **Jun, cold judge, blind** (V52 = X, m1 = Y, m3 + cut = Z; read only Wharton's word, the case and the three texts):
  ranked **Z, Y, X**. On Z: "flexibility pays before the promise does. Whatever is left of the kept half stays hers and
  liquid. No inference needed." On X: "the order of loss is left for the reader to work out." Stumbles: "they" after
  the new sentence (fix: "the stocks"); "margin of what?"; "which day?" (fix: "that day's"). On the P3 cut: "It is the
  sentence I would quote back as the central idea ... I would take that loss for the priority line, but not lose both."
- **Kai, flaw-hunter** (against run.py and results.json): margin TRUE IF (see A1's CORD); kept-half numbers TRUE,
  headline inflated (give the Library both rows); S9's sums TRUE, headline FALSE (CORD above); G's numbers TRUE, reason
  FALSE (CORD above); backstop TRUE; m3's clause TRUE ("Flexibility goes first both times ... the gift pays cheques
  after naming ... only once the half is gone. It's the one sentence that admits the 2033 sale"). Verdict: "m3+cut, with
  'they' made 'the stocks' and a word found elsewhere, because m1 busts the cap and still hides the sale after naming day."
- **Amara, builder, broke her own overage first:** an overage is added once by a maker for a measured loss and never
  handed back; ours is sized in 2031, paid by Laura, and returned; ICH calls overages "discouraged", so we'd cite a
  regulator against ourselves; a judge without pharmacy hears "the till being over"; a second pharmacy idea "makes a
  theme". What survives is the test, for the Final Report: "We add $7,500 to the gap because interest reinvested after
  2033 may earn less; in 200,000 modelled futures that lifts all ten cheques paid from 76% to 99.8%. Amount, reason,
  proof." (S0, checked against results.json: 76.09% -> 99.82%.) From Laura's side: "the range is a promise she made to
  others and cannot quietly halve, while flexibility is one she made to herself", so keep the order.
- **Landed (chair):** C1 ADOPT and C2 ADOPT as the offer m3j (Jun's two one-word fixes in; 498 strict with P3's mirror
  cut, one word owed); m1 alone if no whole idea pays (498 too). Seeds: size the margin each 2031 from the gap's own
  spread (FR); what is Laura's flexibility in the futures where the pocket is empty (Laura's Room).

## What the model can't price
A US default; a deposit that never comes (S3/S5 break the chain's sorts); taxes; the building's cost in Taiwan dollars,
which is the flexibility's other job and has no number in the case. The post-2033 backstop is valued as one lump in 2042.
