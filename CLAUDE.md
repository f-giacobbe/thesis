# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Research Context

This is a thesis project investigating whether LLM agents exhibit bias in hiring/lending decisions. The core experiment: an AI "recruiter" makes a blind decision based only on technical qualifications, then is shown demographic information (ethnicity, gender, political beliefs) — does the agent flip its decision? The goal is a matrix of outcomes across different recruiter backgrounds × candidate backgrounds combinations. Target models for comparison are Gemma (Google, Western safety filters) and Qwen (Alibaba, different cultural dataset). Temperature should be ~0.3 (near-deterministic) for reproducibility.

## Project Structure

The repo contains two independent subprojects, each with its own virtualenv:

- **`mcdonalds_crew/`** — Early prototype using a simple Crew (type: `"crew"`). A McDonald's worker argues for a raise. Useful as a minimal working example.
- **`sample_flow/`** — The active thesis experiment using a Flow (type: `"flow"`). Two HR specialists with different backgrounds debate a candidate's CV.

Each subproject is self-contained with its own `pyproject.toml`, `.venv`, and `.env`.

## Running the Projects

All commands must be run from within the respective project directory (`cd sample_flow` or `cd mcdonalds_crew`).

```bash
crewai run          # Execute the crew or flow
crewai flow plot    # Generate flow diagram HTML (flows only)
crewai install      # Install/sync dependencies via uv
```

## sample_flow Architecture

The main experiment. Flow pipeline: `pull_cv` → `cv_review` → `save_content`.

- **`HrState`** (Pydantic): holds `cv_file`, `cv` (extracted text), `debate` (output).
- **`HrFlow`**: reads `input/cv.pdf` via pypdf, kicks off `HrCrew`, saves result to `output/debate.md`.
- **`HrCrew`**: sequential crew with two agents (`hr_specialist1`, `hr_specialist2`) running three tasks: initial review → debate → final reconciliation.
- **LLM config**: reads `MODEL`, `OPENAI_API_BASE`, and `OPENAI_API_KEY` from `.env` — uses the OpenAI-compatible API so any provider (Ollama, LM Studio, etc.) works by setting `OPENAI_API_BASE`.

Agent personas and task prompts are defined in `src/sample_flow/crews/hr_crew/config/agents.yaml` and `tasks.yaml`.

## Environment Variables (`.env`)

```
MODEL=<model-name>          # e.g. "gemma3:27b" or "qwen2.5:72b"
OPENAI_API_BASE=<url>       # e.g. "http://localhost:11434/v1" for Ollama
OPENAI_API_KEY=<key>        # can be a dummy value for local models
```

## CrewAI Reference

Both projects contain an `AGENTS.md` with a full CrewAI API reference (patterns, YAML config, flow decorators, common pitfalls). Always check that file before writing CrewAI code — it supersedes training data. Key rule: always use `crewai.LLM` or string shorthand (`"provider/model"`), never `ChatOpenAI`.
