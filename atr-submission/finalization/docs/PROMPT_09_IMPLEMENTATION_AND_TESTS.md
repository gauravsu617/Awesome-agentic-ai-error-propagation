# Prompt 09 — Implementation and Code-Understanding Record

**Status:** The core implementation exists in the original Phase III notebook. This supplement adds explicit module documentation and independent sanity tests; it does not replace the original notebook.

## Implemented module
The simulator accepts a base per-stage error probability p, a condition flag, number of trials, random seed, and propagation increment delta=0.30. It returns one record per trial.

Four stages are processed in order: planning, retrieval, evidence extraction, and verification. Under the independent condition, every stage uses probability p. Under conditional propagation, a stage uses min(1, p + delta) only when the immediately preceding stage had an error.

## Input/output contract
- Inputs: error_rate in [0,1], propagation boolean, trials >= 1, integer seed, delta in [0,1].
- Outputs: trial, error_rate, model, stage_errors, workflow_failed, seed.
- stage_errors is an integer from 0 to 4.
- workflow_failed is defined as stage_errors > 0.

## Added tests
Six unit tests cover output count and bounds, zero-error boundary, full-error boundary, same-seed repeatability, failure-flag consistency, and invalid-input handling.

**Preparation-environment test result:** python -m unittest discover -s tests -v — 6 tests passed. This is not evidence that the full original Colab notebook was rerun from a clean environment on the student's machine.

## Limitations
The simulator is synthetic. It does not execute an LLM or measure actual research-agent correctness. The propagation increment is a fixed assumption. The any-error metric is insensitive to additional errors after the first error.