# 01 — Stability Metrics (Definitions and Purpose)

StabilityBench uses multiple metric families to quantify how consistent or inconsistent a model’s outputs are across repeated trials, across prompt variations, and across task types.

Metrics fall into four categories:
1. Agreement-based
2. Semantic similarity-based
3. Entropy-based
4. Structural variability

Each metric provides a different perspective on stability.

---

## 1. Agreement-Based Metrics

### 1.1 TAR (Total Agreement Rate)
**Definition:**  
The proportion of repeated outputs that are *exactly identical* (string match) or have the same parsed answer (for MCQ/Q&A).

**Why it matters:**  
- Provides a simple baseline.
- Easy to compute.
- Useful for factual Q&A or MCQ.
- Breaks down quickly for long-form generation (which is expected).

**Output:**  
A value between 0 and 1.

---

## 2. Semantic Similarity-Based Metrics

### 2.1 Embedding Similarity Variance
**Definition:**  
Take embeddings of repeated outputs → compute pairwise cosine similarities → measure the variance of these values.

**Why it matters:**  
- Captures meaning drift even when surface text differs.
- Identifies subtle instability not visible in raw agreement.

---

### 2.2 Clustering Dispersion
**Definition:**  
Cluster repeated outputs using embeddings (e.g., k-means or HDBSCAN).  
Measure:
- number of clusters,
- cluster size imbalance,
- distance between clusters.

**Why it matters:**  
- Shows whether outputs form one semantic mode or multiple competing interpretations.

---

## 3. Entropy-Based Metrics

Entropy measures how “spread out” or “uncertain” the model’s output distribution is.

### 3.1 Semantic Entropy (SE)
**Definition (high-level):**  
Use a semantic similarity model (or NLI model) to group outputs with similar meaning, then compute Shannon entropy over cluster membership.

**Why it matters:**  
- Higher entropy = more instability.
- Captures semantic variation rather than surface variation.

---

### 3.2 Semantic Spectral Entropy (SSE)
**Definition (high-level):**  
Use a spectral clustering approach over an equivalence graph of outputs.  
Entropy is computed over the spectral cluster distribution.

**Why it matters:**  
- More robust to noise.
- Theoretically grounded (recent 2025 paper).
- Excellent metric for open-ended tasks.

---

## 4. Structural Variability Measures

### 4.1 Response Length Variance
**Definition:**  
Variance of output lengths (number of tokens or characters).

**Why it matters:**  
- Models often respond with wildly different verbosity.
- Useful especially for summarisation tasks.

---

### 4.2 Format Consistency
**Definition:**  
Measure how often the structure changes:
- bullet points vs paragraph
- ordering of sections
- presence/absence of reasoning chains

**Why it matters:**  
- Helps detect stylistic instability.

---

## 5. Metric Summary Table

| Metric | Category | Strength | Weakness |
|-------|----------|----------|----------|
| TAR | Agreement | Simple; good for MCQ | Breaks for long outputs |
| Cosine Variance | Similarity | Captures semantic drift | Depends on embedding quality |
| Cluster Dispersion | Similarity | Reveals multi-modality | Requires parameter tuning |
| Semantic Entropy | Entropy | Meaning-level variability | Requires similarity model |
| Spectral Entropy (SSE) | Entropy | Robust; theoretically sound | More complex to compute |
| Length Variance | Structural | Fast diagnostic | Doesn’t capture meaning |
| Format Consistency | Structural | Good for CoT | Hard to formalise |

---

## 6. MVP Metric Set (Module Version)
The first version of StabilityBench will implement:

- TAR  
- Embedding Similarity Variance  
- Semantic Entropy  
- Length Variance  

SSE will be added next once base pipeline works.

---

## 7. Future Extensions
- Wasserstein distance between output embeddings  
- KL divergence over token distributions  
- Chain-of-thought divergence metrics  
- Task-normalised stability scores  
- Model calibration against temperature changes

---

# End of Metrics Specification
