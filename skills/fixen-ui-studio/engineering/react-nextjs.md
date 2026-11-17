# React and Next.js Guidance

## Inspect first
Read `package.json`, the lockfile, `next.config.*`, and the folder layout. Identify the Next.js and React versions, App Router (`app/`) vs Pages Router (`pages/`), the styling solution, the component library, the test runner, and any i18n setup. Follow what is there; do not migrate routers or styling as a side effect.

## Component boundaries
- In the App Router, components are server components by default. Add `"use client"` only for state, effects, event handlers, or browser APIs, and push it as far down the tree as practical.
- Keep data fetching, state, and presentation separate. Pass plain serializable props across the server/client boundary.
- Keep components small and named for their job. Do not abstract a single-use block into a configurable component.

## Framework facilities
- Use the framework's font loader (`next/font`), image component (`next/image`: set `width`/`height` or `fill` with `sizes`), `Link` for internal navigation, and the metadata API for titles and descriptions, if the project already uses them.
- Use route-level `loading`, `error`, and `not-found` files for those states when the router supports them.
- Forms: use real `form`, `label`, and `button type`. Show field-level errors tied to inputs (`aria-describedby`) and a success state.

## Pitfalls
- Hydration mismatches: do not render `Date.now()`, random values, or locale-dependent formats differently on server and client. Fix a time zone or format on both sides.
- Do not read `window` or `document` during render; use effects or client-only components.
- Stable `key`s from data ids, not array indexes, for reorderable lists.
- Avoid effect-driven state that can be computed during render.
- Dialogs, menus, and popovers: use the project's existing primitive or native `<dialog>`; verify focus trap, Escape to close, and focus return.

## Verification
Run the project's lint, typecheck, build, and relevant tests. A passing build is not proof of visual quality; follow `quality/visual-qa.md`.
