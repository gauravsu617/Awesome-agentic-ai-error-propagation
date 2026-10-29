# References

This page preserves the repository's original 20-paper curated list and adds the updated AITR citation-audit findings from the supplied FINAL ATR ZIP.

## AITR manuscript bibliography source

The archive's `references.bib` is mirrored at [aitr-submission/references.bib](../aitr-submission/references.bib). The citation workbook reports 22 original review references and seven newer candidates, with recorded statuses:
- Original 22: 15 fully supported, six partially supported, one not supported/misattributed.
- New seven: two fully supported/add, five still requiring verification.

See [Citation Verification Audit](../citation/Citation_Verification_Audit.md) for all paper IDs, status labels, DOI links, and required manuscript corrections.

## Newer papers most relevant to the stated research gap

1. Cemri et al. (2025). **Why Do Multi-Agent LLM Systems Fail?** arXiv. [DOI](https://doi.org/10.48550/arXiv.2503.13657). Workbook status: fully supported; recommended to add for the multi-agent failure taxonomy claim.
2. **Where LLM Agents Fail and How They Can Learn From Failures** (2025). arXiv. [DOI](https://doi.org/10.48550/arXiv.2509.25370). Workbook status: fully supported; recommended to add as a close match for failure diagnosis/debugging.
3. Roder et al. (2025). **Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents.** [arXiv](https://doi.org/10.48550/arXiv.2509.14382). Check figures and exact evidence before using.
4. Zhang et al. (2025). **Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems.** [arXiv](https://doi.org/10.48550/arXiv.2505.00212). Confirm the exact venue, identifiers, and quoted numbers.
5. Liu et al. (2026). **PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems.** [ACL Anthology record](https://aclanthology.org/2026.emnlp-main.891/). Hold pending a primary-source read.
6. Toro Isaza et al. (2026). **Context or Capability? Debugging Agentic Workflows.** [IBM Research](https://research.ibm.com/publications/context-or-capability-debugging-agentic-workflows). Hold pending a primary-source read.
7. Bateman et al. (2026). **Agent Error Simulator: Fault Injection for Testing Recovery in Agentic Workflows.** [IIT GRC publication page](https://grc.iit.edu/gnosis/publications/bateman-2026-agent-error-simulator-3c7d/). Venue/details need checking.

Items 5–7 have no DOI recorded in the workbook and remain unverified; do not cite them as confirmed findings without primary-source checks.

## Important correction notes from the citation workbook

- Remove placeholder text such as “DOI: Open DOI / publication page”; use the actual identifiers in the citation audit.
- Do not attribute correlated-error findings to AutoGen/MetaGPT without support; use N01 for the failure-mode claim, while keeping framework citations only for what those papers actually describe.
- Correct the interpretation of Self-Consistency, soften the Reflexion and Generative Agents claims about error persistence, and separate the review author's gap observations from results reported by ALCE/FActScore.
- Correct the title/venue/year record for ReSpAct and ensure the GAIA year is described consistently with the version being cited.

## Original curated references

The original 20-paper list remains below/alongside this AITR-specific update to preserve the repository's prior curated resource collection. Use the per-paper descriptions and links in the repository's README; for the experimental manuscript, prefer the full BibTeX source and audit status rather than a title-only list.
