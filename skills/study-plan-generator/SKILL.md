---
name: study-plan-generator
description: convert a ranked scientific or technical decision into an executable staged study plan with milestones, dependencies, decision gates, fallback branches, evidence checkpoints, and deterministic YAML handoff. use when chatgpt needs to turn a research brief, hypothesis portfolio, experiment plan, critique review, ranking decision, notes, or mixed materials into a practical near-term execution plan while preserving provenance, uncertainty, and explicit assumptions.
---

# Study Plan Generator

## Overview

Turn a recommendation into an executable study sequence.

Use this skill when the next bottleneck is operationalization: what to do first, what must be prepared beforehand, which checkpoints matter, what can run in parallel, and which results should trigger continuation, revision, or stop.

## Workflow

Follow this sequence:

1. Detect the dominant upstream artifact and whether a structured handoff payload is present.
2. Identify the study objective, current recommendation, constraints, and planning horizon.
3. Normalize candidate work into a small set of stages and tasks.
4. Choose the planning mode: lean, standard, or rigorous.
5. Build a staged plan with dependencies, checkpoints, and branch conditions.
6. Produce a structured study plan.
7. Produce a deterministic YAML handoff payload.
8. Recommend the next skill to run.

## Preferred inputs

Accept any mix of:
- a `research_brief_handoff` payload from `research-intake-brief`
- a `hypothesis_portfolio_handoff` payload from `hypothesis-generator`
- an `experiment_plan_handoff` payload from `experiment-designer`
- a `critique_review_handoff` payload from `critic-reviewer`
- a `ranking_decision_handoff` payload from `ranking-and-decision`
- prose briefs, notes, papers, project constraints, resource assumptions, or execution questions
- direct prompts such as “turn this into a study plan”, “what should we do over the next two weeks?”, or “sequence the work”

If a valid structured payload is present, treat it as the canonical structural source. Use surrounding prose only to recover context, constraints, domain nuance, or user preferences.

## Input normalization rules

Read `references/input-contracts.md` before using a handoff payload.

Always preserve the distinction between:
- known facts or directly supported evidence
- user claims needing validation
- inferred assumptions
- unknowns and unresolved dependencies

Never turn a recommendation into a committed plan without exposing the assumptions, prerequisites, and decision gates that make the plan viable.

## Planning mode selection

Choose one mode automatically unless the user specifies otherwise.

- Use **lean** when the user wants a compact near-term action plan, when the scope is small, or when only the first stage matters.
- Use **standard** by default when a realistic staged plan is needed with checkpoints and fallback logic.
- Use **rigorous** when the program is high stakes, resource intensive, cross-functional, or highly sensitive to sequencing errors.

Read `references/planning-modes.md` for the exact behavior of each mode.

## Planning rules

- Plan from the currently recommended option unless the user explicitly wants a multi-path plan.
- Convert the chosen direction into the smallest executable stage sequence.
- Prefer explicit decision gates over vague “continue if promising” wording.
- Keep prerequisites, data needs, and enabling work visible.
- Separate parallelizable tasks from blocking dependencies.
- Include stop, revise, or branch triggers when uncertainty is material.
- Use short planning horizons unless the user explicitly asks for a long program roadmap.
- Avoid pretending exact duration, capacity, or resourcing when these are unknown.
- Use relative timing and stage order unless concrete timing is well supported.

## Output requirements

Read `references/study-plan-template.md` and follow it exactly.

Produce two sections in this order:
1. `## Study Plan`
2. `## Handoff Payload`

The handoff payload must be valid YAML inside a fenced code block.

### Required output behaviors

- Use stable field names.
- Keep each stage outcome-oriented.
- Make dependencies and branch conditions explicit.
- Use `unknown`, `null`, or empty lists instead of invented operational detail.
- Include `recommended_next_skill` and `recommended_next_action`.
- Preserve payload version.

## Downstream handoff rules

Read `references/escalation-and-next-skills.md` when deciding the next step.

Downstream skills should be able to consume the YAML payload directly. Therefore:
- keep the chosen path explicit
- keep stage goals and decision gates inspectable
- attach provenance and confidence where evidence drives sequencing
- state what evidence would trigger escalation, replanning, or execution expansion
- prefer `experiment-designer` when the plan fails because the core test design is still weak
- prefer `critic-reviewer` when hidden risk, bias, or fragility remains the main blocker
- prefer `ranking-and-decision` when multiple live branches still need comparison
- prefer `research-intake-brief` when the work uncovers a reframed problem statement

## Style

Be practical and sequence-aware.
Do not hide uncertainty inside polished project language.
If the study plan is fragile because the recommendation or inputs are weak, say so plainly.
