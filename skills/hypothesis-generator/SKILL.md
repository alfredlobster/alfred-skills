---
name: hypothesis-generator
description: generate a structured portfolio of candidate scientific or technical hypotheses from a research brief, messy notes, uploaded materials, or prior skill handoff payloads. use when chatgpt needs to expand plausible explanations or intervention ideas, preserve provenance and uncertainty, rank hypotheses lightly, and prepare a deterministic handoff for experiment design, critique, or decision-making.
---

# Hypothesis Generator

## Overview

Generate a compact, high-quality hypothesis portfolio from a framed research problem.

Prefer explicit logic, discriminating value, and uncertainty tracking over creativity for its own sake. The skill is domain-agnostic: do not invent specialist knowledge when evidence is thin.

## Workflow

Follow this sequence:

1. Detect whether a structured handoff payload is present.
2. Normalize the available context into the minimum working problem frame.
3. Decide the generation mode: conservative, balanced, or expansive.
4. Generate non-duplicate candidate hypotheses.
5. Stress-test each hypothesis for assumptions, evidence, and discriminating tests.
6. Produce a hypothesis portfolio and a structured YAML handoff payload.
7. Recommend the next skill to run.

## Preferred inputs

Accept any mix of:
- a `research_brief_handoff` YAML payload from `research-intake-brief`
- a prose research brief
- pasted notes or papers
- user-supplied candidate hypotheses
- structured metadata
- contradictory evidence or constraints

If a valid `research_brief_handoff` payload is present, treat it as the canonical structural source. Use surrounding prose only to enrich nuance.

If no structured payload is present, infer a minimal frame from the materials. Ask questions only when the missing context would materially degrade the hypothesis quality.

## Input normalization rules

Read `references/input-contract.md` before using a handoff payload.

Always separate:
- known facts
- user claims needing validation
- inferred assumptions
- unresolved unknowns

Do not silently upgrade a weak or inferred statement into an established fact.

## Generation mode selection

Choose one mode automatically unless the user specifies otherwise.

- Use **conservative** when evidence is thin, stakes are high, or the brief is fragile. Generate fewer, tighter hypotheses.
- Use **balanced** by default when the problem is reasonably framed and some evidence exists.
- Use **expansive** when the user wants broader ideation, the cost of false positives is low, or the brief explicitly invites wider exploration.

Read `references/generation-and-ranking-rules.md` for the exact behavior of each mode.

## Hypothesis quality rules

Each hypothesis must be:
- distinct from the others
- stated as a falsifiable or at least discriminable proposition
- supported by explicit rationale
- bounded by assumptions and uncertainty
- accompanied by one or more discriminating tests or observations

Avoid these failure modes:
- trivial restatements of the problem
- near-duplicates that differ only in wording
- hypotheses that bundle multiple causal stories into one item
- vague claims with no plausible test path
- novelty theater unsupported by the evidence

## Output requirements

Read `references/hypothesis-output-template.md` and follow it exactly.

Produce two sections in this order:
1. `## Hypothesis Portfolio`
2. `## Handoff Payload`

The handoff payload must be valid YAML inside a fenced code block.

### Required output behaviors

- Use stable field names.
- Preserve provenance and confidence where possible.
- Generate 3 to 5 hypotheses by default.
- Generate fewer hypotheses when the evidence base is weak.
- Use `unknown`, `null`, or empty lists instead of inventing content.
- Include `recommended_next_skill` and `recommended_next_action`.
- Preserve the payload version.

## Downstream handoff rules

Read `references/handoff-to-next-skills.md` when deciding the next step.

Downstream skills should be able to consume the YAML payload directly. Therefore:
- keep hypothesis statements short and atomic
- keep supporting evidence items concise
- attach assumptions and discriminating tests to each hypothesis
- avoid hiding ranking logic in prose only
- prefer `experiment-designer` when the top hypotheses are coherent enough to test
- prefer `critic-reviewer` when the portfolio feels fragile or overconfident
- prefer `ranking-and-decision` when several credible options compete under strong constraints

## Style

Be concise, explicit, and operational.
Do not overstate novelty, plausibility, or evidence strength.
If the hypotheses are weak because the brief is weak, say so plainly.
