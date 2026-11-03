(Keel is a simulated team, AI-written.)

# Felix, round 1 research notes (judge with the case and Wharton open)

Case, `competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`
- :91-92 "All ten payments must be funded by the investment portfolio with a high degree of certainty."
- :94-99 "Teams must recommend its size and initial asset composition and explain how its composition should change, if at all, as the annual payments approach and are made. They should also define what they consider a high degree of funding certainty, explain how they evaluated that level of certainty, and identify the assumptions supporting their recommendation." Used for C1 (the lock is the evaluation).
- :101-103 "She recognizes that committing all remaining assets could limit her financial flexibility as the project develops." Used for the weakest answer.
- :117-120 "state how confident they are that her 2033 contribution will fall within that range ... The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment." Used for C1, C3.
- p.4 bullet "Preserves appropriate financial flexibility when determining the facility contribution."
- Same section: "Teams are not expected to determine the size or investment composition of a separate contingency fund or endowment."

Wharton, `keel/WHARTON_WORD.md`
- s2 questions: "How will the portfolio's asset allocation and composition change as future funding needs approach and payments are made?"
- s2: "Not expected in the IPS ... final operating-reserve calculations, detailed portfolio projections, a final facility-contribution range, or the draft communication to co-sponsors." Kills C3 for the IPS.
- s2: "Clearly explain your team's investment strategy and the reasoning behind it." (C2.)
- s3: "Judges want to understand not only what your team decided to do, but also the reasoning, assumptions, and tradeoffs behind those decisions." (C4.)

Word counts (`textcheck.py`, scratch copy /tmp/claude-0/felix_scratch.txt, draft not edited; strict = hyphens split)
- V54 as filed: 497 strict (496 by spaces).
- J wording "as if money paid later sat idle," replaces "at that day's yields, plus a cushion,": 7 v 7 words, +0.
- Fix: "and returning to Laura what the cheques don't need." = 9 strict (end of P9, in place of the full stop). The chair's "and handing back to Laura whatever each rung didn't need" = 10.
- Cuts for 9: ", spread across thousands of companies" 5; "to us," 2 (P3, "That, to us, is what" becomes "That is what"); "roughly" 1; "first" 1 ("deposit first finishes"). Result with J: 497 strict, 496 by spaces. Alternative cut set: "spread across ..." 5 + "liquid any day," 3 + "roughly" 1, but "liquid" is Wharton's own word, so I would keep it.

Table read (BRIEF, MODEL, never in the IPS): KW leaves Laura's kept stocks gone by 2033 in 28.1% / 72.8% / 90.3% of futures; about $17,953 median returns after 2033. That gap is why the return sentence matters.
