"""
StabilityBench-lite

This module defines the conceptual meaning of "stability" in the context
of large language model (LLM) evaluation.

Stability refers to the consistency of model outputs under conditions
where the semantic intent of the prompt is unchanged.
"""

## What is stability?

# Stability = how much a model's output changes when it should not.
#
# More formally, stability is the degree to which an LLM produces
# consistent outputs when the semantic content and task intent of the
# input are held constant.

# Examples:
# - Same prompt, run multiple times: do answers drift?
# - Slightly reworded prompt with identical meaning: does behaviour change?
# - Same task and constraints: does structure, style, or conclusion vary?

## What varies?

# The primary source of variation is the model’s stochastic generation
# process across repeated runs of the same prompt under identical settings.

## What is held constant?

# The task intent, semantic meaning of the prompt, evaluation protocol,
# and experimental setup are held fixed within a given experiment.

## What is measured?

# Stability is measured as the degree of similarity or divergence between
# multiple outputs generated under identical or near-identical conditions.

## Unit of analysis

# The basic unit of analysis is a set of outputs generated from repeated
# executions of the same prompt under fixed experimental conditions.

## Out of scope

# This framework does not evaluate correctness, factual accuracy,
# usefulness, alignment, or creativity. It focuses solely on behavioural
# consistency.