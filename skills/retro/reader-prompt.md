# Reader prompt

Fill in the `<...>` parts and send this to a cheap reader. Send one batch per reader.

````text
You are reading distilled chat logs between a human and coding agents. Your job is to find places where the human did work that a better workflow could have removed. Read only. Don't edit any files.

Files (in <out>/sessions/): <the file names from one line of batches.txt>

Each file is one thread. Its header gives the project, the thread title, the date, the model, tool counts, how often the agent stopped to ask the human, and how many runs the human interrupted. `[human N]` is what the human typed. `[agent, end of reply]` is the last part of the agent's answer just before it. `[human interrupted the agent here]` means the human stopped that reply partway.

Look for these, and only these:

1. Repeated requests: the same instruction or kind of request typed in several sessions, such as "commit this", "run the tests first", or "use the planning skill".
2. Corrections: the human redirects the agent ("no", "I said", "stop", "don't", "again", "why did you") because of a habit, not a one-off misunderstanding.
3. Re-explaining: the human restates context, preferences, or rules the agent should already know.
4. Manual relay: the human copies output between agents or sessions, pastes errors back, or kicks off the next step by hand.
5. Friction: a long back-and-forth to get something simple done, interrupts, the agent asking questions it could have answered itself, or a heavy tool pattern visible in the tool counts.

Skip anything that's only about one project's code, data, or bugs. Keep a finding when it would plausibly happen in any project. If the example happens to be project-specific, describe the general pattern and use the project only as the example.

Never copy secrets, tokens, keys, emails, or personal details into your report, even ones that weren't redacted.

Report in this exact format, most frequent first, at most 15 findings:

## <short name of the pattern>
- Kind: repeated request | correction | re-explaining | manual relay | friction
- Seen in: <count> sessions across <count> projects
- Evidence: <file name> [human N]: "<quote, under 25 words>"   (2 to 4 lines like this)
- What the human was really doing: <one sentence>

End with one line: `Read <n> sessions. <n> findings.`
````
