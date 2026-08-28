# Awesome Agentic AI Error Propagation

A curated collection of research papers, datasets, tools, GitHub implementations, and learning resources related to error propagation in multi-step agentic AI workflows for research automation.

This repository focuses on understanding how errors introduced during planning, retrieval, source selection, evidence extraction, reasoning, tool use, memory, and verification can propagate through downstream stages. It also collects resources for improving the reliability, traceability, and reproducibility of AI-assisted research workflows.

---

## Contents

* [Overview](#overview)
* [AI-Assisted Research Paper](#ai-assisted-research-paper)
* [Citation Integrity Audit](#citation-integrity-audit)
* [Curated Research Papers](#curated-research-papers)

  * [Foundational Papers](#foundational-papers)
  * [Tool Use and Agent Frameworks](#tool-use-and-agent-frameworks)
  * [Evaluation and Benchmarks](#evaluation-and-benchmarks)
  * [Retrieval and Verification](#retrieval-and-verification)
* [Datasets](#datasets)
* [Tools and Libraries](#tools-and-libraries)
* [GitHub Implementations](#github-implementations)
* [Tutorials and Learning Resources](#tutorials-and-learning-resources)
* [Research Challenges](#research-challenges)
* [Research Gaps and Future Directions](#research-gaps-and-future-directions)
* [License](#license)

---

## Overview

Agentic artificial intelligence systems are increasingly being developed to perform complex tasks through sequences of planning, reasoning, information retrieval, tool use, memory, verification, and generation. Research automation is a particularly important application because agentic systems can assist with literature discovery, evidence extraction, synthesis, data analysis, and report generation.

However, the reliability of a multi-step workflow depends not only on the capabilities of the underlying large language model but also on the correctness of intermediate outputs. An error introduced during an early stage can become an input to later stages and subsequently propagate through the workflow.

A research-oriented workflow can be represented as:

**Research Question → Planning → Literature Search → Source Selection → Evidence Extraction → Analysis → Synthesis → Verification → Report Generation**

Major sources of error include planning errors, retrieval failures, source-selection errors, evidence-extraction errors, reasoning mistakes, citation errors, tool-use failures, and memory errors. Propagation can occur through sequential dependencies, error amplification, error masking, correlated errors, and feedback loops.

Reliable research automation therefore requires more than fluent final text. Important approaches include external grounding, tool use, reflection, independent verification, provenance tracking, uncertainty representation, error tracing, and human oversight.

---

## AI-Assisted Research Paper

### Error Propagation in Multi-Step Agentic AI Workflows for Research Automation

This research paper examines error propagation in multi-step agentic AI workflows used for research automation. It analyzes how errors can enter at different stages of the workflow and affect downstream outputs.

The paper discusses:

* Agentic AI and multi-step reasoning
* Tool-augmented language models
* Reflection and self-correction
* Agent evaluation
* Planning and retrieval errors
* Source-selection and evidence-extraction errors
* Reasoning and citation errors
* Tool-use and memory errors
* Sequential error propagation
* Error amplification
* Error masking
* Correlated errors
* Feedback-loop failures
* External grounding
* Independent verification
* Provenance tracking
* Human-in-the-loop systems
* Workflow-level benchmarks
* Causal error tracing
* Evidence-centered generation
* Uncertainty-aware research agents

**Paper:** `paper/AI_Assisted_Research_Paper.pdf`

The paper emphasizes that reliable research automation requires validation throughout the workflow rather than relying only on final-output evaluation.

---

## Citation Integrity Audit

The citation-integrity audit checks whether references and claims in the AI-assisted research paper are reliable.

The verification process considers:

* Correct paper title
* Correct authors
* Publication year
* Journal or conference
* DOI or persistent identifier
* Whether the cited paper exists
* Whether the cited source actually supports the associated claim

**Audit:** `citation-audit/Citation_Integrity_Audit.pdf`

The research paper specifically distinguishes between whether a cited source exists and whether the source actually supports the claim for which it is cited.

---

# Curated Research Papers

The following papers are organized according to their relevance to agentic AI, multi-step reasoning, tool use, research automation, retrieval, verification, and evaluation.

## Foundational Papers

### 1. ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Shunyu Yao et al.
**Year:** 2023
**Venue:** ICLR 2023
**Identifier:** arXiv:2210.03629
**Relevance:** Introduces the reasoning-and-acting paradigm that combines reasoning traces with actions and external information. It is directly relevant to multi-step agent workflows.

**Paper:** [ReAct paper](https://arxiv.org/abs/2210.03629?utm_source=chatgpt.com)

### 2. Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2303.11366
**Relevance:** Investigates verbal feedback and episodic memory for improving agent behavior and is relevant to reflection and self-correction.

**Paper:** [Reflexion paper](https://arxiv.org/abs/2303.11366?utm_source=chatgpt.com)

### 3. Tree of Thoughts: Deliberate Problem Solving with Large Language Models

**Authors:** Shunyu Yao et al.
**Year:** 2023
**Venue:** NeurIPS 2023
**Identifier:** arXiv:2305.10601
**Relevance:** Explores structured search over reasoning paths and is relevant to multi-step reasoning and error recovery.

**Paper:** [Tree of Thoughts paper](https://arxiv.org/abs/2305.10601?utm_source=chatgpt.com)

### 4. Generative Agents: Interactive Simulacra of Human Behavior

**Authors:** Joon Sung Park et al.
**Year:** 2023
**Venue:** UIST 2023
**Identifier:** arXiv:2304.03442
**Relevance:** Introduces agents with memory, reflection, and planning, making it relevant to persistent state and memory-related error propagation.

**Paper:** [Generative Agents paper](https://arxiv.org/abs/2304.03442?utm_source=chatgpt.com)

### 5. MetaGPT: Meta Programming for Multi-Agent Collaborative Framework

**Authors:** Sirui Hong et al.
**Year:** 2024
**Venue:** ICLR 2024
**Identifier:** arXiv:2308.00352
**Relevance:** Uses structured human workflows and multiple specialized agents. The paper is particularly relevant to cascading errors in multi-agent systems.

**Paper:** [MetaGPT paper](https://arxiv.org/abs/2308.00352?utm_source=chatgpt.com)

---

## Tool Use and Agent Frameworks

### 6. Toolformer: Language Models Can Teach Themselves to Use Tools

**Authors:** Timo Schick et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2302.04761
**Relevance:** Studies how language models can learn to use external tools and APIs.

**Paper:** [Toolformer paper](https://arxiv.org/abs/2302.04761?utm_source=chatgpt.com)

### 7. ToolLLM: Facilitating Large Language Models to Master 16,000+ Real-World APIs

**Authors:** Yujia Qin et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2307.16789
**Relevance:** Provides a large-scale tool-use framework and ToolBench dataset for evaluating API-based agent behavior.

**Paper:** [ToolLLM paper](https://arxiv.org/abs/2307.16789?utm_source=chatgpt.com)

### 8. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

**Authors:** Qingyun Wu et al.
**Year:** 2024
**Venue:** COLM 2024
**Identifier:** arXiv:2308.08155
**Relevance:** Provides a framework for building applications using multiple interacting agents, tools, and human inputs.

**Paper:** [AutoGen paper](https://arxiv.org/abs/2308.08155?utm_source=chatgpt.com)

### 9. HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

**Authors:** Yongliang Shen et al.
**Year:** 2023
**Venue:** NeurIPS 2023
**Relevance:** Uses an LLM as a controller for planning tasks, selecting models, executing subtasks, and summarizing results.

**Paper:** [HuggingGPT paper](https://arxiv.org/abs/2303.17580?utm_source=chatgpt.com)

### 10. Voyager: An Open-Ended Embodied Agent with Large Language Models

**Authors:** Guanzhi Wang et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2305.16291
**Relevance:** Demonstrates an agent architecture combining automatic curriculum, skill libraries, and iterative feedback.

**Paper:** [Voyager paper](https://arxiv.org/abs/2305.16291?utm_source=chatgpt.com)

### 11. DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

**Authors:** Omar Khattab et al.
**Year:** 2024
**Venue:** ICLR 2024
**Identifier:** arXiv:2310.03714
**Relevance:** Treats LLM pipelines as optimizable programs and is useful for studying reliability and performance across multi-step LM pipelines.

**Paper:** [DSPy paper](https://arxiv.org/abs/2310.03714?utm_source=chatgpt.com)

---

## Evaluation and Benchmarks

### 12. AgentBench: Evaluating LLMs as Agents

**Authors:** Xiao Liu et al.
**Year:** 2024
**Venue:** ICLR 2024
**Identifier:** arXiv:2308.03688
**Relevance:** Evaluates LLM agents across multiple interactive environments and highlights long-term reasoning and decision-making difficulties.

**Paper:** [AgentBench paper](https://arxiv.org/abs/2308.03688?utm_source=chatgpt.com)

### 13. WebArena: A Realistic Web Environment for Building Autonomous Agents

**Authors:** Shuyan Zhou et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2307.13854
**Relevance:** Provides a realistic and reproducible environment for evaluating long-horizon web agents.

**Paper:** [WebArena paper](https://arxiv.org/abs/2307.13854?utm_source=chatgpt.com)

### 14. GAIA: A Benchmark for General AI Assistants

**Authors:** Grégoire Mialon et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2311.12983
**Relevance:** Evaluates general AI assistants on real-world questions requiring reasoning, web browsing, multimodality, and tool use.

**Paper:** [GAIA paper](https://arxiv.org/abs/2311.12983?utm_source=chatgpt.com)

### 15. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors:** John Yang et al.
**Year:** 2024
**Venue:** NeurIPS 2024
**Identifier:** arXiv:2405.15793
**Relevance:** Studies how agent-computer interfaces influence the performance of language-model agents performing complex multi-step tasks.

**Paper:** [SWE-agent paper](https://arxiv.org/abs/2405.15793?utm_source=chatgpt.com)

### 16. WebArena and Long-Horizon Agent Evaluation

WebArena is particularly relevant to this repository because its tasks are designed to be diverse and long-horizon, making it useful for studying how errors accumulate across sequences of actions.

**Resource:** [WebArena project](https://webarena.dev/?utm_source=chatgpt.com)

---

## Retrieval and Verification

### 17. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis et al.
**Year:** 2020
**Venue:** NeurIPS 2020
**Identifier:** arXiv:2005.11401
**Relevance:** Introduces retrieval-augmented generation to combine parametric language models with external non-parametric memory and improve factual generation.

**Paper:** [RAG paper](https://arxiv.org/abs/2005.11401?utm_source=chatgpt.com)

### 18. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**Authors:** Akari Asai et al.
**Year:** 2023
**Venue:** ICLR 2024
**Identifier:** arXiv:2310.11511
**Relevance:** Combines retrieval, generation, and self-reflection and specifically evaluates factuality and citation accuracy.

**Paper:** [Self-RAG paper](https://arxiv.org/abs/2310.11511?utm_source=chatgpt.com)

### 19. ReSpAct: Harmonizing Reasoning, Speaking, and Acting Towards Building Large Language Model-Based Conversational AI Agents

**Authors:** Vivek Dongre et al.
**Year:** 2024
**Venue:** arXiv
**Identifier:** arXiv:2411.00927
**Relevance:** Examines the coordination of reasoning and acting in LLM-based agents.

**Paper:** [ReSpAct paper](https://arxiv.org/abs/2411.00927?utm_source=chatgpt.com)

### 20. Mind2Web: Towards a Generalist Agent for the Web

**Authors:** Xiang Deng et al.
**Year:** 2023
**Venue:** NeurIPS 2023
**Relevance:** Provides a benchmark and dataset for generalist web agents operating across real-world websites.

**Paper and project:** [Mind2Web project](https://github.com/OSU-NLP-Group/Mind2Web?utm_source=chatgpt.com)

---

# Datasets

The following datasets/benchmarks are relevant to evaluating multi-step agentic systems.

### 1. AgentBench

AgentBench contains multiple environments for evaluating LLM agents, including operating systems, databases, knowledge graphs, games, web shopping, and web browsing. It is particularly useful for evaluating long-term reasoning and decision-making.

**Source:** [AgentBench GitHub](https://github.com/THUDM/AgentBench?utm_source=chatgpt.com)

### 2. Mind2Web

Mind2Web provides data, code, and models for studying generalist web agents. It contains human-demonstrated trajectories and supports evaluation of web interaction capabilities.

**Source:** [Mind2Web GitHub](https://github.com/OSU-NLP-Group/Mind2Web?utm_source=chatgpt.com)

### 3. ToolBench

ToolBench is a tool-use dataset containing instructions and reasoning traces involving thousands of real-world APIs. It is useful for studying tool selection, API use, and multi-tool reasoning.

**Source:** [ToolLLM GitHub](https://github.com/beijixiong1/ToolLLM?utm_source=chatgpt.com)

### Additional benchmark resources

* **WebArena** — realistic long-horizon web-agent evaluation environment.
* **GAIA** — general AI assistant benchmark involving reasoning, web browsing, and tool use.

---

# Tools and Libraries

## 1. LangChain

A framework for developing applications powered by language models, including retrieval, tool use, and agent workflows.

**Official:** [LangChain](https://www.langchain.com/?utm_source=chatgpt.com)

## 2. LlamaIndex

A framework for connecting LLM applications with external data and building retrieval-based workflows.

**Official:** [LlamaIndex](https://www.llamaindex.ai/?utm_source=chatgpt.com)

## 3. AutoGen

An open-source framework for building applications using multiple interacting agents, tools, and human inputs.

**Official:** [AutoGen](https://github.com/microsoft/autogen?utm_source=chatgpt.com)

## 4. CrewAI

A framework for orchestrating autonomous AI agents through collaborative crews and event-driven flows.

**Official:** [CrewAI](https://github.com/crewAIInc/crewAI?utm_source=chatgpt.com)

## 5. DSPy

A framework for programming and optimizing LM pipelines rather than manually constructing prompt chains.

**Official:** [DSPy GitHub](https://github.com/stanfordnlp/dspy?utm_source=chatgpt.com)

---

# GitHub Implementations

### 1. AgentBench

Implementation of the AgentBench evaluation framework and its environments.

**Repository:** [THUDM/AgentBench](https://github.com/THUDM/AgentBench?utm_source=chatgpt.com)

### 2. Mind2Web

Dataset, code, and models for generalist web agents.

**Repository:** [OSU-NLP-Group/Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web?utm_source=chatgpt.com)

### 3. SELF-RAG

Original implementation of the Self-RAG retrieval, generation, and self-reflection framework.

**Repository:** [AkariAsai/self-rag](https://github.com/AkariAsai/self-rag?utm_source=chatgpt.com)

### 4. DSPy

Implementation of the DSPy framework for programming and optimizing language-model pipelines.

**Repository:** [Stanford NLP DSPy](https://github.com/stanfordnlp/dspy?utm_source=chatgpt.com)

### 5. CrewAI

Implementation of a multi-agent automation framework supporting collaborative agents and workflow orchestration.

**Repository:** [CrewAI GitHub](https://github.com/crewAIInc/crewAI?utm_source=chatgpt.com)

### Additional implementations

* **MetaGPT** — multi-agent framework based on structured roles and workflows.
* **SWE-agent** — autonomous software-engineering agent using a custom agent-computer interface.
* **ToolLLM** — implementation for tool learning and API-based agents.
* **WebArena** — implementation of a self-hostable web-agent environment.

---

# Tutorials and Learning Resources

### 1. AgentBench Documentation

Useful for understanding how agent evaluation environments and benchmarks are structured.

**Resource:** [AgentBench GitHub and documentation](https://github.com/THUDM/AgentBench?utm_source=chatgpt.com)

### 2. CrewAI Getting Started

Provides practical guidance for creating and orchestrating AI agents using CrewAI.

**Resource:** [CrewAI documentation](https://docs.crewai.com/?utm_source=chatgpt.com)

### 3. MetaGPT Getting Started

Introduces the setup and use of MetaGPT for multi-agent workflows.

**Resource:** [MetaGPT Getting Started](https://docs.deepwisdom.ai/en/guide/getting-started.html?utm_source=chatgpt.com)

### 4. DSPy Documentation

Provides practical information about programming, composing, and optimizing language-model pipelines.

**Resource:** [DSPy GitHub documentation](https://github.com/stanfordnlp/dspy?utm_source=chatgpt.com)

### 5. WebArena Documentation

Provides setup and evaluation information for a realistic web-agent environment.

**Resource:** [WebArena GitHub](https://github.com/web-arena-x/webarena?utm_source=chatgpt.com)

### 6. LLM Agent Evaluation and Benchmarks

Provides an overview of agent evaluation concepts including long-horizon tasks, benchmark design, and evaluation harnesses.

**Resource:** [Agent Evaluation and Benchmarks](https://llmbook.icsgen-ai.org/part-6-agentic-ai/module-26-ai-agents/section-26.4.html?utm_source=chatgpt.com)

---

# Research Challenges

Several major challenges are identified in the research paper.

### Lack of Standard Error-Propagation Metrics

Existing agent benchmarks provide information about task success and agent performance, but standardized measures for error propagation across complete research workflows remain limited.

Potential metrics include:

* Stage Error Rate
* Propagation Rate
* Amplification Factor
* Recovery Rate
* Undetected Error Rate
* Claim-Support Accuracy

### Causal Attribution

When a final research report is incorrect, identifying the original cause can be difficult because the error may originate from planning, retrieval, source selection, extraction, reasoning, memory, or synthesis.

### Long-Horizon Reliability

Long research workflows increase the importance of state management, intermediate verification, and recovery mechanisms.

### Verification Dependence

An LLM-based verification system can reproduce the same biases or reasoning failures as the system it evaluates. Independent evidence is therefore important.

### Reproducibility

Research agents should preserve search queries, source identifiers, retrieval dates, retrieved evidence, model/version information, tool outputs, and important intermediate decisions.

---

# Research Gaps and Future Directions

The research paper identifies several important directions for future work.

### 1. Workflow-Level Benchmarks

Future benchmarks should evaluate complete research workflows instead of isolated agent capabilities.

### 2. Causal Error Tracing

Systems should identify where an error originated and determine which downstream outputs were affected.

**Error lineage:**

**Initial Error → Affected Intermediate Results → Affected Claims → Affected Conclusions**

### 3. Independent Multi-Agent Verification

Independent verification should use separate prompts, separate evidence retrieval, primary sources, different reasoning paths, and explicit disagreement mechanisms.

### 4. Evidence-Centered Generation

Rather than generating claims and attaching citations afterward, future systems should use:

**Retrieve → Verify → Extract Evidence → Construct Claim → Cite**

### 5. Uncertainty-Aware Research Agents

Agents should explicitly represent different confidence levels such as:

* Verified
* Strongly supported
* Partially supported
* Uncertain
* Unsupported

### 6. Human-AI Collaborative Research

The research paper argues that controlled autonomy may be more reliable than unrestricted autonomy, with AI handling repetitive tasks while humans retain responsibility for interpretation and important decisions.

---

# Key Error Propagation Chain

A central concept of this repository is the propagation of errors through dependent workflow stages.

**Wrong Source → Wrong Summary → Wrong Synthesis → Unsupported Conclusion**

An error that begins as a retrieval or source-selection problem can therefore become a research-level claim after passing through summarization, synthesis, citation, and report generation.

A final report may contain genuine sources and fluent academic writing while still answering the wrong research question. Therefore, citation authenticity alone is not sufficient for research reliability.

---

# References from the AI-Assisted Research Paper

1. Yao, S. et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. arXiv:2210.03629.
2. Shinn, N. et al. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. arXiv:2303.11366.
3. Liu, X. et al. (2024). *AgentBench: Evaluating LLMs as Agents*. ICLR 2024. arXiv:2308.03688.
4. Schick, T. et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. arXiv:2302.04761.
5. Wang, G. et al. (2023). *Voyager: An Open-Ended Embodied Agent with Large Language Models*. arXiv:2305.16291.
6. Dongre, V. et al. (2024). *ReSpAct: Harmonizing Reasoning, Speaking, and Acting Towards Building Large Language Model-Based Conversational AI Agents*. arXiv:2411.00927.
7. Zhou, S. et al. (2024). *WebArena: A Realistic Web Environment for Building Autonomous Agents*. ICLR 2024.
8. Deng, X. et al. (2023). *Mind2Web: Towards a Generalist Agent for the Web*. NeurIPS 2023.
9. Qin, Y. et al. (2023). *ToolLLM: Facilitating Large Language Models to Master 16,000+ Real-World APIs*. arXiv:2307.16789.
10. Yao, S. et al. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. NeurIPS 2023.

## The original paper contains these ten references.

# License

This repository is intended for academic and educational purposes.

Original student-created documentation, analysis, and other original repository content may be distributed under the selected open-source license.

Research papers and other copyrighted materials created by third parties should not be uploaded unless redistribution is permitted. Where possible, link to the publisher, DOI, arXiv, official project page, or authorized open-access source instead.

---

## Repository Structure

```text
awesome-agentic-ai-error-propagation/
│
├── README.md
│
├── paper/
│   └── AI_Assisted_Research_Paper.pdf
│
├── citation-audit/
│   └── Citation_Integrity_Audit.pdf
│
├── references/
│   └── references.md
│
├── datasets/
│   └── datasets.md
│
├── tools/
│   └── tools.md
│
├── implementations/
│   └── github-repositories.md
│
└── LICENSE
```

---

## Repository Requirements Checklist

* [x] Public GitHub repository
* [x] README.md
* [x] Topic overview
* [x] AI-assisted research paper
* [x] Citation-integrity audit section
* [x] 20 curated research papers
* [x] 3+ datasets
* [x] 5+ tools/libraries
* [x] 5+ GitHub implementations
* [x] 5+ tutorials/learning resources
* [x] Research challenges
* [x] Research gaps and future directions
* [x] License section
* [ ] Add your final GitHub repository URL
* [ ] Make at least 5 meaningful commits
