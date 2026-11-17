# Tailwind CSS Guidance

## Inspect first
Determine the Tailwind major version and how it is configured before writing classes.
- v3 style: `tailwind.config.js|ts` with `theme.extend`, `content` globs, and `@tailwind` directives.
- v4 style: CSS-first setup (`@import "tailwindcss"`) with design tokens declared in an `@theme` block.
Do not mix the two models, and do not use utilities or tokens the installed version or config does not provide.

## Tokens
- Put palette, type scale, spacing, and radii in the project's theme once; use semantic names (`--color-ground`, `--color-ink`, `--color-accent`) instead of scattering arbitrary hex values.
- Arbitrary values (`w-[37px]`) are for genuine one-offs. Repeated ones belong in the theme.

## Composition
- Long class strings are acceptable for one-off markup. When a pattern repeats, extract a component (preferred) or a small class helper the project already uses (`cn`, `clsx`, `cva`). Do not introduce a new helper library without need.
- Keep a consistent class order if the project uses a formatter plugin; run it.
- Mobile-first: unprefixed classes are the base, then `sm:`/`md:`/`lg:` add. Avoid conflicting utilities on one element.

## States and accessibility
- Use `focus-visible:` for keyboard focus rings, `disabled:`, `aria-*`/`data-*` variants where available, and `motion-reduce:` or `motion-safe:` for animation.
- Use `min-w-0` on flex/grid children holding text, and `break-words` or `text-balance` where wrapping needs help.
- Container queries are built into v4; in v3 they need a plugin. Check before using them.

## Restraint
Prefer the project's component library and tokens over adding another UI kit. Keep default Tailwind look from becoming the design: set your own palette, type, and radii.
