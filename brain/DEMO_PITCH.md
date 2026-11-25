# DEMO PITCH — evaluation-day script + criteria mapping

Evaluation = live demonstration + viva (brief §4 lists what MUST be shown).
No fixed duration is stated in the afternoon brief — plan a tight **~10
minutes** demo + questions; confirm the slot length with the instructor.

## Demo script (in order — each step names its rubric)
1. **The paper (1 min)** — title, journal, DOI, impact factor, the method in
   three sentences, what we changed and why. *(Paper 10)*
2. **The DL model (2 min)** — dataset, fine-tuning, accuracy + one honest
   failure case from the confusion matrix. *(DL 15)*
3. **The knowledge base (2 min)** — vocabulary table, taxonomy diagram, fact
   counts; show that `recommended/2` is NOT in the fact base. *(KR/KB 20)*
4. **Inference live (3 min)** — Q1 backward chain with the proof tree on
   screen; Q5 forward chaining to fixpoint; point at unification bindings
   in the trace. *(Rules + inference 20)*
5. **Integration moment (1–2 min)** — Q4: show a photo → model predicts →
   fact appears with provenance + confidence → verdict derived. *(Integration 15)*
6. **Conflict + failure (1 min)** — Q3 allergy conflict (exception wins,
   CONFLICT node) and Q7 graceful failure. *(Query + explainability 10,
   Testing 10)*
7. **Close (30 s)** — limitations, honestly: dataset size, confidence
   threshold policy, closed-world assumption. *(Testing/demo 10)*

## Criteria mapping (every MUST → where it is demonstrated)
| Brief requirement | Demo step | Marks |
|---|---|---|
| Paper understood + implemented | 1 (+ report) | 10 |
| DL trained/fine-tuned + evaluated | 2 | 15 |
| Comprehensive KB, predicates, relations | 3 | 20 |
| 20–25 rules, FOL/Horn | 3–4 | 20 |
| Forward/backward chaining + unification | 4 | 20 |
| DL predictions as symbolic facts | 5 | 15 |
| ≥5 user queries | 4–6 (Q1–Q7) | 10 |
| Reasoning traces | 4–6 (every answer) | 10 |
| Testing: success / failure / conflict | 6 + TESTING.md | 10 |

## Backup plan (demo-day failures)
- **Primary safety net:** `python -m app.main --demo` — the whole script as
  one deterministic run.
- **If the machine/GPU fails:** pre-recorded screen capture of the full
  demo run (record in Phase 7), plus printed traces in the report appendix.
- **If the DL checkpoint misbehaves:** `predict.py` has a cached-prediction
  mode over the bundled sample images (predictions pre-computed, clearly
  labelled in rehearsal notes — on the day, disclose if used).
- Printed one-page pipeline diagram as a handout — cheap insurance if the
  projector path fails entirely.
