#!/usr/bin/env bash
# Install the portable agentic workflow skills for one or more agent harnesses.
set -euo pipefail

PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$PACK_DIR/skills"
ENTRY_SKILLS="full-track fast-track one-shot"
ALL_HARNESSES="claude,codex,opencode,gemini,antigravity"

usage() {
  cat <<'USAGE'
Usage:
  install.sh --project <repo-path> [--harness list] [--force]
  install.sh --global [--harness list] [--force]

  --project <path>  Copy skills into <path>/.agents/skills and link
                    <path>/.claude/skills to them. Commit these to share.
  --global          Link skills into your user-level skill directories.
  --harness list    Comma-separated subset of: claude,codex,opencode,gemini,antigravity
                    (default: all)
  --force           Replace existing entries with the same name.
USAGE
}

MODE=""; TARGET=""; FORCE=0; HARNESSES="$ALL_HARNESSES"
while [ $# -gt 0 ]; do
  case "$1" in
    --project) MODE=project; TARGET="${2:-}"; shift 2 ;;
    --global) MODE=global; shift ;;
    --harness) HARNESSES="${2:-}"; shift 2 ;;
    --force) FORCE=1; shift ;;
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

# Claude Code copy of an entry skill, with model invocation disabled.
claude_entry_copy() {
  local src="$1" dest="$2"
  cp -R "$src" "$dest"
  awk '!done && /^name:/ { print; print "disable-model-invocation: true"; done = 1; next } { print }' \
    "$src/SKILL.md" > "$dest/SKILL.md"
}

skill_dirs() { for d in "$SKILLS_SRC"/*/; do echo "${d%/}"; done; }

link_all() {
  local dir="$1"
  mkdir -p "$dir"
  for src in $(skill_dirs); do
    local name; name="$(basename "$src")"
    free_slot "$dir/$name" || continue
    ln -s "$src" "$dir/$name"
    echo "linked: $dir/$name"
  done
}

install_claude() {
  # $1 = destination dir, $2 = "link" to link non-entry skills to $3, or "copy"
  local dir="$1" how="$2" base="${3:-}"
  mkdir -p "$dir"
  for src in $(skill_dirs); do
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
  done
}

if [ "$MODE" = project ]; then
  [ -n "$TARGET" ] && [ -d "$TARGET" ] || { echo "Not a directory: $TARGET" >&2; exit 1; }
  TARGET="$(cd "$TARGET" && pwd)"
  if wants codex || wants opencode || wants gemini || wants antigravity; then
    AG="$TARGET/.agents/skills"
    mkdir -p "$AG"
    for src in $(skill_dirs); do
      name="$(basename "$src")"
      free_slot "$AG/$name" || continue
      cp -R "$src" "$AG/$name"
      echo "copied: $AG/$name"
    done
    wants claude && install_claude "$TARGET/.claude/skills" link "../../.agents/skills"
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
