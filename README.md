# MCP Developer Documentation Bot

A Python tool that scans Python codebases, extracts API details, and generates developer-friendly documentation in Markdown. It also includes a mocked MCP interface so you can ask interactive questions about functions, classes, and modules and produce example conversation logs.

This repository is intended as a reference implementation and starter kit for building documentation assistants powered by an MCP-like interface.

---

## Table of Contents
- [Features](#features)
- [Quick Demo](#quick-demo)
- [Installation](#installation)
- [Usage](#usage)
  - [Generate documentation](#generate-documentation)
  - [Interactive MCP session (mocked)](#interactive-mcp-session-mocked)
  - [PowerShell turnkey script](#powershell-turnkey-script)
- [Project Structure](#project-structure)
- [How it works](#how-it-works)
  - [Repository scanning & parsing](#repository-scanning--parsing)
  - [Documentation generation](#documentation-generation)
  - [MCP mock interface](#mcp-mock-interface)
- [Outputs / Examples](#outputs--examples)
- [Configuration & Requirements](#configuration--requirements)
- [Extending the bot](#extending-the-bot)
- [Contributing](#contributing)
- [License & Contact](#license--contact)

---

## Features

## Core
- Repository scanning: recursively finds .py files in a target directory.
- AST-based parsing: extracts functions, classes, method signatures, arguments and docstrings.
- Documentation generation: creates a project README and a detailed API document in Markdown using Jinja2 templates.
- Interactive MCP (mocked): a simple CLI server that answers questions about code elements and logs conversations.

## Planned
- Dependency mapping and visual graphs
- Diagram generation (UML/class diagrams)
- Multi-language docs and localization
- Versioned docs integrated with Git

---

## Quick demo

1. Generate docs for the example repo and inspect outputs:
   - python run.py tests/example_repo
   - Outputs are written to `sample_output/`

2. Start a mocked MCP interactive session:
   - python run_mcp_logging.py
   - Example queries: explain("add"), explain("Calculator")

---

## Installation

Requirements
- Python 3.8+
- pip

1. Clone
```bash
git clone https://github.com/<your-username>/mcp-doc-bot.git
cd mcp-doc-bot
```

2. (Optional) Create and activate a virtual environment
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Note: requirements.txt should include at least:
- jinja2

If you use extra features add packages like graphviz, pydot, or Sphinx.

---

## Usage

## Generate Documentation
```bash
python run.py <path-to-target-repo> [--out sample_output] [--templates templates/]
```
- Example:
  ```
  - python run.py tests/example_repo
  ```
- Primary outputs:
  ```
  - sample_output/README.md — generated project README
  - sample_output/api_docs.md — function/class API docs
  ```

## Interactive MCP session (mocked)
```bash
python run_mcp_logging.py
```
- Starts a CLI loop that accepts simple commands like:
  - explain("function_name")
  - explain("module.ClassName")
  - regenerate_docs()
- Logs are saved to `tests/results/mcp_conversation_log.txt` (or a configured path).

## PowerShell turnkey script
- run_bot.ps1 automates venv creation, dependency install, scanning and generating docs in one step:
```powershell
.\run_bot.ps1 -TargetPath "tests/example_repo"
```
(Adjust script parameters to suit your environment.)

---

## Project Structure

```
mcp-doc-bot/
│
├── bot/
│   ├── __init__.py
│   ├── scanner.py        # Repository crawler
│   ├── parser.py         # AST-based code analysis
│   ├── generator.py      # Jinja2-based docs generation
│   ├── mcp_server.py     # Mocked MCP interface / CLI
│
├── templates/
│   ├── readme_template.md
│   ├── api_template.md
│
├── sample_output/        # Example generated outputs
│   ├── README.md
│   ├── api_docs.md
│
├── tests/
│   ├── example_repo/     # Small demo repo used for tests
│   │   ├── simple_functions.py
│   │   ├── sample_class.py
│   ├── results/
│       └── mcp_conversation_log.txt
│
├── requirements.txt
├── run.py                # CLI entry: generate docs
├── run_mcp_logging.py    # Run mocked MCP and write logs
├── run_bot.ps1           # Windows convenience script
└── README_submission.md  # Optional submission notes
```

---

## How it works

## Repository scanning & parsing
- scanner.py traverses a target directory and lists Python files.
- parser.py uses Python's AST module to parse each file, extracting:
  - function & method names, arguments (including defaults and annotations)
  - class definitions and their methods
  - top-level docstrings and inline docstrings
- Parser outputs a structured representation (JSON/dict) that generator.py consumes.

## Documentation generation
- generator.py renders Jinja2 templates into Markdown:
  - A README with project overview, install steps, and top-level module summaries.
  - API docs listing modules, classes, functions, signatures, and docstrings.
- Templates live in templates/ for easy customization.

## MCP mock interface
- mcp_server.py is a simplified MCP-like CLI server:
  - Loads the last scan index into memory.
  - Accepts human-like commands and returns helpful summaries.
  - Writes session logs to tests/results/*.txt to demonstrate conversations.

---

## Outputs / Examples

- sample_output/README.md
  - Project summary, how to run, and a short examples section.

- sample_output/api_docs.md
  - Organized by module with:
    - Function signatures and docstrings
    - Class definitions, constructors, and method summaries
    - Example usage snippets when docstrings contain examples

- tests/results/mcp_conversation_log.txt
  - A sample conversation showing explain("add") and explain("Calculator") responses

Include these sample outputs in your submission to show the bot's capabilities.

---

## Configuration & Requirements

- Python version: 3.8+
- Recommended packages (requirements.txt):
  - jinja2
  - (optional) graphviz, pydot, sphinx for advanced features
- Cross-platform: Windows, macOS, Linux
- If running in constrained environments (CI), provide a smaller target path to speed scanning.

---

## Extending the bot

## Ideas to add:
- Diagram generation: integrate graphviz to draw class/module dependency graphs.
- Sphinx output: convert generated Markdown to reStructuredText and build HTML docs.
- Git integration: detect changes and only regenerate docs for modified modules.
- Natural language improvements: replace mock MCP with a live MCP client/SDK to answer more natural queries.

If you add features, please:
- Add tests under tests/
- Update templates/
- Document usage in README_submission.md

---

## Contributing

1. Fork the repo
2. Create a feature branch (feature/your-feature)
3. Write tests and update docs
4. Open a PR describing the change and motivation

Please keep changes focused (one feature/bugfix per PR) and include examples for generated docs.

---

## License & Contact

This project is provided "as-is" for educational and prototyping purposes and MIT LICENSED.

## Author
Shailja

---

## Acknowledgements
- Built with Python's AST module and Jinja2 for templating.
- Inspired by approaches to automated code documentation and developer-assist tools.

