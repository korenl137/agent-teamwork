import shutil
import tempfile
import unittest
from pathlib import Path
from scripts.check import ROOT, check


class DistributionCheck(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "distribution"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self.temp.cleanup()

    def test_current_distribution(self):
        self.assertEqual(check(self.root), [])

    def test_missing_reference_is_rejected(self):
        path = self.root / "skills/team-up/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[missing](references/removed.md)\n", encoding="utf-8")
        self.assertTrue(any("invalid reference" in e for e in check(self.root)))

    def test_execution_tool_is_rejected_for_read_only_role(self):
        path = self.root / "agents/reviewer.md"
        path.write_text(path.read_text(encoding="utf-8").replace("tools: Read, Grep, Glob", "tools: Read, Bash"), encoding="utf-8")
        self.assertTrue(any("role can execute" in e for e in check(self.root)))

    def test_empty_evaluations_are_rejected(self):
        (self.root / "evals/scenarios.json").write_text("[]", encoding="utf-8")
        self.assertTrue(any("three evaluation" in e for e in check(self.root)))

    def test_yaml_spelling_cannot_hide_model_override(self):
        path = self.root / "agents/reviewer.md"
        original = path.read_text(encoding="utf-8")
        for declaration in ("model : opus", '"model": opus'):
            with self.subTest(declaration=declaration):
                path.write_text(original.replace("name: reviewer", "name: reviewer\n" + declaration), encoding="utf-8")
                self.assertTrue(any("public model override" in e for e in check(self.root)))

    def test_duplicate_yaml_tools_are_rejected(self):
        path = self.root / "agents/reviewer.md"
        text = path.read_text(encoding="utf-8").replace("tools: Read, Grep, Glob", "tools: Read, Grep, Glob\ntools: Bash")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("duplicate" in e for e in check(self.root)))

    def test_yaml_tools_list_is_checked(self):
        path = self.root / "agents/reviewer.md"
        original = path.read_text(encoding="utf-8")
        path.write_text(original.replace("tools: Read, Grep, Glob", "tools: [Read, Grep, Glob]"), encoding="utf-8")
        self.assertEqual(check(self.root), [])
        path.write_text(original.replace("tools: Read, Grep, Glob", "tools: [Read, Bash]"), encoding="utf-8")
        self.assertTrue(any("role can execute" in e for e in check(self.root)))

    def test_invalid_yaml_is_rejected(self):
        path = self.root / "agents/reviewer.md"
        text = path.read_text(encoding="utf-8").replace("name: reviewer", "name: [unterminated")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("invalid frontmatter" in e for e in check(self.root)))

    def test_empty_name_does_not_consume_next_field(self):
        path = self.root / "agents/reviewer.md"
        path.write_text(path.read_text(encoding="utf-8").replace("name: reviewer", "name:"), encoding="utf-8")
        self.assertTrue(any("missing name" in e for e in check(self.root)))
