# Phase IV — Source Report Summary

**Source:** `Phase4.zip` inside `FINAL ATR(1).zip`, including `Phase_IV_Report.md`, `evaluate_phaseiv.py`, and the Phase IV notebook.

## Research question
In a four-stage simulated research workflow, how does a conditional downstream error-propagation rule affect stage-error accumulation compared with a constant per-stage error probability?

## Reported setup
- Four ordered stages.
- Conditions: independent errors and conditional downstream propagation.
- Base error rates: 0.0, 0.1, 0.2, and 0.3.
- Project notes describe 30 seeds and 100 trials per seed, rate and condition. Verify the actual row count from the CSV before relying on it.

## Outcomes
- Primary: mean number of stage errors per workflow.
- Secondary: proportion of workflows with at least one stage error; Wilson 95% confidence intervals are suggested if assumptions are appropriate.
- Failure indicator: (F = 1(E > 0)).

If failure is defined as any stage error, later propagated errors may increase stage-error count without changing the binary failure indicator. Equal any-error rates therefore do not imply that propagation has no effect on severity.

## Provisional values in source report

| Base rate | Independent mean errors | Propagation mean errors | Difference |
|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.0000 | 0.0000 |
| 0.1 | 0.3847 | 0.4917 | 0.1070 |
| 0.2 | 0.7887 | 0.9953 | 0.2067 |
| 0.3 | 1.1790 | 1.5100 | 0.3310 |

The report also gives provisional any-error rates 0.3360, 0.5787, and 0.7447 at base rates 0.1, 0.2, and 0.3. These values are transcribed from the supplied report and must be recomputed from raw records before publication.

## Validation and limitations
The supplied evaluator is intended to check required columns, missing values, allowed rates/ranges, consistency of the failure flag, duplicate trial keys when seed/trial columns exist, and grouped summaries. The simulation uses synthetic errors and does not establish real-world failure rates for deployed LLM agents.

**Status:** source report mirrored as a summary; raw-data evaluation still required.
