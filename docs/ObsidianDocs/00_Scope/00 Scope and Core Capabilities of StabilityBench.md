# What is StabilityBench?
StabilityBench is a benchmark that measures how stable or unstable a large language model is when:

* given the **same prompt repeatedly**,
* given **multiple rewritten versions** of the same prompt,
* performing **different type of tasks**,
* or when comparing **different models**.

It quantifies how consistent model behaviour is.

---
# What exactly are we measuring?
We measure behavioural stability:
>*"If I send the **same input** to a model **N times (20-100)**, how similar are the output?"*

This includes:
* whether answers match,
* whether the meaning stays the same,
* whether the reasoning changes,
* how much answer drift across the trials.

StabilityBench introduces metrics to capture this.

---
# Stability Dimensions (Axes)

## Run-to-run Stability (OG)
Same prompt -> ask model 20-100 times -> measure variation.

Questions answered:
* Does the model keep changing its mind?
* Are outputs semantically consistent?

## Prompt-Perturbation Stability (needs confirmation/more work - chatgptfied)
Same meaning -> different wording -> measuring consistency.

Examples:
* paraphrasing
* reordering
* adding harmless details
* removing filler words

Questions answered:
* Does the model give the same meaning, even when the prompt changes?
* Do small wording changes break its reasoning?

## Task-Type Stability
We test whether some task are **naturally more stable.**

Initial task categories:
* **Short Factual Q&A**
*  **MCQ**
* **Summarization**
* **Text refinement**
* **Reasoning / inference / multi step logic**
* (Optional later: math, long-form)

Questions answered:
* Is reasoning more unstable than factual Q&A?
* Is summarisation more variable than rewrite tasks?

---
# Cross-Model Stability Comparison (Funding Based)

StabilityBench compares:

**API Models *(Future Work - dependant credit based funding)*** 
* GPT-4o
* Claude 3.5
* Gemini 1.5

**Local / Open Models (Used in the module)**
* Llama 3
* DeepSeek
* Mistral
* (via Ollama or vLLM)

Questions answered:
* Do different **open-source models** show different levels of run-to-run stability?
- Are some model families (e.g., Llama vs DeepSeek) more consistent across tasks?
- Does the **task type** influence stability differently for different models?
- *(Future)* How do open-source models compare to **frontier API models** once funding allows?

---
# How will we measure stability? (High-Level Only)

We use multiple metric families:

**Agreement-Based (simple)**
* TAR (How often outputs agree)

**Semantic Similarity Based**
* Embedding clustering
- Cosine similarity variance

**Entropy-Based**
- Semantic Entropy
- Semantic Spectral Entropy (SSE) 
- Output distribution spread

**Structural Measures**
- Response length variance
- Format consistency

---
# MVP (First Version) Plan
To avoid exploding the project:
* - 3 task types (Q&A, summarisation, reasoning)
- 10 prompts per task
- 20 repetitions per prompt
- 1–2 models to start

Goal:
> End-to-end system working before scaling up.

---
# Reproducibility
All evaluations will run inside a **Docker container**, ensuring:
- identical environment,
- stable dependencies,
- repeatable experiments across machines.

---
# See Also

- See Also - [[01_Metrics]]

---

# End of Scope and Core Capabilities