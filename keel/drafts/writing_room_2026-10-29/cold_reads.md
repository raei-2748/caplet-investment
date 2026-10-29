# Cold reads, Writing Room, Thu 29 Oct 2026 (beat 7)

(Keel is a simulated team, AI-written.) Readers are AI subagents that saw only Wharton's IPS instructions (BIBLE Book 7),
the client case and two unlabelled texts. They never saw V29, Keel's files or each other. Label shuffle: round 1
X = B (doors, first wording), Y = A (hard fixes only); round 2 P = C, Q = B (final wording). Their reports are summarised
below, with quotes kept word for word where they matter.

## Round 1: A (hard fixes only) vs B (A + the four-doors rule), two readers

The B line they read was the first wording: "Every rule here fires in a year the case already set, never on a hunch; if
needs change, the gift takes it before a cheque does, and never below its named bottom."

| | Professor | Practitioner (liability-matching, 20 years) |
|---|---|---|
| Framework found in A | Only the "in one rule" line. "If needs change, cheques first; floor and stocks are bought smaller together" is "too garbled to work as one". **2/5** | The one rule plus "money she expects insures it", but "I had to put them together myself". **3/5** |
| Framework found in B | The one rule plus the dated line: "a trigger rule plus an order of who gives way first". **3/5** (split between para 2 and para 8) | "That third line tells me when the rules act, so it reads as a framework." **4/5** |
| Reserve over time | B: "adequate: the reserve is the ladder and runs off one rung at a time". A: "never says what the reserve holds" | A: "tops up from what?". B says where the top-up comes from |
| Both tripped on | B: "never below its named bottom" next to "comes off the quoted bottom" | B: the same clash, "on a first read"; after naming, "who pays? 'Her half' is implied but never said" |
| Advance | **B** | **B** |
| What A does better | Para 8 "actually reasons about the cost of quoting too high versus too low" | The same paragraph is "real client reasoning, apart from the made-up 'three times'"; A's smaller-deposit line "can be checked and is true" |

Both readers flagged, in A and B alike: "ten debts of one government stand or fall as one" reads as a confession rather
than an argument; "sized to regrow what's left by 2033" (what is left of what?); "about one dollar in fifteen" (of
what, and when?). The practitioner also called the pharmacist metaphor "gimmicky". That is a taste note, and the
Bible keeps the motif. The practitioner also made a strategy point: once the top is locked, "the range is close to a
single number". That goes to the Courtroom, not to a wording fix.

**Fixes made after round 1:** B's order line became "if needs change, the gift takes it before it is named, her half
after, a cheque last". It says who pays after naming and drops the clashing "never below its named bottom"; the word
count is unchanged at 499. C was built because both readers named the range's reasoning as the one thing A did better.

## Round 2: B (fixed line) vs C (B + the range's reasoning, without "three times" or the donor clause), one reader

**Reader (former endowment CIO; P = C, Q = B):**
- Framework found: P 3/5 ("spread over paras 3, 5 and 9"); Q **4/5**: "'Wipe out every share she owns and no cheque is
  worse off – only the gift' proves the framework right after you read it, and 'never on a hunch' makes the timing
  rule clearer".
- What sticks tomorrow: P "Too high, and she breaks her word, which is worse"; Q the wipe-out line; both the opener,
  "the real winner in both".
- Tripped on, both: **"her first $300,000 buys them in January 2027" vs "That deposit fills any gap in the ladder"**,
  which means "the cheques are not 'made safe' on the day they become promises, and the core rule breaks". This is the
  third reader today to catch it, after the Window's note this morning. Also: "topped up once from her half" next to the
  wipe-out line ("her half holds shares"); "what's left"; "funds that turn to cash" (a judge won't know these are
  defined-maturity bond ETFs); "one dollar in fifteen", "over how long?"
- **Advance Q (B).** "P does better with the client: 'embarrass her twice over' ... is what the case worries about."

**Fixes made after round 2 (in `build.py`):** B adds "or nearly" to the $300,000 line and drops "from her half" from the
reserve line, because the order line already says who pays. B is now 498 words, C 497 and A 499.

## Tally
Three blind readers, three for B. Each of them also named the range's two embarrassments as the one thing the losing
version did better. Wording fixes are applied only where a reader tripped and the fix is a fact (H1-H4). The readers
are models, not judges: three readings is a signal, not a vote.
