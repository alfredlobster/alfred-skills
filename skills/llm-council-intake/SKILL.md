---
name: llm-council-intake
description: Normalize a hard question or idea-evaluation task for the LLM Council workflow and choose the council members and chairman. Use when starting a Karpathy-faithful council run and you need a stable task statement plus explicit model/chairman configuration before parallel first opinions begin.
---

# LLM Council Intake

Prepare one task for a faithful LLM Council run.

## Purpose
Create a normalized intake artifact that can be handed to downstream stages without changing the task mid-run.

## Output boundary
This skill only prepares:
- normalized task statement
- evaluation focus
- council member list
- chairman model
- optional run settings

It does **not** generate first opinions, rankings, or final synthesis.

## Required output fields
- `task`
- `context` (optional but explicit)
- `council_models`
- `chairman_model`
- `evaluation_axes`
- `notes`

## Rules
- Keep the task statement stable and concise
- Make evaluation axes explicit (e.g. correctness, originality, feasibility, strategic value)
- Select chairman separately from the council if needed
- Do not collapse the problem into a solution at intake stage
