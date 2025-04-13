#!/usr/bin/env python3

"""
Fixed MCP Server Search - Correctly handles the double-nested structData structure
"""

import argparse
import json
import sys
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.protobuf.json_format import MessageToDict

# --- Configuration ---
PROJECT_ID = "saib-ai-playground"
LOCATION = "global"
ENGINE_ID = "mcp-search-app-v5-id" # Updated to v5 app
SERVING_CONFIG_ID = "default_search" # Try default_search again for v5 app

def extract_repo_info(doc_id):
    """Extract repository information from a document ID."""
    if doc_id.startswith("github-com-"):
        # Remove "github-com-" prefix
        parts = doc_id[11:].split("-")
        if len(parts) >= 2:
            username = parts[0]
            repo_name = parts[1]
            return {
                "name": f"{username}/{repo_name}",
                "url": f"https://github.com/{username}/{repo_name}"
            }
    return {"name": doc_id, "url": ""}

def search_mcp_servers(query, max_results=10, debug=False):
    """Search for MCP servers using Vertex AI Search."""
    # Initialize the client
    client = discoveryengine.SearchServiceClient()
    
    # Build the serving config string
    serving_config = (
        f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/"
        f"engines/{ENGINE_ID}/servingConfigs/{SERVING_CONFIG_ID}"
    )
    
    # Create the search request
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=query,
        page_size=max_results
    )
    
    # Execute the search
    try:
        response = client.search(request=request)
        
        # Process the results
        results = []
        total_count = 0
        
        for result in response.results:
            total_count += 1
            # Convert proto to dict
            doc_dict = MessageToDict(result.document._pb)
            
            # Print raw document structure if debug is enabled
            if debug:
                print(f"\n--- RAW DOCUMENT STRUCTURE ---")
                print(json.dumps(doc_dict, indent=2))
                print("--- END RAW DATA ---\n")
            
            # Extract document ID
            doc_id = doc_dict.get("id", "")
            
            # Get GitHub info from ID
            github_info = extract_repo_info(doc_id)
            
            # Extract the double-nested structData
            # Level 1: doc_dict -> structData
            # Level 2: structData -> structData
            level1_data = doc_dict.get("structData", {})
            level2_data = {}
            
            # Check if level1 contains nested structData
            if isinstance(level1_data, dict) and "structData" in level1_data:
                level2_data = level1_data.get("structData", {})
            
            # Extract fields, prioritizing level2 data
            def get_field(field_name, default=None):
                # Try level2 first (most data seems to be here)
                if level2_data and field_name in level2_data:
                    return level2_data.get(field_name)
                # Fall back to level1
                if level1_data and field_name in level1_data:
                    return level1_data.get(field_name)
                # Fall back to default
                return default
            
            # Extract fields using the helper
            name = get_field("name", github_info["name"])
            url = get_field("repo_url", github_info["url"])
            description = get_field("server_description", "No description available")
            stars = get_field("stars", 0)
            forks = get_field("forks", 0)
            tools_exposed = get_field("tools_exposed", [])
            
            # Ensure tools_exposed is a list
            if not isinstance(tools_exposed, list):
                tools_exposed = []
            
            # Create the server data object
            server_data = {
                "id": doc_id,
                "name": name,
                "url": url,
                "description": description,
                "stars": stars,
                "forks": forks,
                "tools_count": len(tools_exposed),
                "tools": tools_exposed
            }
            
            results.append(server_data)
        
        # Create API-style response
        api_response = {
            "count": total_count,
            "results": results
        }
            
        return api_response
        
    except Exception as e:
        error_response = {
            "status": "error",
            "message": str(e),
            "count": 0,
            "results": []
        }
        return error_response

def main():
    """Main function to parse arguments and execute search."""
    parser = argparse.ArgumentParser(description="Fixed MCP Server Search")
    parser.add_argument("query", nargs="?", default="github", 
                        help="Search query (default: 'github')")
    parser.add_argument("-n", "--num-results", type=int, default=10,
                        help="Maximum number of results to return (default: 10)")
    parser.add_argument("-p", "--pretty", action="store_true",
                        help="Pretty-print the JSON output")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable debug mode to print raw document structure")
    
    args = parser.parse_args()
    
    # Execute the search
    results = search_mcp_servers(args.query, args.num_results, debug=args.debug)
    
    # Output the JSON results
    if args.pretty:
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(results))

if __name__ == "__main__":
    main()