# Intake Modes

## Purpose

Select the lightest mode that still produces a reliable research brief.

## Fast Mode

Use when the provided material already contains most of the following:
- a clear problem statement
- an objective or decision to support
- some evidence or contextual material
- at least rough constraints or success criteria

### Behavior

- Ask zero to two questions at most.
- Infer minor structure from the supplied material.
- Synthesize quickly.
- Prefer action over interrogation.

### Suitable cases

- a well-framed problem statement
- uploaded papers with a clear user goal
- a detailed set of notes from a prior discussion

## Guided Mode

Use when the problem is plausible but incompletely framed.

### Behavior

- Ask a focused set of three to seven questions.
- Group related questions together.
- Stop asking once the brief is good enough to support the next skill.
- Do not try to eliminate every uncertainty.

### Focus areas

Ask about:
1. the actual research goal
2. success criteria
3. practical constraints
4. the evidence already available
5. key unknowns

### Suitable cases

- the user has a rough idea but not a complete framing
- several sources are present but conflict or overlap
- the user wants a strong brief without a long challenge process

## Rigorous Mode

Use when ambiguity, cost, risk, or conceptual confusion is high.

### Behavior

- Challenge the framing before writing the brief.
- Surface hidden assumptions and potential category errors.
- Test whether the stated problem is the right problem.
- Ask up to ten questions if needed, but keep them decision-relevant.

### Challenge prompts

Use prompts like:
- What decision will this research inform?
- What evidence would falsify the current framing?
- What is being assumed but not yet measured?
- What would make this question irrelevant or poorly posed?
- Which constraints are real versus habitual?

### Suitable cases

- costly or high-stakes experimental work
- vague requests with heavy implied assumptions
- situations where a more precise question could materially change the program

## Auto-selection Rule

Default to auto-selection.

- choose fast if the brief can be drafted immediately with only small gaps
- choose guided if the work benefits from a compact interview
- choose rigorous if the main risk is poor framing rather than missing detail

State the selected mode in the YAML payload.
