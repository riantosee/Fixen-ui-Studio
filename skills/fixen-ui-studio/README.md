# Fixen UI Studio

**Professional AI Design & Engineering Skill — Experimental Hybrid Edition**

Fixen UI Studio helps an AI agent work through the full interface lifecycle: understand the product, choose a fitting art direction, specify the design, implement it, inspect the rendered result, and refine it.

## What makes it different

- Design-first reasoning followed by implementation.
- Anti-generic direction selection rather than one repeated template.
- UX, accessibility, responsive behavior, and interaction states are part of the brief.
- Autonomous visual refinement when browser/screenshot tools are available.
- Honest QA: unavailable tools and unverified claims are explicitly reported.
- Real-image sourcing: search the web, compare composition and crop, check the individual source, and distinguish references from assets actually integrated into the UI.
- A benchmark suite for repeatable evaluation across different agents.

## Install

Current repository: [riantosee/Fixen-ui-Studio](https://github.com/riantosee/Fixen-ui-Studio). Read the canonical [contribution guide](https://github.com/riantosee/Fixen-ui-Studio/blob/main/CONTRIBUTING.md), [Security Policy](https://github.com/riantosee/Fixen-ui-Studio/blob/main/SECURITY.md), and [Code of Conduct](https://github.com/riantosee/Fixen-ui-Studio/blob/main/CODE_OF_CONDUCT.md) before participating. This standalone folder retains the complete MIT License. Security/community policies govern conduct and do not narrow MIT's commercial-use or redistribution permissions.

Copy the `fixen-ui-studio/` directory into the skill directory supported by your agent. The exact installation path differs by agent. The skill uses the open Agent Skills `SKILL.md` convention and avoids requiring a specific model vendor.

## Use

Ask naturally, for example:

- "Design a premium editorial landing page for a boutique architecture studio."
- "Redesign this dashboard for dense operational workflows."
- "Audit the visual hierarchy and accessibility of this page."
- "Create a reusable design system for this product."
- "Implement the approved blueprint in the existing Next.js project."
- "Use $fixen-ui-studio to find three real photos for a tropical architecture article. Show source links, usage terms, and a recommendation; do not build a page yet."
- "Cari mentahan gambar untuk hero landing page ini. Pilih yang cocok, catat sumbernya, lalu integrasikan dan cek crop desktop/mobile."

Slash commands are not required. The agent should infer the requested mode from intent.

## Languages

English is the primary repository documentation language. Translated quick starts are linked from the [main README](https://github.com/riantosee/Fixen-ui-Studio#readme). Communicate in the user's requested language and preserve the product's existing language strategy. For a new product without language direction, use English and state the assumption.

For multilingual UI, read [localization guidance](systems/localization.md). It covers locale formatting, message catalogs, text expansion, fonts, accessible language selection, and RTL. Use [localization scenarios](benchmarks/localization-cases.md) for relevant evaluation; they are briefs, not recorded passing tests. The skill installs no translation engine and does not guarantee all-language quality.

## Tool capabilities

The skill remains useful without external tools. Browser automation, screenshot capture, image generation, Figma integrations, and code execution improve the result but are optional. The agent must never claim to have used a tool it does not have.

Image sourcing uses whichever image-search, web-search, browser, or download tools the agent actually has. It installs no browser and supplies no search service or API key. Image search, source verification, visual review, download, and UI integration are separate steps with separate completion status. A reference-only search does not authorize purchasing assets or publishing a page.

## Repository map

- `core/` orchestration and context inspection
- `design/` creative direction and UX
- `systems/` tokens, components, responsive design, accessibility
- `engineering/` implementation guidance
- `quality/` QA, scoring, refinement
- `benchmarks/` test briefs and scoring rubric
- `templates/` reusable deliverable formats
- `agents/` optional agent metadata

## Benchmark

Start with `benchmarks/benchmark-suite.md`. Score outputs using `benchmarks/scoring-rubric.md`. Compare agents only when they receive equivalent prompts, context, tools, viewport sizes, and time budgets.

## Version

v1.3.0 — restores the localization guidance and evaluation briefs referenced by earlier docs, adds regional/local-business guidance, a copy-versus-facts rule, host-format and static-only QA guidance, and fuller HTML/React/Tailwind/style references; v1.2.1 — adds English-first multilingual documentation and conditional UI localization guidance; v1.2.0 rebrands the skill to Fixen UI Studio, adds repository safety/contribution guidance at the root project, and retains optional browser/web image sourcing, candidate and credit records, crop/integration checks, and image-sourcing test cases. Benchmark scores are not pre-claimed; run the suite to establish a baseline.


