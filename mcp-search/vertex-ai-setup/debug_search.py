#!/usr/bin/env python3

"""
MCP Server Search Debugger - Examine the exact structure of returned documents
"""

import json
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.protobuf.json_format import MessageToDict

# --- Configuration ---
PROJECT_ID = "saib-ai-playground"
LOCATION = "global"
ENGINE_ID = "mcp-search-app-v4-id"
SERVING_CONFIG_ID = "default_config"

def debug_search(query="github", max_results=3):
    """Debug search by dumping complete document structure."""
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
    
    print(f"Executing search for query: '{query}'")
    
    # Execute the search
    try:
        response = client.search(request=request)
        
        print(f"\n==== Found {len(response.results)} results ====\n")
        
        # Process each result
        for i, result in enumerate(response.results):
            print(f"\n---- RESULT {i+1} ----")
            
            # Convert proto to dict
            doc_dict = MessageToDict(result.document._pb)
            
            # Print the entire document structure
            print("\nCOMPLETE DOCUMENT STRUCTURE:")
            print(json.dumps(doc_dict, indent=2))
            
            # Extract the ID 
            doc_id = doc_dict.get("id", "N/A")
            print(f"\nDocument ID: {doc_id}")
            
            # Extract and print structData path
            struct_data = doc_dict.get("structData", {})
            print("\nSTRUCTDATA (Level 1):")
            print(json.dumps(struct_data, indent=2))
            
            # Check if there's a nested structData
            if isinstance(struct_data, dict) and "structData" in struct_data:
                nested_struct_data = struct_data.get("structData", {})
                print("\nSTRUCTDATA (Level 2 - Nested):")
                print(json.dumps(nested_struct_data, indent=2))
                
                # Extract key fields from nested level
                name = nested_struct_data.get("name", "N/A")
                desc = nested_struct_data.get("server_description", "N/A")
                stars = nested_struct_data.get("stars", 0)
                
                print("\nKEY FIELDS FROM NESTED STRUCTDATA:")
                print(f"- Name: {name}")
                print(f"- Description: {desc}")
                print(f"- Stars: {stars}")
            
            print("\n" + "-"*50)
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    debug_search()