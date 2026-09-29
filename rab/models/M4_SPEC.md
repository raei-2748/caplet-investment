# M4 SPEC: the cap share (decision D6), with a pre-registered decision rule

WS2, written and committed 2026-09-30 (Sydney) **before any M4 code was written or run**; the git commit that adds
this file is the pre-registration record. Implementation-independent. AI-generated research (Claude Code) for Team
Caplet; no deliverable text. The result is a decision for the team to ratify (insight_v1 D6, due Mon 26 Oct); nothing
is applied to the IPS or the Sheet.

**Question.** In 2031 Laura announces a range whose top is the floor plus a share s of the stock fund, and the 2033
gift is capped at that top. The adopted default is s = 1/2. Is there a better share, and how should the low end be
announced?

## 1. Inputs

Everything in `M3_SPEC.md` section 1, plus:

| Symbol | Value | Source |
|---|---|---|
| y5 | 0.0506: 5-year par yield, the floor's yield (held as the Jan-2028 rate) | `rab/numbers.yaml` `market.par_curve` 5 Yr (28 Sep 2026) |
| fee_F | 0.0007 a year: the floor fund's expense ratio (iBond ETF) | `rab/models/M1_METHOD.md` E1 (iShares, 0.07%) |
| Delta_r | empirical changes of the 1-year CMT yield over 913 calendar days (30 months), every business day 2 Jan 1990 .. 25 Sep 2026 with an end value | `rab/data/fred/DGS1.csv` (FRED); change = last value on or before (date + 913 days) minus the value on date, in points |
| return paths | the 200,000 paths of M3 models T, BOOT, BAYES (headline variants) and L (reference) | `M3_SPEC.md` section 3 |

## 2. Floor delivery (why the owned floor is not exactly $150,000)

In Laura's real plan the floor is bought in January 2028 in a WInS-listed instrument (strict reading of the FAQ
"for BOTH contributions"; no WInS Treasury matures Feb 2031 - Feb 2036, so an iBond fund such as IBTM). An iBond fund
pays out its income every month and "does not seek to return any predetermined amount" (iShares; rab/assumptions.md
C5), so what the floor finally delivers depends on the rate at which its income is reinvested.

Model (per path, independent of the stock path): cost C = F / (1 + y5)^5; C buys a 5-year par bullet paying y5 C at
the end of each of years 1..5 and C at year 5. Each coupon is reinvested to year 5 at r = max(0, y5 + Delta_r / 100),
with Delta_r drawn uniformly from the empirical list above. Delivery ratio:

    phi = (1 - fee_F)^5 x [1 + y5 x sum_{k=1..5} (1 + r)^(5 - k)] / (1 + y5)^5,   floor paid = phi x F.

(phi = 0.9965 when r = y5; phi = 0.9755 when r = 0.)

## 3. The decision space

x = (s, l, h): s in [0, 1] = share of the fund's 2031 value promised at the top; l in [0, 1] = the fraction of that
stretch also put into the announced low end; h in [0, 0.05] = haircut on the floor when it is announced.

    low end   L = F (1 - h) + l s B3            (adopted: l = 0; h = 0, or "rounded down")
    top       U = F + s B3
    gift      G = min(phi F + s min(B5, B3), U)
    kept      K = phi F + B5 - G

## 4. Measures (defined precisely)

- **Disappointment (primary), D1:** G < L, the gift is below the low end Laura told co-sponsors in 2031. This is the
  case's own test: "If Laura promises more than she can ultimately contribute, she could damage her credibility."
  P_D = P(G < L).
- Reported, not optimised (each is the same for every s when l = 0, because G - F scales with s): D2 top missed,
  G < U; D3 below the middle, G < (L + U) / 2; dollar shortfall below the top, E[U - G].
- **Expected gift** E[G]. **Range width** E[U - L]. **Flexibility** P(K >= 0.10 G): Laura keeps at least 10% of her
  gift. Why 10%: Taiwan construction costs rose about 3.5% a year since 2021 (rab/assumptions.md E8, repo-verified
  27 Sep), and 1.035^3 - 1 = 10.9%, i.e. about three years of cost drift between the 2031 announcement and building.
  The 10% and the 95% below are value judgements, fixed here before any result was seen.

## 5. PRE-REGISTERED DECISION RULE (frozen; any later change must be logged as a deviation)

- **PR-1 Scope.** The recommendation concerns s. The adopted IPS fixes the low end at the owned floor, so l = 0 in the
  recommendation. l > 0 is explored only to price a narrower range (section 6) and is never recommended here; it would
  contradict the IPS and could be at most "note-in-Final-Report". h is a wording choice inside the IPS.
- **PR-2 Models.** The three decision models T, BOOT, BAYES (headline variants), 200,000 paths each, seed 20260930,
  with phi per path from section 2. L is reported for reference and does not vote.
- **PR-3 Announced floor.** h* = the smallest h in {0, 0.005, 0.010, ..., 0.050} with P(phi < 1 - h) <= 0.5%. The
  announced floor A = F (1 - h*) rounded down to a multiple of $5,000. In PR-4 to PR-6, L = A.
- **PR-4 Credibility (hard).** P(G < A) <= 0.5% in every decision model.
- **PR-5 Flexibility (hard).** P(K >= 0.10 G) >= 95% in every decision model.
- **PR-6 Objective.** Maximise E[G]. E[G] rises with s in every model, so in model m the best share s*_m is the
  largest s on the grid {0.00, 0.01, ..., 1.00} that meets PR-4 and PR-5. The robust share s* = min over the three
  models.
- **PR-7 Decisiveness.** If 0.40 <= s* <= 0.60, keep s = 1/2 (the evidence does not justify changing a simple,
  explainable rule). If s* < 0.40, recommend the largest of {1/4, 1/3} not above s* (if s* < 1/4, s* rounded down to
  0.05). If s* > 0.60, recommend the largest of {2/3, 3/4, 1} not above s*. Any recommendation other than 1/2 is
  labelled a decision to ratify, with triage fix-before-6-Nov only if the IPS text states "half".
- **PR-8 Reporting.** Whatever the outcome, publish the s-profile (section 6), the Pareto fronts, and the
  rule-sensitivity table (flexibility threshold 5/10/15/20% x confidence 90/95/99%), and say what would change the
  answer.

## 6. Computations and outputs (`rab/results/M4/`)

1. `floor_delivery.csv`: phi percentiles (p0.5, p1, p5, p50, p95, max); P(phi < 1 - h) for each h on the PR-3 grid;
   h*, A.
2. `s_profile.csv`: for each decision model and L, for s = 0.00 .. 1.00 step 0.01, with l = 0 and L = A: E[G], G p5 /
   p50 / p95, E[K], K p5 / p50, P(K >= 0.10 G), P(G < A), E[U - A], median U, P(top reached), P(G below the middle),
   E[U - G].
3. `decision.csv`: s*_m per model, s*, the PR-7 recommendation, and the adopted s = 1/2's values of every measure.
4. `rule_sensitivity.csv`: s* per model for flexibility thresholds {0.05, 0.10, 0.15, 0.20} x confidence {0.90, 0.95,
   0.99} (A fixed).
5. **Pareto search (pymoo).** Minimise (f1, f2, f3) = (-E[G], P(G < L), E[U - L]) over x = (s, l, h) in
   [0, 1] x [0, 1] x [0, 0.05], subject to 0.95 - P(K >= 0.10 G) <= 0 (L continuous here, not rounded). NSGA-II
   (Deb et al. 2002; pymoo, Blank and Deb 2020), population 120, 200 generations, seed 20260930, evaluated on the
   first 50,000 paths of each decision model; the final non-dominated set is re-evaluated on all 200,000 paths.
   Outputs `pareto_<model>.csv` (s, l, h, E[G], P_D, E[width], P(K >= 0.1 G)).
6. `narrower_range.csv`: "the price of a narrower range" at s = 1/2, h = h*: for l = 0.0, 0.1, ..., 0.9, the median low
   end, median width, and P(G < L) per model.
7. Figures: `fig_M4_s_profile.png` (E[G] and P(K >= 0.1 G) against s, per model, constraint line, adopted s marked),
   `fig_M4_pareto.png` (width against P_D per model, adopted point marked), `fig_M4_floor.png` (phi distribution and
   the announced floor).

## 7. Tolerances (Gate B)

s*_m within 0.02; probabilities within 2 points; E[G] and percentiles within 2%; h* identical; A identical.

## 8. References (DOIs checked on Crossref, 30 Sep 2026)

- Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm:
  NSGA-II. IEEE Trans. Evol. Comput. 6(2), 182-197. doi:10.1109/4235.996017
- Blank, J., & Deb, K. (2020). pymoo: Multi-objective optimization in Python. IEEE Access 8, 89497-89509.
  doi:10.1109/ACCESS.2020.2990567
- WS5 refs [11] Das et al. (2018) (goal tiers and target success rates) and [19] van der Bles et al. (2020) (numeric
  ranges keep trust), `rab/literature/references.md` on rab/ws5.

## 9. Deviations and additions (logged after the first run, 30 Sep 2026; sections 1-8 unchanged)

No change to the decision rule (PR-1 to PR-8) or to any input. Additions, none of which any decision uses:
- A1. `s_profile.csv` also reports `P_top_fund` = P(B5 >= B3). Reason: with phi < 1 the gift almost never equals the
  face-based top U exactly (it falls short by (1 - phi) F), so the spec's D2 measure "G < U" reads as about 75% missed
  even when the fund held its value. D2 is kept as specified.
- A2. The variant "top also announced from the rounded-down floor", U_A = A + s B3 (columns `A_*`, `run_log.txt`).
- A3. A brute-force grid (s, l in steps of 0.05; h in {0, 0.025, 0.05}) on all 200,000 paths, as a check on NSGA-II
  (`pareto_grid_<model>.csv`); the log counts NSGA-II points dominated by a grid point.
- A4. `fig_M4_narrower.png` (plain version of `narrower_range.csv`).

## 10. Gate B clarifications (30 Sep 2026; the decision rule PR-1 to PR-8 is unchanged)

- C1. Section 6.6 (narrower range): which low end? Section 3 with h = h* gives L = F (1 - h*) + l s B3 =
  $146,250 + l s B3. The primary build used the announced floor, L = A + l s B3 = $145,000 + l s B3, which is what
  Laura would actually say. The blind build followed the text literally. At the same typical low end the two readings
  give the same P(G < L) to within 0.04 points in one build, and to within 0.08 points across both builds. Quote the result by the level of the low end (e.g. "about $160k"),
  not by l.
- C2. PR-8 rule sensitivity: the robust s* is "none" when any decision model has no passing share. The primary's
  `run_log.txt` line had skipped the missing model and showed 0.03 at 15% / 99%. This is fixed in `m4_cap.py`; the
  CSV was always right.
- C3. D2 "G = U" depends on the floor draw: it holds only when phi >= 1 + s (B3 - B5)+ / F. Each build samples phi from
  the same 8,565 changes, so the two differ by up to 0.45 points (3.3 standard errors). When phi is averaged over the
  full list, the builds agree to within 0.02 points.
