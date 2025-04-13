# MCP Server Generator

This directory contains the Node.js implementation of the MCP Server Generator CLI tool. It generates customized MCP (Model Context Protocol) servers based on natural language project descriptions.

## Structure

- `bin/`: Contains the CLI entry point
- `src/`: Contains the source code for the generator
  - `analyzer/`: Project analyzer component
  - `cli/`: CLI interface component
  - `generator/`: Code generator component
  - `llm/`: LLM interaction service component
  - `registry/`: MCP registry component
  - `utils/`: Shared utilities
- `templates/`: Contains templates for generated code
- `data/`: Contains data files for the registry
- `docs/`: Contains documentation

## Usage

```bash
# Install dependencies
cd mcp-generator
npm install

# Run the CLI tool
node bin/generate-mcp-server.js
```
