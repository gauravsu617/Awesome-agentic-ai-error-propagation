# GitHub Implementations and Local Research Code

This page distinguishes five maintained external reference implementations from the student's experiment code bundled in FINAL ATR. The source archive files have not all been uploaded to this repository as binaries; the archive manifest lists files that still need syncing.

## A. Five curated external implementations

### 1. AgentBench
Official implementation of the multi-environment LLM-agent benchmark.
- GitHub: https://github.com/THUDM/AgentBench
- Paper: https://arxiv.org/abs/2308.03688

### 2. Mind2Web
Official dataset and implementation resources for generalist web agents.
- GitHub: https://github.com/OSU-NLP-Group/Mind2Web
- Paper: https://arxiv.org/abs/2306.06070

### 3. Self-RAG
Retrieval, generation, and self-reflection approach.
- GitHub: https://github.com/AkariAsai/self-rag
- Paper: https://arxiv.org/abs/2310.11511

### 4. WebShop
Interactive environment for grounded language-agent evaluation.
- GitHub: https://github.com/princeton-nlp/WebShop
- Paper: https://arxiv.org/abs/2207.01206

### 5. AgentDojo
Evaluation environment for prompt-injection attacks and defenses in tool-using LLM agents.
- GitHub: https://github.com/ethz-spylab/agentdojo
- Paper: https://arxiv.org/abs/2406.13352

## B. Student implementation artifacts in the supplied FINAL ATR ZIP

| Artifact in ZIP | Purpose / notes | Current repository mirror status |
|---|---|---|
| `ATR_PHASE_III_CODE.ipynb` | Phase III implementation notebook (248,304 bytes in source ZIP) | Not yet mirrored as a separate file |
| `ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb` | Completed Phase III notebook (242,410 bytes) | Not yet mirrored as a separate file |
| `ATR_PHASE_IV_completed_Prompts_12_14.ipynb` | Phase IV evaluation notebook | Mirrored as `aitr-submission/ATR_PHASE_IV_completed_Prompts_12_14.ipynb` |
| `evaluate_phaseiv.py` | CSV validation, summaries, comparison table, and plots | Mirrored as `aitr-submission/evaluate_phaseiv.py` |
| `agentic_error_propagation_results - Copy.zip` | Raw simulation CSVs, summary CSVs, figures, and validation/environment logs | Selected summary tables and report are mirrored below; full archive is not yet mirrored |
| `Phase4.zip` | Phase IV report, DOCX, evaluator, notebook | Not mirrored as binary archive |
| `Phase5.zip` | Peer-review/revision package and manuscript source | Not mirrored as binary archive |
| `Phase_VI_Complete_Package.zip` | AI-use and research-integrity report, activity log, checklist | Not mirrored as binary archive |

## C. Results included in the latest source ZIP

The results ZIP reports 400 rows in baseline results, 800 in propagation results, and 24,000 in multi-seed results. The summary table below comes from its `predictions/final_comparison.csv`:

| Base error rate | Mean errors: independent | Mean errors: propagation | Delta (propagation − independent) | Failure rate: independent | Failure rate: propagation |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 0.1 | 0.3847 | 0.4917 | 0.1070 | 0.3360 | 0.3360 |
| 0.2 | 0.7887 | 0.9953 | 0.2067 | 0.5787 | 0.5787 |
| 0.3 | 1.1790 | 1.5100 | 0.3310 | 0.7447 | 0.7447 |

At the three non-zero base error rates, the propagation condition has higher reported mean stage errors; the provided binary workflow-failure rate is unchanged. The metric definitions and analysis script must be checked before generalizing. This simulation is separate from the protocol's planned HotpotQA experiment and does not demonstrate real-agent recovery performance.

Summary files copied from the supplied archive:
- [Final comparison CSV](results/final_comparison.csv)
- [Multi-seed summary CSV](results/multi_seed_summary.csv)
- [Input/row validation report](results/validation_report.json)
- [Environment verification log](results/environment_verification.json)
- [GPU verification log](results/gpu_verification.json)

## D. Running the evaluator

From this repository root:

```bash
python -m pip install pandas numpy matplotlib
python aitr-submission/evaluate_phaseiv.py \
  --input path/to/multi_seed_results.csv \
  --outdir results/phase_iv
```

The evaluator expects `error_rate`, `model`, `stage_errors`, and `workflow_failed`. Use the actual CSV from the ZIP or reproduce it from source code; the summary alone is not a substitute for raw data.

## E. Reproducibility guardrails

- Record Python/package versions, code commit, exact input files, model IDs, prompts, and seeds.
- Keep raw inputs/logs separate from computed summaries and figures.
- Inspect data-generating code to establish whether the simulation matches the intended research question.
- Treat `PASS` values in supplied JSON as source-archive logs until independently reproduced.
- See [reproducibility audit](../aitr-submission/docs/REPRODUCIBILITY_AUDIT.md) and [archive manifest](../aitr-submission/ARCHIVE_MANIFEST.md).
