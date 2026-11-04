# Phase V — Manuscript Revision Log

| Revision | Change | Evidence | Status |
|---|---|---|---|
| R1 | Reframed as a synthetic four-stage controlled simulation. | Phase III notebook and raw CSV. | Complete |
| R2 | Recomputed primary means from 24,000 raw records. | multi_seed_results.csv. | Complete |
| R3 | Recomputed paired 95% t intervals using matched (seed, trial) rows. | 3,000 pairs per base rate. | Complete |
| R4 | Clarified workflow_failed = stage_errors > 0. | Notebook invariant and row-level check. | Complete |
| R5 | Added Prompt 9 module specification and six sanity tests. | Supplementary module/test suite. | Complete; 6 tests passed in preparation environment |
| R6 | Prepared ACM sigconf,nonacm LaTeX source. | paper/main_acm_experiment.tex. | Source prepared; compile required |
| R7 | Prepared internal peer review and response table. | Peer-review report. | Complete as internal review |
| R8 | Prepared reproducibility instructions. | Reproducibility guide. | Prepared; clean-clone test required |

## Release gates
- Compile the ACM source in Overleaf and inspect the PDF.
- Verify citations against primary publication records and claim support.
- Run a clean-clone reproduction and retain actual console output.
- Record final commit SHA only after the final source is committed.