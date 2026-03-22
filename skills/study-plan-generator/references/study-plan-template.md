# Study Plan Template

## Output Order

Always produce the following sections in this order:

## Study Plan

Use this exact top-level structure:

### Objective
- one short paragraph stating what this plan is trying to achieve

### Chosen Path And Planning Basis
- one short paragraph describing the selected direction and what artifacts or evidence the plan is based on

### Assumptions And Constraints
- bullets listing assumptions, constraints, and key dependencies

### Stage Plan
For each stage, use this exact substructure:

#### S1. [Short stage label]
- **Purpose:** one or two sentences
- **Inputs / prerequisites:** bullets
- **Core activities:** bullets
- **Expected outputs:** bullets
- **Decision gate:** bullets describing what must be true to continue, revise, or stop
- **Parallel work:** bullets
- **Main risks or blockers:** bullets

Repeat for S2, S3, and so on.

### Cross-Stage Risks And Watchpoints
- bullets for risks that affect multiple stages

### Immediate Next Actions
- bullets for the first concrete actions to start the plan

### Recommended Next Step
- name the next skill and explain why in one short paragraph

## Handoff Payload

Return valid YAML in a fenced code block.

Use this schema and preserve field names exactly:

```yaml
study_plan_handoff:
  version: "1.0"
  source_artifact_type: "research_brief|hypothesis_portfolio|experiment_plan|critique_review|ranking_decision|mixed|unknown"
  source_payload_version: "1.0|unknown"
  planning_mode: "lean|standard|rigorous"
  study_objective: ""
  chosen_path:
    label: ""
    rationale: ""
  planning_basis:
    evidence_basis:
      - statement: ""
        provenance: ""
        confidence: "high|medium|low"
    assumptions: []
    constraints: []
    dependencies: []
  stages:
    - id: "S1"
      label: ""
      purpose: ""
      inputs_or_prerequisites: []
      core_activities: []
      expected_outputs: []
      decision_gate:
        continue_if: []
        revise_if: []
        stop_if: []
      parallel_work: []
      main_risks_or_blockers: []
  cross_stage_risks: []
  immediate_next_actions: []
  recommended_next_skill: "critic-reviewer|experiment-designer|ranking-and-decision|research-intake-brief|unknown"
  recommended_next_action: ""
```

## Missing Information Rules

- Use empty lists where no items are available.
- Use `unknown` for short scalar fields when information is insufficient.
- Do not invent resources, durations, approvals, or exact staffing.
- If the selected path is still provisional, say so explicitly in both the prose section and the YAML payload.

## Compression Rules

Inside YAML:
- keep each stage compact and outcome-oriented
- do not repeat the same dependency in many places unless necessary
- keep gate criteria inspectable and concrete
- keep `immediate_next_actions` short and executable
