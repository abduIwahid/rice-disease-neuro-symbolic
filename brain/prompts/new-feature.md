# Prompt — New feature

Read first: brain/00-START-HERE.md, brain/changes/current-state.md, last 3 session files, brain/PRD.md (scope), brain/BUILD_PLAN.md (current phase).

Feature: <name + one-line description>

Rules:
- Confirm the feature is in PRD scope (MUST/SHOULD/COULD) and in the current BUILD_PLAN phase. If not, stop and flag it.
- **Phase gate:** if Phase 0 (paper + domain approval) has not cleared, no implementation work proceeds — notes only.
- One task ≤ ~30 min; split if bigger. Respect the dependency freeze — no new libraries without an ADR.
- New predicate or rule? It goes into brain/DATA_MODEL.md (vocabulary / rule plan) in the same change.
- Add or update tests (TESTING.md E/S series) for anything touching engine/, kb/ or the integration path.
- Log the session per brain/WORKFLOW.md before ending.
