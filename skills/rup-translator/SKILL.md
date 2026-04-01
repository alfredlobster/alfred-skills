---
name: rup-translator
description: Transform normalized requirements interview output into RUP-compliant actor, use-case, and supplementary specification artifacts for Use Case Point Estimation. Use when the intermediate YAML has already been captured and validated, and you need formal artifacts without conducting further elicitation or performing estimation.
---

# RUP Translator

Transform normalized interview output into formal RUP artifacts.

## Inputs
- One intermediate YAML document that validates against:
  - `schemas/use-case-points/requirements-interview.schema.json`

## Outputs
Produce only these V1 artifacts:
1. Actor catalog
2. Use-case specifications
3. Supplementary specification

These must validate against the corresponding schemas in `schemas/use-case-points/`.

## Boundaries
- Do not interview stakeholders
- Do not estimate
- Do not invent missing facts; surface them as gaps or open questions
- Keep artifact generation faithful to the intermediate YAML

## Transformation rules
- Convert actor entries into actor catalog rows
- Convert use-case candidates into RUP-style use-case specifications
- Move NFRs into the supplementary specification
- Preserve IDs and references consistently across artifacts
