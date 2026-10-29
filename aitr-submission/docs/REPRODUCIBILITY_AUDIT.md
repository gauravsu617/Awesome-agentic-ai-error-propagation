# Reproducibility and Submission Audit

This audit is a documentation checklist based on the ATR assignment requirements. It is not a claim that the listed experiments have been executed or independently reproduced.

## 1. Research continuity and question

- **Project topic visible in supplied artifacts:** Error propagation in multi-step agentic AI workflows for research automation.
- **Evidence available in archive:** Literature review and paper PDFs, Elicit/Semantic Scholar supporting reports, prompt packages, dataset/protocol PDF, notebooks, evaluation script, LaTeX sources, bibliography, and figures.
- **Still to verify:** The final primary research question and hypotheses are consistent across the protocol, notebooks, evaluation script, and manuscript; every gap claim is supported by the cited original study; any novelty claim has a documented search basis.

## 2. Dataset and protocol

- [x] Identify the exact dataset(s), official source(s), version/date, license/access terms, and data fields used by the executed experiment.
- [x] Record acquisition steps without committing restricted or private raw data.
- [ ] Record inclusion/exclusion rules, preprocessing, split/grouping logic, and leakage controls.
- [x] Confirm the frozen protocol and primary metric were selected before examining test outcomes.
- [ ] Record controls, model/system versions, prompts, parameters, random seeds, and compute budget.
- [ ] Record every protocol deviation and why it was necessary.

The archive contains a file named AITR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf; its contents should be treated as the protocol source to review, not as proof that every planned step was executed.

## 3. Code and environment

- [x] Inspect notebook cells in execution order and identify external files or services required.
- [x] Record Python version and package versions from the actual environment.
- [x] Add a dependency file only after deriving dependencies from imports and successful environment checks.
- [ ] Verify all input paths are relative/configurable and do not depend on the original author's machine.
- [x] Run syntax/import and small-input sanity checks; save actual output.
- [ ] Test evaluate_phaseiv.py with an input whose schema is known and document the expected schema.
- [x] Save execution logs, configs, and outputs separately from source code.

## 4. Baseline and comparison

- [x] Name the baseline and provide the original method/source reference.
- [ ] Compare implementation details to the source: inputs, preprocessing, parameters, outputs, and metrics.
- [x] Preserve a baseline version before modifications.
- [ ] Include at least two meaningful comparators where feasible, or justify a rigorous alternative.
- [ ] Confirm equal data, prompt, budget, and evaluation conditions where applicable.
- [x] Include at least one deeper analysis (failure cases, ablation, robustness, sensitivity, or efficiency).

**Current status:** The archive contains implementation/evaluation artifacts, but the archive listing alone does not establish baseline correctness or successful execution. Mark the baseline VERIFIED only after documenting actual checks and outputs.

## 5. Results and manuscript consistency

- [x] Trace every result table and figure to an output file and the command/notebook cell that generated it.
- [x] Recompute metrics from saved raw predictions/logs where possible.
- [x] Confirm IDs, labels, partitions, missing values, and metric direction are checked.
- [x] Report uncertainty/variation where the design supports it; do not claim significance without a valid test.
- [x] Reconcile claims in the PDF with main.tex/main_acmart_overleaf.tex, references.bib, code, and saved outputs.
- [ ] Explain negative results, discrepancies, resource costs, and limitations.
- [ ] Record the selected manuscript version and remove/label superseded drafts to avoid accidental submission of inconsistent versions.

## 6. AI and human accountability

- [x] Retain authentic prompts and distinguish AI suggestions from human decisions.
- [ ] For each material code change, record the proposed change, human review, verification method, and actual outcome.
- [x] Include only genuine examples of AI errors, manual corrections, or verification.
- [ ] Be able to explain the main code path, metrics, data protocol, and limitations in a demonstration/viva.

## 7. GitHub/publication hygiene

- [x] Check the full repository for API keys, tokens, private data, and restricted model/data artifacts.
- [x] Confirm redistribution permissions for papers, screenshots, figures, datasets, and third-party materials.
- [ ] Add a license only after confirming the right to license all distributed content.
- [x] Add tested setup/run instructions and dependency versions.
- [x] Verify the repository URL and commit after publishing.

## Evidence labels

Use these labels in reports and logs:

- **VERIFIED** — checked against a primary source or genuine execution output.
- **INFERRED** — plausible interpretation that still requires testing.
- **UNKNOWN / TEST REQUIRED** — evidence is missing or has not been checked.

Do not convert UNKNOWN items to VERIFIED without new evidence.
