# FINAL ATR Archive Manifest — Updated 29 October 2026

This manifest distinguishes (1) files mirrored into the repository, (2) summaries derived from the supplied ZIP, and (3) files still awaiting binary/local Git upload. A file appearing in the source archive is not evidence that its experiment was independently reproduced.

## Updated repository files now available

### Citation
- `citation/Citation_Verification_Audit.md` — renders the status table, 22 existing review references, seven newer candidates, DOI/source links, and manuscript fixes from `Part_A_Citation_Verification.xlsx`.
- `aitr-submission/docs/CITATION_INTEGRITY_AUDIT.md` — general audit checklist.
- Note: the previous repository's `citation/Citation_Verification_Part_A.xlsx` was a one-byte placeholder, not a valid workbook, and has been removed. The actual workbook in the source ZIP is not yet uploaded as a binary file.

### Dataset
- `datasets/datasets.md` — adds the HotpotQA distractor validation protocol (planned verifier experiment), details fault states C1–C4, reports source-archive simulation summaries, and separates those two experimental designs.
- It preserves AgentBench, Mind2Web, and ToolBench as external reference benchmarks.

### Implementations and results
- `implementations/github-repositories.md` — keeps the five curated external implementations and adds the source archive's student notebooks/code and results status.
- `implementations/results/final_comparison.csv`
- `implementations/results/multi_seed_summary.csv`
- `implementations/results/validation_report.json`
- `implementations/results/environment_verification.json`
- `implementations/results/gpu_verification.json`
- `implementations/results/README.md`
- `aitr-submission/evaluate_phaseiv.py` and `aitr-submission/ATR_PHASE_IV_completed_Prompts_12_14.ipynb` — copied evaluation script and Phase IV notebook.

### Paper
- `paper/README.md` — inventories the newer manuscript candidates in the ZIP, including page counts and the fact that Overleaf/Prism PDFs are byte-identical.
- `paper/RESEARCH_paper.pdf` was already in the repository before this update and has **not** been replaced by a newer ZIP PDF. Binary PDF replacement requires local Git upload; see `aitr-submission/docs/LOCAL_SYNC_AND_UPLOAD.md`.

### References
- `references/references.md` — extends the curated references with the latest citation-audit findings and seven new candidate records.
- `aitr-submission/references.bib` — bibliography source copied into the repository.

### Tools
- `tools/tools.md` — preserves five engineering frameworks and adds the workbook's ratings/observations for ResearchRabbit, Litmaps, Semantic Scholar, and Elicit.

## Present in the source FINAL ATR ZIP, still not mirrored as individual binary/source files

### Manuscripts and literature review
- `ACM_CSUR_Review_Paper_Final.pdf`
- `agentic_ai_error_propagation_research_paper.pdf`
- `Overleaf_Final_Paper.pdf`
- `Prism_Final_Paper.pdf` (same SHA-256 as Overleaf PDF)
- `LiteratureReview_TopicID_MCL2026003_SutariyaGauravKarsanbhai.pdf`
- `Elicit_Report_Error_Propagation.pdf`
- `Elicit - Error Propagation in Multi-Step AI-Agent Workflows.pdf`
- `Elicit_Semantic_Scholar_Evidence_Filled.pdf`
- `Part_B_Reflection.pdf`

### Dataset/protocol and prompts
- `AITR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf`
- `AITR_Prompts_01_02_MCL2026003.pdf`
- `AITR Prompts 03-05 Literature-to-Experiment Package (MCL2026003).pdf`

### Code and data
- `ATR_PHASE_III_CODE.ipynb`
- `ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb`
- `main.tex`
- `main_acmart_overleaf.tex`
- Full raw `predictions/baseline_results.csv`, `predictions/propagation_results.csv`, and `predictions/multi_seed_results.csv` from `agentic_error_propagation_results - Copy.zip`.

### Citation and tool evidence
- `Part_A_Citation_Verification.xlsx`
- `Lab4_Literature_List_and_Tool_Tables.xlsx`
- `Part_B_Collection_Export.ris`
- `ResearchRabbit_Collection_Export.ris`
- `Part_B_Citation_Map_ResearchRabbit.png`
- `Part_B_Citation_Map_Litmaps.png`

### Figures and nested archives
- `Figures/fig1_workflow.png` through `Figures/fig4_taxonomy.png`
- `Phase4.zip`, `Phase5.zip`, `Phase_VI_Complete_Package.zip`
- `agentic_error_propagation_results - Copy.zip`

The compact summary CSVs and selected JSON logs listed above are transcribed from the archive. They are not the full raw run data and the logs have not been independently regenerated during this update.

## Integrity and license note

Before public upload, confirm permission to redistribute all papers, screenshots, figures, datasets, and nested archives. No license file has been added because third-party materials and rights have not been fully audited. Keep experimental claims bounded by the data source, metric definitions, and actual reproduction status.
