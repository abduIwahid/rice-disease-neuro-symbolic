# PRD — Neuro-Symbolic Knowledge-Based Intelligent System (AIC372)

**Core feature (one sentence):** A fine-tuned Deep Learning model classifies an
input; its prediction is converted into symbolic facts; a knowledge base of
domain facts + 20–25 logical rules, driven by a hand-built inference engine
(forward + backward chaining with unification), derives explained conclusions
the DL model alone could never state.

## Problem
Pure DL classifiers output a label and a probability — no reasons, no domain
knowledge, no way to combine a prediction with rules like "this is unsafe for
a nut-allergic user" or "this finding, plus that history, implies this risk
category". Pure rule systems can't perceive. The project (and the 2026 paper
it implements) shows the neuro-symbolic combination: perception from DL,
judgement from logic, and a proof trace joining them.

## Target users
- Primary evaluator: Dr. M. Sharif (demo + viva) — the system must *show*
  KR, rules, inference and traces working live.
- Secondary: the end user of the chosen domain direction (see
  PAPER_SELECTION.md — final domain is chosen together with the paper).

## Goals
1. Implement the core methodology of one 2026 impact-factor journal paper
   (IEEE/Elsevier/Springer), documented with full reference + DOI + verified IF.
2. DL model trained/fine-tuned by the team on a public dataset, evaluated honestly.
3. A knowledge base where knowledge representation is a real contribution:
   typed predicates, a documented vocabulary, domain facts + DL-derived facts
   with provenance.
4. A self-built inference engine: unification, forward chaining, backward
   chaining, conflict/exception handling — with reasoning traces.
5. ≥5 user queries answered by inference (not lookup), incl. one that fails
   gracefully and one that resolves conflicting knowledge.

## Non-goals
- No web app / hosted deployment (CLI demo is the deliverable shape).
- No general-purpose Prolog clone — engine scope is what the demo needs.
- No chasing state-of-the-art DL accuracy; a solid, well-evaluated model wins.
- No implementation before instructor approval (process non-goal: skipping the gate).

## Scope
**MUST** (brief §2/§4 — every item is demonstrated live)
- Trained/fine-tuned DL model for the domain.
- KB: facts, predicates, relationships, logical expressions.
- 20–25 meaningful logical rules (propositional / FOL / Horn as appropriate).
- Inference engine: forward AND backward chaining, unification with variable substitution.
- DL predictions converted to symbolic facts and used in inference.
- ≥5 different user queries deriving new conclusions.
- Reasoning traces for conclusions.
- Testing: successful inference, unsuccessful query, conflicting/exceptional knowledge.
- Paper PDF + reference + DOI + IF evidence; proposal; final report; slides; live demo.

**SHOULD**
- Confidence-aware facts (prediction carries its probability into the KB;
  low-confidence predictions flagged or withheld by a stated threshold policy).
- Both chaining modes used in the demo (forward for "what follows from this
  case?", backward for "is this true, and why?").
- Exception/default rules (e.g. a general rule + a specific override) to make
  the conflict test case real, not staged.

**COULD** (only after MUST+SHOULD are solid; see BUILD_PLAN cut list)
- Certainty-factor style weighting on derived conclusions.
- A tiny forward-chaining "what-if" batch mode over several inputs.
- Simple GUI wrapper — *discouraged*: CLI traces demo better and cost less.*

## Success / acceptance criteria (mirrors brief §4 demo list)
- [ ] Paper approved by instructor before implementation; PDF + DOI + IF in `paper/`.
- [ ] DL model trains end-to-end from `models/train` and beats a stated baseline.
- [ ] KB loads with zero errors; vocabulary table matches the code exactly.
- [ ] 20–25 rules present, each traceable to a line in DATA_MODEL.md's rule plan.
- [ ] All 5+ demo queries run live; traces print facts + rules used.
- [ ] Test suite green, including the failure and conflict cases.
- [ ] Every member can walk the full pipeline unaided (internal viva rehearsal).

## Marks map (brief §6) — detail in DEMO_PITCH.md
| Component | Marks | Earned by |
|---|---|---|
| Research paper selection & understanding | 10 | PAPER_SELECTION process + paper notes + viva answers |
| Deep Learning implementation | 15 | `models/` — fine-tuned model, honest evaluation |
| Knowledge representation & KB | 20 | `kb/` — vocabulary, facts, provenance design (DATA_MODEL.md) |
| Logical rules & inference engine | 20 | 20–25 rules + `engine/` (unification, both chainings) |
| Neuro-symbolic integration | 15 | DL→fact converter + end-to-end pipeline (ARCHITECTURE.md) |
| Query processing & explainability | 10 | `app/` queries + reasoning traces (API_SPEC.md) |
| Testing & demonstration | 10 | TESTING.md cases + rehearsed demo (DEMO_PITCH.md) |
| **Total** | **100** | |

## Roadmap
Phase 0 paper shortlist → **approval gate** → proposal → DL baseline →
KB + rules → engine → integration → queries + traces → testing/report/demo.
Full plan: BUILD_PLAN.md.
