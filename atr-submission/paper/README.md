# Phase V Manuscript Draft

This directory mirrors the manuscript source from `Phase5.zip` in the supplied FINAL ATR archive.

- `main.tex`: IEEE conference-style draft.
- `references.bib`: populated from the repository's 23-entry bibliography; only sources cited in `main.tex` are used by BibTeX, and every cited entry still requires a final primary-source check.

**Important:** The manuscript now reports summary statistics recalculated from the saved multi-seed CSV and includes approximate paired confidence intervals. The data have not been regenerated from scratch, and the evaluator has not yet been run in a clean local environment. Run `../evaluate_phaseiv.py` against `../results/predictions/multi_seed_results.csv`, retain the console output and generated files, verify cited sources against primary papers, compile the LaTeX, and inspect the PDF before submission. The author/institution fields are placeholders and must be completed by the author.

See the Phase V peer review, revision log and submission checklist in `../docs/`.
