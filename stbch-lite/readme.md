# StabilityBench Lite

## What Problem Are We Exploring?

How stable are LLM outputs? When you ask the same question (or slightly different versions of it) multiple times, how much do the answers vary? This project measures output stability under repeated and perturbed prompts — understanding whether an LLM gives consistent, reliable responses or wildly different ones.

## What Is the Smallest Unit of Work?

One prompt → N generations → stability score

Take a single prompt, generate multiple outputs from the same model, measure how similar or different those outputs are, and produce a stability score. That's one complete unit. Everything builds from there.

## What Does "Lite" Mean Here?

- **Single-machine**: No distributed processing or cloud infrastructure required
- **Small models and APIs**: Designed for local models or lightweight API access, not massive parameter counts
- **Few metrics**: A focused set of stability metrics, not comprehensive evaluation suites

This is an experiment, not a production system.

## What Is Explicitly Out of Scope?

- No model training or fine-tuning
- No leaderboard or comparative rankings
- No massive prompt sets or benchmarks
- No infrastructure for running at scale

We're exploring the concept with real constraints. If you need production-grade evaluation, this isn't it.

---

**This README is intent, not documentation.** Come back here when adding major features and make sure they still fit the scope.
