"""Regression tests for package-boundary and invocation metadata validation."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate


class PackageValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills/fixen-ui-studio"
        (self.skill / "agents").mkdir(parents=True)
        self.front = "---\nname: fixen-ui-studio\ndescription: Test interface guidance.\nlicense: MIT\n---\n"
        (self.skill / "SKILL.md").write_text(self.front, encoding="utf-8")
        (self.skill / "agents/openai.yaml").write_text(
            'interface:\n  short_description: "Focused interface guidance for testing"\n'
            '  default_prompt: "Use $fixen-ui-studio for this interface."\n', encoding="utf-8"
        )

    def run_validator(self):
        with patch.object(validate, "ROOT", self.root), patch.object(validate, "SKILL", self.skill), contextlib.redirect_stdout(io.StringIO()):
            validate.main()

    def test_minimal_package(self):
        self.run_validator()

    def test_wrong_invocation(self):
        ui = self.skill / "agents/openai.yaml"
        ui.write_text(ui.read_text().replace("$fixen-ui-studio", "$old-name"), encoding="utf-8")
        with self.assertRaisesRegex(SystemExit, "default_prompt"):
            self.run_validator()

    def test_missing_reference(self):
        (self.skill / "SKILL.md").write_text(self.front + "Read `design/missing.md`.\n", encoding="utf-8")
        with self.assertRaisesRegex(SystemExit, "broken entrypoint reference"):
            self.run_validator()

    def test_reference_cannot_escape(self):
        (self.skill / "SKILL.md").write_text(self.front + "Read `../../external.md`.\n", encoding="utf-8")
        (self.root / "external.md").write_text("Outside the installable skill", encoding="utf-8")
        with self.assertRaisesRegex(SystemExit, "escapes skill package"):
            self.run_validator()

    def test_broken_repository_link(self):
        (self.root / "README.md").write_text("[Contribute](missing.md)", encoding="utf-8")
        with self.assertRaisesRegex(SystemExit, "local Markdown link"):
            self.run_validator()

    def test_valid_repository_link(self):
        (self.root / "README.md").write_text("[Skill](skills/fixen-ui-studio/SKILL.md)", encoding="utf-8")
        self.run_validator()


if __name__ == "__main__":
    unittest.main()
