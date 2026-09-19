# Decision History, Trading Notes & Competition Journal
**Target**: Team Caplet — Authentic Storytelling & Wharton Deliverables  
**Core Asset**: "How Our Thinking Evolved Over the Competition."

---

## 1. Why the Journal Matters

In the Wharton Global High School Investment Competition, teams that try to write their Final Report from memory in late November consistently produce dry, artificial narratives.

Wharton judges repeatedly highlight that **learning, teamwork, mistake recovery, and strategy evolution** are what distinguish global winning teams from ordinary submissions:
> *"Teams are evaluated on the quality and articulation of their overall investment strategy and competition experience... Storytelling, decision process, learning, teamwork and strategy development matter."*

The `wharton-ic` Journal subsystem captures the live pulse of Team Caplet as decisions occur between September 28 and December 4, 2026.

---

## 2. Supported Event Types

The append-only journal records 17 distinct event categories:

| Category | Typical Trigger | Value in Final Report |
| :--- | :--- | :--- |
| `STRATEGY_PROPOSED` | Candidate strategy generated | Explains starting hypothesis |
| `STRATEGY_CHANGED` | Team pivots investment criteria | Demonstrates dynamic learning |
| `COMPANY_RESEARCHED` | Deep dive on candidate stock | Shows rigorous research breadth |
| `COMPANY_REJECTED` | Negative screen triggers rejection | Proves disciplined selectivity |
| `TRADE_PROPOSED` | PM suggests new allocation | Connects strategy to execution |
| `TRADE_APPROVED` | Student committee signs off | Fulfills required Trading Notes |
| `TRADE_EXECUTED` | Order placed in WInS simulator | Documents real-world execution |
| `POSITION_RESIZED` | Rebalance to maintain weights | Explains drift management |
| `POSITION_SOLD` | Exit criteria or stop-loss hit | Shows risk discipline |
| `THESIS_REVISED` | New quarterly earnings report | Proves ongoing active monitoring |
| `RISK_CONCERN_RAISED` | Macro shock or volatility spike | Highlights risk awareness |
| `CLIENT_FIT_CONCERN` | Questioning asset suitability | Proves client-first mindset |
| `UNEXPECTED_EVENT` | Market liquidity panic | Explains real-world stress response |
| `MISTAKE_IDENTIFIED` | Overlooking a key risk factor | **Intellectual honesty (Judge favorite)** |
| `LESSON_LEARNED` | Retrospective takeaway | The intellectual core of the report |

---

## 3. Official Trading Notes Generation

Wharton requires documentation of trading justifications. Calling `wharton-ic journal trading-notes` automatically compiles a formatted Markdown/CSV table:

```markdown
| Date & Time | Action | Ticker / Target | Strategy Justification | Human Approvers |
| :--- | :--- | :--- | :--- | :--- |
| 2026-10-05 14:30:00 | `TRADE_EXECUTED` | TEST_ALPHA (7.5%) | Installed base software expansion; high ROIC moat. | Ray (Lead PM), Sarah (Risk) |
```

---

## 4. Reconstructing the Competition Journey

Calling `wharton-ic journal evolution` automatically synthesizes the complete competition narrative:
- Dates of major team debates
- Who participated and who disagreed
- Which alternatives were rejected
- What mistakes were uncovered
- How the team adapted and strengthened the strategy

This output feeds directly into Section 7 ("Competition Journey & Strategy Evolution") of the Final Report.

---

## 5. Journal CLI Commands

```bash
# Record an authentic team decision
wharton-ic journal add \
  --type "MISTAKE_IDENTIFIED" \
  --title "European Supplier Concentration Overlooked" \
  --decision "Paused buy order on Alpha Dynamics" \
  --reason "Realized German plant expansion carries regulatory execution risk" \
  --participant "Ray" \
  --participant "Elena" \
  --discussion "Heated debate on whether margin of safety protects against supplier delay" \
  --lesson "Always verify international supply chain concentration before sizing."

# View chronological decision timeline
wharton-ic journal timeline

# Export required Trading Notes deliverable
wharton-ic journal trading-notes

# View curated mistakes and lessons learned
wharton-ic journal lessons

# Reconstruct the authentic competition journey story
wharton-ic journal evolution
```
