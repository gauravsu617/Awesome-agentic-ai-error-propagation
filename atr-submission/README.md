# AITR Research Submission: Error Propagation in Multi-Step Agentic AI Workflows

This directory contains selected text-based source and reproducibility materials from the supplied FINAL ATR package for the AI Tools for Research assignment.

## Research scope

The project topic visible in the supplied artifacts is error propagation in multi-step agentic AI workflows used for research automation. The described workflow includes planning, literature search, source selection, evidence extraction, analysis, synthesis, verification, and report generation.

## Files currently mirrored here

- `evaluate_phaseiv.py`: validates a results CSV and writes grouped summaries, comparison tables (when both `independent` and `propagation` models are present), and plots.
- `notebooks/`: two Phase III notebooks, including the completed Prompts 10–11 notebook.
- `figures/`: four project figures.
- `results/predictions/`: original baseline, propagation, multi-seed, summary, and comparison CSVs.
- `results/figures/` and `results/logs/`: simulation plots and environment/validation records.
- `docs/EXPERIMENT_DATA_AUDIT.md`: data-integrity checks and recalculated summary statistics.
- `ATR_PHASE_IV_completed_Prompts_12_14.ipynb`: Phase IV protocol, CSV-validation, summary, and plotting notebook; it requires an actual results CSV to run.
- `references.bib`: bibliography source.
- `Prompts_and_Search_Queries.txt`: saved literature-search query notes.
- `docs/REPRODUCIBILITY_AUDIT.md`: evidence and reproducibility checklist.
- `docs/ZIP_ARCHIVE_INVENTORY.md`: source ZIP inventory and mapping guidance.
- `docs/PHASE_III_RESEARCH_AND_RESULTS.md`: Phase III artifact inventory and verification steps.
- `docs/PHASE_IV_EVALUATION_REPORT.md` and `docs/PHASE_IV_REPORT.md`: Phase IV metrics, validation, and provisional-result caveats.
- `docs/PHASE_V_MANUSCRIPT_REVIEW.md`, `docs/PHASE_V_PEER_REVIEW.md`, `docs/PHASE_V_REVISION_LOG.md`, `docs/PHASE_V_SUBMISSION_CHECKLIST.md`: Phase V review and evidence gates.
- `docs/PHASE_VI_AI_USE_AND_RESEARCH_INTEGRITY.md` and `docs/PHASE_VI_ACTIVITY_LOG_GUIDE.md`: AI-use and authentic activity-log guidance.

The original archive also contains additional LaTeX manuscript sources, PDFs, citation-verification and tool-rating workbooks, RIS exports, citation-map images, and nested phase ZIP files. The two Phase III notebooks, four main figures, raw baseline/propagation/multi-seed CSVs, experiment figures, and environment/validation logs are now mirrored here. The remaining files are listed in the archive manifest. See the [category-by-category archive manifest](ARCHIVE_MANIFEST.md) and [ZIP inventory](docs/ZIP_ARCHIVE_INVENTORY.md). The pre-existing paper artifact in this repository is available at [paper/RESEARCH_paper.pdf](../paper/RESEARCH_paper.pdf).

## Running the Phase IV evaluator

The script requires pandas, numpy, and matplotlib. Confirm compatible package versions in your actual environment before claiming reproducibility.

```bash
python -m pip install pandas numpy matplotlib
python evaluate_phaseiv.py --input path/to/multi_seed_results.csv --outdir results/phase_iv
```

The input CSV must include `error_rate`, `model`, `stage_errors`, and `workflow_failed`. If the evaluator finds invalid or inconsistent rows, it exits with an error. The script is an analysis utility. The committed CSVs have been checked and their summary statistics recalculated, but the evaluator and data-generation notebook still need a clean, documented rerun before claiming independent reproduction.

## Research integrity and reproducibility

- Do not invent experimental results, logs, dataset access, citations, or AI-use experiences.
- Preserve raw predictions/logs and the exact configuration used for each reported result.
- Mark missing evidence as unknown or test required.
- Trace every manuscript result and figure to a real output file and code cell/command.
- Verify third-party redistribution rights before committing PDFs, datasets, screenshots, or nested archives.

See [the reproducibility audit](docs/REPRODUCIBILITY_AUDIT.md), [citation integrity checklist](docs/CITATION_INTEGRITY_AUDIT.md), and [instructions for syncing the remaining archive artifacts](docs/LOCAL_SYNC_AND_UPLOAD.md).
