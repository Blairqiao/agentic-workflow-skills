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
        for obsolete in (*DEPRECATED_PHASE_TERMS, 'One combined spec-and-plan approval'):
            self.assertNotIn(obsolete, core)

    def test_supplied_context_reuse_and_targeted_recovery(self):
        core = self.read('skills/_workflow/core.md')
        for required in ('complete applicable skill or procedure body', 'active conversation',
                         'Do not reopen', 'absent', 'incomplete', 'compaction', 'changed',
                         'different checkout', 'version-sensitive', 'catalog description',
                         'no routine hash check'):
            self.assertIn(required, core)
        agents = self.read('AGENTS.md')
        self.assertIn('skills/_workflow/core.md', agents)
        self.assertIn('supplied-context reuse', agents)

    def test_phase_links_do_not_force_recursive_loading(self):
        core = self.read('skills/_workflow/core.md')
        for required in ('optional reference', 'current step explicitly requires',
                         'active adapter only', 'no ceremonial interview'):
            self.assertIn(required, core)
        discovery = self.read('skills/_workflow/discovery.md')
        self.assertIn('bounded searches', discovery)
        self.assertIn('Save lengthy evidence once', discovery)
        self.assertIn('verbatim', discovery)
        self.assertIn('do not hide failures', discovery)

    def test_every_interactive_repair_needs_its_own_approval(self):
        core = self.read('skills/_workflow/core.md')
        for required in ('every follow-up repair', 'before editing code or tests',
                         'scope, affected files, strategy, acceptance criteria, and verification',
                         'pause for explicit approval', 'does not substitute',
                         'Diagnosis and independent read-only work may continue',
                         'one-shot', 'without interactive approval gates'):
            self.assertIn(required, core)
        antigravity = self.read('skills/_workflow/adapters/antigravity.md')
        self.assertIn('core.md', antigravity)
        self.assertNotIn("inherit only the parent's approved behavior", antigravity)
        gemini = self.read('GEMINI.md')
        self.assertIn('AGENTS.md', gemini)
        self.assertNotIn('without repeating approval gates', gemini)

    def test_unslop_preserves_exemptions_and_single_activation(self):
        text = self.read('skills/unslop/SKILL.md')
        for required in ('code blocks', 'commands', 'logs', 'commit hashes', 'file paths',
                         'verbatim quotes', 'same active use', 'activation announcement',
                         'em dashes', 'parentheses', 'en dashes', 'hyphen-as-dash',
                         'sentence case', 'straight quotes', 'synonym', 'hedging'):
            self.assertIn(required, text)

    def test_repair_policy_is_consistent_in_phase_guidance(self):
        paths = ('README.md', 'skills/_workflow/README.md',
                 'skills/_workflow/execution.md', 'skills/_workflow/planning.md',
                 'skills/_workflow/design.md', 'skills/_workflow/templates/proof.md',
                 'skills/brainstorm/SKILL.md', 'skills/grilling/SKILL.md')
        for path in paths:
            with self.subTest(path=path):
                text = self.read(path)
                self.assertIn('every follow-up repair', text.lower())
                self.assertIn('mini-spec', text)
                self.assertIn('approval', text)
        for path in ('README.md', 'skills/_workflow/README.md',
                     'skills/_workflow/execution.md'):
            text = self.read(path)
            for stale in ('or parent plan', 'within the parent authorization',
                          'then proceed under the parent authorization'):
                self.assertNotIn(stale, text)
        readme = self.read('README.md')
        self.assertIn('supplied-context reuse', readme)
        self.assertIn('optional references', readme)
        self.assertIn('one-shot', readme)
        self.assertIn('autonomous exception', readme)

    def test_declared_fast_startup_reduces_gemini_baseline_bytes(self):
        # Whole-file UTF-8 bytes, not measured live model token use or latency.
        common = ('AGENTS.md', 'skills/fast-track/SKILL.md',
                  'skills/_workflow/core.md', 'skills/unslop/SKILL.md',
                  'skills/_workflow/templates/fast-track.md')
        # Gemini base 366b89e67ef468dd0834129456928210497ecd96 required
        # the common files above, active adapter, and discovery.md, design.md,
        # planning.md under skills/_workflow before fast execution. Baselines
        # sum whole-file bytes at that revision; candidate sums only common
        # files plus active adapter. The plan promises simpler loading, with
        # no numeric percentage target. Keep the semantic safety checks below.
        for harness, baseline in (('codex', 45048), ('antigravity', 45815)):
            files = (*common, 'skills/_workflow/adapters/' + harness + '.md')
            candidate = sum(len((ROOT / path).read_bytes()) for path in files)
            self.assertLess(candidate, baseline, (harness, files, candidate))
        fast = self.read('skills/fast-track/SKILL.md')
        self.assertIn('only when', fast)
        self.assertIn('without loading the full discovery/design/planning chain', fast)
        # Size alone cannot establish these independent safety contracts.
        core = self.read('skills/_workflow/core.md')
        for safeguard in ('Cap failed implementation attempts at 3',
                          'review-fix cycles at 3', 'independent',
                          'red before implementation', 'Preserve unrelated edits',
                          'Do not commit during execution', 'new dependencies',
                          'destructive operations', 'Stage the candidate'):
            self.assertIn(safeguard, core)

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
