# IPS: Wharton compliance check (17 Oct 2026)

AI-generated check (Claude Code) of the IPS as it reads in the IPS Report Doc, Version 5 tab, **with all suggestions
accepted** (= `04_exemplar_ips_tna_17Oct.md`, v5 text). Source of every rule: `competition/official/2026_27/2026_WGY_Investment_Policy-FINAL.txt`
(page numbers below), plus the 6 Oct WInS-only email (COMPETITION.md s4) and the Wharton AI policy.

## Hard requirements (failing any one excludes the IPS from semifinal selection, p.3)

| Rule (page) | Result | How checked |
|---|---|---|
| Page 1 = title page, 1 page max (p.3) | PASS | Doc has a page break after the username line |
| Official team name, same as roster (p.3) | PASS | "Caplet" (COMPETITION.md) |
| Names "First Name, Last Initial", same as roster (p.3) | **TEAM CHECK** | Format correct ("Ray W. \| Ahaan D. ..."); surnames are not in the public repo, so two students must check initials against the submitted roster |
| WInS username (p.3) | PASS | the WInS username (kept out of the repo) |
| Pitch 50 words max (p.1) | PASS | 45 by spaces, 47 with hyphenated words split |
| IPS 500 words max (p.1) | PASS | 487 by spaces, 492 split; 490 / 495 even if the heading is counted |
| Pitch + IPS within pages 2-3 (p.3) | PASS | Rendered in Times-metric font, 1" margins, double spacing: ends on page 3 with about 4 lines spare (Letter) and fits on A4 |
| Times New Roman 12 pt (p.3) | PASS | Every live text run in the tab is TNR 12 |
| Double-spaced (p.3) | PASS | Every paragraph line spacing 200% |
| 1" margins all sides (p.3) | PASS | Doc margins 72 pt on all four sides; page size Letter |
| PDF, 5 MB max (p.3) | PASS expected | Test render 33 KB; check the real export |
| No graphics, charts, images, attachments, links, footnotes or formal citations (p.3) | PASS | Scan: no URLs, no citation markers, no source names |

## Content asked for (p.1-2): all present

| The IPS should make clear (p.2) | Where |
|---|---|
| What we are trying to accomplish | Para 1: two objectives, certainty defined |
| Why it suits Laura | Para 2: capacity vs willingness; 2028 income dependence |
| Growth, liquidity, reliability, risk, flexibility | "for growth", "giving liquidity", matched Treasuries, "Beyond a US default...", "financial flexibility" |
| Construction and diversification | Para 3: ladder, floor, "diversified across thousands of companies", rough mix |
| Planned changes as needs approach; reserve composition over time | Para 3 (no shift into bonds, January review rule); para 4 (reserve runs down by 2042 without sales) |
| Protect payments while supporting a responsible contribution | Para 4 (2031 top less shortfall; cap) and para 5 (cover order ends with the floor) |
| Framework, not individual securities or detailed calculations (p.2) | No tickers; two figures only ($21,000 test, 7% assumption) |
| Not expected: final reserve size, projections, final range, co-sponsor text (p.2) | None given (the range is a rule, with one tested odds figure) |

## Other Wharton rules

| Rule | Result |
|---|---|
| Only WInS-listed securities for both deposits (6 Oct email) | PASS: Treasuries, defined-maturity Treasury funds, one global stock fund |
| Strategy is frozen after 6 Nov; Final Report must follow it (p.2) | Every rule is one the Final Report can apply (floor = 2028 remainder, top formula, cap, cover order, review trigger) |
| No WInS promises (trading freezes 6 Nov) | PASS: no WInS action promised |
| WInS gains not used in projections (case) | PASS |
| **AI policy: AI-generated work may not be submitted as the students' own; the IPS cannot carry a citation** | **OPEN, and the biggest risk.** This text is an AI exemplar. The submitted IPS must be written by the team in its own words; log the exemplar in the AI-use record for the Final Report's Works Cited |

## Before exporting (Thu 5 Nov Sydney at the latest)
1. Write the team's own version; then **reject every [AI] suggestion** so no AI text or label is left.
2. Resolve all suggestions and comments, and export from a **new one-tab document**: whether a PDF exported from the
   15-tab Doc carries other tabs or suggestion marks is UNVERIFIED.
3. Open the PDF: 3 pages, TNR 12 embedded, double spacing, title page alone on page 1.
4. Two students check the title page against the roster, letter by letter.
5. Re-count words (spaces and hyphen-split) on the final text.
