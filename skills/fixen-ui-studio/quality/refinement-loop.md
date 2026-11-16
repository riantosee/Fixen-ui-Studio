# Autonomous Refinement Loop

1. Compare rendered output against the Design Blueprint and acceptance criteria.
2. List defects with evidence and severity.
3. Select the smallest set of changes with the greatest user impact.
4. Implement those changes without destabilizing unrelated areas.
5. Re-render the same viewport and state.
6. Confirm whether the targeted defect improved and check for regressions.
7. Repeat up to three focused cycles by default.

Stop when:
- Critical and major defects are resolved,
- acceptance criteria are met,
- improvements become subjective or low impact,
- tool access or time prevents reliable verification.

If the design still has known issues, report them. Never silently lower acceptance criteria.

