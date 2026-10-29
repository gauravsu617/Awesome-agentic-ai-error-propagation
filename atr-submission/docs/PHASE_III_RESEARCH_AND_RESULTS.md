# Phase III — Simulation, Source Artifacts, and Results Inventory

## Source archive inspected
The uploaded `FINAL ATR(1).zip` contains these Phase III-related artifacts:

- `ATR_PHASE_III_CODE.ipynb`
- `ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb`
- `agentic_error_propagation_results - Copy.zip`
- `evaluate_phaseiv.py`
- A results archive with trial-level and summary CSV files, figures, and logs.

The nested results archive contains:

- `predictions/baseline_results.csv`
- `predictions/propagation_results.csv`
- `predictions/multi_seed_results.csv`
- `predictions/final_comparison.csv`
- `predictions/multi_seed_summary.csv`
- `figures/error_propagation_comparison.png`
- `figures/final_model_comparison.png`
- `figures/environment_test_histogram.png`
- `logs/validation_report.json`
- `logs/environment_console.txt`
- `logs/environment_verification.json`
- `logs/gpu_verification.json`

## Interpretation boundary
The existence of notebooks, CSVs, figures, and logs in the ZIP establishes that these artifacts were supplied; it does not independently establish that they run in a clean environment or that their numerical results are correct. The raw trial-level data must be checked against the evaluator and the methods before numerical results are treated as final.

## Required verification
1. Inspect notebook execution order and outputs; restart the kernel and run all cells in a clean environment.
2. Record Python and package versions and any hardware/environment dependencies.
3. Check the raw CSV schema, row counts, missing values, valid rates, conditions, seeds, and duplicate trial keys.
4. Run the Phase IV evaluator on the actual trial-level CSV.
5. Compare evaluator outputs with the summary tables and manuscript claims.
6. Preserve evaluator logs and checksums alongside generated outputs.
7. Do not infer GPU execution from a GPU verification file alone; inspect the log and the actual experiment path.

## Status
**Source artifacts located in the supplied ZIP; independent reproduction and numerical verification remain required.**
