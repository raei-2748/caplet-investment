# D28: V48, Sun 1 Nov 2026, built from great human sentences (AI DRAFT, Claude; GPTZero: not yet checked)

Caplet's ask (Sun 1 Nov, 10:34 Sydney): "browse exceptional essays and blogs and papers, steal their sentences, and
rephrase them to communicate our meaning. Every sentence need to have a source ... Compelling, nuanced and exceptional
writing with strong, coherent voice and human taste." Then: "Rephrase and steal their tone, structure, and sentences.
Re-assemble sentence by sentence."

**What this is.** V47's ideas and numbers, every one, written again one sentence at a time: each sentence takes the
shape, rhythm and turn of a real sentence by one of 15 writers (Feynman, Didion, Orwell, E. B. White, Buffett, Marks,
Munger, Galbraith, Schwed, Housel, Levine, Bogle, Paul Graham, Sun Tzu, RBA Governor Glenn Stevens) and fills it
with Caplet's meaning. **`SOURCE_LOG.md`** maps all 33 sentences, both headings and the pitch's four sentences to their source, URL and original
sentence, and names every place a few common words overlap. Nothing is copied: the IPS can't cite, so a judge who
spotted a famous writer's phrasing would have an integrity problem. Ahaan's essays were the tuning fork: every borrowed
shape had to sound like him once filled.

Files: `pitch.txt` (49 words), `ips_V48.txt` (**497 strict**, 492 by spaces; `keel/office/tools/textcheck.py`, cap 497),
`SOURCE_LOG.md`, `COLD_READ.md` and `VOICE_READ.md` (two blind readers; see "After the readers").

**Changed from V47 (sentences only).** Two headings that pun and argue ("How to bounce a cheque", Munger's inversion;
"Know thy rival", a bent proverb). A question opening that puts the judge in Laura's chair. The
certainty paragraph as numbered prescriptions (first, second, third), with the recession told as Schwed's two-step
(the same event cutting both ways). The capital-protected note explained before it's named (where the interest goes,
from Levine). The capped range's catch as a warning label, which the closing "Do not crush" pays off. The lock as the
calm version of a later panic sale. The rival's average answered "Sounds good, on average." and its bad case said
flat. The pitch no longer repeats the body's best line word for word.

## Every V47 idea, and where it is now
| V47 idea | V48 sentence |
|---|---|
| One promise, one hope, kept apart | 1-3 (the question, "Laura Gao has to", the gift as a hope) |
| Don't invest the promise; buy it | 4 ("a shopping problem, not an investing one"); pitch P2-P3 |
| First $300,000 buys all ten – or nearly – in January 2027; bonds and funds that mature like bonds, one per January | 5-6 |
| A high degree of certainty is a list of ways to fail | H1, 7 |
| US default | 8 |
| A recession before we buy: dearer ladder AND a smaller 2028 deposit (her income is recession-linked) | 9-10 |
| The leak: early cash earns less if yields fall | 11 (now said plainly: cash that arrives before it's needed) |
| Price it in 2031, set it aside from what she keeps, before any gift | 12 |
| Floor: most of the 2028 deposit in Treasuries maturing late 2032 that grow back into all of it | 13 |
| The floor's expected interest buys one world index fund | 14 |
| A capital-protected note minus the bank's option; shares can't expire worthless | 15 |
| 2031 range: bottom = floor; top = floor + half her stocks | 16-18 |
| The other half stays hers: liquid any day; Taiwan-dollar building costs | 19 |
| The capped range's catch | 20 |
| The lock on naming day | 21 |
| 97 in 100 reach the top (model) | 22 |
| Our first plan, three-quarters stocks, sunk by our own model | 23 |
| Laura's thoughtful risks; the strongest rival (same ladder, deposit mostly stocks, bottom bought January 2031) | 24 |
| $145,000 median bottom; about $15,000 more on average by 2042, gift and what she keeps counted | 25 |
| Worst twentieth of 2028-30: about $90,000 v our $140,000 after the set-aside | 27 |
| We'd pay the $15,000 | 28 |
| From 2033 the ladder is the operating reserve and runs itself down | 29 |
| Priority: cheques, then floor, then hope | 30 |
| Caplet XR: extended release; ten redemptions, one a year; only works whole | 31 |
| Do not crush | 32 |

Nothing whole was cut. Words paid for the headings and the opening question: "the US government defaults" kept,
"paid from this portfolio alone" became "out of one portfolio", "There is a serious case against all this, and we made
it first" became the heading plus "We know it well".

## Numbers and their sources (unchanged from V47)
| Figure | Source |
|---|---|
| $300,000, $150,000 (2028), $50,000 x 10 from 2033 | Client case |
| "all ten – or nearly" | Ladder cost on the latest curve vs $300,000 (`keel/library/ips_numbers_2026-10/`, `keel/models/`) |
| about 97 times in 100 | L-13 (lock + set-aside before naming), Lab ("In our model") |
| $145,000 median bottom; about $15,000 more on average by 2042; about $90,000 v $140,000 | Archive A26, rival A09 (`keel/rooms/archive_checks/A26_results.json`, S0, k 0.75-0.77) ("Modelled", "our model's") |
| three-quarters stocks first plan | 27 Sep model (`keel/library/verified_2026-09-27/strategy_mc.py`) |

Still open from V47's check: the floor ($150,000 deposit) to the $145,000 median bottom isn't bridged in the text; no
stated return assumption; the worst-twentieth slice is the S0 world (S1, rates and stocks falling together, gives
$85,000 v $135,000).

## After the readers (both read the first full text, blind)
**Voice (`VOICE_READ.md`): V48 first, V47 second**, "a clear margin, not a wide one". V48 sounds more like the essays'
author (sets the reader a problem first, pun headings, explains before it jokes, deflates its own good news, and
earns "Do not crush"), and it is easier on one read (numbered risks, the bank's option explained, the lock's reason
given). V47 is "the steadier single voice" and keeps the two best lines in either ("So we don't invest the promise. We
buy it."; "a list of ways to fail, not an adjective"). V48's fault: "mildly" a collage, one author changing costume.
**Cold read (`COLD_READ.md`):** "one voice, not a collage, but it doesn't sound like Ahaan ... a columnist's ... all
kickers"; clear in outline; numbers mostly sourced.

**Fixed the same morning (the readers' points that cost no idea):** "its building" made "the residency's building";
"before we buy" made "before January 2027"; "coupons and early repayments" (Treasuries don't repay early) made "cash
that arrives before it's needed"; "Modelled to name our $145,000 median bottom" made "Asked in our model to name our
typical bottom, $145,000"; "The proper fix is ..." (a consultant prescribing) made "So in 2031 we price ..." (the team
acting); "Prescriptions for a bounced cheque" (used the pharmacy before the capsule appears) made "How to bounce a
cheque"; "Sell low, by appointment" (Laura's own lock also sells on a set day, so the joke could land on our plan)
made "Know thy rival", with "Admittedly" (a stiff hinge) made "We know it well:"; the priority line given a trigger
("Whatever breaks, ..."); four of nine colons turned into commas, full stops or "as". Paid for with "can fall but"
(V47 never had it) and five small words.

**Still open (for the next round, each with its reader):** the bottom has three faces in the rival paragraph (the
owned floor, the "typical" $145,000, "$140,000 after the 2031 set-aside"), cold read; why 97 and not 100 once the
promised half is locked, cold read; "what she keeps" before the kept half is introduced, cold read; the pitch's
"Treasuries that repay it" (the "it" slides from the promise to the deposit), both readers; "all ten – or nearly" has
no size, cold read; inflation and the return assumption never stated, cold read (V47 the same); "all kickers": Ahaan
builds long and lands short, so the next pass should turn two or three short lines into one dash-hinged build, cold
read. Neither reader re-read the fixed text.

## The commandments check (`../../COMMANDMENTS_CHECK.md`; evidence from the two blind readers unless marked)
| # | Commandment | Evidence | Pass? |
|---|---|---|---|
| I | Extraordinary, by our own light | Cold read's three retellable ideas: "the cheques are a shopping problem" (the field's default, buy the payments), the home-made capital-protected note that "can't expire worthless" (default structure, fresh framing), "We'd pay the $15,000" against a priced rival ("the most original move") | Open: one of three is the default |
| II | Wharton's word is the only marking scheme | Both readers argued from the criteria and the IPS questions (cold read s6), not from favourite lines | Pass |
| III | Write like us | Build-then-land: "If you had to pay ... how would you invest? Laura Gao has to."; concession + "But": "Sounds good, on average. But in our model's worst twentieth ..."; wry: "a shopping problem, not an investing one"; real event: "our first plan was three-quarters stocks, until our own model sank it". Voice read: V48 over V47. Cold read: "all kickers" | Open: the moves are there; the long builds aren't |
| IV | Clear on one reading | Cold read's read-twice list; seven fixed, four open (above); not re-read | Fail until re-read |
| V | Every number explains itself | Modelled figures say "our model" or "Asked in our model"; the case's numbers are the case's. "or nearly" has no size | Open (one) |
| VI | GPTZero before Caplet | Not reachable from this environment (`../../DETECTOR_LOG.md`) | Not yet checked |
| VII | Few ideas, full size | Cold read's summary: "The first $300k buys Treasuries maturing before each payment. The 2028 money buys Treasuries that grow back to the deposit, with the interest in a global stock fund. In 2031 Laura promises the floor plus half the stocks, locks that half into bonds, and keeps the rest." | Pass |
| VIII | Lose no idea; critique borrowed ones | Every V47 idea mapped above (writer's map); the note critiqued (the bank's option can expire worthless; shares can't), the rival priced in full | Pass (writer's map; no second reader) |
| IX | Judges who disagree | No six-judge panel run on V48; one blind voice A/B only | Open |
| X | Improve without being asked | `../../THINKING_LOG.md`, Sun 1 Nov, late morning | Pass |

GPTZero: not yet checked. Not for submission as written: Caplet rewrites in its own words.
