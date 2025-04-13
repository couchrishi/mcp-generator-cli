import logging
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.api_core import exceptions as google_exceptions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
project_id = "saib-ai-playground"
location = "global"
engine_id = "mcp-search-app-v5-id" # ID of the engine/app to delete (Updated to v5)

def delete_search_engine_sample(project_id: str, location: str, engine_id: str):
    """Deletes a Discovery Engine Search App (Engine)."""
    logging.info(f"Attempting to delete Search App (Engine) '{engine_id}' in project '{project_id}', location '{location}'...")

    try:
        client = discoveryengine.EngineServiceClient()

        # The full resource name of the engine.
        # Format: projects/{project}/locations/{location}/collections/default_collection/engines/{engine_id}
        name = client.engine_path(
            project=project_id,
            location=location,
            collection="default_collection",
            engine=engine_id,
        )
        logging.info(f"Target Engine path: {name}")

        logging.info("Initiating Search App (Engine) deletion operation...")
        operation = client.delete_engine(name=name)

        logging.info(f"Waiting for operation to complete: {operation.operation.name}")
        operation.result() # Wait for completion, result is None for delete
        logging.info(f"Search App (Engine) '{engine_id}' deleted successfully.")

    except google_exceptions.NotFound:
        logging.warning(f"Search App (Engine) '{engine_id}' not found. Skipping deletion.")
    except Exception as e:
        logging.error(f"Error deleting Search App (Engine): {e}", exc_info=True)


# --- Run the function ---
if __name__ == "__main__":
    delete_search_engine_sample(project_id, location, engine_id)
    logging.info("Search App (Engine) deletion script finished.")