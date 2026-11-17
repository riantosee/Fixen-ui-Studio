# Contributing to Fixen UI Studio

Contributions to documentation, design workflows, accessibility, localization, image sourcing, and evaluation are welcome. Read the [Code of Conduct](CODE_OF_CONDUCT.md) and [Security Policy](SECURITY.md) first.

## Choose a focused change

- Small fixes and typos can go directly to a pull request.
- For a new workflow or substantial behavior change, open an issue describing the need and observable acceptance criteria.
- Report vulnerabilities privately. Use inert, synthetic local fixtures for safe defensive examples.

Favor guidance that changes an agent's decisions. Avoid generic advice, extra personas, unjustified absolute rules, or instructions that override the user's scope. Preserve audit-only mode, honest tool limits, and lightweight handling of small changes.

## Workflow

1. Fork the repository and create a branch for one focused change.
2. Edit `skills/fixen-ui-studio/`; do not modify a user's global installation.
3. Link new references from the entrypoint or the relevant guide and explain when to read them. Do not load every reference for every task.
4. Run `python -m pip install -r requirements-dev.txt`, `python scripts/validate.py`, and `python -m unittest discover -s scripts -p "test_*.py" -v`.
5. For behavior changes, exercise a relevant realistic brief with synthetic data. Record the prompt, tools, observed results, and untested areas. Small documentation changes do not require the entire benchmark suite.
6. Open a PR describing the problem, resulting behavior, and validation evidence. Link the issue when applicable.

## Documentation and translation

English is the primary documentation language. Translated quick starts live in `docs/README.<locale>.md`; the root `README.md` links each available translation. A translation may be proposed or reviewed in its own language; include a short English description when practical so maintainers can route it.

- Preserve `$fixen-ui-studio`, code, paths, version numbers, and command behavior.
- Translate meaning naturally, including experimental status and validation limits. Do not imply guaranteed language support, security, or accessibility conformance.
- Keep MIT permissions and third-party asset licensing accurate. Translation does not create a new license restriction.
- Use working relative links from each document's directory. Include installation, examples, and a link back to the primary README.
- Update affected translations with a behavior change, or explicitly describe the remaining translation gap in the PR. When documentation differs, reconcile it against the English README and changelog.
- For UI localization changes, use the relevant cases in `skills/fixen-ui-studio/benchmarks/localization-cases.md`; report which locales and viewports were actually inspected.

## Evidence standards

Use synthetic data and assets with clear usage rights. Record relevant browser, viewport, renderer, and configuration details. Distinguish static checks from simulation, implementation, and real browser tests. Include screenshots for layout findings; a successful build alone is not evidence of a successful design.

Do not claim compliance, benchmark scores, translation review, tool execution, or asset rights without evidence. Comparative benchmarks need equivalent prompts, context, tools, time budgets, and scoring conditions.

## Safe contributions

Do not include secrets, credentials, private data, proprietary project copies, or exploits targeting real systems. Do not embed hidden instructions to upload data, change permissions, run payloads, or bypass authorization. Security reproductions must be minimal and inert; send sensitive details through the private reporting process.

Contributions involving security abuse, misleading claims, plagiarism, or license violations will be rejected. Maintainers may close issues/PRs or restrict participation under the Code of Conduct. Moderation does not add conditions to MIT.

## License

By contributing, you represent that you have the right to submit your work and agree that accepted contributions are available under the [MIT License](LICENSE). Record third-party assets under their own licenses. No additional CLA is required for ordinary contributions.
