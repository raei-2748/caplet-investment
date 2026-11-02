# Felix, round 3 research note (H-019, Mon 2 Nov 2026)
> FICTION (the speaker is simulated; the sources, counts and readers' words are real). (Keel is a simulated team, AI-written.) Not for submission.

The check: try to prove the order-line cut wrong. No new model calls. Counts are `python3 keel/office/tools/textcheck.py`
(strict, hyphens split) on scratch copies in
`/tmp/claude-0/-home-user-caplet-investment/03dc3032-2d9e-57f6-91b4-70cc152ed434/scratchpad/r3/felix/`.

## 1. What the afternoon readers valued in the order line (H-018, `../../2026-11-02_beside-the-champion/`)

| Where | Exact words | Job it names |
|---|---|---|
| `posts/r2_reader1_sonnet.md:7` | "Y first. It gives the stock sleeve a size ... and fixes the priority ('the cheques, then the floor, then everything above it'). Those are the two things portfolio construction and the time-horizon discipline need." | Priority rule (Investment Strategy: "disciplined planning across Laura's changing time horizons", `keel/WHARTON_WORD.md:18-19`) |
| `posts/r2_reader1_sonnet.md:8` | "X second ... it gives no size for the stocks and no priority order." | Says the text without it has no priority order |
| `posts/r2_reader1_sonnet.md:19` | "The preceding 'The order never changes' line helps. ... It is still a guess." | Q1 crutch (secondary, flagged as a guess) |
| `posts/r2_reader1_sonnet.md:39` | "It doesn't say the order of what, though I took it to be priority of claims." | Clarity fault (Commandment IV) |
| `posts/r2_reader2_haiku.md:9` | "Z. It states the order rule, the stock size and the client trade-off, so it answers the IPS question most fully." | IPS questions |
| `posts/r2_reader2_haiku.md:11` | "Y. ... without the order rule the planned changes are less concrete." | "planned changes in the portfolio" (Wharton IPS instructions, `WHARTON_WORD.md:73`) |
| `posts/r2_reader2_haiku.md:16` | "my inference is 'don't spend ahead of the cheques'" | Q1 crutch |

Neither reader mentions co-sponsors in a ranking reason. The text they ranked without the line, `arms/C_amara_D1.txt`,
has D's P8 byte for byte (line 15, `diff` against `arms/D_round2_majority.txt` line 15: identical) and P9 without the
order line (line 17). It also lacked "That is under a tenth of her money." and V50's "even for the building", so the
afternoon result does not transfer to D one for one.

**Tonight:** every text ranked (A, B, C) kept the order line, so no ranker tonight read its absence. The probe on D
(`blind/probe_RQWN.md:9`) gave "flexibility gives way first ... protected to the very end is the ten cheques" from P8, but
its question asked for exactly that (`blind/probe.md`, P2). On A the line pulled the actuary's Q1 to "reordering the
priorities" (`blind/answers.md:19`); on C (V50's sentence in P2, line kept) no reader used it for Q1. The professor
preferred the explicit P8 sentence to "the priority order" for the unfavourable case (`blind/rank_fable.md:19, 21`);
the actuary called the order line a patch "by implication" (`blind/rank_opus.md:18`).

## 2. Book 11's full circle
`keel/BIBLE.md:327` (Ahaan): "you stated in the introduction that the pills are labelled with 'do not crush' and then you
used that phrase again in the conclusion. That was the whole power." Both A and D meet it. D's last two lines mirror P2's
"delivers its dose on schedule, labelled do not crush" (dose, then label) and P1's "In January 2033" ("From 2033"). Better
as a circle; not required by Ahaan's words.

## 3. Does D say the floor holds before the top?
No. P6 (`D_round2_majority.txt:11`): "money she already owns", "every dollar she promises is already in bonds"; P7 (:13)
keeps the floor out of stocks; P8 (:15): "Whatever the stocks can't cover lowers the whole range." The design reads that
as both ends: `keel/ips_rewrite/IDEA_LEDGER.md:215` "(the top falls with the floor)"; `keel/ips_rewrite/drafts/D33/README.md:22`
"(which end? kept, as in V52; 'both ends' costs a word)". The afternoon skimmer flagged the clash on A, with the order line
present (`r2_reader2_haiku.md:29`). Ledger E4 ("If anything changes: cheques first, then the floor, then the hope",
`IDEA_LEDGER.md:123`, IN) would land in D as V50's sentence (cheques before the building) plus P8 (promise before
flexibility), not as one stated rule; the ledger row needs that note if D is promoted (Commandment VIII).

## 4. What keeping the line costs at the 497 rule (`keel/ips_rewrite/README.md:13`)

| Text | Strict | sha256 (16) |
|---|---|---|
| D (round-2 majority) | 495 | `fb9c9a8463ce9ddd` (= probe's RQWN) |
| D + order line | 508 | |
| D + order line − P8's ", so her flexibility shrinks before her promise does" | 500 (over 497) | `b247d97dc3ba40f1` |
| D + order line − that clause − "for its gap" (= Tess's round-2 D) | 497 | `72d7069d5b47fee5` |
| D + order line − "That is under a tenth of her money." − "for its gap" | 497 | `7d7cefbbe3389b2a` |

The clause is Genius Lab L-16's fix ("the kept stocks pay the gap first, so say the order", `drafts/D33/README.md:14`) and
the only sentence that puts her promise before her own flexibility (Wharton: "communicates ... investment uncertainty clearly
and credibly to prospective co-sponsors", `WHARTON_WORD.md:36`). "Under a tenth" is the other line the afternoon portfolio
manager named. "for its gap" sits in the reserve line, the Q3 leg that decided tonight's test.

Also on the page: Caplet, Book 10 (`keel/BIBLE.md:293`), says AI judges overweight "'framework lines'"; Commandment III
(`BIBLE.md:361`) "No slogans, no triads". Both lean against letting the afternoon's praise of one triad decide.

## 5. Tripwire proposed for Tuesday's scorecard
If two of Tuesday's three blind rankers say, unprompted, that D lacks a priority or order rule, the order line comes back
as Tess's D (497, `72d7069d5b47fee5`). A tripwire, not a text change.
