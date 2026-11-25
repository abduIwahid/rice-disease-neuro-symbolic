# AGENT.md — AIC372 Semester Project: Neuro-Symbolic Knowledge-Based Intelligent System

**Summary (5 lines):** A Python system that integrates a trained/fine-tuned Deep
Learning model with a knowledge base, 20–25 logical rules and a self-built
inference engine (forward + backward chaining with unification), implementing
the core approach of a 2026 research paper from an impact-factor
IEEE/Elsevier/Springer journal. DL predictions become symbolic facts; the
engine reasons over them and prints reasoning traces. Team of 3, AIC372
(Knowledge Representation and Reasoning), COMSATS Attock, Fall 2026.
**Core feature:** DL prediction → symbolic fact → logical inference → explained answer.
**Wow factor:** the system doesn't just classify — it *proves* its conclusions with a readable reasoning trace, and survives conflicting knowledge (e.g. model says "eat it", allergy fact says "don't") by explicit exception rules.
**Current phase:** Phase 0 — paper shortlist. **NO implementation before the paper + domain are approved by Dr. M. Sharif** (brief §7, hard gate).

> ⚠️ **TWO BRIEFS EXIST** — see `brain/00-START-HERE.md` and DECISIONS ADR-001.
> This brain follows the AFTERNOON document of 2026-11-24
> (`AIC372_Semester_Project_Description.pdf`, neuro-symbolic / Python).
> The morning Prolog brief is superseded in this brain unless Wadi says otherwise.

## Read first (in order)
1. `brain/00-START-HERE.md` 2. `brain/PRD.md` 3. `brain/PAPER_SELECTION.md`
4. `brain/ARCHITECTURE.md` 5. `brain/DATA_MODEL.md` 6. `brain/BUILD_PLAN.md`
Then the task-relevant file. Before every work session also read
`brain/changes/current-state.md` + the last 3 files in `brain/changes/sessions/`.

## Hard rules
- **Approval gate:** no DL training, no KB coding beyond paper-study notes until
  the selected paper + domain are approved by the instructor (brief §7).
- **KRR components are hand-built** (KB, rules, inference engine, unification).
  Libraries are fine for the DL side only (brief §7). No `experta`-style engine
  as the core — see DECISIONS ADR-003.
- Every rule must be *meaningful* and documented (vocabulary table in
  DATA_MODEL.md). "DL output wired to bare IF–THEN prints" explicitly fails
  the brief — inference must be real (chaining + unification + traces).
- Log every work session per `brain/WORKFLOW.md` (session file + changelog +
  current-state). Never invent history; tag claims Verified / Inferred / Unknown.
- Academic integrity (brief §7): AI tools are a permitted support resource;
  every line submitted must be understood and explainable by all 3 members.
- No secrets in the repo; datasets only from public sources with licences
  recorded in DATA_MODEL.md.
- Tasks under ~30 minutes; commit after each (Conventional Commits).

## Commands (once code exists — Phase 2+)
- Setup: `python -m venv .venv && pip install -r requirements.txt`
- Run demo: `python -m app.main`
- Tests: `pytest`
- Train DL model: `python -m models.train` (config in `models/config.py`)

## Definition of done (any task)
Code/notes merged + tests or manual check recorded in the session file +
changelog + current-state updated + the responsible member can explain it
out loud (viva test).
