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

    def test_fast_requires_approval_for_each_follow_up(self):
        text = skill('fast-track')
        for required in ('approved behavior', 'parent plan', 'every follow-up repair',
                         "parent's proof", 'non-boost',
                         'No implementation subagents', 'regression test', 'independent review'):
            self.assertIn(required, text)
        self.assertIn('pause for explicit approval before editing code or tests', text)
        self.assertNotIn('without another approval', text)
        template = (ROOT / 'skills/_workflow/templates/fast-track.md').read_text()
        self.assertIn('every follow-up repair', template)
        self.assertIn('Parent behavior approval does not substitute', template)
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

    def test_fast_has_linear_checks_without_recursive_phase_loading(self):
        text = skill('fast-track')
        self.assertNotIn('follow its phase sequence', text)
        for required in ('1. **Fit', '2. **Authorize', '3. **Starting state',
                         '4. **Red and green', '5. **Review', '6. **Handoff',
                         'git worktree list --porcelain', 'git status',
                         'git check-ignore', '.git/info/exclude',
                         'starting revision', 'pre-existing', 'CONTEXT.md',
                         'active adapter', 'only when',
                         'Test amendments', 'three', 'Stage candidate'):
            self.assertIn(required, text)
        self.assertIn('without loading the full discovery/design/planning chain', text)
        self.assertIn('before writing workflow records', text.lower())

    def test_entries_reuse_core_and_load_only_current_operations(self):
        for name in ('fast-track', 'full-track', 'one-shot', 'orchestration-track'):
            text = skill(name)
            self.assertIn('supplied-context reuse', text, name)
            self.assertNotIn('follow its phase sequence', text, name)
        planning = skill('planning')
        self.assertIn('supplied-context reuse', planning)
        self.assertIn('when requirements need exploration', planning.lower())
        self.assertIn('supplied-context reuse', skill('research'))

    def test_gemini_orchestration_preserves_delegated_vertical_slices(self):
        text = skill('orchestration-track')
        for required in ('large multi-part initiatives', 'project jumpstarts',
                         'complex multi-service features', 'full codebase audits',
                         'vertical slices', 'Mandate subagent delegation',
                         'disjoint', 'ready plan', 'independent review',
                         'without repeating approval', 'active adapter'):
            self.assertIn(required, text)
        self.assertNotIn('invoke_subagent', text)
        self.assertNotIn('Gemini 4 Argon', text)
        self.assertNotIn('/boost', text)
        core = (ROOT / 'skills/_workflow/core.md').read_text()
        self.assertIn('Orchestration-track is automatically selected', core)
        self.assertNotIn('Experimental orchestration requires explicit selection', core)
        agents = (ROOT / 'AGENTS.md').read_text()
        self.assertIn('orchestration-track', agents)
        self.assertFalse((ROOT / 'skills/boost-track').exists())

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
