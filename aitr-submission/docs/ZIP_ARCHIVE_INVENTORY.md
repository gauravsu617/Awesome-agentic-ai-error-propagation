# Uploaded ZIP Inventory and Repository Reconciliation

**Archive inspected:** `FINAL ATR(1).zip`  
**Purpose:** Record the source artifacts available for completing the repository without claiming unverified work as complete.

## Major artifacts in the ZIP

| Category | Supplied artifacts | Notes |
|---|---|---|
| Manuscript sources | `main.tex`, `main_acmart_overleaf.tex`, nested Phase V `paper/main.tex` | Multiple versions; compare before choosing canonical source. |
| Rendered papers | `ACM_CSUR_Review_Paper_Final.pdf`, `agentic_ai_error_propagation_research_paper.pdf`, `Overleaf_Final_Paper.pdf`, `Prism_Final_Paper.pdf` | Do not assume they are the same revision. |
| Bibliography | `references.bib` | Validate entries and manuscript citation keys. |
| Phase III notebooks | `ATR_PHASE_III_CODE.ipynb`, `ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb` | Run-all verification remains necessary. |
| Phase IV | `Phase4.zip`, `evaluate_phaseiv.py`, `ATR_PHASE_IV_completed_Prompts_12_14.ipynb` | Phase4.zip includes a report and evaluator copy. |
| Phase V | `Phase5.zip` | Includes manuscript draft, peer review, revision log, and evidence checklist. |
| Phase VI | `Phase_VI_Complete_Package.zip` | Includes AI-use/integrity report, checklist, and activity-log template. |
| Results | `agentic_error_propagation_results - Copy.zip` | Contains trial-level CSVs, summary CSVs, figures, and environment/validation logs. |
| Citation assignment | `Part_A_Citation_Verification.xlsx`, citation-map images, `Part_B_Reflection.pdf`, RIS exports | These are distinct literature-mapping deliverables. |
| Literature/tool records | `Lab4_Literature_List_and_Tool_Tables.xlsx`, Elicit/Semantic Scholar PDFs, literature review PDF | Check privacy, metadata, and assignment relevance before publishing. |
| Figures | `Figures/fig1_workflow.png` through `fig4_taxonomy.png` | Confirm that captions and manuscript references match the selected paper version. |

## Repository mapping guidance
- Phase reports, checklists, and integrity documents belong under `aitr-submission/docs/`.
- Notebooks, evaluator scripts, raw results, and generated figures should be kept in clearly named subdirectories with provenance and run instructions.
- Canonical manuscript source and its bibliography should live together under `paper/`.
- Citation assignment artifacts should be kept separate from the paper's research bibliography to avoid confusing coursework deliverables with manuscript references.
- Avoid duplicate filenames for distinct versions; retain version/source labels when their relationship is not resolved.

## Publishing caution
The uploaded archive contains a mixture of draft papers, assignment deliverables, source code, outputs, and nested archives. Do not upload every PDF or spreadsheet blindly to a public repository. Review author names, student IDs, email addresses, institutional restrictions, dataset licensing, and whether the files are intended for public release.

## Status
This inventory is based on the uploaded archive listing. It does not certify the files' scientific correctness, execution status, or publication readiness.
