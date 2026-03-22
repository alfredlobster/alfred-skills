# Critique Output Template

## Output Order

Always produce the following sections in this order:

## Critique Report

Use this exact top-level structure:

### Artifact Under Review
- one short paragraph describing what was reviewed and at what critique depth

### Overall Assessment
- one short paragraph on whether the artifact is robust, fragile, or mixed

### Major Issues
For each major issue, use this exact substructure:

#### C1. [Short title]
- **Severity:** critical, major, moderate, or minor
- **What the issue is:** one or two sentences
- **Why it matters:** short explanation of the decision risk or interpretive risk
- **Affected element:** hypothesis, experiment, assumption, ranking logic, measurement plan, or other
- **Evidence basis for the critique:** bullets
- **Corrective action:** bullets
- **Confidence in this critique:** high, medium, or low

Repeat for C2, C3, and so on.

### Residual Strengths
- bullets describing what still looks solid

### Recommended Next Step
- name the next skill and explain why in one short paragraph

## Handoff Payload

Return valid YAML in a fenced code block.

Use this schema and preserve field names exactly:

```yaml
critique_review_handoff:
  version: "1.0"
  source_artifact_type: "research_brief|hypothesis_portfolio|experiment_plan|mixed|unknown"
  source_payload_version: "1.0|unknown"
  critique_depth: "quick|standard|deep"
  overall_assessment: "robust|mixed|fragile|unknown"
  major_issues:
    - id: "C1"
      title: ""
      severity: "critical|major|moderate|minor"
      what_the_issue_is: ""
      why_it_matters: ""
      affected_element: ""
      evidence_basis:
        - statement: ""
          provenance: ""
          confidence: "high|medium|low"
      corrective_actions: []
      critique_confidence: "high|medium|low"
  residual_strengths: []
  recommended_next_skill: "ranking-and-decision"
  recommended_next_action: ""
```

## Missing Information Rules

- Use empty lists where no items are available.
- Use `unknown` for short scalar fields when information is insufficient.
- Never fabricate evidence, confounders, or controls.
- If details are missing, critique the absence explicitly rather than inventing specifics.

## Compression Rules

Inside YAML:
- keep each issue atomic
- keep `what_the_issue_is` and `why_it_matters` short
- avoid repeating prose from the human-readable section
- keep corrective actions concise and executable
