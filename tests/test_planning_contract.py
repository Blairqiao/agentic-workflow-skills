"""Guard the written planning and execution handoff and authorization boundaries."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DEPRECATED_PHASE_TERMS = ('R' + 'oom 1', 'R' + 'oom 2', 'two-r' + 'oom')


class PlanningContractTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text()

    def test_explicit_ready_plan_execution_without_repeated_gate(self):
        core = self.read('skills/_workflow/core.md')
        for required in ('planning phase', 'execution phase',
                         'explicit instruction to execute the named ready plan',
                         'Do not repeat approval', 'Ready status alone is not authorization'):
            self.assertIn(required, core)
        for obsolete in (*DEPRECATED_PHASE_TERMS, 'pause for approval', 'One combined spec-and-plan approval'):
            self.assertNotIn(obsolete, core)

    def test_blocked_plan_and_changed_scope_return_to_planning(self):
        planning = self.read('skills/_workflow/planning.md')
        for required in ('consequential blockers cannot be ready', 'return to the planning phase',
                         'new explicit execution instruction', 'starting revision',
                         'protected user edits', 'selected executor'):
            self.assertIn(required, planning)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, planning)

    def test_complete_plan_handoff_and_collision_protection(self):
        template = self.read('skills/_workflow/templates/plan.md')
        for required in ('Execution identity', 'Target checkout',
                         'Target branch', 'Starting revision', 'Protected user edits',
                         'Selected executor', 'Unresolved blockers', 'Execution instruction'):
            self.assertIn(required, template)
        for obsolete in ('Plan content ' + 'dig' + 'est', *DEPRECATED_PHASE_TERMS, 'R' + 'oom 2 instruction'):
            self.assertNotIn(obsolete, template)
        core = self.read('skills/_workflow/core.md')
        for required in ('<feature>-<run-id>', 'Never let concurrent executions',
                         'parent repository', 'reconcile'):
            self.assertIn(required, core)
        self.assertNotIn('plan ' + 'dig' + 'est', core)

    def test_exploration_finishes_as_plan_or_paused_brief(self):
        brainstorm = self.read('skills/brainstorm/SKILL.md')
        self.assertIn('completed plan', brainstorm)
        self.assertIn('paused or abandoned exploration', brainstorm)
        self.assertIn('Planning never edits implementation code or tests', brainstorm)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, brainstorm)
        grilling = self.read('skills/grilling/SKILL.md')
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, grilling)

    def test_planning_skill_consolidates_planning_and_finalizes_at_bottom(self):
        path = ROOT / 'skills/planning/SKILL.md'
        self.assertTrue(path.is_file(), 'skills/planning/SKILL.md must exist')
        text = path.read_text()
        for required in ('brainstorm', 'grilling', 'plans/<feature>.md', 'bottom of the chat response'):
            self.assertIn(required, text)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, text)
        metadata = (ROOT / 'skills/planning/agents/openai.yaml').read_text()
        self.assertIn('planning', metadata)

    def test_paused_brief_template_and_brainstorm_metadata(self):
        brief = self.read('skills/_workflow/templates/brief.md')
        self.assertIn('paused', brief)
        self.assertIn('abandoned', brief)
        self.assertIn('handed off', brief)
        for obsolete in (*DEPRECATED_PHASE_TERMS, 'ready for planning'):
            self.assertNotIn(obsolete, brief)
        metadata = self.read('skills/brainstorm/agents/openai.yaml')
        self.assertNotIn('R' + 'oom 1', metadata)
        self.assertIn('plan', metadata)

    def test_one_shot_exception_and_follow_up_scope(self):
        core = self.read('skills/_workflow/core.md')
        for required in ('one-shot', 'both boost and non-boost', 'approved behavior',
                         "parent's proof", 'standalone fast-track'):
            self.assertIn(required, core)
        for obsolete in (*DEPRECATED_PHASE_TERMS, 'exception to the two-' + 'r' + 'oom model'):
            self.assertNotIn(obsolete, core)
        design = self.read('skills/_workflow/design.md')
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, design)


if __name__ == '__main__':
    unittest.main()
