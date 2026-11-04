#!/usr/bin/env bash
# Install or uninstall the workflow skills.
#   Global:  symlinks each skill into ~/.claude/skills and ~/.agents/skills.
#   Project: copies skills into <repo>/.agents/skills and links them from <repo>/.claude/skills.
set -euo pipefail

PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$PACK_DIR/skills"
# Entries left behind by earlier versions of this pack.
RETIRED="_workflow domain-modeling fast-track full-track grilling human-tdd one-shot workflow-core project-discovery spec-alignment implementation-planning worktree-setup tdd-integrity task-dispatch independent-review verification-evidence integration-handoff"

usage() {
  cat <<'USAGE'
Usage:
  install.sh --global  [--dir <path>]... [--force] [--uninstall]
  install.sh --project <repo> [--force] [--uninstall]

  --global       Link skills into ~/.claude/skills (Claude Code) and ~/.agents/skills
                 (Codex, Gemini CLI, opencode, and other providers that read it).
  --project      Copy skills into <repo>/.agents/skills and link <repo>/.claude/skills to them.
  --dir <path>   With --global, also link into this skills directory. Repeatable.
  --force        Replace existing entries with the same name.
  --uninstall    Remove this pack's skills and retired entries from earlier versions.
USAGE
}

MODE=""; TARGET=""; FORCE=0; UNINSTALL=0; EXTRA_DIRS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --global) MODE=global; shift ;;
    --project) [ -n "${2:-}" ] || { usage; exit 1; }; MODE=project; TARGET="$2"; shift 2 ;;
    --dir) [ -n "${2:-}" ] || { usage; exit 1; }; EXTRA_DIRS+=("$2"); shift 2 ;;
    --force) FORCE=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done
[ -n "$MODE" ] || { usage; exit 1; }

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

DIRS=("$HOME/.claude/skills" "$HOME/.agents/skills")
if [ ${#EXTRA_DIRS[@]} -gt 0 ]; then DIRS+=("${EXTRA_DIRS[@]}"); fi
for dir in "${DIRS[@]}"; do
  if [ "$UNINSTALL" -eq 1 ]; then uninstall_dir "$dir"; continue; fi
  mkdir -p "$dir"
  remove_retired "$dir"
  for name in $(skills); do place "$dir" "$name" link "$SRC/$name"; done
done
