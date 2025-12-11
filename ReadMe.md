# StabilityBench

StabilityBench is an open-source benchmark for analysing and quantifying stability in large language models.

## Overview

StabilityBench is an evaluation framework that measures the **behavioural stability** of large language models (LLMs). Rather than asking "How accurate is the model?", it asks: **"How consistent is the model when nothing changes?"**

LLMs often produce variable outputs for identical prompts. StabilityBench quantifies this variability across:

- Repeated generations (run-to-run stability)
- Reworded prompts with identical meaning (prompt perturbation stability)
- Different task categories (task-type stability)
- Different model families (open-source and API-based models)

## Purpose

This framework provides a **systematic, statistically grounded** approach to evaluate LLM consistency and identify stability patterns:

- Does a model produce consistent answers when prompted repeatedly?
- Does stability vary by task type (e.g., factual Q&A vs reasoning)?
- Do different models exhibit different stability profiles?
- How can we quantify semantic, structural, and distributional variability?

Currently supports open-source models (Llama, DeepSeek, Mistral) with planned integration of API models (GPT-4o, Claude, Gemini).

## Repository Structure

```
StabilityBench/
├── docs/ObsidianDocs/          # Documentation and design notes
├── src/                         # Implementation (in development)
├── data/                        # Datasets and prompts
├── results/                     # Experiment outputs
├── Dockerfile                   # Reproducible environment (planned)
└── README.md
```

## Key Concepts

**Run-to-Run Stability:** Output consistency when repeating the exact same prompt N times.

**Prompt Perturbation Stability:** Model behavior when prompts are paraphrased but retain meaning.

**Task-Type Stability:** Stability variation across task categories (factual Q&A, MCQ, summarization, text refinement, reasoning).

**Cross-Model Stability:** Comparison across open-source and API-based models.

## Metrics

StabilityBench includes metric families defined in `docs/ObsidianDocs/01_Metrics.md`:

- Agreement-based metrics
- Semantic similarity metrics
- Clustering and dispersion metrics
- Entropy-based metrics (Semantic Entropy, SSE)
- Structural variability metrics

## Development Status

**Currently implemented:**
- Repository structure
- Documentation vault
- Scope and metric definitions

**Next steps:**
- Define task prompts
- Implement generation runner
- Implement metric computation
- Experiment on open-source models
- Add Docker support

## Future Work

- API model integration (GPT-4o, Claude, Gemini)
- Expanded task collections
- Statistical test suite
- Visualization tools
- Leaderboards and report templates

## Contact

**Maintainer:** Neelabh Sinha  
UCL MSc Data Science – StabilityBench Project

© 2024 Neelabh Sinha. All rights reserved.
