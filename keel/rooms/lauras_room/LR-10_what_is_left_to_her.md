# FICTION (the room and the simulated people) + the real case. LR-10: what is left to her?

(Keel is a simulated team, AI-written.) AI-generated research (Claude Code), Mon 2 Nov 2026, Laura's Room, round 6
beat 6 (Amara; Kai and Felix in the huddle). Not for submission. Simulated co-sponsors, judges and Laura are tests,
never quotes; no Laura quotes. Huddle H-017: `../../huddles/2026-11-02_what-is-left-to-her/` (2 rounds, 6 posts, three
agents, the routine's cap; the chair landed it). Run: `LR-10_what_is_left_to_her.py` (patches one branch of the Genius
Lab's L-16 block and adds two arms; A0 still equals L-14's XR, the Lab's own assert), numbers `LR-10_results.json`.
**STAMP: curve 22 Oct 2026 (treasury.gov par) | J.P. Morgan 2027 LTCMA world stocks 7.5% | 200,000 paths per world,
seed 20261016 | V52's design (= V53's) via L-13 -> L-14 -> L-16 | MODEL.** Run time 1 min 46 s for four worlds.

**For a judge, in plain words.** The newest draft (V53) spends all of the stocks Laura keeps for herself before it will
lower the range she announces in 2031, even though on that day nobody has heard a number yet. We tested a simple rule
instead: she always keeps back a quarter of those stocks on naming day, and anything the rest can't cover lowers the
range before anyone hears it. Her pocket is empty by 2033 in about 1 future in 15 instead of 1 in 5, the number she
announces is actually delivered more often, the cheques are no worse, and it costs under $1,000 of the average gift.

## 1. Why this, today
Beat 6 reads the Lab's challengers three ways. The Lab's C1 (add a cushion) and C2 (say who pays first) were already in
V53 (`../../ips_rewrite/drafts/D33/`, 497 strict) by 15:10, so the room took the seed the Lab left it (H-016): "If the
kept half is empty in two futures in three when yields fall for good, what is Laura's flexibility in those futures?"
Not a repeat of LR-07 to LR-09 (the bottom's cost, the rival's bad day, the cheques' own number): today's ground is the
flexibility the case names twice (:102-103; strategy bullet 5, :145) and the lens of the day, the other side (who
stands behind Laura's pocket). North stars 3 and 4; Client Knowledge, Investment Strategy. IPS lines that change: P8's
last two sentences, P7, P9's first sentence, one P5 sentence cut.

## 2. The test (MODEL; nothing here goes into the IPS: Book 11)
Two new arms on V53's design. **H25 / H50:** on naming day the kept half pays the gap plus cushion only down to a
quarter (half) of itself; the rest leaves the promised half that day, into the same bills, and lowers both ends of the
quote by that much (rounded up to $5k). After naming nothing changes: in January 2033 the kept stocks pay any top-up
first, then the gift (V53's order, P8-P9). G = the Lab's "gap first, then halve" (parked in L-16).

| World | Arm | Cheques in full | Kept half all gone by Jan 2033 | Range lowered on naming day | Top reached | Below quoted bottom (per 10,000) | Median top quoted | Gift mean | Laura 2042 mean |
|---|---|---|---|---|---|---|---|---|---|
| S0 base | A0 = V53 | 99.82 | **19.0** | 16.9 | 97.90 | 0 | $165k | $159,957 | $49,270 |
| | **H25** | 99.86 | **6.6** | 23.5 | **99.31** | 0 | $165k | $159,127 | $50,832 |
| | H50 | 99.85 | 4.9 | 36.3 | 99.61 | 0 | $160k | $157,721 | $53,569 |
| | G (Lab) | 99.86 | 6.6 | 5.0 | 97.48 | 3 | $160k | $157,588 | $55,542 |
| S2 deposit halved | A0 | 99.74 | **41.6** | 37.9 | 96.67 | 0 | $80k | $71,946 | $27,995 |
| | **H25** | 99.80 | **23.2** | 48.2 | **98.44** | 0 | $75k | $70,986 | $29,581 |
| S6 yields 2 pts lower for good | A0 | 99.68 | **65.4** | 62.8 | 96.02 | 0 | $145k | $141,771 | $23,725 |
| | **H25** | 99.77 | **44.5** | 68.8 | **98.87** | 0 | $140k | $140,096 | $26,549 |
| S9 both bad | A0 | 98.49 | **86.1** | 83.5 | 95.89 | 1 | $40k | $37,464 | $13,409 |
| | **H25** | 98.51 | **54.8** | 92.5 | **97.68** | 0 | $35k | $36,359 | $15,339 |

H50 and G in the bad worlds: `LR-10_results.json` and the huddle brief. Why the top is reached more often under H: under
A0, when naming day empties the kept half, a January 2033 top-up can only come out of the gift (it does so in 16.1 base
futures in 100 under A0, 5.9 under H25; S6 61.2 v 43.2), and the gift then misses its quoted top; under H25 the kept
quarter pays it first. Felix checked this against L-16 `run.py` (the kept stocks are sold first, then the gift): it holds.
"All gone by Jan 2033" under H25 means the 2033 top-up took the quarter to protect the named number, or the pocket was
under $500 to begin with (S9's median untouched half is $5,293). **Not tested:** any share between nothing and a
quarter; the quarter is the knee we tried, and the Final Report owns its size (Kai).

## 3. Read three ways (the Lab's C2 as V53 says it, and the room's challenger)
| | SIMULATED Laura (Amara, case only) | SIMULATED co-sponsor + practitioner (Kai) | Judge with the case open (Felix) | Verdict |
|---|---|---|---|---|
| **V53 P8: "so her flexibility shrinks before her promise does"** | KILL the clause, keep the order. "On naming day nobody has heard a number. A smaller one costs me nothing I've said. An empty pocket costs me what I asked you to keep." (:109-116, :102-103) | Round 1 PASS ("a waterfall in eight words"); **round 2 KILL**: his own line, P7 covers "a number said aloud", and the pitch calls the cheques "a promise" | KILL: :145 asks for flexibility "when determining the facility contribution"; under V53 she names the range with nothing kept in about 63 S6 futures in 100; "promise" is the pitch's word for the cheques, so a judge hears the cheques shrinking second | **KILL 3-0** (the order survives inside the new sentence) |
| **H25** (keep a quarter on naming day) | PASS: "A slightly smaller number with a quarter kept is a thoughtful risk. Spending the last of it before anyone asked isn't." (:68-74) | ADOPT. Co-sponsor: "Tell me $160k with something behind it, not $165k with nothing. If her pocket's empty and the building runs over, who pays? Read your own case, :84-86. Us." Practitioner: a clearing house's own layer is "pre-funded" and still standing once members are exposed (CME, below) | PASS: rests on :102-103, :145, :114-116; the cheques are no worse in any world (:119-120); the cost lands on :110-112 | **ADOPT 3-0** |
| **H50** | KILL: 1.7 more futures in 100 for $5,000 off the median top; spends her signal (:110-112) | KILL: "Same medicine, double the dose, barely more effect." | KILL: lowers the base-world quote, the one co-sponsors are most likely to hear | **KILL 3-0** |

**The Lab's seed, answered (3-0):** where her pocket is empty, her flexibility is nothing. The cushion comes back after
the last cheque, in 2042, and the case's flexibility is "as the project develops" (:103), from 2033. Kai: "a refund,
not a roof." H25 does not cure the bad worlds (empty 44.5 in 100 in S6); it changes what the money is spent on: a
number she has said, not one she hasn't (Felix). That sentence belongs in the Final Report's "what we gave up".

**The practitioner, in its own words** (Kai, `../../huddles/2026-11-02_what-is-left-to-her/research/kai.md`): CME Group,
"101 Overview: CME Clearing Financial Safeguards Waterfalls",
https://www.cmegroup.com/articles/brochures-and-handbooks/101-overview-cme-clearing-financial-safeguards-waterfalls.html,
read 2 Nov 2026: "CME Clearing would utilize its own contribution to the relevant financial safeguards waterfall";
"pre-funded at $100 million for base products and $150 million for IRS products", ahead of "non-defaulting clearing
members' pre-funded contributions to the guaranty fund". Read through WebFetch only (the proxy refused the host to
curl and to `fetch_text.py`, re-tried by the chair at 15:30: 403), so the words are **not byte-checked**. What it
teaches: the owner's own layer comes first AND is a set sum kept for the moment others are exposed. V53 had the first
half and spent the layer before anyone was exposed.

## 4. The offer (landed by the chair from the votes; AI DRAFT (Claude, 2 Nov 2026); GPTZero: not yet checked)
| Where | V53 | Offer | Vote | Words |
|---|---|---|---|---|
| P8, last two sentences | "...and set it aside from the stocks Laura keeps, so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range." | "...and set it aside from the stocks Laura keeps, until only a quarter is left. Anything still missing lowers the whole range, before anyone hears it." | 3-0 on the words (Amara's "until only a quarter is left" and "Anything still missing", Felix's "set it aside"); Kai's comma after "keeps" kept by the chair: without it the clause reads as Laura keeping the stocks "until only a quarter is left" (a meaning fix, posted in parallel, so the other two never saw it) | 0 |
| P7 | "We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be quietly halved if markets turn." | "We could put the floor into stocks and chase a bigger gift to attract co-sponsors. But a number said aloud cannot be quietly halved if markets turn." | 3-0 (Amara; :110-112, why size matters) | +1 |
| P9, first sentence | "From 2033, the ladder becomes the operating reserve, paying out one bond per cheque." | "From 2033, the ladder and everything set aside for it become the operating reserve, paying out one bond per cheque." | 3-0 on the fix (Felix; :95-96 "must recommend its size": as written the reserve is the thing P8 says falls short), 2-1 on "everything" over Felix's "the money" | +6 |
| P5 | "That is under a tenth of her money." | cut | 2-1 (Felix, Kai; Amara would cut ", but the cheques never depend on it" instead, which Kai withdrew: it is the one place the 7.5% assumption is tied to the cheques, :146) | -8 |

**V53 with all four: 496 strict** (495 by spaces; `textcheck.py` on the chair's scratch copy, the same as Kai's). Amara's dissent kept for the thread: "under a tenth" is the only plain answer to the balance between
"pursuing growth and protecting the capital" (:72-74); if the thread keeps it, P9's +6 needs another payer.

## 5. V53 against every case line (Felix, ranked; checked by the chair)
1. **This one matters: flexibility** (:102-103, :145, :146-148) — offer above.
2. **The reserve's size** (:95-96) — offer above.
3. Holds, no sentence: inflation (P6's "costs more in Taiwan dollars" for the building; the locked TNA's TIPS reflection
   for the cheques, "an inflation risk that is nonexistent"; the case reads the three deliverables "together", :161);
   why half (FR); outside funding (implied by P1; FR); the cheques and certainty (:88-93, :97-98); composition as dates
   approach (P3, P5, P6, P9); good and bad markets moving the range (:118-120). Wharton does not expect a final range or
   confidence in the IPS (`../../WHARTON_WORD.md` s2).

`CORD:` (chair) the brief and the script's first docstring said the case's strategy bullets were missing from the text
export; Felix found them at :134-145 (the chair's line-numbering script had dropped tabbed lines). Fixed in the script.
`CORD:` (chair) Felix's post cites "Wharton :38" for "judged together"; that is our own gloss (LS-14, this morning). The
case's words are :161, "Evaluators will consider the three deliverables together". Corrected here and in the memo.
