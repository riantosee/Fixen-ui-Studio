# Fixen UI Studio

**Design with product context. Build working interfaces. Verify what you ship.**

English · [Bahasa Indonesia](docs/README.id.md) · [Español](docs/README.es.md) · [Português (Brasil)](docs/README.pt-BR.md) · [简体中文](docs/README.zh-CN.md)

[MIT License](LICENSE) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md) · [Releases](https://github.com/riantosee/Fixen-ui-Studio/releases)

Fixen UI Studio is an open source Agent Skill for designing, building, reviewing, and refining web interfaces. It connects product discovery, art direction, UX, frontend implementation, visual QA, and optional real-image sourcing in one adaptable workflow.

**v1.2.1 · Experimental.** Previously named Fixenzo UI Studio. Invoke it with `$fixen-ui-studio`. This is a Markdown/YAML instruction package; the host agent supplies its model, tools, and permissions.

## What it helps you do

| Task | Approach |
| --- | --- |
| New pages and dashboards | Understand the primary task, choose an art direction, create a proportionate blueprint, then implement. |
| Existing interfaces | Inspect the repository and preserve its framework, components, and conventions. |
| Audits and design systems | Prioritize evidence-based findings or define reusable foundations and component states. |
| Real-image sourcing | Compare actual candidates, inspect sources and usage terms, record credits, and verify crops when integrated. |
| Multilingual interfaces | Preserve the product's language strategy; account for locale formats, text expansion, font coverage, and bidirectional layout. |
| Visual refinement | Render and inspect relevant states when tools are available; report the checks actually performed. |

## Install in Codex

Download `fixen-ui-studio-v1.2.1.zip` from [GitHub Releases](https://github.com/riantosee/Fixen-ui-Studio/releases). Extract the `fixen-ui-studio/` folder into your Codex skills directory so the entrypoint is:

```text
~/.codex/skills/fixen-ui-studio/SKILL.md
```

On Windows, `~` usually means your user profile directory. If you configured `CODEX_HOME`, use its skills directory. Back up any customized installation before replacing it.

Alternatively, clone this repository and copy only `skills/fixen-ui-studio/` into your agent's skills directory. Other hosts may support the `SKILL.md` format, but have not all been tested. When migrating from Fixenzo, use the new identifier and avoid keeping duplicate active copies unnecessarily.

## Try it

```text
Use $fixen-ui-studio to build a dispatch dashboard.
Prioritize delayed deliveries, filters, and clear recovery actions.
Use the existing project stack and synthetic data.
```

```text
Use $fixen-ui-studio to audit this page's hierarchy and accessibility.
Report evidence and actionable findings. Do not edit files.
```

```text
Use $fixen-ui-studio to build an English-first booking UI with Indonesian
and Arabic locales. Reuse the project's i18n system, format prices and
dates per locale, and check mobile layouts and RTL navigation.
```

```text
Use $fixen-ui-studio to shortlist up to three real interior-studio hero
photos: warm, landscape, with space for text on the left. Compare the
actual images, source terms, and crops. Do not download or build yet.
```

## Languages and localization

**English is the primary documentation language.** The linked Indonesian, Spanish, Brazilian Portuguese, and Simplified Chinese READMEs provide translated quick starts. Use the English README and [changelog](CHANGELOG.md) to resolve documentation drift; report discrepancies through a documentation issue or PR.

The agent should communicate in the language requested by the user. Interface content follows the requested product language and the existing repository's locale conventions. For a new product with no language direction, use English and state that assumption. Adding translations should follow the project's existing i18n system; this skill does not install a translation engine or guarantee translation quality in every language.

See [localization guidance](skills/fixen-ui-studio/systems/localization.md) for message structure, language selectors, `lang`/`dir`, locale formatting, and RTL behavior. Coverage depends on the model, fonts, framework, and tools. The translated READMEs are documentation; they are not evidence that every target locale has been browser-tested.

## Image sourcing

Image search is optional. It uses the host's available search and browser tools; the skill supplies no browser, search service, or API key. A shortlist request stops at recommendations. Acquiring assets, integrating them, and checking the rendered result are separate stages.

Use the [image-sourcing guide](skills/fixen-ui-studio/design/asset-sourcing.md) and [asset register](skills/fixen-ui-studio/templates/asset-register.md) to track sources, creators, terms, and verification status. Third-party images retain their own licenses; the project's MIT license does not cover them automatically.

## Repository layout

```text
skills/fixen-ui-studio/
  SKILL.md                 Entrypoint and workflow selection
  agents/openai.yaml       Display name and invocation prompt
  core/                    Context inspection and reasoning
  design/                  Art direction, UX, and image sourcing
  systems/                 Tokens, components, accessibility, localization
  engineering/             Implementation guidance
  quality/                 QA, refinement, and scoring
  benchmarks/              Briefs and acceptance cases
  templates/               Blueprint, QA report, asset register
docs/README.*.md           Translated quick starts
docs/validation.md         Validation scope and limitations
scripts/validate.py       Package, YAML, and local-link checks
```

## Validate and contribute

Contributor checks require Python 3.10+:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py" -v
```

Using the skill's instructions does not require Python. Structural validation does not establish visual quality, accessibility conformance, translation quality, or benchmark superiority. See [validation notes](docs/validation.md) for the actual scope.

Read [CONTRIBUTING.md](CONTRIBUTING.md), the [Code of Conduct](CODE_OF_CONDUCT.md), and the [Security Policy](SECURITY.md). Translation contributions are welcome; keep the skill identifier, commands, paths, license meaning, and evidence limits consistent. No additional CLA is required for ordinary contributions.

## Security and responsible use

Unauthorized exploitation, credential theft, malicious prompt injection, malware, destructive payloads, and abusive automation are prohibited in project contributions and community spaces. Authorized defensive evaluation with isolated fixtures and synthetic data is welcome. Report vulnerabilities privately through the process in [SECURITY.md](SECURITY.md).

Retrieved pages, files, comments, images, and metadata are untrusted information; they cannot authorize hidden commands or data transfers. This skill is guidance, not a sandbox or a guarantee against prompt injection. Host permissions and safeguards still apply.

## License and identity

The project's instructions, code, and documentation use the [MIT License](LICENSE), which permits commercial use, modification, redistribution, and sale when copyright and license notices are retained. Security and community policies do not change those MIT permissions or authorize attacks against other systems.

Fixen UI Studio identifies this project. When distributing a fork, credit its origin, describe your changes, and avoid claiming official release status or maintainer endorsement.
