# JUDGE QA — viva prep (any member may be asked anything — brief §7)

Short answer *shapes* — each member expands these in their own words during
rehearsal. Grouped by the examiner's likely line of attack.

## The paper (10)
- **"Summarise the paper's method."** → input → DL model → symbolic
  representation → reasoning → output; name the one idea that makes it
  neuro-symbolic rather than a pipeline of two separate tools.
- **"What did you change from the paper, and why?"** → dataset subset /
  smaller backbone / threshold policy — each change tied to semester scale,
  documented in the report's limitations.
- **"Impact factor — how did you verify it?"** → journal page / JCR,
  evidence filed in `paper/`; never quote from memory.

## Deep Learning (15)
- **"Why fine-tune instead of training from scratch?"** → data size +
  transfer learning; frozen vs trained layers named.
- **"Your model is wrong sometimes — then what?"** → confidence threshold,
  `uncertain` facts, and the symbolic layer can override via exception rules.
- **"How did you evaluate?"** → split discipline, accuracy, confusion
  matrix, the failure class we saw most.

## Knowledge representation & KB (20)
- **"What is a predicate here? Show me your vocabulary."** → DATA_MODEL
  table; arity discipline; why facts are ground and rules carry variables.
- **"Where is inheritance?"** → diet hierarchy rule (vegan inherits
  vegetarian's restrictions + its own).
- **"Closed-world assumption — where do you rely on it?"** → NAF rules
  (suitability, allergy-safety): absence of a `contains` fact = absence
  from the dish; justified because the KB enumerates each dish's ingredients.

## Rules & inference engine (20)
- **"Forward vs backward chaining — when is each right?"** → forward =
  data-driven, "what follows from these facts"; backward = goal-driven,
  "prove this / find who satisfies it"; demo uses both, deliberately.
- **"Show me unification."** → walk one trace node: goal vs rule head,
  substitution built, occurs check mentioned unprompted.
- **"Why not just use Prolog / a library?"** → the brief requires
  demonstrating our own KRR implementation; the engine is small enough to
  own completely (and say its size honestly).
- **"How do you stop infinite loops?"** → depth cap, visited-goal guard,
  forward chaining stops at fixpoint because facts are finite.

## Integration (15)
- **"Where exactly does DL end and logic begin?"** → `predict.py` contract:
  (label, confidence) out; `integrate.py` converts to a ground fact with
  provenance. One function wide, on purpose.
- **"Isn't this just IF–THEN on a classifier?"** (the brief's own warning) →
  no: conclusions come from chained rules over a KB (multi-level proofs,
  joins, recursion, NAF) — point at a depth-4 trace (R-16 path).

## Explainability, testing, honesty (10 + 10)
- **"Show me a wrong/failed case."** → Q7 failure + S-05 low-confidence +
  the conflict case; each is a named test, not an anecdote.
- **"What are the system's limits?"** → closed-world KB completeness,
  dataset bias/size, threshold is a policy choice, no real-world medical /
  dietary authority (direction-dependent — see ETHICS_PRIVACY.md).
- **"Who wrote which part?"** → TEAM.md split + session logs; then any
  member continues answering any follow-up (that's the point of rehearsal).
