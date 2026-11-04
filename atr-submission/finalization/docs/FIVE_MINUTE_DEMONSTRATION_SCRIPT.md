# Five-Minute Research Demonstration Script

## 0:00–0:40 — Research problem
Explain that the project studies how an error at one stage of a multi-step workflow may increase the probability of an error at the next stage. The four simulated stages are planning, retrieval, evidence extraction, and verification.

## 0:40–1:30 — Research question and design
Compare independent errors with conditional propagation. In the propagation condition, if the previous stage has an error, the next stage uses min(1, p + 0.30). Test p = 0.0, 0.1, 0.2, and 0.3, with 30 seeds and 100 trials per seed/rate/condition, for 24,000 records.

## 1:30–2:30 — Code walkthrough
Show the simulator function, the previous-stage error flag, the conditional probability adjustment, the CSV output columns, and the Prompt 9 sanity tests.

## 2:30–3:40 — Results
Show that mean stage errors increase under propagation: differences are 0.1070, 0.2067, and 0.3310 at base rates 0.1, 0.2, and 0.3.

## 3:40–4:30 — Interpretation
Explain why the binary any-error rate is equal: the workflow is already marked failed at the first error. Later errors increase stage-error count but do not change the binary flag.

## 4:30–5:00 — Limitations
State clearly that this is a synthetic simulation, not a live LLM-agent or HotpotQA experiment. Future work should test real agent traces, recovery, terminal-output correctness, and evidence-support accuracy.

## Checklist
- Open the Phase III notebook.
- Show the conditional rule.
- Show the raw CSV and validation report.
- Show the recalculated table and graph.
- Explain the any-error metric and synthetic-simulation limitation.