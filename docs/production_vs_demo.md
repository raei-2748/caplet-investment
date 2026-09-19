# Production vs. Demo Modes: Isolation & Fail-Closed Protocols
**Target**: Team Caplet — Operational Safety  
**Principle**: Fictional Data Never Enters Competition Deliverables.

---

## 1. The Necessity of Mode Isolation

During early software development, engineering teams frequently rely on:
- Synthetic client profiles (e.g., Dr. Elena Vance)
- Mock stocks and toy models
- Deterministic mock LLM responses for offline unit tests

If these synthetic prototypes are mixed with actual competition operations, students risk submitting fictional research, fake client goals, or ungrounded mock analysis to Wharton judges.

`wharton-ic` solves this by strictly separating execution into two mutually exclusive modes: **DEMO** and **PRODUCTION**.

---

## 2. Mode Capabilities Matrix

| Dimension | DEMO Mode (`WHARTON_MODE=demo`) | PRODUCTION Mode (`WHARTON_MODE=production`) |
| :--- | :--- | :--- |
| **Client Mandate** | Permitted to use prototype `demo_client_mandate.yaml` | **FAILS CLOSED** if official 2026 client case is missing |
| **Security Universe**| Permitted to use synthetic fixtures (`TEST_ALPHA`, etc.) | Requires official approved Wharton stock universe |
| **LLM Reasoning** | Deterministic mock generator active if no API keys | **FAILS CLOSED** (`CouncilPartialError`) if API keys missing |
| **Rules Registry** | Explores hypothetical constraints | Strict enforcement of verified 2026-27 rules |
| **Output Paths** | Saves to `decisions/demo/`, `outputs/demo/` | Saves to `decisions/`, `outputs/` |
| **Submission Export**| Banners prominently marked **DEMONSTRATION ONLY** | Clean, verified student deliverable packages |

---

## 3. Physical Directory Segregation

All demonstration assets generated during system testing are isolated in dedicated demo directories:

```
wharton-ic/
├── decisions/
│   ├── demo/                  <── SYNTHETIC DATA ONLY (Fictional MSFT prototype)
│   ├── strategy/              <── Authentic student strategy decisions
│   └── journal/               <── Authentic competition decision logs
│
├── outputs/
│   ├── demo/                  <── Prototyping charts and mock report packs
│   ├── report_pack/           <── Audited evidence pack for current competition
│   └── research_assistance/  <── Live AI debate logs and prompt records
│
└── data/
    ├── demo/                  <── Synthetic price and fundamental fixtures
    ├── point_in_time/         <── Production point-in-time stores
    └── cache/                 <── Verified SEC and market caches
```

Every file in `decisions/demo/`, `outputs/demo/`, and `data/demo/` contains the explicit notice:
```text
# DEMONSTRATION ONLY - SYNTHETIC DATA
## NOT COMPETITION RESEARCH - NOT FOR SUBMISSION
```

---

## 4. Switching Modes

By default, the repository runs in `DEMO` mode to facilitate safe local testing and development.

To engage **PRODUCTION** mode:
```bash
# Enable production mode in terminal environment
export WHARTON_MODE=production

# Verify production readiness
wharton-ic rules status
```

In production mode:
- If `config/wharton_private_2026_27.yaml` is still awaiting September 15 materials, any attempt to run a full portfolio optimization halts with:
  `ProductionMissingMaterialError: Official private competition materials for 2026-2027 have not been ingested.`
- If an LLM provider is requested without an active API key, the system halts with:
  `CouncilPartialError: ANTHROPIC_API_KEY is not set. Cannot complete council deliberation in production mode.`
