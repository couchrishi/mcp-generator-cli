import logging
import json
import os
import pathlib # Import pathlib
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.api_core import exceptions as google_exceptions
from google.protobuf.struct_pb2 import Struct # Import Struct
from google.protobuf.json_format import ParseDict # Helper to convert dict to Struct

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
project_id = "saib-ai-playground"
location = "global"
data_store_id = "mcp-servers-datastore-v4" # Target v4 data store (Updated to v4)
# Get the directory where this script is located
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
# Path relative to the script's location, then resolved to absolute
schema_file_path = SCRIPT_DIR.parent / "schema-generator" / "vertex_ai_schema.json"

def upload_schema(project_id: str, location: str, data_store_id: str, schema_file_path: str):
    """Uploads or updates the schema for a given data store."""
    logging.info(f"Attempting to upload schema from '{schema_file_path}' to data store '{data_store_id}'...")

    try:
        # Read the schema from the local JSON file
        logging.info(f"Reading schema file: {schema_file_path}")
        with open(schema_file_path, 'r') as f:
            schema_dict = json.load(f)
            # Basic validation (Commented out as we now use Vertex AI specific format)
            # if "properties" not in schema_dict or "type" not in schema_dict or schema_dict["type"] != "object":
            #      raise ValueError("Schema JSON must be a valid JSON Schema object with 'type': 'object' and 'properties'")

        # Convert the Python dictionary to a Protobuf Struct
        schema_struct = Struct()
        ParseDict(schema_dict, schema_struct) # Use ParseDict for conversion
        logging.info("Converted schema dictionary to Protobuf Struct.")


        client = discoveryengine.SchemaServiceClient()

        schema_name = client.schema_path(
            project=project_id,
            location=location,
            data_store=data_store_id,
            schema="default_schema", # Use 'default_schema' ID for structured data stores
        )
        logging.info(f"Target schema path: {schema_name}")

        # Construct the Schema object using struct_schema with the Struct
        schema_obj = discoveryengine.Schema(
            name=schema_name,
            struct_schema=schema_struct # Pass the Protobuf Struct object
        )
        logging.info(f"Schema object configured with Struct.") # Simplified log

        # Construct the UpdateSchemaRequest
        request = discoveryengine.UpdateSchemaRequest(
            schema=schema_obj
            # update_mask can be added if needed (Removed as it caused error)
        )
        logging.info(f"UpdateSchemaRequest constructed.") # Simplified log


        logging.info("Initiating schema update operation...")
        # Pass the request object to the update_schema method
        operation = client.update_schema(request=request)

        logging.info(f"Waiting for schema update operation to complete: {operation.operation.name}")
        response = operation.result()
        logging.info(f"Operation completed successfully.")

        metadata = discoveryengine.UpdateSchemaMetadata(operation.metadata)

        logging.info(f"Schema updated: {response.name}") # Log only name for brevity
        logging.info(f"Update time: {metadata.update_time}")

    except FileNotFoundError:
        logging.error(f"Schema file not found at: {schema_file_path}", exc_info=True)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding schema JSON from {schema_file_path}: {e}", exc_info=True)
    except ValueError as e:
        logging.error(f"Schema validation error: {e}", exc_info=True)
    except Exception as e:
        logging.error(f"Error uploading schema: {e}", exc_info=True)


# --- Run the function ---
if __name__ == "__main__":
    upload_schema(project_id, location, data_store_id, schema_file_path)
    logging.info("Schema upload script finished.")