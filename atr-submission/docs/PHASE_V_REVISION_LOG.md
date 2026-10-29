# Phase V — Manuscript Revision Log

**Source:** `Phase5.zip` inside `FINAL ATR(1).zip`.

| ID | Revision/check | Required evidence | Status |
|---|---|---|---|
| V01 | Draft IEEE-style manuscript structure | `paper/main.tex` | Drafted in source package |
| V02 | Verify numerical table against raw CSV | Raw CSV and evaluator output | PASS — exact CSV reproduction and Phase IV evaluation passed in GitHub Actions run #7; newest manuscript revision is being rebuilt |
| V03 | Specify propagation probability equation | Actual simulation source | PASS — manuscript documents the implemented conditional increment and cap; exact output reproduced by standalone script |
| V04 | Confirm trial count, seed policy and matched conditions | Raw CSV/configuration | PASS — 24,000 rows, 30 seeds, 100 trials, two conditions, four rates; matched by seed/trial/rate |
| V05 | Add verified original-source bibliography | Original papers/publisher records | PARTIAL — all 23 entries are now cited in the manuscript; source-level metadata and claim-support audit remains open |
| V06 | Compile LaTeX and inspect PDF | Actual build log and PDF | PARTIAL — run #7 built PDF and uploaded artifacts successfully; latest bibliography/manuscript edits require a fresh successful build and visual PDF inspection |
| V07 | Technical peer review and response | Peer review and evidence-backed responses | Initial review drafted |
| V08 | Validate README commands from clean clone | Terminal output | TEST REQUIRED |
| V09 | Check repository URL, branch, license and public files | Repository inspection | PARTIAL — repository URL and main branch are confirmed; license and redistribution review remains open |

## Revision rule
Do not mark an item complete merely because text or code exists. Close it only after the listed evidence has been inspected and saved. The source package specifically warns that its manuscript numbers were transcribed from earlier notes and were not independently recomputed during drafting.
