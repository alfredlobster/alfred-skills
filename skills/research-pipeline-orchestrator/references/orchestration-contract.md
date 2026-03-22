# Orchestration Contract

## State Machine
- INIT -> STAGE1 -> STAGE2 -> STAGE3 -> STAGE4 -> STAGE5 -> STAGE6 -> COMPLETE
- Any stage parse failure: PARSE_FAIL(stage)
- Any execution failure: EXEC_FAIL(stage)

## Per-Stage Required Artifact
1: research_brief_handoff
2: hypothesis_portfolio_handoff
3: experiment_design_handoff
4: critique_review_handoff
5: ranking_decision_handoff
6: study_plan_handoff

## Stage Result Record
For each stage emit:
- stage_name
- status: OK|WARN|FAIL
- artifact_present: yes|no
- notes: short

## Final Verdict Logic
- PASS: all stages OK or at most one WARN, no FAIL
- PARTIAL: >=1 WARN and no hard-stop FAIL
- FAIL: hard-stop due to parse or execution failure

## Minimal Final Output
- Final verdict
- Recommended option/path (from stage 5/6)
- Immediate next actions (from stage 6)
