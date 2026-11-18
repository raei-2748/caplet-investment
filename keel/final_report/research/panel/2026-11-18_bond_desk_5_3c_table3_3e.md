# Bond desk 5: 3c, Table 3 and 3e's two figures, read for precision (Wed 18 Nov 2026, evening, Sydney)

Reader: a fixed-income portfolio manager who builds Treasury and liability-matched portfolios. Question: would a desk
sign each figure and each word? Read blind: no other panel file, no SCORECARD, LESSONS or ARGUMENT_LOG. Nothing in the
repo was edited; scratch scripts in the session scratchpad, output to the terminal only.

## What I read (file, lines, Sydney time read)

| File | Lines | Read at |
|---|---|---|
| `FINAL_IPS_as_submitted.txt` | 1-24 (whole) | 19:44:30 |
| `NUMBERS.md` | 1-138 (header, section 0, section 1) | 19:44:32 |
| `NUMBERS.md` | 139-378 (sections 2, 3, bond desk 4's check figures) | 19:44:35 |
| `NUMBERS.md` | 379-634 (sections 4, 5, trade-day limit, "most") | 19:44:45 |
| `NUMBERS.md` | 987-1141 (8h) | 19:44:52 |
| `NUMBERS.md` | 1429-1474 (8m) | 19:44:57 |
| `NUMBERS.md` | 2207-2435 (8t, 8u, 8v) | 19:44:57 |
| `NUMBERS.md` | 841-869 (8d, for row 7's building-cost band); 1754-1800 (8q head) | 19:48:29; about 19:50 |
| `SKELETON.md` | l.45 (3c), l.47 (3e), l.274-306 (Exhibits list and open items) | 19:45:34; 19:45:36; 19:49 |
| `exhibits/tables.md` | whole (Tables 1-3, Figure 1) | 19:46:34-19:46:41 |
| `WORDS.md` | whole | 19:46:44 |
| `numbers/completion.py`, `plan.py`, `break_test.py` | the range rule, `zero_per_dollar`, `plan.run`, 8u's flexibility block | 19:46-19:50 |
| `CANON.md` | C19, D2 only (grep: the floor is the same fund as the 2033 rung) | 19:46:49 |

Other workers were writing tonight. At 19:54-19:55 `NUMBERS.md` (19:54:27), `SKELETON.md` (19:54:28) and
`exhibits/tables.md` (19:53:29) had new times. I checked the diffs against the commit. The changes were: Table 2's note
(no median figure; "past frequencies"); 3e area (1)'s median wording; a new 8q block (card Q131, strong Taiwan dollar
windows); a label in 8u's bottom row; section 5(c)'s $78,324. None of them changes a finding below. Line numbers are as
of 19:55. Table 3's rows are now at `tables.md` l.103-111 and Table 2's note at l.92.

## Findings

### High

**H1. 3e's note 2 sentence and WORDS name "the two Treasury funds behind the top". There is one fund.**
SKELETON.md:47 (note 2's figure: "what the two Treasury funds behind the top pay (the 2032 fund bought in January 2028
and the one the moved shares buy, each named ...)"). WORDS.md:35 ("the two Treasury funds behind the top"); WORDS.md:32
("put into the same kind of Treasury fund"). NUMBERS.md:2313 ("The two funds pay less than the top"), :318, :463.
Table 2's note, tables.md:92 ("the funds' costs").
- The floor and the shares moved before the 2031 meetings both buy IBTM, the late-2032 iBond fund. `plan.py`'s
  docstring says "IBTM again, maturing late 2032". CANON C19 and D2 say the floor is "the same fund (IBTM) as the 2033
  rung".
- IBTM is bought three times: for the 2033 payment (January 2027), the floor (January 2028) and the moved shares
  (before the 2031 meetings).
- Table 1 prints IBTM as "2033 and the floor" (tables.md:23). Figure 1's note says "the floor's IBTM shares are a
  separate lot".
- So a judge who checks will not find a second fund. A desk does not sign a sentence that names two funds where the
  holdings table shows one ticker.
- Smallest fix: "what the late-2032 Treasury fund pays on the two purchases behind the top (January 2028, and the
  shares moved before the 2031 meetings)". WORDS l.32: "the same Treasury fund". WORDS l.35's parenthesis: the same.
  In the register, "the two lots" or "the floor and the moved shares" in place of "the two funds".

**H2. 3e's note 3 figure ("about 25%") is given on "today's market rates", but that basis leaves out the share
forecast that makes up most of it.**
SKELETON.md:47 (note 3: "Figure: about 25%, on today's market rates (8u's basis, forwards with shares at 7.5%)").
WORDS.md:40 defines "today's market rates" as "the interest rates the bond market expects today".
- Of the $28,682, $21,179 is the half of VT kept, grown at J.P. Morgan's 7.5% a year for five years. Only the $7,503
  above the top comes from Treasury rates.
- So the figure moves with the share forecast. At 6.5% a year it is $27,159, covering 23.6%. At 5.0% it is $24,959,
  covering 21.7% (8v, my arithmetic).
- The 1-in-20 low simulated future covers 15.8% (8q l.1788: "The rise her flexibility covers 19 times in 20").
- Read by the report's own definition, "on today's market rates" says the figure rests on interest rates alone. That
  is the one thing 3e, the assumptions section, must not imply.
- A second precision point is in the same sentence. "A budget set on the $115,000 top" is her part of the building
  budget, not the building's whole budget. If the whole building's cost rises 25%, the co-sponsors' parts rise too.
- Smallest fix: "if shares earn the 7.5% a year assumed (Table 2's note), her flexibility plus anything above the top,
  about $28,700, covers a rise of about 25% in the US-dollar cost of her $115,000 part of the building budget".
- Table 3 row 7 (tables.md:111) prints "$28,700 in 2033" on the same basis. It needs the same five words in the note.

**H3. 3c's headline "about $95,000 to $115,000 on today's figures" is undated in the prose, and its bottom moves one
$5,000 step for about a tenth of a point in yields.**
SKELETON.md:45 (headline). WORDS.md:40 and :63-65 allow the basis to be said once, without a date.
- "Today" in the register is the 6 Nov 2026 close (section 0). 8u (NUMBERS.md:2312) gives the sensitivity: a fall of
  about 0.10 points before 1 Jan 2027 lowers the bottom to $90,000, and a rise of 0.09 points raises it to $100,000.
- I re-ran the plan on the 13 Nov 2026 par curve, the one section 5 (l.591) says was read at source. I used the same
  rule, the same IBTM holdings and VT at 7.5%. My scratch arithmetic, not a register figure:
  - the ten plus the extra Treasuries cost $330,402 in 1 Jan 2027 money (6 Nov: $337,499);
  - the first slice of the 2028 deposit is $31,859 (register via card Q98: $32,074);
  - floor money is $86,597;
  - the unrounded ends are $105,407 and $126,323, so the range is **$105,000 to $125,000**.
- So one week after the freeze, the same rule states a range $10,000 higher at each end.
- The register is right to stay on one curve. Without a date, though, a judge who reads "today's figures" in December
  reads a range that a week's market move had already shifted by two steps.
- Smallest fix: date it once in 3c's headline sentence, or at the head of Section 3 for every figure after it: "on the
  Treasury curve of 6 Nov 2026, the day trading froze". Table 2's note already does this.

### Medium

**M1. "About 2%" (3e note 2; Table 2's note "about 2% centrally") is a one-time share of what the fund pays. Fund costs
are quoted a year.**
SKELETON.md:47; tables.md:92; NUMBERS.md:2313.
- 2.32% is 1 - $115,000 / $117,731: a share of the whole zero-interest payout. The fee it sits beside, 0.07%, is a
  yearly rate.
- A reader who takes "2%" as a year reads about four times the real room. As a yearly cost beyond the fees, charged
  from each trade day, the top's room is used up at **0.58 points a year**, about eight times the fee. The bottom's is
  used up at 0.71 points a year (my bisection on `zero_per_dollar`'s method).
- SKELETON already guards the 0.5% ("one-time, never 'a year'", l.45) but not the 2%.
- Smallest fix: "about 2% of what it pays, in all", two words. Or give the yearly form once: "costs of more than about
  half a point a year beyond the fees".

**M2. A fund ended, merged or moved long before late 2032 is outside the 0.5% margin. Table 3 row 4 says the margin
meets the gap.**
tables.md:107 ("Changes: the fund; a gap met from the 0.5% margin the payments and the range each carry");
tables.md:125-126; NUMBERS.md:103 (section 0's haircut list counts "a fund swap under Table 3 row 4"); NUMBERS.md:321
and :469 ("true by construction").
- The margin pays for a trade's costs. It does not pay for the lost lock on the rate.
- Suppose the lots of the late-2032 fund are sold at net asset value on today's forwards and the cash then waits in the
  short-term Treasury ETF earning nothing, which is the standard "certain" is stated on. Then (my scratch run on the
  engine's IBTM holdings):

  | Exit date | What happens to the stated figures |
  |---|---|
  | 2 Jan 2031, after the move | Both lots pay $110,411: **$4,589 under the $115,000 top** |
  | 1 Jul 2031 | $112,744, **$2,256 under** |
  | 1 Jan 2032 | $115,172: covered, with $172 to spare |
  | 1 Jan 2029, before anything is stated | The floor lot pays $84,443, $10,557 under $95,000. This lowers what she could state; it breaks nothing |

- At today's market rates the short-term ETF earns roughly what was given up, so the gap belongs to the zero-interest
  standard alone.
- The table's own reservoir says "a gap beyond that is met only from interest the waiting cash earns" (l.126). The
  printed cell does not say so.
- One concentration point also belongs here. IBTM carries the 2033 payment, the bottom and the top, so one IBTM notice
  touches all three.
- Smallest fix, row 4: "Changes: the fund, for a Treasury or Treasury fund ending before the payment; a cost gap from
  the 0.5% margin". In 3e note 2's events or the register, name the fund being ended or merged before its last year as
  covered at today's market rates, not with cash waiting earning nothing. In section 0, take "a fund swap" off the list
  of things the 0.5% covers, or limit it to the swap's trading costs.

**M3. 3c's closing condition uses "the margin" where Table 2's note uses "the room".**
SKELETON.md:45 ("only if those costs passed the margin, with cash waiting earning nothing, would the contribution fall
short of the top, and Table 2's note says by how much"); tables.md:92 ("used up the room under the top ... about 2%").
- Centrally, costs past the 0.5% margin break nothing. The shortfall starts past 2.32%.
- "Only if" is logically a necessary condition, but a reader hears a trigger. The note then gives a different
  threshold for the same event.
- Smallest fix: "only if those costs used up the margin and the rounding down".

**M4. Table 3 row 1's "$57,455 if cash waiting earns nothing" is on a different basis from Figure 1, which defines that
phrase.**
tables.md:103; NUMBERS.md:2311 (8u: "$57,455 ... ($58,775 with the short-term Treasury ETF's fee)").
- Figure 1's title and note 1 define "if cash waiting earns nothing", and its figures carry the 0.15% fee ($444,080 +
  $55,920). Row 1's $57,455 carries no fee. On Figure 1's basis it is **$58,775**.
- Also in row 1: "the ten short $3,016 at today's rates" is the 2033 payment alone, the only rung left unbought.
- Smallest fix: "$58,775 if cash waiting earns nothing" and "the 2033 payment short $3,016".

**M5. Table 3 row 5: "prices within 0.5% of net asset value" does not cover the bonds and does not say which net asset
value.**
tables.md:108; NUMBERS.md:512, :542.
- (a) Five of the 2027 purchases and five of the extra Treasuries in 2028 are T-bonds, which have no net asset value.
  As printed, the row has no condition for them. Their 25-basis-point curve test sits in the reservoir only (l.127).
  On these bonds 25 basis points is **1.8% to 2.8% of price** (my repricing, January 2027 and January 2028), four to
  six times the funds' 0.5%.
- (b) A fund's net asset value is struck at the close. A limit order is set against the intraday indicative value or
  the prior close.
- Smallest fix: "funds: limit within 0.5% of the fund's indicative value". If a bond test is printed, give it in price
  or tighten it (the WInS fills were 2.6 to 8.8 basis points off the curve, 8m).

**M6. Table 3 row 7: an undefined "trend", and a scale figure that counts the currency alone.**
tables.md:111; NUMBERS.md:844 (8d); the new 8q block, Wed 18 Nov evening.
- (a) "Building-cost trend 1.5% to 5.0% a year" names no window.
  - DGBAS's latest year is +7.18% (October 2026), outside the band. The five-year rate, 3.19% a year, is inside it.
  - A reader who opens today's index sees a breach and a row with no trigger for it.
  - Fix: "five-year building-cost rise 1.5% to 5.0% a year (3.2% to October 2026)".
- (b) "$11,500 more on $115,000" is the Taiwan dollar alone.
  - The 8q block added tonight looks at the 30 two-year windows since 1991 when the Taiwan dollar was 10% or more
    stronger. In those windows the US-dollar cost of the building rose a median 22.3%, about $25,600 on the top, and
    never less than 9.3%.
  - So when this trigger fires, history puts the joint cost near the 24.9% her flexibility covers, not near $11,500.
  - Fix: "(the currency alone)" after $11,500. If room, the 22.3% median goes in the note.

**M7. 3e note 1(d), "Late, not short", is stated as a category. History supports it, but the plan does not guarantee
it.**
SKELETON.md:47 ("(d) Late, not short: a broker failure while the account holds more than SIPC covers"); NUMBERS 8t
(NUMBERS.md:2267-2268: "at risk only if that pool is short by more than SIPC fills").
- SIPC's $500,000 caps its own advance. Above it, Laura is short only if the broker's customer-property pool is short,
  which happens in fraud or commingling.
- A desk signs "late" and signs "short only if ...". It does not sign "not short".
- The set-up decision in SKELETON's Exhibits item 4(c) (two brokers, or confirmed excess cover, before the account
  passes $500,000 in August 2029) is in neither Table 3 nor note 1.
- Smallest fix: "late, and short only if the broker had lost customers' securities beyond what SIPC fills". If the
  event is named, name the set-up in the same clause.

### Low

- **L1.** SKELETON.md:45: "the 0.5% margin of the funds' value". The base is what the fund pays if cash waiting earns
  nothing, not its market value or net asset value. Say "0.5% of what the fund pays".
- **L2.** SKELETON.md:45: "both ends are Treasuries she already owns". They are units of a Treasury fund that holds the
  Treasuries. Say "owned through a Treasury fund" or "held for her" (the law's word, UCC 8-503). Book 19's strong
  words can stay on the Treasuries.
- **L3.** tables.md:113 (note): "cash dates: fund payouts, maturities, trade days". The iBond funds pay every month, so
  on this wording every month is a cash date and row 3's carry-on condition can never hold during a debt-limit
  standoff. SKELETON item 4 says "a fund's final payout". Say "fund end payouts".
- **L4.** tables.md:104: the five-business-day test is S&P's for long-term debt. I checked it at source, S&P Global
  Ratings Definitions: 'D' "unless S&P Global Ratings believes that such payments will be made within the next five
  business days in the absence of a stated grace period".
  - On S&P's short-term scale a bill has only its stated grace period. The waiting money sits in a bill ETF, so
    "any marketable Treasury" is looser than S&P for bills.
  - Fine as a team trigger. If a source is named, say "S&P's test for notes and bonds".
- **L5.** NUMBERS.md:2314 (8u) and 8q's "lower reading": "30.2% on the bottom" is $28,682 / $95,000. The contribution
  equals the stated top in every path, so a budget set on $95,000 has $48,682 behind it (51.2%). Keep it out of prose,
  or relabel it.
- **L6.** NUMBERS.md:2343 (8u's "Words for 3e") says "about 25%" goes with "on today's figures". SKELETON.md:47 says
  "never 'on today's figures'" for it. Align them, after H2.
- **L7.** SKELETON.md:45, the uncertainty clause: "lower if Treasury interest rates fall before the 2028 deposit is
  invested, higher if share prices rise". Both move it either way. Rates rose after 6 Nov, which on 13 Nov's curve
  would raise the bottom (H3). Say "Treasury rates before January 2028 and share prices before the 2031 meetings move
  it, up or down".

## Figures re-derived (mine against the register)

The first way uses the engine's own route, imported read-only (`plan.run`, `completion.rule`). The second way uses one
flat forward yield per trade day on the 4.2513% IBTM stand-in, with the fee compounded yearly: not the engine's pricing
loop. Everything is on the 6 Nov 2026 curve unless marked.

| Figure | Register | Mine, first way | Mine, second way |
|---|---|---|---|
| Floor money / moved shares' money | $81,244 / $18,349 | $81,244.28 / $18,349.05 | VT by hand: $29,593.75 x 1.075^3 x 0.9994^3 / 2 = $18,349.05 |
| What $1 pays at zero interest: floor / moved | 1.207415 / 1.070113 | 1.207415 / 1.070113 | 1.207557 / 1.070129 |
| Unrounded bottom / top | $97,605 / $117,142 | $97,605.08 / $117,142.45 | $97,617 / $117,154 |
| Stated range | $95,000 to $115,000 | same | same |
| Room under the top, cash waiting earning nothing | 2.32% | 2.320% | 2.33% |
| Room under the bottom | 3.16% | 3.156% | 3.17% |
| Room under the top at today's market rates | 6.12% | 6.125% | |
| The room as a yearly cost beyond the fees (top / bottom) | not in the register | 0.58 / 0.71 points a year | |
| The 0.5% margin as a yearly cost (floor / moved) | "one-time" | 0.11 / 0.27 points a year | |
| What the two lots pay / the excess | $122,503 / $7,503 | $122,503.13 / $7,503.13 | floor $102,365 + moved $20,138 by hand |
| Her flexibility plus anything above the top | $28,682 | $28,682.31 | $21,179 + $7,503 by hand |
| Rise it covers on the $115,000 top | 24.9% | 24.94% (a 25% rise needs $28,750: $68 short) | at 6.5% / 5.0% shares: 23.6% / 21.7% (8v's pots) |
| About $120 for each 0.1% past the room | $118 | 0.1% x $117,731 = $118 | |
| A $3,016 / $57,455 / $58,775 missed deposit | 8u | not re-run (asserted in `break_test.py`) | |
| Table 3 row 7: 10% stronger Taiwan dollar on $115,000 | $11,500 | $11,500 | |
| 25 basis points on the five T-bonds, in price | not in the register | 1.97% to 2.82% (January 2027); 1.82% to 2.68% (January 2028) | |
| Range on the 13 Nov 2026 curve (scratch, disclosed only) | section 5: first slice $32,074, floor $86,440 | first slice $31,859, floor $86,597, range $105,000 to $125,000 | |
| Forced exit to the short-term ETF, cash earning nothing | not in the register | top short $4,589 (2 Jan 2031) / $2,256 (1 Jul 2031); covered from about 1 Jan 2032 | |

Every register figure I re-derived matches to the dollar. The second way agrees within $12 at each end and 0.01 points
on each room. The gaps are in words, not arithmetic.

## Scores (precision, 1-5)

- **3c: 3.** The rule and both ends reproduce two ways to the dollar. What stops a desk signing is the wording: an
  undated "today" on a range that a week's market moved by two steps (H3), "margin" where the threshold is the room
  (M3), and "certain" stated without the fund being ended early, which sits outside the margin (M2). With the date and
  "the margin and the rounding down", this is a 4.
- **Table 3 (monitoring): 3.** Each trigger is dated and every figure is in the register, and the five-business-day
  default test matches S&P's definition. But:
  - the trade-day limit leaves the bonds without a test and does not say which net asset value (M5);
  - row 1's no-interest figure is off Figure 1's basis (M4);
  - row 4 promises the margin will meet a gap it cannot meet at zero interest (M2);
  - row 7's "trend" has no window and its scale figure counts the currency alone (M6).
- **3e: 2.5.** Both figures re-derive exactly, but neither sentence can be signed as planned. The 2% is set against
  "two Treasury funds" that are one fund (H1) and reads as a yearly rate (M1). The 25% rests on a share forecast that
  "today's market rates" hides (H2). About a dozen words fix both, and then this is a 4.
