# DESIGN — presentation surfaces (CLI, slides, report figures)

The product is a terminal program; "design" here means the three surfaces
the examiner actually sees. House rules apply (solid colours, no gradients,
no AI-glow palettes).

## Terminal output
- Plain text, fixed-width friendly; traces indent by 3 spaces per proof level.
- Markers: `[fact, kb]`, `[dl_model, conf=0.87]`, `[derived via R-09]`,
  `NOT PROVABLE: … (closed world)`, `CONFLICT: …`.
- No colour dependence: output must read correctly in a plain log file or
  printed handout (colour, if the terminal supports it, is emphasis only).

## Slides + report figures
- Near-white background, near-black text, ONE accent (deep green `#1F7A4D`
  — food/health-neutral, print-safe). Accent used for the pipeline diagram
  arrows and table headers only.
- Font: a clean sans (Calibri/Arial family per university documents);
  pipeline + taxonomy diagrams drawn as simple boxes/arrows, reproducible
  from ARCHITECTURE.md / DATA_MODEL.md.
- Every figure carries a caption that states what it proves (figures are
  viva props, not decoration).
