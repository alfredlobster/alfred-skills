# Evidence and Decision Rules

## Provenance categories

Use these consistently:
- `user-provided`
- `uploaded`
- `web`
- `connector`
- `inferred`
- `mixed`

## Confidence labels

- `high`: directly supported by high-quality evidence or explicit user input.
- `medium`: plausible and partially supported, but still uncertain.
- `low`: speculative, weakly supported, or mainly inferred.

## Fact discipline

Separate these categories when reasoning:
- established fact
- user assertion needing validation
- model inference
- open unknown

Do not let design convenience collapse these categories.

## Experiment selection rules

Prioritize experiments that:
1. Distinguish among competing hypotheses.
2. Reduce a critical uncertainty that blocks downstream decisions.
3. Are feasible relative to the stated constraints.
4. Produce interpretable readouts with acceptable confounding risk.

Deprioritize experiments that:
- only restate the current uncertainty without improving a decision
- are expensive but low-information
- depend on assumptions not yet stress-tested
- create difficult interpretation because controls are weak

## When to ask questions before planning

Ask questions only when one or more of these materially blocks design quality:
- the actual decision to enable is unclear
- the system under study is ambiguous
- the available measurements or instruments are unknown and central
- the constraints change the experiment class entirely
- safety, ethics, or regulated conditions could alter the plan

If the user appears to want speed, provide a draft plan and mark the blocked items as open questions instead.
