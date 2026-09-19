# The Wharton-IC Competition Playbook V2
**Target**: Team Caplet — Season Roadmap (Sept 15 – Dec 4, 2026)  
**Execution**: Strict Alignment with Verified Wharton Milestones.

---

## 1. Master Competition Timeline

```
SEPT 15            SEPT 28             OCT 09             NOV 06             DEC 04
   │                  │                  │                  │                  │
   ├── Materials      ├── WInS Trading   ├── Official       ├── Investment     ├── WInS Simulator
   │   Released       │   Begins         │   Roster Due     │   Policy         │   Closes
   │                  │                  │                  │   Statement Due  │
   └── Private Case   └── Live Trading   └── Finalize Team  └── Submit IPS     └── Final Report &
       Ingested           Sim Starts         Roles              Deliverable        Trading Notes Due
```

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
1. Populate `config/client_mandate.yaml` with verified client facts, citing page and paragraph numbers.
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

### Phase 7: Investment Policy Statement (IPS) Submission (Due November 6, 2026)
1. Export current evidence pack:
   ```bash
   wharton-ic report evidence-pack
   ```
2. Write IPS narrative in `report/student_authored/IPS.md`.
3. Submit official IPS deliverable on SurveyMonkey Apply.

### Phase 8: Final Report & Trading Notes Submission (Due December 4, 2026)
1. WInS trading closes at 4:00 PM EST on December 4.
2. Compile complete Report Evidence Pack:
   ```bash
   wharton-ic report evidence-pack
   ```
3. Export official Trading Notes deliverable:
   ```bash
   wharton-ic journal trading-notes > outputs/report_pack/official_trading_notes.md
   ```
4. Run Judge Review Council to stress-test draft:
   ```bash
   wharton-ic report judge-review
   ```
5. Audit student narrative for AI policy compliance:
   ```bash
   wharton-ic report audit-ai
   ```
6. Format final PDF and submit before the 11:59 PM deadline.
