---
name: research-intake-brief
description: create a structured research brief from messy scientific or technical inputs such as a research question, pasted notes, uploaded papers, problem statements, and metadata. use when chatgpt needs to frame a research problem, interview for missing context, normalize evidence, label provenance and confidence, and prepare a deterministic handoff payload for downstream skills such as hypothesis generation, experiment design, ranking, critique, or study planning.
---

# Research Intake Brief

## Overview

Create a canonical research brief and a structured YAML handoff payload from incomplete, mixed-quality, or multi-source research input.

The skill is domain-agnostic. Do not pretend to have deep domain expertise where evidence is thin. Separate established facts, user claims, inferred assumptions, and open questions. Prefer clarity and traceability over eloquence.

## Workflow

Follow this sequence:

1. Inspect the input and identify what was provided.
2. Decide the intake mode: fast, guided, or rigorous.
3. Gather only the missing information needed to produce a useful brief.
4. Synthesize the research brief.
5. Produce the YAML handoff payload.
6. Recommend the next skill to run.

## Input handling

Accept any mix of:
- a research question
- a problem statement
- pasted notes
- uploaded papers or excerpts
- structured metadata
- partial hypotheses
- contradictory context
- constraints, timelines, or evaluation criteria

If the user provides rich material already, do not force an interview. Synthesize directly unless material gaps would materially reduce the value of the brief.

If external sources or tools are available, use them. Make provenance explicit for every nontrivial claim.

## Intake mode selection

Choose one mode automatically.

- Use **fast** when the prompt and attached material already provide a clear problem, constraints, and enough evidence to draft the brief.
- Use **guided** when the problem is understandable but important fields are missing. Ask a compact set of questions, then synthesize.
- Use **rigorous** when ambiguity, risk, or weak framing is high, or when the user appears to be optimizing the wrong question. Challenge assumptions before locking the brief.

Read `references/intake-modes.md` for the exact behavior of each mode.

## Interview rules

Ask questions only when they close material gaps. Prefer the smallest question set that unlocks a high-quality brief.

Prioritize these missing fields, in order:
1. research goal
2. success criteria
3. constraints
4. available evidence or materials
5. scope boundaries
6. critical unknowns or assumptions

Do not ask for information that is already present in the prompt or attachments.

## Evidence and reasoning rules

Read `references/evidence-and-provenance-rules.md` before finalizing the brief.

Always:
- distinguish fact from inference
- distinguish user assertion from validated evidence
- mark unresolved ambiguity explicitly
- preserve uncertainty rather than smoothing it away
- keep unsupported speculation out of the fact sections

If a claim is important but weakly supported, move it into `user_claims_needing_validation`, `inferred_assumptions`, or `unknowns` rather than `known_facts`.

## Output requirements

Read `references/research-brief-template.md` and follow it exactly.

Produce two sections in this order:
1. `## Research Brief`
2. `## Handoff Payload`

The handoff payload must be valid YAML inside a fenced code block.

Use the payload as the canonical machine-readable summary for downstream skills. The prose brief is for human review and nuance.

### Required output behaviors

- Use a fixed top-level structure.
- Keep field names stable.
- Use `null`, `unknown`, or empty lists when information is genuinely unavailable.
- Do not invent content to fill the schema.
- Include `recommended_next_skill` and `recommended_next_action`.
- Preserve the payload version.

## Downstream handoff rules

Read `references/escalation-to-next-skills.md` when deciding the next step.

Downstream skills should be able to consume the YAML payload directly. Therefore:
- prefer compact, precise entries over long narrative text inside YAML
- keep provenance and confidence attached to claims where possible
- avoid restating the same point across multiple fields
- keep candidate hypothesis directions high level unless the input supports more detail

## Style

Be concise, explicit, and operational.
Do not overstate novelty or confidence.
If the brief is weak because the input is weak, say so plainly.
