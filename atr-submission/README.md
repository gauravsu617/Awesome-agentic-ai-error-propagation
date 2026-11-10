# ATR — Error Propagation in Agentic Research Workflows

This repository contains the literature review and a controlled synthetic simulation study for the AI Tools for Research (ATR) assignment.

## Current experimental scope

Paper 2 models a four-stage research workflow: planning, retrieval, evidence extraction, and verification. It compares independent stage errors with a conditional one-step propagation rule. The primary archived dataset contains 24,000 trial records; the sensitivity analysis varies the assumed propagation increment over five settings.

**Important limitation:** this is a synthetic simulation. It is not a live LLM-agent experiment, a multi-agent framework evaluation, or a HotpotQA benchmark. The propagation increment is a fixed modelling assumption, not an empirically calibrated parameter. Conclusions apply only to the specified simulator.

## Repository layout

- `finalization/paper/` — Paper 2 LaTeX source and bibliography.
- `finalization/src/` — simulator support module.
- `finalization/tests/` — simulator unit tests.
- `results/predictions/` — archived primary CSV results.
- `notebooks/` — original Phase III notebooks.
- `docs/` — research decisions, validation, reproducibility, review, AI-use and viva materials.
- `paper/` — earlier literature-review manuscript sources; do not confuse these with the Paper 2 finalization source.

## Reproduction

From the repository root:

```bash
python -m pip install pandas numpy matplotlib
python atr-submission/simulate_phaseiii.py --outdir atr-submission/results/phase_iii_reproduced
python atr-submission/evaluate_phaseiv.py --input atr-submission/results/predictions/multi_seed_results.csv --outdir atr-submission/results/phase_iv_ci
```

Run simulator tests:

```bash
cd atr-submission/finalization
python -m unittest discover -s tests -v
```

Compile Paper 2 from `atr-submission/finalization/paper/` with the ACM `acmart` class and BibTeX.

## Reproducibility status

The GitHub Actions workflow runs the simulator tests, reproduces Phase III data, checks the regenerated 24,000-row CSV against the committed source CSV, evaluates Phase IV, and compiles the Paper 2 finalization manuscript. A passing workflow verifies those automated steps; it does not establish real-world agent performance or replace a student clean-clone check.
