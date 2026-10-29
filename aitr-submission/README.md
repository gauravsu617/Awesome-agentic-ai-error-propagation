# AITR Research Submission: Error Propagation in Multi-Step Agentic AI Workflows

This directory contains selected text-based source and reproducibility materials from the supplied FINAL ATR package for the AI Tools for Research assignment.

## Research scope

The project topic visible in the supplied artifacts is error propagation in multi-step agentic AI workflows used for research automation. The described workflow includes planning, literature search, source selection, evidence extraction, analysis, synthesis, verification, and report generation.

## Files currently mirrored here

- `evaluate_phaseiv.py`: validates a results CSV and writes grouped summaries, comparison tables (when both `independent` and `propagation` models are present), and plots.
- `ATR_PHASE_IV_completed_Prompts_12_14.ipynb`: Phase IV protocol, CSV-validation, summary, and plotting notebook; it requires an actual results CSV to run.
- `references.bib`: bibliography source.
- `Prompts_and_Search_Queries.txt`: saved literature-search query notes.
- `docs/REPRODUCIBILITY_AUDIT.md`: evidence and reproducibility checklist.

The original archive also contains LaTeX manuscript sources, Jupyter notebooks, PDFs, spreadsheets, figures, RIS exports, and nested phase ZIP files. Those files are listed in the original local package but are not all mirrored as separate GitHub files in this directory. The pre-existing paper artifact in this repository is available at [paper/RESEARCH_paper.pdf](../paper/RESEARCH_paper.pdf).

## Running the Phase IV evaluator

The script requires pandas, numpy, and matplotlib. Confirm compatible package versions in your actual environment before claiming reproducibility.

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
