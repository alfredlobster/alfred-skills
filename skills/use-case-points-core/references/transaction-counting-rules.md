# UCP Transaction Counting Rules

## Purpose
Define how transaction counts are derived from use-case specifications for UCP classification.

## Counting principle
A transaction is a meaningful interaction step across the system boundary that advances the use case.

## Count as transactions
- Actor input that causes system processing
- System response that returns meaningful state or output to an actor
- Distinct request/response interactions with external systems when explicitly part of the use-case flow

## Do not count separately
- Pure UI formatting or cosmetic rendering details
- Validation wording variants that do not change control flow
- Logging/audit internals unless they are explicit use-case behavior across the boundary

## Ambiguity rules
Flag for review when:
- the main flow is too abstract to count consistently
- alternate flows appear to hide core main-flow steps
- a single bullet combines multiple interactions
- background integrations are implied but not specified

## Output expectation
Transaction counting should return:
- `transaction_count`
- `counting_notes`
- `ambiguity_flags`
- `derived_from_sections` (main flow, alternate flow, exception flow)
