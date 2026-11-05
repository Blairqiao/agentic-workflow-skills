---
name: visual-proof
description: Take screenshots of the running app as proof that a UI change works, and embed them in a proof document. Use after UI work, when the user asks for screenshots or visual proof, or at the end of `orchestrate` when the UI changed.
---

# Visual proof

Show that the change works in the real app. A passing build doesn't prove a UI works.

## 1. Run the app

Find the dev command in the README or manifest and start it in the background. Use the project's existing dev server if one is already running. Wait until it responds before you shoot.

## 2. Pick a screenshot tool

Running this skill counts as the user asking for browser work, including when `orchestrate` or a plan's final check calls for it. Harness rules against unrequested browser checks don't apply here.

Use the first one that works:

1. **T3 Code preview tools.** They are often deferred, so load them first with ToolSearch: `select:mcp__t3-code__preview_open,mcp__t3-code__preview_snapshot,mcp__t3-code__preview_resize,mcp__t3-code__preview_act,mcp__t3-code__t3_preview_close`. Then:
   - Call `preview_open` with `target: {kind: "environment-port", port: <dev port>, path: "/..."}`, `open: false`, and `reuseExistingTab: false`. Keep the returned `tabId`.
   - For mobile, call `preview_resize` with `mode: "preset", preset: "iphone-14-pro-max"`. Go back with `mode: "fill"`.
   - Call `preview_snapshot` with `save: true`. Without `save: true`, no file is written. It returns a `screenshotPath` under `~/.t3/userdata/browser-artifacts/`. Copy that file into `.agent-docs/proofs/images/`.
   - Use `preview_act` for clicks and typing, then snapshot again.
   - When you're done, call `t3_preview_close` on your tab.
2. **Another browser MCP server**, such as Playwright or Chrome DevTools, or the harness's built-in browser.
3. **Playwright in the project.** If it's in the project's dependencies, run `npx playwright screenshot --viewport-size=1280,800 <url> <file>.png`. Don't use `npx` to fetch it otherwise, since that installs a new dependency.
4. **Desktop or native apps.** Use `screencapture -x <file>.png` on macOS. If it fails or the image comes out blank, the app running the agent needs Screen Recording permission in System Settings > Privacy & Security.

Don't install a new tool without asking. If nothing works, report the exact error from each attempt, not just "screenshots aren't available", and describe what you checked by hand instead.

## 3. Capture

Plan the shots from the task's done-when criteria. For each changed screen or state:

- **The state that proves the change.** Show the new button, the saved item, the error message.
- **Before and after**, if it's a fix and the before state is easy to reproduce.
- **Desktop (1280×800) and mobile (390×844)** when layout changed.
- **Interaction results.** Click, type, or submit, then capture the result, not just the initial page.

Screenshots and page snapshots are large, so take each shot once, and retake it only if it failed or the page changed. Look at every screenshot after you take it. A blank page, a wrong route, or an error overlay is a failure. Fix it or report it. Never present it as proof.

Save images to `.agent-docs/proofs/images/<feature>-<shot>.png`, with `.agent-docs/` listed in `.git/info/exclude`.

## 4. Write the proof

Create or update `.agent-docs/proofs/<feature>.md`:

```markdown
# <Feature> proof

**What was checked.** One line per done-when criterion and whether it passed.

## <Screen or state>

![Desktop: saved todo appears at top of list](/.agent-docs/proofs/images/<feature>-saved-desktop.png)

Steps: open /todos, type "milk", press Enter.

## Not verified

Anything you couldn't check and why.
```

Use repository-rooted image paths that start with `/.agent-docs/`, never absolute machine paths. Keep captions specific. "Screenshot 1" tells the reader nothing.

## 5. Report

Stop any dev server you started. In chat, list what passed and what didn't. End your chat message with a clickable markdown link to the proof file on its own line, using the absolute path: `[<feature>.md](/abs/path/to/repo/.agent-docs/proofs/<feature>.md)`. A bare or relative path isn't clickable.
