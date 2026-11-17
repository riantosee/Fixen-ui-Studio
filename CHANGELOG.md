# Changelog

## 1.3.0 — 2026-11-17

- Added the localization guidance (`systems/localization.md`) and five evaluation briefs (`benchmarks/localization-cases.md`) that earlier docs already referenced but the repository did not contain.
- Added the locale and content-facts section to the design blueprint that the 1.2.1 notes described.
- Added `design/regional-context.md`: local-business page pattern and an Indonesia worked example (WhatsApp links, Rupiah format, payment cues, time zones, register, mobile-first).
- Added a copy-versus-facts rule: never invent business facts; use visible placeholders and list them in the handoff.
- Added host-format guidance for hosts that provide their own design, canvas, or artifact format.
- Added static-only QA checks so environments without rendering still get contrast, overflow, semantics, and placeholder checks, labeled as static-only.
- Expanded the HTML/CSS, React/Next.js, and Tailwind guides and the style catalog (direction recipes, palette construction, type pairing).
- Added benchmark case B21 (local food-and-drink shop landing page).
- Validator now checks nested skill references and that the skill version matches the latest changelog entry; added three regression tests.

## 1.2.1 — 2026-11-17

- Made English the primary README and contribution-guide language.
- Added linked quick starts in Indonesian, Spanish, Brazilian Portuguese, and Simplified Chinese.
- Added conditional UI localization guidance for message catalogs, locale formats, language selection, font coverage, and RTL layouts.
- Preserved existing product languages; English is a stated default only for new products with no language direction.
- Added locale fields to the design blueprint and five localization evaluation briefs without claiming they passed browser QA.
- Documented translation contributions and language-review limitations; retained MIT and project security policies.

## 1.2.0 — 2026-11-16

- Rebranded the installable skill from Fixenzo UI Studio to Fixen UI Studio.
- Added root repository documentation, MIT license, contribution guidance, Code of Conduct, Security Policy, templates, and CI validation.
- Added explicit responsible-use boundaries and private vulnerability-reporting guidance.
- Added the optional real-image sourcing workflow, asset register, and asset-sourcing benchmark cases.
- Updated the Codex invocation identifier to `$fixen-ui-studio`.
- Restored complete MIT disclaimer text in the distributable package, consolidated the scoring formula into one rubric, and linked previously undiscoverable references.

## 1.1.0

- Added optional web image sourcing, candidate comparison, source-term checks, asset records, and crop verification guidance.

## 1.0.0

- Initial experimental Fixenzo UI Studio skill package.
