# Experimental Data Audit and Recalculated Results

**Status:** raw CSV structure and summary arithmetic checked against the files currently committed to this repository. This is not an independent regeneration of the simulation.

## Inputs checked

| File | Data rows | Findings |
|---|---:|---|
| `results/predictions/baseline_results.csv` | 400 | Four rates × 100 trials; required fields present |
| `results/predictions/propagation_results.csv` | 800 | Four rates × two conditions × 100 trials |
| `results/predictions/multi_seed_results.csv` | 24,000 | Four rates × two conditions × 30 seeds × 100 trials |
| `results/predictions/multi_seed_summary.csv` | 8 | Recalculated means and standard deviations match the stored summary |
| `results/predictions/final_comparison.csv` | 4 | Mean differences and any-error rates match the recalculation |

The raw multi-seed records have no missing required values, invalid error-rate values, negative stage-error counts, mismatches between `workflow_failed` and `stage_errors > 0`, or duplicate keys when keyed by seed, trial, rate, and model.

## Recalculated summary

| Base error probability | Independent mean stage errors | Propagation mean stage errors | Paired mean difference | Approx. 95% CI for paired difference | Any-error rate in both conditions |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000–0.0000 | 0.0000 |
| 0.1 | 0.3847 | 0.4917 | 0.1070 | 0.0933–0.1207 | 0.3360 |
| 0.2 | 0.7887 | 0.9953 | 0.2067 | 0.1886–0.2247 | 0.5787 |
| 0.3 | 1.1790 | 1.5100 | 0.3310 | 0.3092–0.3528 | 0.7447 |

There are 3,000 observations per condition and rate. Paired differences are computed by matching seed, trial, and base error probability. Confidence intervals use the approximate normal form mean difference ± 1.96 × standard error of the paired differences.

## Interpretation and limits

- The notebook's generator uses four stages. For the propagation condition, the next stage's error probability is `min(1, p + 0.30)` if the immediately preceding stage had an error; otherwise it is `p`.
- The generator resets the same random seed for each condition, so independent and propagation rows can be matched. In these saved records, propagation stage-error counts are never below the matched independent counts. Treat this as a consequence of the simulator's construction, not as a measured property of deployed AI agents.
- `workflow_failed` means “at least one stage error.” Once a workflow has its first error, further downstream errors cannot increase this binary indicator. Therefore equal any-error rates are expected and do not test terminal-answer correctness.
- The environment/GPU JSON logs and existing `validation_report.json` are artifacts supplied with the archive. Their PASS labels are not proof that the full simulation was rerun in this session.
- The analysis above is a direct recalculation from the committed CSV data. The Python evaluator and the data-generation notebook still need to be executed in a clean, documented environment; save their console output and generated artifacts before calling the experiment independently reproduced.

## Local evaluator command

From the repository root, run:

```cmd
python atr-submission\evaluate_phaseiv.py --input atr-submission\results\predictions\multi_seed_results.csv --outdir atr-submission\results\phase_iv_recomputed
```

The evaluator requires pandas, numpy, and matplotlib. Preserve the input CSV and compare the newly generated summary and plots against the values above. Any discrepancy should be investigated and documented rather than silently overwritten.


## Standalone regeneration workflow

A standalone script transcribed from the final multi-seed simulation cell in
`notebooks/ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb` is available at
`simulate_phaseiii.py`. It writes to a separate directory so that the committed
input CSVs are not overwritten.

From the repository root, run:

```cmd
python atr-submission\simulate_phaseiii.py --outdir atr-submission\results\phase_iii_reproduced
```

This should generate 24,000 rows (30 seeds, four rates, two conditions, and 100
trials per seed/rate/condition), a summary CSV, and a JSON manifest with SHA-256
checksums. Compare the regenerated CSVs to the committed files before describing
the experiment as independently reproduced. The script is a faithful standalone
transcription of the notebook cell, but the regeneration command must actually
be run and its output inspected on the target machine.

The evaluator also exports paired mean-difference confidence intervals to
`phaseiv_comparison.csv` when the input contains `seed`, `trial`, and
`error_rate` columns. Run the updated evaluator after pulling the latest
repository changes; preserve its console output and generated artifacts.
