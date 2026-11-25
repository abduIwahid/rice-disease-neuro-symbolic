# Session 01 — Brain scaffold + same-day re-scope

- **Date:** 2026-11-24
- **Goal / request:** Create the project brain + full plan (NO code) for the
  AIC372 KRR semester project. Domain confirmed by Wadi that day: Restaurant
  Menu and Diet Recommendation System; team: Abdul Wahid, Faseeh,
  Daniyal Badshah.
- **What happened:** Mid-task, a STOP-AND-RE-SCOPE instruction arrived: Wadi
  had uploaded a *different* official brief
  (`AIC372_Semester_Project_Description.pdf`) — a Neuro-Symbolic
  Knowledge-Based Intelligent System in **Python** (DL model → symbolic
  facts → KB + 20–25 rules → inference engine → traces), centred on
  implementing a **2026 impact-factor journal paper** (IEEE/Elsevier/
  Springer) with **instructor approval of paper + domain before
  implementation**. The morning brief (SWI-Prolog expert system) had been
  read but **no files had been written from it**, so nothing on disk needed
  discarding.
- **What was done:** full brain written for the AFTERNOON brief —
  AGENT.md / README.md / CONTRIBUTING.md at root; brain/: 00-START-HERE
  (with the two-briefs warning), PRD (marks map for the new rubric),
  PAPER_SELECTION (implementability filter, search sources, 4 candidate
  directions incl. restaurant re-imagined + healthcare, shortlist procedure
  + template), ARCHITECTURE (pipeline, module map, hand-built engine design:
  unification, forward/backward chaining, NAF, conflict resolution,
  provenance), DATA_MODEL (fact layers, taxonomy, full predicate vocabulary
  + 22-rule plan for Direction A, dataset plan), API_SPEC (query contract,
  Q1–Q7, trace format), BUILD_PLAN (Phases 0–7 with the approval gate + cut
  list), TEAM (division proposal), SUBMISSION (new deliverables checklist),
  DECISIONS (ADR-001…005), TESTING (E/S matrices incl. success/failure/
  conflict), DEMO_PITCH, DEMO_DATA, JUDGE_QA, DESIGN, TOOLS, WORKFLOW,
  DEPLOYMENT, ENV, SECURITY, PRODUCTION_READINESS, RISKS, GLOSSARY,
  ETHICS_PRIVACY, RETRO, prompts/ (7 house templates, re-written for this
  project), changes/ initialised. Registry file created at
  `~/workspace/brain/projects/restaurant-diet-expert.md`.
- **Decisions + reasoning:** ADR-001 follow the afternoon brief (pending
  Wadi's confirmation) · ADR-002 domain not locked; paper+domain chosen
  together · ADR-003 hand-built inference engine (brief §7 grades KRR
  understanding; experta hides it) · ADR-004 fine-tuned PyTorch CNN ·
  ADR-005 CLI demo, no GUI.
- **Problems + fixes:** prompt templates initially copied from the
  face-attendance project carried its specifics (camera/GPS/Zod) — deleted
  and re-written for this project.
- **Status:** Done. **Next steps:** (1) Wadi confirms which brief is
  authoritative; (2) Phase 0 — each member brings 2 candidate papers;
  (3) approval meeting with Dr. M. Sharif.
- **Commit:** none (no repo yet).
