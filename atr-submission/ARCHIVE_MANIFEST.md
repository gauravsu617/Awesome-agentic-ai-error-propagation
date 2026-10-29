# FINAL ATR Archive Manifest — Updated 30 October 2026

This manifest distinguishes (1) files mirrored into the repository, (2) summaries derived from the supplied ZIP, and (3) files still awaiting binary/local Git upload. Presence in the source archive is not proof that an experiment has been independently reproduced.

## Updated files already present in GitHub

### Citation
- `citation/Citation_Verification_Audit.md` — 22 original review references, seven newer candidates, recorded citation statuses, DOI/source links, and manuscript corrections from `Part_A_Citation_Verification.xlsx`.
- `atr-submission/docs/CITATION_INTEGRITY_AUDIT.md` — audit process checklist.
- The old `citation/Citation_Verification_Part_A.xlsx` repository object was a one-byte placeholder, not a valid workbook, and has been removed. The original workbook from the ZIP is not yet mirrored as a binary file.

### Dataset
- `datasets/datasets.md` — HotpotQA distractor validation protocol settings, fault states and C1–C4 checks; source-archive synthetic results; distinction between the planned QA verifier experiment and the simulation; three related benchmark links.

### Implementation and results
- `implementations/github-repositories.md` — preserves the five curated external implementations and adds the source archive's student code/results inventory.
- `implementations/results/final_comparison.csv`
- `implementations/results/multi_seed_summary.csv`
- `implementations/results/validation_report.json`
- `implementations/results/environment_verification.json`
- `implementations/results/gpu_verification.json`
- `implementations/results/README.md`
- `atr-submission/evaluate_phaseiv.py`
- `atr-submission/ATR_PHASE_IV_completed_Prompts_12_14.ipynb`

The full raw CSVs, experiment figures, and environment/validation logs are now mirrored under `atr-submission/results/`. The saved `validation_report.json` is an archive artifact; its PASS label alone does not prove independent reproduction.

### Paper
- `paper/README.md` — inventories the ZIP's manuscript candidates and distinguishes the ACM CSUR survey version from the other manuscript drafts.
- `atr-submission/paper/main.tex` — Phase V IEEE-style draft source mirrored from the nested Phase5 package; provisional numerical results and author placeholders remain.
- `atr-submission/paper/references.bib` — intentionally incomplete placeholder from the Phase V package, not a submission-ready bibliography.
- `atr-submission/paper/README.md` — manuscript verification and build instructions.
- Existing `paper/RESEARCH_paper.pdf` was in the repo before this update and has **not** been replaced by a newer ZIP PDF; a local binary Git push is still required.

### References
- `references/references.md` — original 20-paper curated list retained, with the AITR reference audit appendix.
- `references/references.bib` — corrected bibliography in the references category.
- `atr-submission/references.bib` — matching bibliography source for the AITR materials.

### Tools
- `tools/tools.md` — five engineering frameworks retained and four literature-discovery tools added with ratings and observations copied from the workbook.

### Submission notes
- `atr-submission/README.md`
- `atr-submission/ARCHIVE_MANIFEST.md`
- `atr-submission/docs/REPRODUCIBILITY_AUDIT.md`
- `atr-submission/docs/LOCAL_SYNC_AND_UPLOAD.md`

## Source ZIP files still awaiting binary/local Git upload

### Manuscripts and literature-review evidence
- `ACM_CSUR_Review_Paper_Final.pdf`
- `agentic_ai_error_propagation_research_paper.pdf`
- `Overleaf_Final_Paper.pdf`
- `Prism_Final_Paper.pdf` (same SHA-256 as the Overleaf PDF)
- `LiteratureReview_TopicID_MCL2026003_SutariyaGauravKarsanbhai.pdf`
- `Elicit_Report_Error_Propagation.pdf`
- `Elicit - Error Propagation in Multi-Step AI-Agent Workflows.pdf`
- `Elicit_Semantic_Scholar_Evidence_Filled.pdf`
- `Part_B_Reflection.pdf`

### Protocol and prompt PDFs
- `AITR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf`
- `AITR_Prompts_01_02_MCL2026003.pdf`
- `AITR Prompts 03-05 Literature-to-Experiment Package (MCL2026003).pdf`

### Code, raw data, and phase deliverables
- `ATR_PHASE_III_CODE.ipynb` — mirrored at `atr-submission/notebooks/ATR_PHASE_III_CODE.ipynb`.
- `ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb` — mirrored at `atr-submission/notebooks/ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb`.
- `main.tex`, `main_acmart_overleaf.tex`
- Full raw CSVs in `agentic_error_propagation_results - Copy.zip` (400-row baseline, 800-row propagation, 24,000-row multi-seed results) and its figures/logs — now mirrored at `atr-submission/results/`.
- `Phase4.zip`, `Phase5.zip`, `Phase_VI_Complete_Package.zip`

### Workbooks, exports, and figures
- `Part_A_Citation_Verification.xlsx`
- `Lab4_Literature_List_and_Tool_Tables.xlsx`
- `Part_B_Collection_Export.ris`, `ResearchRabbit_Collection_Export.ris`
- `Part_B_Citation_Map_ResearchRabbit.png`, `Part_B_Citation_Map_Litmaps.png`
- `Figures/fig1_workflow.png` through `Figures/fig4_taxonomy.png` — mirrored at `atr-submission/figures/`.

The original FINAL ATR ZIP remains the source for additional manuscripts, PDFs, spreadsheets, RIS exports, citation-map images, and nested phase ZIP files that are still not mirrored. The Phase III notebooks, four project figures, full raw CSVs, result figures, and logs are now uploaded. The [experimental data audit](docs/EXPERIMENT_DATA_AUDIT.md) records the checks completed and the remaining reproduction steps.

## Integrity and license note

Before public upload, confirm permission to redistribute manuscripts, screenshots, figures, datasets, and nested archives. No license file has been added because rights have not been fully audited. Keep experimental claims bounded by the source data, metric definitions, and actual reproduction status.

