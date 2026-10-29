# Research Paper — Canonical Replacement

## Selected manuscript

The PDF attached in this conversation as `research paper.pdf` is the intended replacement for `paper/RESEARCH_paper.pdf`.

- **Title:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation
- **Author shown in PDF:** Sutariya Gaurav Karsanbhai
- **Pages:** 13
- **Size:** 470,387 bytes
- **SHA-256:** `a4b8bc4d27355c43bb619ac0c15cfeba247de91171199083322060e7f917ef96`
- **Source match:** Byte-identical to `FINAL ATR/agentic_ai_error_propagation_research_paper.pdf` in the supplied ZIP.
- **Different version:** `Overleaf_Final_Paper.pdf` and `Prism_Final_Paper.pdf` form a separate 14-page, byte-identical pair.

## Replacement status

The connected GitHub writer can update text files but could not upload the attached raw PDF bytes directly. Therefore, the remote `paper/RESEARCH_paper.pdf` has **not been replaced by this edit alone**.

The repository now includes [`replace_research_paper.sh`](replace_research_paper.sh). Download the attached PDF or the [replacement bundle](sandbox:/mnt/data/research-paper-replacement-bundle.zip), clone/pull the repository, and run from a clean local `main` checkout:

```bash
bash paper/replace_research_paper.sh "/path/to/research paper.pdf"
```

The script checks the repository origin and branch, fast-forwards `main`, verifies the exact SHA-256, replaces the PDF and indexes, creates a commit, and pushes it. The replacement is complete only after that push succeeds and GitHub shows the PDF blob size as 470,387 bytes with the expected Git blob SHA.

## Related project documentation

- [Citation verification audit](../citation/Citation_Verification_Audit.md)
- [Dataset and experiment protocol](../datasets/datasets.md)
- [Implementation and result inventory](../implementations/github-repositories.md)
- [Bibliography](../references/references.md)
- [Reproducibility audit](../aitr-submission/docs/REPRODUCIBILITY_AUDIT.md)
