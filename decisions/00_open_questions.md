# 00 — Open Questions (humans must answer; the model runs both scenarios meanwhile)

| # | Question | Why it matters | Where to check | Current assumption |
|---|---|---|---|---|
| Q1 | WInS starting cash for 2026–27: $100k or $500k? | Position sizing in Trading Notes; scale of example trades | WInS dashboard / SMApply "trading requirements" Box doc | UNVERIFIED — plan in % weights; `config/competition.yaml` says $100k, 2025–26 was $500k |
| Q2 | Can WInS trade ETFs (incl. bond ETFs such as iBonds IBTO–IBTR, SHY, IEF, GOVT)? | Decides whether the Treasury reserve can be *shown* in WInS or only on paper (D7) | Approved securities list on SMApply | UNVERIFIED — D7 has a plan for both |
| Q3 | Approved securities list, min price, max position %, min number of holdings, trade limits | Growth-sleeve construction (D4) | SMApply trading requirements | UNVERIFIED |
| Q4 | Trading Notes Analysis format (length, how many notes, required fields) | Stage 5 template | SMApply Box doc (due 23 Oct) | UNVERIFIED — template kept generic |
| Q5 | IPS length/format limits | IPS outline density | SMApply Box doc (due 6 Nov) | UNVERIFIED |
| Q6 | Are the $50k payments USD? | Currency risk framing | Case PDF (states "$50,000"; residency in Taiwan) | Assume USD, as the case prices everything in $ |
| Q7 | Team: who owns which decision memo (D1–D8)? | Competition Experience criterion rewards clear roles | Team meeting | — |
| Q8 | Student committee sign-off on `config/client_mandate.yaml` transcription (`human_approved: true`) | Production-mode gate in `src/wharton_ic/core/config.py` (now fails closed until `human_approved: true`). Note: `tests/governance` test 6 expects the gate to be closed, so update that test when you approve | Team review | false |
