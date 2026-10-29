#!/usr/bin/env bash
set -euo pipefail

EXPECTED_SHA='a4b8bc4d27355c43bb619ac0c15cfeba247de91171199083322060e7f917ef96'
EXPECTED_REMOTE='https://github.com/gauravsu617/Awesome-agentic-ai-error-propagation.git'
SOURCE_PDF="${1:-}"

if [[ -z "$SOURCE_PDF" || ! -f "$SOURCE_PDF" ]]; then
  echo "Usage: bash paper/replace_research_paper.sh /path/to/research-paper.pdf" >&2
  exit 2
fi
SOURCE_PDF="$(cd "$(dirname "$SOURCE_PDF")" && pwd)/$(basename "$SOURCE_PDF")"
REPO_DIR="$(git rev-parse --show-toplevel)"
REMOTE="$(git -C "$REPO_DIR" remote get-url origin)"
case "$REMOTE" in
  "$EXPECTED_REMOTE"|git@github.com:gauravsu617/Awesome-agentic-ai-error-propagation.git|https://github.com/gauravsu617/Awesome-agentic-ai-error-propagation)
    ;;
  *) echo "Error: origin does not match the target repository: $REMOTE" >&2; exit 3 ;;
esac
BRANCH="$(git -C "$REPO_DIR" branch --show-current)"
if [[ "$BRANCH" != "main" ]]; then
  echo "Error: run this from a clean main branch (current: $BRANCH)." >&2
  exit 3
fi
if [[ -n "$(git -C "$REPO_DIR" status --porcelain)" ]]; then
  echo "Error: working tree has uncommitted changes. Commit or stash them first." >&2
  exit 3
fi
git -C "$REPO_DIR" pull --ff-only origin main

ACTUAL_SHA="$(sha256sum "$SOURCE_PDF" | awk '{print $1}')"
if [[ "$ACTUAL_SHA" != "$EXPECTED_SHA" ]]; then
  echo "Error: PDF hash mismatch: $ACTUAL_SHA" >&2
  exit 4
fi
install -m 0644 "$SOURCE_PDF" "$REPO_DIR/paper/RESEARCH_paper.pdf"

cat > "$REPO_DIR/paper/README.md" <<'EOF'
# Research Paper — Canonical Version

## Selected manuscript

- **Title:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation
- **Author shown in PDF:** Sutariya Gaurav Karsanbhai
- **Pages:** 13
- **Size:** 470,387 bytes
- **SHA-256:** `a4b8bc4d27355c43bb619ac0c15cfeba247de91171199083322060e7f917ef96`

The canonical repository file is `paper/RESEARCH_paper.pdf`. Verify the SHA-256 after downloading or cloning the repository to confirm the exact file version.

## Related project documentation

- [Citation verification audit](../citation/Citation_Verification_Audit.md)
- [Dataset and experiment protocol](../datasets/datasets.md)
- [Implementation and result inventory](../implementations/github-repositories.md)
- [Bibliography](../references/references.md)
- [Reproducibility audit](../aitr-submission/docs/REPRODUCIBILITY_AUDIT.md)
EOF

python3 - "$REPO_DIR/README.md" <<'PY'
import sys
from pathlib import Path
p = Path(sys.argv[1])
s = p.read_text()
s = s.replace(
    "**Paper currently in repository:** [RESEARCH_paper.pdf](paper/RESEARCH_paper.pdf) (not replaced by the newer ZIP PDF in this text-file update).",
    "**Canonical research paper:** [RESEARCH_paper.pdf](paper/RESEARCH_paper.pdf) — 13-page version; SHA-256 `a4b8bc4d27355c43bb619ac0c15cfeba247de91171199083322060e7f917ef96`."
)
p.write_text(s)
PY

INSTALLED_SHA="$(sha256sum "$REPO_DIR/paper/RESEARCH_paper.pdf" | awk '{print $1}')"
if [[ "$INSTALLED_SHA" != "$EXPECTED_SHA" ]]; then
  echo "Error: installed file hash mismatch: $INSTALLED_SHA" >&2
  exit 5
fi

git -C "$REPO_DIR" add paper/RESEARCH_paper.pdf paper/README.md README.md
if git -C "$REPO_DIR" diff --cached --quiet; then
  echo "Repository already has the canonical paper; no commit needed."
  exit 0
fi
git -C "$REPO_DIR" diff --cached --stat
git -C "$REPO_DIR" commit -m "Replace research paper with uploaded 13-page PDF"
git -C "$REPO_DIR" push origin main
echo "Replacement pushed. PDF SHA-256: $INSTALLED_SHA"
