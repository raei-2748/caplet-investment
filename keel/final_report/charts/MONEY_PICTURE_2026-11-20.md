# Where the money goes: a picture tested against Caplet's version 61 questions (Fri 20 Nov 2026, morning)

Analysis notes for the Final Report, not report prose. `OVERDRIVE_PLAN.md`, Fri 20 analysis line: "A picture of where the
money goes, tested against Caplet's version 61 questions." Files beside this note: `c5_where_the_money_goes.py` (the
script), `c5_where_the_money_goes.png` (192 dpi) and `.svg` (text kept as text). Rerun from the repo root:
`python3 -I keel/final_report/charts/c5_where_the_money_goes.py` (a few seconds; 26 figure checks, then the render, then
a fit-and-overlap check of every label).

## In brief

- **What it is.** One half-page figure that follows Laura's two deposits from the day each arrives to where each dollar
  ends up, on today's figures. Every pot the prose will name (the top-up, the extra Treasuries, the floor, the shares
  moved, the bottom, the top, her flexibility, what comes back) appears in it with its size, where its money comes from
  and what it pays, before any sentence has to name it.
- **Decision.** A new exhibit, the first figure of Section 3 (it becomes Figure 1 and the reserve figure becomes Figure
  2), taking the place of the c3 candidate ("when owned"), which it absorbs. It replaces no built exhibit and is not a
  change to the reserve figure. It costs about 12.8 double-spaced lines, a little over half a Letter page, about 180
  words of prose, and it pays for itself only if 3.0, 3a, 3b and 3c drop the sentences that would otherwise introduce
  each pot (named below). It goes in only if it wins the Mon 23 Nov fresh read against the same pages without it.
- **The test.** Of the 26 questions in WHY_V61_FAILED's table, the picture alone answers **12** (6 of them by showing
  that a step version 61 described is not in Caplet's plan at all), answers **8 partly**, and **6 not**. Three changes
  (below) would move it to about 18.

## 1. The design

**The question a judge should answer in five seconds:** where does each of Laura's dollars go, and when?

**Form.** A flow on a time line, drawn as a schematic: four date columns (Jan 2027, Jan 2028, Jan 2031, then Dec 2032
to 2042 for the uses) and one horizontal lane per holding, each starting on the day it is bought. The deposits are
dark bars at their dates, running across exactly the lanes they pay for, so "$300,000 deposited" visibly splits into
two lanes and "$150,000 deposited" into four. Each lane ends in an arrow to a white box that says what the money
pays for. Why this form and not the others:

- *Not a Sankey with widths to scale.* The $2,388 top-up would be 0.01 inch thick and the $18,349 of shares moved
  thinner than its label, so the small pots, which are most of Caplet's questions, would vanish. Lanes are equal in
  height and every amount is printed; the image says "Not drawn to scale". Proportions stay where they are read
  better: Table 1 (the holdings at cost) and the reserve figure.
- *Not a table.* A table gives the amounts but not the order of events, and Caplet's questions were as often about
  "when" and "why then" (bought in 2028, not 2031; both ends held for her in Treasuries before anyone hears them) as about "how much".
- *Not c3 ("when owned").* c3 showed four promises turning solid on their dates but not the money behind them; this
  picture carries c3's message through its fills (grey from the day a lane is bought in Treasuries, hatched while it
  sits in shares) and adds the dollars and the arrows.

**The one idea the layout is built around: the late-2032 fund is bought three times.** IBTM is drawn as one dashed
outline holding three purchases: $35,621 from the first deposit (completed by the $2,388 top-up) for the 2033 payment,
$81,244 from the second deposit (the floor), and $18,349 of shares moved in January 2031. Its first purchase has an
arrow up into the 2033 square; the other two join and feed the facility contribution. That single outline answers
"the fund behind the 2033 payment", "the 2028 holding" and "since when did it have a payout" at once, and it is the
plan's one concentration (NUMBERS 8w: $165,000 of the $615,000 promised rests on it), shown rather than said.

**Encoding (greyscale; checked: 0 non-grey pixels).** Light grey = Treasuries (held directly or through iBonds funds);
hatched = shares; white with a black rule = where the money goes; dark grey bars = deposits; dashed outline = one fund.
Identity is always carried by the words in the mark, never by tone alone (dataviz skill; `../exhibits/specs.md`
section 0). Liberation Serif (Times New Roman's metrics), 10 pt at printed size throughout, 6.5 x 3.76 in.

**Words.** Every label uses `../WORDS.md`'s names: the top-up, the extra Treasuries, the floor, the bottom, the top,
facility contribution, cash waiting, the world share fund (VT), the late-2032 Treasury fund. Two fixes made while
building it: $28,682 is labelled as her flexibility *and* what is paid above the top, never "her flexibility" alone
(WORDS l.28; NUMBERS, Thu 19 Nov); and the key says Treasuries "held to the end, they pay out on set dates", not "pay a
set sum", because an iBonds fund's payout is not fixed (Trading Note 2; WORDS: "certain" and "guaranteed" never take a
fund's payout as subject). No pencil or ink in the picture (CONCEIT V2.2: the conceit is said beside an exhibit, never
in it); the prose beside it can say that everything grey is in ink from the day its lane starts, and the hatched half
never is.

**Labels in the image, top to bottom.**
- Header: "Jan 2027 / $300,000 deposited"; "Jan 2028 / $150,000 deposited"; "Jan 2031 / half the shares move, then she
  tells co-sponsors $95,000 to $115,000"; "Dec 2032 to 2042 / where the money goes, on today's figures: Treasury yields
  of 6 Nov 2026; shares 7.5% a year".
- Lanes: "$264,379: Treasuries for 2034–2042 (four iBonds funds, then five Treasury bonds)"; "$36,774: extra
  Treasuries"; the late-2032 fund's three purchases ("$35,621", "+ $2,388 top-up: together they pay the 2033 payment";
  "$81,244: the floor; pays $102,365 in Dec 2032"; "$18,349; pays $20,138"); "World share fund (VT)": "$29,594,
  growing 7.5% a year", "half of $36,698 moves", "other half".
- Uses: "Ten payments of $50,000, each 1 January" with ten squares 33 to 42; "Extra Treasuries fill any gap in the ten if
  cash waiting earns nothing. If rates hold they are never needed, and all of it is hers by 2042: $46,566, valued at 1
  January 2033"; "Facility contribution: $115,000, the top / the bottom, $95,000: held in Treasuries since 2028 / the
  rest, $20,000: from the shares moved in 2031 / Each end is counted below the expected payout"; "$7,503 above the top"
  (arrow down); "Her flexibility, $21,179 in shares, and $7,503 paid above the top: $28,682 in 2033, promised to no
  one, for building costs that overrun, a stronger Taiwan dollar or a co-sponsor falling short".

**What the picture leaves out on purpose:** the reserve's size on 1 Jan 2033 (printed once, in 3a, WORDS); cash waiting
and each payment's split between its own Treasury and the extra Treasuries (the reserve figure's job); the range's
uncertainty before the move (Table 2's job); the operating reserve as a named bracket (the label would cost a line and
answers none of Caplet's questions).

## 2. Every figure in the picture, with its source

All on today's figures: the Treasury curve of 6 November 2026 and its forward rates, world shares at J.P. Morgan's 7.5%
a year (NUMBERS section 0). The script reads each modelled figure from the engine's results files and stops if it
differs from the register's printed figure; the two first-deposit sums are Keel arithmetic on NUMBERS section 1's rung
table and are checked to add to $300,000.

| Printed | What it is | Source | Read from | Check |
|---|---|---|---|---|
| $300,000; $150,000 | The two deposits, Jan 2027 and Jan 2028 | The case; FACTS_PLAIN | (typed) | Lanes add to each |
| $264,379 | The nine Treasuries for 2034-2042 bought in Jan 2027 (four iBonds funds $133,875, five bonds $130,504) | NUMBERS 1, rung table: $36,065 + $34,300 + $32,588 + $30,922 + $29,136 + $27,567 + $26,051 + $24,582 + $23,168 (Keel arithmetic) | `results_2026-11-17.json` C3 rungs | $264,379 + $35,621 = $300,000 |
| $35,621 | The 2033 payment's share of the late-2032 fund bought in Jan 2027 | NUMBERS 1: the 2033 rung, $37,908, less the $2,287 still unbought in 1 Jan 2027 money (Keel arithmetic; 8w calls it the own lot with "$2,287 tail Jan 2028") | C3 rungs, ten instruments $302,287 | as above |
| $2,388 | The top-up: completes the ten, into the 2033 payment's fund | NUMBERS 2 (headline), 8a ("The IBTM tail"); WORDS; FACTS_PLAIN | `results_topup_2026-11-17.json` | 2028 deposit adds to $150,000 |
| $36,774 | The extra Treasuries (more of the 2036-2042 Treasuries) | NUMBERS 2 (backstop table), 4 | `results_topup` | as above |
| $81,244 | The floor: more of the late-2032 fund, Jan 2028 | NUMBERS 4 ("Floor money", 54.2%) | `results_2026-11-17.json` plan H_plain central (left over less VT) | as above |
| $29,594 | VT bought, Jan 2028 | NUMBERS 4 | same | as above |
| 7.5% a year; $36,698 | VT's growth assumed; VT on 1 Jan 2031 | NUMBERS 0 (J.P. Morgan 2027); NUMBERS 4 | same | |
| $18,349 | Half the shares, moved into the late-2032 fund in Jan 2031 | NUMBERS 8w (moved money) | $36,698 / 2 | |
| $102,365 | What the floor pays, Dec 2032 | NUMBERS 4 ("Floor payout"), 2 | same | |
| $20,138 | What the shares moved pay, Dec 2032 | NUMBERS 4 ("The moved half, paid late 2032") | same | $102,365 + $20,138 = $122,503 (NUMBERS 4) = $115,000 + $7,503 |
| $95,000; $115,000 | The bottom and the top; the facility contribution is the top | NUMBERS 4 ("Bottom/Top Laura states", "The 2033 contribution") | central rule | |
| $20,000 | The top less the bottom: the part the shares moved in 2031 added | Arithmetic on the two stated figures; FACTS_PLAIN ("The 2031 move added the rest") | | |
| $7,503 | Paid above the top, to her | NUMBERS 4 ("Excess"), 8k | central rule | |
| $21,179 | The other half of the shares on 1 Jan 2033: her flexibility | NUMBERS 4 ("Half kept"), 8k | central | |
| $28,682 | Her flexibility plus what is paid above the top, 1 Jan 2033 (prose: "about $28,700") | NUMBERS 4, 8k; WORDS l.28 | central rule | $21,179 + $7,503 |
| $46,566 | What comes back from the extra Treasuries if rates hold, valued at 1 Jan 2033 ($75,934 by 1 Jan 2042) | NUMBERS 2, 4, 8h, 8k; WORDS ("about $46,600") | `results_returns_2026-11-17.json`, `results_reserve_2026-11-17.json` | |
| $50,000 x 10 | The ten payments, 1 Jan 2033 to 2042; the 2033 one paid by the late-2032 fund's own purchase | The case; NUMBERS 8w ($50,000 at today's forwards; $47,338 if cash waiting earns nothing, the extra Treasuries paying $2,662, 8h) | `results_one_fund_2026-11-19.json` | |

FACTS_PLAIN version 3 (Fri 20 Nov) changes no figure in the picture. It names the fund "IBTM, the fund that closes in
mid-December 2032" where the picture, WORDS and NUMBERS say "the late-2032 Treasury fund (IBTM)"; the group label can
take version 3's name in one edit of `c5_where_the_money_goes.py` if WORDS adopts it. Version 3 also keeps "owned"
off dollar figures ("held for her"); the picture never calls a figure owned.

Every figure matches the task brief's list (FACTS_PLAIN version 2): $36,774, $2,388, $81,244, $29,594, the top $115,000,
the bottom $95,000, about $21,200 and about $28,700 in all. One addition the brief did not list and the picture needs:
the first deposit is split by lane ($35,621 into the late-2032 fund for 2033, $264,379 into the other nine), so the
2033 payment's Treasury can be drawn inside the late-2032 fund. Said in words that is "five iBonds funds for 2033-2037,
five bonds for 2038-2042", as the brief asks; the lane label says "four iBonds funds, then five Treasury bonds" because
the fifth fund is the late-2032 fund, drawn in its own outline.

## 3. Decision: a new exhibit, first in Section 3, in c3's place

**Where.** The head of Section 3 (3.0), where the report turns from the competition portfolio at $300,000 (Section 2,
Table 1) to Laura's plan for both deposits at $450,000. Not Section 2: its headroom is 46 words (`../exhibits/specs.md`,
Page cost), and two scales in one section read as two plans (coherence readers 4 and 6). 3.0's aha is "certainty has
dates" (SKELETON l.229), which this picture shows by its columns. APA numbers figures by first call-out, so it becomes
Figure 1 and the reserve figure becomes Figure 2 (Tables 1-3 keep their numbers).

**Why not a replacement or a change.**
- *Not a replacement for the reserve figure.* That figure is the evidence for the standard, payment by payment ($47,338
  + $2,662 = $50,000 if cash waiting earns nothing), and the case asks for the reserve's composition "as the annual
  payments approach and are made". This picture says the extra Treasuries fill any gap; it cannot show that they do.
- *Not a change to the reserve figure.* Adding the floor, the shares and her flexibility to it would cost more than a
  separate half page and give a judge two five-second questions in one frame.
- *Not a replacement for Table 2 or Table 3*: different questions (markets; monitoring).
- *It does replace c3*, a candidate never in the budget, so the four built exhibits stand as they are.

**What it costs.** The image is 6.5 x 3.76 in: 9.8 double-spaced lines (27.6 pt each). With its number, a one-line title
and the blank line after, 12.8 lines, 0.55 of a Letter page (23.5 lines); with a two-line title 13.8 (0.59). A note
of about 35 words adds 2.5 lines. That is about 180 words of prose (about 215 with the note). Section 3 has no
headroom (SKELETON l.10: budget 1,900 words, ceiling about 1,960), so the picture is paid for by the words it makes
unnecessary, and only if they are cut:

| Where | Words the picture replaces (the reason stays; the inventory goes) | About |
|---|---|---|
| 3.0 | The sentence that lists what is bought when; 3.0 calls the figure out and keeps its claim and "certain" | 25 |
| 3a | What the 2028 deposit's first dollars buy (the top-up, then the extra Treasuries) and what comes back if rates hold; 3a keeps the standard, its price and Figure 2 | 35 |
| 3b | Her flexibility's make-up (half the shares plus what is paid above the top) | 20 |
| 3c | The range rule's description beyond one sentence (the bottom from the floor; the top adding the shares moved) | 30 |
| Figure 2's note (the reserve) | Item 2's purchase line and item 6's top-up clause | 30 |
| Table 2's note | "flexibility: the half of VT promised to no one plus whatever the fund pays above the top" | 20 |
| Table 3's note | The $39,162's two parts, now in the picture | 12 |
| **Total** | | **about 170** |

The last 10 to 45 words (with or without a note) are the lead's call. A half-page version exists if needed: move the
"Extra Treasuries ..." box's sentence into the note and the image drops to about 3.4 in (11.9 lines, half a page).

**The condition.** DESIGNS.md's rule stands: four exhibits by default, a fifth only if it wins a cold read. Send it
to the Mon 23 Nov fresh reader with only its title, and to a literal reader told to use only what the page shows,
calibrated first on Caplet's 17 lines (WHY_V61_FAILED, "What Keel's own readers and its prediction missed"). The
question test below is Keel's own reading and should not be believed until a literal reader repeats it.

**Note items (for 27 Nov; not wording).** Modelled, on today's figures (dated once); "cash waiting" defined as money a
bond or fund has paid out that waits for the 1 January payment it belongs to (or a pointer to Figure 2's note, which
defines it); what an iBonds fund is (change 3); the bottom and top counted as if cash waiting earns nothing, less 0.5%,
rounded down (change 1, if not drawn); amounts in each lane's own year's dollars, $46,566 valued at 1 January 2033.

## 4. The question test

One row per question in WHY_V61_FAILED's table ("Where Caplet caught it"), in its order, then four more from Caplet's
full list (Book 22) that the table folds into its rows. Strict reading: "yes" only if a reader who knows only the case
can answer the question from the picture alone, including where the money comes from; a label that names a thing
without showing its source or its reason is "partly". "Moot" marks a question about a step version 61 described that
is not in Caplet's IPS (WHY_V61_FAILED, "Two questions were about a design Caplet never chose"): the picture answers it
by showing what the plan actually does.

| # | Caplet's question | Picture alone | What it shows | What the prose still has to give |
|---|---|---|---|---|
| 1 | "a balanced mix" (what is it; how is "the last third" used) | **No** | The plan, not the mix it was compared with (it does show "how it's going to be invested", Caplet's sub-question) | Nothing, if the contrast is dropped (WHY note 5); otherwise the mix itself, before the comparison |
| 2 | "the fund behind the 2033 payment" | **Yes** | One outline, the late-2032 Treasury fund: its $35,621 from the first deposit plus the $2,388 top-up pay the 2033 square | Why one fund does two jobs: no Treasury bond on the list matures between February 2031 and February 2036 |
| 3 | "the 2028 holding" (and "since when did it have a payout") | **Yes** | $81,244 of the 2028 deposit, the floor, inside the same fund; pays $102,365 in Dec 2032 | Why most of the 2028 deposit goes there (IPS l.15) |
| 4 | "the bottom" | **Partly** | $95,000, the part held in Treasuries since 2028, fed by the floor | Why $95,000 and not $102,365: counted as if cash waiting earns nothing, less 0.5%, rounded down (change 1) |
| 5 | "the top" | **Partly** | $115,000 = $95,000 + $20,000 from the shares moved; the facility contribution; $7,503 above it goes to her | The same rule, and why co-sponsors count the top |
| 6 | "both ends" (held for her in Treasuries before anyone hears them) | **Yes** | Both purchases sit in the grey fund before the Jan 2031 column, where "then she tells co-sponsors $95,000 to $115,000" | "Certain", once, with the stated range as its subject |
| 7 | "the extra reserve" | **Yes** | $36,774 of the 2028 deposit, extra Treasuries; their job and what comes back ($46,566 by 2042) | What "cash waiting earns nothing" means (row 20) |
| 8 | "the tenth rung" | **Partly** | The tenth square, 2042, paid by the Treasuries for 2034-2042 | Nothing, if the report never says "rung" (WORDS bans it) |
| 9 | "the difference" ("roughly its interest") | **Yes** (moot) | VT is bought with $29,594, the last part of the $150,000 after $2,388, $36,774 and $81,244: there is no "difference" | Only "the rest of the 2028 deposit" |
| 10 | "the rest" ("the 2028 holding's payout makes up the rest") | **Yes** (moot) | The extra Treasuries come from the 2028 deposit in 2028; the floor makes up nothing | Nothing |
| 11 | "after this" ("what that holding will pay after this") | **Yes** (moot) | The floor's lane runs untouched from Jan 2028 to Dec 2032 | Nothing |
| 12 | "what they hold" ("paying out what they hold") | **No** | Funds pay out in December; nothing says the payout is what their Treasuries are worth | One sentence on what an iBonds fund is (change 3) |
| 13 | "what was set aside for it" (the tenth payment) | **Partly** | The extra Treasuries fill any gap in the ten | Which holdings and interest pay the 2042 payment (Figure 2's last row) |
| 14 | "the money waiting for them" | **No** | "Cash waiting" appears only as a condition | Figure 2 draws it (the 10.5- and 7.5-month waits); the prose names it once (change 2) |
| 15 | "anything paid beyond the top" | **Yes** | "$7,503 above the top" arrow into her flexibility | Nothing |
| 16 | "bought in 2028, not 2031" (where did 2031 come from?) | **Partly** | The floor is bought the month the 2028 deposit arrives; 2031 is when half the shares move | Only if the rival is raised (NUMBERS 8c), its reason; otherwise no contrast at all |
| 17 | "up to half" (why "up to"?) | **Yes** (moot) | Exactly half: "half of $36,698 moves", "other half" | Nothing |
| 18 | "whatever of the first half isn't sold" | **Yes** (moot) | The other half is kept, never sold for the range: $21,179 in 2033 | Nothing |
| 19 | "bought in 2028, not 2031, because the residency can't depend on shares" (the middle step) | **Partly** | The floor's money is grey (Treasuries) from 2028; only the hatched lane rides on shares | The middle step: waiting until 2031 would keep that money in shares until then |
| 20 | Reinvestment risk ("interest arrives years before the payment it serves, so money waits") | **No** | The cover (extra Treasuries) and its condition, not the risk | Which holdings pay interest when, and what it costs if it earns nothing: the Nov 2039 bond, $43,197 from its own interest and face, $6,803 from interest on that interest (NUMBERS 8a; WHY_V61_FAILED) (change 2) |
| 21 | "would swing like the shares of a heavily borrowed company" | **No** | Nothing to draw | Nothing, if the image goes (WHY note 8) |
| 22 | "she sells the other half" (why sell the second half as well?) | **Yes** (moot) | Only one half moves; the other stays in shares as her flexibility | Nothing |
| 23 | Two figures, when "we already know how much money we will have" | **Partly** | The two figures are two things with two dates (held since Jan 2028; added by shares in Jan 2031), both bought before she speaks, and the contribution is the top | Why state two at all: the case asks for a range and a confidence; co-sponsors are told to count the top (WHY_V61_FAILED, "Why two figures") |
| 24 | "Five are funds of Treasuries that all mature in one year" (false as read) | **Partly** | Ten squares, one per year; four iBonds funds for 2034-2037 plus the late-2032 fund for 2033 | That each fund holds Treasuries maturing in a year of its own (change 3) |
| 25 | "she keeps room as the project develops" | **Yes** | $28,682: $21,179 in shares and $7,503 above the top, promised to no one, for the IPS's three uses | What each use might cost ($11,500 for a 10% stronger Taiwan dollar; about 25% building-cost cover, NUMBERS 8u) |
| 26 | "the plan's biggest strength" | **No** | Not a picture's job | Delete it (WHY note 10) |
| S1 | "it costs less than it returns" | Yes | The floor costs $81,244 and pays $102,365 | |
| S2 | "the shares only risk that interest"; "since when was VT only funded by whatever 'interest'?" | Yes (moot) | VT is bought with $29,594 of the deposit, not with interest | |
| S3 | "if that half falls short" | Yes (moot) | No step in which half the shares buys the extra Treasuries | |
| S4 | "what ... does 'a fund's payout isn't fixed' have to do with a margin?" | Partly | "Each end is counted below the expected payout" | The reason, in one sentence (change 1) |

**Count, the 26 table rows:** yes 12 (rows 2, 3, 6, 7, 15, 25 on Caplet's own design; rows 9, 10, 11, 17, 18, 22 moot),
partly 8 (rows 4, 5, 8, 13, 16, 19, 23, 24), no 6 (rows 1, 12, 14, 20, 21, 26). Of the questions the brief named,
the picture answers the fund behind the 2033 payment, the 2028 holding, both ends, the extra reserve, the difference,
"she sells the other half" and what her flexibility pays for; it answers the bottom, the top, the tenth rung, "why
2028 not 2031", "why two figures" and the five funds only in part. Of the 6 noes, three (1, 21, 26) are not picture
questions at all: the prose fixes them by deleting a sentence.

## 5. Three changes that would answer the questions still open

1. **Draw how each end is counted (rows 4, 5, 23, S4).** One line under the contribution box, or the note's first
   item if the line does not fit: "$102,365 expected; $98,096 if cash waiting earns nothing; $97,605 after 0.5% off;
   $95,000 rounded down", and for the top "$122,503; $117,731; $117,142; $115,000" (NUMBERS 4 and 8w; $98,096 x 0.995 =
   $97,605 and $117,731 x 0.995 = $117,142, checked). A reader then sees that the gap is caution, not a leak, and that
   the payout above the top is hers. Cost: about 0.3 in (one line of prose's worth) in the picture, or about 30 words
   in the note. Moves 4, 5 and S4 to yes and 23 nearer (its last step, why a range at all, stays prose).
2. **Leave interest and cash waiting to Figure 2, and put it next (rows 13, 14, 20, 8).** The picture should not try to
   show interest: it would need a strand from every Treasury lane and would double the labels. Figure 2 already draws
   cash waiting. What it lacks is the one worked example Caplet asked for: in its note or 3a's prose, the Nov 2039 bond,
   bought for about $26,000, repays $27,536 and pays $15,661 of interest along the way ($43,197 in all), so the other
   $6,803 of the 2040 payment must come from interest earned on that interest while it waits; the extra Treasuries
   cover it if that interest earns nothing (NUMBERS 8a, WHY_V61_FAILED). Placing the money picture directly before
   Figure 2 lets 3a's first sentence point from one to the other. Moves 14 and 20 to yes in the pair (not in this
   picture alone), and 13 and 8 with them.
3. **Say what an iBonds fund is, in the picture (rows 12, 24).** Two brace labels over the squares, "iBonds funds" over
   33-37 and "Treasury bonds" over 38-42, and a key entry or note line: "an iBonds fund holds Treasuries that mature in
   one year, closes that December and pays out what they are then worth" (FACTS_PLAIN). Cost: about 0.17 in for the
   braces (the header's basis line would move to the note to make room). Moves 12 and 24 to yes.

With changes 1 and 3 the picture alone answers about 17 of the 26 (rows 4, 5, 12, 24 added; 23 still partly); with
change 2, Figure 1 and Figure 2 together answer about 21. The rest are prose: row 1 (drop the contrast), 16 and 19
(give the reason, or raise no rival), 21 and 26 (delete).
