# UCP Estimator Workflow

## Purpose
Convert validated artifacts into a deterministic Use Case Point estimate.

## Required source artifacts
- `rup-actor-catalog.schema.json`
- `rup-usecase-spec.schema.json`
- `rup-supplementary-spec.schema.json`
- `ucp-estimation-input.schema.json`
- `tcf-factors.json`
- `ecf-factors.json`

## Steps
1. Compute UAW from actor classifications and weights
2. Compute UUCW from use-case classifications and transaction counts
3. Compute UUCP = UAW + UUCW
4. Compute TFactor and TCF
5. Compute EFactor and ECF
6. Compute final UCP = UUCP × TCF × ECF
7. If productivity factor is supplied, compute effort separately

## Output shape
Return:
- `uaw_breakdown`
- `uucw_breakdown`
- `uucp`
- `tcf_breakdown`
- `tcf`
- `ecf_breakdown`
- `ecf`
- `ucp`
- `effort_hours` (optional)
- `blocking_findings` (if estimation cannot proceed)
