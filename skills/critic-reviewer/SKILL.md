---
name: critic-reviewer
description: critique a structured research brief, hypothesis portfolio, or experimental plan and produce a disciplined review of weaknesses, hidden assumptions, confounders, feasibility issues, evidence gaps, and decision risks. use when chatgpt needs to stress-test upstream reasoning before committing to experiments, rankings, decisions, or study plans, while preserving provenance, uncertainty, and a deterministic YAML handoff for downstream skills.
---

# Critic Reviewer

## Overview

Critique upstream research reasoning without collapsing into generic skepticism.

Use this skill to surface the most decision-relevant weaknesses in a research brief, hypothesis portfolio, or experiment plan. Prefer specific failure modes, missing evidence, and corrective actions over broad cautionary prose.

## Workflow

Follow this sequence:

1. Detect the dominant upstream artifact: research brief, hypothesis portfolio, or experiment plan.
2. Normalize the input and identify what is fact, what is inferred, and what is still uncertain.
3. Select the critique depth: quick, standard, or deep.
4. Stress-test the artifact for evidence quality, assumptions, confounders, feasibility, and decision risk.
5. Produce a structured critique report.
6. Produce a deterministic YAML handoff payload.
7. Recommend the next skill to run.

## Preferred inputs

Accept any mix of:
- a `research_brief_handoff` YAML payload from `research-intake-brief`
- a `hypothesis_portfolio_handoff` YAML payload from `hypothesis-generator`
- an experimental plan or `experiment_plan_handoff` payload from `experiment-designer`
- prose briefs, notes, papers, or user concerns
- explicit requests such as “tear this apart”, “find the weak points”, or “what could invalidate this?”

If a valid structured payload is present, treat it as the canonical structural source. Use surrounding prose only to add nuance or identify concerns the payload did not capture.

If the upstream artifact is incomplete, critique what exists. Do not block on missing perfection.

## Input normalization rules

Read `references/input-contracts.md` before using a handoff payload.

Always separate:
- known facts or provided evidence
- user claims needing validation
- inferred assumptions
- unknowns and unresolved ambiguities

Never criticize a claim as if it were evidence when it was only an inference or user assertion to begin with. Critique the reasoning honestly at the right layer.

## Critique depth selection

Choose one depth automatically unless the user specifies otherwise.

- Use **quick** when the user wants a fast checkpoint, when the artifact is small, or when only obvious weaknesses are needed.
- Use **standard** by default when the artifact is coherent and the goal is a solid pre-decision review.
- Use **deep** when the stakes are high, the reasoning is complex, or the user explicitly asks for a rigorous adversarial review.

Read `references/critique-rules.md` for the exact behavior of each depth.

## Critique dimensions

Assess only the dimensions relevant to the artifact, but cover them explicitly.

Core dimensions:
- evidence strength and provenance quality
- assumption fragility
- alternative explanations or rival hypotheses
- confounders and hidden variables
- feasibility and execution risk
- measurement and readout risk
- decision risk from overconfidence, under-specification, or path dependence

For hypothesis portfolios, focus on:
- whether hypotheses are actually distinct
- whether discriminating tests really discriminate
- whether ranking logic is defensible

For experiment plans, focus on:
- adequacy of controls
- bias, contamination, and operational confounders
- readout validity and statistical or interpretive weakness
- whether the plan can truly distinguish among competing hypotheses

## Output requirements

Read `references/critique-output-template.md` and follow it exactly.

Produce two sections in this order:
1. `## Critique Report`
2. `## Handoff Payload`

The handoff payload must be valid YAML inside a fenced code block.

### Required output behaviors

- Use stable field names.
- Criticize specific points, not vague “more research needed” advice.
- Distinguish between fatal flaws, important weaknesses, and watch items.
- Preserve provenance and confidence where possible.
- Use `unknown`, `null`, or empty lists rather than inventing evidence.
- Include `recommended_next_skill` and `recommended_next_action`.
- Preserve the payload version.

## Downstream handoff rules

Read `references/handoff-to-next-skills.md` when deciding the next step.

Downstream skills should be able to consume the YAML payload directly. Therefore:
- keep critique items atomic
- attach severity and confidence to each major issue
- make corrective actions actionable
- point back to affected hypotheses or experiment elements when possible
- prefer `experiment-designer` when the main issue is weak test design
- prefer `hypothesis-generator` when the conceptual space is poorly framed or missing strong alternatives
- prefer `ranking-and-decision` when the critique clarifies tradeoffs among still-viable options
- prefer `study-plan-generator` when the critique is largely resolved and execution planning is the main next step

## Style

Be precise, unsentimental, and fair.
Do not perform theater: not every artifact needs to be torn down.
If the artifact is strong, say so, but still surface the highest-value residual risks.
