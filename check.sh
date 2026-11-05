#!/usr/bin/env bash
# Sanity checks: frontmatter name matches folder, description present, relative links resolve.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
fail=0

for skill in skills/*/SKILL.md; do
  dir="$(basename "$(dirname "$skill")")"
  name="$(awk '/^---$/{n++; next} n==1 && /^name:/{print $2; exit}' "$skill")"
  desc="$(awk '/^---$/{n++; next} n==1 && /^description:/{print; exit}' "$skill")"
  [ "$name" = "$dir" ] || { echo "FAIL $skill: name '$name' does not match folder '$dir'"; fail=1; }
  [ -n "$desc" ] || { echo "FAIL $skill: missing description"; fail=1; }
done

for md in AGENTS.md README.md skills/*/*.md; do
  base="$(dirname "$md")"
  # Markdown links outside code fences, skipping URLs, anchors, and placeholders.
  for link in $(awk '/^```/{f=!f; next} !f' "$md" | grep -o '\](\([^)]*\))' | sed 's/^](//; s/)$//; s/#.*//'); do
    case "$link" in ''|http*|mailto:*|*'<'*) continue ;; esac
    if [ "${link#/}" != "$link" ]; then path=".${link}"; else path="$base/$link"; fi
    [ -e "$path" ] || { echo "FAIL $md: broken link $link"; fail=1; }
  done
done

bash -n install.sh || fail=1
for hook in hooks/*.sh; do bash -n "$hook" || fail=1; [ -x "$hook" ] || { echo "FAIL $hook: not executable"; fail=1; }; done
[ "$fail" -eq 0 ] && echo "ok"
exit "$fail"
