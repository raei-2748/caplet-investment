---
name: stop-slop
description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.
metadata:
  trigger: Writing prose, editing drafts, reviewing content for AI patterns
  author: Hardik Pandya (https://hvpandya.com)
---

# Stop Slop

Eliminate predictable AI writing patterns from prose.

## Core Rules

1. **Cut filler phrases.** Remove throat-clearing openers, emphasis crutches, and all adverbs. See [references/phrases.md](references/phrases.md).

2. **Break formulaic structures.** Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency. See [references/structures.md](references/structures.md).

3. **Use active voice.** Every sentence needs a human subject doing something. No passive constructions. No inanimate objects performing human actions ("the complaint becomes a fix").

4. **Be specific.** No vague declaratives ("The reasons are structural"). Name the specific thing. No lazy extremes ("every," "always," "never") doing vague work.

5. **Put the reader in the room.** No narrator-from-a-distance voice. "You" beats "People." Specifics beat abstractions.

6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.

7. **Trust readers.** State facts directly. Skip softening, justification, hand-holding.

8. **Cut quotables.** If it sounds like a pull-quote, rewrite it.

## Quick Checks

Before delivering prose:

- Any adverbs? Kill them.
- Any passive voice? Find the actor, make them the subject.
- Inanimate thing doing a human verb ("the decision emerges")? Name the person.
- Sentence starts with a Wh- word? Restructure it.
- Any "here's what/this/that" throat-clearing? Cut to the point.
- Any "not X, it's Y" contrasts? State Y directly.
- Three consecutive sentences match length? Break one.
- Paragraph ends with punchy one-liner? Vary it.
- Em-dash anywhere? Remove it.
- Vague declarative ("The implications are significant")? Name the specific implication.
- Narrator-from-a-distance ("Nobody designed this")? Put the reader in the scene.
- Meta-joiners ("The rest of this essay...")? Delete. Let the essay move.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |

Below 35/50: revise.

## Examples

See [references/examples.md](references/examples.md) for before/after transformations.

## License

MIT

---

## Keel house rules (local addition, 5 Nov 2026; not part of the upstream skill)

Installed for Team Keel / Caplet at Ray's request (5 Nov 2026, `keel/INSTRUCTIONS.md` I85). Everything above this line
is Hardik Pandya's skill, unchanged (source and pinned commit in `SOURCE.md`). In this repo:

**When.** Only when a Caplet student asks for it. Ray, 5 Nov: "I am not asking you to use stop slop yet", so Keel does
not run it on drafts on its own until a student says so. When it runs, fix each flag or keep it with one line saying
why. Suggestions for Caplet's own docs stay suggestions.

**Where Keel's standing rules win over the skill:**
1. **Dashes.** No em dashes (agreed). En dashes stay: Ray, 25 Oct, they are correct in Australian English. The
   upstream `examples.md` example 4 uses an em dash itself; ignore that.
2. **The case's words and the locked record.** Never swap the case's own terms (operating payments, operating reserve,
   facility contribution, credible range, co-sponsors, high degree of certainty) for "plainer" ones (Ray, 4 Nov, I83),
   and keep any phrase chosen to match Caplet's submitted trading notes or TNA (e.g. "main weakness", "A Treasury bond
   held to maturity").
3. **Words that carry a fact.** The adverb and "lazy extreme" bans target emphasis and hedging. Keep "only", "first",
   "roughly", "already", "never" or "every" when the word changes the meaning and is literally true (a ladder held to
   maturity never needs rebalancing). Cut it when it only adds force or softens.
4. **Normal finance verbs are not false agency.** Money buys, a bond pays, a fund matures, a deposit completes a ladder:
   keep them. Flag a thing doing what only people do (decides, waits, bets, notices, promises someone).
5. **No "you".** In the IPS and Final Report the reader is a judge and Laura is "she". Put the reader in the room with
   specifics, not by switching to "you".
6. **Three-item lists from the case stay** (her income: book advances, speaking fees and licensing).
7. **No self-score.** Skip the 1-10 "sounds human?" scorecard: Keel doesn't grade its own AI-likeness (Ahaan, Book 9).
   GPTZero, run by Caplet, stays the test. Use the checks to find and fix, never to certify a draft.
8. **Rewrite, don't squeeze.** Fix a flag by rewriting the sentence with a person doing something, or by cutting a whole
   idea; never by squeezing words out (Book 10). Recount words after fixes (IPS 500, pitch 50, strictest count).
9. This list overlaps the AI habits Ray already banned (slogan flips, two-word kickers, "That is X." runs, one-line
   endings: `keel/ips_rewrite/drafts/D35/README.md`). Both apply.
