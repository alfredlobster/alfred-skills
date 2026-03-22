# Input Contracts

## Accepted Structured Payloads

This skill may receive any of the following payloads.

### Research Brief
Use this payload as the canonical source for problem framing, evidence, assumptions, constraints, and unknowns.

```yaml
research_brief_handoff:
  version: "1.0"
  mode: "fast|guided|rigorous"
  research_goal: ""
  problem_statement: ""
  domain_context: ""
  success_criteria: []
  constraints: []
  provided_materials: []
  known_facts: []
  user_claims_needing_validation: []
  inferred_assumptions: []
  unknowns: []
  literature_context: {}
  candidate_hypothesis_directions: []
  risks_and_confounders: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

### Hypothesis Portfolio
Use this payload as the canonical source for candidate hypotheses, supporting evidence, assumptions, and discriminating tests.

```yaml
hypothesis_portfolio_handoff:
  version: "1.0"
  source_payload_version: "1.0|unknown"
  research_goal: ""
  problem_statement: ""
  hypothesis_generation_mode: "conservative|balanced|expansive"
  hypotheses: []
  cross_hypothesis_observations: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

### Experiment Plan
Use this payload as the canonical source for test design, controls, measurements, sequencing, and operational risk.

```yaml
experiment_plan_handoff:
  version: "1.0"
  source_payload_version: "1.0|unknown"
  research_goal: ""
  problem_statement: ""
  design_mode: "lean|balanced|rigorous"
  experiments: []
  portfolio_level_risks: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

## Canonical Input Selection

If multiple payloads are present:
1. Prefer the most downstream payload for structure.
2. Use upstream payloads to recover omitted context.
3. Do not silently overwrite contradictions. Surface them explicitly.

## Normalization Rules

Always preserve these distinctions:
- fact versus inference
- user claim versus validated evidence
- uncertainty versus absence
- critique of reasoning versus critique of reality

## Missing Information Rules

- If the payload is partial, critique only the visible structure.
- If a field is missing, mark the gap and explain why it matters.
- Do not assume a plan includes controls, replication, or clear readouts unless they are actually stated.
