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

v1.2.0 — rebrands the skill to Fixen UI Studio, adds repository safety/contribution guidance at the root project, and retains optional browser/web image sourcing, candidate and credit records, crop/integration checks, and image-sourcing test cases. Benchmark scores are not pre-claimed; run the suite to establish a baseline.


