import json
import os

def get_json_schema_type(vertex_type):
    """Maps Vertex AI type to JSON Schema type."""
    if vertex_type == "STRING":
        return "string"
    elif vertex_type == "NUMBER":
        return "number"
    elif vertex_type == "BOOLEAN":
        return "boolean"
    elif vertex_type == "STRING_ARRAY":
        # For standard JSON schema, define as array with string items
        return "array", {"type": "string"}
    else:
        return "string" # Default fallback

# Define the fields and their Vertex AI types and properties
# Note: 'id' is handled by Vertex AI import/search, not defined in schema properties
vertex_fields_config = [
    # --- Core Info ---
    {"name": "name", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True},
    {"name": "repo_url", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True},
    {"name": "type", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True}, # Ensure filterable/facetable
    # --- Repo Metadata ---
    {"name": "stars", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "forks", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    # --- Technical Info ---
    {"name": "language_stack", "type": "STRING_ARRAY"}, # Revert to Array
    {"name": "package_manager", "type": "STRING_ARRAY"}, # Revert to Array
    {"name": "dependencies_file", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True},
    {"name": "has_dockerfile", "type": "BOOLEAN", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "has_docs", "type": "BOOLEAN", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "has_readme", "type": "BOOLEAN", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "has_examples", "type": "BOOLEAN", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "has_tests", "type": "BOOLEAN", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "base_docker_image", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True},
    # --- Content ---
    {"name": "server_description", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True},
    {"name": "tools_exposed", "type": "STRING_ARRAY"}, # Revert to Array
    # --- MCP Security ---
    {"name": "mcp_sec_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "mcp_sec_risk", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "mcp_sec_top_findings", "type": "STRING_ARRAY"}, # Revert to Array
    {"name": "mcp_sec_top_recommendations", "type": "STRING_ARRAY"}, # Revert to Array
    {"name": "mcp_sec_tool_poisoning_risk", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "mcp_sec_input_validation_risk", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "mcp_sec_authentication_risk", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "mcp_sec_data_exfiltration_risk", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "mcp_sec_dependency_security_risk", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    # --- API Security ---
    {"name": "api_sec_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "api_sec_auth_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True},
    {"name": "api_sec_rate_limit_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True},
    {"name": "api_sec_input_validation_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True},
    {"name": "api_sec_error_handling_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True},
    {"name": "api_sec_https_tls_score", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True},
    # --- Container Security ---
    {"name": "cont_sec_base_image_name", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True},
    {"name": "cont_sec_base_image_provenance", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_base_image_tag_type", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_base_image_freshness", "type": "STRING", "indexable": True, "searchable": True, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_base_image_age_days", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_runs_as_root", "type": "BOOLEAN", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_vuln_critical", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_vuln_high", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_vuln_total", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
    {"name": "cont_sec_vuln_fixable", "type": "NUMBER", "indexable": True, "searchable": False, "retrievable": True, "dynamicFacetable": True},
]

# Build the properties dictionary with both standard types and Vertex AI annotations
properties = {}
for field_config in vertex_fields_config:
    field_name = field_config["name"]
    vertex_type = field_config["type"]
    schema_type_info = get_json_schema_type(vertex_type)

    # Basic type definition for standard JSON Schema part
    prop_def = {}
    if isinstance(schema_type_info, tuple): # Handle array type
        prop_def["type"] = schema_type_info[0]
        prop_def["items"] = schema_type_info[1]
        # No annotations for array types
        pass
    else: # Handle simple types (string, number, boolean)
        prop_def["type"] = schema_type_info
        # Add Vertex AI annotations for simple types
        prop_def["indexable"] = field_config.get("indexable", False)
        prop_def["dynamicFacetable"] = field_config.get("dynamicFacetable", False)
        prop_def["searchable"] = field_config.get("searchable", False)
        prop_def["retrievable"] = field_config.get("retrievable", True) # Default to True

    properties[field_name] = prop_def

# Define the final schema structure expected by the upload API
# It needs the standard JSON schema structure AND the Vertex AI annotations within properties
final_schema_for_upload = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": properties
    # Note: Vertex AI uses the annotations within 'properties'
    # The separate 'documentSchema' key caused issues previously.
}


# Define the output path
output_dir = "." # Output in the current directory (schema-generator)
output_filename = "vertex_ai_schema.json"
output_path = os.path.join(output_dir, output_filename)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Write the schema to the JSON file
try:
    with open(output_path, 'w') as f:
        json.dump(final_schema_for_upload, f, indent=2)
    print(f"Successfully generated combined schema at: {output_path}")
except IOError as e:
    print(f"Error writing schema file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")