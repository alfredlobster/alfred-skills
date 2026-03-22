# Handoff to Next Skills

## Purpose

Choose the next skill based on the main bottleneck after hypothesis generation.

## Recommended next skills

### experiment-designer

Use when one or more hypotheses are coherent enough to test and the next need is protocol design, controls, measurements, feasibility planning, or sequencing.

Choose this when:
- at least one hypothesis has medium or high plausibility
- discriminating tests can already be stated in outline form
- the main gap is execution design

### critic-reviewer

Use when the likely failure mode is weak reasoning, confirmation bias, confounding, or overconfidence.

Choose this when:
- most hypotheses depend on fragile assumptions
- the evidence base is thin or conflicted
- the portfolio appears prematurely converged

### ranking-and-decision

Use when multiple credible hypotheses compete and explicit prioritization is the main need.

Choose this when:
- constraints or resource tradeoffs dominate
- the user already has enough ideas but needs a decision
- two or more hypotheses look similarly viable

### study-plan-generator

Use when the user needs a near-term program of work that may include experiments, data collection, and sequencing beyond a single test.

Choose this when:
- the top hypotheses are clear enough to organize into a staged plan
- dependencies and timing matter
- the need is operational planning rather than more ideation

## Default rule

If the portfolio has one or more reasonably testable hypotheses, recommend `experiment-designer`.
If the portfolio feels fragile, recommend `critic-reviewer`.
If the main problem is prioritization under constraints, recommend `ranking-and-decision`.
