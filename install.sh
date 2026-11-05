#!/usr/bin/env bash
# Install or uninstall the workflow skills.
#   Global:  symlinks each skill into ~/.claude/skills and ~/.agents/skills.
#   Project: copies skills into <repo>/.agents/skills and links them from <repo>/.claude/skills.
#   Hooks:   with --global --hooks, also installs the hooks in hooks/ for each harness found.
set -euo pipefail

PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$PACK_DIR/skills"
# Entries left behind by earlier versions of this pack.
RETIRED="_workflow domain-modeling fast-track full-track grilling human-tdd one-shot workflow-core project-discovery spec-alignment implementation-planning worktree-setup tdd-integrity task-dispatch independent-review verification-evidence integration-handoff"

usage() {
  cat <<'USAGE'
Usage:
  install.sh --global  [--dir <path>]... [--hooks] [--force] [--uninstall]
  install.sh --project <repo> [--force] [--uninstall]

  --global       Link skills into ~/.claude/skills (Claude Code) and ~/.agents/skills
                 (Codex, Gemini CLI, opencode, and other providers that read it).
  --project      Copy skills into <repo>/.agents/skills and link <repo>/.claude/skills to them.
  --dir <path>   With --global, also link into this skills directory. Repeatable.
  --hooks        With --global, also install the block-git-push hook for Claude Code,
                 Codex, and Antigravity (each only if installed). Needs jq.
                 With --uninstall, remove it again.
  --force        Replace existing entries with the same name.
  --uninstall    Remove this pack's skills and retired entries from earlier versions.
USAGE
}

MODE=""; TARGET=""; FORCE=0; UNINSTALL=0; HOOKS=0; EXTRA_DIRS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --global) MODE=global; shift ;;
    --project) [ -n "${2:-}" ] || { usage; exit 1; }; MODE=project; TARGET="$2"; shift 2 ;;
    --dir) [ -n "${2:-}" ] || { usage; exit 1; }; EXTRA_DIRS+=("$2"); shift 2 ;;
    --hooks) HOOKS=1; shift ;;
    --force) FORCE=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done
[ -n "$MODE" ] || { usage; exit 1; }
if [ "$HOOKS" -eq 1 ]; then
  [ "$MODE" = global ] || { echo "--hooks works with --global only" >&2; exit 1; }
  command -v jq >/dev/null || { echo "--hooks needs jq (https://jqlang.org)" >&2; exit 1; }
fi

skills() {
  for d in "$SRC"/*/; do [ -f "$d/SKILL.md" ] && basename "$d"; done
}

# Remove a retired entry only when it clearly came from this pack.
remove_retired() {
  local dir="$1" name path
  for name in $RETIRED; do
    path="$dir/$name"
    if [ -L "$path" ]; then
      case "$(readlink "$path")" in *agentic-workflow-skills*|../*) rm -f "$path"; echo "removed retired: $path" ;; esac
    elif [ -d "$path" ] && { [ "$name" = _workflow ] || grep -qs '_workflow/' "$path/SKILL.md"; }; then
      rm -rf "$path"; echo "removed retired: $path"
    fi
  done
}

# place <dest-dir> <name> <link|copy> <source>
place() {
  local dest="$1/$2" how="$3" from="$4"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" -eq 1 ]; then rm -rf "$dest"; else echo "skip, exists: $dest (use --force)"; return 0; fi
  fi
  if [ "$how" = link ]; then ln -s "$from" "$dest"; else cp -R "$from" "$dest"; fi
  echo "$how: $dest"
}

uninstall_dir() {
  local dir="$1" name
  [ -d "$dir" ] || return 0
  for name in $(skills); do
    if [ -e "$dir/$name" ] || [ -L "$dir/$name" ]; then rm -rf "${dir:?}/$name"; echo "removed: $dir/$name"; fi
  done
  remove_retired "$dir"
}

if [ "$MODE" = project ]; then
  [ -d "$TARGET" ] || { echo "Not a directory: $TARGET" >&2; exit 1; }
  TARGET="$(cd "$TARGET" && pwd)"
  SHARED="$TARGET/.agents/skills"; CLAUDE="$TARGET/.claude/skills"
  if [ "$UNINSTALL" -eq 1 ]; then uninstall_dir "$CLAUDE"; uninstall_dir "$SHARED"; exit 0; fi
  mkdir -p "$SHARED" "$CLAUDE"
  remove_retired "$SHARED"; remove_retired "$CLAUDE"
  for name in $(skills); do
    place "$SHARED" "$name" copy "$SRC/$name"
    place "$CLAUDE" "$name" link "../../.agents/skills/$name"
  done
  exit 0
fi

HOOK_NAME="block-git-push"
HOOK_LINK="$HOME/.agents/hooks/$HOOK_NAME.sh"

# json_edit <file> <jq args...>: rewrite a JSON file in place (keeping its
# permissions), saving the original as <file>.bak. A missing file starts as {}.
json_edit() {
  local file="$1" tmp; shift
  tmp="$(mktemp)"
  if [ -s "$file" ]; then jq "$@" "$file" > "$tmp"; else echo '{}' | jq "$@" > "$tmp"; fi || { rm -f "$tmp"; echo "failed to update $file" >&2; return 1; }
  if [ -f "$file" ]; then cp "$file" "$file.bak"; fi
  cat "$tmp" > "$file"; rm -f "$tmp"
}

# Drop any PreToolUse handler whose command runs this hook, and empty groups left behind.
STRIP_PRETOOL='
  if (.hooks.PreToolUse | type) == "array" then
    .hooks.PreToolUse |= (map(.hooks |= map(select((.command // "") | contains($name) | not)))
                          | map(select((.hooks | length) > 0)))
    | if (.hooks.PreToolUse | length) == 0 then del(.hooks.PreToolUse) else . end
    | if (.hooks | length) == 0 then del(.hooks) else . end
  else . end'

# Claude Code and Codex share the PreToolUse schema; Codex gets no matcher so its
# shell tool matches whatever it is named (the script ignores non-shell calls).
hooks_claude_style() {
  local file="$1" matcher="$2" label="$3" cmd
  cmd="'$HOOK_LINK'"
  if [ "$UNINSTALL" -eq 1 ]; then
    [ -f "$file" ] || return 0
    json_edit "$file" --arg name "$HOOK_NAME" "$STRIP_PRETOOL"
    echo "unhooked: $label ($file)"; return 0
  fi
  json_edit "$file" --arg name "$HOOK_NAME" --arg cmd "$cmd" --arg m "$matcher" "$STRIP_PRETOOL"'
    | .hooks.PreToolUse += [({hooks: [{type: "command", command: $cmd, timeout: 10}]}
                             + (if $m == "" then {} else {matcher: $m} end))]'
  echo "hooked: $label ($file)"
}

hooks_antigravity() {
  local file="$1" cmd
  cmd="'$HOOK_LINK'"
  if [ "$UNINSTALL" -eq 1 ]; then
    [ -f "$file" ] || return 0
    json_edit "$file" --arg name "$HOOK_NAME" 'del(.[$name])'
    echo "unhooked: Antigravity ($file)"; return 0
  fi
  json_edit "$file" --arg name "$HOOK_NAME" --arg cmd "$cmd" \
    '.[$name] = {PreToolUse: [{matcher: "run_command", hooks: [{type: "command", command: $cmd, timeout: 10}]}]}'
  echo "hooked: Antigravity ($file)"
}

install_hooks() {
  if [ "$UNINSTALL" -eq 1 ]; then
    if [ -L "$HOOK_LINK" ]; then rm -f "$HOOK_LINK"; echo "removed: $HOOK_LINK"; fi
  else
    mkdir -p "$(dirname "$HOOK_LINK")"
    ln -sfn "$PACK_DIR/hooks/$HOOK_NAME.sh" "$HOOK_LINK"; echo "link: $HOOK_LINK"
  fi
  if [ -d "$HOME/.claude" ]; then hooks_claude_style "$HOME/.claude/settings.json" Bash "Claude Code"; fi
  if [ -d "$HOME/.codex" ]; then hooks_claude_style "$HOME/.codex/hooks.json" "" "Codex"; fi
  if [ -d "$HOME/.gemini/config" ]; then hooks_antigravity "$HOME/.gemini/config/hooks.json"; fi
}

DIRS=("$HOME/.claude/skills" "$HOME/.agents/skills")
if [ ${#EXTRA_DIRS[@]} -gt 0 ]; then DIRS+=("${EXTRA_DIRS[@]}"); fi
for dir in "${DIRS[@]}"; do
  if [ "$UNINSTALL" -eq 1 ]; then uninstall_dir "$dir"; continue; fi
  mkdir -p "$dir"
  remove_retired "$dir"
  for name in $(skills); do place "$dir" "$name" link "$SRC/$name"; done
done
if [ "$HOOKS" -eq 1 ]; then install_hooks; fi
