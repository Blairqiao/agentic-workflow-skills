"""Check executor boundaries and repair authorization in installed track guidance."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DEPRECATED_PHASE_TERMS = ('R' + 'oom 1', 'R' + 'oom 2', 'two-r' + 'oom')


def skill(name):
    return (ROOT / 'skills' / name / 'SKILL.md').read_text()


class TrackContractTests(unittest.TestCase):
    def test_full_is_delegated_non_boost_execution(self):
        text = skill('full-track')
        self.assertIn('non-boost', text)
        self.assertNotIn('/boost', text)
        self.assertNotIn('with boost capabilities', text)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, text)
        for required in ('ready plan', 'without repeating approval',
                         'Mandate subagent delegation', 'Material scope changes return to the planning phase'):
            self.assertIn(required, text)

    def test_fast_reuses_only_approved_defect_authorization(self):
        text = skill('fast-track')
        for required in ('approved behavior', 'parent plan', 'without another approval',
                         "parent's proof", 'non-boost',
                         'No implementation subagents', 'regression test', 'independent review'):
            self.assertIn(required, text)
        self.assertNotIn('pause for approval before modifying code', text)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, text)

    def test_standalone_fast_runs_in_single_chat(self):
        text = skill('fast-track')
        for required in ('Standalone', 'single chat', 'mini-spec',
                         '.agent-docs/fast-track/<feature>.md'):
            self.assertIn(required, text)
        for obsolete in DEPRECATED_PHASE_TERMS:
            self.assertNotIn(obsolete, text)
        template = (ROOT / 'skills/_workflow/templates/fast-track.md').read_text()
        for required in ('Parent plan', 'Authorization boundary', 'Invalidated evidence'):
            self.assertIn(required, template)

    def test_harness_specific_tracks_removed_from_public_bundle(self):
        self.assertFalse((ROOT / 'skills/boost-track').exists(), 'boost-track must not be in public root bundle')
        self.assertFalse((ROOT / 'skills/orchestration-track').exists(), 'orchestration-track must not be in public root bundle')

    def test_one_shot_preserves_autonomy_with_either_executor(self):
        text = skill('one-shot')
        for required in ('explicitly requested',
                         'boost and non-boost', 'Record the selected executor',
                         'Do not silently switch', 'without interactive',
                         'native boost owns', 'single run document'):
            self.assertIn(required, text)
        for obsolete in (*DEPRECATED_PHASE_TERMS, 'exception to the two-' + 'r' + 'oom model'):
            self.assertNotIn(obsolete, text)
        metadata = (ROOT / 'skills/one-shot/agents/openai.yaml').read_text()
        self.assertIn('allow_implicit_invocation: false', metadata)

    def test_zero_google_model_naming_conventions(self):
        for path in (ROOT / 'skills/_workflow').rglob('*.md'):
            text = path.read_text().lower()
            for forbidden in ('ar' + 'gon', 'fla' + 'sh_lite', 'fla' + 'sh'):
                self.assertNotIn(forbidden, text, f"Forbidden Google model naming '{forbidden}' found in {path.name}")


if __name__ == '__main__':
    unittest.main()
