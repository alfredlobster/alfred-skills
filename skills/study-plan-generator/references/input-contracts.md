# Input Contracts

## Accepted Structured Payloads

This skill may receive any of the following payloads.

### Research Brief
Use this payload for problem framing, constraints, evidence, and unknowns.

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
Use this payload for hypothesis candidates, rationale, and uncertainty.

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
Use this payload for experiments, controls, readouts, key risks, and data requirements.

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
Use this payload for issues that must shape the plan or introduce gates and fallback branches.

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

### Ranking Decision
Use this payload as the canonical source when an option has already been ranked and selected.

```yaml
ranking_decision_handoff:
  version: "1.0"
  source_artifact_type: "research_brief|hypothesis_portfolio|experiment_plan|critique_review|mixed|unknown"
  source_payload_version: "1.0|unknown"
  decision_mode: "quick|balanced|rigorous"
  decision_question: ""
  decision_criteria: []
  options: []
  ranked_order: []
  recommended_option_id: "O1|unknown"
  recommendation_rationale: ""
  key_tie_breakers: []
  conditions_that_would_change_decision: []
  recommended_next_skill: "study-plan-generator"
  recommended_next_action: ""
```

## Canonical Input Selection

If multiple payloads are present:
1. Prefer `ranking_decision_handoff` for the chosen path and criteria.
2. Use `experiment_plan_handoff` for concrete actions, controls, and readouts.
3. Use `critique_review_handoff` to introduce safeguards, gates, and fallback logic.
4. Use upstream payloads to recover missing context, constraints, and assumptions.
5. Surface contradictions explicitly rather than silently resolving them.

## Planning Horizon Rules

Unless the user specifies otherwise:
- default to near-term planning
- focus on the next meaningful tranche of work
- avoid pretending to know full program timelines
- prefer stage order and gating over calendar certainty

## Normalization Rules

Always preserve these distinctions:
- plan versus commitment
- blocker versus inconvenience
- dependency versus nice-to-have
- evidence-backed gate versus arbitrary milestone
- uncertainty versus missing information

## Missing Information Rules

- If the selected path is unclear, make that the first planning issue and recommend `ranking-and-decision`.
- If operational detail is missing, keep the plan abstract but executable.
- If the plan depends on unknown resources, approvals, or datasets, expose them as dependencies rather than assuming availability.
