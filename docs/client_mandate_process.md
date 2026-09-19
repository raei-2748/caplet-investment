# Client Mandate Extraction, Audit & Governance Process
**Target**: Team Caplet — Wharton Global High School Investment Competition 2026–2027  
**Core Standard**: Fiduciary Alignment & Fact Lineage.

---

## 1. Hierarchy: Wharton Rules → Client Mandate → Strategy

The client case study sits immediately below official Wharton competition rules. A portfolio that produces exceptional simulated returns but violates the client's risk profile or ethical exclusions is an automatic losing strategy in the eyes of Wharton judges.

---

## 2. The Three Mandate Tiers

Every item in the client mandate is categorized into one of three strict tiers:

```
+-------------------------------------------------------------------------------+
| 1. CLIENT_FACT                                                                |
|    Directly quoted or cited from the official case study PDF.                  |
|    Must have an exact page and paragraph reference.                           |
+-------------------------------------------------------------------------------+
                                      │
                                      ▼
+-------------------------------------------------------------------------------+
| 2. TEAM_INTERPRETATION                                                        |
|    Logical deductions authored by the student team to resolve ambiguity.      |
|    Must be explicitly labeled as student interpretation, never client fact.   |
+-------------------------------------------------------------------------------+
                                      │
                                      ▼
+-------------------------------------------------------------------------------+
| 3. STRATEGIC_ASSUMPTION                                                       |
|    Pragmatic choices made by the team where the case study is silent.         |
|    Must be defended in the Investment Policy Statement (IPS).                 |
+-------------------------------------------------------------------------------+
```

**Non-Negotiable Rule**: No AI agent or automated script may convert a `TEAM_INTERPRETATION` or `STRATEGIC_ASSUMPTION` into a `CLIENT_FACT`.

---

## 3. Client Mandate Schema

The `ClientMandate` model (`src/wharton_ic/client/models.py`) captures:
- **Financial Objectives**: Return target, inflation benchmark, endowment growth.
- **Non-Financial Objectives**: Sustainability themes, community education, legacy.
- **Horizon & Liquidity**: Investment window and periodic cash distribution needs.
- **Risk Capacity vs. Tolerance**: Objective ability to absorb losses vs. emotional comfort with drawdowns.
- **Ethical Preferences & Exclusions**: Hard negative screens (tobacco, defense, fossil fuels).
- **Dialectical Tensions**: Documented conflicts between objectives (e.g., high return aspirations vs. capital preservation).
- **Human Approval Metadata**: Mandatory student officer signatures and rationale.

---

## 4. The Mandate Audit Engine

Before any strategy candidate can be generated, `ClientMandateAuditor` audits the mandate:
1. **Source Lineage Check**: Flags any item labeled `CLIENT_FACT` that lacks an official page/paragraph citation.
2. **Dialectical Tension Detection**: Identifies incompatible requirements (e.g., aggressive return goals with strict capital preservation).
3. **Ambiguity Inventory**: Assembles all uncertainties that require student team assumptions.
4. **Governance Verification**: Verifies that human approval has been recorded in the ledger.

---

## 5. Student Workflow & CLI Commands

```bash
# Display the active client mandate
wharton-ic client show

# Run the provenance and tension audit
wharton-ic client audit

# Approve the client mandate (Mandatory before running Strategy Council)
wharton-ic client approve --signer "Ray (Lead PM)" --notes "Audited against official case study pages 1-4; verified financial and ethical constraints."
```
