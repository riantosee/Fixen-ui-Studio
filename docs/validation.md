# Validation notes — Fixen UI Studio 1.2.0

This document records package checks for the first public rebrand release. It is not a claim of universal quality, tool availability, WCAG conformance, or benchmark superiority.

## Package checks

- `scripts/validate.py` checks frontmatter, name, description length, default prompt, unfinished TODO markers, package boundaries, entrypoint references, symlinks, repository YAML syntax, and local Markdown links.
- GitHub Actions runs the same validator with Python and PyYAML on pushes and pull requests.
- The package contains no executable helper besides the read-only validator. The skill itself is Markdown/YAML guidance.
- The current release keeps the original image-sourcing guidance and adds root-level policies/documentation.

Local release checks passed: the bundled Codex `quick_validate.py` with PyYAML available, the repository validator (25 entrypoint references), and six validator regression tests. The tests cover a minimal valid package, wrong invocation, missing reference, an escaping reference, and valid/broken Markdown links. These are package/validator checks, not UI behavior benchmarks. They run in a project-local virtual environment rather than changing global Python packages.

## Scope

The public repository has no baseline commit at the time of this release preparation. The release therefore provides a complete initial tree rather than a delta against prior GitHub history. Changes were prepared from the local v1.1.0 package and rebranded to the v1.2.0 identifier.

The included skill was previously exercised on a local logistics dashboard and a shortlist-only web image sourcing task. Those are usage examples, not reproducible CI tests. The following remain to be run by contributors under their own tool conditions:

- full image acquisition and desktop/mobile integration;
- audit-only, redesign, and existing-project implementation runs;
- repeated benchmark cases and an equivalent no-skill baseline;
- full accessibility audit and cross-browser review;
- GitHub Actions execution after the first push.

## Security boundary

The repository prohibits unauthorized exploitation and unsafe contributions. MIT still allows commercial use, modification, redistribution, and sale of copies; project safety policies govern conduct and reporting, not copyright permissions. The skill cannot itself sandbox an agent or guarantee prompt-injection resistance, so hosts must enforce permissions and review.
