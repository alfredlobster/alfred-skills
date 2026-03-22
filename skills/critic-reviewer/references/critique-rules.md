# Critique Rules

## Critique Depths

### Quick
Use for fast checkpointing.

Behavior:
- identify the top 3 to 5 issues only
- focus on the highest expected decision risk
- keep remediation short and practical
- avoid exhaustive edge-case hunting

### Standard
Use by default.

Behavior:
- cover all relevant critique dimensions
- distinguish major issues from secondary watch items
- include at least one alternative explanation or failure path when relevant
- propose targeted corrective actions

### Deep
Use for high-stakes or high-complexity review.

Behavior:
- interrogate assumption chains explicitly
- test whether upstream ranking logic survives counterarguments
- search for confounders, omitted variables, and measurement traps
- assess whether planned experiments can truly discriminate among hypotheses
- include adversarial reasoning without becoming speculative theater

## Severity Definitions

- **critical**: could invalidate the core conclusion or make the next step unsafe or wasteful
- **major**: materially weakens confidence, prioritization, or interpretability
- **moderate**: worth resolving if resources allow, but not always blocking
- **minor**: useful cleanup or caution, not decision-driving on its own

## Confidence Definitions

- **high**: the critique follows directly from the provided artifact or evidence gap
- **medium**: the critique is well grounded but depends on some interpretation
- **low**: plausible concern, but the artifact does not provide enough detail to be sure

## Good Critique Patterns

Prefer critique items like these:
- a discriminating test does not actually separate H1 from H2 because both predict the same readout
- the experimental plan lacks a negative control, so any positive signal is hard to interpret
- the highest-ranked hypothesis relies on an unstated assumption that was never supported
- the proposed measurement is downstream of several latent variables and may not map cleanly to the target phenomenon

Avoid critique items like these:
- more evidence is needed
- there may be confounders
- the study should be robust
- the hypothesis may be wrong

## Corrective Action Rules

Each major issue should have a corresponding corrective action whenever possible.

Corrective actions should be:
- specific
- feasible
- proportional to the issue
- targeted at the actual weakness rather than generic “do more research” guidance
