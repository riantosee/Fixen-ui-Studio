# Validation notes — Fixen UI Studio

This document distinguishes package checks from UI behavior and language review. Passing structural validation does not establish universal quality, WCAG conformance, translation accuracy, or benchmark superiority.

## Package checks

`scripts/validate.py` checks frontmatter, naming, invocation metadata, unfinished TODO markers, package boundaries, entrypoint and nested skill references, version/changelog consistency, symlinks, repository YAML syntax, and local Markdown links. The GitHub Actions workflow runs this validator and nine validator regression tests on main-branch pushes and pull requests.

The regression tests cover a minimal valid package, incorrect invocation, missing and escaping references, and valid/broken Markdown links. These are validator tests, not UI behavior tests. Validation dependencies are installed in a project-local virtual environment. The installable skill itself contains Markdown/YAML guidance; repository validator scripts are contributor tooling.

## v1.3.0 scope

This update restores the localization guidance and briefs that earlier documents referenced but the repository lacked, adds regional/local-business guidance, a copy-versus-facts rule, static-only QA checks, and fuller engineering and style references. It builds on 1.2.1, which made English the primary README and contribution language and added quick starts in Indonesian, Spanish, Brazilian Portuguese, and Simplified Chinese. The blueprint records language/locale decisions when relevant. English documentation does not authorize translating an existing product or changing its currency.

Release preparation checks include the Codex quick validator, the repository validator and local links, the nine regression tests, and ZIP integrity with byte-for-byte comparison against tracked source. Actual publication and CI outcomes are reported separately in the release handoff rather than assumed here.

The translations are authored documentation. They have not received an independent review by a qualified speaker of each language. The localization scenarios are briefs, not executed browser tests. No claim is made that all target scripts, locale formats, RTL interactions, or runtime locale switching have passed QA.

## Earlier exercises and remaining work

Before the public rebrand, the skill was exercised on a local logistics dashboard and a shortlist-only web image task. Those were usage examples, not reproducible CI tests or an independent no-skill comparison.

Further evaluation can cover full image acquisition/integration, audit-only and redesign behavior, existing-project changes, repeated equivalent benchmark cases, accessibility and cross-browser review, and the relevant localization scenarios under recorded host conditions. Report only the cases actually run.

## Security boundary

The repository rejects unauthorized exploitation and unsafe contributions. MIT permits commercial use, modification, redistribution, and sale; project security and community policies govern conduct and reporting without changing those permissions. The skill cannot sandbox an agent or guarantee prompt-injection resistance. Hosts must enforce permissions and credential protection.
