# PRODUCTION READINESS — read: SUBMISSION readiness

Adapted from the standard checklist; tags are for THIS project's budget
(a graded coursework demo, not a product launch).

## MUST
- [ ] Paper + domain approved by instructor before implementation (brief §7)
- [ ] Paper PDF + full reference + DOI + IF evidence filed in `paper/`
- [ ] DL model trains from a clean checkout; metrics recorded honestly
- [ ] KB loads with zero errors; vocabulary table == code (test S-07)
- [ ] 20–25 rules, each with ID + comment; rule count verified by test
- [ ] Both chaining modes + unification demonstrably working (E-series)
- [ ] DL→fact integration end-to-end (Q4) with provenance + threshold policy
- [ ] ≥5 queries live, traces printed (Q1–Q7 implemented)
- [ ] Testing trio present: success / unsuccessful / conflict (S-01/02/03)
- [ ] `--demo` deterministic run + backup recording exist
- [ ] Final report complete (methodology, implementation, experiments,
      results, limitations, paper modifications)
- [ ] All 3 members rehearsed on ALL components

## SHOULD
- [ ] Confidence-aware facts visibly affecting at least one derivation
- [ ] Confusion matrix + one analysed DL failure in the report
- [ ] Printed pipeline handout for the examiner

## SKIP-FOR-NOW
- Any GUI, web deployment, user accounts, or persistence beyond files —
  zero rubric value for this brief (DECISIONS ADR-005)
