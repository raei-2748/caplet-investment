# START HERE, TEAM CAPLET!
## Student Team Handbook & Operational Guide
**Competition**: 2026–2027 Wharton Global High School Investment Competition  
**Team**: Team Caplet  
**System**: `wharton-ic` Institutional Decision-Support Operating System

---

## Welcome to Team Caplet!

This document is your team's single source of truth. It explains how our operating system works, how we make decisions, how we use AI ethically, and how we will run our campaign from Day 1 to the Final Report.

---

## 1. What This System Is (and What It Is NOT)

### What It IS:
- An **institutional-grade research, governance, and audit system** that gives our high school team the analytical rigor of an institutional investment committee.
- A **decision journal** that records our team discussions, mistakes, pivots, and lessons across the 10-week competition so we can write an unforgettable Final Report in December.
- An **adversarial review council** that attacks our stock ideas and strategies to find flaws before judges do.
- A **compiler of verified facts and numbers** that prevents any hallucinated or fabricated data from ever entering our competition submissions.

### What It Is NOT:
- It is **NOT** a magical algorithmic trading bot that tries to game short-term stock prices.
- It is **NOT** a tool that ghostwrites our final report. (That violates Wharton rules and causes immediate disqualification).
- It is **NOT** allowed to make investment decisions for us. **Every single strategy choice, stock purchase, and report sentence belongs to us.**

---

## 2. Core Competition Reality: How Wharton Winners Are Judged

Many beginner teams make the fatal mistake of thinking the winner is whoever makes the most money on the WInS simulator.

**That is completely wrong.** Official Wharton rules state:
> *"Portfolio performance does not determine the winner. WInS return performance has little to do with the final outcome. Teams are evaluated on the quality and articulation of their overall investment strategy, alignment with client goals, and competition experience."*

Judges look for:
1. **Did you genuinely serve the client?** (Not your own personal stock interests).
2. **Is your strategy coherent, explainable, and intellectually defensible?**
3. **Did you learn from your mistakes?** (Teams that pretend they had zero losses or made no errors look naive).
4. **Is your research grounded in primary evidence?** (Audited 10-K filings, cash flows, economic moats).
5. **Can you explain it without burying the judges in technical jargon?**

---

## 3. What We Do Before September 28 (Pre-Kickoff Phase)

1. **Practice with Synthetic Data**:
   The system currently runs in **DEMO** mode using synthetic test companies (`TEST_ALPHA`, `TEST_BETA`, `TEST_GAMMA`). Practice running screens, running council debates, and signing off on decisions.
2. **Review Past Winner Case Studies**:
   Read `docs/benchmark_against_previous_teams.md` to see what separated past finalists from the rest of the world.
3. **Master the Valuation Logic**:
   Read `docs/methodology.md`. Understand why **Reverse DCF** is our primary secret weapon during judge Q&A (it tells us what the market is pricing in, rather than guessing future revenue).

---

## 4. What We Do Once Official Materials Are Released (Sept 15, 2026)

On September 15, Wharton will release the private competition package on SurveyMonkey Apply. Here is our exact sequence:

```bash
# Step 1: Ingest official files into the repository
wharton-ic ingest-official /path/to/official_client_case.pdf --type client_case
wharton-ic ingest-official /path/to/approved_securities.csv --type approved_securities_list

# Step 2: Extract client facts into config/client_mandate.yaml and audit
wharton-ic client audit

# Step 3: Approve the client mandate (Must be signed by team members)
wharton-ic client approve --signer "Your Name (Lead PM)" --notes "Audited against official case study PDF."

# Step 4: Run the Strategy Council (Architects A, B, and C)
wharton-ic strategy run-council

# Step 5: Team discussion meeting! Review candidate strategies, debate them, and approve:
wharton-ic strategy approve \
  --id "STRAT-A-QUALITY-MOAT" \
  --signer "Student 1" \
  --signer "Student 2" \
  --rationale "Selected for superior Q&A defensibility and quality compounding."
```

---

## 5. How Our AI Council Works (and Why It Cannot Make Decisions)

When we evaluate a stock, our system spins up a council of specialized AI personas:
- **Fundamental Analyst**: Checks return on capital (ROIC) vs cost of capital (WACC).
- **Valuation Analyst**: Builds a 3-stage DCF and tests reverse DCF implied growth.
- **Bull Researcher**: Presents the strongest secular compounding argument.
- **Bear Researcher**: Acts as a harsh skeptic, presenting the structural risks and thesis-breakers.
- **Client Steward**: Ensures the stock fits our client's horizon and ethical screens.
- **Evidence Auditor**: Validates that all numbers cited match our Python math.
- **Committee Chair**: Synthesizes the debate into a recommendation (`SUPPORT` / `REJECT`).

**CRITICAL RULE**: The Committee Chair can only **recommend**. A real student team member must execute the governance command:
```bash
wharton-ic review TICKER --approve --signer "Your Name" --notes "Approved following committee debate."
```
Without this command, no trade can be approved!

---

## 6. How Trading Decisions & Trading Notes Are Logged

Whenever we place a trade or adjust our portfolio on the WInS simulator, we immediately log it:

```bash
wharton-ic journal add \
  --type "TRADE_EXECUTED" \
  --title "Bought TEST_ALPHA (7.5% weight)" \
  --decision "Entered position on WInS" \
  --reason "Core Compounder role; 18.5% ROIC with strong economic moat" \
  --participant "Ray" \
  --participant "Sarah" \
  --discussion "Agreed to size at 7.5% to respect single-stock risk bounds."
```

Whenever we identify a mistake or have a team disagreement:
```bash
wharton-ic journal add \
  --type "MISTAKE_IDENTIFIED" \
  --title "Supplier Concentration Concern" \
  --decision "Paused position increase" \
  --reason "Realized 30% of revenue comes from a single European buyer" \
  --participant "Team" \
  --lesson "Always inspect customer concentration footnotes in 10-K before increasing position."
```

At the end of the competition, running `wharton-ic journal trading-notes` produces our exact required Trading Notes deliverable!

---

## 7. How the Final Report Is Assembled

In late November, we do **NOT** ask an AI to write our report. Instead:

1. We run the Report Engine:
   ```bash
   wharton-ic report evidence-pack
   ```
   This generates `outputs/report_pack/report_evidence_pack.md`, containing all our verified numbers, audited tables, charts, trading notes, and our complete decision timeline.
2. We author the chapters in `report/student_authored/` using our own words, thoughts, and reflections.
3. We run the Judge Review Council to critique our draft:
   ```bash
   wharton-ic report judge-review
   ```
   This gives us adversarial feedback from 9 perspectives (Client Alignment, Simplicity, Storytelling, Skeptical Judge).
4. We audit our text through the AI Authorship Firewall:
   ```bash
   wharton-ic report audit-ai
   ```
   This proves that 100% of our narrative is authentic student work.

---

## 8. Master Command Cheat Sheet

| Task | Command |
| :--- | :--- |
| **Check Rule Registry Status** | `wharton-ic rules status` |
| **List Verified Rules** | `wharton-ic rules list` |
| **Ingest Official File** | `wharton-ic ingest-official <file_path> --type <type>` |
| **Show Client Mandate** | `wharton-ic client show` |
| **Audit Client Mandate** | `wharton-ic client audit` |
| **Approve Client Mandate** | `wharton-ic client approve --signer "<name>" --notes "<notes>"` |
| **Run Strategy Council** | `wharton-ic strategy run-council` |
| **Approve Strategy** | `wharton-ic strategy approve --id "<id>" --signer "<s1>" --signer "<s2>" --rationale "<text>"` |
| **Show Active Strategy** | `wharton-ic strategy show` |
| **Screen Stocks** | `wharton-ic screen --top-n 10` |
| **Value a Company** | `wharton-ic value <TICKER> --wacc 0.08 --growth 0.03` |
| **Run Security Council** | `wharton-ic propose <TICKER>` |
| **Approve Security Trade** | `wharton-ic review <TICKER> --approve --signer "<name>" --notes "<notes>"` |
| **Add Journal Event** | `wharton-ic journal add --type <TYPE> --title "<title>" ...` |
| **View Trading Notes** | `wharton-ic journal trading-notes` |
| **View Decision Timeline** | `wharton-ic journal timeline` |
| **Reconstruct Story** | `wharton-ic journal evolution` |
| **Compile Evidence Pack** | `wharton-ic report evidence-pack` |
| **Run Judge Review** | `wharton-ic report judge-review` |
| **Audit AI Authorship** | `wharton-ic report audit-ai` |

---

## 9. Let's Win Wharton!

You now have the most sophisticated, ethical, and auditable operating system in the entire Wharton competition. Focus on client fit, master your company moats, be honest about mistakes, and enjoy the journey as a team!
