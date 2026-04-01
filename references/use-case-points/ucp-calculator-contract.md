# Use Case Point Deterministic Calculator Contract

## Purpose
Define the deterministic input/output contract for UCP calculation.

## Scope
The calculator reads validated actor and use-case artifacts and applies fixed formulas for:
- UAW
- UUCW
- UUCP
- TCF
- ECF
- UCP

It does **not** gather requirements, classify ambiguous cases via LLM judgment, or infer missing ratings.

## Inputs
- Actor catalog with per-actor complexity classification
- Use-case specifications with transaction counts and per-use-case complexity classification
- TCF ratings (T1-T13)
- ECF ratings (E1-E8)
- Optional productivity factor (hours per UCP), handled separately from scope estimate

## Core formulas
- `UAW = sum(actor_count_by_class * class_weight)`
- `UUCW = sum(use_case_count_by_class * class_weight)`
- `UUCP = UAW + UUCW`
- `TFactor = sum(T_weight * T_rating)`
- `TCF = 0.6 + (0.01 * TFactor)`
- `EFactor = sum(E_weight * E_rating)`
- `ECF = 1.4 + (-0.03 * EFactor)`
- `UCP = UUCP * TCF * ECF`

## Output shape
The calculator should return a traceable structure including:
- UAW breakdown
- UUCW breakdown
- UUCP
- TFactor and TCF
- EFactor and ECF
- final UCP
- optional effort estimate if productivity factor is supplied

## Boundary rule
All math is deterministic. If classification or ratings are missing, the calculator should fail validation rather than improvise.
