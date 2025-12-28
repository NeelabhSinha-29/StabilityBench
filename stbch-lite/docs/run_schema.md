# Run Schema Documentation (StabilityBench-lite)

A **run** is one complete execution of the stability experiment:
**one prompt → N generations under fixed generation settings → stored outputs → derived stability metrics**.

The purpose of this schema is to ensure every run is **reproducible, comparable, and traceable**.

---

## Fields

### `run_id`
**Type:** string  
**Required:** yes  
A **globally unique** identifier for this run instance. Generated once per run and never changes. Used to reference the run across files/analysis.

---

### `timestamp`
**Type:** string (ISO 8601)  
**Required:** yes  
The date and time the run was initiated, recorded in **UTC**. Used for logging and ordering runs over time.

---

### `prompt`
**Type:** object  
**Required:** yes  
The input stimulus provided to the language model.

- `prompt_text` (string, required): The exact text sent to the model.
- `prompt_id` (string, optional but recommended): A stable identifier for the prompt (useful when you later add paraphrases or prompt sets).

---

### `model_name`
**Type:** string  
**Required:** yes  
The name/identifier of the language model used to generate outputs for this run (e.g., a local model name or an API model name). This is provenance information for comparing behaviour across models.

---

### `gen_parameters`
**Type:** object  
**Required:** yes  
All generation settings that can influence the output distribution. If changing a parameter could change the outputs, it must be recorded here.

Common examples (not exhaustive):
- `n_generations` (int): N, the number of outputs generated for this run.
- `temperature` (float)
- `top_p` (float) and/or `top_k` (int)
- `max_tokens` (int)
- `seed` / `seed_strategy` (string or int): how randomness is controlled across the N generations.

---

### `outputs`
**Type:** array of strings  
**Required:** yes  
An **ordered** list of generated outputs produced by the model for the given prompt under `gen_parameters`. The list length must equal `gen_parameters.n_generations`.

---

### `metrics`
**Type:** object (dictionary)  
**Required:** yes (can be empty initially)  
A dictionary of **derived** stability measurements computed from `outputs`. Metrics are computed **after** generation and can be added later without regenerating outputs.

Example entries:
- `unique_ratio`
- `mean_output_length`
- `pairwise_similarity_*` (if using embedding-based metrics later)

---

## Notes / Invariants

- Runs must save **raw outputs** before any metrics are computed.
- `outputs` are observational data; `metrics` are derived summaries.
- A run is reproducible only if `prompt`, `model_name`, and `gen_parameters` are fully recorded.
