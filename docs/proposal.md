*Draft — for presentation to the instructor on selection*

# Neuro-Symbolic Rice Disease Diagnosis with a Rule-Based Reasoning Engine

**AIC372 — Knowledge Representation and Reasoning · Semester Project Proposal**
**Team:** Abdul Wahid · Faseeh · Daniyal Badshah

## 1. The paper we will implement

Singh, C., Singh, A., & Dhelim, S. (2026). "Neuro-symbolic AI for rice disease
diagnosis with calibrated attention and rule-aware explanations."
*Information Processing in Agriculture* (Elsevier), available online
11 February 2026. DOI: 10.1016/j.inpa.2026.02.006 · Journal impact factor:
**8.9** (publisher's journal page, verified November 2026).

The paper couples a fine-tuned ResNet-34 + CBAM classifier with temperature-
scaling calibration and an RDF/OWL rule graph that audits each prediction
against agronomic symptom rules. On a rigorously de-duplicated test split of
the public PaddyDoctor corpus (16,225 field images, 13 classes), it reports
**95.13% accuracy (weighted F1: 95.14%)** with a median latency of 4.6 ms.

## 2. What we will build

- **DL model:** fine-tune ResNet-34 + CBAM on PaddyDoctor in PyTorch, with
  temperature scaling so the confidence score is calibrated, as in the paper.
- **Prediction → facts:** each output becomes symbolic facts — predicted
  disease, calibrated confidence, and observed symptom cues.
- **Knowledge base:** facts and relations for the 13 classes — diseases,
  their symptoms, severity levels, treatments, and contraindications.
- **Rules:** 20–25 rules covering diagnosis confirmation, severity
  escalation, treatment selection, and low-confidence / conflict handling.
- **Inference engine:** hand-built, with forward and backward chaining and
  unification; every conclusion carries a step-by-step reasoning trace.
- **Queries & demo:** a query interface answering 5+ sample queries (e.g.
  "Why was this leaf diagnosed as bacterial leaf blight?", "Which treatment
  applies, and what must be avoided?"), each answered with its trace.

## 3. Declared extension

The paper's symbolic layer is a post-hoc validator: it checks a prediction
against symptom rules and labels it Aligned / Conflict / NA, but it does not
itself reason — no chaining, no unification, no treatment knowledge, no
queries. We state openly that we extend that validator into a full knowledge
base and hand-built rule engine (Sections 2, bullets 3–6). The paper's model,
dataset, calibration, and audit idea are implemented as published; the
reasoning engine on top of them is our addition, documented as such.

## 4. Work division

- **Abdul Wahid** — DL model, prediction→fact integration, the paper's
  methodology and its faithful reproduction.
- **Faseeh** — knowledge base and the 20–25 rules (diseases, symptoms,
  treatments, contraindications).
- **Daniyal Badshah** — inference engine, query interface and reasoning
  traces; report and slides.

## 5. Tools

Python · PyTorch (training on a free Colab GPU) · a hand-built rule engine
in pure Python — no Prolog and no off-the-shelf reasoner, per the brief.
