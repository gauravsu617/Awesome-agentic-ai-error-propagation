# Phase V — Evidence and Submission Checklist

**Source:** `Phase5.zip` inside `FINAL ATR(1).zip`.

## Manuscript
- [ ] Verify the research brief and question against earlier phases.
- [x] Document the simulation rule from the notebook source; standalone regeneration script added, but it must be run and compared before claiming independent reproduction.
- [ ] Run evaluation on the original trial-level CSV.
- [x] Replace provisional manuscript values with statistics recalculated from the committed raw multi-seed CSV; clean evaluator rerun remains pending.
- [ ] Add verified original references and complete BibTeX.
- [ ] Add actual figures/tables exported by the evaluator.
- [ ] Check methods, results, discussion and limitations against evidence.
- [ ] Update the abstract after final verified results.
- [ ] Compile LaTeX and inspect the generated PDF.
- [ ] Confirm author metadata, formatting and page-length requirements.

## Technical review
- [ ] Resolve raw-result verification.
- [x] Specify the propagation equation and random-seed behavior in the manuscript/audit; rerun the updated paired-CI evaluator after pulling latest changes.
- [ ] Check pairing and choose uncertainty estimates accordingly.
- [ ] Address related-work coverage and novelty wording.
- [ ] Avoid generalizing beyond the simulation.
- [ ] Complete author responses with evidence, not assertions.

## Repository/reproducibility
- [ ] Confirm repository URL, branch and commit.
- [ ] Include verified dependencies and versions.
- [x] Document the raw CSV locations, simulation provenance, and exact evaluator command; licensing review remains pending.
- [x] Document the raw CSV row counts, required fields, failure-flag definition, and paired key in `EXPERIMENT_DATA_AUDIT.md`.
- [ ] Preserve output from a clean run of `simulate_phaseiii.py` and the updated evaluator, compare regenerated CSVs to committed inputs, and inspect the checksum manifest.
- [ ] Test the workflow from a clean clone.

A checked box should mean the corresponding evidence exists and has been inspected, not merely that the task is planned.
