# Prompt — Refactor

Read first: brain/00-START-HERE.md, brain/changes/current-state.md, brain/ARCHITECTURE.md (module map + conventions).

Refactor: <what + why>

Rules:
- Behaviour must not change: full pytest run before AND after, same results.
- Module boundaries in ARCHITECTURE.md are the target shape — refactor toward them, not away.
- kb/ data files: a refactor never changes a fact or rule's meaning; vocabulary table stays in sync in the same commit.
- One refactor per session; log it per brain/WORKFLOW.md.
