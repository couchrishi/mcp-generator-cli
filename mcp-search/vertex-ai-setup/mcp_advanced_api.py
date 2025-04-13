#!/usr/bin/env python3

"""
MCP Server Advanced Search API - Enhanced implementation with pagination,
advanced filtering, semantic search, and faceted results for MCP servers.
"""

import argparse
import json
import sys
import re
from datetime import datetime
from typing import Dict, List, Optional, Union, Any
import logging # Added logging

# Only import Google Cloud libraries if needed
try:
    from google.cloud import discoveryengine_v1alpha as discoveryengine
    from google.protobuf.json_format import MessageToDict
    GOOGLE_CLOUD_AVAILABLE = True
except ImportError:
    GOOGLE_CLOUD_AVAILABLE = False
    # Define dummy classes or skip API calls if library not available (optional)
    pass

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
PROJECT_ID = "saib-ai-playground"
LOCATION = "global"
ENGINE_ID = "mcp-search-app-v5-id" # Updated to v5 app
SERVING_CONFIG_ID = "default_search" # Use default_search based on simple script test

# --- Advanced Search Options ---
SEARCH_MODES = ["text", "semantic"]
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

def find_field_in_nested_dict(data: Dict[str, Any], field_name: str) -> Any:
    """Recursively search for a field in a nested dictionary."""
    if not isinstance(data, dict):
        return None

    if field_name in data:
        return data[field_name]

    for key, value in data.items():
        if isinstance(value, dict):
            result = find_field_in_nested_dict(value, field_name)
            if result is not None:
                return result

    return None

def extract_repo_info(doc_id: str) -> Dict[str, str]:
    """Extract repository information from a document ID."""
    # Parse a GitHub repository ID
    if doc_id.startswith("github-com-"):
        # Extract parts after "github-com-"
        parts = doc_id[11:].split("-")
        if len(parts) >= 2:
            username = parts[0]
            # The repo name might contain multiple parts
            repo_name = '-'.join(parts[1:]) # Join remaining parts for repo name
            # Construct GitHub URL
            github_url = f"https://github.com/{username}/{repo_name}"
            # Generate a better display name
            display_name = f"{username}/{repo_name}"
            return {
                "name": display_name,
                "url": github_url,
                "platform": "GitHub",
                "owner": username,
                "repo": repo_name
            }

    # Handle NPM package format
    if doc_id.startswith("npm-"):
        package_name = doc_id[4:]
        return {
            "name": package_name,
            "url": f"https://www.npmjs.com/package/{package_name}",
            "platform": "NPM"
        }

    # Handle PyPI package format
    if doc_id.startswith("pypi-"):
        package_name = doc_id[5:]
        return {
            "name": package_name,
            "url": f"https://pypi.org/project/{package_name}",
            "platform": "PyPI"
        }

    # Handle other repository types or formats
    return {
        "name": doc_id, # Use ID as name fallback
        "url": "",
        "platform": "Unknown"
    }

def clean_value(value: Any) -> Any:
    """Clean and normalize values for consistent output."""
    if value is None:
        return None
    if isinstance(value, str) and not value.strip():
        return None
    return value

def build_filter_expression(filters: Dict[str, Any]) -> str:
    """Build a filter expression from a dictionary of filters."""
    if not filters:
        return ""

    expressions = []

    # Handle simple equality filters
    for key, value in filters.items():
        if isinstance(value, bool):
            expressions.append(f"{key}={str(value).lower()}")
        elif isinstance(value, (int, float)):
            expressions.append(f"{key}={value}")
        elif isinstance(value, str):
             # Handle array contains filter (e.g., language_stack:python)
            if ':' in value and key in ['language_stack', 'tools_exposed', 'package_manager']:
                 expressions.append(f"{key}:{value.split(':', 1)[1]}")
            else:
                expressions.append(f"{key}=\"{value}\"")
        elif isinstance(value, dict) and "min" in value and "max" in value:
            expressions.append(f"{key}>={value['min']} AND {key}<={value['max']}")
        elif isinstance(value, dict) and "min" in value:
            expressions.append(f"{key}>={value['min']}")
        elif isinstance(value, dict) and "max" in value:
            expressions.append(f"{key}<={value['max']}")

    return " AND ".join(expressions)

def extract_facets_from_response(response) -> Dict[str, Any]:
    """Extract facet information from search response."""
    facets = {}
    if hasattr(response, 'facets'):
        for facet in response.facets:
            facet_name = facet.key
            facet_values = []
            for value in facet.values:
                facet_values.append({
                    "value": value.value if hasattr(value, 'value') else value.interval, # Handle interval facets
                    "count": value.count
                })
            facets[facet_name] = facet_values
    return facets

def format_server_data(doc_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Format and clean the server data for API output."""
    doc_id = doc_dict.get("id", "")
    repo_info = extract_repo_info(doc_id)
    struct_data = doc_dict.get("structData", {}) or {}

    # Helper function to get value from structData
    def get_value(key, default=None):
        value = struct_data.get(key)
        return value if value is not None else default

    name = get_value("name")
    if not name or isinstance(name, dict) or (isinstance(name, str) and name.startswith("projects/")):
        name = repo_info["name"]

    repo_url = get_value("repo_url")
    if not repo_url:
        repo_url = repo_info["url"]

    description = get_value("server_description", "No description available")
    server_type = get_value("type", "Unknown")
    stars = get_value("stars", 0)
    forks = get_value("forks", 0)
    last_updated = get_value("last_updated") # Keep as None if missing
    tools_exposed = get_value("tools_exposed", [])
    language_stack = get_value("language_stack", [])

    if not isinstance(tools_exposed, list): tools_exposed = []
    if not isinstance(language_stack, list): language_stack = []

    has_docs = bool(get_value("has_docs", False))
    has_readme = bool(get_value("has_readme", False))
    has_examples = bool(get_value("has_examples", False))
    readme_quality = get_value("readme_quality", "Unknown")

    mcp_sec_score = get_value("mcp_sec_score")
    api_sec_score = get_value("api_sec_score")
    cont_sec_vuln_critical = get_value("cont_sec_vuln_critical", 0)
    cont_sec_vuln_high = get_value("cont_sec_vuln_high", 0)

    security_risk = "Unknown"
    if mcp_sec_score is not None:
        if mcp_sec_score >= 80: security_risk = "Low"
        elif mcp_sec_score >= 60: security_risk = "Medium"
        else: security_risk = "High"
    elif cont_sec_vuln_critical > 0: security_risk = "High"
    elif cont_sec_vuln_high > 5: security_risk = "Medium"

    server_data = {
        "id": doc_id,
        "name": name,
        "url": repo_url,
        "description": description,
        "type": server_type,
        "last_updated": last_updated,
        "repository": {
            "platform": repo_info["platform"],
            "stars": stars or 0,
            "forks": forks or 0,
            "languages": language_stack
        },
        "mcp_details": {
            "tools_count": len(tools_exposed),
            "top_tools": tools_exposed[:5],
            "all_tools": tools_exposed,
            "documentation": {
                "has_docs": has_docs,
                "has_readme": has_readme,
                "has_examples": has_examples,
                "readme_quality": readme_quality
            }
        },
        "security": {
            "risk_level": security_risk,
            "mcp_score": mcp_sec_score,
            "api_score": api_sec_score,
            "vulnerabilities": {
                "critical": cont_sec_vuln_critical or 0,
                "high": cont_sec_vuln_high or 0
            }
        }
    }
    return server_data

def search_mcp_servers(
    query: str,
    page_size: int = DEFAULT_PAGE_SIZE,
    page_token: str = None,
    filter_expr: str = None,
    facets: List[str] = None,
    search_mode: str = "text",
    order_by: str = None
) -> Dict[str, Any]:
    """Search for MCP servers with advanced options."""
    if not GOOGLE_CLOUD_AVAILABLE:
        logging.error("Google Cloud Discovery Engine library not available. Cannot perform search.")
        return {"status": "error", "message": "Discovery Engine library not installed."}

    logging.info(f"Performing search: query='{query}', mode='{search_mode}', page_size={page_size}, filter='{filter_expr}', order_by='{order_by}'")

    if page_size > MAX_PAGE_SIZE: page_size = MAX_PAGE_SIZE
    if search_mode not in SEARCH_MODES: search_mode = "text"

    client = discoveryengine.SearchServiceClient()
    serving_config = (
        f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/"
        f"engines/{ENGINE_ID}/servingConfigs/{SERVING_CONFIG_ID}"
    )

    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=query,
        page_size=page_size
    )

    if page_token: request.page_token = page_token
    if filter_expr: request.filter = filter_expr
    if order_by: request.order_by = order_by

    if facets:
        request.facet_specs = [
             discoveryengine.SearchRequest.FacetSpec(facet_key=f) for f in facets
        ]

    if search_mode == "semantic":
        # Configure for semantic search (example settings)
        request.content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
             snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                 return_snippet=True
             ),
             summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                 summary_result_count=3, # Number of results to summarize
                 include_citations=True
             ),
             extractive_content_spec=discoveryengine.SearchRequest.ContentSearchSpec.ExtractiveContentSpec(
                 max_extractive_answer_count=1
             )
        )
        logging.info("Semantic search options enabled.")

    try:
        logging.debug(f"Executing SearchRequest: {request}")
        response = client.search(request=request)
        logging.debug("Search response received.")

        results = []
        total_size = getattr(response, 'total_size', 0) # Get total size if available

        for result in response.results:
            doc_dict = MessageToDict(result.document._pb)
            server_data = format_server_data(doc_dict)
            # Include semantic search results if available
            if search_mode == 'semantic' and hasattr(result, 'derived_struct_data') and 'extractive_answers' in result.derived_struct_data:
                 server_data['extractive_answers'] = MessageToDict(result.derived_struct_data['extractive_answers']._pb)
            if search_mode == 'semantic' and hasattr(result, 'derived_struct_data') and 'snippets' in result.derived_struct_data:
                 server_data['snippets'] = MessageToDict(result.derived_struct_data['snippets']._pb)

            results.append(server_data)

        facet_data = extract_facets_from_response(response)
        summary_data = None
        if search_mode == 'semantic' and hasattr(response, 'summary'):
             summary_data = MessageToDict(response.summary._pb)


        api_response = {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "search_mode": search_mode,
            "total_size": total_size, # Total results matching query
            "count": len(results), # Results on this page
            "results": results
        }

        if hasattr(response, 'next_page_token') and response.next_page_token:
            api_response["pagination"] = {"next_page_token": response.next_page_token}
        if facet_data: api_response["facets"] = facet_data
        if filter_expr: api_response["filter"] = filter_expr
        if order_by: api_response["order_by"] = order_by
        if summary_data: api_response["summary"] = summary_data


        return api_response

    except Exception as e:
        logging.error(f"Error during search execution: {e}", exc_info=True)
        error_response = {
            "status": "error",
            "timestamp": datetime.now().isoformat(),
            "message": str(e),
            "query": query
        }
        return error_response

def main():
    """Main function to parse arguments and execute search."""
    parser = argparse.ArgumentParser(description="MCP Server Advanced Search API")
    parser.add_argument("query", nargs="?", default="github",
                        help="Search query (default: 'github')")
    parser.add_argument("-n", "--page-size", type=int, default=DEFAULT_PAGE_SIZE,
                        help=f"Number of results per page (default: {DEFAULT_PAGE_SIZE}, max: {MAX_PAGE_SIZE})")
    parser.add_argument("-t", "--page-token", type=str,
                        help="Pagination token for getting next page of results")
    parser.add_argument("-f", "--filter", type=str,
                        help="Filter expression (e.g., 'stars>=100 AND has_docs=true')")
    parser.add_argument("-m", "--mode", type=str, default="text", choices=SEARCH_MODES,
                        help="Search mode: text (default) or semantic")
    parser.add_argument("--facets", type=str,
                        help="Comma-separated list of facet fields (e.g., 'type,language_stack')")
    parser.add_argument("-o", "--order-by", type=str,
                        help="Field to order results by (e.g., 'stars desc')")
    parser.add_argument("-p", "--pretty", action="store_true",
                        help="Pretty-print the JSON output")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")


    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    facets_list = [f.strip() for f in args.facets.split(",")] if args.facets else None

    results = search_mcp_servers(
        query=args.query,
        page_size=args.page_size,
        page_token=args.page_token,
        filter_expr=args.filter,
        facets=facets_list,
        search_mode=args.mode,
        order_by=args.order_by
    )

    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))

if __name__ == "__main__":
    main()