# Pencil and ink: one figure (Sat 28 Nov 2026)

Files: `pencil_and_ink.svg` (vector), `pencil_and_ink.png` (about 400 dpi at 6.5 x 1.9 in), `make_figure.py` (builds the SVG from
the model file), `render.js` (SVG to PNG with the pre-installed Chromium). Not inserted in the Google Doc.

## Suggested APA title and note

**Figure 1**

*From January 2028, Share Prices Can Change Only What Laura Has Not Yet Promised*

*Note.* Ink is what Laura has promised and holds Treasuries for from January 2028: ten payments of $50,000 (2033-2042)
and the first $95,000 for the building. Pencil is everything else she has in January 2033: the contribution above $95,000
plus what she keeps. "Do very well" is the 1-in-20 high outcome for shares from 2028 to 2031; the 40% fall is measured
from the January 2028 purchase price, with 7.5% a year after the move. Bars are drawn to scale. Model, on the Treasury
curve of 6 November 2026; assumes both deposits arrive and fund payouts fall no more than 0.5% short. Source: team
calculations.

## The numbers (model, `numbers/results_range_rule_2026-11-17.json` and NUMBERS 8p)

| World | Contribution | Kept, incl. paid above the top | Pencil (contribution - $95,000 + kept) |
|---|---:|---:|---:|
| Shares do very well (1 in 20) | $130,000 | $41,132 | $76,132 |
| Shares earn 7.5% a year | $115,000 | $28,682 | $48,682 |
| Shares fall 40% before 2031 | $105,000 | $17,320 | $27,320 |
| Shares become worthless | $95,000 | $7,365 | $7,365 |

Ink, $595,000, is the same in every world (NUMBERS section 4 and 8p: all ten paid; bottom $95,000). The audit of 28 Nov
confirmed the central range, the 40% fall's range, "$28,700" ($28,568 on its own sizes) and that the bottom does not
depend on VT. The history windows are left out on purpose: the audit and the register disagree by about $2,000 on the
worst one, so they are not drawn. The pencil in the worthless world is not zero because the floor's Treasuries are
expected to pay a little above $95,000 (about $7,365 at today's forward rates; about $3,100 if cash waiting earns nothing).
