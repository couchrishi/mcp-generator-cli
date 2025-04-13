import json
import os
import re # Import re for substitution
import pathlib # Import pathlib for robust path handling

# --- Configuration ---
# Get the directory where this script is located
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

# Define input/output directories relative to the script's location
INPUT_DIR = SCRIPT_DIR.parent / "schema-generator" / "schema-inputs"
OUTPUT_DIR = SCRIPT_DIR # Output in the current directory (corpus-builder)
OUTPUT_FILENAME = "mcp_servers_corpus.ndjson"

# Construct absolute paths for input/output files
MAIN_DATA_FILE = INPUT_DIR / "discovered_mcp_servers_with_metadata.json"
API_SEC_FILE = INPUT_DIR / "api_security_results.json"
CONT_SEC_FILE = INPUT_DIR / "container_security_results.json"
MCP_SEC_FILE = INPUT_DIR / "mcp_security_results.json"

OUTPUT_PATH = OUTPUT_DIR / OUTPUT_FILENAME

# --- Helper Functions ---
def load_json(filepath):
    """Loads JSON data from a file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: File not found - {filepath}. Skipping.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filepath}: {e}. Skipping.")
        return None

def build_lookup(data, key_field):
    """Builds a lookup dictionary from a list of records."""
    lookup = {}
    if data and 'repositories' in data:
        for repo in data['repositories']:
            if key_field in repo:
                lookup[repo[key_field]] = repo
    return lookup

def sanitize_id(url):
    """Replaces invalid characters in a URL to create a valid Vertex AI ID."""
    if not url:
        return None
    # Remove protocol
    sanitized = re.sub(r'^https?://', '', url)
    # Replace invalid characters (/, ., :, ?, =, #, &) with hyphen
    sanitized = re.sub(r'[/.:?=#&]', '-', sanitized)
    # Ensure it starts with alphanumeric (though unlikely for URLs)
    if not re.match(r'^[a-zA-Z0-9]', sanitized):
        sanitized = "id-" + sanitized # Prepend if needed
    return sanitized


# --- Main Logic ---
print("Loading data...")
main_data = load_json(MAIN_DATA_FILE)
api_sec_data = load_json(API_SEC_FILE)
cont_sec_data = load_json(CONT_SEC_FILE)
mcp_sec_data = load_json(MCP_SEC_FILE)

if not main_data or 'items' not in main_data:
    print(f"Error: Main data file {MAIN_DATA_FILE} is missing or invalid. Cannot proceed.")
    exit(1)

print("Building security data lookups...")
api_sec_lookup = build_lookup(api_sec_data, 'repo_url')
cont_sec_lookup = build_lookup(cont_sec_data, 'repo_url')
mcp_sec_lookup = build_lookup(mcp_sec_data, 'repo_url')

print(f"Processing {len(main_data.get('items', []))} server records...")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    with open(OUTPUT_PATH, 'w') as outfile:
        for item in main_data.get('items', []):
            repo_url = item.get('repo_url')
            if not repo_url:
                print(f"Warning: Skipping item with missing repo_url: {item.get('name', 'N/A')}")
                continue

            sanitized_doc_id = sanitize_id(repo_url)
            if not sanitized_doc_id:
                 print(f"Warning: Could not generate valid ID for repo_url: {repo_url}. Skipping.")
                 continue


            analysis = item.get('analysis_results', {}) or {} # Ensure analysis is a dict
            api_sec = api_sec_lookup.get(repo_url, {}).get('api_security', {}) or {}
            cont_sec = cont_sec_lookup.get(repo_url, {}).get('container_security', {}) or {}
            mcp_sec = mcp_sec_lookup.get(repo_url, {}).get('mcp_security', {}) or {}

            # Safely get nested values, defaulting to None if keys are missing
            mcp_detailed = mcp_sec.get('detailed_results', {}) or {}
            cont_base = cont_sec.get('base_image', {}) or {}
            cont_vuln = cont_sec.get('vulnerability_summary', {}) or {}

            record = {
                "id": sanitized_doc_id, # Use sanitized repo_url as the unique ID
                "name": item.get('name'),
                "repo_url": repo_url,
                "type": item.get('type'),

                "stars": analysis.get('stars'),
                "forks": analysis.get('forks'),
            
                "language_stack": analysis.get('language_stack', []), # Keep as array
                "package_manager": analysis.get('package_manager', []), # Keep as array
                "dependencies_file": analysis.get('dependencies_file'),
                "has_dockerfile": analysis.get('has_dockerfile'),
                "has_docs": analysis.get('has_docs'),
                "has_readme": analysis.get('has_readme'),
                "has_examples": analysis.get('has_examples'),
                "has_tests": analysis.get('has_tests'),
                "base_docker_image": analysis.get('base_docker_image'),

                "server_description": analysis.get('server_description'),
                "tools_exposed": analysis.get('tools_exposed', []), # Keep as array

                "mcp_sec_score": mcp_sec.get('overall_score'),
                "mcp_sec_risk": mcp_sec.get('overall_risk_level'),
                "mcp_sec_top_findings": mcp_sec.get('top_findings', []), # Keep as array
                "mcp_sec_top_recommendations": mcp_sec.get('top_recommendations', []), # Keep as array
                "mcp_sec_tool_poisoning_risk": mcp_detailed.get('tool_poisoning', {}).get('risk_level'),
                "mcp_sec_input_validation_risk": mcp_detailed.get('input_validation', {}).get('risk_level'),
                "mcp_sec_authentication_risk": mcp_detailed.get('authentication', {}).get('risk_level'),
                "mcp_sec_data_exfiltration_risk": mcp_detailed.get('data_exfiltration', {}).get('risk_level'),
                "mcp_sec_dependency_security_risk": mcp_detailed.get('dependency_security', {}).get('risk_level'),

                "api_sec_score": api_sec.get('overall_score'),
                "api_sec_auth_score": api_sec.get('authentication', {}).get('score'),
                "api_sec_rate_limit_score": api_sec.get('rate_limiting', {}).get('score'),
                "api_sec_input_validation_score": api_sec.get('input_validation', {}).get('score'),
                "api_sec_error_handling_score": api_sec.get('error_handling', {}).get('score'),
                "api_sec_https_tls_score": api_sec.get('https_tls', {}).get('score'),

                "cont_sec_base_image_name": cont_base.get('name'),
                "cont_sec_base_image_provenance": cont_base.get('provenance'),
                "cont_sec_base_image_tag_type": cont_base.get('tag_type'),
                "cont_sec_base_image_freshness": cont_base.get('freshness_rating'),
                "cont_sec_base_image_age_days": cont_base.get('age_days'),
                "cont_sec_runs_as_root": cont_base.get('runs_as_root'),
                "cont_sec_vuln_critical": cont_vuln.get('critical_count'),
                "cont_sec_vuln_high": cont_vuln.get('high_count'),
                "cont_sec_vuln_total": cont_vuln.get('total_count'),
                "cont_sec_vuln_fixable": cont_vuln.get('fixable_count'),
            }

            # Ensure all fields defined in the schema are present, adding null if missing
            # Revert to: Structure required for ImportDocuments: {"id": "...", "structData": { ... }}
            struct_data = {}
            expected_fields_set = {
                 "name", "repo_url", "type", "stars", "forks", "language_stack", # Exclude 'id' here
                "package_manager", "dependencies_file", "has_dockerfile", "has_docs",
                "has_readme", "has_examples", "has_tests", "base_docker_image",
                "server_description", "tools_exposed", "mcp_sec_score", "mcp_sec_risk",
                "mcp_sec_top_findings", "mcp_sec_top_recommendations",
                "mcp_sec_tool_poisoning_risk", "mcp_sec_input_validation_risk",
                "mcp_sec_authentication_risk", "mcp_sec_data_exfiltration_risk",
                "mcp_sec_dependency_security_risk", "api_sec_score", "api_sec_auth_score",
                "api_sec_rate_limit_score", "api_sec_input_validation_score",
                "api_sec_error_handling_score", "api_sec_https_tls_score",
                "cont_sec_base_image_name", "cont_sec_base_image_provenance",
                "cont_sec_base_image_tag_type", "cont_sec_base_image_freshness",
                "cont_sec_base_image_age_days", "cont_sec_runs_as_root",
                "cont_sec_vuln_critical", "cont_sec_vuln_high", "cont_sec_vuln_total",
                "cont_sec_vuln_fixable"
            }
            for field in expected_fields_set:
                 struct_data[field] = record.get(field) # Defaults to None (null in JSON) if not found

            final_record_for_import = {
                "id": record.get("id"), # Keep 'id' at the top level
                "structData": struct_data
                # "content": {} # Removed empty content field
            }

            # Write the processed record as a JSON line
            outfile.write(json.dumps(final_record_for_import) + '\n')

    print(f"Successfully generated corpus file at: {OUTPUT_PATH}")

except IOError as e:
    print(f"Error writing corpus file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")