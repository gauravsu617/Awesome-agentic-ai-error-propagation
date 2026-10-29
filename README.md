# Awesome Agentic AI Error Propagation

A curated collection of research papers, datasets, tools, GitHub implementations, and learning resources related to error propagation in multi-step agentic AI workflows for research automation.

This repository focuses on how errors introduced during planning, retrieval, source selection, evidence extraction, reasoning, tool use, memory, and verification can propagate through downstream stages. It also collects resources for improving reliability, traceability, reproducibility, and evidence-grounded research automation.

## Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Curated Research Papers](#curated-research-papers)
  - [Agent Reasoning and Reflection](#agent-reasoning-and-reflection)
  - [Tool Use and Multi-Agent Systems](#tool-use-and-multi-agent-systems)
  - [Retrieval and Grounding](#retrieval-and-grounding)
  - [Evaluation and Reliability](#evaluation-and-reliability)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [Research Challenges](#research-challenges)
- [Research Gaps and Future Directions](#research-gaps-and-future-directions)
- [License](#license)

## Overview

Agentic artificial intelligence systems perform complex tasks through sequences of planning, reasoning, information retrieval, tool use, memory, verification, and generation. Research automation is an important application because agents can assist with literature discovery, evidence extraction, analysis, synthesis, and report generation.

However, the reliability of a multi-step workflow depends on the correctness of intermediate outputs. An error introduced during an early stage can become an input to later stages and propagate through the workflow. A research workflow can therefore be represented as:

**Research Question → Planning → Literature Search → Source Selection → Evidence Extraction → Analysis → Synthesis → Verification → Report Generation**

Major error sources include planning errors, information-retrieval failures, source-selection errors, evidence-extraction errors, reasoning errors, citation errors, tool-use errors, and memory errors. Errors can propagate through sequential dependencies, amplification, masking, correlated errors, and feedback loops.

Reliable research automation requires more than fluent final text. Important approaches include external grounding, tool-augmented research, reflection, independent verification, provenance tracking, uncertainty representation, error tracing, and human-in-the-loop review. This repository collects research and practical resources for studying these problems and developing more reliable multi-step AI research systems.

## AI-Assisted Research Paper

### Error Propagation in Multi-Step Agentic AI Workflows for Research Automation

This research paper examines how errors can enter different stages of an agentic research workflow and affect downstream outputs. It discusses error sources, propagation mechanisms, current reliability approaches, research challenges, and future directions.

**Paper currently in repository:** [RESEARCH_paper.pdf](paper/RESEARCH_paper.pdf) (not replaced by the newer ZIP PDF in this text-file update).  
**Manuscript version inventory:** [paper/README.md](paper/README.md) lists the latest PDFs and LaTeX sources present in FINAL ATR and explains which binary files still need uploading.

### Main Workflow

**Research Question → Planning → Literature Search → Source Selection → Evidence Extraction → Analysis → Synthesis → Verification → Report Generation**

## Citation Integrity Audit

The citation-integrity audit checks whether references and claims in the AI-assisted research paper are reliable. The audit considers bibliographic metadata, source existence, identifiers, and whether cited evidence supports the associated claim.

**Audit checklist:** [Citation Integrity Audit Checklist](aitr-submission/docs/CITATION_INTEGRITY_AUDIT.md)  
**Latest citation review:** [Citation Verification Audit](citation/Citation_Verification_Audit.md), summarising the 22 original references, seven new candidates, recorded statuses, and manuscript corrections from the supplied workbook. The raw XLSX is still in the local ZIP; its former GitHub file was a one-byte placeholder, so it was removed.

## Curated Research Papers

Exactly 20 distinct scholarly papers are listed below as the repository's curated baseline list. For the AITR project's expanded 22-reference verification table, seven newer candidates, and paper-specific corrections, see [Citation Verification Audit](citation/Citation_Verification_Audit.md) and [references/references.md](references/references.md). Each paper in the curated list has a one-line relevance description.

### Agent Reasoning and Reflection

1. **ReAct: Synergizing Reasoning and Acting in Language Models** — Shunyu Yao et al. (2023), ICLR. Combines reasoning traces with actions and external information, forming a foundation for multi-step agent workflows.  
   [Paper](https://arxiv.org/abs/2210.03629)

2. **Reflexion: Language Agents with Verbal Reinforcement Learning** — Noah Shinn et al. (2023), arXiv. Uses verbal feedback and memory to support iterative self-correction in agents.  
   [Paper](https://arxiv.org/abs/2303.11366)

3. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** — Shunyu Yao et al. (2023), NeurIPS. Explores structured search over multiple reasoning paths for difficult tasks.  
   [Paper](https://arxiv.org/abs/2305.10601)

4. **Generative Agents: Interactive Simulacra of Human Behavior** — Joon Sung Park et al. (2023), UIST. Introduces agents combining memory, reflection, and planning.  
   [Paper](https://arxiv.org/abs/2304.03442)

5. **Voyager: An Open-Ended Embodied Agent with Large Language Models** — Guanzhi Wang et al. (2023), arXiv. Combines automatic curriculum, a skill library, and iterative feedback for an open-ended agent.  
   [Paper](https://arxiv.org/abs/2305.16291)

### Tool Use and Multi-Agent Systems

6. **Toolformer: Language Models Can Teach Themselves to Use Tools** — Timo Schick et al. (2023), arXiv. Studies how language models can learn to call external tools and APIs.  
   [Paper](https://arxiv.org/abs/2302.04761)

7. **ToolLLM: Facilitating Large Language Models to Master 16,000+ Real-World APIs** — Yujia Qin et al. (2023), arXiv. Provides large-scale research on API/tool use and tool-selection reasoning.  
   [Paper](https://arxiv.org/abs/2307.16789)

8. **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation** — Qingyun Wu et al. (2023), arXiv. Provides a framework for applications involving multiple interacting agents, tools, and humans.  
   [Paper](https://arxiv.org/abs/2308.08155)

9. **MetaGPT: Meta Programming for Multi-Agent Collaborative Framework** — Sirui Hong et al. (2023), arXiv. Organizes multiple agents around structured software-development workflows and roles.  
   [Paper](https://arxiv.org/abs/2308.00352)

10. **HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face** — Yongliang Shen et al. (2023), NeurIPS. Uses an LLM as a controller to plan tasks, select models, execute subtasks, and summarize results.  
    [Paper](https://arxiv.org/abs/2303.17580)

### Retrieval and Grounding

11. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** — Patrick Lewis et al. (2020), NeurIPS. Introduces retrieval-augmented generation for combining language models with external knowledge.  
    [Paper](https://arxiv.org/abs/2005.11401)

12. **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection** — Akari Asai et al. (2024), ICLR. Combines retrieval, generation, and self-critique to improve factuality and quality.  
    [Paper](https://arxiv.org/abs/2310.11511)

13. **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents** — Shunyu Yao et al. (2022), NeurIPS. Provides an interactive web environment for grounded language-agent evaluation.  
    [Paper](https://arxiv.org/abs/2207.01206)

14. **Mind2Web: Towards a Generalist Agent for the Web** — Xiang Deng et al. (2023), NeurIPS. Introduces a benchmark and dataset for generalist web agents operating on real websites.  
    [Paper](https://arxiv.org/abs/2306.06070)

15. **ReSpAct: Harmonizing Reasoning, Speaking, and Acting Towards Building Large Language Model-Based Conversational AI Agents** — Vivek Dongre et al. (2024), arXiv. Studies coordination between reasoning, communication, and action in conversational agents.  
    [Paper](https://arxiv.org/abs/2411.00927)

### Evaluation and Reliability

16. **AgentBench: Evaluating LLMs as Agents** — Xiao Liu et al. (2023), arXiv / ICLR 2024. Evaluates LLM agents across multiple interactive environments and long-term tasks.  
    [Paper](https://arxiv.org/abs/2308.03688)

17. **WebArena: A Realistic Web Environment for Building Autonomous Agents** — Shuyan Zhou et al. (2023), arXiv / ICLR 2024. Provides a realistic, reproducible environment for evaluating long-horizon web agents.  
    [Paper](https://arxiv.org/abs/2307.13854)

18. **GAIA: A Benchmark for General AI Assistants** — Grégoire Mialon et al. (2023), arXiv. Evaluates general AI assistants on questions requiring reasoning, browsing, and tool use.  
    [Paper](https://arxiv.org/abs/2311.12983)

19. **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** — John Yang et al. (2024), NeurIPS. Studies how agent-computer interfaces affect autonomous multi-step task performance.  
    [Paper](https://arxiv.org/abs/2405.15793)

20. **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents** — Edoardo Debenedetti et al. (2024), arXiv. Evaluates agent reliability and robustness when agents interact with tools and untrusted data.  
    [Paper](https://arxiv.org/abs/2406.13352)

## Datasets and Benchmarks

Three external reference benchmarks are curated here. The latest AITR protocol separately names HotpotQA distractor validation as its planned primary dataset; the results ZIP contains a separate synthetic simulation, not HotpotQA question-answer runs. See [Datasets and Experiment Protocols](datasets/datasets.md) for the distinction and status.

### 1. AgentBench

A multi-environment benchmark for evaluating LLM agents across interactive tasks, useful for studying long-horizon reasoning and decision-making.

**Source:** [AgentBench](https://github.com/THUDM/AgentBench)

### 2. Mind2Web

A dataset and benchmark for generalist web agents, including human-demonstrated web interaction trajectories.

**Source:** [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web)

### 3. ToolBench

A tool-use dataset and benchmark involving real-world APIs, useful for studying tool selection, API calls, and multi-step tool reasoning.

**Source:** [ToolBench / ToolLLM](https://github.com/OpenBMB/ToolBench)

## Tools and Libraries

Five engineering frameworks remain in the curated list. The latest AITR workbook also records a separate evaluation of four literature-discovery tools (ResearchRabbit, Litmaps, Semantic Scholar, and Elicit); see [tools/tools.md](tools/tools.md) for the workbook's ratings and limitations.

### 1. LangChain

An open-source framework for building LLM applications and agents with model, tool, retrieval, and workflow integrations.

**Official:** [LangChain](https://www.langchain.com/)

### 2. LlamaIndex

A framework for connecting LLM applications with external data and building retrieval and agent workflows.

**Official:** [LlamaIndex](https://www.llamaindex.ai/)

### 3. LangGraph

A low-level orchestration framework for building stateful agent workflows with graph-based execution, persistence, and human-in-the-loop capabilities.

**Official:** [LangGraph](https://www.langchain.com/langgraph)

### 4. AutoGen

An open-source framework for building applications with multiple interacting agents, tools, and human inputs.

**Official:** [AutoGen](https://github.com/microsoft/autogen)

### 5. DSPy

A framework for programming and optimizing language-model pipelines and modular AI systems.

**Official:** [DSPy](https://github.com/stanfordnlp/dspy)

## GitHub Implementations

Five external reference implementations remain in the curated list. The student's code notebooks, evaluator, and provided result summaries are catalogued in [GitHub Implementations and Local Research Code](implementations/github-repositories.md). Some original binaries from the ZIP are still awaiting upload; see [the archive manifest](aitr-submission/ARCHIVE_MANIFEST.md).

### 1. AgentBench

Implementation of the AgentBench multi-environment evaluation framework.

**Repository:** [THUDM/AgentBench](https://github.com/THUDM/AgentBench)

### 2. Mind2Web

Official implementation and resources for the Mind2Web generalist web-agent benchmark.

**Repository:** [OSU-NLP-Group/Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web)

### 3. SELF-RAG

Official implementation of Self-RAG, including models and training data for retrieval, generation, and self-reflection.

**Repository:** [AkariAsai/self-rag](https://github.com/AkariAsai/self-rag)

### 4. WebShop

Official implementation of the WebShop interactive environment and search agents.

**Repository:** [princeton-nlp/WebShop](https://github.com/princeton-nlp/WebShop)

### 5. AgentDojo

Official implementation of the AgentDojo dynamic environment for evaluating prompt-injection attacks and defenses in LLM agents.

**Repository:** [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo)

## Tutorials and Learning Resources

Exactly 5 learning resources are included.

### 1. LangChain Agents Quickstart

A practical introduction to creating agents, adding tools, and running agent workflows.

**Resource:** [LangChain Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart)

### 2. LangChain Deep Research Agent Quickstart

A tutorial for building a multi-step research agent with planning, file tools, and subagents.

**Resource:** [Deep Agents Quickstart](https://docs.langchain.com/oss/python/deepagents/quickstart)

### 3. LangChain Learn

A collection of tutorials covering agents, RAG, semantic search, SQL agents, multi-agent systems, memory, and deep research.

**Resource:** [LangChain Learn](https://docs.langchain.com/oss/python/learn)

### 4. WebArena

Documentation and setup resources for a realistic web-agent environment and long-horizon agent evaluation.

**Resource:** [WebArena GitHub](https://github.com/web-arena-x/webarena)

### 5. AgentDojo

Documentation and practical setup instructions for evaluating tool-using agents against prompt-injection attacks and defenses.

**Resource:** [AgentDojo GitHub](https://github.com/ethz-spylab/agentdojo)

## Research Challenges

### Lack of Standard Error-Propagation Metrics

Agent benchmarks commonly report task success or overall performance, but standardized measures for tracking error propagation across complete research workflows remain limited.

Potential metrics include:

- Stage Error Rate
- Propagation Rate
- Amplification Factor
- Recovery Rate
- Undetected Error Rate
- Claim-Support Accuracy

### Causal Attribution

When a final research report is incorrect, identifying the original cause can be difficult because the error may originate in planning, retrieval, source selection, extraction, reasoning, memory, or synthesis.

### Long-Horizon Reliability

Long research workflows increase the importance of state management, intermediate verification, and recovery mechanisms.

### Verification Dependence

A verification model can reproduce the same biases or reasoning failures as the system it evaluates. Independent evidence and independent verification are therefore important.

### Reproducibility

Research agents should preserve search queries, source identifiers, retrieval dates, retrieved evidence, model/version information, tool outputs, and important intermediate decisions.

## Research Gaps and Future Directions

### 1. Workflow-Level Benchmarks

Future benchmarks should evaluate complete research workflows instead of isolated agent capabilities.

### 2. Causal Error Tracing

Systems should identify where an error originated and determine which downstream outputs were affected.

**Error lineage:**

**Initial Error → Affected Intermediate Results → Affected Claims → Affected Conclusions**

### 3. Independent Multi-Agent Verification

Independent verification can use separate prompts, separate evidence retrieval, primary sources, different reasoning paths, and explicit disagreement mechanisms.

### 4. Evidence-Centered Generation

A reliable research workflow should move toward:

**Retrieve → Verify → Extract Evidence → Construct Claim → Cite**

### 5. Uncertainty-Aware Research Agents

Agents should explicitly represent confidence levels such as:

- Verified
- Strongly supported
- Partially supported
- Uncertain
- Unsupported

### 6. Human-AI Collaborative Research

Controlled autonomy may be more reliable than unrestricted autonomy, with AI handling repetitive tasks while humans retain responsibility for interpretation and important decisions.

## Key Error Propagation Chain

A central concept of this repository is the propagation of errors through dependent workflow stages:

**Wrong Source → Wrong Summary → Wrong Synthesis → Unsupported Conclusion**

An error that begins as a retrieval or source-selection problem can become a research-level claim after passing through summarization, synthesis, citation, and report generation.

A final report may contain genuine sources and fluent academic writing while still answering the wrong research question. Therefore, citation authenticity alone is not sufficient for research reliability.


## AITR Implementation-Based Research Submission

The repository now includes a selected AITR source-and-audit subset for **Error Propagation in Multi-Step Agentic AI Workflows for Research Automation**. The full supplied FINAL ATR archive is not yet mirrored file-for-file; see the archive manifest for the distinction between files present in GitHub and files still only in the original package.

- [Open the AITR submission package](aitr-submission/README.md)
- [FINAL ATR archive manifest and mirror status](aitr-submission/ARCHIVE_MANIFEST.md)
- [Reproducibility and evidence audit](aitr-submission/docs/REPRODUCIBILITY_AUDIT.md)
- [Citation integrity audit checklist](aitr-submission/docs/CITATION_INTEGRITY_AUDIT.md)
- [Instructions to sync remaining archive files](aitr-submission/docs/LOCAL_SYNC_AND_UPLOAD.md)

The research package distinguishes existing artifacts from experiments that still require execution or verification. Do not interpret the presence of a notebook, result archive, or manuscript as proof that all experiments were executed successfully. Results should be reported only after running the documented workflow and preserving logs.

## License

No LICENSE file is currently present, so the repository does not yet state an explicit project license. Before adding one, confirm that the owner has the right to license every included item.

Third-party research papers and copyrighted materials should not be uploaded unless redistribution is permitted. Where possible, link to publisher pages, DOI records, arXiv, official project pages, or other authorized sources.

## Repository Structure

```text
awesome-agentic-ai-error-propagation/
├── README.md
├── citation/
│   └── Citation_Verification_Audit.md
├── datasets/
│   └── datasets.md
├── implementations/
│   ├── github-repositories.md
│   └── results/
│       ├── final_comparison.csv
│       ├── multi_seed_summary.csv
│       ├── validation_report.json
│       ├── environment_verification.json
│       └── gpu_verification.json
├── paper/
│   ├── RESEARCH_paper.pdf
│   └── README.md
├── references/
│   ├── references.md
│   └── references.bib
├── tools/
│   └── tools.md
└── aitr-submission/
    ├── ARCHIVE_MANIFEST.md
    ├── README.md
    ├── references.bib
    ├── ATR_PHASE_IV_completed_Prompts_12_14.ipynb
    ├── evaluate_phaseiv.py
    └── docs/
        ├── CITATION_INTEGRITY_AUDIT.md
        ├── LOCAL_SYNC_AND_UPLOAD.md
        └── REPRODUCIBILITY_AUDIT.md
```

## Submission Checklist

- [x] Repository title and description
- [x] Clickable Table of Contents
- [x] 150–300 word topic overview
- [x] AI-assisted research paper section
- [x] Citation-integrity audit section
- [x] Exactly 20 distinct scholarly papers
- [x] Meaningful paper categories
- [x] One-line description for each paper
- [x] Exactly 3 datasets/benchmarks
- [x] Exactly 5 tools/libraries
- [x] Exactly 5 GitHub implementations
- [x] Exactly 5 learning resources
- [x] Research challenges
- [x] Research gaps and future directions
- [ ] Add a suitable license after confirming redistribution rights
- [ ] Verify every external link before submission
- [ ] Ensure no unauthorized copyrighted PDFs are uploaded
- [ ] Make at least 5 meaningful Git commits
- [ ] Keep repository public
