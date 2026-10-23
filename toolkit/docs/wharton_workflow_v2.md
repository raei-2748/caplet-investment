# The Wharton-IC Competition Playbook V2
**Target**: Team Caplet — Season Roadmap (Sept 15 – Dec 4, 2026)  
> **Update 2026-10-14:** timeline and Phase 7-8 corrected to the official 2026-27 dates. WInS facts: $300,000 virtual cash; $25 per stock/ETF trade, $10 per Treasury bond trade; max 200 trades; stocks, any ETF on WInS and US Treasury bonds on WInS are allowed; no required sector count or allocation. There is no official approved-securities CSV to ingest. See COMPETITION.md.

**Execution**: Strict Alignment with Verified Wharton Milestones.

---

## 1. Master Competition Timeline

```
SEPT 15      SEPT 28        OCT 09       OCT 23         NOV 06              NOV 09          DEC 04
   │            │              │            │              │                   │               │
   ├ Materials  ├ Official     ├ Roster     ├ Trading      ├ IPS due;          ├ Final Report  ├ Final Report +
   │ released   │ trading      │ due        │ Notes        │ TRADING ENDS,     │ instructions  │ school
   │ (practice  │ begins       │ (locked)   │ Analysis due │ WInS portfolio    │ released      │ documentation
   │ 15-25 Sep) │              │            │              │ frozen            │               │ letter due
```
All deadlines 5:00 pm ET. WInS does not trade after 6 Nov; nothing about WInS or Trading Notes is due on 4 Dec.

---

## 2. Phase-by-Phase Execution Protocol

### Phase 1: Materials Ingestion (September 15 – 18, 2026)
1. **Download Official Packet**: Log into SurveyMonkey Apply and download:
   - Official Client Case Study PDF
   - Approved Securities List CSV / Excel
   - Deliverable Instructions & Rubrics
2. **Ingest into Repository**:
   ```bash
   wharton-ic ingest-official /path/to/official_client_case.pdf --type client_case
   wharton-ic ingest-official /path/to/approved_securities.csv --type approved_securities_list
   ```
3. **Verify Rules**:
   ```bash
   wharton-ic rules list
   wharton-ic rules verify RULE_ID --by "Student Name"
   ```

### Phase 2: Client Mandate Extraction & Approval (September 18 – 21, 2026)
1. Populate `toolkit/config/client_mandate.yaml` with verified client facts, citing page and paragraph numbers.
2. Run audit:
   ```bash
   wharton-ic client audit
   ```
3. Formally approve mandate in human gate:
   ```bash
   wharton-ic client approve --signer "Lead PM" --notes "Audited against official case PDF."
   ```

### Phase 3: Strategy Council & Human Selection (September 21 – 25, 2026)
1. Run independent Strategy Architects and Adversarial Red Team:
   ```bash
   wharton-ic strategy run-council
   ```
2. Hold team deliberation meeting to review candidates A, B, and C.
3. Sign off on official strategy:
   ```bash
   wharton-ic strategy approve \
     --id "STRAT-A-QUALITY-MOAT" \
     --signer "Student 1" \
     --signer "Student 2" \
     --rationale "Chosen for Q&A defensibility and quality compounding."
   ```

### Phase 4: Trading Simulator Kickoff (September 28 – October 9, 2026)
1. Refresh universe price and financial caches:
   ```bash
   wharton-ic update-data
   ```
2. Screen approved securities through strategy filters:
   ```bash
   wharton-ic screen --top-n 15
   ```
3. Log team formation and initial screen in journal:
   ```bash
   wharton-ic journal add --type "COMPANY_SHORTLISTED" --title "Initial 15 Shortlist" ...
   ```

### Phase 5: Valuation, Council Review & Trade Execution (October – November 2026)
1. Perform 3-stage DCF, WACC, and reverse DCF for candidate securities:
   ```bash
   wharton-ic value TICKER --wacc 0.08 --growth 0.03
   ```
2. Run adversarial debate and evidence verification:
   ```bash
   wharton-ic propose TICKER
   ```
3. Execute human governance gate:
   ```bash
   wharton-ic review TICKER --approve --signer "Lead PM" --notes "Approved following council debate."
   ```
4. Enter trade on WInS simulator and log Trading Note:
   ```bash
   wharton-ic journal add --type "TRADE_EXECUTED" --title "TICKER Buy Order" ...
   ```

### Phase 6: Mid-Competition Monitoring & Thesis Audits (Ongoing)
1. Track portfolio drift and sector allocations:
   ```bash
   wharton-ic monitor --drift-threshold 0.03
   ```
2. If unexpected market events or company earnings surprise, log mistakes and adjustments:
   ```bash
   wharton-ic journal add --type "MISTAKE_IDENTIFIED" --title "..." ...
   ```

### Phase 7: Investment Policy Statement (IPS) Submission (Due November 6, 2026, 5:00 pm ET)
1. Export current evidence pack:
   ```bash
   wharton-ic report evidence-pack
   ```
2. Write IPS narrative in `report/student_authored/IPS.md`.
3. Submit official IPS deliverable on SurveyMonkey Apply.
4. **Trading ends at the IPS deadline and the WInS portfolio is frozen the same day.** Any last trades must be placed before 6 Nov, 5:00 pm ET.

(The Trading Notes Analysis, three notes matching executed WInS trades, was due separately on 23 Oct 2026.)

### Phase 8: Final Report Submission (Due December 4, 2026, 5:00 pm ET)
1. Final Report instructions are released 9 Nov 2026; follow them over anything below.
2. No trading happens in this phase: the WInS portfolio has been frozen since 6 Nov.
3. Compile complete Report Evidence Pack:
   ```bash
   wharton-ic report evidence-pack
   ```
4. Run Judge Review Council to stress-test draft:
   ```bash
   wharton-ic report judge-review
   ```
5. Audit student narrative for AI policy compliance:
   ```bash
   wharton-ic report audit-ai
   ```
6. Submit the Final Report PDF and the official school documentation letter (separate file) on SurveyMonkey Apply before 5:00 pm ET on 4 Dec.
