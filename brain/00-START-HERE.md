# 00 — START HERE

**One-liner:** A Deep Learning model's predictions become symbolic facts; a
hand-built knowledge base + inference engine reasons over them and *shows its
proof* — an implementation of a 2026 neuro-symbolic research paper, in Python.

**Current phase:** Phase 0 — paper shortlist. Brain complete; no code yet.
See `changes/current-state.md`.

## ⚠️ TWO DIFFERENT BRIEFS ARRIVED ON 2026-11-24 — READ THIS FIRST
| When | Document | Project it describes |
|---|---|---|
| Morning | `~/workspace/user/files/Project_Description.pdf` | SWI-Prolog expert system, 40+ facts / 15+ rules, zip `AIC372_Project_GroupNo.zip` |
| **Afternoon** | **`~/workspace/user/files/AIC372_Semester_Project_Description.pdf`** | **Neuro-Symbolic system: Python + Deep Learning + KB + 20–25 rules + inference engine + implement a 2026 impact-factor journal paper** |

**This brain follows the AFTERNOON document** (it is the later, more specific,
instructor-issued semester-project description) — recorded as DECISIONS
ADR-001. **Status: pending Wadi's confirmation of which brief is
authoritative.** If the morning Prolog brief turns out to be the real one,
this brain's paper/DL phases are void and the plan reverts — ask before
Phase 1 either way.

What survived the re-scope: project identity (AIC372, team of 3), the brain
structure, the restaurant/diet domain as a *candidate direction* (now
re-imagined neuro-symbolically — see PAPER_SELECTION.md). What was discarded:
all SWI-Prolog design, the `facts.pl` file plan, the old 100-marks map, the
`AIC372_Project_GroupNo.zip` checklist.

## Reading order
1. `PRD.md` — what we're building, rubric mapping
2. `PAPER_SELECTION.md` — **the gate**: how the 2026 paper + domain get chosen and approved
3. `ARCHITECTURE.md` — pipeline, modules, engine design
4. `DATA_MODEL.md` — KB design, predicate vocabulary, dataset plan
5. `API_SPEC.md` — query interface + reasoning-trace format
6. `BUILD_PLAN.md` — phases in order, owners, cut list
7. `DECISIONS.md` — why things are the way they are
8. `TEAM.md` — division of work + viva ownership
9. `SUBMISSION.md` — deliverables checklist (brief §5)
10. `TESTING.md`, `RISKS.md`, `PRODUCTION_READINESS.md`
11. `TOOLS.md`, `ENV.md`, `DEPLOYMENT.md` (demo-machine setup), `WORKFLOW.md`
12. `DEMO_PITCH.md`, `DEMO_DATA.md`, `JUDGE_QA.md`, `GLOSSARY.md`,
    `ETHICS_PRIVACY.md`, `SECURITY.md`, `DESIGN.md`, `RETRO.md`

## Working files
- `changes/current-state.md` — what actually exists right now (read before every session)
- `changes/changelog.md` — verified changes only
- `changes/sessions/` — one file per work session
- `prompts/` — task templates

## Golden rules
- **No implementation before instructor approval of paper + domain.**
- KRR core (KB, rules, engine, unification) is hand-written Python; libraries
  only on the DL side.
- Every conclusion the system prints must carry a reasoning trace.
- All 3 members must be able to explain every part (brief §7) — ownership ≠ silo.
