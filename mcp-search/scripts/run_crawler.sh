#!/bin/bash
# Script to run the Vertex AI docs crawler

# Activate the Python virtual environment
source .mcp-cli/bin/activate

# Run the crawler script
python vertex_ai_docs_crawler.py

echo "Crawler script execution complete!"