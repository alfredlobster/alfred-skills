# Handoff to Next Skills

## Goal

Choose the next skill that best resolves the critique, not simply the next item in a linear chain.

## Preferred Next Skill Logic

### Use `hypothesis-generator` when:
- the conceptual framing is weak
- rival explanations are missing
- hypotheses are not distinct enough to justify testing
- the problem statement itself likely needs reframing

### Use `experiment-designer` when:
- the main weaknesses are about controls, measurements, sequencing, or feasibility
- the hypotheses are reasonable but the test plan is not yet discriminating enough
- operational confounders dominate the risk profile

### Use `ranking-and-decision` when:
- several options remain viable after critique
- the user needs explicit tradeoff handling under constraints
- the critique clarified priorities more than it invalidated them

### Use `study-plan-generator` when:
- the remaining issues are manageable
- the user is ready to translate the reviewed artifact into an execution program
- work breakdown, sequencing, and milestones are now more important than conceptual debate

## Recommended Next Action

The `recommended_next_action` field should:
- point to the most important unresolved item
- be executable in one next step
- name what must be changed, added, or decided

Good examples:
- revise the top experiment to add a negative control and a measurement that separates H1 from H2
- regenerate hypotheses with explicit alternative mechanisms for the unexplained observation
- rank the remaining options against cost, speed, evidence strength, and expected learning value
- convert the reviewed experiment portfolio into a 6-week study plan with milestones and decision gates
