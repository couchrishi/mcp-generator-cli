# MCP Search Project - Decision Log

## Technical Decisions

[2025-04-13 17:22:40] - **Selection of Google Vertex AI Search**
- Decision: Use Google Vertex AI Search as the search backend
- Rationale: 
  - Provides managed search infrastructure with minimal setup
  - Supports structured data and complex filtering
  - Offers AI-powered relevance and ranking
  - Integrates well with other Google Cloud services
- Implications:
  - Requires Google Cloud project and billing
  - Schema design must conform to Vertex AI Search capabilities
  - Application is tied to Google Cloud ecosystem

[2025-04-13 17:22:40] - **API Structure**
- Decision: Implement multiple API layers (debug, simple, full)
- Rationale:
  - Debug API provides visibility into raw data structures
  - Simple API offers straightforward search functionality
  - Full API delivers comprehensive, structured results
- Implications:
  - Maintainability of multiple API implementations
  - Consistent underlying search mechanisms
  - Flexibility for different use cases

[2025-04-13 17:22:40] - **Schema Design**
- Decision: Include security assessment data in the search schema
- Rationale:
  - Enables filtering and ranking based on security metrics
  - Provides valuable context for MCP server selection
  - Allows for security-aware search functionality
- Implications:
  - Requires integration with security scanning tools
  - Adds complexity to the schema
  - Increases data preparation requirements

[2025-04-13 17:25:44] - **Advanced Search Features Implementation**
- Decision: Implement advanced search API with pagination, facets, semantic search, and enhanced filtering
- Rationale:
  - Pagination enables handling large result sets efficiently
  - Faceted search provides better discovery and filtering capabilities
  - Semantic search improves results relevance for natural language queries
  - Enhanced filtering allows for more precise search results
- Implications:
  - More complex API surface but with greater flexibility
  - Additional Google Vertex AI features utilized (semantic search, facets)
  - Improved search results quality and user experience
  - Future integration with various frontend interfaces simplified

[2025-04-13 17:25:44] - **Type Hints Introduction**
- Decision: Use Python type hints in new code
- Rationale:
  - Improves code readability and maintainability
  - Provides better IDE support for developers
  - Helps catch type-related bugs earlier
  - Documents function interfaces more clearly
- Implications:
  - Slightly increased verbosity in function definitions
  - Better code documentation and IDE support
  - Gradual adoption approach (new code only)

[2025-04-14 01:52:40] - **Switch to Schema Auto-Detection**
- Decision: Use Vertex AI's schema auto-detection feature instead of uploading a custom schema.
- Rationale:
  - Persistent inconsistencies and missing data were observed when using the custom schema, even after recreating resources and verifying input data/scripts.
  - Auto-detection successfully inferred the correct schema from the NDJSON data, resolving the search result issues.
  - Avoids potential bugs or undocumented behavior related to custom schema updates/application in Vertex AI.
- Implications:
  - Less explicit control over schema details (e.g., specific indexing or faceting options for fields might rely on Vertex AI's inference).
  - Schema might drift if the structure of input data changes significantly over time without explicit management.
  - Requires ensuring the input NDJSON data structure is consistently correct.