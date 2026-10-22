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
    "orchestration-track",
    "full-track",
    "fast-track",
    "one-shot",
    "grilling",
    "human-tdd",
    "unslop",
    "domain-modeling",
    "research",
    "brainstorm",
    "planning",
}


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

    def install(self, *extra):
        result = subprocess.run(
            ["bash", str(self.source / "install.sh"), "--project", str(self.project), *extra],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    def install_global(self, *extra):
        env = dict(os.environ, HOME=str(self.home))
        result = subprocess.run(
            ["bash", str(self.source / "install.sh"), "--global", *extra],
            capture_output=True, text=True, env=env,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout

    def assert_bundle(self, location):
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
        brainstorm = location / "brainstorm/SKILL.md"
        self.assertNotIn("disable-model-invocation: true", brainstorm.read_text())
        self.assertEqual(
            set(re.findall(r"^([a-z][\w-]*):", brainstorm.read_text().split("---", 2)[1], re.MULTILINE)),
            {"name", "description"},
        )
        # Follow the skill's installed references, including shared procedures and templates.
        pending = [brainstorm]
        visited = set()
        while pending:
            resource = pending.pop().resolve()
            if resource in visited:
                continue
            visited.add(resource)
            # Code samples can contain illustrative paths that are not resource links.
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
            if name in {"full-track", "fast-track", "one-shot", "orchestration-track"}:
                self.assertTrue((skill.parent / "../_workflow/core.md").is_file())
            self.assertNotIn("disable-model-invocation: true", skill.read_text())

    def test_project_install(self):
        self.install("--force")
        self.assert_bundle(self.project / ".agents/skills")
        self.assertFalse((self.project / ".claude").exists())

    def test_source_bundle_exposes_only_public_skills(self):
        self.source = ROOT
        self.install()
        self.assert_bundle(self.project / ".agents/skills")

    def test_global_install_and_link_integrity(self):
        self.install_global()
        config_skills = self.home / ".gemini/config/skills"
        cli_skills = self.home / ".gemini/antigravity-cli/skills"
        self.assertFalse((self.home / ".agents").exists())
        self.assertFalse((self.home / ".claude").exists())
        for location in (config_skills, cli_skills):
            self.assertTrue(location.is_dir(), f"{location} must be a directory")
            self.assert_bundle(location)
            wf_link = location / "_workflow"
            self.assertTrue(wf_link.is_symlink(), f"{wf_link} must be a symlink")
            self.assertTrue(wf_link.exists(), f"{wf_link} target must exist")
            for name in PUBLIC:
                skill_link = location / name
                self.assertTrue(skill_link.is_symlink(), f"{skill_link} must be a symlink")
                self.assertTrue(skill_link.exists(), f"{skill_link} target must exist")

    def test_global_uninstall(self):
        self.install_global()
        config_skills = self.home / ".gemini/config/skills"
        cli_skills = self.home / ".gemini/antigravity-cli/skills"
        for location in (config_skills, cli_skills):
            custom = location / "custom/SKILL.md"
            custom.parent.mkdir()
            custom.write_text("custom skill\n")
            retired = location / "task-dispatch/SKILL.md"
            retired.parent.mkdir()
            retired.write_text("retired skill\n")
        self.install_global("--uninstall")
        for location in (config_skills, cli_skills):
            self.assertTrue((location / "custom/SKILL.md").is_file())
            self.assertFalse((location / "task-dispatch").exists())
            self.assertFalse((location / "_workflow").exists())
            for name in PUBLIC:
                self.assertFalse((location / name).exists())

    def test_existing_destinations_are_preserved_without_force(self):
        self.install()
        skill = self.project / ".agents/skills/full-track/SKILL.md"
        skill.write_text("user-owned content\n")
        procedure = self.project / ".agents/skills/_workflow/core.md"
        procedure.write_text("user-owned procedure\n")
        self.install()
        self.assertEqual(skill.read_text(), "user-owned content\n")
        self.assertEqual(procedure.read_text(), "user-owned procedure\n")

    def test_force_refreshes_bundle_without_pruning_other_skills(self):
        self.install()
        extra = self.project / ".agents/skills/custom/SKILL.md"
        extra.parent.mkdir()
        extra.write_text("custom skill\n")
        old = self.project / ".agents/skills/task-dispatch/SKILL.md"
        old.parent.mkdir()
        old.write_text("previous installation\n")
        self.install("--force")
        self.assertEqual(extra.read_text(), "custom skill\n")
        self.assertEqual(old.read_text(), "previous installation\n")
        self.assertTrue((self.project / ".agents/skills/_workflow/core.md").is_file())

    def test_uninstall_removes_bundle_and_retired_skills_while_preserving_custom(self):
        self.install()
        custom = self.project / ".agents/skills/custom/SKILL.md"
        custom.parent.mkdir()
        custom.write_text("custom skill\n")
        retired = self.project / ".agents/skills/task-dispatch/SKILL.md"
        retired.parent.mkdir()
        retired.write_text("retired skill\n")
        self.install("--uninstall")
        self.assertTrue(custom.is_file())
        self.assertFalse(retired.exists())
        self.assertFalse((self.project / ".agents/skills/_workflow").exists())
        self.assertFalse((self.project / ".claude").exists())
        for name in PUBLIC:
            self.assertFalse((self.project / ".agents/skills" / name).exists())

    def test_missing_option_arguments_fail_cleanly(self):
        for flag in ("--project",):
            result = subprocess.run(
                ["bash", str(self.source / "install.sh"), flag],
                capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Usage:", result.stdout + result.stderr)
        # Passing removed harness option should fail cleanly
        result = subprocess.run(
            ["bash", str(self.source / "install.sh"), "--harness", "claude"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Usage:", result.stdout + result.stderr)

    def test_existing_research_resources_are_preserved_without_force(self):
        self.install()
        skill = self.project / ".agents/skills/research/SKILL.md"
        procedure = self.project / ".agents/skills/_workflow/research-audit.md"
        self.assertTrue(skill.is_file())
        self.assertTrue(procedure.is_file())
        skill.write_text("user-owned research skill\n")
        procedure.write_text("user-owned audit procedure\n")
        self.install()
        self.assertEqual(skill.read_text(), "user-owned research skill\n")
        self.assertEqual(procedure.read_text(), "user-owned audit procedure\n")

    def test_approval_gate_and_inline_presentation_guidance(self):
        self.install()
        installed = self.project / ".agents/skills"
        core = (installed / "_workflow/core.md").read_text()
        self.assertIn("inline", core)
        self.assertIn("explicit approval", core)
        self.assertIn("follow-up repair", core)
        self.assertIn("orchestration", core.lower())
        for name in ("orchestration-track", "full-track", "fast-track", "planning"):
            skill = (installed / name / "SKILL.md").read_text()
            self.assertIn("../_workflow/core.md", skill, name)
            self.assertIn("supplied-context", skill, name)
        agents_guide = (ROOT / "AGENTS.md").read_text()
        self.assertIn("every follow-up repair", agents_guide)
        self.assertIn("Skill Activated:", agents_guide)
        self.assertIn("/skills/_workflow/core.md", agents_guide)
        self.assertIn("/skills/planning/SKILL.md", agents_guide)
        self.assertLess(len(agents_guide.splitlines()), 40)
        gemini_rules = (ROOT / "GEMINI.md").read_text()
        self.assertIn("AGENTS.md", gemini_rules)
        self.assertIn("adapters/antigravity.md", gemini_rules)
        self.assertLess(len(gemini_rules.splitlines()), 15)

    def test_antigravity_tools_and_discovery_guidance(self):
        self.install()
        installed = self.project / ".agents/skills"
        adapter = (installed / "_workflow/adapters/antigravity.md").read_text()
        for tool in ("invoke_subagent", "view_file", "run_command"):
            self.assertIn(tool, adapter)
        self.assertIn("exposed", adapter)
        for name in ("discovery", "execution"):
            procedure = (installed / f"_workflow/{name}.md").read_text()
            self.assertIn("adapter", procedure)
            self.assertNotIn("Argon", procedure)
        agents_guide = (ROOT / "AGENTS.md").read_text()
        self.assertIn("automatically", agents_guide)
        self.assertIn("/skills/orchestration-track/SKILL.md", agents_guide)
        self.assertIn("vertical slices", agents_guide)
        self.assertNotIn("Gemini 4 Argon", agents_guide)

    def test_existing_brainstorm_resources_are_preserved_then_refreshed(self):
        self.install()
        resources = (
            "brainstorm/SKILL.md",
            "brainstorm/agents/openai.yaml",
            "_workflow/templates/brief.md",
        )
        for relative in resources:
            installed = self.project / ".agents/skills" / relative
            self.assertTrue(installed.is_file(), str(installed))
            installed.write_text("user-owned brainstorm resource\n")
        self.install()
        for relative in resources:
            installed = self.project / ".agents/skills" / relative
            self.assertEqual(installed.read_text(), "user-owned brainstorm resource\n")
        self.install("--force")
        for relative in resources:
            installed = self.project / ".agents/skills" / relative
            self.assertEqual(installed.read_text(), (self.source / "skills" / relative).read_text())

    def test_antigravity_boost_guidance_and_gemini_rules(self):
        self.install()
        installed = self.project / ".agents/skills"
        adapter = (installed / "_workflow/adapters/antigravity.md").read_text()
        self.assertIn("/boost", adapter)
        self.assertIn("../core.md", adapter)
        core = (installed / "_workflow/core.md").read_text()
        for safeguard in ("test integrity", "independent", "verification"):
            self.assertIn(safeguard, core)
        self.assertIn("evidence", adapter)
        self.assertIn("Do not claim a skill activates", adapter)
        gemini_rules = ROOT / "GEMINI.md"
        self.assertTrue(gemini_rules.is_file(), "GEMINI.md must exist at root")
        self.assertIn("adapters/antigravity.md", gemini_rules.read_text())
        orch_track = (installed / "orchestration-track/SKILL.md").read_text()
        self.assertIn("adapter", orch_track)
        self.assertIn("../_workflow/core.md", orch_track)

    def test_reactive_wakeups_and_prose_parentheses(self):
        self.install()
        execution = (self.project / ".agents/skills/_workflow/execution.md").read_text()
        self.assertIn("reactive wakeups", execution)

        candidate_files = [
            ROOT / "skills/orchestration-track/SKILL.md",
            ROOT / "skills/full-track/SKILL.md",
            ROOT / "skills/_workflow/execution.md",
            ROOT / "skills/_workflow/planning.md",
            ROOT / "skills/_workflow/core.md",
            ROOT / "skills/_workflow/adapters/antigravity.md",
            ROOT / "AGENTS.md",
            ROOT / "GEMINI.md",
            ROOT / "README.md",
        ]
        for f in candidate_files:
            lines = f.read_text().splitlines()
            for idx, line in enumerate(lines, 1):
                clean = re.sub(r"!?\[[^\]]*\]\([^)]+\)", "", line)
                self.assertNotIn("(", clean, f"Prose parenthesis found in {f.name}:{idx}: {line}")
                self.assertNotIn(")", clean, f"Prose parenthesis found in {f.name}:{idx}: {line}")


if __name__ == "__main__":
    unittest.main()
