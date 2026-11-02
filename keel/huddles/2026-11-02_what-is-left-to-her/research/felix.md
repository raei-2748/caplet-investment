(Keel is a simulated team, AI-written.)

# Felix, round 1: the lines I quoted (read Mon 2 Nov 2026, Sydney; all files in the repo, nothing fetched online)

## The case (`competition/official/2026_27/Laura_Gao_2026_Client_Profile.txt`)
- :88-89 "Laura will make ten annual payments of $50,000 toward the residency's operating expenses, one at the
  beginning of each year from 2033 through 2042."
- :91-92 "All ten payments must be funded by the investment portfolio with a high degree of certainty. Teams may not rely
  on co-sponsors, grants, program fees, or other outside funding to meet this requirement."
- :95-97 "This set-aside is called the operating reserve. Teams must recommend its size and initial asset composition
  and explain how its composition should change, if at all, as the annual payments approach and are made."
- :97-99 "They should also define what they consider a high degree of funding certainty, explain how they evaluated
  that level of certainty, and identify the assumptions supporting their recommendation."
- :101-103 "After establishing the operating reserve in 2033, Laura must decide how much of the remaining portfolio she
  can responsibly contribute toward the cost of establishing the residency facility. She recognizes that committing all
  remaining assets could limit her financial flexibility as the project develops."
- :104-105 "Teams must recommend and justify the extent to which Laura can responsibly contribute, based on their
  investment strategy, projected portfolio outcomes, assumptions, and understanding of her goals."
- :110-112 "A meaningful personal contribution may signal that the residency is financially viable, demonstrate Laura's
  commitment to the project, and make potential co-sponsors more willing to contribute."
- :114-116 "If Laura promises more than she can ultimately contribute, she could damage her credibility and lose the
  confidence or participation of co-sponsors. Rather than promising one exact amount, she wants to communicate a
  credible range for her potential contribution."
- :118-120 "They should explain how favorable and unfavorable market outcomes could affect the amount she can provide.
  The proposed range must also protect the portfolio's ability to fund the ten-year operating commitment."
- :134-145 (the strategy bullets; present in the text export, contrary to the brief :37) ending at :145 "Preserves
  appropriate financial flexibility when determining the facility contribution."
- :146-148 "Teams should identify and explain their assumptions about investment performance, the timing of cash flows,
  outside funding, the effect of inflation on portfolio projections and facility costs, and the financial flexibility
  Laura should preserve."

## Wharton's word (`keel/WHARTON_WORD.md`)
- :38 "The Trading Notes Analysis, the IPS and the Final Report are judged together on these five."
- :53-54 "How will the portfolio's asset allocation and composition change as future funding needs approach and payments
  are made?"
- :55-56 "How will your strategy protect the operating commitment while preserving flexibility for a responsible facility
  contribution?"
- :67-69 "establish your strategic approach to preparing for the operating commitment, managing the operating reserve's
  asset composition over time, determining a responsible facility contribution, and preserving appropriate financial
  flexibility."
- :85-86 Not expected in the IPS: "final operating-reserve calculations, detailed portfolio projections, a final
  facility-contribution range, or the draft communication to co-sponsors."

## The draft (`keel/ips_rewrite/drafts/D33/`)
- `ips_V53.txt` :9 (P5) "The remainder, roughly the interest it should earn, goes into one world index fund, spread
  across thousands of companies. That is under a tenth of her money."
- `ips_V53.txt` :11 (P6) "The other half stays with Laura, liquid any day, as her flexibility, in case the building
  costs more in Taiwan dollars."
- `ips_V53.txt` :13 (P7) "But a number said aloud to co-sponsors cannot be quietly halved if markets turn."
- `ips_V53.txt` :15 (P8) "If yields fall and stay low, that interest earns less, and the ladder falls short. Before she
  names the range, we price that gap at that day's yields, add a cushion, and set it aside from the stocks Laura keeps,
  so her flexibility shrinks before her promise does. Whatever the stocks can't cover lowers the whole range."
- `ips_V53.txt` :17 (P9) "From 2033, the ladder becomes the operating reserve, paying out one bond per cheque."
- `pitch.txt` :1 "Laura's ten $50,000 cheques are a promise, so we don't invest for them."
- `README.md` (P5 row): "about a fifteenth of her money" became "under a tenth of her money" because "a fifteenth holds
  only at today's yields" (Library O2).

## The model, read to check the chair's reading (MODEL; none of it goes into the IPS)
- `keel/rooms/lauras_room/LR-10_what_is_left_to_her.py` :37-40 (A0): `x_ = np.minimum(need31_, 0.5 * V31)` and
  `u31_ = ceil5(np.maximum(need31_ - 0.5 * V31, 0))`: the range comes down only after the kept half is used up, so
  under A0 "range lowered on naming day" equals "kept half empty on naming day" (S6: 62.8 in 100).
- Same file :42-50 (H): `x_ = np.minimum(need31_, (1 - phi_) * 0.5 * V31)`, then the rest from the promised half
  (`y_`), the quote lowered at both ends.
- `keel/rooms/lab/L-16_two_jobs_one_pocket/run.py` :48-50: `at_2033(...)` is passed the kept half; `fgift = cash - c0 -
  sold` ("the gift pays a cheque after naming"). The kept stocks are sold first, then the gift. The chair's reading
  (brief :88-90) holds.
- Brief tables :62-70 and :75-86 (the figures I used: kept half gone, range lowered, top reached, median top).

## The locked TNA and the ledger
- `keel/ips_rewrite/00_GROUND_TRUTH.md` :64-65: nominal Treasury "matches the liability perfectly", no TIPS.
- `keel/VOICE.md` :36 (Ahaan's locked reflection): TIPS "would hedge against an inflation risk that is nonexistent".
- `keel/ips_rewrite/IDEA_LEDGER.md` :54 "Inflation can shrink what $50,000 buys, can't bounce a cheque (M4): Final Report."
  :150 "the inflation pair (**B9** -> FR; the 'dearer building' clause stays)".

## Count (scratch copy, not in the repo)
`/tmp/claude-0/-home-user-caplet-investment/d9b76da1-3b4f-5017-8958-dde1849a8130/scratchpad/V53_felix.txt` = V53
with the P8 swap (+2), the P9 swap (+6), the P5 cut (-8). `textcheck.py`: "496 by spaces, 497 split on hyphens".
