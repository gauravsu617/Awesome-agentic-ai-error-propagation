# FINAL ATR Archive Manifest

This manifest records the artifacts that were present in the supplied FINAL ATR package and the items currently mirrored in the AITR subdirectory of this repository. It prevents a partial GitHub update from being mistaken for a full archive upload.

## Currently mirrored in this repository

- aitr-submission/README.md — package scope and execution notes
- aitr-submission/evaluate_phaseiv.py — Phase IV CSV validation and summary/plot generation script
- aitr-submission/references.bib — bibliography source
- aitr-submission/Prompts_and_Search_Queries.txt — saved literature search queries
- aitr-submission/docs/REPRODUCIBILITY_AUDIT.md — execution, evidence, baseline, and reporting checklist
- aitr-submission/docs/CITATION_INTEGRITY_AUDIT.md — citation-checking checklist (not completed citation results)

The repository also already had paper/RESEARCH_paper.pdf before this update; do not assume it is byte-identical to any one PDF from the supplied archive.

## Present in the original FINAL ATR package but not mirrored here as separate files

### Manuscripts and literature review
- ACM_CSUR_Review_Paper_Final.pdf
- agentic_ai_error_propagation_research_paper.pdf
- Overleaf_Final_Paper.pdf
- Prism_Final_Paper.pdf
- LiteratureReview_TopicID_MCL2026003_SutariyaGauravKarsanbhai.pdf
- Elicit_Report_Error_Propagation.pdf
- Elicit - Error Propagation in Multi-Step AI-Agent Workflows.pdf
- Elicit_Semantic_Scholar_Evidence_Filled.pdf

### Protocol and prompt package PDFs
- AITR_Prompts_01_02_MCL2026003.pdf
- AITR Prompts 03-05 Literature-to-Experiment Package (MCL2026003).pdf
- AITR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf

### Notebooks and code
- ATR_PHASE_III_CODE.ipynb
- ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb
- ATR_PHASE_IV_completed_Prompts_12_14.ipynb
- main.tex
- main_acmart_overleaf.tex

### Citation and research-support data
- Part_A_Citation_Verification.xlsx
- Lab4_Literature_List_and_Tool_Tables.xlsx
- Part_B_Collection_Export.ris
- ResearchRabbit_Collection_Export.ris
- Part_B_Citation_Map_ResearchRabbit.png
- Part_B_Citation_Map_Litmaps.png
- Part_B_Reflection.pdf

### Figures and nested archives
- Figures/fig1_workflow.png
- Figures/fig2_propagation.png
- Figures/fig3_safeguards.png
- Figures/fig4_taxonomy.png
- Phase4.zip
- Phase5.zip
- Phase_VI_Complete_Package.zip
- agentic_error_propagation_results - Copy.zip

The original package also contained a README, .gitignore, and a short submission-scope note. The package's binary files, notebooks, and LaTeX source files need a separate authenticated file upload or a local Git push to complete the full mirror.

## Integrity note

The existence of a paper draft, notebook, results archive, spreadsheet, or figure does not by itself prove that an experiment ran successfully or a citation was fully verified. Report results only after inspecting the supporting files and checking their provenance. Do not commit restricted data or third-party PDFs unless redistribution is permitted.
