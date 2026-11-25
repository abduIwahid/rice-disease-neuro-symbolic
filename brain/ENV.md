# ENV — environment variables

This project needs **no secrets and no required env vars**. The only
credential in play is optional and lives outside the repo:

| Name | Purpose | Secret? | Where |
|---|---|---|---|
| Kaggle API credentials (`kaggle.json`) | dataset download, only if the chosen dataset is Kaggle-hosted | YES | `~/.kaggle/kaggle.json` on the dev machine — never in the repo, never in the submission zip |

Runtime knobs are code config, not env vars: confidence threshold and
chaining depth cap live in `engine/integrate.py` / `engine/backward.py`
and are documented in ARCHITECTURE.md.
