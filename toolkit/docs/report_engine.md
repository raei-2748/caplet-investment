# Wharton Report Engine V2 & Evidence Pack Architecture
**Target**: Team Caplet — Deliverable Compilation  
**Principle**: Evidence Packs for Students, Not Ghostwritten Prose.

---

## 1. Ethical Report Architecture

A major pitfall in applying AI to academic competitions is having an LLM ghostwrite the submission paper. This violates Wharton's explicit AI rules:
> *"AI-generated work may NOT be submitted as the students' own work... Plagiarism, misuse of AI and academic dishonesty are prohibited."*

`WhartonReportEngineV2` enforces a strict separation:
- **The System's Role**: Assemble verified rules, deterministic calculations, client facts, decision timelines, and chart exhibits into a **Report Evidence Pack**.
- **The Student's Role**: Review the evidence pack, debate the findings, and author the actual narrative text in `report/student_authored/`.

---

## 2. Contents of the Report Evidence Pack

Calling `wharton-ic report evidence-pack` generates `outputs/report_pack/report_evidence_pack.md` and `.json`:

1. **Verified Rules & Deadlines**: Authority-checked dates, deliverables, and team limits.
2. **Client Mandate Summary**: Verified client facts and student-approved strategic assumptions.
3. **Approved Strategy Foundation**: Central philosophy, portfolio roles, screening rules, and exit criteria.
4. **Trading Notes & Execution Log**: Formatted table of all approved trades and justifications.
5. **Decision Timeline**: Chronological log of team meetings, pivots, and debates.
6. **Accounting Quality & Valuation Tables**: Sloan accruals, Altman Z, ROIC/WACC spreads, and DCF sensitivities compiled directly from Python math.
7. **Risk & Stress Diagnostics**: Historical crash replays (2008, 2020, 2022) and Monte Carlo goal probabilities.
8. **Mistakes & Lessons Learned**: Curated list of team reflection items.
9. **Evidence & Citation Appendix**: Full bibliographic citations for all sources and rules.
10. **Audit Alerts**: Prominent warnings if any required approvals, evidence links, or citations are missing.

---

## 3. Team Caplet Report Architecture

Until official private deliverable instructions are released on September 15, the evidence pack organizes materials into the **Team Caplet Report Architecture**:

- **Section 1: Executive Summary & Client Mandate Alignment**
- **Section 2: Investment Strategy & Core Philosophy**
- **Section 3: Portfolio Construction & Role Allocation**
- **Section 4: Fundamental & Forensic Security Selection**
- **Section 5: Intrinsic Valuation & Margin of Safety (DCF / Reverse DCF)**
- **Section 6: Comprehensive Risk Management & Scenario Stress Testing**
- **Section 7: Competition Journey & Strategy Evolution**
- **Section 8: Reflection, Mistakes, and Lessons Learned**
- **Section 9: Appendix: Rule Citations, Evidence Tables & AI Use Disclosure**

**Rule**: This structure is explicitly labeled `TEAM CAPLET REPORT ARCHITECTURE` to avoid confusing team preferences with mandatory Wharton section headings.

---

## 4. Final Compilation & Firewall

```bash
# Assemble the latest Report Evidence Pack
wharton-ic report evidence-pack

# Run the 9-member Judge Review Council on the evidence pack
wharton-ic report judge-review

# Audit student drafts for AI policy compliance
wharton-ic report audit-ai
```
