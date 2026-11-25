# SHORTLIST — 2026 paper candidates (Phase 0)

Screened 24 Nov 2026 against the 5-point filter in `../brain/PAPER_SELECTION.md`.
Every bibliographic detail below was verified on the publisher's / journal's own
pages during this pass (ScienceDirect article pages, the DCU institutional
repository copy of the article PDF, and the AIED society knowledge-base entry).
Impact-factor figures are quoted **from the publisher's journal pages as seen on
24 Nov 2026** — re-screenshot them into this folder as formal evidence before
the proposal goes to Dr. Sharif, per `README.md`.

## Verdict by direction

| Direction | Viable 2026 paper? |
|---|---|
| A. Restaurant / Diet | **No.** No 2026 IEEE/Elsevier/Springer journal paper with a real symbolic half was found (see near-misses). Do not force this direction. |
| B. Healthcare | **No clean pass.** The one on-method paper is a Scientific Reports *Article in Press* with the same "is Springer Nature = Springer?" ambiguity as the already-rejected Anitha & Banu paper (see near-misses). |
| C. Agriculture | **Yes — two strong papers** (Candidates 1 and 2). |
| D. Education | **Yes, with flags** (Candidate 3: dataset substitution required). |

---

## Candidate 1 — Rice disease diagnosis (Direction C) ⭐ TOP PICK

| Field | Value |
|---|---|
| Title / authors | "Neuro-symbolic AI for rice disease diagnosis with calibrated attention and rule-aware explanations" — Chatter Singh, Amar Singh, Sahraoui Dhelim |
| Journal / publisher / year | *Information Processing in Agriculture* — published by Elsevier B.V. on behalf of China Agricultural University (stated on the article itself). Received 22 Nov 2025, accepted 10 Feb 2026, **available online 11 Feb 2026** — a clean 2026 publication, no date ambiguity |
| DOI | 10.1016/j.inpa.2026.02.006 |
| Impact factor + where verified | **8.9**, shown on the journal's ScienceDirect page (Elsevier) as accessed 24 Nov 2026. (An older crawl of the journal's insights page showed 7.4 — a previous JCR year. Use the current publisher figure and screenshot it.) |
| Dataset (name, public?, licence) | **PaddyDoctor** — public corpus of 16,225 field images, 13 classes incl. Healthy; the paper's data-availability statement confirms it is publicly available from the original authors' repository, subject to their terms |
| DL model (architecture, size, train cost) | Fine-tuned **ResNet-34 + CBAM attention**, temperature-scaling calibration. Small — trains on a free Colab GPU in hours |
| Symbolic half (KB/rules/inference in the paper) | Agronomic symptom rules encoded in a lightweight **RDF/OWL knowledge graph**; a rule-aware validator checks predictions and produces auditable, human-readable explanations. Real but **post-hoc and thin** — a validator, not a full inference engine |
| What we implement / what we modify or cut | Implement the pipeline as published (CNN → calibrated probabilities → rule validation → explanation). **Extension (documented):** grow the validator into the project's full KB + forward/backward-chaining engine with treatment rules, so the brief's 20–25-rule and inference requirements are met by our KRR layer, exactly the kind of modification §3 of the brief asks us to document |
| Biggest risk | The symbolic half is the weakest of the three finalists — the viva defence must show our engine is a genuine extension of the paper's method, not decoration |

**Filter score:** 1 Small DL core ✅ (ResNet-34 fine-tune) · 2 Public dataset ✅ (PaddyDoctor, confirmed in the paper) · 3 Real symbolic half ⚠️ partial (genuine RDF/OWL rule validation, but post-hoc only) · 4 Five-box pipeline ✅ (image → CNN → facts → rule check → explained verdict) · 5 Verifiable venue ✅ (Elsevier journal, 2026, DOI resolves, IF on publisher page)

## Candidate 2 — Crop nutrient-deficiency diagnosis (Direction C) ⭐ TOP PICK

| Field | Value |
|---|---|
| Title / authors | "Concept and rule guided neural network for early crop leaf nutrient deficiency diagnosis" — Semanto Mondal, Antonino Ferraro, Fabiano Pecorelli, Martina Iammarino, Giuseppe De Pietro |
| Journal / publisher / year | *Computers and Electronics in Agriculture* (Elsevier), **Vol. 248, Article 111735** — issue dated July 2026; the article was already live on ScienceDirect as an article in press earlier in 2026 (exact online-first date not captured in this pass — verify on the article page) |
| DOI | 10.1016/j.compag.2026.111735 |
| Impact factor + where verified | **10.3**, shown on the journal's ScienceDirect page (Elsevier) as accessed 24 Nov 2026 (an older insights crawl showed 8.9 — previous JCR year) |
| Dataset (name, public?, licence) | **EarlyNSD** (ash-gourd leaf nutrient deficiencies). The paper's data-availability statement says "we have used publicly available dataset" — **but the exact download location was NOT located during this screening pass. Verify before committing** |
| DL model (architecture, size, train cost) | **ResNet-50 with a dual head**: deficiency-classification head + concept-prediction head (yellowing, edge discoloration, spots, vein greenness). Standard fine-tune, Colab-feasible |
| Symbolic half (KB/rules/inference in the paper) | The strongest of the three: predefined agronomic rules are combined with concept scores, domain knowledge is integrated as **differentiable fuzzy-logic rules** that guide learning, and an agricultural knowledge base drives recommendations. The concept bottleneck *is* the DL→symbolic bridge the brief wants |
| What we implement / what we modify or cut | Implement ResNet-50 dual-head + concept layer + fuzzy-rule guidance + KB recommendations. **Cut/replace:** the paper's RAG/LLM recommendation pipeline — replace with our own rule engine producing the recommendation and its trace (keeps the demo deterministic and the KRR marks ours). Document as a modification per brief §3 |
| Biggest risk | Dataset access: if EarlyNSD cannot actually be downloaded, the paper falls. Confirm the dataset link first; a PlantVillage-style substitute changes the task (disease ≠ nutrient deficiency), so this is a harder substitution than Candidate 3's |

**Filter score:** 1 Small DL core ✅ (ResNet-50 fine-tune) · 2 Public dataset ⚠️ flagged (authors state public; download location unverified) · 3 Real symbolic half ✅ (fuzzy rules + KB are core to the method, not bolted on) · 4 Five-box pipeline ✅ (image → concepts → rules → diagnosis + recommendation) · 5 Verifiable venue ✅ (Elsevier journal, 2026, DOI resolves, IF on publisher page)

## Candidate 3 — Educational data mining with KBANN (Direction D)

| Field | Value |
|---|---|
| Title / authors | "Towards responsible and trustworthy educational data mining: Comparing symbolic, sub-symbolic, and neural-symbolic AI methods" — Danial Hooshyar, Eve Kikas, Yeongwook Yang, Gustav Šír, Raija Hämäläinen, Tommi Kärkkäinen, Roger Azevedo |
| Journal / publisher / year | *International Journal of Artificial Intelligence in Education* (IJAIED), Article 100016, 2026 — cited from the accepted pre-proof; no volume/pages assigned yet. **Publisher note:** IJAIED moved from Springer to **Elsevier**; this article's DOI carries the Elsevier prefix (10.1016), so it satisfies the brief's Elsevier condition — expect older web listings to still say Springer |
| DOI | 10.1016/j.ijaied.2026.100016 |
| Impact factor + where verified | IJAIED is JCR-listed (Q1). The publisher figure visible in this pass was **8.5 (2024 JCR)**, shown on the journal's former Springer page and the AIED 2025 society page; aggregator sites cite a higher newer figure, which we do **not** rely on. **Re-verify the current JCR figure on the journal's Elsevier page and screenshot it before the proposal** |
| Dataset (name, public?, licence) | The paper's own data (Estonian Grade-3 SRL assessments → Grade-7 maths outcomes) is **NOT public** — the AIED knowledge-base entry states the data cannot be shared (confidentiality agreement with the Estonian Education and Youth Board). Filter point 2 therefore passes only via the allowed faithful substitute: **UCI Student Performance** (public) or OULAD (public), with the substitution declared in the proposal |
| DL model (architecture, size, train cost) | Small: a deep neural network baseline and **KBANN** (knowledge-based artificial neural network) as the neuro-symbolic method. Trains in minutes on CPU |
| Symbolic half (KB/rules/inference in the paper) | KBANN compiles self-regulated-learning theory rules into the network's structure; the symbolic knowledge measurably rescues the under-represented class (low performers) — a clean, explainable knowledge-injection story |
| What we implement / what we modify or cut | Implement KBANN with an SRL/advising rule set on the substitute dataset; **extension:** an advising layer (eligibility, interventions) on top of the risk prediction, which the paper does not build. Cut: the 7-model comparison (keep DNN vs KBANN only) |
| Biggest risk | Two viva exposures: (i) dataset substitution must be argued as faithful; (ii) the paper is a *comparison study*, so "implementing its core approach" = the KBANN method, not a finished system — the system around it is our extension |

**Filter score:** 1 Small DL core ✅ (small tabular networks) · 2 Public dataset ⚠️ partial (paper's data private; faithful public substitute exists and is declared) · 3 Real symbolic half ✅ (KBANN rule injection is the paper's core) · 4 Five-box pipeline ✅ (student record → model → risk fact → advising rules → explained advice) · 5 Verifiable venue ✅ with note (Elsevier 2026 article + DOI verified; current-year IF figure still to be screenshot-verified)

---

## Ranked recommendation

**1. Candidate 1 — Singh et al., rice disease (Direction C).** The lowest-risk
approval package: every fact is verified, the dataset is unambiguously public
and downloadable today, the DL model is the smallest of the three, the 2026
date is clean (online 11 Feb 2026, no in-press or issue-year ambiguity), and
the venue check is one screenshot. The thin symbolic half is a *known,
fixable* weakness — the brief explicitly allows documented extensions, and
building the full rule engine on top of the paper's validator is precisely the
KRR work the project is graded on.

**2. Candidate 2 — Mondal et al., nutrient deficiency (Direction C).** The
most genuinely neuro-symbolic method of the three (concept bottleneck +
fuzzy rules + KB) and the strongest journal (IF 10.3) — on method alone it
would be #1. It is ranked second for one practical reason: EarlyNSD's
download location could not be verified in this pass. **Action: spend 30
minutes confirming the dataset link; if it downloads, this becomes a
co-equal first choice and the team can pick on viva preference (concepts and
fuzzy rules vs. calibration and rule validation).**

Candidate 3 is a legitimate fallback if Dr. Sharif prefers the education
domain, but it carries the most explaining (private data + comparison-study
framing), so take it to the approval meeting as the runner-up, not the lead.

**Direction consequence:** both top picks are Direction C (agriculture). The
restaurant direction (A) has no viable 2026 paper and should be dropped at
the approval meeting with the screening evidence below; healthcare (B)
likewise has no clean pass this year.

---

## Near-misses — screened out, and why (auditable)

| Paper | Venue / DOI | Why it failed the filter |
|---|---|---|
| Singh et al., "ΔSemantics: a neuro-symbolic framework…" | *Knowledge and Information Systems* (Springer), 2026, DOI 10.1007/s10115-026-02897-w | Already screened out in the earlier pass: venue/year pass, but the method (ontology reasoning with proof-carrying ML over HotpotQA/FB15k-237 scale) is not implementable by a semester team — fails point 1 |
| Anitha & Banu, "Biometrically Anchored and Psychological States Aware Deep Learning for Enhanced Personalized Food Recommendation Systems" | *Scientific Reports* (2026), DOI 10.1038/s41598-026-62997-z | Already screened out: Article in Press, CNN over text features (not food images), no symbolic half (points 3), and Springer Nature vs "Springer" ambiguity (point 5) |
| Odhaib, Al-Maflehi, Gharaei & Gemci, "A tiered deep learning and symbolic reasoning framework for safe, explainable disease diagnosis" | *Scientific Reports* (2026), DOI 10.1038/s41598-026-68770-6 — received 25 Dec 2025, accepted 24 Aug 2026, published 10 Sep 2026 | Method is genuinely on-brief (residual MLP on the public DDXPlus dataset + ICD-10 neuro-symbolic safety layer) — but it is an **Article in Press** and carries the **same Springer Nature ambiguity** as Anitha & Banu, so it fails point 5 under the same strict reading applied before. Pipeline also sprawls (n8n orchestration + LLM router) against point 4. **If Dr. Sharif confirms Scientific Reports counts as "Springer", this becomes a viable Direction B candidate — worth one question at the approval meeting** |
| Deng & Tu, "NutriRec: Multimodal Large Language Models Enhanced Personalized Dietary Recommendation" | *IEEE Access* (2026), DOI 10.1109/access.2026.3660702 | Venue passes (IEEE journal), but the core is a multimodal-LLM representation learner + sequential recommender — no KB, rules, or inference (fails point 3), and the DL core is LLM-centric rather than a small trainable model (fails point 1) |
| Banerjee, "Physics-Informed Neuro-Symbolic Recommender System: A Dual-Physics Approach for Personalized Nutrition" | arXiv:2601.19244 (Jan 2026) | Preprint only — no journal publication found (fails point 5). Method is also heavy (heterogeneous GNN + thermodynamic loss + simulated-annealing optimiser) for a semester team (point 1) |
| Chhetri et al., "Symbolic knowledge extraction for explainable nutritional recommenders" | *Computer Methods and Programs in Biomedicine* (Elsevier) | Methodologically the ideal Direction A paper (NN → Prolog rules + expert prescriptions → explainable recommendations) — but it is from **2023**, not 2026 (fails point 5's year). Cited here as evidence the restaurant paper-type exists, just not in 2026 |
| Fu et al., "EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction" | arXiv:2608.26107 (May 2026) | Preprint only (also on Research Square); no IEEE/Elsevier/Springer journal version found (fails point 5). Temporal Transformer core is also at the heavy end (point 1) |
| Hooshyar et al., "Neural-Symbolic Knowledge Tracing" (Responsible-DKT) | arXiv:2604.08263 (Apr 2026) | Preprint only at screening time; no journal version found (fails point 5). Same group's journal-published neuro-symbolic work is Candidate 3 |
| Mohanraj & Shanmugavadivu, "A Neuro-Symbolic Feedback Engine for Evidence-Grounded Feedback to At-Risk Students…" | *International Research Journal on Advanced Science Hub* (2026), DOI 10.47392/IRJASH.2026.037 | Publisher is not IEEE/Elsevier/Springer and no JCR impact factor could be verified (fails point 5) |
| Wang & Qin, "Explainable neuro-symbolic AI for automated interpretation of corneal topography…" (+ the group's chronic-eye-disease paper) | *Frontiers in Artificial Intelligence* / *Frontiers in Digital Health* (2026), DOIs 10.3389/frai.2026.1713747, 10.3389/fdgth.2026.1836890 | Frontiers is not one of the three named publishers (fails point 5); methods are also LLM- and CNN–ViT-heavy with private clinical data (points 1–2) |
| Zou et al., "Neuro-symbolic AI model with heart failure ontology…" | *European Heart Journal* Suppl. (Oxford Academic), 2026, DOI 10.1093/eurheartj/ehag785.1193 | Conference-supplement abstract, wrong publisher (OUP), and a private multicentre registry dataset (fails points 2 and 5) |
| "Graph–Neurosymbolic Neural Networks for Trustworthy Clinical Decision Support" | *Proc. Machine Learning Research* 319 (IndabaX Nigeria 2026) | Conference proceedings, not a journal (fails point 5); MIMIC-IV/eICU are credentialed-access datasets and the GNN+logic framework is heavy (points 1–2) |
| Mondal et al. — see Candidate 2 | — | — |

## What could NOT be verified in this pass (flagged, not filled in)

1. **EarlyNSD download location** (Candidate 2) — authors state the dataset is
   public; no repository link was located. Verify before the approval meeting.
2. **Candidate 2's exact online-first date** — the issue is dated July 2026
   (Vol. 248) and the article was live on ScienceDirect before that; the
   precise "available online" date was not captured.
3. **IJAIED's current-JCR-year impact factor** (Candidate 3) — the verified
   publisher figure from this pass is 8.5 (2024 JCR); screenshot the current
   figure from the journal's Elsevier page as formal evidence.
4. **Candidate 3's volume/pages** — none assigned yet (accepted pre-proof,
   article 100016).
5. Whether *Scientific Reports* counts as "Springer" under the brief — only
   Dr. Sharif can settle this; it decides whether the Odhaib et al. healthcare
   paper (near-miss table) is usable.

---

## Friday prep — access update (25 Nov 2026)

Soft copies prepared in `friday/` for the Friday 27 Nov selection class
(see `friday/COMPARISON.md`):

- **Candidate 1 (rice):** full publisher's PDF obtained — open access (CC BY),
  copy taken from the DCU institutional repository (DORAS, doras.dcu.ie/32440),
  15 pp., DOI printed on p.1. Saved as `friday/01-rice-disease.pdf`.
- **Candidate 2 (nutrient):** the article is confirmed **open access (CC BY
  4.0)** via the Elsevier API and OpenAlex/Semantic Scholar — there is no
  paywall. However, ScienceDirect's bot check blocked every direct PDF
  download attempt at prep time, and no repository copy exists yet, so only
  the official abstract page was saved (`friday/02-crop-nutrient-ABSTRACT-ONLY.html`).
  The full PDF is a one-click "View PDF" download from the article page in a
  normal browser, or via the university library. EarlyNSD's download link is
  still unlocated (unchanged from the screening above).
- **Candidate 3 (KBANN):** full text obtained as the authors' preprint
  (arXiv:2504.00615v2, 53 pp., via the alphaXiv mirror) — same title/authors
  as the journal article; the journal version remains an accepted pre-proof.
  Saved as `friday/03-education-kbann.pdf`.
