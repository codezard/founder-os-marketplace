---
description: Show which Founder OS stage gates are open or closed for the current project's founder/ workspace.
---

# /founder-os:status

Run the gate checker against the founder's workspace and report where they are on the stage map.

## What to do

1. Locate the `founder/` workspace (in the current project root, or ask the founder where it is).
2. Run the checker:

   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/scripts/gate_check.py" --workspace <path-to>/founder
   ```

   (Omit `--workspace` to auto-detect `./founder` or `../founder`.)
3. Relay the output plainly: for each stage show CLOSED/OPEN, which artifacts exist, which are missing, and the gate condition.
4. Name the current stage and remind the founder not to run later-stage skills while an earlier gate is open (principle: don't run stage N+1 while stage N's gate is open).
5. If no workspace exists yet, point them to `find-business-idea` to start Stage 0.

Do not fabricate progress. A gate is only closed when its artifacts exist and one declares a `Gate: PASS` line. Reference: `references/stage-map.md`.
