# UCP Review / Validation Issue Categories

## Completeness
Use when required structural information is missing.
Examples:
- actor missing description
- use case missing trigger
- empty main flow

## Consistency
Use when references or IDs do not line up.
Examples:
- actor referenced by use case not found in actor catalog
- NFR reference unresolved
- duplicated IDs

## Classification Readiness
Use when there is not enough information to classify actors/use cases confidently.
Examples:
- actor complexity unclear
- transaction count cannot be derived
- flow wording too abstract

## Estimation Readiness
Use when calculation inputs are incomplete or blocked.
Examples:
- TCF/ECF ratings missing
- unclassified actors remain
- validation errors present in upstream artifacts
