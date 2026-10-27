# The Courtroom, Tue 27 Oct 2026 (18:20 run): LR-04 on trial. "Don't pad the bottom; mark it in 2031"

(Keel is a simulated team, AI-written.) AI-generated (Claude Code); the room and the people are fiction, the
arguments and numbers are real work. Not for submission. Kai prosecutes, Amara defends her own LR-04, Nora rules.
Requests closed: Laura's Room's two roasts (LR-04, filed 27 Oct; LR-03, filed 26 Oct). Numbers: MODEL, 22 Oct curve,
J.P. Morgan 2027 7.5% world stocks, 200,000 paths; "worst" = stocks and yields falling together (rho 0.5) at 6.5%.
Script `../../rooms/courtroom/C-02_mark_vs_promise.py` -> `C-02_results.json` (reuses LR-04's patch, model unchanged).
**Star and criterion:** north stars 3 and 4; Investment Strategy and Portfolio Analysis. **Line it changes:** the IPS
sentence that says how the 2031 bottom is set.

## The claim
LR-04: no fixed margin under the 2031 bottom. In 2031, before Laura speaks, take off only the coupon gap the bond market
already shows that the 2027 leftover and her half of the stocks can't cover. A clearing house would call the fixed
margin "initial" and the 2031 mark "variation". Model: 0 of 200,000 paths break (7 in the worst case).

## Count 1. "A bottom that can be cut breaks the locked TNA" (IBTM note: "giving co-sponsors a minimum figure in 2031")
**Kai.** The VT note calls it her "promised minimum". Promise a minimum, then shave it, and you've broken it.
**Amara.** Nothing is shaved after it's said. The mark is taken in 2031, and then she names the figure. The TNA
promises a figure *in 2031*, and that's what she gives.
**Ruling: UPHELD.** The TNA dates the minimum to 2031, and the rule sets it in 2031. Keep "cut" and "margin" out of
the IPS, because both words suggest a promise was trimmed.

## Count 2. "Then what does the IPS promise?" (the catch nobody had priced)
Kai's follow-up: the drafts and `00_GROUND_TRUTH.md` s5 say the floor is "quoted at $145k". The run says that number
was never safe to promise, with or without the mark:

| 2031 bottom (MODEL) | Below $145k | Below $140k | Lowered by the 2031 mark | Bottom broken in 2033 |
|---|---|---|---|---|
| floor rounded down, no mark | 43.5% | 30.9% | 0 | 0.75% (worst 1.43%) |
| **LR-04 rule (gap rounded up to $5k)** | 45.5% (worst 46.1%) | 33.5% | 8.2% of paths, ~$9.9k each time | **0 of 200,000 (worst 7)** |
| gap netted against the rounding first | 45.2% | 32.9% | 6.4% | 1 (worst 14) |
| gap also allowed to use the $3,700 | 36.0% | 25.1% | 4.0% | 35 (worst 186) |

The bottom sits below $145k in 43% of paths *before any mark*, because the 2028 deposit tops up the ladder first
(4bp of headroom on 22 Oct). The mark adds only two points to that. So the IPS can't promise a dollar bottom today
anyway. **What it can promise is the rule.**
**Ruling: UPHELD, with the bigger point.** The IPS gives the bottom as a rule ("what the floor will pay, rounded down,
less any gap the bond market has already shown") and never as $145k. If a figure has to appear, write "up to about
$145,000". This also corrects this morning's Trial 2 ("quoting $145k against ~$150k owned").

## Count 3. "The clearing-house parallel is costume"
**Kai.** Variation margin is cash paid every day between two parties. This is one valuation, and no money moves.
**Amara.** The logic is the same: post for what *could* happen, settle what *has* happened.
**Ruling: EXACT IN LOGIC, and it made a prediction.** Clearing houses never run on variation margin alone. They keep
a small initial margin for the "margin period of risk", the gap between the last mark and the close-out. Here that
gap is 2031 to 2033, and the existing $3,700 plus rounding is that small margin. Take it away (last row) and breaks
go from 0 to 35 (7 to 186 in the worst case). The analogy predicted that, and the model confirmed it. That isn't
costume. Still, it belongs in the Final Report: in 500 words the plain version does the job.

## Count 4. "LR-03's donors were mail and phone households, not institutions" (closes the 26 Oct request)
**Ruling: AMENDED.** The direction carries over to co-sponsors, and if anything it's stronger. A finance team can
count only an unconditional promise (ASU 2018-08), so the bottom is the only number it can count. The size of the
effect doesn't carry over. Elasticity 0.94 comes from a $3,000 computer-lab mail campaign. So no "% of co-sponsor
money lost" figure goes into any Caplet text. The ranking is the finding, not the decimals.

## The two standing charges, on LR-04's candidate line
- **"Reads as AI":** "The bottom isn't a forecast" passes, because it answers the case's credibility line (:113-115).
  "Reached about **seven years in ten**" fails: there's only one 2033. Change it to "seven times in ten".
  And the rooms disagree on the number: R05 says "three in four" (top within $1k, 76.7%), LR-04 says "seven in ten"
  (exact top, 69.9%). Pick one definition before Thursday's synthesis (request to the Genius Lab).
- **"Competent but forgettable":** the line a judge remembers is "less any gap the bond market has already shown
  her". Keep it, and cut what's around it.

## Nora's ruling: AMENDED. LR-04 stands (rule as written; the two variants were tried and rejected)
**The one change that matters most:** the IPS states the 2031 bottom as a rule, never as a dollar figure.
(Investment Strategy: the form asks for a decision-making framework, and a rule is one. Portfolio Analysis: "$145k"
would be wrong in 43 of 100 modelled futures.)

- **Kai:** I came for the clearing house and lost. It predicted the 35 breaks before we ran them. What I did find
  is worse for us: "$145k" was wobbling long before 2031. We'd been quoting a number that the January bond market
  gets to set.
- **Amara:** A co-sponsor writes the bottom into a board paper, so it should be as big as it honestly can be and
  never move once said. The mark does both. And yes, "seven years in ten" was mine. There's one 2033. Fixed.
- **Nora:** Amended, not struck. The bottom is a rule Laura applies in 2031, not a number we guess in 2026. Any
  draft that prints $145k as a promise comes back here.
