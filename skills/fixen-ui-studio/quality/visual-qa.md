# Visual QA Protocol

## Preconditions
Use the available project run command and browser/rendering tool. Never assume a browser tool exists.

## Viewports
At minimum, inspect:
- Wide desktop (for example 1440 × 900)
- Narrow mobile (for example 390 × 844)

Add tablet or other target sizes when the layout requires them. These are test viewports, not universal breakpoints.

## Inspection checklist
- First-screen hierarchy and primary action
- Alignment, spacing rhythm, and grid consistency
- Typography scale, line length, wrapping, and legibility
- Color contrast and semantic status clarity
- Image crop, resolution, and asset consistency
- Overflow, clipping, and responsive reflow
- Navigation and interaction behavior
- Empty/loading/error/success states
- Keyboard focus and reduced-motion behavior
- Visual consistency across related pages

## Defect priority
- P0: blocks core task, broken layout, inaccessible critical control.
- P1: major hierarchy, responsiveness, or interaction defect.
- P2: noticeable inconsistency or polish issue.
- P3: minor cosmetic issue.

## Evidence
Record the viewport, route, observed defect, severity, and whether it was fixed. If no screenshot/browser tool is available, label the review static-only.

