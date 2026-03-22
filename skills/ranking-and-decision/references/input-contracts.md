# Input Contracts

## Accepted Structured Payloads

This skill may receive any of the following payloads.

### Research Brief
Use this payload as the canonical source for problem framing, evidence, constraints, and unknowns.

```yaml
research_brief_handoff:
  version: "1.0"
  mode: "fast|guided|rigorous"
  research_goal: ""
  problem_statement: ""
  success_criteria: []
  constraints: []
  known_facts: []
  user_claims_needing_validation: []
  inferred_assumptions: []
  unknowns: []
  candidate_hypothesis_directions: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

### Hypothesis Portfolio
Use this payload as the canonical source for candidate hypotheses, supporting evidence, assumptions, and current prioritization hints.

```yaml
hypothesis_portfolio_handoff:
  version: "1.0"
  source_payload_version: "1.0|unknown"
  research_goal: ""
  problem_statement: ""
  hypotheses: []
  cross_hypothesis_observations: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

### Experiment Plan
Use this payload as the canonical source for candidate experiments, controls, readouts, feasibility notes, and operational risks.

```yaml
experiment_plan_handoff:
  version: "1.0"
  source_payload_version: "1.0|unknown"
  research_goal: ""
  problem_statement: ""
  experiments: []
  data_requirements: []
  key_risks: []
  open_questions: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

### Critique Review
Use this payload as the canonical source for issues, severity, and corrective actions that should affect ranking.

```yaml
critique_review_handoff:
  version: "1.0"
  source_artifact_type: "research_brief|hypothesis_portfolio|experiment_plan|mixed|unknown"
  source_payload_version: "1.0|unknown"
  overall_assessment: "robust|mixed|fragile|unknown"
  major_issues: []
  residual_strengths: []
  recommended_next_skill: ""
  recommended_next_action: ""
```

## Canonical Input Selection

If multiple payloads are present:
1. Prefer the most downstream payload for structure.
2. Use upstream payloads to recover omitted context and constraints.
3. Let critique findings adjust confidence, feasibility, or risk rather than replacing the underlying options.
4. Do not silently overwrite contradictions. Surface them explicitly.

## Option Reconstruction Rules

If there is no explicit options list:
- derive options from candidate hypotheses, experiments, strategies, or study directions in the input
- collapse near-duplicates
- generate only the smallest decision-worthy option set
- name options clearly and consistently as O1, O2, O3, and so on

## Normalization Rules

Always preserve these distinctions:
- evidence versus argument
- fact versus inference
- user preference versus objective constraint
- uncertainty versus absence

## Missing Information Rules

- If criteria are missing, infer a minimal criteria set and say so.
- If an option is badly specified, keep it provisional rather than pretending detail.
- If the option set is too weak to rank honestly, say that the main need is reframing or more design work.
