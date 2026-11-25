# RISKS — top risks + fallback for each

| # | Risk | Impact | Fallback / mitigation |
|---|---|---|---|
| R-1 | **Wrong brief followed** — two official PDFs conflict (ADR-001) | whole project wrong | brain follows the afternoon doc; Wadi confirms with instructor at the Phase 0 approval meeting — ask explicitly |
| R-2 | No implementable 2026 IF-journal paper found for the favourite domain | Phase 0 stalls | 4 candidate directions × 6-paper pool; choose paper-first if a strong paper appears in another direction |
| R-3 | Instructor rejects the proposed paper/domain | re-plan | always carry a runner-up one-pager to the approval meeting |
| R-4 | Paper's dataset is private/gated | DL phase blocked | filter step 2 in PAPER_SELECTION kills these at shortlist stage; public substitute dataset is an accepted, documented modification |
| R-5 | DL training too slow / Colab limits | Phase 2 slips | smaller backbone (cut list), subset classes, checkpoint discipline (TOOLS.md) |
| R-6 | Engine scope creep (building a Prolog clone) | Phase 4 eats the schedule | engine scope frozen in ARCHITECTURE.md: terms, unify, two chainings, NAF, tracer — nothing else without an ADR |
| R-7 | "Just IF–THEN" criticism at the viva (brief's own warning) | integration/rules marks lost | depth-4 traces, recursion rule, NAF + conflict design — and JUDGE_QA rehearses the rebuttal |
| R-8 | A member can't explain another's module at the viva | demo marks lost (brief §7) | cross-training rehearsal in Phase 7; session logs keep contributions honest |
| R-9 | Demo-day machine failure | testing/demo marks | `--demo` deterministic mode, backup recording, printed pipeline handout (DEMO_PITCH.md) |
| R-10 | Nutrition/clinical KB facts are wrong or unsourced | credibility + ethics | every fact group carries a source comment; public sources only; educational-use disclaimer |
| R-11 | Deadline announced late and close | compression | cut list order is pre-agreed (BUILD_PLAN); MUST items are already minimal |
