---
name: ucp-review-validator
description: Review Use Case Point Estimation artifacts for ambiguity, missing NFRs, weak actor boundaries, incompleteness, and estimation readiness. Use when requirements interview output, RUP artifacts, or estimate inputs need a structured issue list before final UCP estimation is accepted.
---

# UCP Review / Validation

Review UCP workflow artifacts and emit a structured issue list.

## Purpose
Catch ambiguity and incompleteness before final estimation is accepted.

## Inputs
This skill can review one or more of:
- intermediate interview YAML
- RUP actor catalog
- RUP use-case specifications
- supplementary specification
- estimation input package

## Output
Return a validation report aligned with:
- `skills/use-case-points-core/schemas/ucp-validation-report.schema.json`

## Required checks
Always assess:
1. Completeness
2. Consistency
3. Classification readiness
4. Estimation readiness

## Common findings to detect
- Missing actor definitions
- Weak or ambiguous actor boundaries
- Missing trigger / preconditions / postconditions
- Main flow too abstract to count transactions reliably
- Alternate or exception flows not separated clearly
- Missing NFRs or unresolved NFR references
- Missing TCF/ECF ratings
- Unclassified actors or use cases

## Severity policy
- `error`: estimation must stop
- `warning`: estimation may proceed with caution
- `info`: note only

## Boundary
- Do not invent missing facts
- Do not fix the artifacts silently
- Surface issues in a structured, reviewable form
