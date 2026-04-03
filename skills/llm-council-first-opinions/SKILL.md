---
name: llm-council-first-opinions
description: Run the first-opinion stage of an LLM Council by sending the same normalized task to all selected council models independently. Use when the intake artifact is already prepared and you need parallel first-pass answers before any peer review or ranking occurs.
---

# LLM Council First Opinions

Generate independent first-pass answers from all council models.

## Purpose
Reproduce Stage 1 of Karpathy's design: parallel, independent answers before review begins.

## Input
- one intake artifact from `llm-council-intake`

## Output boundary
This stage outputs only first-opinion records.
It must not:
- anonymize responses yet
- review or rank them
- synthesize a final answer

## Required output per model
- `model`
- `response`
- `status`
- `error` (if failed)

## Rules
- Every model receives the same task
- Models do not see each other's answers at this stage
- Keep successful responses even if some models fail
- Preserve response text exactly for downstream anonymized review
