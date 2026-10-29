# Finish syncing the complete FINAL ATR package

The GitHub AITR directory currently contains selected source-and-audit files. The prepared archive includes additional PDFs, spreadsheets, figures, RIS exports, notebooks, LaTeX sources, and nested phase ZIPs that were not all transferred through the current file-writing path.

To mirror the full archive without overwriting the repository's existing curated README or current audit files, place the archive contents in a separate folder named aitr-submission/original-archive.

## Ubuntu / Linux

1. Download the prepared FINAL ATR GitHub-ready ZIP from the conversation and note its local path.
2. Clone the repository:
   
   ```bash
   git clone https://github.com/gauravsu617/Awesome-agentic-ai-error-propagation.git
   cd Awesome-agentic-ai-error-propagation
   ```

3. Extract the ZIP to a temporary directory. Replace /path/to/final-atr-research-github-ready.zip with the ZIP's actual path:
   
   ```bash
   mkdir -p /tmp/final-atr-upload
   unzip /path/to/final-atr-research-github-ready.zip -d /tmp/final-atr-upload
   mkdir -p aitr-submission/original-archive
   rsync -av --exclude='.git' "/tmp/final-atr-upload/FINAL ATR/" aitr-submission/original-archive/
   ```

4. Review the staged files and confirm redistribution rights before pushing:
   
   ```bash
   git status --short
   git add aitr-submission/original-archive
   git diff --cached --stat
   git commit -m "Add remaining FINAL ATR archive artifacts"
   git push origin main
   ```

Do not force-push. If the remote branch advances before your push, fetch and reconcile the history first.

## Before making the repository public

Check the paper PDFs, screenshots, nested archives, and any datasets for redistribution permissions. Do not commit credentials, private records, or restricted datasets. Keep the reproduction audit status as UNKNOWN / TEST REQUIRED until the experiments have actually run on the documented inputs and the outputs have been inspected.
