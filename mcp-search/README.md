# MCP Search for MCP Servers

This directory contains Python tools for creating a semantic search layer for MCP servers. It includes scripts for crawling documentation and implementing semantic search functionality.

## Setup

```bash
# Activate the Python virtual environment
source .mcp-cli/bin/activate

# Install dependencies (if not already installed)
pip install -r requirements.txt
```

## Usage

### Documentation Crawler

```bash
# Crawl documentation from URLs in docs_url.txt
python vertex_ai_docs_crawler.py
```

### Semantic Search

```bash
# Run semantic search in interactive mode
python semantic_search.py

# Search with a specific query
python semantic_search.py --query "create github issue"
```

See the README.md file in this directory for more detailed instructions.
