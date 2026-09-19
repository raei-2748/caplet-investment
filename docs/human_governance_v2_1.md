# Human Decision Governance and Team Roster (Caplet V2.1)

---

## 1. The Principle of Student Sovereignty

In the Wharton Investment Competition, AI is an analytical advisor—never a decision-maker.

Caplet V2.1 enforces three strict governance invariants:
1. **Registered Student Identities**: All human approvals must reference active, registered student members from `TeamRoster` (`src/wharton_ic/governance/roster.py`).
2. **Distinct Multi-Signature Threshold**: Strategic decisions (Client Mandate, Strategy Selection, Portfolio Execution) require at least two distinct registered student signatures. Duplicate names or single individuals signing twice fail validation.
3. **No Fabricated Deliberation Records**: If students choose not to record a disagreement, discussion note, or retrospective lesson, the system stores `NOT_RECORDED`. It **never** generates plausible synthetic quotes or canned deliberations.

---

## 2. Team Roster Architecture

```json
[
  {
    "member_id": "CAPLET-01",
    "display_name": "Lead Portfolio Manager",
    "role": "Portfolio Manager",
    "active": true,
    "source": "WHARTON_OFFICIAL_REGISTRATION",
    "eligibility_status": "VERIFIED_HIGH_SCHOOL_STUDENT"
  },
  {
    "member_id": "CAPLET-02",
    "display_name": "Chief Risk Officer",
    "role": "Risk Lead",
    "active": true,
    "source": "WHARTON_OFFICIAL_REGISTRATION",
    "eligibility_status": "VERIFIED_HIGH_SCHOOL_STUDENT"
  }
]
```

---

## 3. Human Approval Gates

1. **Client Mandate Approval Gate**:
   ```bash
   wharton-ic client approve --signer "CAPLET-01" --signer "CAPLET-02" --notes "Reviewed against official PDF"
   ```
2. **Strategy Selection Gate**:
   ```bash
   wharton-ic strategy approve --id "STRAT-QUALITY-MOAT" --signer "CAPLET-01" --signer "CAPLET-02" --rationale "Fits client horizon"
   ```
3. **Security Trade Approval Gate**:
   ```bash
   wharton-ic review TEST_ALPHA --approve --signer "CAPLET-01" --signer "CAPLET-02" --notes "Council recommendation accepted"
   ```
