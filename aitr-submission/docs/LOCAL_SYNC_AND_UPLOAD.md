# Sync all remaining FINAL ATR files into their repository categories

The repository now contains updated category documentation, the citation status summary, corrected BibTeX, and compact result/log summaries. The remaining PDFs, images, XLSX workbooks, Phase III notebook files, and raw CSVs need a local Git push because the connected GitHub file-writing route used for this update accepts UTF-8 text but not raw binary file bytes.

## 1. Download, clone, and unpack

Download the GitHub-ready ZIP from the conversation. In Ubuntu/Linux:

```bash
git clone https://github.com/gauravsu617/Awesome-agentic-ai-error-propagation.git
cd Awesome-agentic-ai-error-propagation
mkdir -p /tmp/final-atr-new
unzip /path/to/final-atr-research-github-ready.zip -d /tmp/final-atr-new
SRC="/tmp/final-atr-new/FINAL ATR"
```

Replace the ZIP path with its actual location. Ensure the extracted source directory is `FINAL ATR`.

## 2. Sync the source artifacts into category folders

These commands retain the curated Markdown indexes and place originals in clearly named subdirectories.

```bash
mkdir -p citation/source-workbooks citation/source-maps
mkdir -p datasets/source-protocols datasets/source-prompt-packs
mkdir -p implementations/source-notebooks implementations/source-results
mkdir -p implementations/source-phase-packages
mkdir -p paper/archive-candidates paper/latex-source paper/archive-figures paper/revision-evidence
mkdir -p references/source-exports references/source-bibliography references/literature-evidence
mkdir -p tools/source-workbooks
mkdir -p aitr-submission/phase-vi

# Citation workbook and maps
cp "$SRC/Part_A_Citation_Verification.xlsx" citation/source-workbooks/
cp "$SRC/Part_B_Citation_Map_ResearchRabbit.png" "$SRC/Part_B_Citation_Map_Litmaps.png" citation/source-maps/

# Dataset protocol and prompt packs
cp "$SRC/AITR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf" datasets/source-protocols/
cp "$SRC/AITR_Prompts_01_02_MCL2026003.pdf" datasets/source-prompt-packs/
cp "$SRC/AITR Prompts 03-05 Literature-to-Experiment Package (MCL2026003).pdf" datasets/source-prompt-packs/

# Tool-rating workbook and experiment code
cp "$SRC/Lab4_Literature_List_and_Tool_Tables.xlsx" tools/source-workbooks/
cp "$SRC/ATR_PHASE_III_CODE.ipynb" "$SRC/ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb" implementations/source-notebooks/
cp "$SRC/ATR_PHASE_IV_completed_Prompts_12_14.ipynb" implementations/source-notebooks/
cp "$SRC/evaluate_phaseiv.py" implementations/source-notebooks/

# Expand the raw result ZIP so CSVs, figures and logs are individual repository files
mkdir -p implementations/source-results/agentic-error-propagation-results
unzip -oq "$SRC/agentic_error_propagation_results - Copy.zip" -d implementations/source-results/agentic-error-propagation-results/

# Phase deliverables (both archive and extracted material)
cp "$SRC/Phase4.zip" "$SRC/Phase5.zip" "$SRC/Phase_VI_Complete_Package.zip" implementations/source-phase-packages/
unzip -oq "$SRC/Phase4.zip" -d implementations/source-phase-packages/phase4/
unzip -oq "$SRC/Phase5.zip" -d implementations/source-phase-packages/phase5/
unzip -oq "$SRC/Phase_VI_Complete_Package.zip" -d aitr-submission/phase-vi/

# Manuscript candidates, source, and figures
cp "$SRC/ACM_CSUR_Review_Paper_Final.pdf" "$SRC/agentic_ai_error_propagation_research_paper.pdf" \
   "$SRC/Overleaf_Final_Paper.pdf" "$SRC/Prism_Final_Paper.pdf" \
   "$SRC/LiteratureReview_TopicID_MCL2026003_SutariyaGauravKarsanbhai.pdf" \
   paper/archive-candidates/
cp "$SRC/main.tex" "$SRC/main_acmart_overleaf.tex" paper/latex-source/
cp "$SRC"/Figures/*.png paper/archive-figures/
cp "$SRC/Part_B_Reflection.pdf" paper/revision-evidence/
cp "$SRC/Elicit_Report_Error_Propagation.pdf" "$SRC/Elicit - Error Propagation in Multi-Step AI-Agent Workflows.pdf" \
   "$SRC/Elicit_Semantic_Scholar_Evidence_Filled.pdf" references/literature-evidence/

# Bibliographic exports
cp "$SRC/Part_B_Collection_Export.ris" "$SRC/ResearchRabbit_Collection_Export.ris" references/source-exports/
cp "$SRC/references.bib" references/source-bibliography/references.bib
```

## 3. Validate the source files before committing

```bash
sha256sum "$SRC/Overleaf_Final_Paper.pdf" "$SRC/Prism_Final_Paper.pdf"
unzip -t "$SRC/agentic_error_propagation_results - Copy.zip"
python - <<'PY'
import json
from pathlib import Path
p = Path("implementations/source-results/agentic-error-propagation-results/predictions/multi_seed_results.csv")
assert p.exists(), f"Raw multi-seed CSV missing: {p}"
print("multi_seed_results.csv bytes:", p.stat().st_size)
PY
git status --short
git diff --stat
```

The original archive's validation JSON reports 24,000 rows in its multi-seed CSV, 800 propagation rows and 400 baseline rows. Treat those as reported checks until you independently inspect/re-run validation.

## 4. Commit and push

```bash
git add citation/source-workbooks citation/source-maps datasets/source-protocols datasets/source-prompt-packs \
  implementations/source-notebooks implementations/source-results implementations/source-phase-packages \
  paper/archive-candidates paper/latex-source paper/archive-figures paper/revision-evidence \
  references/source-exports references/source-bibliography references/literature-evidence references/references.bib tools/source-workbooks \
  aitr-submission/phase-vi

git commit -m "Add FINAL ATR source artifacts to research categories"
git push origin main
```

Do not force-push. If the remote advances, fetch and reconcile before pushing.

## 5. Important interpretation and license notes

- The HotpotQA verifier design in the Phase II PDF is a planned QA experiment; its freeze checklist still marks several items open.
- The provided result CSVs describe a separate synthetic `independent` versus `propagation` simulation. Do not present them as HotpotQA verifier results or real-LLM recovery rates.
- Verify rights before committing PDFs, screenshots, datasets, or nested archives. Do not add secrets or private data.


## Replace the paper PDF only

The user-uploaded `research paper.pdf` is byte-identical to `FINAL ATR/agentic_ai_error_propagation_research_paper.pdf` (470,387 bytes; SHA-256 `a4b8bc4d27355c43bb619ac0c15cfeba247de91171199083322060e7f917ef96`). It is a 13-page draft, not the distinct 14-page Overleaf/Prism version.

Download `research-paper-replacement.zip` from this conversation and extract it into your local clone root so it overwrites `paper/RESEARCH_paper.pdf`. Then run:

```bash
chmod +x apply_research_paper_replacement.sh
./apply_research_paper_replacement.sh
```

The script checks the PDF SHA-256, updates the paper-status text in `README.md` and `paper/README.md`, commits those changes with the PDF replacement, and pushes to `origin main`. It does not force-push. Review `git status` first if you have unrelated local changes.
