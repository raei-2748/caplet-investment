# FICTION (the room, the simulated readers) + real work (the case check, the run). LR-07: what the bottom gives up

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), not for submission. Laura's Room, Fri 30
Oct 2026, 15:10 Sydney, round 3 beat 6 (Amara). Script `LR-07_narrow_from_below.py`, results `LR-07_results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA, global equities 7.5% | 200,000 paths per
world, seed 20261016 | rho 0.5 unless S0 | L-13's chain unchanged, one block appended; L-13's slide reproduced to the
digit (top reached 97.9 / 97.6 / 96.0 / 96.7%) | MODEL.** Simulated readers are tests, never quotes; nothing here may
be quoted as Laura's or anyone's words. One cold reader (a fresh agent playing a competition judge, given only the case
and two texts) is a test too, not a judge's verdict.

**Read:** the Lab's four challengers (round file s5, `../lab/L-13_slide_the_range.md`): A slide the range (ADOPTED), B a
top at a fixed chance (PARKED), C bona fide width (PARKED), D "too low costs their gifts" (to the Writing Room); against
B3 (`../courtroom/C-03_B3_candidate.txt`, 498) and the case (`../../../competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`).

**Why this, today.** Q10, why a range and what each end costs; lens 22, what did we give up? North stars 3 and 4;
Client Knowledge (case :110-120), Investment Strategy. IPS line that could change: B3 para 13 (the range) and para 17
(the slide's one word). **Sealed guess before the run (Amara):** "Once the range slides, the cheques can still take
$15k or more off the gift after naming in a bad world, so the bottom has to stay low." **Wrong, by about half.**

## 1. Three readings of each challenger
| | Co-sponsor (programme officer, SIMULATED) | Competition judge with the case open | Practitioner from the find's field | Verdict |
|---|---|---|---|---|
| **A slide** | "So the old top was counting dollars the bottom had already handed to the cheques?" Yes: in 16.9-62.9% of paths the mark cut the bottom and left the top. To her that is not caution, it's a double count, and the slide removes it before she hears a number | Case :119-120, the range "must also protect" the ten payments; para 19's "the change lands on what isn't yet promised" is false at the top without it (L-13). Kai's "limbo in reverse" fails here: the bar didn't move, the double count did | ECM banker (reasoned from how ranges are revised, Ritter's revision tables, round s4 F1): when news lands before pricing, the issuer files an amended range, and both ends move. Hanley's partial adjustment says ranges under-react to news; the slide is the full adjustment for news the plan already has | **PASS, sharpened** (s2, s3) |
| **B fixed-chance top** | Same number to me as A's, plus a formula I can't check | Book 7 (BIBLE rule 8): the IPS is "a framework, not ... calculations"; a projected floor is a calculation | Forecaster (BoM, s4 K-finds): fixed chances (75 / 25) suit someone who forecasts every day for millions; Laura names one range, once | **PARK to the FR** (agree with the Lab) |
| **C bona fide width** | Has never heard of the SEC rule; "honest" is a word she wants someone else to award | No case line asks for a width test; a team that calls its own range "honest" is grading itself | SEC (W-03): the 20% test is for a share-price range in a registration statement. s2 shows the risk the width still carries after naming is under 7% of the top, so the width is a choice, not a measurement | **PARK to the FR** (agree), with s2's number |
| **D "their gifts"** | Yes, it's *our* giving a timid number costs (List and Lucking-Reiley: "a nearly sixfold increase") | The cold reader: "Co-sponsors appear nowhere in the 500 words, so neither 'gifts' in X nor 'their' in Y points to anyone." B3 never says "co-sponsor" (grep: 0); the case's whole section :108-124 is about them | Campaign counsel (T3): go public once most of the number is in hand, and say the lead gift out loud | **PASS with one word more:** "too low costs co-sponsors' gifts; too high, her word" (+1) |

## 2. The run: once the range slides, how far can the cheques still reach?
With the slide, the only thing between the quoted top and the gift after naming day is the 2033 re-measure of the coupon
gap (door 4), after spare cash and her half. Over 800,000 paths it never takes more than **$9,768**.

| World | Quoted bottom / top (p50) | Gift short of the slid top: p99 / p99.9 / p99.99 / max | short >$1k | short >$5k |
|---|---|---|---|---|
| S0 base | $145k / $165k | $932 / $3,946 / $5,833 / **$8,312** | 0.95% | 0.03% |
| S1 recession-linked | $145k / $165k | $1,216 / $4,048 / $6,191 / **$8,331** | 1.16% | 0.03% |
| S6 yields -2pt for good | $130k / $145k | $2,026 / $4,713 / $6,900 / **$9,768** | 2.07% | 0.07% |
| S2 deposit halved | $65k / $80k | $2,044 / $4,914 / $7,223 / **$8,865** | 1.87% | 0.09% |

**So the bottom sits about twice as far below the top as anything can reach it.** The width is $15-20k at the median;
the most the cheques can still take is under $10k. Narrowing from below (bottom = the slid top less $10k, never lower
than today's bottom) raises the quoted bottom by a median **$10k in S0 and S1** (in 96% of paths), $5k in S6, $0 in S2,
and the gift lands below it in **0 / 0 / 1 / 2 of 200,000** paths (S0 / S1 / S6 / S2; worst $2,226): the same paths
that already break V29's own bottom (s3), so narrowing by $10k adds no break at all. At $5k it breaks
63-177 times per world; at $15k, as at $10k. Same money, same cheques, same mean gift: the narrow range is a pure
change in what she *says*, which is exactly what the seed-money study prices.

## 3. The one-in-200,000 break, traced: it was always there
I expected the S6 and S2 breaks to be the slide's own bug (a slid top quoted below its bottom). **Wrong.** Counted, not
rounded: the slid top is never below the bottom (0 paths in S6 and S2), and V29's own bottom, with or without the slide,
is broken in **1 path of 200,000 in S6 ($2,226) and 2 in S2 (worst $806)**; 0 in S0 and S1. L-12 and L-13 report "0"
because their share is rounded to four decimals (1 in 200,000 = 0.000005). The breaks don't depend on the top at all:
in those paths the cheques' 2033 claim is bigger than the whole gift above the bottom. And the narrow bottom ($10k under
the top) breaks in exactly the same paths, no others, in all four worlds. **So "the bottom is never broken" should read
"broken in 3 of 800,000 paths, by at most $2,226"** wherever it is quoted (request to the Window). It changes no line of
B3 (the IPS has no number), and it is a better FR sentence than zero: a judge believes three far more than none.

## 4. Then why not narrow it? The cold reader, and what we give up
The model says the bottom could rise $10k for free. The words say no. One cold reader, given only the case and two
full texts differing in para 13, B3 + slide (X) and the same with the bottom written as "the top less the most the
cheques could still need" (Y, 497 words), scored the range paragraph **X 7 clarity / 7 credibility, Y 4 / 5**: "I would
rather put X's bottom in a board paper. 'Treasuries she already owns, rounded down' survives an audit committee"; Y
"reads as a point estimate with a haircut", "claims to know a worst case for an open-ended interest-rate risk", and
seems to "deduct the same shortfall a second time after para 17". The last is a misreading (para 17 settles the gap
*today's* yields imply; Y's "most" is the 2033 re-measure), but a misreading 500 words can't prevent is a real cost.

**That is lens 22's answer, and it belongs in the Final Report.** The bottom gives up about $10k of signal (the
bookable number on a co-sponsor's board paper, LR-04; the low side's price, seed money "nearly sixfold") to keep a
bottom anyone can audit: Treasuries she bought in 2028, rounded down. We could quote higher and never break it in
the model; we choose a bottom whose proof is a statement, not a simulation. The cold reader also caught what X costs:
"once the half is locked in Treasuries, the gift almost always lands at the top, so the bottom looks needlessly low.
Its own line, 'too low costs gifts', cuts against it." The FR has to say that out loud before a judge does.

**Kill, sharpen or pass: E (narrow from below) PARKED to the FR**, as the priced alternative we turned down. The 28 Oct
kill ("raising the quoted bottom with the lock: below it in 3-5% of paths") is out of date: with the slide it adds no
break to the 3 in 800,000 the bottom already has. The reason to turn it down is now words, not risk.

## 5. Case-requirement check on what survives (B3 + slide + D), as a judge would
| Case requirement | Line | B3 + slide | Gap and the fixing sentence |
|---|---|---|---|
| Recommend the range | :117 | Floor rounded down to floor + half the stocks (para 13) | None (Book 7: no dollar range in the IPS) |
| State confidence | :117-118 | **Not in B3.** The cold reader: "Neither paragraph states a confidence level" | Book 7 puts the numbers in the FR; the IPS can carry the principle in eight words. The Library's clause (inbox 30 Oct) is the candidate; the Writing Room weighs it |
| Favourable and unfavourable outcomes | :118-119 | The cap (para 15): falls hit the gift, rises go to Laura, until naming; after it, Treasuries | None. s2 gives the FR its number: after naming, only yields move the gift, by under $10k |
| Protect the ten payments | :119-120 | Cheques first; with the slide, para 19's line is true at the top too | None if the slide goes in; it's one word |
| Who the range is for | :109-116 | Co-sponsors never named | D's word: "co-sponsors' gifts" |
| Fundraising text | :123-124 | FR | FR (bank #89: "expect the top; the bottom is bought") |

## 6. Open request Q7, the blister pack (Kitchen, 29 Oct): what Laura does each January from 2033
Read B3 as a dose administration aid: everything is packed in advance, sealed and dated, so the patient decides
nothing on the day. **What she does each January, 2034-2042: nothing.** The holding due that December turns to cash
and becomes the cheque (para 5, "funds that turn to cash before each January"). **What the plan spares her:** choosing
what to sell, timing a market, topping up, or reading a statement in a bad year. **Break first (LS-04):** a pack is
refilled weekly by a pharmacist who checks it; Laura's is packed once (2027, finished 2028), so who checks? The plan has
exactly one scheduled check, January 2033: door 4 re-measures the coupon gap and tops up once (para 17), and after that
the reserve only shrinks. A pharmacist checks every week because doses change; Laura's doses are fixed in dollars by
the case (:88-90), so one check is enough. **Verdict: FR only.** B3 para 17 already says it ("topped up once; after
that it only shrinks"), and the case's "if at all" (:96) is answered there. FR line, bank #90: "From 2034 she decides
nothing in January. That's the point."

## Honest weaknesses
- The $10k ceiling is the model's tail (200,000 paths per world, one yield model), not a law; a yield fall between 2031
  and 2033 faster than any modelled path could reach further. This is one more reason E stays out of the IPS.
- One cold reader, one read. The co-sponsor and practitioners in s1 are reasoned readings; the ECM banker's "amended
  range" is general practice, not a quoted source.
- The Q7 reading adds no IPS words and no new number.
