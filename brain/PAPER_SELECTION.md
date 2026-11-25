# PAPER SELECTION — the gate everything waits on

Brief §3 + §7: the group must **select and implement a research paper
published in 2026** in an **impact-factor journal** from **IEEE, Elsevier or
Springer**, with full reference + DOI + verified impact factor — and the
**paper AND domain must be approved by Dr. M. Sharif before implementation**.
Nothing in BUILD_PLAN Phase 2+ starts before this gate clears.

## What "implementable in one semester" means — the filter
A candidate paper passes only if ALL of these hold:
1. **Small DL core** — the model is a standard architecture (CNN / ResNet /
   EfficientNet / small transformer / MLP) that fine-tunes on a laptop or
   free Colab GPU in hours, not days. No large-language-model training, no
   exotic hardware, no private data.
2. **Public dataset** — the paper's dataset (or a faithful public substitute)
   is downloadable: Kaggle, Hugging Face Datasets, UCI, or the authors' page.
   Licence recorded. If the dataset is gated/private → reject the paper.
3. **A real symbolic half** — the paper's method includes (or cleanly admits)
   a knowledge base + rules + inference. A pure-DL paper forces us to invent
   the whole symbolic side (allowed, but riskier to defend as "implementing
   the paper"); a paper that is already neuro-symbolic is the ideal.
4. **Method fits a pipeline diagram** — inputs → DL → symbolic facts → rules →
   conclusions can be drawn in 5 boxes. If the method needs 3 models and a
   distributed system → reject.
5. **Verifiable venue** — journal (not conference, not preprint-only),
   publisher ∈ {IEEE, Elsevier, Springer}, 2026 publication date, DOI
   resolves, impact factor checkable on the journal's official page /
   Clarivate JCR. **Never quote an IF number from memory — screenshot the
   source into `paper/` as evidence.**

## Where to search
| Source | Use for |
|---|---|
| IEEE Xplore (ieeexplore.ieee.org) | IEEE journal papers, 2026, "neuro-symbolic" + domain |
| ScienceDirect (sciencedirect.com) | Elsevier journals (e.g. Expert Systems with Applications, Knowledge-Based Systems, Neurocomputing) |
| SpringerLink (link.springer.com) | Springer journals (e.g. Neural Computing and Applications, Applied Intelligence) |
| Google Scholar (year filter 2026) | Discovery only — verify venue/DOI/IF at the publisher |
Search strings: `"neuro-symbolic" 2026 <domain>`, `"knowledge-based" deep learning 2026 <domain> journal`, `"explainable" rule-based deep learning 2026 <domain>`.

## Candidate domain directions (domain + paper are chosen TOGETHER)
Status of all four: **candidates only — none is locked.** The restaurant
direction is the team's earlier pick re-imagined; the final choice is
whichever direction yields an approvable 2026 paper.

### A. Restaurant / Diet — "see the dish, reason the diet" *(leading candidate)*
- **DL:** dish image classification — fine-tune ResNet18/EfficientNet-B0 on a
  Food-101 subset (or a Kaggle food-images set); output: dish + top-k candidates.
- **Symbolic:** predicted dish → facts (`predicted_dish/3` with confidence);
  KB holds ingredients, nutrition, diet rules (vegan/vegetarian/halal/
  diabetic/allergy); engine derives `suitable_for/2`, `recommended/2`,
  `avoid/3` with traces. Conflict case is natural: model says "eat", allergy
  fact says "don't" — exception rule decides, trace shows it.
- **Dataset:** Food-101 (public, ETH Zurich page / Kaggle mirror) — verify
  licence at download. Nutrition data: hand-built KB facts from public
  nutrition tables (cite in report).
- **Paper type needed:** 2026 neuro-symbolic / knowledge-based food or
  diet-recommendation paper in an IF journal.
- **Why strong:** every rubric item has a natural home; demo is visual and
  easy to follow; KB is genuinely rich (40+ facts trivially).

### B. Healthcare — clinical decision support *(plays to Wadi's ML strength)*
- **DL options:** (i) chest X-ray pneumonia classification (he already built
  a pneumonia CNN in PAI Lab 9 — dataset and pitfalls known), or (ii) tabular
  risk model (diabetes/heart disease, MLP on UCI/Kaggle data).
- **Symbolic:** predicted condition + patient facts → clinical-guideline
  rules → risk category, recommended next step, red-flag overrides
  (exception rules: a single danger sign escalates regardless of model output).
- **Dataset:** Kaggle chest X-ray pneumonia set (public) or UCI Heart
  Disease / Pima diabetes (public). Record licence + the "not for real
  diagnosis" disclaimer (ETHICS_PRIVACY.md).
- **Paper type needed:** 2026 neuro-symbolic / explainable clinical
  decision-support paper in an IF journal.
- **Why strong:** Wadi's WhyRisk + Ezitech healthcare-ML background makes the
  viva safest here; red-flag exception rules are the best conflict demo of
  all four directions. **Risk:** medical claims must stay educational;
  dataset licensing needs care.

### C. Agriculture — plant leaf disease → treatment reasoning
- **DL:** leaf image classification on PlantVillage (Kaggle, public).
- **Symbolic:** predicted disease → facts; KB of treatments, dosage rules,
  weather/season conditions, contraindications → engine derives a treatment
  plan + warnings.
- **Paper type needed:** 2026 neuro-symbolic / knowledge-based plant-disease
  paper in an IF journal.
- **Why strong:** dataset is famously easy to get and train on; demo is
  visual; rules are concrete. **Risk:** none of the team has agriculture
  depth — viva answers stay shallow; KB facts need careful sourcing.

### D. Education — student performance → advising rules
- **DL:** tabular model (MLP/small gradient boosting via PyTorch or sklearn)
  predicting pass/at-risk from UCI Student Performance data.
- **Symbolic:** predicted risk + enrolment facts → advising rules: course
  eligibility, prerequisite chains (natural recursion/path rules),
  intervention recommendations.
- **Paper type needed:** 2026 neuro-symbolic / learning-analytics paper in an
  IF journal.
- **Why strong:** the team *lives* this domain (own university rules as KB
  sources); prerequisite chains show off recursion. **Risk:** tabular DL is
  less impressive on demo day than an image model.

## Shortlist procedure (Phase 0, in order)
1. Each member brings **2 candidate papers** (any direction) that pass the
   5-point filter → pool of ~6.
2. Score the pool on: implementability, dataset availability, symbolic-half
   strength, viva defensibility. Keep the **top 3** (template below).
3. One-page summary per finalist: reference + DOI + IF evidence, method in 5
   lines, what we would build, what we would cut/modify.
4. **Take the shortlist to Dr. Sharif** — present the top pick + runner-up,
   get paper + domain approved **in that meeting** if possible.
5. Record the outcome as an ADR in DECISIONS.md; file the paper PDF +
   reference + DOI + IF screenshot in `paper/`. Only then Phase 1 starts.

## Shortlist template (one per finalist paper)
| Field | Value |
|---|---|
| Title / authors | |
| Journal / publisher / year | |
| DOI | |
| Impact factor + where verified (URL + date) | |
| Dataset (name, public?, licence) | |
| DL model (architecture, size, train cost) | |
| Symbolic half (KB/rules/inference in the paper) | |
| What we implement / what we modify or cut | |
| Biggest risk | |

## Shortlist delivered 24 Nov 2026 (Muse screening — NOT yet approved)

Screened against the 5-point filter above; paper + domain still need
Dr. Sharif's approval before any implementation (hard gate, brief §7).

- **#1 RECOMMENDED — Rice Disease Diagnosis (agriculture):** Information
  Processing in Agriculture (Elsevier, IF 8.9); public PaddyDoctor dataset
  (16,000+ photos); small ResNet-34 fine-tune. Best fit on implementability
  + dataset + symbolic half.
- **#2 Runner-up — Crop Nutrient Deficiency:** Computers and Electronics in
  Agriculture (IF 10.3); claimed-public dataset, but the download link had
  NOT been found in this pass — verify before presenting.
- **#3 — Education (KBANN):** a KBANN paper with a private dataset; usable
  only if a public dataset substitute is accepted.
- **No clean 2026 neuro-symbolic paper found** for the restaurant/diet or
  healthcare directions in this pass.
- **Screened OUT:** (a) Singh et al., "ΔSemantics", Knowledge and
  Information Systems (Springer) 68, 283 (2026), DOI
  10.1007/s10115-026-02897-w — passes venue/year but fails semester
  implementability (ontology reasoning with proof certificates over
  HotpotQA/FB15k-237/Visual Genome, no small DL core); useful only as an
  example of the venue bar. (b) Anitha & Banu, Scientific Reports (2026),
  DOI 10.1038/s41598-026-62997-z — Article in Press, CNN on text features
  (not food images), no symbolic half; Scientific Reports counts as
  "Springer" only if Dr. Sharif confirms — conditional healthcare fallback.
- **Next step:** Wadi picks a paper (recommendation stands at #1 Rice
  Disease); take top pick + runner-up to Dr. Sharif for paper + domain
  approval, and ask the deadline + submission method missing from the
  brief at that meeting.
