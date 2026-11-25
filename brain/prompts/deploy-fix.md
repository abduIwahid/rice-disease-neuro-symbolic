# Prompt — Deploy/demo fix

Read first: brain/DEPLOYMENT.md, brain/DEMO_PITCH.md (backup plan), brain/changes/current-state.md.

Problem: <what breaks on the demo machine / in the demo run>

Rules:
- The goal is a clean `python -m app.main --demo` on the demo machine — optimise for that, nothing else.
- Prefer pinning, bundling or caching over re-architecting (no new dependencies this close to the demo without an ADR).
- Verify with networking disabled — the demo must not depend on the internet.
- Log the session per brain/WORKFLOW.md, including the exact environment delta that caused the failure.
