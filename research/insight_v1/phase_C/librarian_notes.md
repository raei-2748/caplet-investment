# Phase C Librarian notes: merging the 472 Phase B questions

Summary: the 472 questions (20 Phase B agents, 10 lenses; exact duplicates already removed) collapse into
**248 clusters**: 109 merged clusters that hold 333 questions, plus 139 singletons. Every input id appears in exactly
one cluster; this was checked with Python (472 ids in, 472 ids out, no id repeated, none missing). No id was left
unplaced. File: `research/insight_v1/phase_C/librarian_clusters.json` (list of `{source_ids, canonical_text,
domain_tag}`, largest clusters first).

Method (ASSUMPTION: this is a judgement rule, not a formula): two questions were merged only when answering one would
take the same research as answering the other and would change the same decision, number or sentence. Related
questions that change different things stayed apart. For example, "what share of the 2031 sleeve to lock"
(B6a-07/B6b-02/B10a-07), "lock progressively before 2031" (B4a-16/B10a-09/B9a-10) and "barbell in 2028" (B10a-02)
are three clusters. So are "which chart" and "which words label the range ends". Each canonical question keeps the
sharpest member's wording and its concrete anchor (for example $300k, 173 of 185 days, 27bp, ~$204k, 42-46% of paths).

Cluster sizes: 4 clusters of 7, 1 of 6, 6 of 5, 23 of 4, 27 of 3, 48 of 2, 139 of 1.
Domain tags of the 248 clusters: D9 53, D5 30, D3 29, D7 25, D6 24, D8 23, D1 21, D10 21, D4 15, D2 7.

## Biggest clusters (and how many separate lenses asked them)

| Size | Lenses | Tag | What it is about |
|---|---|---|---|
| 7 | 5 (B1,B2,B4,B7,B8) | D9 | A fixed format for every WInS trade note: a one-line purpose, a role named in the Guide's own words, one dated cash flow of Laura's, one checkable number and one named risk |
| 7 | 5 (B2,B3,B4,B8,B10) | D1 | The rule if rates fall and the ladder costs more than $300k in January 2027: buy what the deposit affords, longest rungs first, then top up from the 2028 deposit ("fully funded by 1 Jan 2028 at the latest") |
| 7 | 5 (B1,B4,B8,B9,B10) | D5 | An explicit rule or share for "financial flexibility" (the money kept uncommitted after the reserve), instead of "whatever is left" |
| 7 | 3 (B1,B4,B7) | D7 | Making the three Trading Notes "supported / tested / refined", with a pre-written rule that fires a real trade before Oct 23 |
| 6 | 5 (B1,B2,B3,B7,B9) | D10 | Whether WInS should hold the literal 2027 book (about 97% ladder) or the post-2028 target mix, and the one sentence that joins WInS to the 16-year plan |
| 5 | 4 (B2,B4,B7,B8) | D6 | A pre-committed "bad-year rule" for Laura's emotions in a downturn |
| 5 | 4 (B2,B4,B8,B9) | D5 | Ordering the 2031 message: bought floor first, then a conditional stretch, then an invitation to partners |
| 5 | 4 (B3,B5,B8,B9) | D2 | AI exposure: no "AI hedge" tilt, plain disclosure of index concentration, any tilt left to Laura |
| 5 | 3 (B1,B7,B10) | D8 | Which "if X, then Y" rules the IPS must pre-declare, so the Final Report applies them instead of redesigning |
| 5 | 2 (B3,B9) | D3 | The correlation between the 2028 deposit and 2027 equity returns, or named scenarios instead |
| 5 | 2 (B7,B10) | D7 | What makes our lock-early plan different from the textbook answer that AI tools and hundreds of teams will give |

## Themes that many lenses asked on their own (a signal of importance)

These are the places where agents with different briefs (case anomalies, Wharton history, Laura's record,
practitioner benchmarks, markets, co-sponsors, judging, behaviour, red team) reached the same question separately.
Counting lenses rather than questions is fairer, because one agent can repeat itself.

1. **The WInS book and the Trading Notes as evidence (tier 1, due now).** Five clusters, with 4-5 lenses each: the
   note format, supported/tested/refined, staged hedge trades, how our note differs from Wharton's Treasury-ETF
   example, and the "literal 2027 book" question. Taken together: WInS is the rehearsal of Laura's January 2027
   purchase, and every note must show it.
2. **Laura's risk tolerance, stated in her own terms.** Four clusters over B2, B3, B4, B7, B8, B9, B10: ability vs
   willingness; "floor first, then leap" from her career move; a low total equity share reading as timid; a stated
   loss she can accept on the sleeve. A plain risk-tolerance sentence is the most-asked Laura-specific item.
3. **The 2031 co-sponsor range.** At least ten clusters: range today vs rule in 2031, confidence defined on the
   bottom, bought floor plus stretch, what funders count, the lock share, where money above the top goes, the chart,
   the late-2032 checkpoint. Every co-sponsor-facing lens (B1, B2, B4, B6, B8, B9, B10) came back to "the floor is
   the only promise".
4. **Pre-commitment rules in the 500-word IPS.** Contingency rules, governance, the rates-fall rule, the late-deposit
   sentence, the bad-year rule, no regret after the lock. The official "no redesign after results" line (Guide p.5)
   pushed five lenses to the same list.
5. **The 2028 deposit as the main uncertainty that is not market risk.** Correlation vs scenarios, how late, what
   label goes on "will", the joint tail with falling rates, and political rather than market drivers of her income.
   This is asked by B3, B5, B8, B9, B10.
6. **Refusing tokenism.** Identity-themed securities, book-title puns, "gimmicks", the swap test, Taiwan and Wuhan,
   the pull quote's attribution. Six lenses separately said to use her professional record, never her identity, as
   the reason.
7. **Fees and honest disclosure.** Fee on the sleeve only, what her CFPB and trading-desk background would check,
   AI-use record, banned "finance-bro" words, adviser-style disclosure instead of a pitch. Lenses B1, B2, B3, B4, B7,
   B8, B9, B10.
8. **Taiwan and currency risk.** TSMC and AI concentration in the sleeve, the single correlated crisis scenario, an
   NT$ band vs a US$ range, and facility-cost inflation. These questions are mostly from B3, B5 and B8 and are more
   spread out, as smaller clusters.

Lens-specific singletons are not weaker because they are singletons. Many are sharp technical checks that only one
lens could raise (e.g. B5a-06 Nov-15 maturities as a payment-delay buffer, B1a-06 the WInS volume rule, B7b-14 the
word counter). The ranking phase should judge them on value, not on repetition.

## Judgement calls the next phase may want to revisit
- B2a-02 (narrative spine + WInS mirror) and B2a-11 (cash-flow calendar + note names cash flow) each have two parts;
  I placed them by their decision part (the WInS book; the note format).
- B8a-09 sits with "political vs market drivers of her income", not with the "media underweight" cluster, although it
  touches both.
- B10b-04 (equity "hump" incoherent) was merged with the "reads as timid" cluster because both are fixed by one
  goal-by-goal risk sentence.
- The historical-paths cluster (B6b-22, B10a-18, B5b-23) merges three tests of different outputs because they need
  the same backtest.

## What this teaches
Many questions come down to a few decisions. 472 questions from 20 agents turned into 248 distinct ones, and about a
dozen themes were asked independently by four or five different lenses. When people looking from different angles
ask the same thing, that question is probably central, so it deserves research time first. Merging also forces
precision: two questions are "the same" only if the same research would change the same decision. That test stops a
librarian from blurring "how big is the floor" into "how do we word the floor", which need different work.
