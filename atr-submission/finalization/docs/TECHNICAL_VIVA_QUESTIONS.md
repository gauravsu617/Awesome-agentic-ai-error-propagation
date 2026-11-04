# Technical Viva Questions and Suggested Answers

1. **What is error propagation?** An error generated at one stage affects later stages and may increase downstream errors.
2. **What are the four stages?** Planning, retrieval, evidence extraction, and verification.
3. **What is the independent condition?** Every stage uses the same base error probability p.
4. **What is the propagation condition?** If the immediately previous stage has an error, the next-stage probability becomes min(1, p + 0.30).
5. **Why use 0.30?** It is a fixed design parameter for this synthetic simulation, not a value calibrated from real agent traces.
6. **How many records?** 30 seeds × 100 trials × 4 base rates × 2 conditions = 24,000.
7. **What is the primary metric?** Mean stage-error count per workflow.
8. **Why are binary failure rates equal?** The flag is stage_errors > 0; after the first error, later errors cannot change the binary flag.
9. **Why pair comparisons?** The same random seed is reset for both conditions, allowing matching by seed and trial.
10. **What are the paired mean differences?** 0.1070, 0.2067, and 0.3310 at p=0.1, 0.2, and 0.3.
11. **Is this a live LLM experiment?** No. It is a synthetic stochastic simulation.
12. **Was HotpotQA used?** It appears in planning materials as a possible validation dataset; the reported experiment is not a HotpotQA run.
13. **What are the limitations?** Fixed propagation increment, four stages, binary errors, no recovery, and no real-agent terminal correctness.
14. **What is the next step?** Add verification/recovery interventions and evaluate real agent traces and terminal outputs.
15. **What was the student's personal contribution?** The student reports checking the paper, executing the notebook, and checking and verifying the final results.