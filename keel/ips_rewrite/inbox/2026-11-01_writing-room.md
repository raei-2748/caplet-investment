# Writing Room -> the rewrite thread, Sun 1 Nov 2026: five places, one page (round 5, beat 7; huddle H-012)

> **Late, 17:40 Sydney: W1 is withdrawn; read `../../drafts/writing_room_2026-11-01/V50_check.md` first.** Ahaan's
> Book 11 (16:26) rejected V49 and the thread rebuilt it as V50 while this run was reading. W1 breaks Book 11 four ways
> (the opening question, "our model" and its numbers, "we built it first", "Do not crush." cut). **Two findings are
> live in V50:** (1) the top end lost its 2031 move into Treasuries, so a fall after naming comes off a number said
> aloud, which V50's own para 7 rules out (fix +12: "Before any co-sponsor hears the number, that half moves into
> Treasuries too."); (2) the 2028 deposit's first job, finishing the ladder if the first $300,000 falls short, is gone,
> so para 3 and para 5 ("sized to grow back to the deposit") overclaim (fix +11). Both need no figures. V50 is at 497,
> so 23 words must go as whole ideas; one candidate is para 8's second half, which repeats para 7 (-21).
> The record below is how today's rooms' offers were judged on V49; it stays for the method and the Final Report.

AI-generated (Claude Code), the Writing Room (Tess hosts; Amara, Kai). (Keel is a simulated team, AI-written.)
Suggestions only; the thread drafts. Every arm, sheet, reader reply and count: `../../drafts/writing_room_2026-11-01/`
(README first). Read against **V49** (D29, branch `claude/project-thread-3ahu9r`, 493 strict). GPTZero: not yet checked.

## The offer: W1, V49 with today's rooms folded in, 497 strict (pitch unchanged, 49)
Full text `../../drafts/writing_room_2026-11-01/final_package_W1.txt` (AI DRAFT, Claude, 1 Nov 2026); diff against
V49 beside it. Every room's paragraph was read like for like against V49's own by two blind outside readers on other
models (Haiku 5.5; Sonnet 5.5 as a portfolio manager who distrusts marketing), then argued over three rounds, then
paraphrased by a cold reader on a small model (Commandment IV).

| Place | Taken | Readers (Haiku / Sonnet) | Room |
|---|---|---|---|
| Opener | V49's own, **"shopping problem" kept** (Laura's Room's cut overturned) | 1st / 1st | 3-0 |
| P4 | + "If the recession halves that deposit, our model bounces a cheque once in 66." (Laura's Room, LR-09 S9) | 1st / 1st | 3-0 |
| P6 | V49's own; the $145,000 leaves P9 instead of a bridge in P6 | (bridge 1st / 1st, but reader 2 took "a fund's payout" for the stock fund) | 3-0 |
| P7 | Laura's Room's repair ("So in January 2031, before any co-sponsor hears a number ...") | 1st / 1st | 3-0 (r3) |
| P9 | V49's own + the Courtroom's callback "that morning comes mid-slump" + the linked pair | 2nd / 1st | 3-0 |

**Paid by** (whole lines, never squeezes): both headings, "Sounds good, on average.", "Do not crush." (both outside
readers would cut it; Caplet praised it on 25 Oct, so this is the thread's call, and "it only works whole" stays),
"The US government defaults." (to the Final Report), ", not after", and the $145,000 in P9.

## Five hard issues in V49 (each with its minimal fix; all are in W1)
1. **P5 "enough to grow back into all of it" is false in about 47 modelled futures in 100.** If the ladder costs more
   than $300,000 in January 2027, the 2028 deposit tops it up first and the floor is lower by the same amount (L-10
   `results.json`: `p_ladder_over_300k` 0.4693, median $9,758 when it does; `IPS_number_sheet.md` line 14 says so; it
   also contradicts P2's "or nearly"). Fix (0 words): "enough to grow back into whatever the ladder didn't take: her floor." (Kai, round 3)
2. **P7 is mis-timed** (Laura's Room): before naming day there is no top for a rise to pass. Fix (+1): Laura's Room's
   repair, which both outside readers put first of four.
3. **P9's worst-twentieth pair comes from the world P4 argues against** (the Window's near-breach 2). Fix (0): about
   $85,000 against our $135,000 (Archive A26, S1, linked; the mean lead $15,399 still reads "about $15,000").
4. **"Set-aside" is never introduced, and P4 says the shortfall comes "from what she keeps", so no reader can see why
   our bottom falls to $135,000** (outside reader 2; both cold readers failed the same question). In the model the
   uncovered gap comes off the floor once her half runs out, and both ends step down (L-13 `run.py:29`; L-15
   `run.py:92`). Fix (+1 with ", not after" gone): "take it from what she keeps, then the gift's floor, before she
   names a range." and in P9 "after the shortfall".
5. **The $150,000 floor beside "our typical bottom, $145,000"** (the Window's near-breach 1; a judge tripped on it 31
   Oct; both outside readers flagged it). Fix (-2): drop the figure, "Matched in our model to our typical bottom, it
   leaves Laura ...". The bridge (+14) costs more and reads "a fund" as the stock fund.

## What the readers said about lines nobody offered to change
- **Read twice by all four readers:** "The rest, the interest they should earn". W1 adds "worth" (+1). "Grow back
  into all of it" was the other (now fix 1).
- **"Why 97 and not 100 once the half is in Treasuries?"** Three readers. L-13 has the answer (the 2033 top-up after
  naming; a median miss of about $1,000, sent to the Final Report in V43). The room's seed: does it come back, and
  what pays for it?
- **"We'd pay the $15,000" is asserted, not argued** (reader 2, who wanted the case's credibility line). Kai ruled
  it taste: the rival buys its bottom before naming it, so it never promises more than it owns either; the
  credibility line doesn't separate the two plans.
- QUOTE picks: "Whatever breaks, the order will not change: the cheques, then the floor, then the hope." (Haiku);
  the capital-protected-note sentence (Sonnet). Both CUT picks: "Do not crush."

## Requests closed
The Library's like-for-like read (Jun's P6 bridged, Kai's P8 repaired; Amara's P7 binned by the Lab), the Genius Lab's
Nora (i) read, the Window's flat yes and bridge, the Courtroom's callback, and the Kitchen's agreed value. Verdicts:
Kai's repaired P8 came first with one reader and last with the other ("the rival has a flaw – and we can say where" is
"marketing voice"), +26: not taken. The flat yes read as "a device" and "staged": not taken. The agreed value read as
"unexplained insurance jargon" and 4th-5th; Amara dropped it herself (a premium is certain cash; Laura's $15,000 is an
average she may never pay; MoneySmart, "Choosing car insurance", read 1 Nov 2026: "If you use an agreed value, you'll
pay a higher premium", not "always cheaper"). The Courtroom's callback is in.
