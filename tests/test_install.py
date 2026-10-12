"""Exercise installed skill bundles without touching user skill directories."""

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = {"full-track", "fast-track", "one-shot", "grilling", "human-tdd", "unslop"}


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="workflow install ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source with spaces"
        self.source.mkdir()
        shutil.copy2(ROOT / "install.sh", self.source / "install.sh")
        shutil.copytree(ROOT / "skills", self.source / "skills")
        self.project = self.base / "project with spaces"
        self.project.mkdir()

    def install(self, harness, *extra):
        result = subprocess.run(
            ["bash", str(self.source / "install.sh"), "--project", str(self.project),
             "--harness", harness, *extra], capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    def assert_bundle(self, location, claude=False):
        self.assertEqual({p.parent.name for p in location.glob("*/SKILL.md")}, PUBLIC)
        self.assertTrue((location / "_workflow/core.md").is_file())
        self.assertFalse((location / "_workflow/SKILL.md").exists())
        for name in PUBLIC:
            skill = location / name / "SKILL.md"
            self.assertTrue(skill.is_file(), name)
            if name in {"full-track", "fast-track", "one-shot"}:
                self.assertTrue((skill.parent / "../_workflow/core.md").is_file())
                self.assertEqual("disable-model-invocation: true" in skill.read_text(), claude)
                adapter = skill.parent / "agents/openai.yaml"
                self.assertIn("allow_implicit_invocation: false", adapter.read_text())

    def test_shared_harness_project_installs(self):
        for harness in ("codex", "antigravity", "gemini", "opencode"):
            with self.subTest(harness=harness):
                self.install(harness, "--force")
                self.assert_bundle(self.project / ".agents/skills")

    def test_source_bundle_exposes_only_public_skills(self):
        self.source = ROOT
        self.install("codex")
        self.assert_bundle(self.project / ".agents/skills")

    def test_claude_only_is_self_contained(self):
        self.install("claude")
        self.assert_bundle(self.project / ".claude/skills", claude=True)
        self.assertFalse((self.project / ".agents").exists())

    def test_mixed_install_has_working_links(self):
        self.install("claude,codex,antigravity")
        self.assert_bundle(self.project / ".agents/skills")
        self.assert_bundle(self.project / ".claude/skills", claude=True)

    def test_existing_destinations_are_preserved_without_force(self):
        self.install("codex")
        skill = self.project / ".agents/skills/full-track/SKILL.md"
        skill.write_text("user-owned content\n")
        procedure = self.project / ".agents/skills/_workflow/core.md"
        procedure.write_text("user-owned procedure\n")
        self.install("codex")
        self.assertEqual(skill.read_text(), "user-owned content\n")
        self.assertEqual(procedure.read_text(), "user-owned procedure\n")

    def test_force_refreshes_bundle_without_pruning_other_skills(self):
        self.install("codex")
        extra = self.project / ".agents/skills/custom/SKILL.md"
        extra.parent.mkdir()
        extra.write_text("custom skill\n")
        old = self.project / ".agents/skills/task-dispatch/SKILL.md"
        old.parent.mkdir()
        old.write_text("previous installation\n")
        self.install("codex", "--force")
        self.assertEqual(extra.read_text(), "custom skill\n")
        self.assertEqual(old.read_text(), "previous installation\n")
        self.assertTrue((self.project / ".agents/skills/_workflow/core.md").is_file())


if __name__ == "__main__":
    unittest.main()
