---
name: experiment-designer
description: design scientific experiments from a structured research brief or hypothesis handoff. use when chatgpt needs to turn hypotheses, open questions, papers, notes, problem statements, or structured metadata into a rigorous experimental plan with objectives, variables, controls, readouts, confounders, risks, feasibility notes, and a structured handoff for downstream critique, ranking, or study-planning skills.
---

# Experiment Designer

Turn a research brief, hypothesis handoff, or mixed scientific context into an experiment plan that is explicit about evidence, uncertainty, controls, and discriminating power.

## Workflow

1. Read the provided research brief or hypothesis handoff first.
2. Detect whether the request contains one primary hypothesis, multiple competing hypotheses, or only exploratory directions.
3. Separate facts, user assertions, and inferences before designing experiments. Use [references/evidence-and-decision-rules.md](references/evidence-and-decision-rules.md) when provenance or confidence is unclear.
4. Choose the design depth:
   - Use a compact design when the user asks for speed or a lightweight plan.
   - Use the default design when the user asks for a normal experimental plan.
   - Use a rigorous design when risk, cost, ethics, safety, or ambiguity is high.
5. Produce a human-readable experimental plan using [references/experiment-plan-template.md](references/experiment-plan-template.md).
6. End with a structured YAML handoff payload that downstream skills can consume deterministically.
7. Recommend the next skill to run.

## Decision Rules

- Prefer experiments that discriminate among competing hypotheses instead of merely generating more data.
- State the decision each experiment is meant to enable.
- Do not silently convert low-confidence assumptions into fixed design facts.
- Mark all design elements as one of: established, assumed, inferred, unknown.
- If key design information is missing, ask only the minimum number of high-value questions unless the user explicitly wants a fast draft.
- When external sources are available and enabled, use them, but label provenance clearly.
- When the user supplies a structured handoff payload, treat it as the primary source of structure and use surrounding prose only for nuance.

## Planning Heuristics

- Prefer a small number of high-information experiments over a long unranked list.
- Include positive controls, negative controls, and baseline or reference conditions whenever relevant.
- Distinguish exploratory from confirmatory work.
- Surface practical constraints early: sample availability, throughput, instrumentation, time, budget, reproducibility, and safety.
- Explicitly call out likely confounders, failure modes, and measurement limitations.
- When multiple experiments are proposed, order them by information gain and feasibility.

## Output Requirements

Produce two sections in this order:

1. **Experimental Plan**
2. **Handoff Payload**

Always use the structure in [references/experiment-plan-template.md](references/experiment-plan-template.md).

## References

- Use [references/experiment-plan-template.md](references/experiment-plan-template.md) for the required plan structure and YAML schema.
- Use [references/evidence-and-decision-rules.md](references/evidence-and-decision-rules.md) for provenance, confidence, and experiment-selection rules.
- Use [references/experiment-design-patterns.md](references/experiment-design-patterns.md) for compact, default, and rigorous design modes.
- Use [references/escalation-and-next-skills.md](references/escalation-and-next-skills.md) to decide the next skill and preserve handoff compatibility.
