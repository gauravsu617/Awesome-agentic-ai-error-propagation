# References

This file contains the 20 scholarly papers curated for the repository.

## 1. Agent Reasoning and Reflection

1. Yao, S. et al. (2023). **ReAct: Synergizing Reasoning and Acting in Language Models.** ICLR.
   https://arxiv.org/abs/2210.03629

2. Shinn, N. et al. (2023). **Reflexion: Language Agents with Verbal Reinforcement Learning.** arXiv.
   https://arxiv.org/abs/2303.11366

3. Yao, S. et al. (2023). **Tree of Thoughts: Deliberate Problem Solving with Large Language Models.** NeurIPS.
   https://arxiv.org/abs/2305.10601

4. Park, J. S. et al. (2023). **Generative Agents: Interactive Simulacra of Human Behavior.** UIST.
   https://arxiv.org/abs/2304.03442

5. Wang, G. et al. (2023). **Voyager: An Open-Ended Embodied Agent with Large Language Models.** arXiv.
   https://arxiv.org/abs/2305.16291

## 2. Tool Use and Multi-Agent Systems

6. Schick, T. et al. (2023). **Toolformer: Language Models Can Teach Themselves to Use Tools.** arXiv.
   https://arxiv.org/abs/2302.04761

7. Qin, Y. et al. (2023). **ToolLLM: Facilitating Large Language Models to Master 16,000+ Real-World APIs.** arXiv.
   https://arxiv.org/abs/2307.16789

8. Wu, Q. et al. (2023). **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.** arXiv.
   https://arxiv.org/abs/2308.08155

9. Hong, S. et al. (2023). **MetaGPT: Meta Programming for Multi-Agent Collaborative Framework.** arXiv.
   https://arxiv.org/abs/2308.00352

10. Shen, Y. et al. (2023). **HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face.** NeurIPS.
    https://arxiv.org/abs/2303.17580

## 3. Retrieval and Grounding

11. Lewis, P. et al. (2020). **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.** NeurIPS.
    https://arxiv.org/abs/2005.11401

12. Asai, A. et al. (2024). **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection.** ICLR.
    https://arxiv.org/abs/2310.11511

13. Yao, S. et al. (2022). **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents.** NeurIPS.
    https://arxiv.org/abs/2207.01206

14. Deng, X. et al. (2023). **Mind2Web: Towards a Generalist Agent for the Web.** NeurIPS.
    https://arxiv.org/abs/2306.06070

15. Dongre, V. et al. (2024). **ReSpAct: Harmonizing Reasoning, Speaking, and Acting Towards Building Large Language Model-Based Conversational AI Agents.** arXiv.
    https://arxiv.org/abs/2411.00927

## 4. Evaluation and Reliability

16. Liu, X. et al. (2023). **AgentBench: Evaluating LLMs as Agents.** arXiv / ICLR.
    https://arxiv.org/abs/2308.03688

17. Zhou, S. et al. (2023). **WebArena: A Realistic Web Environment for Building Autonomous Agents.** arXiv / ICLR.
    https://arxiv.org/abs/2307.13854

18. Mialon, G. et al. (2023). **GAIA: A Benchmark for General AI Assistants.** arXiv.
    https://arxiv.org/abs/2311.12983

19. Yang, J. et al. (2024). **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering.** NeurIPS.
    https://arxiv.org/abs/2405.15793

20. Debenedetti, E. et al. (2024). **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.** arXiv.
    https://arxiv.org/abs/2406.13352

## Relevance to This Repository

These papers collectively cover the major components of multi-step agentic workflows:

* Reasoning
* Planning
* Reflection
* Memory
* Tool use
* Multi-agent collaboration
* Retrieval
* External grounding
* Web interaction
* Agent evaluation
* Long-horizon tasks
* Reliability and robustness

They provide the scholarly foundation for studying how errors can arise and propagate across agentic AI research workflows.


## Updated AITR Literature and Citation-Audit Findings — 29 October 2026

The supplied FINAL ATR ZIP contains `Part_A_Citation_Verification.xlsx` and `references.bib`. The bibliography source is also mirrored at [aitr-submission/references.bib](../aitr-submission/references.bib). The workbook records 22 original review references with 15 fully supported, six partially supported, and one unsupported/misattributed citation; it lists seven new candidates, two marked fully supported and five still requiring verification. These are workbook-reported statuses, not an independent re-audit in this commit.

### Newer topic-relevant papers

1. Cemri et al. (2025). **Why Do Multi-Agent LLM Systems Fail?** [DOI](https://doi.org/10.48550/arXiv.2503.13657). Workbook status: fully supported; recommended for the multi-agent failure-taxonomy claim.
2. **Where LLM Agents Fail and How They Can Learn From Failures** (2025). [DOI](https://doi.org/10.48550/arXiv.2509.25370). Workbook status: fully supported; recommended as a close match to the project's focus.
3. Roder et al. (2025). **Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents.** [DOI](https://doi.org/10.48550/arXiv.2509.14382). Check figures against the primary paper before use.
4. Zhang et al. (2025). **Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems.** [DOI](https://doi.org/10.48550/arXiv.2505.00212). Confirm venue, identifiers, and numerical claims.
5. Liu et al. (2026). **PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems.** [ACL Anthology](https://aclanthology.org/2026.emnlp-main.891/). Hold pending primary-source verification.
6. Toro Isaza et al. (2026). **Context or Capability? Debugging Agentic Workflows.** [IBM Research](https://research.ibm.com/publications/context-or-capability-debugging-agentic-workflows). Hold pending primary-source verification.
7. Bateman et al. (2026). **Agent Error Simulator: Fault Injection for Testing Recovery in Agentic Workflows.** [IIT GRC publication page](https://grc.iit.edu/gnosis/publications/bateman-2026-agent-error-simulator-3c7d/). Venue and details need verification.

See the [full citation verification audit](../citation/Citation_Verification_Audit.md) for the per-paper status and source links.

### Manuscript corrections identified by the workbook

- Replace placeholder DOI text in the reference list with actual identifiers.
- Keep AutoGen and MetaGPT citations for framework descriptions, but do not use them as direct evidence for correlated-error claims; the workbook marks P10 unsupported/misattributed and P11 partially supported, and recommends N01 for the specific failure-mode claim.
- Reword Self-Consistency as sampling multiple reasoning paths and selecting the most consistent answer.
- Soften claims that Reflexion makes subsequent drafts more forceful or that Generative Agents directly demonstrates memory-error propagation.
- Label the claim that citation-generation and FActScore work does not measure error propagation as the review author's gap observation, not as a finding from those papers.
- Correct the ReSpAct title spelling/venue/year, and use a consistent GAIA version/year.

## How to use these records

Use the original 20-paper list above as the curated repository collection. Use the AITR bibliography and its audit table for the manuscript's expanded reference set. Never treat an abstract-level or workbook-labelled record as verified evidence for a specific sentence until the primary source has been checked.
