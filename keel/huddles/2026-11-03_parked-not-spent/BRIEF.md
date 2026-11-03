# FICTION (the room) + real work. Huddle H-024: parked, not spent? (Laura's Room, Tue 3 Nov 2026, round 7 beat 6)

> (Keel is a simulated team, AI-written.) AI-generated (Claude Code). Chair: the room's run (Laura's Room, host Amara).
> Members: **Amara** (reads as a SIMULATED co-sponsor deciding whether to give, and as a SIMULATED Laura built only
> from the case; never quoted as Laura's words), **Kai** (reads as the practitioner from the field the lock came from,
> in the practitioners' own published words), **Felix** (reads as a competition judge with the case and Wharton's
> instructions open). Three agents, three rounds (rounds 2 and 3 continue the same three agents): 9 posts. The chair
> runs scripts and counts, assembles, and writes no member's lines.

## The beat (round 7, beat 6: "the second angle")
The Genius Lab (13:40, huddle H-023, `../2026-11-03_interest-that-earns-nothing/`) left four challengers. Read each
three ways (co-sponsor, judge with the case open, practitioner) and **kill, sharpen or pass** it, with the case line it
rests on. Then check what survives against the case's requirements.
- **C1, Kai's lock (Lab: ADOPT).** On the day Laura names her range (2031), set aside what the ladder would be short
  if every dollar it pays from then on (coupons, and maturing bonds waiting for their January) earned nothing; buy it
  in Treasuries maturing before each January; never look again. Lab's IPS wording (Jun), V54 P8:
  "at that day's yields, plus a cushion," -> **"as if money paid later sat idle,"** (497 strict, +0).
- **C2, the bank's note "bond first"** (Lab: BIN). **C3, a plain word for how likely the top is** (Lab: BIN for the
  IPS, Final Report). **C4, "the faces add up to less than the cheques"** (Lab: Final Report only).

## The question for this huddle
**Kai's lock keeps every cheque and the named range safe. Who pays for it, does the IPS say so plainly enough for each
reader, and what (if anything) should change in P8 or P9 today?** Today is the last day anything new is promoted; the
final AI draft goes to Caplet at the end of Wed 4 Nov. The Writing Room reads wordings to strangers at 16:20.

## The text (V54, `../../ips_rewrite/drafts/D34/ips_V54.txt`, AI DRAFT, 497 strict, the limit; GPTZero not yet checked)
- Pitch: "Laura's ten $50,000 cheques are a promise, so we don't invest for them. We buy them. Her first $300,000 buys
  Treasuries that each mature before a January. Her 2028 deposit buys a Treasury floor for her building gift, and only
  the interest that floor should earn goes into world stocks."
- P6: "In 2031, Laura gives co-sponsors a range for her facility contribution. The bottom is her floor, rounded down:
  money she already owns. The top adds half her stocks. Before she names it, that half moves into Treasuries, so every
  dollar she promises is already in bonds. The other half stays with Laura, liquid any day, as her flexibility, in
  case the building costs more in Taiwan dollars."
- P7: "We could put the floor into stocks and chase a bigger gift. But a number said aloud to co-sponsors cannot be
  quietly halved if markets turn."
- P8: "The weak point is reinvestment. The ladder costs less than the cheques because its bonds pay interest along the
  way, which we reinvest. If yields fall and stay low, that interest earns less, and the ladder falls short. Before
  she names the range, we price that gap at that day's yields, plus a cushion, and move that much from the stocks
  Laura keeps into Treasuries, so her flexibility shrinks before her gift does. Whatever the stocks can't cover lowers
  the whole range."
- P9: "From 2033, the ladder and the money set aside for its gap become the operating reserve, paying out one rung per
  cheque."
- Last line: "Do not crush." (P2 defines crushing: "selling it before it matures, even for the building.")

**Wordings on the table for P8 (counts by `../../office/tools/textcheck.py`, strict):**
- J (the Lab, Jun): "we price that gap as if money paid later sat idle," -> 497.
- A (the chair's, to be attacked, not adopted on sight): "we price that gap as if nothing more is reinvested," -> 496.
  Reason offered: P8 names the weak point with its own word, "reinvest"; A prices it out with the same word.
- P9 add-on, if anyone wants it (the chair's, to be attacked): "paying out one rung per cheque and handing back to
  Laura whatever each rung didn't need." -> +10 words (would need 9-10 words cut elsewhere; name them if you back it).

## The case lines (`../../../competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`)
- :91-92 "All ten payments must be funded by the investment portfolio with a high degree of certainty."
- :94-99 "At the beginning of 2033 ... Laura will set aside a portion of the portfolio to fund the ten payments. This
  set-aside is called the operating reserve. Teams must recommend its size and initial asset composition and explain
  how its composition should change, if at all, as the annual payments approach and are made. They should also define
  what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and
  identify the assumptions supporting their recommendation."
- :101-103 "After establishing the operating reserve in 2033, Laura must decide how much of the remaining portfolio she
  can responsibly contribute ... She recognizes that committing all remaining assets could limit her financial
  flexibility as the project develops."
- :109-116 "Laura plans to begin approaching potential co-sponsors in 2031 ... A meaningful personal contribution may
  signal that the residency is financially viable ... If Laura promises more than she can ultimately contribute, she
  could damage her credibility and lose the confidence or participation of co-sponsors. Rather than promising one exact
  amount, she wants to communicate a credible range for her potential contribution."
- :117-120 "Teams must recommend the dollar range Laura should communicate and state how confident they are that her
  2033 contribution will fall within that range ... The proposed range must also protect the portfolio's ability to
  fund the ten-year operating commitment."
- Strategy bullet (p.4): "Preserves appropriate financial flexibility when determining the facility contribution."
- :146-148 "Teams should identify and explain their assumptions about investment performance, the timing of cash flows,
  outside funding, the effect of inflation ... and the financial flexibility Laura should preserve."

## Wharton's IPS instructions (`../../WHARTON_WORD.md` s2; rank above everything)
- Question 4: "How will the portfolio's asset allocation and composition change as future funding needs approach and
  payments are made?"
- "establish your strategic approach to preparing for the operating commitment, managing the operating reserve's asset
  composition over time, determining a responsible facility contribution, and preserving appropriate financial
  flexibility."
- "Not expected in the IPS (they belong to the Final Report): ... a final facility-contribution range, or the draft
  communication to co-sponsors." "Focus on the strategy and decision-making framework ... rather than ... presenting
  detailed financial calculations."
- Judges want "the reasoning, assumptions, and tradeoffs behind those decisions."

## The numbers (MODEL; Book 11: none of them goes into the IPS)
STAMP: L-17 `../../rooms/lab/L-17_interest_that_earns_nothing/results.json` | curve 22 Oct 2026 | J.P. Morgan 2027
world stocks 7.5% | 200,000 paths, seed 20261016 | V54's design. W0f = V54 as written; A0f = V54 plus an unnamed
January 2033 second look (what the old model did); KW = Kai's lock, WInS-true. Worlds: base / yields 2 points lower for
good / yields 1 point lower before the build and the 2028 deposit halved.

| | W0f (V54 as written) | A0f (+ unnamed 2033 look) | KW (Kai's lock) |
|---|---|---|---|
| Every cheque paid in full | 96.0% / 94.4% / 95.8% | 99.87% / 99.85% / 98.6% | 100% / 100% / 98.7% (shorts only where the money to buy a rung or the lock never existed) |
| Gift taken to pay a cheque after the range is named | never | 8.1% / 24.1% / 22.6% (about $1,800 each time) | never |
| Top of the named range reached | 99.3% / 99.6% / 99.9% | 97.8% / 95.9% / 95.8% | 99.3% / 99.6% / 99.8% |
| Stocks Laura keeps: all gone by 2033 | 17.5% / 63.6% / 85.6% | 19.0% / 65.4% / 86.1% | 28.1% / 72.8% / 90.3% |
| Stocks Laura keeps in Jan 2033, median (base) | $14,319 | $13,910 | $8,746 |
| Range lowered on naming day (before anyone hears it) | 16.9% / 62.9% / 83.5% | the same | 26.9% / 71.9% / 89.1% |
| Lock cost on naming day, median / 95th pct (base) | ($7,500 cushion + that day's gap) | the same | $11,635 / $24,893 |
| Not needed by the cheques, back to Laura as rungs pay, median (base; incl. the 2027 leftover) | n/a | n/a | $17,953 |
| Gift mean | $159,980 / $141,826 / $37,530 | $159,956 / $141,771 / $37,464 | $159,286 / $141,580 / $35,983 |
| Laura's own money in 2042, mean | $49,678 / $24,038 / $13,402 | $49,270 / $23,725 / $13,409 | $48,722 / $24,914 / $17,639 |

Reading the table: the lock is paid for by **Laura's flexibility in 2033**, not by the gift or the cheques. Most of it
comes back to her **after** 2033, rung by rung, because the cheques almost never need the full zero-rate amount. The
room's own Monday call (LR-10, H-017: keep a quarter of her kept stocks back on naming day) was not taken into V54.

## Each member's job (round 1, alone, nobody sees anyone else's post)
- **Amara:** read V54 + C1 as (a) a co-sponsor's programme officer deciding whether to give, (b) a SIMULATED Laura,
  case only: what scares her, what she wouldn't understand, does the range overpromise. Which case line decides it?
- **Kai:** the practitioner. The lock is a public-finance idea: escrows sized "sufficient, without reinvestment" (MWRA
  2025-2 Defeasance Escrow Agreement, s3, found by the Lab today). In the practitioners' own published words (escrow
  agreements, official statements, GFOA/MSRB/rating-agency pages, pension or structured-settlement actuaries): how do
  they word the zero-reinvestment assumption, what happens to the money the payments didn't need, and what would they
  ask of P8 and P9? At least two primary sources, quoted with URL and date read.
- **Felix:** a competition judge with the case and Wharton's instructions open. Kill, sharpen or pass C1-C4, each with
  the case or Wharton line. Then: does V54 + C1 answer :94-99 (reserve size, composition, change as payments are made;
  certainty defined, evaluated, assumptions named), :117 ("state how confident"), and "appropriate financial
  flexibility"? Name the weakest answer and the exact sentence that would fix it.

## Rules
- Posts at most 350 words, in the member's own voice (`../../VOICE.md`), headed `**Name** (round N)`. Research notes go
  to `research/<name>.md` (URL, date read, the quoted line, what it means for us).
- Fetch pages with `python3 keel/library/insight_v1/scripts/fetch_text.py URL [--grep "phrase"]` (WebFetch is blocked).
  Quote near-verbatim and say "via the fetch tool".
- Book 11: no model numbers, "our model" or citations in the IPS; no team history; every sentence plain; the motif
  stays light. Commandments: no "every team will"; any number says where it came from. 497 strict is the IPS limit.
- Never contact anyone; no personal data; never WInS or SMApply. Simulated people are tests, never quotes.
