# DEMO DATA — the fixed demo world (direction A shape)

Everything the live demo touches is frozen here so rehearsals and the real
run use identical data. (Values finalised in Phase 3 against the approved
paper; the structure below is the plan.)

## Demo users
| User | Diet | Allergy | Goal | Story in the demo |
|---|---|---|---|---|
| ali | vegetarian | — | weight_loss | Q1/Q2: gets real recommendations |
| sara | (none) | **nut** | maintenance | Q3/Q6: the conflict + safe-swap star |
| bilal | halal | — | muscle_gain | Q4: presents the photo |

## Demo dishes (KB subset the script relies on)
grilled_chicken · veg_biryani · beef_burger · peanut_noodles (Sara's trap:
model/user path likes it, peanut → nut class → avoid) · garden_salad ·
fruit_bowl · paneer_tikka · mushroom_soup · chocolate_cake · grilled_fish ·
lentil_dal · chicken_karahi — 12 dishes, each with ingredients, nutrition,
category per DATA_MODEL.md.

## Sample images (for Q4)
- 3 bundled test images matching KB dishes (from the dataset's test split —
  never training images), stored in `app/demo_images/`.
- One deliberately ambiguous image for the low-confidence path (S-05).

## Frozen expectations
- Q1 for ali returns ≥2 dishes; Q3 for sara/peanut_noodles returns `avoid`
  with a CONFLICT node; Q7 returns "No proof found". If Phase 3 data changes
  break any of these, DEMO_DATA and TESTING.md are updated in the same commit.
