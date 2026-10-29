# Sync all remaining FINAL ATR files into their repository categories

The repository now contains updated category documentation, citation-audit findings, and compact result summaries. Some original binaries and raw source files still need a local Git push because the file-writing route used for this update accepts UTF-8 text, not raw PDF/image/XLSX bytes.

## 1. Download and unpack

Download the GitHub-ready ZIP from the conversation, then in Ubuntu/Linux:

```bash
git clone https://github.com/gauravsu617/Awesome-agentic-ai-error-propagation.git
cd Awesome-agentic-ai-error-propagation
mkdir -p /tmp/final-atr-new
unzip /path/to/final-atr-research-github-ready.zip -d /tmp/final-atr-new
SRC="/tmp/final-atr-new/FINAL ATR"
```

Replace `/path/to/final-atr-research-github-ready.zip` with the actual downloaded ZIP path.

## 2. Copy current archive assets into category subfolders

This preserves the repository's curated markdown while making the complete package easy to trace:

```bash
mkdir -p citation/source-workbooks citation/source-maps
mkdir -p datasets/source-protocols
mkdir -p implementations/source-notebooks implementations/source-results
mkdir -p paper/archive-candidates paper/latex-source
mkdir -p references/source-exports tools/source-workbooks

cp "$SRC/Part_A_Citation_Verification.xlsx" citation/source-workbooks/
cp "$SRC/Lab4_Literature_List_and_Tool_Tables.xlsx" tools/source-workbooks/
cp "$SRC/Part_B_Collection_Export.ris" "$SRC/ResearchRabbit_Collection_Export.ris" references/source-exports/
cp "$SRC/Part_B_Citation_Map_ResearchRabbit.png" "$SRC/Part_B_Citation_Map_Litmaps.png" citation/source-maps/
cp "$SRC/AITR_Phase_II_Dataset_Sheet_and_Frozen_Protocol_MCL2026003.pdf" datasets/source-protocols/
cp "$SRC/ATR_PHASE_III_CODE.ipynb" "$SRC/ATR_PHASE_III_CODE_completed_Prompts_10_11.ipynb" implementations/source-notebooks/
cp "$SRC/agentic_error_propagation_results - Copy.zip" implementations/source-results/
cp "$SRC/ACM_CSUR_Review_Paper_Final.pdf" "$SRC/agentic_ai_error_propagation_research_paper.pdf" "$SRC/Overleaf_Final_Paper.pdf" "$SRC/Prism_Final_Paper.pdf" paper/archive-candidates/
cp "$SRC/main.tex" "$SRC/main_acmart_overleaf.tex" paper/latex-source/
cp "$SRC/references.bib" references/
```

Add the remaining relevant review PDFs, Elicit reports, prompt-pack PDFs, figure images, and phase archives into subfolders as listed in [ARCHIVE_MANIFEST.md](../ARCHIVE_MANIFEST.md). Review redistribution rights before adding third-party content.

## 3. Validate before committing

```bash
sha256sum "$SRC/Overleaf_Final_Paper.pdf" "$SRC/Prism_Final_Paper.pdf"
unzip -t "$SRC/agentic_error_propagation_results - Copy.zip"
git status --short
git diff --stat
```

Confirm the citation XLSX opens as a workbook and do not overwrite the derived `citation/Citation_Verification_Audit.md` page with an invalid file. The source protocol's HotpotQA experiment and the supplied simulation results are different designs; do not merge their outcomes.

## 4. Commit and push

```bash
git add citation/source-workbooks citation/source-maps datasets/source-protocols \
  implementations/source-notebooks implementations/source-results \
  paper/archive-candidates paper/latex-source references/source-exports references/references.bib \
  tools/source-workbooks

git commit -m "Add FINAL ATR source artifacts to research categories"
git push origin main
```

Do not force-push. If the remote has advanced, fetch and reconcile before pushing.
