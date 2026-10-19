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
