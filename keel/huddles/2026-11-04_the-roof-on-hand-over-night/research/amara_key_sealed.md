(Keel is a simulated team, AI-written.)
SEALED before Tess's proposal was read.

# The README test: Amara's key (H-033, round 3, Wed 4 Nov 2026, about 21:10 Sydney)

`research/readme_proposed.md` turned up in this folder while I was writing. I haven't opened it, and I won't until the
chair posts the score. This key comes from what the three cards say about themselves in their own opening lines, and
from what's true about the plan and the hand-over. It doesn't come from a guess about what Tess wrote. If her page routes
a task to a different card than this key does, the page goes back. If I've got a card's job wrong, that's the key's
fault, and I'd rather the chair said so out loud than scored around it.

**What I keyed against** (sha256, first 16): `ips.txt` b9368f5b5fa9ffc5 (the FINAL, 495 strict), `pitch.txt`
2f94abe7c30be498, `CASE_CARD.md` fefd2f64558e5035, `LOOK_ALIKE_CARD.md` ce66e7fd5ec3bac9, `READERS_CARD.md`
7a5a5c906c32277f, and today's `README.md` 0e211f5035b6ba31 (still "tends to dry up").

## How the chair runs it
- One first-time reader, a Year 11 student with no stake who has never seen a Keel file. They get Tess's proposed README
  and nothing else: no cards, no IPS, no pitch. Questions from `reader_questions.md`, word for word.
- Score the first answer. No follow-ups, no hints. Copy the answers out word for word beside the score.
- Each question is right or wrong; nothing counts as half right. "The page doesn't say" counts as wrong.
- Questions 1 to 3: a card counts if the reader names the file or describes it in a way that fits only that card, in
  the README's own words for it. Naming two or three cards with no first, or "all of them", is wrong.

## The questions and the key

**1. Cutting a sentence: which file first?**
- **Right:** the case card (`CASE_CARD.md`), or "the one that lists what the case asks and which words answer it".
- **Why, from the card itself:** "Each row pairs something the case or Wharton asks with the words in our IPS that
  answer it; if you cut those words, put the answer back in your own." And its own split: "The look-alike card checks
  facts; this one checks answers." A sentence that's gone can't be false, but it can take its answer with it. Cut
  "which never needs rebalancing" and the case's question about how the reserve changes, "if at all" (case 95-97), goes
  with it. Only this card would show that.
- **Wrong:** the look-alike card first, the readers card first, the full record, "all three", "none".

**2. Swapping words, or putting a fact another way: which file first?**
- **Right:** the look-alike card (`LOOK_ALIKE_CARD.md`), or "the one with each fact next to a false version of it".
- **Why, from the card itself:** "Each row gives a fact in our words (you needn't keep them), a false look-alike and why
  it's false"; "this card checks that each answer is still true"; and if no row fits, "check each word you swapped,
  added or cut against its IPS line". Every break we've seen came from changing words and keeping the sentence. All five
  test rewrites, by five different writers, turned "one redeemed before each January" into "one redeemed each January",
  and Jun's three blind rewrites broke 7 facts.
- **Wrong:** the case card first. It's the likeliest wrong answer, because it has a "Keep these words" column, but it
  only tells you an answer is still there, not that it's still true. Also wrong: the readers card, "all three", "none".

**3. Keeping the last sentence, or taking a suggested cut: which file first?**
- **Right:** the readers card (`READERS_CARD.md`), or "the one about what outside readers stumbled on". "The readers
  card, then my own ear" is right too.
- **Why, from the card itself:** it's the only card that deals with either choice: "The last line. Every reader in both
  tests called [it] the corny one. Your call, but the ending must still pay off 'do not crush'", and "We suggest cutting
  ', to us,'". Neither the case card nor the look-alike card mentions the last sentence or ", to us,".
- **Wrong:** the case card or look-alike card first. "No file, it's just my call" is also wrong if the reader never names
  the readers card: the choice is theirs, but this question checks whether the page points them to what readers said.

**4. What does Laura's first $300,000 buy, and what is it for?**
- **Right, both parts needed:** (a) Treasuries: US government bonds and/or Treasury funds ("ten Treasury holdings", "a
  ladder" both count); (b) they pay her ten $50,000 yearly payments (2033-2042), one holding per payment, each paying out
  before its January payment, so no payment depends on shares. "To pay her yearly $50,000" is enough for (b) without
  the dates.
- **Wrong:** shares or a share fund in it; "invested to grow"; "for the building"; "kept in the bank". Two slips count
  as wrong because the look-alike card names them as false: anything maturing or redeemed **in** January (row A: each
  holding ends earlier, the funds in December, the bonds in February, May or November), and "every payment is
  guaranteed" or "it can't fall short" (row D: the plan says the ladder can fall short if rates fall and stay low). "Pays
  each January's payment" is fine, and so is "safe" or "doesn't rely on shares".

**5. What does the plan do with Laura's 2028 money? Does any of her money end up in shares?**
- **Right, both parts needed:** (a) most of it buys a Treasury fund (ending in late 2032) that sets the minimum, or
  floor, of her building gift. "A Treasury fund that goes towards the building" counts. (b) Yes, a small part, about the
  interest that fund will earn, goes into one world share fund. Saying it first tops up the payments' ladder if needed
  is welcome but not required: today's README leaves that step out, so a reader can't be marked down for missing it.
- **Wrong:** "no shares at all" or "the plan avoids shares" (row F: a first-time reader already took "bet on shares
  twice" as a ban on shares); "most or all of it goes into shares"; "it pays the yearly payments" given as its main job.

**6. What does the page say the team must do themselves before the IPS goes in?**
- **Right, both needed:** (a) rewrite the IPS (and pitch) in their own words before pasting them in; (b) run it through
  GPTZero, or "an AI-writing checker", because we couldn't, and rewrite what it flags if the "human" score is under
  50%. Welcome but not required: decide the last sentence (and ", to us,"); write "each payment has its own bond", not
  "we don't duration-match"; check the rewrite against the cards; submit it themselves by Sat 7 Nov 09:00 Sydney (Fri
  6 Nov 5 pm ET), since Keel submits nothing.
- **Why these two:** the label beside the FINAL says "The team rewrites any draft in its own words before submitting;
  nothing here goes to Wharton as written" and "GPTZero: not yet checked". Book 10 puts every draft through GPTZero, and
  none of our sessions can reach it, so the students are the only people who can do it.
- **Wrong:** missing (a) or (b); "paste it in as it is"; "Keel hands it in"; "the page doesn't say".

**Left out on purpose:** the income line. Any question about "can" or "tends to" gives away the answer, and Jun's
search tonight covers the words themselves. If the reader brings up her income without being asked and says it "does",
"always" or "tends to" fall with shares, the chair writes that down beside question 5 (look-alike row E) and doesn't
score it.

## The pass bar (sealed)

**PASS if questions 1, 2 and 3 are all right and at least two of questions 4, 5 and 6 are right. Anything less is a
FAIL.** Question 1 fails the page by itself if the reader names any file other than the case card first, whatever else
they get right, because a cut sentence takes its answer to the case with it and no other card would show the hole.

Why: getting a tired student to the right card is the one job this page has on Thursday, so routing gets no slack;
questions 4 to 6 only check that the page doesn't teach anything false along the way, and one slip by one stranger is
as likely to be the stranger as the page.

A pass from one reader means "not failed", never "clear" (round 7's rule: a word is clear only if a stranger can say it
back and act on it, and even three readers can only say "not failed"). If it fails, the chair says which question
failed and in which words, and the README goes back to Tess before 23:00. Nobody edits this key after the chair has
its hash.
