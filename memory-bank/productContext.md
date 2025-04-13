# MCP Search Project - Product Context

## Overview
The MCP (Model Context Protocol) Search project provides search capabilities for discovering and evaluating MCP servers. It leverages Google Vertex AI Search to index and retrieve MCP server information with enhanced relevance and filtering.

## Project Goals
- Create a searchable index of MCP servers and their capabilities
- Provide structured search results with relevant metadata
- Enable filtering and sorting of search results
- Expose search functionality through simple APIs
- Integrate security assessment information for MCP servers

## Components
1. **Corpus Builder**: Tools for creating and maintaining the MCP servers dataset
2. **Schema Generator**: Utilities for defining and generating the Vertex AI Search schema
3. **Vertex AI Setup**: Scripts for creating and managing the Vertex AI search infrastructure
4. **Search APIs**: Python-based APIs for searching and retrieving MCP server information

## Technical Architecture
- **Data Store**: Google Vertex AI Search data store for MCP server information
- **Search App**: Google Vertex AI Search application for handling search queries
- **API Layer**: Python-based API for interacting with the search infrastructure
- **Schema**: Structured schema defining MCP server metadata and attributes

## Integration Points
- **Vertex AI Search**: Primary search backend
- **MCP Server Registry**: Source of MCP server metadata
- **Security Scanning**: Integration with security assessment data

[2025-04-13 17:21:57] - Initial documentation of the MCP Search project.