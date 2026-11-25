# BUILD PLAN — phases in order (deadline: TBD — needs human decision)

No calendar dates are invented: the brief's PDF states no due date. Phases
are sequenced by dependency; % is share of total effort. **Phase 0 ends at a
hard gate — nothing below it starts early.**

## Phase 0 — Paper shortlist + INSTRUCTOR APPROVAL (≈10%) 🚪 GATE
- [ ] Each member brings 2 candidate papers passing the PAPER_SELECTION filter
- [ ] Pool scored; top-3 one-pagers written (reference, DOI, IF evidence)
- [ ] Shortlist presented to **Dr. M. Sharif**; paper + domain approved
- [ ] ADR records the choice; paper PDF + IF screenshot filed in `paper/`
- Owners: all three (Wadi leads the meeting prep)

## Phase 1 — Proposal (≈8%)
- [ ] Project proposal per brief §5: problem, objectives, methodology
      (paper's method + our modifications), dataset, module diagram
- [ ] Finalise DATA_MODEL.md vocabulary + rule plan against the chosen paper
- Owners: Wadi (method), Faseeh (KB sections), Daniyal (engine sections)

## Phase 2 — DL baseline (≈18%)
- [ ] Dataset downloaded, licence recorded, splits fixed, label set == KB vocabulary
- [ ] Fine-tune pretrained model; baseline metrics (accuracy, confusion matrix)
- [ ] `models/predict.py` meets the ARCHITECTURE contract
- Owner: Abdul Wahid

## Phase 3 — Knowledge base + rules (≈20%)
- [ ] `kb/facts.py` — full domain fact base, sourced comments
- [ ] `kb/rules.py` — all 20–25 rules with IDs matching DATA_MODEL.md
- [ ] Vocabulary registry == DATA_MODEL table (checked by a test)
- Owner: Faseeh

## Phase 4 — Inference engine (≈20%)
- [ ] `engine/terms.py` + `unify.py` (occurs check, standardising apart)
- [ ] `engine/backward.py` with proof-tree capture; `engine/forward.py` with firing log
- [ ] NAF + conflict/exception resolution per ARCHITECTURE
- [ ] Engine unit tests green (TESTING.md E-series)
- Owner: Daniyal Badshah

## Phase 5 — Neuro-symbolic integration (≈10%)
- [ ] `engine/integrate.py`: predictions → facts (threshold policy, provenance)
- [ ] End-to-end: image in → verdict + trace out (Q4 path)
- [ ] **DEPENDENCY FREEZE** at the end of this phase — no new libraries after
- Owners: Wadi (converter) + Daniyal (engine hookup)

## Phase 6 — Queries, traces, CLI (≈7%)
- [ ] Q1–Q7 implemented; `--demo` scripted run works start to finish
- [ ] Trace rendering matches API_SPEC.md format exactly
- Owner: Daniyal; Faseeh checks KB answers by hand

## Phase 7 — Testing, report, slides, demo prep (≈7% + rehearsal)
- [ ] Full TESTING.md matrix green (success / failure / conflict cases)
- [ ] Final report: methodology, implementation, experiments, results, limitations
- [ ] Slides + 10–12 min demo rehearsed twice; backup recording made
- [ ] SUBMISSION.md checklist verified line by line
- Owners: all; Daniyal assembles report/slides

## Cut list (drop in this order if time squeezes)
1. COULD items (certainty weighting, what-if batch mode, any GUI idea)
2. Q6/Q7 extra queries (keep the mandatory 5)
3. DL model size (EfficientNet-B0 → ResNet18 → MobileNet) — never cut evaluation honesty
4. Extra demo users/dishes beyond the plan minimums
**Never cut:** a chaining mode, the conflict case, traces, or the paper documentation.

## Phase-end reporting rule
At each phase end: session file written, BUILD_PLAN boxes ticked,
current-state updated, and a one-line status (on track / behind / cut applied).
