# Final AITR Reproducibility Guide

## Research scope
The executable study is a four-stage synthetic simulation comparing independent stage errors with conditional downstream propagation. It is not a live LLM-agent experiment and does not evaluate HotpotQA.

## Experimental settings
- Stages: planning, retrieval, evidence extraction, verification.
- Base error probabilities: 0.0, 0.1, 0.2, 0.3.
- Propagation increment: 0.30, capped at 1.0.
- Seeds: 2026–2055 (30 seeds).
- Trials: 100 per seed, rate, and condition.
- Total: 24,000 rows; 3,000 records per rate-condition cell.

## Statistical pairing
The notebook resets the same Python random seed for each condition. Pair records by (seed, trial) within each error rate. The paired comparison therefore uses 3,000 differences per rate.

## Reproduction
The repository contains Phase III notebooks and the Phase IV evaluator. Use the actual raw CSV path and preserve the original input:
```bash
python -m pip install numpy pandas matplotlib scipy
python atr-submission/evaluate_phaseiv.py --input atr-submission/results/predictions/multi_seed_results.csv --outdir atr-submission/results/final_recalculation
```

## ACM source
The local course-paper source uses \documentclass[sigconf,nonacm]{acmart}. Compile it in Overleaf with the ACM class and inspect the resulting PDF. It is a course manuscript, not an ACM-published article.

## Limitations
- Synthetic stochastic model; no live LLM or external benchmark execution.
- Fixed propagation increment.
- No terminal-output correctness or claim-level citation score.
- Clean-clone reproduction and ACM compilation remain student-side release checks.

## Prompt 9 sanity tests
From the repository root:
```bash
cd atr-submission/finalization
python -m unittest discover -s tests -v
```
The six tests cover output bounds, boundary probabilities, deterministic repeatability, failure-flag consistency, and invalid inputs. Re-run and preserve your own console output before claiming a test pass in your environment.
