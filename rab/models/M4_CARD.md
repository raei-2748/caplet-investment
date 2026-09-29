# M4 model card: the cap share (decision D6)

WS2, 30 Sep 2026 (Sydney). Code `rab/models/m4_cap.py`; spec and **pre-registered rule** `M4_SPEC.md` section 5
(committed as 3d98ce0 before any M4 code); results `rab/results/M4/`. AI-generated research (Claude Code). All
figures are Laura's plan, MODEL.

**What it does.** It tests the share s of the stock fund promised at the top of the 2031 range (adopted: half). The
test runs on M3's three decision models, with one addition: the floor itself may pay a little less than $150,000.

**Floor delivery.** Under the strict reading of "for BOTH contributions", the floor in Laura's real plan is a coupon
Treasury or an iBond fund, so its income has to be reinvested. The model reinvests at today's 5-year yield plus a
historical 30-month change in the 1-year yield (FRED DGS1, 1990-2026, 8,565 changes, floored at 0%), less a 0.07%
fund fee. The floor pays $149,404 at the median and $146,330 at worst, and falls short of $150,000 in 69% of cases.
Rule PR-3 therefore announces the floor as **$145,000** (h* = 2.5%, rounded down to $5k). The floor holding alone pays
at least that in every scenario. (A zero-coupon STRIPS would pay exactly $150,000.)

**Result under the pre-registered rule.**

| | Fat tails | History | Uncertain mean |
|---|---|---|---|
| Largest share passing both hard rules (s*) | 0.50 | 0.47 | 0.47 |
| At s = 1/2: chance Laura keeps >= 10% of her gift | 95.3% | 93.6% | 93.2% |
| At s = 1/2: chance the gift is below the announced $145k | 0 | 0 | 0 |
| At s = 1/2: expected gift / kept money 1-in-20 | $174k / $17k | $174k / $15k | $174k / $15k |

The robust s* is 0.47, inside the [0.40, 0.60] band, so PR-7 **keeps one half**. Half sits at the edge of the
flexibility rule: it is about the largest share at which Laura keeps a tenth of her gift in 19 of 20 outcomes.

**What would change it** (`rule_sensitivity.csv`, robust s*): if Laura needs to keep only 5% of the gift, the rule gives
about 0.72 (so 2/3). At 15% it gives about 0.23 (so 1/4). Asking for 99% instead of 95% confidence at 10% gives 0.20.
The answer depends on how much flexibility Laura wants, not on the stock model.

**Three things the share does not change** (the same for every s, because gift minus floor scales with s): the chance
of reaching the top, the chance of landing below the middle, and the chance of breaking the low end. Raising s moves
dollars from Laura's kept money to the gift, one for one in expectation (`fig_M4_s_profile.png`).

**The price of a narrower range** (explored only; PR-1 rules it out as a recommendation because the IPS sets the bottom
at the owned floor). At half, raising the announced low end from $145k to about $155k breaks the promise in 0 to 3 of
10,000 paths. At about $160k it is 3 to 42 in 10,000, and at about $165k it is 0.9% to 2.1%, with the history model
always the worst (`narrower_range.csv`, `fig_M4_narrower.png`). NSGA-II found the same frontier. A brute-force grid
dominates 7-8 of its roughly 120 points (`pareto_*.csv`, `pareto_grid_*.csv`), so treat the front as indicative.

**Added after the first run (not pre-registered; no decision uses it).** If the top is also announced from the
rounded-down floor ($145k + half the fund), the gift reaches the top in 90-93% of paths instead of 72-75%. The median
top falls to about $170k and the expected gift falls by about $3k.

**Limits and failure modes.** The 10% flexibility threshold and the 95% level are value judgements, fixed in advance
(Taiwan building costs rose about 3.5% a year: rab/assumptions.md E8). The floor model is a stylised coupon bullet with
one reinvestment rate per path and no link between rates and stocks. The disappointment odds are small numbers from a
finite sample: 0 in 200,000 is not proof of impossibility.

**What this teaches (plain English).** Promising more of the stock fund does not make it likelier that Laura lets
co-sponsors down. It only decides who gets the upside, the building or Laura's own reserve. Half is about the most she
can promise while still keeping a tenth of her gift aside in 19 of 20 outcomes. Say the floor as $145,000 so that the
"owned" part is true in every case.
