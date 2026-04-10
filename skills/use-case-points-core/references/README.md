# Deterministic UCP Tooling Layer

This directory is the thin deterministic backend for the Use Case Point Estimation workflow.

## Intended functions
- `classify_actor_complexity()`
- `classify_usecase_complexity()`
- `count_ucp_transactions()`
- `validate_rup_artifact()`
- `compute_ucp()`
- `generate_traceability_matrix()`

## Design boundary
- Skills gather and transform information.
- This tooling layer performs deterministic classification, validation, counting, and estimation.
- Final math must never be improvised by an LLM.
