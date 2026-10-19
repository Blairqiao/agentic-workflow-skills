#!/usr/bin/env bash
# Install or uninstall the portable agentic workflow skills for Google Antigravity.
set -euo pipefail

PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$PACK_DIR/skills"
RETIRED_SKILLS="workflow-core project-discovery spec-alignment implementation-planning worktree-setup tdd-integrity task-dispatch independent-review verification-evidence integration-handoff"

usage() {
  cat <<'USAGE'
Usage:
  install.sh --project <repo-path> [--force] [--uninstall]
  install.sh --global [--force] [--uninstall]

  --project <path>  Copy skills and shared docs into <path>/.agents/skills.
  --global          Link skills into ~/.gemini/config/skills and ~/.gemini/antigravity-cli/skills.
  --force           Replace existing entries with the same name.
  --uninstall       Remove installed workflow skills, _workflow, and retired bundle entries.
USAGE
}

MODE=""; TARGET=""; FORCE=0; UNINSTALL=0
while [ $# -gt 0 ]; do
  case "$1" in
    --project)
      if [ $# -lt 2 ] || [ -z "${2:-}" ]; then
        echo "Missing path for --project" >&2
        usage
        exit 1
      fi
      MODE=project; TARGET="$2"; shift 2 ;;
    --global) MODE=global; shift ;;
    --force) FORCE=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done
[ -n "$MODE" ] || { usage; exit 1; }

# Returns 0 when the destination is free to write, 1 when it should be skipped.
free_slot() {
  local dest="$1"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" -eq 1 ]; then rm -rf "$dest"; return 0; fi
    echo "skip, already exists: $dest"
    return 1
  fi
  return 0
}

skill_dirs() {
  for d in "$SKILLS_SRC"/*/; do
    [ -f "$d/SKILL.md" ] || continue
    echo "${d%/}"
  done
}

# Shared procedures have no SKILL.md and must travel beside every bundle.
install_docs() {
  local dir="$1" how="$2" base="${3:-$SKILLS_SRC}"
  free_slot "$dir/_workflow" || return 0
  if [ "$how" = link ]; then
    ln -s "$base/_workflow" "$dir/_workflow"
  else
    cp -R "$SKILLS_SRC/_workflow" "$dir/_workflow"
  fi
}

link_all() {
  local dir="$1"
  mkdir -p "$dir"
  install_docs "$dir" link
  while IFS= read -r src; do
    local name; name="$(basename "$src")"
    free_slot "$dir/$name" || continue
    ln -s "$src" "$dir/$name"
    echo "linked: $dir/$name"
  done < <(skill_dirs)
}

uninstall_dir() {
  local dir="$1"
  [ -d "$dir" ] || return 0
  if [ -e "$dir/_workflow" ] || [ -L "$dir/_workflow" ]; then
    rm -rf "$dir/_workflow"
    echo "removed: $dir/_workflow"
  fi
  while IFS= read -r src; do
    local name; name="$(basename "$src")"
    if [ -e "$dir/$name" ] || [ -L "$dir/$name" ]; then
      rm -rf "$dir/$name"
      echo "removed: $dir/$name"
    fi
  done < <(skill_dirs)
  for retired in $RETIRED_SKILLS; do
    if [ -e "$dir/$retired" ] || [ -L "$dir/$retired" ]; then
      rm -rf "$dir/$retired"
      echo "removed retired: $dir/$retired"
    fi
  done
}

if [ "$UNINSTALL" -eq 1 ]; then
  if [ "$MODE" = project ]; then
    [ -n "$TARGET" ] && [ -d "$TARGET" ] || { echo "Not a directory: $TARGET" >&2; exit 1; }
    TARGET="$(cd "$TARGET" && pwd)"
    uninstall_dir "$TARGET/.agents/skills"
  elif [ "$MODE" = global ]; then
    uninstall_dir "$HOME/.gemini/config/skills"
    uninstall_dir "$HOME/.gemini/antigravity-cli/skills"
  fi
  exit 0
fi

if [ "$MODE" = project ]; then
  [ -n "$TARGET" ] && [ -d "$TARGET" ] || { echo "Not a directory: $TARGET" >&2; exit 1; }
  TARGET="$(cd "$TARGET" && pwd)"
  AG="$TARGET/.agents/skills"
  mkdir -p "$AG"
  install_docs "$AG" copy
  while IFS= read -r src; do
    name="$(basename "$src")"
    free_slot "$AG/$name" || continue
    cp -R "$src" "$AG/$name"
    echo "copied: $AG/$name"
  done < <(skill_dirs)
fi

if [ "$MODE" = global ]; then
  link_all "$HOME/.gemini/config/skills"
  link_all "$HOME/.gemini/antigravity-cli/skills"
fi
