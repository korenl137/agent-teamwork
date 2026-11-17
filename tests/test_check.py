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
