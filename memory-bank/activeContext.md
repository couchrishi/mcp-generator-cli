# MCP Search Project - Active Context

## Current Focus
[2025-04-14 01:52:14] - Troubleshooting and resolving data inconsistencies in Vertex AI Search results. Successfully implemented and verified `simple_mcp_search.py` after switching to schema auto-detection.

## Recent Changes
[2025-04-13 17:22:14] - Set up the Memory Bank.
[2025-04-13 17:24:35] - Implemented `mcp_advanced_api.py`.
[2025-04-13 17:30:02] - Created focused `simple_mcp_search.py` script.
[2025-04-13 17:35:02] - Added debug mode to `simple_mcp_search.py` to inspect raw results.
[2025-04-13 17:36:50] - Refined data extraction logic in `simple_mcp_search.py` to handle potential nesting.
[2025-04-13 17:42:51] - Simplified extraction logic in `simple_mcp_search.py` based on schema/sample data.
[2025-04-13 17:53:31] - Fixed relative path issues in `prepare_vertex_data.py`.
[2025-04-13 17:55:57] - Switched `import_data.py` to `FULL` reconciliation mode.
[2025-04-13 18:07:25] - Started recreating resources with v4 suffix due to deletion delays.
[2025-04-13 18:09:45] - Fixed relative path issues in `upload_schema.py`.
[2025-04-13 18:11:51] - Switched plan to use schema auto-detection with v5 resources.
[2025-04-13 18:13:33] - Removed invalid `update_mask` from `upload_schema.py`.
[2025-04-14 01:47:41] - Configured `import_data.py` for auto-detection (removed `data_schema` and `id_field`).
[2025-04-14 01:48:22] - Created v5 data store and search app.
[2025-04-14 01:49:19] - Updated `simple_mcp_search.py` to target v5 resources.
[2025-04-14 01:51:32] - Verified `simple_mcp_search.py` works correctly with auto-detected schema.

## Open Questions/Issues
[2025-04-14 01:52:14] - Root cause of Vertex AI indexing inconsistency when using custom schema remains unclear (though bypassed).
[2025-04-14 01:52:14] - Long-term implications of using auto-detected schema vs custom schema (e.g., control over faceting, indexing options).

## Next Steps
[2025-04-14 01:52:14] - Consider next development phase (e.g., web interface, tests, ranking).
[2025-04-14 01:52:14] - Clean up unused v3/v4 resources in Google Cloud if desired.