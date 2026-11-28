# Graphics plan: an adversarial review (Sat 28 Nov 2026)

Reviewed: Caplet's "Visual Identity and Graphic Concepts" proposal (thread message, Sat 28 Nov, 21:22 Sydney), checked
against the draft in the "big w's big w" tab of the Final Report Google Doc (read in full, read only), the "IPS" tab,
`keel/final_report/NUMBERS.md`, the model outputs in `keel/final_report/numbers/`, and Wharton's Final Report
instructions (`keel/final_report/WHARTON_NORTH_STAR.md` section 0). Nothing in the Doc was edited and no final graphic
was made. The independent numbers rebuild (`AUDIT_2026-11-28.md`) had not landed when this was written, so every check
below is against the register and the model files; where the two disagree, the audit wins.

## The short answer

1. **Make two figures, not five, and let each one replace something.** The draft is already at or over Wharton's page
   limits (section 3 below), so a graphic that adds paper breaks a minimum requirement.
2. **Your Figure 5 is the best idea in the proposal. Promote it to the headline figure.** The model already has six
   comparable worlds, July 1929 among them, on one basis. A chart in which the payments and the $95,000 stay still
   while everything bought with shares moves *is* the pencil-and-ink argument, shown rather than said.
3. **Keep the reserve schedule Keel built on 23 Nov in place of Table 2, not the stacked bars.** Stacked bars that all
   reach $50,000 by construction prove nothing. The schedule shows *when* each holding pays and how long the cash waits,
   which is the whole reason the extra $36,774 exists.
4. **Do not draw Figure 3 as proposed.** Its numbers are right, but the line at $95,000 makes the plan look as if it
   misses its own floor 1.5% of the time, and the figures are not "assets in January 2031" (section 2, finding A).
5. **Cut Figure 1 (the flowchart) and Figure 4 (the timeline).** Keel tried the flowchart on 23 Nov and a fresh reader
   called it "too busy"; both repeat prose that is already in the draft.
6. **Use two inks, not four colours.** Your gold and grey are indistinguishable once printed in greyscale (contrast
   1.05 to 1), and sage and gold nearly so (1.16).

## 1. Every figure in the proposal, checked

| Proposal figure | In the draft? | Register / model | Verdict |
|---|---|---|---|
| $339,162 + $81,244 + $29,594 = $450,000 | Yes | NUMBERS section 4: $300,000 + $39,162; $81,244; $29,594 | Adds up exactly. But see finding C |
| $110,838 left after the ten payments | Yes | $150,000 - $39,162 | Correct |
| $57,070 original shortfall; $442,930 own receipts | Yes (Table 2) | NUMBERS 8h: $442,929.57 + $57,070.43 | Correct; all ten Table 2 rows match the model to the dollar |
| $36,774 extra Treasuries | Yes | NUMBERS (17 Nov re-size) | Correct. See finding D on putting it beside $57,070 |
| Table 3: $100,477 / $123,036 / $151,053 and $76,556 / $130,471 / $222,342 | Yes | NUMBERS 8c, house model | Numbers correct; label wrong (finding A) |
| 1.5% / 16.4% below $95,000 | Yes | NUMBERS 8c | Correct; meaning differs from how a chart will read it (finding B) |
| -$7,435 median / +$23,921 5th percentile | Yes | Arithmetic on 8c | Correct (a difference of medians, not a cost in every path: the plan is behind the rival in 59.8% of paths) |
| 2031 conversion of half of VT | Yes ("Before the meeting, Laura sells half..."; "January 2031: Move half of VT into IBTM") | IPS: "the other half will move into Treasuries" | Present and consistent with the IPS |
| 1929 stress test | Yes ("she would retain only about $12,500") | Model window starting July 1929: kept half $6,699 + paid above the top $5,843 = $12,542; range $95,000-$100,000 | Present and correct |
| 40% equity decline, range $95,000-$105,000 | Yes | NUMBERS 8p | Correct |
| $95,000-$115,000 range | Yes | NUMBERS section 4 | Correct |

**Consistency with the frozen IPS.** The plan agrees with the IPS on every structural point: ten Treasuries bought in
January 2027, the 2028 deposit completing the ladder first, "most" of it into the late-2032 Treasury fund ($81,244 is
54.2% of $150,000), the rest in VT, half the shares promised to no one, the other half moved before the 2031 meetings.
The one new element is the $36,774 of extra Treasuries, which the IPS does not mention. The draft handles it well in
prose ("The principle established in our IPS remains unchanged"). A figure headlined on an "original shortfall" puts
it at risk (finding D).

## 2. What is wrong or will mislead

**A. Table 3 (and proposed Figure 3) measure a December 2032 payout, not January 2031 assets.** The same three numbers
appear twice in NUMBERS: in 8c labelled "Money owned in Jan 2031", and in section 4 as "What the floor and the moved
half pay", whose central value, $122,503, is the late-2032 payout of the Treasuries. They are the modelled payout,
before the 0.5% cut and the rounding to $5,000. So the draft's sentence "These figures measure the assets Laura holds
in 2031, rather than what she can contribute in 2033" has it the wrong way round, and the proposal's instruction to
"explicitly distinguish January 2031 facility assets from the January 2033 contribution" would draw a distinction the
data does not support. Correct label: "What her Treasuries will pay in December 2032 (held from January 2031)".
*Ask the audit thread to confirm before printing.*

**B. A line at $95,000 makes the plan look as if it fails its own floor.** In the plan's column, the 1.5% below
$95,000 are futures in which yields fell before the 2027-28 purchases, so the floor bought less and Laura would have
stated a lower bottom (as low as $80,000 at the 1-in-20 point). Measured against the bottom she would actually have
stated, the plan falls short in 0 of 200,000 paths. A reader who sees the draft's own claim ("Even if her shares
were worth nothing ... a $95,000 facility contribution") and then a chart with the plan below $95,000 in 1 path in 67
will think the report contradicts itself. The same point applies to Table 3's note, "Treasury rates follow the 6
November 2026 forward curve": that is true of the historical rows only. The 200,000 simulations move rates too, and
that rate movement is what produces the 1.5%.

**C. The $450,000 flow does not match Table 1, and the draft never says why.** Table 1 at 1.5 times gives VT about
$39,800 (8.84%); the flow gives $29,594 (6.6% of $450,000). The WInS book was built before the operating reserve was
sized, which the register reconciles ($293,830 / $109,148 / $39,787 against $339,162 / $81,244 / $29,594) but the
draft does not. A judge who reads Table 1 and then a flowchart will see two different portfolios. Whatever figure
carries the $450,000 split needs that one sentence beside it, and Wharton's minimum requirement "demonstrate
consistency with the strategy established in the IPS" makes it worth the space.

**D. $57,070 beside $36,774 invites the wrong subtraction.** Readers will ask where the other $20,296 came from. The
$57,070 is paid between 2033 and 2042; the $36,774 is what those payments cost to buy in January 2028. A chart can
make that clear only by keeping the two in different units on different axes, which is hard in a stacked bar. A figure
whose largest label is "shortfall" against the "original ladder" also hands a judge the idea that the IPS plan was
underfunded. Label it by what changed, the standard: "if cash waiting for a payment earns nothing".

**E. A horizontal line at $50,000 is met by construction.** The extra Treasuries are sized so each year reaches
exactly $50,000, with nothing left after 2042. Ten bars touching a line they were built to touch is decoration, not
evidence. The information is in *when* the money arrives.

**F. A "1929 scenario" can be assembled wrongly.** The worst historical top ($100,000) comes from a window starting
December 1928; the worst payout ($105,843) and the $12,542 come from July 1929. Take every number in a scenario row
from one window. The model file has the July 1929 window complete
(`numbers/results_range_rule_2026-11-17.json`, `exhibit3_rows`).

**G. Uncited data.** Table 3 uses US equity returns since 1871, but no source for them is in the References (Keel's
exhibits cited Shiller, n.d.). Wharton requires every source cited in APA. Any figure built on the history needs it.

## 3. Pages: there is no room to add anything

At about 275 words a double-spaced page (12-point Times New Roman, 1-inch margins), the draft measures roughly:

| Section | Prose | Tables | Estimate | Wharton |
|---|---|---|---|---|
| Portfolio Implementation | 639 words | Table 1 | about 3.0 pages | 2-3 |
| Integrated Recommendation and Reflection | 2,186 words | Tables 2, 3 | about 8.5-9 pages | 6-8 |

These are estimates; lay the draft out in the real format to measure. But they say Section 2 cannot take a figure at
all, and Section 3 has to lose about half a page to a page before anything is added. Wharton allows tables and
graphics single-spaced, which helps. The rule for every figure is therefore: **it replaces a table or about 150 words
of prose, or it does not go in.** Five figures cannot pass that rule; two can.

## 4. The visual identity

**What works.** Solid for what Treasuries already hold, hatched or dashed for what depends on share prices. This is a
convention any finance reader knows (projections are dashed), and it carries the pencil-and-ink idea without a word.
That fits the team's own decision on 25 Nov to keep the conceit to an opening reference and a closing echo: the
figures can carry it silently, which is more striking than saying it again.

**What does not.**
- **Four colours for four meanings is too many, and three of them merge.** Measured contrast: gold against graphite
  1.05 to 1, sage against gold 1.16, sage against graphite 1.21. Printed in greyscale, or seen by a colour-blind
  judge, they are one colour. Only navy stands apart (11.8 to 1 against white).
- **The meanings mix categories.** "Tradeoffs and facility funding" (gold) is not a kind of money; "growth" and
  "flexibility" (sage) are different jobs; "uncertainty" and "alternative strategies" (graphite) are different
  things. A colour should answer one question everywhere. The useful question is: *does a share price change this
  number?*
- **Recommended palette:** ink navy (#26394D) for money held in Treasuries; graphite hatching for anything bought with
  shares; a light grey for the rival strategy, used only in a comparison. Drop sage and gold. If one accent is needed
  for a single highlight per figure, use navy at full weight and everything else lighter.

**Editorial ideas worth keeping.** APA tables with three horizontal rules and no vertical ones (Table 1 is currently a
full grid). APA figure format: **Figure n** in bold, title in italic title case above, note and data source below.
Titles that state the finding ("Share Prices Move Only What Laura Has Not Promised"), not the contents. A restrained
title page, as long as every required item stays (team name, advisor, members, WInS username).

## 5. Figure by figure

| Proposal | Verdict | Why |
|---|---|---|
| 1. What Laura promises, what Laura keeps (flowchart) | **Cut** | Tried on 23 Nov as Keel's "where the money goes" and read as too busy; every number in it is already in the paragraph that begins "Once the operating commitments have been provided for"; it exposes finding C. If a bridge is wanted, one sentence under Table 1 does it |
| 2. The bills that must be paid (stacked bars) | **Replace with the reserve schedule** | Findings D and E. Keel's reserve schedule (`exhibits/figure1_reserve_2x.png`) shows each holding as a bar from 2027 to the day its cash arrives, the 10.5 and 7.5 months the 2038 and 2039 money waits, and the two columns of Table 2 beside it. It replaces Table 2 at about the same height, so it costs no page. It needs relabelling to the draft's words |
| 3. The price of certainty | **Keep as a table, fix it** | Findings A, B, G. The comparison is the report's best piece of analysis, but the table already does it in three lines. Fix the row label, measure "short" against the bottom she would have stated, fix the note on rates, cite the history. The single most memorable fact in it is one sentence: from a July 1929 start, buying the floor early leaves $105,843; waiting leaves $22,573 |
| 4. Sixteen years, four decisions | **Cut** | The four bold dates under "Between now and 2042" are already a timeline, and Wharton asks for the monitoring in prose. The reserve schedule's axis already runs 2027-2042 |
| 5. The cost of being wrong | **Promote to the headline figure** | See section 6 |

## 6. The figure to make: "Share prices move only what Laura has not promised"

One small-multiples chart, one row per world, the same three columns in every row. Every number is in the model files
on one basis (rates at the 6 November 2026 forwards; history rows are US stocks with dividends over the three years
from the start shown).

| World | Ten payments | Range Laura states in 2031 | Contribution, 2033 | Her flexibility, 2033 |
|---|---|---|---|---|
| Shares earn 7.5% a year (central) | All paid | $95,000-$115,000 | $115,000 | $28,682 |
| Shares 40% below cost at the 2031 move | All paid | $95,000-$105,000 | $105,000 | $17,320 * |
| US shares from January 2000 | All paid | $95,000-$105,000 | $105,000 | $21,161 |
| US shares from January 2008 | All paid | $95,000-$110,000 | $110,000 | $26,256 |
| US shares from July 1929 | All paid | $95,000-$100,000 | $100,000 | $12,542 |
| Shares worth nothing | All paid | $95,000 | $95,000 | $7,365 |

\* $10,229 kept plus $7,091 paid above the top (NUMBERS 8p); the sum is Keel arithmetic and should be registered
before it prints. "Flexibility" here is the draft's own basis for "$28,700 ... including surplus facility assets".

**How it looks.** Each row: ten small solid navy squares (identical in every row); a contribution bar whose first
$95,000 is solid navy and identical in every row, with a hatched segment above it that grows and shrinks; a hatched
flexibility bar. The eye finds the answer before reading a label: the solid stays put, the hatching moves. About a
third of a page, single-spaced.

**What it replaces.** The three sentences on the 40% fall, the 1929 test and "Even if her shares were worth nothing",
about 120 words, and most of the proposal's Figures 1, 4 and 5. It answers three of Wharton's required elements at
once (the payments, the contribution with flexibility, the range "across varying outcomes").

**Where it goes.** At the end of "Laura's holding", where the draft states the 1929 and 40% results, or at the opening
of Section 3 if the team moves the deletion test there (as V3's working tab suggests).

**One honest addition.** The bottom itself is not fixed until January 2028: if yields fall before the purchases, the
floor buys less (1-in-20: a stated range of $80,000-$100,000). A judge who knows bonds will ask. A footnote line, or a
seventh row marked as a different kind of risk, answers it and makes the point sharper: share prices never move the
bottom; only yields before 2028 do.

## 7. The recommended set

1. Table 1 (required), restyled as an APA table, with one bridge sentence to the $450,000 plan (finding C).
2. Figure 1: share prices move only what Laura has not promised (section 6). New.
3. Figure 2: the reserve schedule, in place of Table 2. Exists; relabel only.
4. Table 3 (renumbered Table 2), fixed per findings A, B and G.

Net change in length: about one table's height saved, about 120 words saved, one third of a page added. The draft
still needs prose cuts in Section 3 to meet the eight-page limit.

## 8. Not checked

- The independent numbers rebuild had not landed; recheck findings A and B against it when it does.
- Page counts are estimates from word counts, not a typeset layout.
- Outside the proposal, noticed in passing: the draft's "$96,700 in 2026 dollars" uses 2.5% inflation, while the
  register uses J.P. Morgan's 2.4% (about $97,400). Pick one.
