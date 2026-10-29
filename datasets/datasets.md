# Datasets and Experiment Protocols

This page is updated from the supplied FINAL ATR ZIP (especially `ATR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf` and `agentic_error_propagation_results - Copy.zip`). It separates the planned HotpotQA verifier experiment from the separate synthetic error-propagation simulation in the results archive. They must not be described as the same experiment.

## A. Primary dataset named by the frozen-protocol document: HotpotQA

**Planned configuration:** HotpotQA, distractor setting, validation/development split.

**Research question in the protocol:** In a ReAct-style agent, how often does a corrupted first observation reach the final answer, and does a separate verifier with clean-source access recover more answers than same-model self-critique?

**Task:** multi-hop question answering over Wikipedia paragraphs. The protocol explicitly describes this as a controlled stand-in for a “read source, extract, answer” chain—not a literature-review pipeline. Conclusions should not be generalized directly to automated literature reviews.

- Project page: https://hotpotqa.github.io/
- Official repository named in protocol: https://github.com/hotpotqa/hotpot
- Hugging Face dataset ID named in protocol: https://huggingface.co/datasets/hotpotqa/hotpot_qa
- Expected source file: `hotpot_dev_distractor_v1.json`
- Reported fields: question, answer, type, level, supporting facts, and context paragraphs.
- The protocol reports 90,447 training and 7,405 validation examples for the Hugging Face distractor configuration and describes a CC BY-SA 4.0 dataset license. Confirm those details at the official dataset card before redistribution; the protocol itself labels online findings as not yet independently confirmed.

### Frozen design settings

| Design component | Protocol setting |
|---|---|
| Pilot | 20 questions |
| Frozen test | 60 disjoint questions; IDs intended to be generated once with sampling seed 42 |
| Few-shot examples | Proposed six examples from train only; IDs to be recorded |
| Main agent | ReAct-style loop over the question's ten paragraphs; Search/Lookup/Finish actions; maximum seven steps |
| Fault-free condition | Clean retrieval |
| F1 fault | First lookup returns a plausible paragraph from a different question's context (wrong entity) |
| F2 fault | First lookup's true gold paragraph has one number/year changed; ineligible questions are excluded from F2 |
| Fault timing | First lookup only; later lookup of the same title returns clean text |
| C1 | No check |
| C2 | Same-model self-critique |
| C3 | Same-model critique plus clean gold source |
| C4 | Separate verifier plus clean gold source |
| Retry policy | One retry with critique appended, same rule across conditions |
| Primary metric | Recovery Rate, comparing C4 vs C2 pooled over F1/F2 |
| Other metrics | EM, F1, propagation rate, false-alarm rate, clean-state EM change, undetected-error rate, calls/tokens |
| Statistical plan | Paired McNemar test; paired bootstrap intervals with 10,000 resamples; Holm correction for confirmatory tests |

### Status must be treated cautiously

The supplied protocol's pre-experiment checklist still has open items, including final model IDs, prompt files/hashes, few-shot IDs, fault-injector tests, and test split IDs. The source therefore documents a planned/frozen design but does not by itself prove that the 60-question HotpotQA experiment was completed.

## B. Separate data in the supplied results archive: synthetic error-propagation simulation

The ZIP contains `predictions/baseline_results.csv` (400 rows), `predictions/propagation_results.csv` (800 rows), and `predictions/multi_seed_results.csv` (24,000 rows), along with two summary CSVs, figures, and environment-validation logs. These records use base per-stage `error_rate` values of 0.0, 0.1, 0.2, and 0.3 and compare `independent` with `propagation` conditions. They are not HotpotQA question/answer records.

### Recorded summary in `predictions/final_comparison.csv`

| Base error rate | Independent mean stage errors | Propagation mean stage errors | Difference | Independent failure rate | Propagation failure rate |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 0.1 | 0.3847 | 0.4917 | 0.1070 | 0.3360 | 0.3360 |
| 0.2 | 0.7887 | 0.9953 | 0.2067 | 0.5787 | 0.5787 |
| 0.3 | 1.1790 | 1.5100 | 0.3310 | 0.7447 | 0.7447 |

In the provided summary, propagation has a higher mean stage-error count at non-zero base error rates, while failure rates are identical between the two conditions. Because the output definition treats a workflow with any stage error as failed, stage-error accumulation and binary failure are different outcomes. This is a descriptive pattern from the provided CSV, not proof of statistical significance or real-LLM behavior.

The archive's validation report says the CSVs had no missing values or duplicate rows and reported status PASS. Those logs are packaged artifacts and have not been independently regenerated in this repository update.

## C. Related benchmarks retained in this repository (not the current protocol's primary dataset)

### 1. AgentBench
Multi-environment benchmark for evaluating LLM agents. Useful background/reference for interactive task evaluation.
- Repository: https://github.com/THUDM/AgentBench
- Paper: https://arxiv.org/abs/2308.03688

### 2. Mind2Web
Web-agent dataset/benchmark with human-demonstrated interaction trajectories.
- Repository: https://github.com/OSU-NLP-Group/Mind2Web
- Paper: https://arxiv.org/abs/2306.06070

### 3. ToolBench
Tool-use/API dataset and benchmark.
- Repository: https://github.com/OpenBMB/ToolBench
- Paper: https://arxiv.org/abs/2307.16789

These three resources are curated reference benchmarks. They are not evidence that the project's planned HotpotQA verifier experiment has been run.

## Reproduction and data handling

- Record the downloaded dataset revision, official license/access terms, and exact split IDs.
- Keep pilot IDs disjoint from frozen test IDs, and keep supporting facts out of the writer's input.
- Preserve raw trajectories, fault-injection logs, verifier verdicts, model IDs, timestamps, prompts, seeds, token counts, and scorer outputs.
- Do not redistribute dataset material or derived files until the official license and applicable share-alike terms have been checked.
- See [the reproducibility audit](../aitr-submission/docs/REPRODUCIBILITY_AUDIT.md).
