# Neuro-Symbolic Knowledge-Based Intelligent System — AIC372 Semester Project

> A Deep Learning model whose predictions become **symbolic facts**, reasoned
> over by a hand-built knowledge base (20–25 logical rules) and inference
> engine (forward + backward chaining with unification) — with a readable
> **reasoning trace** for every conclusion. Implementation of a 2026 research
> paper (impact-factor IEEE/Elsevier/Springer journal), in Python.

**Course:** Knowledge Representation and Reasoning (AIC372), COMSATS University
Islamabad, Attock Campus — Fall 2026. Instructor: Dr. M. Sharif.
**Team:** Abdul Wahid · Faseeh · Daniyal Badshah (see `brain/TEAM.md`).

## Status
🧠 Brain complete — **no code yet.** Current phase: **Phase 0, paper
shortlist.** The research paper + application domain must be approved by the
instructor before any implementation (brief §7).

## The pipeline
```
 input (image / record)
        │
        ▼
 ┌─────────────┐   prediction + confidence   ┌──────────────────┐
 │ DL model    │ ───────────────────────────▶│ Fact converter   │
 │ (PyTorch,   │                             │ (threshold,      │
 │ fine-tuned) │                             │  provenance)     │
 └─────────────┘                             └────────┬─────────┘
                                                      ▼ symbolic facts
 ┌──────────────────────────────────────────────────────────────┐
 │ Knowledge base — domain facts + 20–25 FOL/Horn rules         │
 │ Inference engine — unification · forward chaining (data-     │
 │ driven) · backward chaining (goal-driven) · conflict rules    │
 └────────────┬─────────────────────────────────────────────────┘
              ▼
   Query interface (CLI)  +  Reasoning trace for every answer
```

## Repository layout (planned)
```
models/     DL model: dataset loading, training, evaluation, inference wrapper
kb/         facts, rules, vocabulary (knowledge engineering)
engine/     terms, unification, forward chaining, backward chaining, tracer
app/        CLI: menu, query processing, demo script runner
tests/      pytest: engine unit tests + scenario tests (success/fail/conflict)
paper/      selected paper PDF, reference, DOI, impact-factor evidence, notes
report/     proposal, final report, slides
brain/      this project's brain (start at brain/00-START-HERE.md)
```

## Marks target (brief §6)
Paper 10 · DL 15 · KR + KB 20 · Rules + inference 20 · Integration 15 ·
Queries + explainability 10 · Testing + demo 10 = **100**.
Full mapping: `brain/DEMO_PITCH.md` and `brain/PRD.md`.

## Documents
- Assignment brief (authoritative, 24 Nov 2026 afternoon):
  `~/workspace/user/files/AIC372_Semester_Project_Description.pdf`
- Brain: `brain/00-START-HERE.md`
