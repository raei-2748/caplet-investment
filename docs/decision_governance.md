# Decision Governance & Human Approval Gates
**Target**: Team Caplet — Fiduciary Accountability  
**Rule**: No Autonomous AI Trade Execution.

---

## 1. Governance Principles

Wharton competition guidelines state:
> *"Students are responsible for developing and implementing the investment strategy, conducting research, analyzing data, and placing trades... Student work must genuinely belong to the students."*

In `wharton-ic`, AI agents operate strictly as **research assistants and adversarial critics**. Every capital allocation, strategy adoption, thesis revision, and simulator order must pass through a formal human governance gate.

---

## 2. The Three Governance Gates

```
+-------------------------------------------------------------------------------+
| GATE 1: CLIENT MANDATE SIGN-OFF                                               |
| Pre-requisite for running Strategy Council.                                  |
| Requires verification of client facts and dialectical tensions.              |
+-------------------------------------------------------------------------------+
                                      │
                                      ▼
+-------------------------------------------------------------------------------+
| GATE 2: STRATEGY SELECTION SIGN-OFF                                           |
| Pre-requisite for security research and universe screening.                  |
| Requires minimum 2 student signatures and documented selection rationale.    |
+-------------------------------------------------------------------------------+
                                      │
                                      ▼
+-------------------------------------------------------------------------------+
| GATE 3: SECURITY & TRADE EXECUTION SIGN-OFF                                   |
| Pre-requisite for executing trades on WInS simulator.                         |
| Requires student PM review of council recommendation and thesis falsifiers.   |
+-------------------------------------------------------------------------------+
```

---

## 3. The 16 Immutable Decision Artifacts

When a security is proposed, `wharton-ic` generates a dossier of 16 structured artifacts in `decisions/`:

1. `00_metadata.json` — Unique decision ID, timestamp, target allocation, and governance status.
2. `01_client_fit.json` — Exact clauses from the client mandate satisfied by this security.
3. `02_sources.json` — SHA-256 hashes of primary SEC 10-K filings and price matrices used.
4. `03_fundamentals.json` — Deterministic ROIC, Sloan accruals, Altman Z, and operating margins.
5. `04_valuation.json` — DCF fair value, WACC components, and reverse DCF implied growth.
6. `05_quant.json` — Factor Z-scores, Beta, and pairwise correlation metrics.
7. `06_macro.md` — Scenario exposure to inflation, interest rates, and commodity regimes.
8. `07_independent_model_A.md` — Blind qualitative analysis from Model A.
9. `08_independent_model_B.md` — Blind qualitative analysis from Model B.
10. `09_bull_case.md` — Adversarial secular growth and pricing power thesis.
11. `10_bear_case.md` — Adversarial structural risks and exit conditions.
12. `11_risk.json` — Marginal Volatility, Marginal CVaR, and position sizing bounds.
13. `12_portfolio_impact.json` — Before-and-after sector concentration and diversification delta.
14. `13_evidence_audit.json` — Forensic audit of numbers cited against deterministic calculations.
15. `14_committee_verdict.json` — Committee Chair synthesis and recommendation (`SUPPORT` / `REJECT`).
16. `15_human_decision.md` — **The Governance Gate**: Signed student verdict, rationale, and target weight.

### The Human Approval Gate (`15_human_decision.md`)
The WInS trade execution interface checks `15_human_decision.md`. If `human_status != "APPROVED"` or the student signature is missing, the system throws `HumanApprovalRequiredError` and blocks order placement.

---

## 4. CLI Governance Commands

```bash
# Review security decision dossier
wharton-ic review TEST_ALPHA

# Record human investment committee sign-off
wharton-ic review TEST_ALPHA --approve \
  --signer "Ray (Lead PM)" \
  --notes "Unanimous student committee sign-off following council debate. Approved at 7.5% weight."
```
