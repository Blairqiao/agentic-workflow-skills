#!/usr/bin/env bash
# Install or uninstall the portable agentic workflow skills for one or more agent harnesses.
set -euo pipefail

PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$PACK_DIR/skills"
ENTRY_SKILLS="one-shot"
RETIRED_SKILLS="workflow-core project-discovery spec-alignment implementation-planning worktree-setup tdd-integrity task-dispatch independent-review verification-evidence integration-handoff"
ALL_HARNESSES="claude,codex,opencode,gemini,antigravity"

usage() {
  cat <<'USAGE'
Usage:
  install.sh --project <repo-path> [--harness list] [--force] [--uninstall]
  install.sh --global [--harness list] [--force] [--uninstall]

  --project <path>  Copy skills and shared docs into <path>/.agents/skills and link
                    <path>/.claude/skills to them. Commit these to share.
  --global          Link skills into your user-level skill directories.
  --harness list    Comma-separated subset of: claude,codex,opencode,gemini,antigravity
                    (default: all)
  --force           Replace existing entries with the same name.
  --uninstall       Remove installed workflow skills, _workflow, and retired bundle entries.
USAGE
}

MODE=""; TARGET=""; FORCE=0; UNINSTALL=0; HARNESSES="$ALL_HARNESSES"
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
    --harness)
      if [ $# -lt 2 ] || [ -z "${2:-}" ]; then
        echo "Missing value for --harness" >&2
        usage
        exit 1
      fi
      HARNESSES="$2"; shift 2 ;;
    --force) FORCE=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done
[ -n "$MODE" ] || { usage; exit 1; }

wants() { case ",$HARNESSES," in *",$1,"*) return 0 ;; esac; return 1; }
is_entry() { case " $ENTRY_SKILLS " in *" $1 "*) return 0 ;; esac; return 1; }

for h in ${HARNESSES//,/ }; do
  case "$h" in claude|codex|opencode|gemini|antigravity) ;; *) echo "Unknown harness: $h" >&2; exit 1 ;; esac
done

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

# Claude Code copy of a manual-only entry skill, with model invocation disabled and Codex adapter removed.
claude_entry_copy() {
  local src="$1" dest="$2"
  cp -R "$src" "$dest"
  rm -rf "$dest/agents"
  awk '
    NR == 1 && /^---$/ { in_fm = 1; print; next }
    in_fm && /^---$/ { in_fm = 0; print; next }
    in_fm && !done && /^name:/ { print; print "disable-model-invocation: true"; done = 1; next }
    { print }
  ' "$src/SKILL.md" > "$dest/SKILL.md"
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

install_claude() {
  # $1 = destination dir, $2 = "link" to link non-entry skills to $3, or "copy"
  local dir="$1" how="$2" base="${3:-}"
  mkdir -p "$dir"
  install_docs "$dir" "$how" "${base:-$SKILLS_SRC}"
  while IFS= read -r src; do
    local name; name="$(basename "$src")"
    free_slot "$dir/$name" || continue
    if is_entry "$name"; then
      claude_entry_copy "$src" "$dir/$name"
      echo "copied, manual-only: $dir/$name"
    elif [ "$how" = link ]; then
      ln -s "$base/$name" "$dir/$name"
      echo "linked: $dir/$name"
    else
      cp -R "$src" "$dir/$name"
      echo "copied: $dir/$name"
    fi
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
    if wants codex || wants opencode || wants gemini || wants antigravity; then
      uninstall_dir "$TARGET/.agents/skills"
    fi
    if wants claude; then
      uninstall_dir "$TARGET/.claude/skills"
    fi
  elif [ "$MODE" = global ]; then
    if wants codex || wants opencode || wants gemini; then uninstall_dir "$HOME/.agents/skills"; fi
    if wants claude; then uninstall_dir "$HOME/.claude/skills"; fi
    if wants antigravity; then
      uninstall_dir "$HOME/.gemini/config/skills"
      uninstall_dir "$HOME/.gemini/antigravity-cli/skills"
    fi
  fi
  exit 0
fi

if [ "$MODE" = project ]; then
  [ -n "$TARGET" ] && [ -d "$TARGET" ] || { echo "Not a directory: $TARGET" >&2; exit 1; }
  TARGET="$(cd "$TARGET" && pwd)"
  if wants codex || wants opencode || wants gemini || wants antigravity; then
    AG="$TARGET/.agents/skills"
    mkdir -p "$AG"
    install_docs "$AG" copy
    while IFS= read -r src; do
      name="$(basename "$src")"
      free_slot "$AG/$name" || continue
      cp -R "$src" "$AG/$name"
      echo "copied: $AG/$name"
    done < <(skill_dirs)
    if wants claude; then
      install_claude "$TARGET/.claude/skills" link "../../.agents/skills"
    fi
  elif wants claude; then
    install_claude "$TARGET/.claude/skills" copy
  fi
fi

if [ "$MODE" = global ]; then
  if wants codex || wants opencode || wants gemini; then link_all "$HOME/.agents/skills"; fi
  if wants claude; then install_claude "$HOME/.claude/skills" link "$SKILLS_SRC"; fi
  if wants antigravity; then
    link_all "$HOME/.gemini/config/skills"
    link_all "$HOME/.gemini/antigravity-cli/skills"
  fi
fi

if wants claude && wants opencode; then
  echo
  echo "note: opencode also reads .claude/skills, so it may list each skill twice."
  echo "      If it complains, rerun with --harness to leave one of them out."
fi
