# Datasets and Benchmarks

This repository includes exactly three datasets/benchmarks relevant to agentic AI, tool use, web interaction, and multi-step workflows.

## 1. AgentBench

**Type:** Agent evaluation benchmark

**Description:**
AgentBench is a benchmark for evaluating large language models as agents across multiple interactive environments. It is useful for studying reasoning, decision-making, and long-horizon agent behavior.

**Use in this topic:**
AgentBench can be used to evaluate whether errors accumulate during multi-step agent interactions.

**Repository:**
https://github.com/THUDM/AgentBench

**Paper:**
https://arxiv.org/abs/2308.03688

---

## 2. Mind2Web

**Type:** Web-agent dataset and benchmark

**Description:**
Mind2Web provides data and evaluation resources for developing generalist web agents. It contains human-demonstrated web interaction trajectories and supports research on web-based agent behavior.

**Use in this topic:**
The multi-step web interaction setting makes it useful for studying errors in action selection, tool use, and long-horizon workflows.

**Repository:**
https://github.com/OSU-NLP-Group/Mind2Web

**Paper:**
https://arxiv.org/abs/2306.06070

---

## 3. ToolBench

**Type:** Tool-use dataset and benchmark

**Description:**
ToolBench is designed for studying language models that interact with real-world APIs and tools. It contains tasks involving tool selection and multi-step API use.

**Use in this topic:**
ToolBench can support research into tool-selection errors, incorrect API calls, and downstream error propagation.

**Repository:**
https://github.com/OpenBMB/ToolBench

**Paper:**
https://arxiv.org/abs/2307.16789

---

## Dataset Selection Rationale

These three resources represent complementary aspects of agentic workflows:

| Dataset    | Main Focus       | Error-Propagation Relevance         |
| ---------- | ---------------- | ----------------------------------- |
| AgentBench | Agent evaluation | Multi-step decision errors          |
| Mind2Web   | Web interaction  | Action and navigation errors        |
| ToolBench  | Tool/API use     | Tool-selection and execution errors |

No dataset files are redistributed in this repository. Users should obtain datasets from their official sources and follow their respective licenses and terms of use.
