# Phase IV — Contribution, Evaluation, and Evidence

**Research topic:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation  
**Source:** Phase IV report and evaluator included in the uploaded `FINAL ATR(1).zip`.

## Research question
In a four-stage simulated research workflow, how does a conditional downstream error-propagation rule affect stage-error accumulation compared with a constant per-stage error probability?

## Prespecified comparison
- Conditions: `independent` and `propagation`.
- Base error rates described in the source report: 0.0, 0.1, 0.2, and 0.3.
- Workflow length: four stages.
- Earlier project description: 30 seeds × 100 trials per seed × four rates × two conditions (24,000 rows); verify this against the actual data.
- Primary outcome: mean number of stage errors per workflow.
- Secondary outcome: proportion of workflows containing at least one stage error, with Wilson 95% confidence intervals.

## Evaluator checks
The supplied `evaluate_phaseiv.py` is described as checking required columns, missing values, allowed rates and stage-error ranges, Boolean parsing of `workflow_failed`, consistency between `workflow_failed` and `stage_errors > 0`, duplicate trial keys when seed/trial columns exist, and grouped summary metrics.

Example command documented in the source report:

```bash
python evaluate_phaseiv.py --input predictions/multi_seed_results.csv --outdir results/phase_iv
```

Run it from the correct project directory and adjust paths only to match the checked-out tree. A command written in a report is not proof it has been executed successfully.

## Important metric caveat
If `workflow_failed` is defined as `stage_errors > 0`, the binary failure indicator is already true after the first stage error. Later propagated errors can increase the stage-error count without changing the binary any-error failure rate. Equal failure rates under this definition do not show that propagation has no effect.

## Provisional values from the source report
These values were transcribed in the source Phase IV report and must be recomputed from the original CSV before being treated as verified findings.

| Base error rate | Mean stage errors: independent | Mean stage errors: propagation | Difference |
|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.0000 | 0.0000 |
| 0.1 | 0.3847 | 0.4917 | +0.1070 |
| 0.2 | 0.7887 | 0.9953 | +0.2067 |
| 0.3 | 1.1790 | 1.5100 | +0.3310 |

The source report also gives provisional any-error failure rates of 0.3360, 0.5787, and 0.7447 at base rates 0.1, 0.2, and 0.3, respectively. Recompute these as well.

## Limitations
The described simulator uses synthetic errors, four stages, a specified propagation mechanism, and no recovery or handoff verification. It does not establish the error rates of deployed LLM agents, real-world research quality, terminal-output correctness, or generalization beyond the simulator. The propagation increment is a modeling assumption unless independently calibrated.

## Status
**Evaluation protocol documented. Numerical claims remain provisional until the supplied raw data are checked and the evaluator is run with saved logs.**
