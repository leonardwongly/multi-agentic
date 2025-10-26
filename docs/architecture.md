# System Architecture

## Overview
The project implements a multi-agent support workflow orchestrated with [LangGraph](https://github.com/langchain-ai/langgraph). Three specialised agents collaborate to intake customer requests, query an FAQ knowledge base, and deliver a final resolution message.

## Components
- **Agents**
  - `IntakeAgent`: summarises customer input into a structured problem statement.
  - `KnowledgeAgent`: searches a YAML FAQ store using fuzzy matching and proposes a solution.
  - `ResolutionAgent`: produces the final response and marks the workflow as complete.
- **Tools**
  - `FAQTool`: loads and searches the FAQ knowledge base stored in `src/multi_agentic/data/faq.yml`.
- **LLM Abstraction**
  - `MockLLM`: deterministic templates for unit tests and offline experimentation.
- **Workflow**
  - `SupportWorkflow`: `langgraph` state machine chaining agents in sequence. The workflow is compiled once during initialisation and invoked for each conversation.

## Data Flow
1. `SupportWorkflow.run` receives one or more user messages and builds a `TicketState` with LangChain message objects.
2. The state graph routes the state through each agent:
   - Intake agent summarises the issue.
   - Knowledge agent queries the FAQ tool and enriches the state with a candidate solution.
   - Resolution agent formats a user-facing message and marks the state as finished.
3. The completed state is returned, including the conversation history and proposed resolution.

## Logging & Telemetry
Python's `logging` module records workflow start/end events and each agent's output. This provides lightweight observability without introducing external services.

## Extensibility
- Swap `MockLLM` for a real OpenAI-powered implementation by providing a class conforming to `LanguageModel`.
- Add new tools (e.g., ticketing system lookup) and extend the graph with additional nodes.
- Incorporate conditional routing in LangGraph to handle escalations or fallback flows.
