# UCP Artifact Validation Rules

## Purpose
Define deterministic validation checks for interview and RUP artifacts before estimation.

## Validation categories
1. Completeness
2. Consistency
3. Classification readiness
4. Estimation readiness

## Core checks
### Completeness
- Missing actor IDs or names
- Missing use-case trigger
- Missing preconditions or postconditions
- Empty main success scenario
- Missing non-functional requirements when referenced

### Consistency
- Actor IDs referenced by use cases must exist in actor catalog
- NFR references must resolve to supplementary specification entries
- Use-case IDs must be unique
- Business-goal references must resolve when present

### Classification readiness
- Actor descriptions must be sufficient for simple/average/complex classification
- Transaction count must be derivable or explicitly flagged
- Use-case classification must follow configured thresholds

### Estimation readiness
- TCF and ECF ratings must be complete
- No unclassified actors/use cases may proceed to final estimation
- Any ambiguity flags must be surfaced to human review

## Severity levels
- `error`: estimation must stop
- `warning`: estimation may proceed with caution and explicit note
- `info`: helpful note only
