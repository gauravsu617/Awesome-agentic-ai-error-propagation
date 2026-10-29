# Phase V — Evidence and Submission Checklist

**Source:** `Phase5.zip` inside `FINAL ATR(1).zip`.

## Manuscript
- [ ] Verify the research brief and question against earlier phases.
- [x] Document the simulation rule from the notebook source; standalone regeneration script added, but it must be run and compared before claiming independent reproduction.
- [x] Run evaluation on the original trial-level CSV; Phase IV evaluator completed successfully in GitHub Actions run #7.
- [x] Recalculate manuscript statistics from the committed raw multi-seed CSV; the evaluator outputs summary/comparison tables and plots, including paired confidence intervals.
- [ ] Add verified original references and complete BibTeX.
- [x] Include the evaluator-derived results table in the manuscript; generated plots are retained as workflow artifacts. Consider adding a plot to the final paper if page limits permit.
- [ ] Check methods, results, discussion and limitations against evidence.
- [x] Update the abstract with recalculated results from the committed CSV; recheck after final author and formatting edits.
- [ ] Compile LaTeX and inspect the generated PDF.
- [ ] Confirm author metadata, formatting and page-length requirements.

## Technical review
- [ ] Resolve raw-result verification.
- [x] Specify the propagation equation and random-seed behavior in the manuscript/audit; rerun the updated paired-CI evaluator after pulling latest changes.
- [x] Match trials by seed, trial, and base error rate; report approximate paired normal confidence intervals for mean stage-error differences.
- [x] Expand related work to cite all 23 bibliography entries and avoid claiming that background frameworks directly validate the simulated effect; primary-source and claim-support review remains open.
- [ ] Avoid generalizing beyond the simulation.
- [ ] Complete author responses with evidence, not assertions.

## Repository/reproducibility
- [ ] Confirm repository URL, branch and commit.
- [ ] Include verified dependencies and versions.
- [x] Document the raw CSV locations, simulation provenance, and exact evaluator command; licensing review remains pending.
- [x] Document the raw CSV row counts, required fields, failure-flag definition, and paired key in `EXPERIMENT_DATA_AUDIT.md`.
- [x] Preserve clean-run outputs as GitHub Actions artifacts; generator output exactly matches the committed input CSV and the updated evaluator passed in run #7. Checksum-manifest inspection remains open.
- [x] Test the automated workflow in a clean GitHub-hosted Ubuntu runner; run #7 passed simulation, exact CSV comparison, evaluation, bibliography compilation, PDF generation, and artifact upload. Latest manuscript edits still require a fresh successful run.

A checked box should mean the corresponding evidence exists and has been inspected, not merely that the task is planned.
