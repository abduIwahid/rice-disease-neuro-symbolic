# WORKFLOW — how the team + agents work on this project

## Roles (separate passes, no overlap)
Planner (brain/docs) → Builder (one module at a time) → Reviewer (checks
against PRD / DATA_MODEL / TESTING). The three members rotate Reviewer for
each other's modules (TEAM.md ownership).

## Task loop
1. Read `00-START-HERE.md`, `changes/current-state.md`, last 3 session files.
2. Pick ONE task ≤ ~30 min from BUILD_PLAN.md's current phase.
3. Build it. 4. Test it (TESTING.md). 5. Commit (Conventional Commits,
referencing the session file). 6. Log it (below).

## Logging system (HARD RULE — "git for conversations")
After EVERY feature/fix/decision:
1. Create `changes/sessions/YYYY-MM-DD-NN-short-title.md`: goal/request,
   what was done (files), decisions + reasoning, problems + fixes,
   status (Done/Partial/Blocked), next steps.
2. Append to `changes/changelog.md`: Change → Reason → Affected Area →
   Impact → Evidence → Status.
3. Update `changes/current-state.md` (what exists, what's incomplete).
4. Tick BUILD_PLAN.md checkboxes; add ADRs to DECISIONS.md when a real
   choice was made.
5. Never invent history. Tag claims Verified / Inferred / Unknown.

## Freeze rules
- **Approval freeze:** Phases 2+ do not exist until Phase 0's gate clears.
- **Dependency freeze:** end of Phase 5 — no new libraries after, without
  all three members agreeing (log as ADR).
- **KB freeze:** 48h before the demo (whenever the date is announced) —
  facts/rules change only to fix a failing test.
