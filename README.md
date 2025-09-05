# movie-agent-from-scratch

This small project is a study exercise in building an AI agent from scratch, without relying on external frameworks like LangChain or LangGraph.
The goal is to understand and implement the core components of an agent—routing, decision graphs, and tool execution—using only Python standard libraries and a few lightweight dependencies.

The agent uses a two-level router powered by an LLM to classify user prompts:
• Top router: decides if the input is about movies or not.
• Movie router: further routes to theater, streaming, or high-score recommendations.

Execution is handled through a simple directed acyclic graph (DAG) built with NetworkX, with each node mapped to a function executor. A small fake movie database (MOVIES_DB) is included for demo purposes.

Key points:
• No LangChain, LangGraph, or orchestration frameworks.
• Emphasis on clear modular code (executors, routers, agent, graph, client).
• Demonstrates how agents work under the hood, not just how to use them.
• Compatible with local models (e.g., LM Studio) or OpenAI-style APIs.

## Quickstart

1. Clone

```
git clone https://github.com/psdiaspedro42/movie-agent-from-scratch.git
cd movie-agent-from-scratch
```

2. Venv

macOS / Linux

```
python -m venv .venv
source .venv/bin/activate
```

Windows

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install requirements.txt

```
pip install -U pip
pip install -r requirements.txt
```

4. Config .env

```
cp .env.example .env
```

5. Runing

Mock prompts on cli.py

```
python -m src.cli
```

Own prompt

```
python -m src.cli "What movies are available on Netflix?"
```
