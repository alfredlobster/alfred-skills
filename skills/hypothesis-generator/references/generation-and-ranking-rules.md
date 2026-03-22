# Generation and Ranking Rules

## Mode behavior

### Conservative

Use when evidence is weak, risk is high, or overproduction would create noise.

Default behavior:
- generate 2 to 3 hypotheses
- stay close to the evidence base
- prefer plausibility and testability over novelty
- surface missing evidence aggressively

### Balanced

Use as the default.

Default behavior:
- generate 3 to 5 hypotheses
- mix near-term plausible explanations with one or two broader alternatives
- maintain a visible distinction between stronger and weaker candidates

### Expansive

Use when the user explicitly wants broader search or the cost of extra candidates is low.

Default behavior:
- generate 5 to 7 hypotheses
- explore wider causal or intervention possibilities
- keep weakly supported candidates clearly labeled as such
- avoid turning brainstorming into pseudo-facts

## Ranking dimensions

For each hypothesis, assess these dimensions using qualitative labels only:
- novelty
- plausibility
- impact_if_true
- testability
- overall_priority

Use `high`, `medium`, `low`, or `unknown`.

## Scoring guidance

Do not compute fake numeric scores.
Use lightweight judgment anchored in the evidence.

- `novelty`: how different the hypothesis is from obvious baseline explanations in the provided context
- `plausibility`: how well it fits the known facts and established mechanisms, given current evidence
- `impact_if_true`: how important it would be if supported
- `testability`: how feasible it is to discriminate with available or likely experiments
- `overall_priority`: synthesis of plausibility, impact, testability, and current constraints

## Distinctness rule

A new hypothesis must differ by mechanism, causal story, or intervention logic.
A wording variation is not a new hypothesis.

## Evidence rule

Every hypothesis must name at least one supporting evidence item or explicitly say that evidence is currently weak.
Never fabricate literature support.
