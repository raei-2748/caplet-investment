# The mock judges, rebuilt (Fri 30 Oct 2026, Commandment IX)

AI-generated (Claude Code). Caplet, 30 Oct (BIBLE Book 10): the old judges were "diverse not just in label" in name
only, "approving almost every change", converging on single sentences and "framework lines", and "thinking
suspiciously similarly to both one another and Keel and you". Their "only allegiance in terms of marking is to the
marking guide from Wharton, and ABSOLUTELY NOTHING ELSE."

## What was wrong with the old panels (diagnosis)
1. **Same model, same prompt shape.** Every judge was the same model with a different job title, so they shared one
   taste: elegant sentences, internal consistency, quotable lines.
2. **They knew what we wanted.** Panels were briefed with our change notes ("V29 settles the coupon gap ...") or asked
   head-to-head "V29 vs V28", so they rewarded the change we had just made.
3. **They hunted sentences.** Prompts asked for "the line that wins" and "the weakest line", which taught them to
   decide on one sentence.
4. **No outside field.** Most panels compared our drafts only with each other, so "better than last night" passed for
   "top 50 of 2,300".
5. **Nobody measured agreement.** Identical rankings were reported as confidence, not as a warning.

## The new panel: six judges, different in model, priors and method
Every judge reads the same six blind entries in a **different random order** (three of ours, three simulated rivals of
different strategies), gets **only** Wharton's word (`../../WHARTON_WORD.md`) and the case, never our notes, and is
told that no single sentence may decide a score.

| # | Judge | Model | Prior (what they believe going in) | Method (how they decide) |
|---|---|---|---|---|
| J1 | **The skimmer**: alumni volunteer, marketing background, 40 entries tonight | Haiku | Good strategies are easy to explain | Reads each entry once, never re-reads; gut score per criterion; lists every sentence not understood first time |
| J2 | **The growth hawk**: ex equity portfolio manager | Sonnet | A client "willing to take thoughtful risks" with 6-16 years is short-changed by bond-heavy plans | Advance / don't advance each entry, then rank; must name the upside each plan gave away |
| J3 | **The actuary**: pension liability-matching specialist | Opus | Most student plans have a hole nobody priced | Stress-tests each plan's logic against the case's cash flows, finds its failure point; criterion points |
| J4 | **The teacher**: economics teacher who has judged student competitions for years | Sonnet | Polish is cheap; real thinking by real students is rare | One holistic read for voice and honesty, then rank; asks "does this sound like teenagers who did the work?" |
| J5 | **The professor**: decision-science professor | Fable | A standard ladder is table stakes; only a new idea earns a top score | Pairwise tournament; for each entry, "what did I learn that I didn't know?" |
| J6 | **The programme manager**: runs the competition | Haiku | Teams that answer the question asked win | Ticks Wharton's five "make it clear" points and the five criteria, then ranks |

**Disagreement is the point.** The panel file reports Kendall's tau between every pair of judges. If the average is
above 0.6, or every judge puts the same entry first for the same reason, the panel is suspect and is rebuilt before
anyone believes it.

## Files
`panel_V31/` = the first panel, `panel_V32/` = the second (entries per judge, KEY.json, each judge's scores,
SUMMARY.md with the agreement statistics and what Keel did about it).
