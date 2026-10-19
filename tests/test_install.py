"""Exercise installed skill bundles without touching user skill directories."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = {
    "planning",
    "full-track",
    "fast-track",
    "one-shot",
    "brainstorm",
    "domain-modeling",
    "grilling",
    "human-tdd",
    "unslop",
    "research",
}
DEPRECATED_PHASE_TERMS = ('R' + 'oom 1', 'R' + 'oom 2', 'two-r' + 'oom')


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
        self.home = self.base / "home with spaces"
        self.home.mkdir()

    def install(self, harness=None, *extra):
        args = ["bash", str(self.source / "install.sh"), "--project", str(self.project)]
        if harness:
            args.extend(["--harness", harness])
        args.extend(extra)
        result = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    def install_global(self, harness=None, *extra):
        env = dict(os.environ, HOME=str(self.home))
        args = ["bash", str(self.source / "install.sh"), "--global"]
        if harness:
            args.extend(["--harness", harness])
        args.extend(extra)
        result = subprocess.run(args, capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    def assert_bundle(self, location, claude=False):
        self.assertEqual({p.parent.name for p in location.glob("*/SKILL.md")}, PUBLIC)
        self.assertTrue((location / "_workflow/core.md").is_file())
        self.assertTrue((location / "_workflow/templates/fast-track.md").is_file())
        self.assertTrue((location / "_workflow/templates/plan.md").is_file())
        self.assertTrue((location / "_workflow/templates/proof.md").is_file())
        self.assertTrue((location / "_workflow/templates/taskboard.md").is_file())
        self.assertTrue((location / "_workflow/templates/reviewer-brief.md").is_file())
        self.assertTrue((location / "_workflow/templates/research-audit.md").is_file())
        self.assertTrue((location / "_workflow/templates/brief.md").is_file())
        self.assertFalse((location / "_workflow/templates/spec.md").exists())
        self.assertFalse((location / "_workflow/templates/walkthrough.md").exists())
        self.assertFalse((location / "_workflow/SKILL.md").exists())
        self.assertTrue((location / "domain-modeling/references/context-format.md").is_file())
        research_files = (
            location / "research/SKILL.md",
            location / "_workflow/research-explain.md",
            location / "_workflow/research-audit.md",
        )
        for resource in research_files:
            self.assertTrue(resource.is_file(), str(resource))
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", resource.read_text()):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue(
                        (resource.parent / target.split("#", 1)[0]).is_file(),
                        f"Broken installed reference in {resource}: {target}",
                    )
        frontmatter = research_files[0].read_text().split("---", 2)[1]
        self.assertEqual(
            set(re.findall(r"^([a-z][\w-]*):", frontmatter, re.MULTILINE)),
            {"name", "description"},
        )
        self.assertNotIn("allow_implicit_invocation: false", (
            location / "research/agents/openai.yaml"
        ).read_text())
        brainstorm = location / "brainstorm/SKILL.md"
        self.assertNotIn("disable-model-invocation: true", brainstorm.read_text())
        self.assertNotIn("allow_implicit_invocation: false", (
            location / "brainstorm/agents/openai.yaml"
        ).read_text())
        self.assertEqual(
            set(re.findall(r"^([a-z][\w-]*):", brainstorm.read_text().split("---", 2)[1], re.MULTILINE)),
            {"name", "description"},
        )
        planning = location / "planning/SKILL.md"
        self.assertTrue(planning.is_file())
        self.assertEqual(
            set(re.findall(r"^([a-z][\w-]*):", planning.read_text().split("---", 2)[1], re.MULTILINE)),
            {"name", "description"},
        )
        # Follow the skill's installed references, including shared procedures and templates.
        pending = [brainstorm, planning]
        visited = set()
        while pending:
            resource = pending.pop().resolve()
            if resource in visited:
                continue
            visited.add(resource)
            prose = re.sub(r"```.*?```|`[^`\n]*`", "", resource.read_text(), flags=re.DOTALL)
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
                if "://" in target or target.startswith("#"):
                    continue
                linked = (resource.parent / target.split("#", 1)[0]).resolve()
                self.assertTrue(linked.is_file(), f"Broken installed reference in {resource}: {target}")
                if linked.suffix == ".md":
                    pending.append(linked)
        for name in PUBLIC:
            skill = location / name / "SKILL.md"
            self.assertTrue(skill.is_file(), name)
            if name in {"full-track", "fast-track", "one-shot"}:
                self.assertTrue((skill.parent / "../_workflow/core.md").is_file())
            if name == "one-shot":
                self.assertEqual("disable-model-invocation: true" in skill.read_text(), claude)
                if claude:
                    self.assertFalse((skill.parent / "agents/openai.yaml").exists())
                else:
                    adapter = skill.parent / "agents/openai.yaml"
                    self.assertIn("allow_implicit_invocation: false", adapter.read_text())
            elif name in {"full-track", "fast-track"}:
                self.assertNotIn("disable-model-invocation: true", skill.read_text())
                adapter = skill.parent / "agents/openai.yaml"
                self.assertNotIn("allow_implicit_invocation: false", adapter.read_text())

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

    def test_global_install_and_link_integrity(self):
        self.install_global("antigravity,gemini,codex,claude")
        config_skills = self.home / ".gemini/config/skills"
        cli_skills = self.home / ".gemini/antigravity-cli/skills"
        agents_skills = self.home / ".agents/skills"
        claude_skills = self.home / ".claude/skills"
        for location in (config_skills, cli_skills, agents_skills):
            self.assertTrue(location.is_dir(), f"{location} must be a directory")
            self.assert_bundle(location)
            wf_link = location / "_workflow"
            self.assertTrue(wf_link.is_symlink(), f"{wf_link} must be a symlink")
            self.assertTrue(wf_link.exists(), f"{wf_link} target must exist")
            for name in PUBLIC:
                skill_link = location / name
                self.assertTrue(skill_link.is_symlink(), f"{skill_link} must be a symlink")
                self.assertTrue(skill_link.exists(), f"{skill_link} target must exist")
        self.assertTrue(claude_skills.is_dir())
        self.assert_bundle(claude_skills, claude=True)

    def test_global_uninstall(self):
        self.install_global("antigravity,gemini,codex,claude")
        locations = [
            self.home / ".gemini/config/skills",
            self.home / ".gemini/antigravity-cli/skills",
            self.home / ".agents/skills",
            self.home / ".claude/skills",
        ]
        for location in locations:
            custom = location / "custom/SKILL.md"
            custom.parent.mkdir(parents=True, exist_ok=True)
            custom.write_text("custom skill\n")
            retired = location / "task-dispatch/SKILL.md"
            retired.parent.mkdir(parents=True, exist_ok=True)
            retired.write_text("retired skill\n")
        self.install_global("antigravity,gemini,codex,claude", "--uninstall")
        for location in locations:
            self.assertTrue((location / "custom/SKILL.md").is_file())
            self.assertFalse((location / "task-dispatch").exists())
            self.assertFalse((location / "_workflow").exists())
            for name in PUBLIC:
                self.assertFalse((location / name).exists())

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

    def test_uninstall_removes_bundle_and_retired_skills_while_preserving_custom(self):
        self.install("claude,codex")
        custom = self.project / ".agents/skills/custom/SKILL.md"
        custom.parent.mkdir()
        custom.write_text("custom skill\n")
        retired = self.project / ".agents/skills/task-dispatch/SKILL.md"
        retired.parent.mkdir()
        retired.write_text("retired skill\n")
        self.install("claude,codex", "--uninstall")
        self.assertTrue(custom.is_file())
        self.assertFalse(retired.exists())
        self.assertFalse((self.project / ".agents/skills/_workflow").exists())
        self.assertFalse((self.project / ".claude/skills/_workflow").exists())
        for name in PUBLIC:
            self.assertFalse((self.project / ".agents/skills" / name).exists())
            self.assertFalse((self.project / ".claude/skills" / name).exists())

    def test_missing_option_arguments_fail_cleanly(self):
        for flag in ("--project", "--harness"):
            result = subprocess.run(
                ["bash", str(self.source / "install.sh"), flag],
                capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Usage:", result.stdout + result.stderr)

    def test_existing_research_resources_are_preserved_without_force(self):
        self.install("codex")
        skill = self.project / ".agents/skills/research/SKILL.md"
        procedure = self.project / ".agents/skills/_workflow/research-audit.md"
        self.assertTrue(skill.is_file())
        self.assertTrue(procedure.is_file())
        skill.write_text("user-owned research skill\n")
        procedure.write_text("user-owned audit procedure\n")
        self.install("codex")
        self.assertEqual(skill.read_text(), "user-owned research skill\n")
        self.assertEqual(procedure.read_text(), "user-owned audit procedure\n")

    def test_plan_entry_and_authorization_guidance(self):
        self.install("codex")
        core = (self.project / ".agents/skills/_workflow/core.md").read_text()
        self.assertIn("execution phase", core)
        self.assertIn("planning phase", core)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, core)
        full_track = (self.project / ".agents/skills/full-track/SKILL.md").read_text()
        self.assertIn("without repeating approval", full_track)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, full_track)
        fast_track = (self.project / ".agents/skills/fast-track/SKILL.md").read_text()
        self.assertIn("without another approval", fast_track)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, fast_track)
        agents_guide = (ROOT / "AGENTS.md").read_text()
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, agents_guide)
        self.assertIn("Skill Activated:", agents_guide)
        gemini_rules = (ROOT / "GEMINI.md").read_text()
        self.assertIn("Skill Activated:", gemini_rules)

    def test_existing_brainstorm_resources_are_preserved_then_refreshed(self):
        self.install("codex")
        resources = (
            "brainstorm/SKILL.md",
            "brainstorm/agents/openai.yaml",
            "_workflow/templates/brief.md",
        )
        for relative in resources:
            installed = self.project / ".agents/skills" / relative
            self.assertTrue(installed.is_file(), str(installed))
            installed.write_text("user-owned brainstorm resource\n")
        self.install("codex")
        for relative in resources:
            installed = self.project / ".agents/skills" / relative
            self.assertEqual(installed.read_text(), "user-owned brainstorm resource\n")
        self.install("codex", "--force")
        for relative in resources:
            installed = self.project / ".agents/skills" / relative
            self.assertEqual(installed.read_text(), (self.source / "skills" / relative).read_text())

    def test_prose_parentheses(self):
        candidate_files = [
            ROOT / "skills/full-track/SKILL.md",
            ROOT / "skills/fast-track/SKILL.md",
            ROOT / "skills/one-shot/SKILL.md",
            ROOT / "skills/_workflow/execution.md",
            ROOT / "skills/_workflow/planning.md",
            ROOT / "skills/_workflow/core.md",
            ROOT / "skills/_workflow/adapters/antigravity.md",
            ROOT / "AGENTS.md",
            ROOT / "GEMINI.md",
            ROOT / "README.md",
        ]
        for f in candidate_files:
            if not f.is_file():
                continue
            lines = f.read_text().splitlines()
            for idx, line in enumerate(lines, 1):
                clean = re.sub(r"!?\[[^\]]*\]\([^)]+\)", "", line)
                self.assertNotIn("(", clean, f"Prose parenthesis found in {f.name}:{idx}: {line}")
                self.assertNotIn(")", clean, f"Prose parenthesis found in {f.name}:{idx}: {line}")


if __name__ == "__main__":
    unittest.main()
