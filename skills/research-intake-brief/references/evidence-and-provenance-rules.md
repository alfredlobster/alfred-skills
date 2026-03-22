# Evidence and Provenance Rules

## Core principle

Trace every important claim to its origin or mark it clearly as inference or uncertainty.

## Claim classes

Use these classes consistently.

### Known facts

Put a claim in `known_facts` only if it is directly supported by the user's material, accessible sources, or a clearly attributable external source.

Each fact should include:
- the statement
- provenance
- confidence

### User claims needing validation

Put a claim here when the user states it but the available material does not yet validate it.

Examples:
- assumed mechanism statements
- performance claims without data
- causal interpretations that may only be correlation

### Inferred assumptions

Put a claim here when it was introduced by reasoning rather than directly supplied or demonstrated.

Examples:
- assumed success metrics
- implied operational constraints
- inferred domain context

### Unknowns

Put missing or unresolved questions here.

Examples:
- absent baseline data
- unclear confounders
- uncertain feasibility constraints

## Provenance labels

Use concise provenance labels such as:
- user-provided
- uploaded paper
- uploaded notes
- web search
- connector search
- inferred from prompt
- inferred from multiple supplied sources

## Confidence labels

Use:
- high: directly supported and specific
- medium: plausible and partly supported
- low: weakly supported or heavily dependent on inference

Confidence is not a measure of importance.

## Forbidden behaviors

Do not:
- turn inference into fact
- imply validation that did not occur
- hide important uncertainty in prose
- cite inaccessible or non-existent sources
