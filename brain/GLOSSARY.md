# GLOSSARY — terms as this project uses them

- **Neuro-symbolic AI** — systems combining neural (DL) perception with
  symbolic knowledge representation and logical reasoning; here: DL predicts,
  logic judges, traces explain.
- **Fact** — a ground compound term asserted as true, with provenance
  (`kb`, `dl_model` + confidence, or `derived(rule)`).
- **Predicate** — a named relation with fixed arity, e.g. `contains/2`;
  the vocabulary table in DATA_MODEL.md is the contract.
- **Rule (Horn clause)** — `head :- body`: head is derivable whenever the
  body goals are provable under one substitution.
- **Unification** — finding a substitution that makes two terms identical;
  with occurs check (a variable never binds to a term containing itself).
- **Substitution / binding** — the Var→term mapping a proof produces; query
  answers are reported as bindings.
- **Standardising apart** — renaming a rule's variables fresh at each use so
  two uses in one proof can't collide.
- **Forward chaining** — data-driven: fire rules on facts until fixpoint;
  answers "what follows?".
- **Backward chaining** — goal-driven SLD-style proof search; answers "is
  this derivable, and how?".
- **Negation as failure (NAF)** — `not_provable(G)`: G is treated as false
  because no proof of G exists in the KB (closed-world assumption).
- **Closed-world assumption** — what the KB doesn't state (and can't derive)
  is false. Justified per rule in DATA_MODEL.md.
- **Reasoning trace** — the recorded proof tree / firing log rendered as
  readable text; the project's explainability deliverable.
- **Provenance** — where a fact came from; DL facts also carry confidence.
- **Impact factor (IF)** — journal metric the brief requires us to verify
  from an official source, never from memory.
