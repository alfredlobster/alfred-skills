# Tie Break And Escalation

## Goal

Choose the next skill that best resolves what remains after the decision, not simply the next item in a fixed chain.

## Preferred Next Skill Logic

### Use `study-plan-generator` when:
- a lead option is clear enough to execute
- sequencing, milestones, dependencies, and work breakdown are now the main need
- the decision is made and the problem shifts to operational planning

### Use `experiment-designer` when:
- the ranking depends on a better discriminating experiment
- the recommended option is still too abstract to execute
- additional test design would reduce the main decision risk

### Use `critic-reviewer` when:
- the ranking still rests on fragile assumptions
- hidden confounders, feasibility risk, or reasoning quality remain the main blocker
- critique would likely change the recommendation materially

### Use `hypothesis-generator` when:
- the option set is conceptually thin or missing plausible alternatives
- all current options are weak
- the real need is expanding or reframing the candidate set

## Recommended Next Action

The `recommended_next_action` field should:
- be executable in one next step
- point to the main unresolved blocker or execution move
- say what artifact should be produced next

Good examples:
- convert O2 into a 6-week study plan with milestones, decision gates, and required resources
- redesign the top-ranked experiment to include a readout that separates O1 from O2
- run a deeper critique on O1 focused on operational confounders and measurement validity
- generate two additional alternatives that could satisfy the same objective under tighter budget limits
