# MCP Search Project - System Patterns

## Architectural Patterns

### Search Pipeline Architecture
[2025-04-13 17:22:26] - The project uses a pipeline architecture for search processing:
1. Data Collection (corpus-builder) → Schema Generation (schema-generator) → Data Store Creation (vertex-ai-setup) → Search App Configuration (vertex-ai-setup) → API Layer (vertex-ai-setup)

### API Layer Pattern
[2025-04-13 17:22:26] - The project implements multiple API layers with progressive complexity:
- Debug API (`mcp_debug_api.py`): Exposes raw data structures for debugging
- Simple API (`mcp_simple_api.py`): Provides basic search functionality
- Full Search API (`mcp_search_api.py`): Comprehensive search with structured results
- Advanced API (`mcp_advanced_api.py`): Enhanced search with pagination, facets, and semantic search capabilities

### Data Transformation Pattern
[2025-04-13 17:22:26] - The project employs a consistent data transformation pattern:
1. Raw Data → Structured Schema → Search Index → API Response

## Code Patterns

### Configuration Management
[2025-04-13 17:22:26] - Configuration values are defined at module level in each script rather than using a central configuration system.

### Result Processing
[2025-04-13 17:22:26] - Search results are processed using a common pattern:
1. Execute search query
2. Transform protocol buffer responses to dictionaries
3. Extract and clean relevant fields
4. Structure the data for API output

### Error Handling
[2025-04-13 17:22:26] - Consistent error response pattern across APIs:
```python
{
    "status": "error",
    "timestamp": current_time,
    "message": error_message,
    "query": original_query
}
```

### Advanced Search Features Pattern
[2025-04-13 17:25:13] - The advanced search implementation follows a progressive enhancement pattern:
1. Core text search as base functionality
2. Semantic search as an optional enhancement
3. Faceted search for result navigation
4. Pagination for handling large result sets
5. Advanced filtering for refined queries

### Type Safety Pattern
[2025-04-13 17:25:13] - The advanced API introduces type hints to improve code quality:
```python
def search_mcp_servers(
    query: str,
    page_size: int = DEFAULT_PAGE_SIZE,
    page_token: str = None,
    filter_expr: str = None,
    facets: List[str] = None,
    search_mode: str = "text",
    order_by: str = None
) -> Dict[str, Any]:
    # Implementation
```