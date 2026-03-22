---
name: ranking-and-decision
description: rank competing scientific or technical options and recommend a next decision under constraints. use when chatgpt needs to compare hypotheses, experiments, study paths, or strategies from a research brief, hypothesis portfolio, experiment plan, critique review, notes, or mixed materials; make tradeoffs explicit; preserve provenance and uncertainty; avoid fake precision; and produce a deterministic YAML handoff for downstream execution or replanning.
---

# Ranking And Decision

## Overview

Turn multiple plausible options into a clear recommendation without hiding uncertainty or inventing precision.

Use this skill when the bottleneck is not generating more ideas but deciding what to do next under constraints such as time, cost, feasibility, evidence strength, learning value, and strategic fit.

## Workflow

Follow this sequence:

1. Detect the dominant upstream artifact and whether a structured handoff payload is present.
2. Normalize the candidate options and remove wording duplicates.
3. Identify the active decision question, constraints, and decision criteria.
4. Choose the decision mode: quick, balanced, or rigorous.
5. Rank the options using explicit tradeoffs and gating rules.
6. Produce a structured decision memo.
7. Produce a deterministic YAML handoff payload.
8. Recommend the next skill to run.

## Preferred inputs

Accept any mix of:
- a `research_brief_handoff` payload from `research-intake-brief`
- a `hypothesis_portfolio_handoff` payload from `hypothesis-generator`
- an `experiment_plan_handoff` payload from `experiment-designer`
- a `critique_review_handoff` payload from `critic-reviewer`
- prose briefs, papers, notes, options lists, or decision criteria
- direct questions such as “what should we do first?”, “rank these”, or “which option is best under our constraints?”

If a valid structured payload is present, treat it as the canonical structural source. Use surrounding prose only to enrich nuance, add constraints, or apply user-specified decision criteria.

If the user has not provided explicit options, derive a compact set of decision-worthy options from the input. Do not inflate the option set with near-duplicates.

## Input normalization rules

Read `references/input-contracts.md` before using a handoff payload.

Always separate:
- known facts or directly supported evidence
- user claims needing validation
- inferred assumptions
- open unknowns

Never treat a prior ranking, critique, or recommendation as evidence by itself. Treat it as reasoning to be assessed.

## Decision mode selection

Choose one mode automatically unless the user specifies otherwise.

- Use **quick** when the user wants a fast prioritization, when the option set is small, or when only the top recommendation is needed.
- Use **balanced** by default when there are multiple credible options and a normal decision needs to be made.
- Use **rigorous** when the stakes are high, constraints are severe, tradeoffs are complex, or the decision may commit significant resources.

Read `references/decision-frameworks.md` for the exact behavior of each mode.

## Ranking rules

- Use hard constraints as gates before ranking softer tradeoffs.
- Prefer a small, explicit set of criteria rather than a sprawling pseudo-framework.
- Use user-specified criteria and weights when provided.
- If criteria are missing, infer a minimal set and say so.
- Avoid fake numeric scoring unless the user explicitly asks for a weighted matrix.
- If using a matrix, keep the method simple and auditable.
- Preserve the distinction between evidence strength and expected value.
- Make tie-breakers and reversal conditions explicit.

## Output requirements

Read `references/ranking-output-template.md` and follow it exactly.

Produce two sections in this order:
1. `## Ranking And Decision`
2. `## Handoff Payload`

The handoff payload must be valid YAML inside a fenced code block.

### Required output behaviors

- Use stable field names.
- Rank only genuinely distinct options.
- Keep every option summary short and atomic.
- Distinguish strongest recommendation from provisional ranking.
- Use `unknown`, `null`, or empty lists instead of inventing certainty.
- Include `recommended_next_skill` and `recommended_next_action`.
- Preserve the payload version.

## Downstream handoff rules

Read `references/tie-break-and-escalation.md` when deciding the next step.

Downstream skills should be able to consume the YAML payload directly. Therefore:
- keep the decision question explicit
- keep criteria and weights short and inspectable
- attach provenance and confidence to evidentiary basis where possible
- state what would change the recommendation
- prefer `study-plan-generator` when the main need is execution sequencing
- prefer `experiment-designer` when the decision depends on a better discriminating test
- prefer `critic-reviewer` when hidden risk or weak reasoning is still the main blocker
- prefer `hypothesis-generator` when the option set is conceptually weak or incomplete

## Style

Be decisive without pretending certainty.
Show the tradeoffs.
If the ranking is fragile because the evidence is thin or the options are poorly framed, say so plainly.
