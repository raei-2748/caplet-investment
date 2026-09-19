# AI Authorship Compliance & Academic Integrity Firewall
**Target**: Team Caplet — Wharton AI Policy & Fiduciary Ethics  
**Standard**: 100% Genuine Student Authorship.

---

## 1. Wharton Global Youth AI Regulations

The Wharton Global Youth Program maintains strict guidelines regarding artificial intelligence:
- Generative AI may be utilized solely for **brainstorming, scenario exploration, and idea generation**.
- AI-generated prose **MAY NOT** be submitted as the students' own work.
- Any generative AI idea or structure incorporated into a submission must be **properly cited and disclosed**.
- Failure to comply constitutes academic dishonesty, resulting in immediate disqualification.

---

## 2. Content-Block Authorship Tracking

Every paragraph, table, or figure intended for potential inclusion in competition deliverables is assigned an immutable `AuthorshipType`:

```
┌─────────────────────────┬────────────────────────────────────────────────────────┐
│ Authorship Type         │ Status in Final Student Deliverable                    │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ HUMAN_AUTHORED          │ PERMITTED. Genuinely written by student team members.  │
│ HUMAN_EDITED            │ PERMITTED. Substantially rewritten/synthesized by team.│
│ DETERMINISTIC_CODE      │ PERMITTED. Python output (tables, charts, sensitivities│
│ SOURCE_QUOTATION        │ PERMITTED. Formally cited excerpt from filings/case.   │
│ AI_ASSISTED_IDEA        │ PERMITTED WITH CITATION. Brainstormed idea with cite.  │
│ AI_GENERATED            │ PROHIBITED. Raw LLM prose; blocked by firewall.       │
│ UNKNOWN                 │ PROHIBITED. Unclassified text; blocked by firewall.    │
└─────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 3. Physical Directory Segregation

To prevent accidental contamination of student deliverables with raw LLM text:

```
wharton-ic/
├── outputs/
│   └── research_assistance/  <── AI outputs, council transcripts, adversarial debates
│                                 (NEVER compiled into submission PDFs)
│
└── report/
    └── student_authored/     <── Authentic text written directly by student team members
                                  (The exclusive narrative source for final compilation)
```

---

## 4. The AI Authorship Firewall

Before `WhartonReportEngineV2.compile_final_report()` produces any final deliverable, it runs `AIAuthorshipFirewall.assert_compliant()`:
1. **Raw AI Rejection**: If any block is marked `AI_GENERATED`, the compiler immediately halts with `AIAuthorshipViolationError`.
2. **Provenance Audit**: If any block has `UNKNOWN` authorship, compilation is rejected.
3. **Disclosure Audit**: If a block represents an `AI_ASSISTED_IDEA`, it must carry a formal citation referencing the specific model, date, and prompt ID.

---

## 5. Model Citation Standard for Team Caplet Reports

When ideas originated from AI brainstorming, the team includes formal citations in the report appendix:

> **Example Appendix Disclosure:**  
> *"Section 4.2 incorporates scenario sensitivity concepts explored using Anthropic Claude 3.5 Sonnet on October 14, 2026 (Prompt ID: `WHARTON-PROMPT-BEAR-V2`). All calculations, valuations, and final thesis conclusions were independently performed and authored by the student team."*
