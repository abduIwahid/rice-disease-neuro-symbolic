# SECURITY — proportionate to a local CLI coursework project

- **Secrets:** none required. Kaggle API token (if used) lives outside the
  repo (`~/.kaggle/`), never committed — check before every push.
- **Inputs:** all CLI input is validated (API_SPEC.md): malformed goals,
  unknown predicates, missing files → friendly errors. Image inputs are
  opened read-only via the DL loader; no path from user input reaches a
  shell command.
- **Dependencies:** pinned in `requirements.txt`; only the TOOLS.md list —
  additions need an ADR (dependency freeze, WORKFLOW.md).
- **Data files:** dataset downloads are data, never executed; model
  checkpoints are loaded with `weights_only=True` where the framework
  supports it (pickle-based checkpoints from untrusted sources are code
  execution — only our own or official pretrained weights are loaded).
