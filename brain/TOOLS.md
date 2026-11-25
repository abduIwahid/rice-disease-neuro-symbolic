# TOOLS — one per category, fewest services possible

| Category | Pick | Why / notes |
|---|---|---|
| Language | Python 3.11+ | brief mandates Python |
| DL framework | **PyTorch + torchvision** | team's PAI stack; pretrained weights for fine-tuning. Fallback: TensorFlow/Keras only if the approved paper's official code demands it (ADR it) |
| Tabular baseline | scikit-learn | only if the chosen direction is tabular (B-ii / D) |
| Rule/KRR engine | **hand-written Python** | ADR-003 — no experta/kanren core |
| CLI | stdlib (`argparse`, `cmd` or plain loop) | zero dependencies for the interface |
| Tests | pytest | |
| Training compute | Local machine first; **Google Colab free GPU** as the scale-up | free tier: session limits apply — checkpoint to Drive after every epoch block; never leave the only copy of a checkpoint in a Colab session |
| Dataset hosts | Kaggle / Hugging Face Datasets / UCI / official dataset pages | account: Kaggle (Wadi has one); licence recorded per dataset in DATA_MODEL.md |
| Paper search | IEEE Xplore, ScienceDirect, SpringerLink, Google Scholar (discovery) | access via university subscriptions where needed — verify on official pages |
| Docs/report | Markdown in-repo; final report in Word/PDF per university format | slides: PowerPoint/Google Slides |
| Version control | Git + GitHub, `main` only | repo creation is a Phase 1 task (name TBD by Wadi) |

**Accounts to create now:** none new. **Free-tier gotchas:** Colab sessions
die — checkpoint discipline above; Kaggle download needs the account's API
token (never commit it); dataset "research use" licences — redistribution
limits checked before anything is committed or zipped (SUBMISSION.md).
