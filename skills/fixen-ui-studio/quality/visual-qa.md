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

## Static-only checks (when nothing can be rendered)
Many hosts cannot render or screenshot. Do not stop at "not verified"; run these from the source and report them as static-only, never as a visual pass.
- **Contrast:** compute ratios from the actual token values (relative luminance per WCAG). Body text 4.5:1; large text and UI boundaries 3:1. Check text on every colored surface, including button labels and text over images.
- **Overflow risks:** fixed widths, `white-space: nowrap`, long unbroken strings, missing `min-width: 0` on flex or grid children, wide tables without a scroll container.
- **Responsive:** fluid sizing (`clamp`, `minmax`, `auto-fit`) and wrapping at 390 px; tap targets 44 px; no hover-only content.
- **Semantics:** one `h1`, heading order, landmarks, labels, accessible names for icon controls, alt text, `lang`.
- **Focus and motion:** visible `:focus-visible`, tab order follows reading order, reduced-motion handled.
- **Consistency:** every color, size, and radius used comes from the tokens; states exist for controls.
- **Content integrity:** list every placeholder still in the page and every business fact that was not supplied.
If code execution is available, a short script can compute contrast ratios from the token list instead of estimating by eye.

