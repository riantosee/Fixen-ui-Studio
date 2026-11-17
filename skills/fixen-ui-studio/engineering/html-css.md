# HTML and CSS Guidance

## Structure and semantics
- Use landmarks (`header`, `nav`, `main`, `footer`), one `h1`, and headings in order. Lists for lists, `button` for actions, `a href` for navigation, `label` tied to every input.
- Never put `role` or click handlers on a `div` or `span` to fake a control; it drops out of keyboard order.
- Decorative SVG gets `aria-hidden="true"`. Meaningful SVG gets `role="img"` and an accessible name.

## Tokens
Define shared decisions once and consume them everywhere:
```css
:root {
  --ground: #f6eedc; --ink: #2b1a0f; --accent: #a8480f;
  --space-1: .5rem; --space-2: 1rem; --space-3: 2rem;
  --measure: 65ch;
  --step-0: clamp(1rem, .95rem + .3vw, 1.125rem);
  --step-3: clamp(2rem, 1.4rem + 3vw, 4rem);
}
```
Offer a dark scheme only when the product wants one: redefine the same variables under `@media (prefers-color-scheme: dark)` and set `color-scheme`.

## Layout
- Grid and flexbox for structure. Absolute positioning only for overlays and badges.
- Flexible columns: `grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr))`.
- Flex children that hold text need `min-width: 0` to avoid overflow. Long words: `overflow-wrap: anywhere` where needed.
- Limit reading width (`max-width: var(--measure)`). Use `clamp()` for type and spacing before adding breakpoints; add a media or container query only where content breaks.
- Prefer logical properties (`margin-inline`, `padding-block`) when the product may be localized (`systems/localization.md`).

## Media and loading
- Give images `width` and `height` (or `aspect-ratio`) to prevent layout shift; `object-fit` for crops; `loading="lazy"` below the fold; `alt` that states purpose, empty `alt=""` when decorative.
- Fonts: limit families and weights, set `font-display: swap`, and define a real fallback stack. Do not rely on a font that may not load.
- Include `<meta name="viewport" content="width=device-width, initial-scale=1">`. For edge-to-edge mobile pages respect `env(safe-area-inset-*)`.

## Interaction
- `:focus-visible` outline with at least 3:1 contrast against its surroundings. Do not remove outlines without replacing them.
- Hover is never the only way to reveal something.
- Wrap motion in `@media (prefers-reduced-motion: no-preference)` or provide a reduced alternative. Animate `transform` and `opacity`, not layout properties.
- Targets at least 44 × 44 px for primary touch actions (WCAG 2.2 sets a 24 px minimum).

## Hygiene
Scope selectors to components, avoid `!important`, avoid global resets that alter unrelated pages, and check stacking contexts (`z-index`, `position`, `transform`) before adding overlays. Keep CSS organized per the project's convention.
