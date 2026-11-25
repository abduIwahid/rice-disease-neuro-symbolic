# Prompt — Bugfix

Read first: brain/00-START-HERE.md, brain/changes/current-state.md, the session file that introduced the area, brain/TESTING.md.

Bug: <symptom + where it shows>

Rules:
- Reproduce first (a failing test or a scripted run); no fix without a reproduction.
- Smallest change that fixes the root cause — no drive-by refactors.
- The reproduction becomes a regression test in tests/ in the same change.
- If the bug is in engine/ semantics (unification, chaining, NAF), re-check the design notes in brain/ARCHITECTURE.md before touching code — the design wins ties.
- Log the session per brain/WORKFLOW.md (problem + fix section is mandatory).
