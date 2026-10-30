# Panel 5 (Fri 30 Oct 2026, night): V37a and V37b against a new field

AI-generated (Claude Code), not for submission. Same six judges (`../README.md`), blind, new orders (seeds 5001-5006).
Field: **V37a** (V36 + the Archive's A25 fix: "In our model, a cheque fails only if ... under about $125,000"),
**V37b** (V37a with the 60/40 sentence swapped for an answer to the Rooftop's Q12, "why not the ladder and the rest in
stocks?": "Had her 2028 deposit gone into stocks, the top would usually be higher, and the bottom whatever a 2030 crash
left"), A09 (ladder + ~80% stocks), CV5 (Caplet's Version 5, 14 Oct), H21 (lead-gift team) and **S01, a new
outside-style rival** (`../rivals/S01.md`: a Singapore junior-college team, Treasury ladder + a CPPI growth sleeve,
written fresh tonight by a different model from only the case and Wharton's word).

| Judge | Ranking (best first) |
|---|---|
| J1 skimmer (Haiku) | CV5 > V37b > A09 > V37a > H21 > S01 |
| J2 growth hawk (Sonnet) | S01 > V37a > A09 > V37b > H21 > CV5 |
| J3 actuary (Opus) | S01 > V37b > V37a > CV5 > A09 > H21 |
| J4 teacher (Sonnet) | V37a > V37b > CV5 > S01 > A09 > H21 |
| J5 professor (Fable) | V37a > V37b > S01 > H21 > CV5 > A09 |
| J6 programme manager (Haiku) | S01 > V37a > A09 > V37b > H21 > CV5 |

**Agreement:** mean Kendall tau 0.21 (healthy disagreement). **Mean rank:** V37a 2.17, V37b 2.67, S01 2.67, CV5 4.17,
A09 4.17, H21 5.17. **V37a beat V37b with four of six judges.**

**Flaw in this panel's input:** H21's entry carried its "SIMULATOR NOTES" block (the extractor took everything after
"## IPS"; earlier panels stripped it). Judges J3, J5 and J6 said they ignored it; H21's last place is not to be trusted.
The V37a/V37b/S01 comparison is unaffected. Fix for the next panel: cut each rival at "## SIMULATOR NOTES".

## What the judges said (their reasons, not their lines)
1. **S01 is the first rival to take #1 from three judges (J2, J3, J6).** Their reasons: the growth money follows a
   stated rule, the assumptions (returns, volatility) are on the page, the range comes with a stated confidence, and the
   rule's failure modes are named and accepted. J1 and J4 marked it down as too technical to picture.
2. **No return assumptions are stated in V37a/b** (J3, J6; J5 indirectly). V34 had "world stocks at 7.5% a year";
   V35-V37 lost it.
3. **The 60/40 comparison is the trade-off judges want** (J1, J2, J4, J5, J6 preferred it to the counterfactual), but
   it does not say how much richer (J1, J2), and J3 asked what range a 60/40 plan would have named.
4. **Small growth share** (J2, J3, J5, J6): about a fifteenth in stocks reads as timid to growth-minded judges. That
   is the strategy, and para 6 (capacity, not willingness) is its answer; no judge said the answer was wrong.
5. **Still hard on one read:** what "97 in 100" covers (J1, J6), why the promised half moves into Treasuries (J1, J2,
   J4), "sized to grow back to the whole remainder" (J6), "coupons reinvested" (J1).
6. J4 and J5 find the XR pill paragraph decorative. Caplet XR is Caplet's locked name (26 Oct) and stays.

## What Keel did (V38, `../drafts/D18/`)
- Kept the 60/40 sentence (V37a won), added the assumption to it ("with world stocks at 7.5% a year"), and **corrected
  its number: in the 7.5% worlds a 60/40 plan breaks a promise in 32-36% of model paths (M7: lognormal 36%, storms 32%,
  bootstrap 35%), so "about one time in three", not "one in four"** (the 25% came from M7's 22-36% across all rivals).
- The floor sentence made plain: "Treasuries that grow back to the whole remainder by late 2032".
- Paid for it with a redundancy cut: "she has already taken the big one. The residency is her boldest bet" said one
  thing twice; now "she has already taken the big one: the residency."
- V37b's "owned since 2028" counterfactual is banked in the ledger (it is the qualitative answer to Q12; it waits for
  the Lab's A09 run, Sat 31 Oct, to give it a number).
