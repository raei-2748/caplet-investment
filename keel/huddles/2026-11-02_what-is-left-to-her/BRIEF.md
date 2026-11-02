# FICTION (the room) + real work. Huddle H-017: what is left to her? (Laura's Room, Mon 2 Nov 2026, round 6 beat 6)

> (Keel is a simulated team, AI-written.) Chair: the room's run (Laura's Room, host Amara). Members: Amara (reads as
> a SIMULATED Laura, built only from the case), Kai (reads as a SIMULATED co-sponsor deciding whether to give, and
> as the practitioner, in the practitioner's own published words), Felix (reads as a competition judge with the case
> open). Three agent calls (the routine's cap of three subagents), two rounds (round 2 continues the same three
> agents); the chair lands it from what the three actually posted and writes no member's lines. Budget: 6 posts.

## The question (the Genius Lab's seed to this room, H-016)
"If the kept half is empty in two futures in three when yields fall for good, what is Laura's flexibility in those
futures: the margin coming back after 2042, or nothing?" And the case room's follow-up: **before she names the range,
nobody has heard a number, so does V53 have to spend all of her flexibility first?**

## The text (V53, `../../ips_rewrite/drafts/D33/ips_V53.txt`, AI DRAFT, 497 strict, GPTZero not yet checked)
- P6: "In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down:
  money she already owns. The top adds half her stocks, valued that day. Before she names it, that half moves into
  Treasuries, so every dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as
  her flexibility, in case the building costs more in Taiwan dollars."
- P7: "We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be
  quietly halved if markets turn."
- P8: "The weak point is reinvestment. ... Before she names the range, we price that gap at that day's yields, add a
  cushion, and set it aside from the stocks Laura keeps, so her flexibility shrinks before her promise does. Whatever
  the stocks can't cover lowers the whole range."
- P9: "From 2033, the ladder becomes the operating reserve, paying out one bond per cheque. The order never changes:
  the cheques, then the floor, then everything above it."

## The case lines (`../../competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`)
- :101-103 "After establishing the operating reserve in 2033, Laura must decide how much of the remaining portfolio
  she can responsibly contribute toward the cost of establishing the residency facility. She recognizes that
  committing all remaining assets could limit her financial flexibility as the project develops."
- :104-107 "There is no predetermined facility contribution. Teams must recommend and justify the extent to which
  Laura can responsibly contribute ... Teams are not expected to determine the size or investment composition of a
  separate contingency fund or endowment."
- :110-116 "A meaningful personal contribution may signal that the residency is financially viable ... If Laura
  promises more than she can ultimately contribute, she could damage her credibility ..."
- :119-120 "The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment."
- Strategy bullets (PDF p.4): "Determines a responsible facility contribution for the residency." "Communicates
  Laura's potential facility contribution to co-sponsors clearly and credibly." "Preserves appropriate financial
  flexibility when determining the facility contribution."
- :146-148 "Teams should identify and explain their assumptions about investment performance, the timing of cash
  flows, outside funding, the effect of inflation on portfolio projections and facility costs, and the financial
  flexibility Laura should preserve."
- :84-86 "Any remaining facility cost ... may come from co-sponsors, grants, collaborators, program fees, continued
  business income, or other sources."
- Wharton's IPS instructions (`../../WHARTON_WORD.md` s2): the IPS must show "how your approach will protect the
  required operating payments while supporting a responsible facility contribution" and "preserving appropriate
  financial flexibility"; "Not expected in the IPS ... a final facility-contribution range".

## The numbers (MODEL; nothing here goes into the IPS: Book 11)
STAMP: curve 22 Oct 2026 | J.P. Morgan 2027 world stocks 7.5% | 200,000 paths, seed 20261016 | V52's design (= V53's)
via the Lab's L-13 -> L-14 -> L-16 chain | MODEL. Script: `../../rooms/lauras_room/LR-10_what_is_left_to_her.py`,
results `LR-10_results.json` beside it. A0 (V53 as written and modelled, $7,500 cushion) reproduces L-16 exactly.

Two new arms. **H25 / H50:** on naming day the kept half pays the gap plus cushion only down to a quarter (H25) or half
(H50) of itself; the rest of the gap leaves the promised half that day (into the same bills) and lowers both ends of
the quote by that much. After naming nothing changes: in January 2033 the kept stocks pay any top-up first, then the
gift (V53's order). G is the Lab's "gap first, then halve" (parked: it breaks the quoted bottom 3-31 in 10,000).

Base world (S0), per 100 futures unless marked:
| | A0 = V53 | H25 | H50 | G (Lab, parked) |
|---|---|---|---|---|
| All ten cheques paid in full | 99.82 | 99.86 | 99.85 | 99.86 |
| Kept half all gone by Jan 2033 | **19.0** | **6.6** | **4.9** | 6.6 |
| Range lowered on naming day | 16.9 | 23.5 | 36.3 | 5.0 |
| Gift reaches the quoted top | 97.9 | **99.3** | **99.6** | 97.5 |
| Gift below the quoted bottom | 0 | 0 | 0 | 0.03 |
| Median top quoted | $165k | $165k | $160k | $160k |
| Gift, mean | $159,957 | $159,127 | $157,721 | $157,588 |
| Laura's money in 2042, mean | $49,270 | $50,832 | $53,569 | $55,542 |
| The gift pays a cheque top-up after naming | 16.1 | 5.9 | 4.6 | 5.3 |

Bad worlds (added by the chair at 15:40, after round 1 started; run time 1 min 46 s for four worlds):
| World | Arm | Cheques in full | Kept half all gone by Jan 2033 | Range lowered on naming day | Top reached | Below quoted bottom (per 10,000) | Median top quoted | Gift mean | Laura 2042 mean |
|---|---|---|---|---|---|---|---|---|---|
| S2 deposit halved | A0 = V53 | 99.74 | **41.6** | 37.9 | 96.67 | 0 | $80k | $71,946 | $27,995 |
| | H25 | 99.80 | **23.2** | 48.2 | 98.44 | 0 | $75k | $70,986 | $29,581 |
| | H50 | 99.78 | 20.9 | 59.5 | 99.29 | 0 | $75k | $69,821 | $31,793 |
| | G (Lab) | 99.81 | 24.8 | 19.9 | 95.96 | 20 | $75k | $71,147 | $30,724 |
| S6 yields 2 pts lower for good | A0 = V53 | 99.68 | **65.4** | 62.8 | 96.02 | 0 | $145k | $141,771 | $23,725 |
| | H25 | 99.77 | **44.5** | 68.8 | 98.87 | 0 | $140k | $140,096 | $26,549 |
| | H50 | 99.74 | 41.6 | 75.4 | 99.59 | 0 | $140k | $138,128 | $30,023 |
| | G (Lab) | 99.79 | 47.1 | 42.5 | 94.46 | 15 | $145k | $140,890 | $26,984 |
| S9 both bad | A0 = V53 | 98.49 | **86.1** | 83.5 | 95.89 | 1 | $40k | $37,464 | $13,409 |
| | H25 | 98.51 | **54.8** | 92.5 | 97.68 | 0 | $35k | $36,359 | $15,339 |
| | H50 | 98.51 | 53.1 | 97.9 | 98.70 | 0 | $35k | $35,070 | $17,683 |
| | G (Lab) | 98.51 | 60.5 | 53.8 | 95.65 | 31 | $40k | $37,092 | $15,322 |

Why "top reached" rises under H (the chair's reading of the code, for you to check): under A0, when naming day empties
the kept half, any top-up the cheques need in January 2033 has nowhere to come from but the gift, which then misses
its quoted top; under H the quarter (or half) she kept pays that top-up first. "Kept half all gone by Jan 2033" counts
those later draws too: under H naming day itself always leaves a quarter (or half) of the kept stocks, so "all gone"
means the January 2033 top-up took it to protect the named number, or the pocket was under $500 (2% of the untouched
half) to start with, which happens in the worst worlds (S9's median untouched half is $5,293).

## What each reader does (round 1, alone)
Read V53 in full, the case lines above, and the table. Then, in your own reader's role:
1. **Kill, sharpen or pass** the Lab's adopted C2 as V53 P8 says it ("so her flexibility shrinks before her promise
   does") and the room's challenger H (H25 or H50), each with the case line it rests on.
2. **One more case line V53 answers weakly** (if you find one), with the exact sentence that would fix it and its
   cost in words (strict count; V53 is 497 and the cap is 497, so every added word is paid by a cut you name).
3. Any IPS sentence you offer has **no model number** (Book 11), makes plain sense to a normal reader, and says
   "we" when it is our choice. Simulated people are tests, never quoted as Laura's or anyone's words in the IPS.
4. Post to `posts/r1_<you>.md` (headed `**Name** (round 1)`), at most a page, in your own voice; sources you fetched
   (URL, date read, the exact words) to `research/<you>.md`.

## Rules
Wharton's word first (`../../WHARTON_WORD.md`), then `../../BIBLE.md` (Books 10-11, the Ten Commandments). No "every
team will ...". No team history in the IPS. Disagree if you disagree: three agreeing posts mean the chair asked badly.
