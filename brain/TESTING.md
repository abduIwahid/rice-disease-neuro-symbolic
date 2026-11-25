# TESTING — strategy and case matrix

Three layers: engine unit tests, scenario tests (the brief §4 testing
requirement: **successful inference, unsuccessful queries, conflicting /
exceptional knowledge**), and a manual demo-path checklist. pytest throughout.

## Engine unit tests (E-series)
| ID | Case | Expected |
|---|---|---|
| E-01 | unify atom with itself / different atoms | success / failure |
| E-02 | unify `f(X, b)` with `f(a, Y)` | subst {X=a, Y=b} |
| E-03 | occurs check: unify `X` with `f(X)` | failure (no infinite term) |
| E-04 | standardising apart: same rule used twice in one proof | independent bindings |
| E-05 | backward chain depth 3 (R-09 path) | proof found, tree has 3 rule levels |
| E-06 | forward chaining reaches fixpoint, no duplicate facts | terminates, set-stable |
| E-07 | NAF: goal with no proof under `not_provable` | succeeds; provable goal fails it |
| E-08 | malformed goal / unknown predicate via CLI | friendly error, no traceback |

## Scenario tests (S-series — the graded testing story)
| ID | Scenario | Expected |
|---|---|---|
| S-01 | **Successful inference:** Q1 recommended dishes for a demo user | ≥1 answer, trace shows R-09 chain |
| S-02 | **Unsuccessful query:** Q7 (vegan dessert under a tight calorie cap, none qualifies) | "No proof found" + failed-branch explanation |
| S-03 | **Conflicting knowledge:** DL/user path recommends a dish the user is allergic to | `avoid` wins via R-12; trace prints the CONFLICT node |
| S-04 | **Exceptional knowledge:** dish with missing nutrition data | treated as not goal-fit (stated NAF policy), no crash |
| S-05 | **Low-confidence DL prediction** (conf < 0.60) | fact flagged `uncertain`; no recommendation derived from it alone |
| S-06 | **Entailment check:** `recommended/2` facts are absent from the fact base before inference | asserted in test — proves answers are derived, not stored |
| S-07 | Vocabulary/code consistency: every predicate in code ∈ DATA_MODEL table; rule count ∈ [20, 25] | test reads the registry |

(IDs S-* here are the test-plan IDs; the session-06/07 naming in other
projects used T-## — in THIS project, engine tests are E-##, scenarios S-##.)

## Manual critical-path checklist (before every demo/rehearsal)
- [ ] Fresh clone → venv → `pip install -r requirements.txt` → `--demo` runs clean
- [ ] Q1–Q7 all produce answers/traces on the demo machine
- [ ] Image demo (Q4) works with the bundled sample images, offline
- [ ] Model checkpoint loads; KB stats print the expected fact/rule counts

## Definition of done (testing)
All E + S tests green in CI-less local run, output pasted into the session
file; the three graded scenario classes (success / failure / conflict) each
have a named test — the examiner will ask for exactly these.
