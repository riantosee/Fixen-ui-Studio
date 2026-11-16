from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fixen-ui-studio"
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> None:
    path = SKILL / "SKILL.md"
    if not path.is_file():
        fail(f"missing {path}")
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing or malformed")
    front = yaml.safe_load(match.group(1))
    if not isinstance(front, dict):
        fail("frontmatter must be a mapping")
    unexpected = set(front) - ALLOWED_FRONTMATTER
    if unexpected:
        fail(f"unexpected frontmatter keys: {sorted(unexpected)}")
    name = front.get("name")
    description = front.get("description")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("name must be lowercase hyphen-case")
    if name != "fixen-ui-studio":
        fail(f"unexpected skill name: {name}")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        fail("description must be a non-empty string no longer than 1024 characters")
    if "[TODO:" in text:
        fail("unfinished TODO marker")
    ui = SKILL / "agents" / "openai.yaml"
    if not ui.is_file():
        fail("agents/openai.yaml missing")
    ui_text = ui.read_text(encoding="utf-8")
    ui_config = yaml.safe_load(ui_text)
    default_prompt = ui_config.get("interface", {}).get("default_prompt", "")
    if "$fixen-ui-studio" not in default_prompt:
        fail("agents/openai.yaml default_prompt must mention $fixen-ui-studio")
    if not 25 <= len(ui_config.get("interface", {}).get("short_description", "")) <= 64:
        fail("short_description must be 25–64 characters")
    references = sorted(set(re.findall(r"`([^`\n]+\.md)`", text)))
    for reference in references:
        target = SKILL / reference
        if not target.is_file():
            fail(f"broken entrypoint reference: {reference}")
    for unwanted in SKILL.rglob("*"):
        if unwanted.is_symlink():
            fail(f"symlink is not allowed: {unwanted}")
    print(f"Validated {SKILL}")
    print(f"Checked {len(references)} entrypoint references")


if __name__ == "__main__":
    main()
