"""Acceptance contracts for executor ownership and evidence boundaries."""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1] / 'skills' / '_workflow'


class ExecutorContractTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text()

    def test_native_boost_owns_internal_coordination(self):
        text = self.read('execution.md')
        self.assertIn('Boost owns internal task decomposition, worker dispatch, scheduling, and implementation', text)
        self.assertIn('Do not add a mandatory custom taskboard', text)
        self.assertIn('Full-track uses non-boost', text)
        self.assertIn('parent proof', text)

    def test_native_review_requires_observable_evidence(self):
        text = self.read('review.md')
        self.assertIn('Native independent review can satisfy', text)
        self.assertIn('targeted independent review', text)
        self.assertIn('incomplete', text)
        self.assertIn('test amendment', text)

    def test_reviewer_brief_supplies_complete_candidate_inputs(self):
        text = self.read('templates/reviewer-brief.md')
        for requirement in (
                'Exact plan path and revision', 'execution slug', 'selected executor',
                'evidence ownership', 'Workspace, candidate branch, and base revision',
                'git diff <base-revision>', 'untracked candidate files',
                'Acceptance criteria', 'Settled design decisions', 'non-goals',
                'Domain dictionary', 'Red and green test outputs',
                'Exact commands and verbatim', 'Test amendments',
                'every existing test expectation changed', 'Suite and UI evidence'):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text)

    def test_reviewer_contract_does_not_recursively_load_workflow(self):
        text = self.read('templates/reviewer-brief.md')
        self.assertIn('This brief is the complete reviewer contract', text)
        self.assertIn('Applicable repository guidance', text)
        self.assertIn('Exclude the implementer', text)
        self.assertNotIn('](../review.md)', text)
        self.assertNotIn('](review.md)', text)
        for instruction in ('Read the track', 'Read workflow core',
                            'Read the taskboard template', 'Read the proof template'):
            self.assertNotIn(instruction, text)
        procedure = self.read('review.md')
        self.assertIn('templates/reviewer-brief.md', procedure)
        self.assertIn('Keep the reviewer checklist in that contract', procedure)

    def test_reviewer_contract_audits_evidence_and_missing_proof(self):
        text = self.read('templates/reviewer-brief.md')
        for requirement in (
                'every acceptance criterion', 'complete candidate diff',
                'weakened assertions', 'missing edge cases', 'fixture-specific production',
                'inappropriate mocks', 'accept or reject every test amendment',
                'Reproduce commands', 'Missing red evidence cannot be reconstructed',
                'later passing run does not replace', 'review incomplete',
                'input handling', 'authentication', 'authorization', 'stored data',
                'dependencies', 'external boundaries', 'data loss', 'locking', 'rollback',
                'documentation', 'requirements were not rewritten to hide defects'):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, text)

    def test_reviewer_verdict_and_orchestrator_resolution_are_explicit(self):
        brief = self.read('templates/reviewer-brief.md')
        for requirement in (
                'Method and independence', 'Candidate identity and base revision',
                'pass, blocking findings, or incomplete', 'Criterion-by-criterion',
                'exact file locations', 'consequences', 'Optional polish',
                'Amendment dispositions', 'Missing evidence and limitations'):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, brief)
        procedure = self.read('review.md')
        for requirement in ('fresh review subagent', 'high-reasoning',
                            'independent session', 'ask the user', 'loss of independence',
                            '3 rounds', 'Re-review', 'restore modified candidate files',
                            'retain isolated candidates', 'test amendment'):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, procedure)

    def test_native_workers_and_persistent_candidate_have_distinct_rules(self):
        text = self.read('workspace.md')
        self.assertIn('native ephemeral workers', text)
        self.assertIn('final candidate', text)
        self.assertIn('harness-managed', text)
        self.assertIn('execution slug', text)

    def test_boost_entry_is_explicit_and_no_silent_substitution(self):
        text = self.read('adapters/antigravity.md')
        self.assertIn('/boost', text)
        self.assertIn('Do not claim a skill activates', text)
        self.assertIn('do not silently switch', text)
        self.assertIn('full-track', text)

    def test_runner_specific_mappings_live_only_in_active_adapter(self):
        discovery = self.read('discovery.md')
        for runner_api in ('invoke_subagent', 'TypeName:', 'view_file', 'run_command'):
            self.assertNotIn(runner_api, discovery)
        adapter = self.read('adapters/antigravity.md')
        self.assertIn('only when exposed', adapter)
        self.assertIn('inspect', adapter)
        one_shot = (ROOT.parent / 'one-shot/SKILL.md').read_text()
        self.assertIn('active adapter', one_shot)
        self.assertNotIn("Apply [the Antigravity adapter", one_shot)

    def test_proof_identifies_plan_and_missing_live_checks(self):
        text = self.read('verification.md') + self.read('templates/proof.md')
        self.assertIn('execution slug', text)
        self.assertIn('Missing evidence', text)
        self.assertIn('live Antigravity', text)

    def test_handoff_preserves_uncommitted_candidate_before_merge(self):
        text = self.read('handoff.md')
        self.assertIn('user commits the candidate branch', text)
        self.assertIn('actual repository verification commands', text)
        self.assertIn('git merge --squash', text)
        self.assertNotIn('npx tsc --noEmit && npm test', text)

    def test_worker_brief_protects_plan_and_records_executor(self):
        text = self.read('templates/implementer-brief.md')
        self.assertIn('Do not rewrite the plan', text)
        self.assertIn('executor', text)
        self.assertIn('execution slug', text)


if __name__ == '__main__':
    unittest.main()
