# Council State and Checkpointing (Caplet V2.1)

Adapted from `TauricResearch/TradingAgents`, `wharton-ic` implements typed state tracking and deterministic checkpointing.

---

## 1. Typed Shared State (`CouncilRunState`)

The council run state is an explicit, serializable Pydantic model (`src/wharton_ic/orchestration/state.py`):
- `run_id`: Unique identifier for the multi-agent deliberation.
- `council_type`: `"STRATEGY"`, `"SECURITY"`, or `"REVIEW"`.
- `wharton_rules_snapshot_id`: Ensures deliberations are tied to an immutable ruleset snapshot.
- `client_mandate_version`: Tracks the specific client profile and constraints evaluated.
- `input_artifact_hashes`: SHA-256 hashes of all inputs; used for checkpoint invalidation.
- `completed_stages`: Ordered list of finished workflow stages.
- `agent_outputs`: Structured dictionary of outputs by stage and agent name.
- `disagreements`: Preserved dialectical tensions between agents.
- `uncertainties`: Explicitly surfaced unknown facts or unprovable assumptions.
- `failures`: Detailed trace of any provider outages or node errors.
- `human_decisions`: Cryptographically auditable record of human approvals.

---

## 2. Checkpoint Invalidation Protocol

A long multi-agent council run can be interrupted by network timeouts, API rate limits, or human review pauses.

To prevent re-running completed analytical stages, `CouncilCheckpointer` calculates a deterministic run signature:
$$\text{sig} = \text{SHA-256}(\text{run\_id} \,\|\, \text{input\_hashes} \,\|\, \text{prompt\_versions} \,\|\, \text{model\_config})[:16]$$

### Invalidation Rules:
1. **Resume**: If `run_id`, `input_hashes`, and `prompt_versions` match an existing checkpoint, the graph loads completed stage outputs and continues from the first uncompleted node.
2. **Invalidation**: If student team members edit the client mandate, change Wharton rule files, or update prompt templates, `input_hashes` change. The signature changes, invalidating prior downstream checkpoints and forcing a fresh run.
