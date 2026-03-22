# Decision Frameworks

## Decision Modes

### Quick
Use for fast prioritization.

Behavior:
- rank the top 2 to 4 options only
- use a minimal criteria set
- focus on the most decision-relevant tradeoffs
- keep the rationale short and actionable

### Balanced
Use by default.

Behavior:
- compare all distinct credible options
- use a compact but explicit criteria set
- state the main tradeoffs and uncertainty drivers
- provide a recommendation plus at least one reversal trigger

### Rigorous
Use for high-stakes or high-commitment decisions.

Behavior:
- apply hard gates before soft ranking
- separate must-have criteria from preference criteria
- include sensitivity and reversal conditions explicitly
- show why the top option wins and why the runners-up lose
- highlight information that would most change the decision

## Default Criteria Set

Use only the criteria that matter for the case. Default candidates:
- evidence_strength
- expected_value
- feasibility
- speed
- learning_value
- resource_efficiency
- strategic_fit

Do not use all criteria just because they exist.

## Weighting Rules

- If the user provides weights or priorities, use them.
- If the user gives only qualitative priorities, translate them into `high`, `medium`, `low`, or `unknown`.
- If no weighting is given, infer a minimal weighting logic and say so plainly.
- Do not fabricate quantitative precision.

## Gating Rules

Before ranking, check for gating constraints such as:
- safety or ethics blockers
- time or budget hard limits
- missing critical resources or instrumentation
- evidence too weak for the implied commitment

If an option fails a hard gate, do not let strong soft scores hide that fact.

## Good Ranking Patterns

Prefer reasoning like:
- O2 is slower than O1 but has higher learning value and lower interpretive risk, so it ranks first under a learning-driven objective
- O3 is promising but fails the current throughput constraint, so it is deferred rather than ranked highly
- O1 and O2 are close, but O2 wins because the critique identified a major confounder in O1 that is not yet resolved

Avoid reasoning like:
- O1 scored 87 and O2 scored 82 without a visible method
- O3 feels best overall
- everything is a tradeoff with no recommendation

## Tie-Break Rules

When options are close, break ties using:
1. hard constraints
2. evidence strength
3. discriminating learning value
4. reversibility of the decision
5. implementation feasibility under stated constraints

## Reversal Rules

For every recommendation, state what new information would most likely change the ranking.
