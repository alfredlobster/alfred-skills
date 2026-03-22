---
name: research-pipeline-reporter
description: Build a single clean markdown report from a full multi-skill research run (research-intake-brief -> hypothesis-generator -> experiment-designer -> critic-reviewer -> ranking-and-decision -> study-plan-generator). Use when outputs exist across stages and the user wants one concise executive + technical report with final verdict, ranked decision, study plan, risks, and next actions.
---

# Research Pipeline Reporter

Create one combined markdown report from a completed 6-step research pipeline run.

## Required Inputs
- Stage outputs or YAML payloads from:
  1. research-intake-brief
  2. hypothesis-generator
  3. experiment-designer
  4. critic-reviewer
  5. ranking-and-decision
  6. study-plan-generator

If one stage is missing, explicitly mark it as missing and continue.

## Output Contract
- Produce one markdown file/report with this exact top structure:
  1. Title
  2. Run Summary (status, date, run mode)
  3. Initial Question
  4. Stage-by-Stage Results (1-6)
  5. Final Decision
  6. Execution Plan Snapshot
  7. Risks and Watchpoints
  8. Immediate Next Actions
  9. Appendix: Consolidated YAML Index

## Rules
- Keep conclusions auditable: tie each conclusion to stage output.
- Do not add new scientific claims beyond provided stage content.
- Prefer crisp bullets over long prose.
- Include explicit verdict line: `Pipeline verdict: PASS|PARTIAL|FAIL`.
- Include explicit recommendation confidence: High|Medium|Low.

## Template
Read `references/combined-report-template.md` and fill it deterministically.
