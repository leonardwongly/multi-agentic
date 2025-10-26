# Multi-Agent Support Workflow

This project implements a deterministic multi-agent support workflow using [LangGraph](https://github.com/langchain-ai/langgraph). It demonstrates how specialised agents collaborate to process a help-desk inquiry end to end.

## Project Structure

```
.
├── demo/                  # Sample transcripts and scripted scenarios
├── docs/                  # Architecture and design documentation
├── src/multi_agentic/     # Application source code and workflow definition
├── tests/                 # Automated test suite
├── pyproject.toml         # Project metadata and dependencies
└── .env.example           # Environment variable template
```

## Features
- Three collaborating agents (`Intake`, `Knowledge`, `Resolution`) managed by a LangGraph workflow.
- FAQ search tool backed by a YAML knowledge base.
- Mock LLM templates for deterministic behaviour during testing.
- Typer-based CLI for running demo conversations.
- Pytest coverage for key workflow scenarios.

## Prerequisites
- Python 3.11+
- `uv` or `pip` for dependency management.

## Setup
1. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\\Scripts\\activate`
   ```
2. **Install dependencies**
   ```bash
   pip install -e .[dev]
   ```
3. **Configure environment variables (optional)**
   ```bash
   cp .env.example .env
   # Populate OPENAI_API_KEY if you plan to integrate a real language model
   ```

## Running the Demo
Execute the CLI command with a customer issue description:
```bash
python -m multi_agentic.cli demo --message "The printer on floor 3 is jammed again."
```
The command prints the final ticket state as JSON, including conversation history and the recommended resolution.

## Step-by-Step Testing Guide
1. **Ensure the virtual environment is active** (see Setup step 1).
2. **Install development dependencies** if not already done:
   ```bash
   pip install -e .[dev]
   ```
3. **Run the test suite with coverage**
   ```bash
   pytest --cov=multi_agentic --cov-report=term-missing
   ```
4. **Interpret results**
   - All tests should pass with exit code 0.
   - Coverage output lists exercised files; ensure the agent workflow modules appear in the report.

## Extending the Project
- Replace the `MockLLM` in `src/multi_agentic/factory.py` with a real OpenAI-powered implementation respecting the `LanguageModel` protocol.
- Add new nodes to `SupportWorkflow` for escalations, approvals, or ticket updates.
- Expand the knowledge base by editing `src/multi_agentic/data/faq.yml`.

## License
This repository is provided for educational purposes.
