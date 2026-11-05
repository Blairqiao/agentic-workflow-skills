#!/usr/bin/env bash
# Pre-tool hook: block `git push`. Commits are allowed.
# Installed by `install.sh --global --hooks` for Claude Code, Codex, and
# Antigravity. It also reads Copilot CLI's payload shape. Claude Code, Codex,
# and Copilot deny on exit code 2 with a stderr reason; Antigravity denies on
# stdout JSON {"decision":"deny"}.
#
# Matches `git push`, `git -C dir push`, `cd x && git push`, etc.,
# but not `git commit -m "push fix"`.
input=$(cat)
cmd=$(printf '%s' "$input" | jq -r '
  def str: if type == "array" then join(" ") elif type == "string" then . else "" end;
  (.toolArgs | if type == "string" then (fromjson? // {}) else (. // {}) end) as $copilot
  | [.tool_input.command, .tool_input.cmd, $copilot.command, $copilot.cmd,
     .toolCall.args.CommandLine]
  | map(select(. != null) | str) | join("\n")
')
reason="Blocked: git push is disabled for agents. Commit locally; the user pushes."
antigravity=$(printf '%s' "$input" | jq -r 'has("toolCall")' 2>/dev/null)

if printf '%s\n' "$cmd" | grep -qE '(^|[;&|({[:space:]])git([[:space:]]+-[^[:space:]]+([[:space:]]+[^-[:space:]][^[:space:]]*)?)*[[:space:]]+push([[:space:]]|$)'; then
  if [ "$antigravity" = "true" ]; then
    jq -nc --arg r "$reason" '{decision: "deny", reason: $r}'
    exit 0
  fi
  echo "$reason" >&2
  exit 2
fi
[ "$antigravity" = "true" ] && echo '{"decision":"allow"}'
exit 0
