# D7: How the WInS account represents the strategy

**Status:** DECIDED (two branches, pending Q1–Q3 in `00_open_questions.md`) · **Evidence:** D1, D3, D4; Wharton FAQ; Trading Notes brief

## Question
WInS is a short-term, virtual account (trading 28 Sep – 4 Dec 2026), and its gains don't enter Laura's projections. How do we use it to *show* a strategy that is mostly a Treasury ladder, when we don't yet know which securities WInS allows?

## Facts
- Wharton: WInS standings "have little to do with the final outcome." The Trading Notes Analysis (due 23 Oct) must "demonstrate how [our] investment decisions reflected the strategy," and the case adds that trades should show how decisions "reflected, tested, or refined" it.
- **Unverified:** starting cash ($100k or $500k); whether ETFs, including bond ETFs, are tradeable. An unofficial page says stocks from an approved list only, with Treasuries "recommended but not traded on WInS."
- Laura's steady-state mix after 2028 (Strategy A, today's yields): ladder ≈ $298k of $450k ≈ **66%**; growth sleeve ≈ **34%** (80/20 → ~27% equity, ~7% Treasuries).

## Options
1. **Mirror:** WInS holds the full strategy in proportion.
2. **Sleeve only:** WInS holds only the equity part of the growth sleeve; the reserve is tracked on paper.
3. **All-stock "active" portfolio** with no link to the reserve. **Rejected:** it would contradict the IPS, and judges penalise inconsistency across the three deliverables.

## Debate
- **Advocate (branch by rules):** Consistency across the three deliverables is an explicit criterion. If bond ETFs are allowed, mirroring is the strongest proof we mean it. If not, we must say clearly what WInS represents.
- **Opponent:** A 66% bond WInS account gives little to write about in the Trading Notes.
- **Advocate:** The Trading Notes should show *decisions*, not activity. Some examples:
  - building the ladder;
  - tracking that its value moves with the liability when yields change (the hedge working live);
  - choosing each stock with the D4 filters;
  - a rebalancing rule triggered by drift.
  Those are richer notes than 30 stock trades.
- **Judge:** Branch on the rules. In the stocks-only branch, run a **shadow ladder** spreadsheet alongside WInS, so the Trading Notes can still show the reserve working through real market moves in Oct–Nov 2026.

## Decision
**Branch 1: ETFs allowed.** Mirror the strategy in WInS:
| Sleeve | WInS weight | Holdings |
|---|---|---|
| Reserve ladder | ~66% | iBonds IBTM, IBTO, IBTP, IBTQ, IBTR (≈ 6.6% each, 2033–37 payments) + an intermediate/long Treasury ETF standing in for the 2038–42 rungs (≈ 33%) |
| Growth: Treasuries | ~7% | Intermediate Treasury ETF |
| Growth: equity core | ~16% | Broad US + international index ETFs |
| Growth: conviction stocks | ~11% | 8–12 D4 stocks, ~1% each |

**Branch 2: stocks only.** WInS = the **equity part of the growth sleeve** (100% of WInS):
- ~60% in large, diversified "core" stocks spread across sectors (a proxy for the index core);
- ~40% in 8–12 D4 conviction stocks.

The IPS and Trading Notes must say explicitly: *"WInS represents the equity portion of Laura's growth sleeve (~27% of her total portfolio); her Treasury reserve is shown in a shadow ladder at [file]."*

**Shadow ladder (both branches, recommended):**
- **To build:** `outputs/laura/shadow_ladder.xlsx`, with ten $50k rungs priced weekly from the Treasury yield curve.
- Each week, record the liability PV and the ladder value. They should move together; that is the hedge working.
- This is also good Trading Notes material.

## What would change our mind
Official WInS rules on minimum holdings or maximum position sizes. Re-weight within the same structure.

## Plain English for Laura
The competition account is a small working model of your plan. If it lets us buy bond funds, it holds your bond ladder and your growth investments in the same proportions as your real portfolio. If it only allows stocks, it shows the stock part of your growth money, and we track your bond ladder separately so you can see it doing its job.

**Sources:**
- [Wharton FAQ](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/faq/)
- [SMApply deliverables](https://wghsinvcomp.smapply.us/res/p/deliverables/)
- [wghs.org.cn rules (unofficial)](https://en.wghs.org.cn/rules)
