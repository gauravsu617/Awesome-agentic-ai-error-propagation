# Tools and Libraries

This page retains the five curated engineering frameworks and adds the four literature-discovery tools evaluated in the supplied FINAL ATR workbook. These are separate categories: frameworks help implement agent workflows; discovery tools help locate and synthesize research literature.

## A. Five engineering frameworks retained in the curated list

### 1. LangChain
**Purpose:** LLM application and agent development.  
**Official website:** https://www.langchain.com/  
**GitHub:** https://github.com/langchain-ai/langchain

### 2. LlamaIndex
**Purpose:** Data and retrieval integration for RAG/agent workflows.  
**Official website:** https://www.llamaindex.ai/  
**GitHub:** https://github.com/run-llama/llama_index

### 3. LangGraph
**Purpose:** Stateful, graph-based agent orchestration and human-in-the-loop control.  
**Official website:** https://www.langchain.com/langgraph  
**GitHub:** https://github.com/langchain-ai/langgraph

### 4. AutoGen
**Purpose:** Multi-agent application development.  
**GitHub:** https://github.com/microsoft/autogen  
**Reference paper:** https://arxiv.org/abs/2308.08155

### 5. DSPy
**Purpose:** Programming and optimization of language-model pipelines.  
**GitHub:** https://github.com/stanfordnlp/dspy  
**Reference paper:** https://arxiv.org/abs/2310.03714

## B. Literature-discovery and synthesis tools evaluated in FINAL ATR

Ratings below reproduce the values in `Lab4_Literature_List_and_Tool_Tables.xlsx`. They are the workbook author's recorded ratings, not an independent universal benchmark.

| Criterion (1â€“5) | ResearchRabbit | Litmaps | Semantic Scholar | Elicit |
|---|---:|---:|---:|---:|
| Ease of use | 4 | 4 | 5 | 4 |
| Relevance of discovered literature | 2 | 2 | 4 | 5 |
| Topic coverage | 3 | 3 | 4 | 2 |
| Discovery of recent research | 5 | 4 | 4 | 4 |
| Discovery of foundational research | 3 | 4 | 4 | 2 |
| Discovery of less obvious related work | 4 | 4 | 3 | 2 |
| Identifying themes | 3 | 4 | 2 | 5 |
| Comparing papers | 2 | 2 | 2 | 5 |
| Identifying research gaps | 2 | 2 | 2 | 5 |
| Quality of literature-review input | 2 | 2 | 4 | 4 |
| Overall usefulness | 3 | 3 | 4 | 4 |
| **Average rating recorded in workbook** | **3.00** | **3.09** | **3.45** | **3.82** |

Links:
- ResearchRabbit: https://www.researchrabbit.ai/
- Litmaps: https://www.litmaps.com/
- Semantic Scholar: https://www.semanticscholar.org/
- Elicit: https://elicit.com/

### How the supplied workbook says the tools were used

- **ResearchRabbit:** a seed collection of two papers and a â€œSimilar articlesâ€ map; approximately 20 nodes, mostly labelled 2025â€“2026. No new paper was added from the map because relevance was not confirmed.
- **Litmaps:** a citation timeline around one 2026 seed; approximately 12 labelled nodes spanning 2020â€“2026. Used for orientation, not as standalone evidence.
- **Semantic Scholar:** four targeted searches on multi-agent failure, automated failure attribution, propagation-aware uncertainty, and fault injection. The workbook says two papers were added and three held out pending verification.
- **Elicit:** structured comparison query on where errors originate/propagate and how they are measured/mitigated. It surfaced two closely related 2025 papers, but the workbook warns that the report's coverage is narrow and figure claims need checking in the primary paper.

Recorded prompts and queries are in [Prompts_and_Search_Queries.txt](../atr-submission/Prompts_and_Search_Queries.txt). Citation status is summarized in [the citation verification audit](../citation/Citation_Verification_Audit.md).

## Tool selection guidance for this project

Use Semantic Scholar and publisher/preprint records for source discovery and bibliographic checks; use Elicit for structured comparison only as a secondary aid; use ResearchRabbit and Litmaps for discovery maps. Claims should be verified in the primary paper, and AI/search summaries should not substitute for checking the cited evidence.

