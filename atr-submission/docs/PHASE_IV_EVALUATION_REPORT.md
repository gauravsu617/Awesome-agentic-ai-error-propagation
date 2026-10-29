# Phase IV Evaluation Report

## Current status

The raw CSV files are now committed under `atr-submission/results/predictions/`. Their structure and summary arithmetic have been checked, and the current recalculated values are recorded in [EXPERIMENT_DATA_AUDIT.md](EXPERIMENT_DATA_AUDIT.md).

**Important:** this audit recalculates the saved CSVs. It is not a clean rerun of the Python evaluator or a regeneration of the simulation. Those remain reproduction steps.

## Inputs and counts

| File | Rows | Notes |
|---|---:|---|
| `baseline_results.csv` | 400 | 4 base rates × 100 trials |
| `propagation_results.csv` | 800 | 4 base rates × 2 conditions × 100 trials |
| `multi_seed_results.csv` | 24,000 | 4 base rates × 2 conditions × 30 seeds × 100 trials |
| `multi_seed_summary.csv` | 8 | 4 rates × 2 conditions |
| `final_comparison.csv` | 4 | One comparison row per base rate |

The multi-seed CSV has no missing required values, invalid base error rates, negative stage-error counts, failure-flag mismatches, or duplicate keys on `seed`, `trial`, `error_rate`, and `model`.

## Recalculated summary

| Base error probability | Mean errors: independent | Mean errors: propagation | Difference | Any-error rate: independent | Any-error rate: propagation |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 0.1 | 0.3847 | 0.4917 | 0.1070 | 0.3360 | 0.3360 |
| 0.2 | 0.7887 | 0.9953 | 0.2067 | 0.5787 | 0.5787 |
| 0.3 | 1.1790 | 1.5100 | 0.3310 | 0.7447 | 0.7447 |

The approximate 95% confidence intervals for the paired increase in mean stage errors are 0.0933–0.1207, 0.1886–0.2247, and 0.3092–0.3528 for base rates 0.1, 0.2, and 0.3. The paired unit is matched by seed, trial, and base error rate. Details and interpretation limits are in the experimental data audit.

## Interpretation guardrails

The generator uses four stages. In the propagation condition, the current-stage error probability is `min(1, p + 0.30)` when the immediately preceding stage had an error. It reuses the same seed for both conditions, so trial records are paired. The saved propagation count is never below the matched independent count; this is a property of the shared-random-number simulation design and must not be generalized to real AI systems.

The binary metric `workflow_failed` is defined as `stage_errors > 0`. Because a workflow is already marked failed after its first stage error, later errors can increase the stage-error count without increasing this binary rate. The current data therefore support a comparison of simulated stage-error accumulation, not a claim about end-to-end answer correctness.

## Reproduction command

From the repository root, run:

```cmd
python atr-submission\evaluate_phaseiv.py --input atr-submission\results\predictions\multi_seed_results.csv --outdir atr-submission\results\phase_iv_recomputed
```

Install `pandas`, `numpy`, and `matplotlib` if needed. Preserve the console output and generated summary/plots. Then rerun the data-generation notebook in a clean environment and compare the regenerated CSV with the committed file before describing the experiment as independently reproduced.
