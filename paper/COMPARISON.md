# Friday Paper Selection — Comparison Sheet

**AIC372 KRR Semester Project** · Team: Abdul Wahid, Faseeh, Daniyal Badshah
**For:** Dr. Muhammad Sharif — paper selection, Friday 27 Nov 2026 class
**Brief:** implement the core approach of a 2026 neuro-symbolic paper from an IEEE / Elsevier / Springer impact-factor journal.

| | **1 — Rice disease** ⭐ | **2 — Crop nutrient deficiency** ⭐ | **3 — Education (KBANN)** |
|---|---|---|---|
| **Title** | Neuro-symbolic AI for rice disease diagnosis with calibrated attention and rule-aware explanations | Concept and rule guided neural network for early crop leaf nutrient deficiency diagnosis | Towards responsible and trustworthy educational data mining: Comparing symbolic, sub-symbolic, and neural-symbolic AI methods |
| **Authors** | Chatter Singh, Amar Singh, Sahraoui Dhelim | Semanto Mondal, Antonino Ferraro, Fabiano Pecorelli, Martina Iammarino, Giuseppe De Pietro | Danial Hooshyar, Eve Kikas, Yeongwook Yang, Gustav Šír, Raija Hämäläinen, Tommi Kärkkäinen, Roger Azevedo |
| **Journal (publisher)** | *Information Processing in Agriculture* (Elsevier) | *Computers and Electronics in Agriculture* (Elsevier), Vol. 248, Art. 111735 | *International Journal of Artificial Intelligence in Education* (Elsevier; formerly Springer) |
| **Impact factor** | **8.9** (publisher's journal page, Nov 2026) | **10.3** (publisher's journal page, Nov 2026) | **8.5** (2024 JCR figure — current-year figure to be re-verified) |
| **DOI** | 10.1016/j.inpa.2026.02.006 | 10.1016/j.compag.2026.111735 | 10.1016/j.ijaied.2026.100016 |
| **Soft copy brought** | ✅ Full paper — publisher's version, 15 pp. (`01-rice-disease.pdf`) | ⚠️ **Abstract page only** (`02-crop-nutrient-ABSTRACT-ONLY.html`) — the article is open access (CC BY), but ScienceDirect's bot check blocked the PDF download at prep time; full PDF is one click (“View PDF”) on the article page or via the university library | ✅ Full paper — author preprint (arXiv:2504.00615v2), 53 pp. (`03-education-kbann.pdf`); the journal version is an accepted pre-proof with the same content |

## The method, in two lines each

1. **Rice disease** — A fine-tuned ResNet-34 with CBAM attention classifies rice-leaf photos; temperature scaling calibrates its confidence. An RDF/OWL rule graph then checks each prediction against agronomic symptom rules and explains the verdict in plain language.
2. **Crop nutrient deficiency** — A ResNet-50 with two heads predicts the deficiency *and* human-named visual concepts (yellowing, edge discoloration, spots, vein greenness). Differentiable fuzzy-logic rules built from agronomic knowledge guide training, and a knowledge base turns outputs into recommendations.
3. **Education (KBANN)** — Seven models from three AI families are compared on predicting students' later maths performance from self-regulated-learning data. The neuro-symbolic entry, KBANN, has theory rules compiled directly into the neural network's structure — and it is the only method that keeps finding the low performers when the data is imbalanced.

## Dataset

1. **PaddyDoctor** — public, 16,225 field images, 13 classes. Downloadable today. ✅
2. **EarlyNSD** (ash-gourd nutrient deficiencies) — authors state it is publicly available, **but the download link has not been located yet** ⚠️ — first task if this paper is selected is confirming dataset access.
3. The paper's own data is **private** (Estonian school data under a confidentiality agreement) ⚠️ — implementation would use a declared public substitute (UCI Student Performance or OULAD), which the brief allows if documented.

## What implementation means for our team (3 students, one semester)

1. **Rice** — Smallest DL job of the three (ResNet-34 fine-tune, hours on a free Colab GPU). The paper's rule layer is a post-hoc validator, so *our* main KRR work — growing it into a full knowledge base with 20–25 rules and a forward/backward-chaining engine — is a documented extension, exactly what the brief rewards.
2. **Nutrient** — The most complete neuro-symbolic method as published (concept bottleneck + fuzzy rules + KB), so the implementation follows the paper most faithfully. We would replace its RAG/LLM recommendation step with our own rule engine (documented modification). Risk sits entirely in the dataset question above.
3. **Education** — Lightest compute (small tabular networks, trains in minutes on CPU). Two things to defend in the viva: the dataset substitution, and that "implementing the paper" means implementing the KBANN method (the paper is a comparison study, not a finished system) plus our own advising layer on top.

## Recommendation

**1st choice: Paper 1 (Rice disease)** — every fact verified, dataset public and in hand, smallest model, cleanest 2026 date, full text already with us. **Co-equal if the dataset checks out: Paper 2 (Nutrient deficiency)** — the strongest method and journal; it becomes first choice the moment EarlyNSD is confirmed downloadable. **Paper 3 (Education)** is a sound fallback if an education-domain project is preferred, accepting the dataset substitution.

**Why is there no restaurant/diet paper in this set?** We screened for one first — it was our original domain — but no 2026 IEEE/Elsevier/Springer journal paper with a genuine symbolic-reasoning half exists for food/diet recommendation (the closest matches were an LLM recommender with no rules, a preprint, and a perfect-fit paper from 2023). The full screening is documented in `../SHORTLIST.md`, so we brought the three papers that actually pass the brief's filter instead.
