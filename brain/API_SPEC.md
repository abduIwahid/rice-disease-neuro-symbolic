# API SPEC — query interface & reasoning-trace format

No HTTP API — the "interface" is the CLI query contract: what a user can
ask, what an answer contains, and exactly what a reasoning trace looks like.
(Written for direction A; the contract shape is direction-independent.)

## Query contract
A query is a goal with variables, e.g. `recommended(Dish, ali)`. The engine
answers with: **(1)** yes/no or the list of variable bindings, **(2)** the
facts used, **(3)** the rules fired, **(4)** the trace. An underivable query
is a first-class answer — `No proof found` plus the branch that failed —
never an exception.

## The demo queries (brief: ≥5 different user queries)
| # | Query (plain words) | Engine mode | Shows off |
|---|---|---|---|
| Q1 | "What dishes are recommended for Ali?" | backward | chaining depth, joins |
| Q2 | "Why is grilled_chicken recommended for Ali?" | backward + trace | explainability (10 marks) |
| Q3 | "Is this dish safe for Sara (nut allergy)?" — answer: **no, with the avoid-trace** | backward | NAF + exception/conflict |
| Q4 | "Here is a photo — what is it, and should Bilal eat it?" | DL → facts → backward | **integration (15 marks)** |
| Q5 | "What follows from today's facts?" (all derived conclusions) | forward | forward chaining + fixpoint log |
| Q6 | "Suggest a safe alternative to the dish Sara can't eat" | backward | safe_swap recovery rule |
| Q7 | "Is there a vegan dessert under 300 kcal?" — designed to **fail** if none qualifies | backward | graceful unsuccessful query |

## Reasoning-trace format (the explainability deliverable)
Indented proof tree, printed for every answer. Example (Q3 shape):
```
GOAL avoid(peanut_noodles, sara, allergy)
└─ RULE R-10 avoid(Dish, User, allergy)
   ├─ contains(peanut_noodles, peanut)            [fact, kb]
   ├─ ingredient_class(peanut, nut)               [fact, kb]
   └─ user_allergy(sara, nut)                     [fact, kb]
CONFLICT: recommended(peanut_noodles, sara) was also derivable via R-09,
but R-12 (exception priority) decides: final_verdict = avoid.
```
Rules: every node names its rule ID or `[fact, source]`; DL facts show
`[dl_model, conf=0.87]`; NAF steps print as `NOT PROVABLE: <goal> (closed
world)` so the examiner sees the mechanism, not a magic "no".

## CLI surface (app/main.py)
Menu: 1) ask a goal 2) run demo queries Q1–Q7 3) classify an image and
reason about it 4) forward-chain everything and list derived facts
5) show KB stats (facts, rules, predicates) 0) exit.
Input validation: unknown predicate, wrong arity, malformed goal, missing
image file → friendly error + re-prompt (never a traceback). All demo queries
must also run non-interactively: `python -m app.main --demo` prints the full
scripted run (demo-day safety net, see DEMO_PITCH.md).
