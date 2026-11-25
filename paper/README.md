# Paper

This project implements one paper:

**Singh, C., Singh, A., & Dhelim, S. (2026).** "Neuro-symbolic AI for rice
disease diagnosis with calibrated attention and rule-aware explanations."
*Information Processing in Agriculture* (Elsevier), impact factor 8.9
(publisher's journal page, verified November 2026).

- DOI: [10.1016/j.inpa.2026.02.006](https://doi.org/10.1016/j.inpa.2026.02.006)
- File: [`singh-2026-rice-disease.pdf`](singh-2026-rice-disease.pdf)
- Open access (CC BY) — publisher's version of record, obtained via the
  DCU DORAS institutional repository.

**Headline result (as reported in the paper):** on a rigorously
de-duplicated test split of the public PaddyDoctor corpus (16,225 field
images, 13 classes), the model achieves **95.13% accuracy (weighted F1:
95.14%)** with a median latency of 4.6 ms.

**What we take from it:** the ResNet-34 + CBAM classifier, temperature-
scaling calibration, the PaddyDoctor benchmark protocol, and the idea of
auditing predictions against agronomic symptom rules.

**Our declared extension:** the paper's symbolic layer is a post-hoc
validator (it labels each prediction Aligned / Conflict / NA against
symptom rules — no chaining, no unification, no treatment knowledge, no
queries). We extend it into a full knowledge base with 20–25 rules and a
hand-built inference engine with reasoning traces, as documented in
[`../docs/proposal.md`](../docs/proposal.md). The selection record for
this paper lives in the project brain (`../brain/PAPER_SELECTION.md`).
