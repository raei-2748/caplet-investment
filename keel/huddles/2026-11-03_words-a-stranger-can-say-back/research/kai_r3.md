# Kai, round 3: did W3 lose the job "first" did? (H-025)

(Keel is a simulated team, AI-written. Quotes are real file text; line numbers as of 3 Nov 2026.)

## The text under test
V54 P5 (`arms/A_V54.txt`): "Her 2028 deposit first finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund maturing in late 2032. That is her floor."
W3 P5 (`arms/W3_amara.txt`): "Her 2028 deposit finishes any rung the first $300,000 couldn't buy. Most of the rest buys a Treasury fund maturing in late 2032. That is her floor."
Only difference: the word "first".

## What the register actually protects
- `keel/rooms/archive.md` line 58 (Coherence register, 1 Nov): "V50 keeps A1, A2, A3, A4/A22, A6/A23/A25 ("Her 2028 deposit first finishes any rung")". The quoted words are a label for V50's wording; the rules are in the rows.
- A6, line 74: IBTR note: a yield fall means "the 2028 deposit would top up the ladder, leaving less for the facility". Rule: the IPS echoes top-up, then what is left goes to the facility/floor. "The strongest echo across the set."
- A23, line 91: IBTO/IBTR notes; "the IPS must keep 'fills any gap' (dropping it would read as a change of plan)". Rule: the top-up stays.
- A25, line 93: "Write what the deposit does for the cheques, not that it does nothing: 'So her 2028 deposit only insures the cheques: it plugs any gap in the ladder, then builds her gift.'" Rule: gap first, then build.
- `keel/ips_rewrite/IDEA_LEDGER.md` line 40: "the 2028 deposit plugs the gap, then the floor"; line 87 (B13): "the cheques are bought in 2027 and the 2028 deposit plugs any gap". Searching both files for "first finishes" finds only the archive line 58 label; the ledger never says it.

## Is the job carried in W3?
The job = ORDER (ladder topped up before the floor is bought) + LEFTOVER (the floor gets what the top-up leaves, so a bigger gap "leaves less for the facility").
- "finishes any rung" keeps the top-up (A23's "fills any gap"). Carried.
- "Most of the rest buys" carries order and leftover: "the rest" can only mean what remains of the deposit after the rungs. Carried, by grammar.
- Cost of the loss, honestly: "first" is the only word that says "before". In the four strangers' summaries, V54 readers kept the top-up (R1: "fills any gap in that ladder and buys a Treasury fund"; R4: "tops up any bond they couldn't afford, then buys"). The W3 reader R2 wrote "Laura's second deposit in 2028 buys more of this safe stuff" and lost the top-up altogether (r2_reader2_sonnet.md line 16). One reader, one summary, not a score: but it points the way "first" would have helped.

## Verdict: CARRIED (my round-1 "breaks a won rule" was too strong)
A6/A23/A25 are met by "finishes any rung" + "Most of the rest buys". The register keeps the rule, not the adverb. Optional 1-word fix if Tess has the margin (497 now, cap 500, so 498): "Most of the rest *then* buys". I would not spend it unless R2's drop is judged to matter.

Still standing from my round 1, separate from "first": W3 keeps "so her flexibility shrinks before her gift does" (Amara's own table, line P8), so that job is not lost either. I withdraw both charges against W3. The quarter in B_LR11 remains an unsourced number; that charge is about B, not W3.

## My lock phrase, one honest hit
"as if later bond payments sat idle", against the Genius Lab's rule (price the gap as if every dollar the ladder pays from naming day on, coupons AND maturing bonds waiting for their January, earns nothing; money already reinvested keeps its bonds).
- A maturing bond's principal IS a "bond payment", so the phrase covers it. Principal that lands in the cheque's own January is spent, not idle; fine.
- Weak spot 1: five of the ten rungs are funds (IBTM-IBTQ), whose distributions and final payout are not "bond payments" strictly (TNA reflection 2: "a net asset value, as opposed to a promise of par"). The phrase is false only in that narrow sense. It matters little for the gap (the Lab's model treats them alike) but it breaks the Archive's A11 habit of not calling the funds bonds. Untested fix, 0 words: "later ladder payments sat idle". Cost: "ladder" is a word two strangers stumbled on ("rung", "ladder"), though P3 has already explained it.
- Weak spot 2: "bond payments" can be heard as the ten cheques (the same trap I charged the Lab with). 0 of 4 strangers fell in; I'd say so plainly.
- Weak spot 3: "later" could read as later than today, not later than naming day; the paragraph's "Before she names the range" sits two clauses before, which fixes it.
