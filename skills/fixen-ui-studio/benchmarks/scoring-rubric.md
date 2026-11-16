# Design Arena Scoring Rubric

This is the canonical rubric for review and benchmarking. Score assessed dimensions from 1–5 and normalize them to a 100-point maximum. Do not multiply raw ratings by weights and report that sum as a score out of 100.

| Dimension | Weight | What reviewers assess |
|---|---:|---|
| Task clarity and UX | 20 | Can the target user complete the primary task? |
| Visual hierarchy and composition | 15 | Is attention guided intentionally? |
| Distinctiveness and product fit | 15 | Does the design feel specific rather than templated? |
| Typography and readability | 10 | Is type hierarchy clear and legible? |
| Responsive quality | 10 | Does it adapt without losing task quality? |
| Interaction and states | 10 | Are controls and system states coherent? |
| Accessibility | 10 | Semantics, keyboard, contrast, labels, motion |
| Implementation quality | 10 | Maintainability, correctness, and project fit |

## Anchors
1 — Broken or seriously inadequate.
2 — Major weaknesses; task completion or clarity suffers.
3 — Adequate; usable with visible shortcomings.
4 — Strong; minor issues only.
5 — Excellent; clear evidence of thoughtful, robust execution.

Reviewers must cite concrete evidence (route, viewport, element, behavior, screenshot). Mark not assessable rather than guessing. Report both weighted score and evidence coverage.

## Calculation

For assessed dimensions only:

```text
score = 100 * sum(weight * rating / 5) / sum(assessed weights)
evidence coverage = sum(assessed weights) / 100 * 100%
```

All ratings 5 yield 100; all ratings 3 yield 60; all ratings 1 yield 20. This scale has a minimum of 20 when evidence exists; it is not a 0–5 scale. Exclude N/A dimensions from both score sums, but disclose them and reduced coverage. If no dimension is assessable, report no score, with 0% coverage.

Example: UX weight 20 rated 4 and hierarchy weight 15 rated 3, all others N/A: `100 * (20*4/5 + 15*3/5) / 35 = 71.4`, coverage 35%. Do not compare this low-coverage result directly with a fully assessed score.

Keep functional acceptance separate: a broken primary action, unauthorized mutation, or critical inaccessible control fails the relevant case even if the visual score is high. Scores do not establish production readiness or WCAG conformance.

