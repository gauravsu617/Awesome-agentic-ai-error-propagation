# AITR Research Submission: Error Propagation in Multi-Step Agentic AI Workflows

This directory holds the text-based source and reproducibility materials from the supplied FINAL ATR package for the AI Tools for Research assignment.

## Research scope

The project studies error propagation in multi-step agentic AI workflows used for research automation. The workflow described by the supplied materials includes planning, literature search, source selection, evidence extraction, analysis, synthesis, verification, and report generation.

## Files in this repository

- `evaluate_phaseiv.py`: validates a results CSV and writes grouped summaries, comparison tables (when both `independent` and `propagation` are present), and plots.
- `main.tex` and `main_acmart_overleaf.tex`: LaTeX manuscript sources from the supplied package.
- `references.bib`: bibliography source.
- `Prompts_and_Search_Queries.txt`: saved search-query notes.
- `ATR_PHASE_III_CODE.ipynb`, `ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb`, and `ATR_PHASE_IV_completed_Prompts_12_14.ipynb`: experiment notebooks from the supplied package.
- `docs/REPRODUCIBILITY_AUDIT.md`: evidence and reproducibility checklist.

The original archive also contains PDFs, spreadsheets, figures, RIS exports, and nested phase ZIP files. Not every binary artifact is mirrored in this GitHub directory; use the original FINAL ATR package for those files. The pre-existing paper artifact in this repository is available at [paper/RESEARCH_paper.pdf](../paper/RESEARCH_paper.pdf).

## Running the Phase IV evaluator

Python packages used by the script: pandas, numpy, and matplotlib. Confirm compatible package versions in your actual environment before claiming reproducibility.

Example:

```bash
python -m pip install pandas numpy matplotlib
python evaluate_phaseiv.py --input path/to/multi_seed_results.csv --outdir results/phase_iv
```

The input CSV must include `error_rate`, `model`, `stage_errors`, and `workflow_failed`. If the evaluator finds invalid or inconsistent rows, it exits with an error. The script is an analysis utility; its presence does not show that the experiments were executed.

## Research integrity and reproducibility

- Do not invent experimental results, logs, dataset access, citations, or AI-use experiences.
- Preserve raw predictions/logs and the exact configuration used for each reported result.
- Mark missing evidence as unknown or test required.
- Trace every manuscript result and figure to a real output file and code cell/command.
- Verify third-party redistribution rights before committing PDFs, datasets, screenshots, or nested archives.

See [the reproducibility audit](docs/REPRODUCIBILITY_AUDIT.md) for the checklist and status labels.
