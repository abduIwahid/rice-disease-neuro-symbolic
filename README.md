# Rice Disease Diagnosis — Neuro-Symbolic AI System

A neuro-symbolic system for diagnosing rice leaf diseases: a deep-learning
classifier reads a leaf photo, and a hand-built knowledge base and rule
inference engine reason over its prediction to produce a diagnosis and
treatment advice — with a step-by-step reasoning trace for every conclusion.

## How it works

```
leaf image
   │
   ▼
ResNet-34 + CBAM classifier (PaddyDoctor dataset)
   │  predicted disease + calibrated confidence
   ▼
symbolic facts ──► knowledge base (diseases · symptoms · treatments)
   │                        │
   ▼                        ▼
20–25 logical rules ──► hand-built inference engine
                        (forward / backward chaining, unification)
   │
   ▼
diagnosis + treatment advice + reasoning trace
```

## Paper

This project implements:

> Singh, C., Singh, A., & Dhelim, S. (2026). "Neuro-symbolic AI for rice
> disease diagnosis with calibrated attention and rule-aware explanations."
> *Information Processing in Agriculture* (Elsevier).
> DOI: [10.1016/j.inpa.2026.02.006](https://doi.org/10.1016/j.inpa.2026.02.006)

The paper couples a fine-tuned ResNet-34 + CBAM classifier with temperature
scaling and an RDF/OWL rule graph, reporting 95.13% accuracy (weighted F1:
95.14%) on a de-duplicated test split of the public PaddyDoctor corpus
(16,225 field images, 13 classes). Our declared extension: the paper's
post-hoc rule validator is grown into a full knowledge base with 20–25 rules
and a hand-built inference engine — see [`docs/proposal.md`](docs/proposal.md)
and the [`paper/`](paper/) index.

## Status

**Proposal phase.** The paper and the agriculture (rice disease) domain go
to the course instructor for approval on **27 Nov 2026**; implementation
follows the approval. The full project brain — plan, architecture,
decisions, risks — lives in [`brain/`](brain/).

## Dataset

**Paddy Doctor (PaddyDoctor)** — 16,225 labelled rice-leaf images in 13
classes, publicly released by Petchiammal et al. The images are **not**
stored in this repository; see [`datasets/README.md`](datasets/README.md)
for the source, licence, expected layout, and download instructions, or use
[`scripts/download_dataset.py`](scripts/download_dataset.py).

## Repository layout

| Path | Contents |
|---|---|
| `brain/` | Full project brain: PRD, architecture, build plan, paper-selection gate, decisions, risks, team, submission and testing notes |
| `paper/` | The implemented paper — PDF, citation and source note |
| `docs/` | The one-page project proposal |
| `datasets/` | Dataset guide (source, classes, licence, layout, download steps) — no images in git |
| `scripts/` | Helper scripts, starting with the dataset downloader |

## Team

- **Abdul Wahid** — DL model, prediction→fact integration, paper reproduction
- **Faseeh** — knowledge base and the 20–25 rules
- **Daniyal Badshah** — inference engine, query interface, reasoning traces, report and slides

## Tech

Python · PyTorch · a hand-built rule engine in pure Python (no off-the-shelf
reasoner).

## License

MIT — see [`LICENSE`](LICENSE). The paper PDF in `paper/` is the publisher's
open-access (CC BY) version of record and remains under its own licence.
