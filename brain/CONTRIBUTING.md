# CONTRIBUTING — team rules (3 members)

Team: **Abdul Wahid · Faseeh · Daniyal Badshah.** Ownership split is a
*proposal* in `brain/TEAM.md` — Wadi can re-assign; ownership means "leads and
explains first", never "only person who understands it" (the brief requires
**every** member to understand the complete project).

## Working rules
- Work directly on `main` (Wadi's standing rule) — small, frequent commits,
  Conventional Commits format (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
- One focused change per commit; message says what and why.
- Nobody merges code they cannot explain line-by-line in a viva.
- Every work session gets a log entry (see `brain/WORKFLOW.md`).
- Knowledge files (`kb/`) are edited carefully: any new predicate must be
  added to the vocabulary table in `brain/DATA_MODEL.md` in the same commit.
- Disagreement on design → write it in `brain/DECISIONS.md` as an ADR with
  options, decide once, move on.

## Folder ownership (proposal — mirrors brain/TEAM.md)
| Area | Lead |
|---|---|
| `models/` (DL) + integration glue | Abdul Wahid |
| `kb/` (facts, rules, vocabulary) | Faseeh |
| `engine/` + `app/` (inference, queries, traces) | Daniyal Badshah |
| `report/`, slides, demo | Shared; Daniyal assembles |
