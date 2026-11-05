# Third-party skills (added 5 Nov 2026, Ray's request)

Three community skills were copied in unchanged from public GitHub repos (all MIT; each folder keeps its LICENSE).
None of them comes from Wharton or the CFA Institute. Use them as checklists and editors, never as sources to cite.

| Skill | Source (commit) | Use for | Notes |
|---|---|---|---|
| `avoid-ai-writing` | github.com/conorbronsdon/avoid-ai-writing (30971f1, v3.38.0) | Editing out AI writing patterns in drafts (`detect` mode to flag only) | An editing aid, not a verdict. It does not replace the GPTZero check (BIBLE Book 10), and Keel still never judges its own AI-likeness (INSTRUCTIONS I53/I56). Only the files SKILL.md needs were copied: `references/patterns.md`, four scripts, the detector and examples (needs Node 18+). Its scripts were not run here. |
| `investment-policy` | github.com/joellewis/finance_skills, `plugins/wealth-management/skills/investment-policy` (5c498ea) | Checking the IPS and Final Report against a standard IPS outline: required return, ability vs willingness, the five constraints, review schedule | Its cross-references name skills that are not installed; ignore them. Wharton's own IPS questions (`keel/WHARTON_WORD.md`) rank above it. |
| `asset-liability-management` | github.com/daemon-blockint-tech/agentic-enteprises-skill (526df1c) | Explaining the ladder as liability matching: duration, DV01, immunization, reinvestment risk, stress tests | Written for insurers, pensions and banks, so skip the ALCO and capital material. Numbers still come from the repo's own scripts. |

To update one, re-copy its folder from the source repo and change the commit here.
