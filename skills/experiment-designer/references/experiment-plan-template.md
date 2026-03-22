# Experiment Plan Template

Use this exact top-level structure. Adapt detail inside sections, but do not change section names.

## Experimental Plan

### 1. Research objective
- Restate the objective in operational terms.
- State the decision this plan is intended to support.

### 2. Hypothesis frame
- Identify the primary hypothesis or candidate directions.
- Note the strongest competing explanations.
- State what would count as support, contradiction, or ambiguity.

### 3. Experimental strategy
- State whether the plan is exploratory, confirmatory, or staged.
- Briefly explain why this strategy is appropriate.

### 4. Proposed experiments
For each experiment, include:
- name
- purpose
- key variables or factors
- controls and comparators
- readouts and measurements
- expected informative outcomes
- discriminating value across competing hypotheses
- practical notes on feasibility

### 5. Data and measurement plan
- Define primary and secondary readouts.
- Call out thresholds, endpoints, or success signals when possible.
- Note data quality requirements and likely measurement limitations.

### 6. Confounders and risks
- Identify technical confounders.
- Identify interpretation risks.
- Identify operational risks.

### 7. Prioritization
- Rank experiments by information gain, feasibility, and urgency.
- Explain sequencing logic.

### 8. Open questions
- List missing details that materially affect design quality.

### 9. Recommended next skill
- Choose one next skill.
- Explain why.

## Handoff Payload

Always append this YAML block after the human-readable plan.

```yaml
experiment_design_handoff:
  version: "1.0"
  design_mode: "compact|default|rigorous"
  source_brief_type: "research-brief|hypothesis-handoff|mixed|other"
  research_objective: ""
  decision_to_enable: ""
  primary_hypothesis:
    statement: ""
    provenance: "user-provided|uploaded|web|connector|inferred|mixed"
    confidence: "high|medium|low"
  competing_hypotheses:
    - statement: ""
      confidence: "high|medium|low"
  strategy_type: "exploratory|confirmatory|staged"
  experiments:
    - id: "exp-1"
      name: ""
      purpose: ""
      priority: 1
      information_gain: "high|medium|low"
      feasibility: "high|medium|low"
      variables:
        manipulated:
          - ""
        observed:
          - ""
      controls:
        positive:
          - ""
        negative:
          - ""
        baseline:
          - ""
      readouts:
        primary:
          - ""
        secondary:
          - ""
      expected_outcomes:
        supports_hypothesis:
          - ""
        weakens_hypothesis:
          - ""
        ambiguous:
          - ""
      confounders:
        - ""
      feasibility_notes:
        - ""
      provenance: "user-provided|uploaded|web|connector|inferred|mixed"
  data_requirements:
    - ""
  key_risks:
    - ""
  open_questions:
    - ""
  recommended_next_skill: "critic-reviewer"
  recommended_next_action: ""
```

## Missing Information Rules

- Use empty lists when a field is intentionally blank.
- Use `"unknown"` for scalar values that cannot be determined.
- Do not invent controls, thresholds, or readouts when they are truly unspecified.
- If uncertainty is high, state it explicitly in both the prose plan and the handoff payload.
