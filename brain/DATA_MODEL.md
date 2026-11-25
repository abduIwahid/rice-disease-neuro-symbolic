# DATA MODEL — knowledge base design, vocabulary, dataset

The KB is the 20-marks component: it must read as *knowledge engineering*,
not as a config file. This file is written for the **leading candidate
direction (A: restaurant/diet)** as the worked example; if the approved paper
points elsewhere, the same design pattern re-maps (predicates change, the
structure — domain facts / DL facts / derived facts, provenance, vocabulary
discipline — does not).

## Fact layers
| Layer | Contents | Source tag |
|---|---|---|
| Domain facts | dishes, ingredients, nutrition, diets, users, taxonomy | `kb` (hand-built, sourced) |
| DL facts | predictions converted by `engine/integrate.py` | `dl_model` (+ confidence) |
| Derived facts | conclusions produced by chaining, with the firing rule | `derived(R-xx)` |

## Taxonomy (inheritance structure)
```
ingredient_class:  food_item ⊃ {meat, dairy, egg, gluten_grain, nut, seafood,
                   vegetable, fruit, legume, spice, oil, sweetener}
diet hierarchy:    vegan ⊂ vegetarian ⊂ (no restriction)
                   diet ⊃ {vegan, vegetarian, halal, gluten_free, diabetic,
                         low_calorie, high_protein, nut_free}
dish categories:   dish ⊃ {breakfast, main, snack, dessert, drink}
                   main ⊃ {grilled, fried, curry, pasta, salad, soup}
```
Inheritance flows through rules, e.g. anything forbidden for `vegetarian`
is inherited by `vegan` plus vegan's own extra restrictions (rule R-04).

## Predicate vocabulary (worked example — direction A)
Every predicate used anywhere must appear here first (name, arity, meaning).

| Predicate | Args | Meaning |
|---|---|---|
| `dish/3` | Name, Cuisine, Category | a dish on the menu |
| `contains/2` | Dish, Ingredient | dish is made with ingredient |
| `ingredient_class/2` | Ingredient, Class | taxonomy membership |
| `calories/2` | Dish, Kcal | energy per serving |
| `protein_g/2` | Dish, Grams | protein per serving |
| `spicy_level/2` | Dish, 0–3 | heat level |
| `diet_avoids/2` | Diet, IngredientClass | diet forbids a whole class |
| `diet_limits_calories/2` | Diet, MaxKcal | diet caps calories/serving |
| `user_diet/2` | User, Diet | user's chosen diet |
| `user_allergy/2` | User, IngredientClass | hard medical constraint |
| `user_goal/2` | User, Goal | weight_loss / muscle_gain / maintenance |
| `user_dislikes/2` | User, Ingredient | soft preference |
| `predicted_dish/3` | ImageId, Dish, Confidence | **DL fact** (provenance: model) |
| `image_shown_by/2` | ImageId, User | who presented this image |
| `suitable_for/2` | Dish, Diet | derived: no avoided class present (NAF) |
| `allergy_safe/2` | Dish, User | derived: no allergen class present (NAF) |
| `within_calorie_goal/2` | Dish, User | derived via diet/goal limits |
| `recommended/2` | Dish, User | derived: suitable + safe + goal-fit |
| `avoid/3` | Dish, User, Reason | derived: exception conclusions |
| `meal_candidate/3` | Dish, User, ScoreBand | derived: ranked recommendation |

## Facts plan (direction A — target ≥ 45 domain facts)
| Group | Count | Examples |
|---|---|---|
| dishes (`dish/3`) | 12 | grilled_chicken, veg_biryani, beef_burger, … |
| contains (per dish 3–5) | ~45 | contains(grilled_chicken, chicken) … |
| ingredient_class | ~20 | ingredient_class(peanut, nut) … |
| nutrition (`calories/2`, `protein_g/2`) | 24 | two per dish |
| diet rules data (`diet_avoids/2`, limits) | ~12 | diet_avoids(vegan, meat) … |
| users (diet, allergy, goal, dislikes) | ~12 | 3 demo users × ~4 facts |
Counts overlap the brief's spirit (the old brief's "40 facts" is gone; the
new brief demands a "comprehensive" KB — this plan is comfortably that).
Knowledge sources to cite in the report: public nutrition tables
(USDA FoodData Central), diet definitions from public health guidance —
record exact URLs in the report's references, never invent values silently:
each nutrition fact gets a `% source:` comment in `kb/facts.py`.

## Rules plan (20–25 required; 22 planned, direction A)
Each rule: ID, what it derives ← from what. Depth = longest chain to a fact.

| ID | Rule (head ← body sketch) | Notes |
|---|---|---|
| R-01 | `forbidden_for_diet(I,Diet)` ← ingredient_class(I,C), diet_avoids(Diet,C) | base |
| R-02 | `suitable_for(Dish,Diet)` ← dish, ¬∃ ingredient: contains ∧ forbidden | **NAF #1** |
| R-03 | `allergy_safe(Dish,U)` ← ¬∃ ingredient of allergen class of U | **NAF #2** |
| R-04 | `diet_avoids(vegan,C)` ← diet_avoids(vegetarian,C) ∨ C ∈ {dairy, egg, …} | inheritance |
| R-05 | `within_calorie_goal(Dish,U)` ← user_diet→limit, calories ≤ limit | comparison |
| R-06 | `protein_rich(Dish)` ← protein_g ≥ 25 | threshold |
| R-07 | `goal_fit(Dish,U)` ← goal=weight_loss ∧ within_calorie_goal | chain |
| R-08 | `goal_fit(Dish,U)` ← goal=muscle_gain ∧ protein_rich | chain |
| R-09 | `recommended(Dish,U)` ← suitable_for ∧ allergy_safe ∧ goal_fit | **depth 3+** |
| R-10 | `avoid(Dish,U,allergy)` ← contains allergen class of U | exception base |
| R-11 | `avoid(Dish,U,diet_violation)` ← ¬suitable_for ∧ user_diet | **NAF #3** |
| R-12 | `final_verdict(Dish,U,avoid)` ← avoid(...) — beats recommended | **conflict rule** |
| R-13 | `final_verdict(Dish,U,recommended)` ← recommended ∧ ¬avoid | NAF + priority |
| R-14 | `dish_matches_image(Img,Dish)` ← predicted_dish(Img,Dish,C), C ≥ 0.60 | DL bridge |
| R-15 | `uncertain_prediction(Img)` ← predicted_dish max C < 0.60 | DL honesty |
| R-16 | `verdict_for_image(Img,U,V)` ← dish_matches_image ∧ final_verdict | **depth 4, integration star** |
| R-17 | `meal_candidate(Dish,U,high)` ← final_verdict=recommended ∧ protein_rich ∨ low-cal per goal | ranking |
| R-18 | `meal_candidate(Dish,U,ok)` ← final_verdict=recommended ∧ ¬high | NAF |
| R-19 | `safe_swap(Dish,Alt,U)` ← avoid(Dish,U) ∧ same category Alt ∧ recommended(Alt,U) | helpful recovery |
| R-20 | `category_member(Dish,RootCat)` ← category chain via taxonomy (recursive) | **recursion/path rule** |
| R-21 | `shares_ingredient(D1,D2,I)` ← contains both — similarity for "more like this" | join |
| R-22 | `daily_pick(U,Dish)` ← image_shown_by ∧ verdict_for_image=recommended, first by confidence | demo closer |

Entailments (answers NOT stored as facts): `recommended/2`, `avoid/3`,
`final_verdict/3`, `verdict_for_image/3`, `safe_swap/3`, `category_member/2`
— all exist only as derivations; the demo points at the empty fact base to
prove it.

Defaults + exceptions (brief §4 "conflicting or exceptional knowledge"):
- **Default 1:** a dish is suitable for a diet *unless* a forbidden-class
  ingredient is present (R-02, NAF) — closed-world: the KB lists all
  ingredients; absence from `contains/2` means absence from the dish.
- **Default 2:** a confident DL prediction is accepted as the dish
  *unless* a hard constraint (allergy) fires `avoid` (R-12 over R-14/R-09).
- **Default 3:** a dish with no recorded calories is treated as *not*
  goal-fit (NAF on missing data) rather than crashing — stated policy.

## Dataset plan (DL side, direction A)
- Food-101 (101 classes) is too broad for the KB; use a **subset of ~12
  classes matching the 12 KB dishes** — the DL label space and the KB
  vocabulary are the same set by design (this alignment IS the integration).
- Splits: dataset's own train/test, carved val 15%; record counts in the
  final report. Licence: Food-101 is publicly distributed for research —
  verify terms on the official page at download time and cite.
- Other directions' datasets: PAPER_SELECTION.md (pneumonia X-ray / UCI
  tabular / PlantVillage) — same alignment principle applies.
