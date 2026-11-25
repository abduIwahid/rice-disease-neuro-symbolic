# Prompt — Review

Read first: brain/00-START-HERE.md, brain/PRD.md, brain/DATA_MODEL.md, brain/TESTING.md, the change under review (diff or files).

Review: <scope>

Check, in order:
1. Scope — is everything in PRD MUST/SHOULD or flagged as COULD-creep?
2. Brain–code sync — predicates/rules in code match DATA_MODEL.md exactly (names, arities, IDs).
3. Engine correctness — unification (occurs check, standardising apart), chaining termination, NAF usage matches the documented policy.
4. Traces — every answer path produces a trace in the API_SPEC.md format.
5. Tests — new behaviour has E/S coverage; the success/failure/conflict trio is intact.
6. Integrity — no copied code without citation; comments explain, not decorate.
Report findings as a list (blocker / should-fix / note). Do not edit code in a review pass.
