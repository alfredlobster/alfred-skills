---
name: ucp-estimator
description: Produce deterministic Use Case Point estimates from validated RUP artifacts and configured technical/environmental factors. Use when actor catalogs, use-case specifications, and supplementary specifications already exist and you need a traceable UCP breakdown without LLM-improvised math.
---

# UCP Estimator

Estimate Use Case Points from validated artifacts.

## Inputs
Required inputs:
- actor catalog
- use-case specifications
- supplementary specification
- TCF ratings
- ECF ratings

These inputs must conform to the schemas and contracts in `skills/use-case-points-core/schemas/` and `skills/use-case-points-core/configs/`.

## Deterministic boundary
- Do not invent formulas
- Do not infer missing ratings
- Do not estimate if actors or use cases remain unclassified
- Fail validation rather than guessing

## Formula components
- UAW
- UUCW
- UUCP
- TCF
- ECF
- UCP

Use the deterministic calculator contract in `references/estimator-workflow.md`.

## Output requirements
Always return a traceable structure including:
- actor weight breakdown
- use-case weight breakdown
- UUCP
- TCF inputs and result
- ECF inputs and result
- final UCP
- optional effort estimate if productivity factor is supplied

## Workflow
1. Confirm artifacts are present and validated
2. Confirm actor and use-case classifications are complete
3. Confirm TCF and ECF ratings are complete
4. Apply deterministic formulas only
5. Return structured estimate and any blocking issues
