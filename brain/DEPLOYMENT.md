# DEPLOYMENT — demo-machine setup (there is no server)

"Deployment" for this project = the system running reliably on the demo
machine. Checklist:

- [ ] Python 3.11+ and a fresh venv; `pip install -r requirements.txt`
      completes offline-after-install (wheels cached once — do the install
      BEFORE demo day, on the actual machine).
- [ ] Model checkpoint + KB files present; `python -m app.main --demo`
      passes end-to-end with networking disabled.
- [ ] Sample images bundled under `app/demo_images/` (no downloads on the day).
- [ ] Backup: full repo + checkpoint on a USB stick AND the backup demo
      recording (DEMO_PITCH.md).
- [ ] Rollback = the last green commit; `git status` clean before leaving
      for the demo.
