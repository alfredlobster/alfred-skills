# Planning Modes

## Lean

Use when the user mainly needs the next few moves.

Behavior:
- produce a short stage sequence
- keep only the most important dependencies and gates
- focus on immediate learning value
- avoid long-range branching unless critical

## Standard

Use by default for most requests.

Behavior:
- produce a staged plan with prerequisites, activities, outputs, and checkpoints
- include the main dependencies and fallback branches
- distinguish blocking work from parallelizable work
- expose enough detail for handoff into execution or deeper design

## Rigorous

Use when the plan is expensive, high risk, or cross-functional.

Behavior:
- make stage entry and exit conditions explicit
- add stronger failure, stop, and review triggers
- expose operational, evidentiary, and governance dependencies
- show where replanning should occur instead of assuming linear progress

## Override Rules

If the user specifies a mode, honor it.
If the user asks for a roadmap, increase breadth but keep uncertainty explicit.
If the user asks only for the first step, compress to lean mode unless the situation is clearly fragile.
