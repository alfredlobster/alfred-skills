---
name: research-pipeline-orchestrator
description: Orchestrate the full six-skill scientific pipeline in strict order with YAML handoff chaining and optional final combined report generation. Use when a user wants end-to-end execution from one initial question through intake, hypotheses, experiment design, critique, ranking, and study plan.
---

# Research Pipeline Orchestrator

Run the 6-skill chain in strict order and carry forward YAML payloads.

## Ordered Execution
1. research-intake-brief
2. hypothesis-generator
3. experiment-designer
4. critic-reviewer
5. ranking-and-decision
6. study-plan-generator

## Chaining Rules
- Extract the fenced YAML payload from each step.
- Pass only the relevant payload + short context to the next step.
- If payload parse fails, stop and emit `CHAIN_ERROR` with failing stage.
- Preserve payload version fields.

## Output Rules
- Return:
  - a short status line per stage (OK|WARN|FAIL)
  - final verdict (PASS|PARTIAL|FAIL)
  - final recommendation and immediate actions
- If requested, call `research-pipeline-reporter` at the end.

## Failure Policy
- Missing critical fields in a payload => WARN and continue only if next stage can still run.
- Two consecutive stage failures => FAIL and stop.

## Determinism
Read `references/orchestration-contract.md` and follow exact state transitions.
