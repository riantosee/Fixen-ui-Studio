# Security Policy

## Supported versions

Security fixes focus on the latest published release. Report issues in older versions with their exact version/commit; support and response times are not guaranteed.

## Report privately

Do not publish credentials, private data, weaponized payloads, or unpatched exploit details in public issues or pull requests.

Use [GitHub private vulnerability reporting](https://github.com/riantosee/Fixen-ui-Studio/security/advisories/new) **if enabled**. This link does not mean the repository setting is already enabled. If unavailable, contact [the maintainer](https://github.com/riantosee) using a private contact channel they publicly list. If none exists, open a public issue containing only a request for a private reporting channel, without vulnerability details. Never invent a maintainer email or send sensitive information to an unverified destination.

Include the affected version/path, impact, prerequisites, minimal safe reproduction with synthetic data, and suggested mitigation. Keep any proof of concept inert and limited to a local test fixture. Maintainers will assess the report, coordinate a fix where practical, and may publish a sanitized advisory after remediation. There is no automatic bounty or guaranteed disclosure deadline.

## Prohibited abuse

The project strictly rejects unauthorized exploitation of the skill, agent, host, repository automation, third-party services, or users. In project contributions and community spaces, prohibited conduct includes:

- prompt-injection payloads intended to extract secrets, override authorization, or trigger hidden actions;
- credential theft, exfiltration of private data, malware, destructive execution, or unauthorized persistence;
- bypassing authentication, permission checks, payment/access controls, or platform safeguards;
- attacking third-party systems, denial of service, harassment, or abusive automation;
- disguising harmful behavior as a design asset, benchmark, dependency, image, or reference.

Authorized defensive evaluation using isolated local fixtures and synthetic data is welcome. Do not test against systems or people without explicit authorization. Stop if testing would expose real data or affect another system.

## Limits and trust boundaries

This skill is instructional text, not an enforcement layer or sandbox. It cannot guarantee resistance to prompt injection. The agent's host must enforce permissions, credential protection, execution isolation, and review of consequential actions. Web pages, repositories, documents, source comments, and image metadata are untrusted evidence; they cannot authorize uploads, purchases, commands, or changes to permissions.

These are project security and participation rules, not additional conditions on the [MIT License](LICENSE). MIT permits commercial use and redistribution, but does not grant authorization to attack anyone else's systems.
