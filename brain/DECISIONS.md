# DECISIONS — ADR log (newest last)

## ADR-001 — 2026-11-24 — Follow the AFTERNOON brief (neuro-symbolic, Python)
- **Context:** two different official PDFs arrived the same day. Morning:
  `Project_Description.pdf` (SWI-Prolog expert system). Afternoon:
  `AIC372_Semester_Project_Description.pdf` (Neuro-Symbolic system, Python +
  DL + 2026 paper implementation, different rubric).
- **Decision:** the brain and plan follow the **afternoon** document.
- **Why:** it is later, more specific, and matches the "Semester Project"
  framing with a full evaluation scheme; the Prolog design was discarded
  wholesale (nothing Prolog-specific is in this brain's plan).
- **Status:** **pending Wadi's confirmation** that the afternoon brief is
  authoritative. If reversed, this brain's Phases 0–2 and marks map are void.

## ADR-002 — 2026-11-24 — Domain is NOT locked; domain + paper are chosen together
- **Context:** Wadi confirmed "Restaurant Menu and Diet Recommendation" on
  2026-11-24 — under the *morning* brief. The afternoon brief makes the paper
  the primary object and requires instructor approval of paper + domain.
- **Decision:** restaurant/diet stays as **leading candidate (Direction A)**,
  re-imagined neuro-symbolically (dish-image DL → diet reasoning); three
  further directions are kept open in PAPER_SELECTION.md. The folder name
  `restaurant-diet-expert` is a working name, not a lock.
- **Why:** locking the domain before finding an approvable 2026 paper risks
  an un-implementable pairing; the approval gate decides.

## ADR-003 — 2026-11-24 — Inference engine is hand-built Python (no experta core)
- **Options:** (a) self-built engine (terms/unify/forward/backward in plain
  Python) · (b) `experta` (CLIPS-style rule engine) · (c) pyDatalog /
  kanren logic libraries.
- **Decision:** (a).
- **Why:** brief §7 allows libraries for DL but requires the team to
  *demonstrate understanding and implementation of the KRR components*;
  unification + both chaining modes are 20 marks of rubric. experta gives
  forward chaining only, with pattern matching instead of FOL unification,
  and would hide exactly what is being graded. A self-built engine is a few
  hundred lines and every line is viva-explainable. Fallback: if Phase 4
  stalls, revisit (b) for forward chaining only and keep the hand-built
  backward chainer + unifier.

## ADR-004 — 2026-11-24 — DL = fine-tuned pretrained CNN (PyTorch/torchvision)
- **Why:** the team's existing stack (PAI course), trains on free Colab,
  honest baselines are easy; brief rewards a sound DL implementation (15),
  not novelty. Exact architecture follows the approved paper (Phase 0/2).

## ADR-005 — 2026-11-24 — CLI demo, no web UI
- **Why:** traces are the star of the demo and print best in a terminal;
  `--demo` scripted mode gives a deterministic fallback. A GUI would spend
  Phase 6–7 budget for zero rubric marks.

## Open decisions (need humans)
- Which brief is authoritative (ADR-001) — **Wadi**.
- Final paper + domain — **Dr. M. Sharif's approval** (Phase 0 gate).
- Team division sign-off (TEAM.md is a proposal) — **Wadi**.
- Training compute: local GPU vs Colab — decide in Phase 2 from model size.
- Bonus scope (certainty weighting / what-if batch): default NO unless
  Phase 6 ends early (see BUILD_PLAN cut list).
