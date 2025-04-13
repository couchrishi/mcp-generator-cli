import logging
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.api_core import exceptions as google_exceptions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
project_id = "saib-ai-playground"
location = "global"
data_store_id = "mcp-servers-datastore-v4" # Target the v4 store for deletion (Updated to v4)

def delete_data_store_sample(project_id: str, location: str, data_store_id: str):
    """Deletes a Discovery Engine data store."""
    logging.info(f"Attempting to delete data store '{data_store_id}' in project '{project_id}', location '{location}'...")

    try:
        client = discoveryengine.DataStoreServiceClient()

        # The full resource name of the data store.
        # Format: projects/{project}/locations/{location}/collections/default_collection/dataStores/{data_store_id}
        name = client.data_store_path(
            project=project_id,
            location=location,
            data_store=data_store_id,
            # collection="default_collection", # Removed collection ID argument
        )
        logging.info(f"Target data store path: {name}")

        logging.info("Initiating data store deletion operation...")
        operation = client.delete_data_store(name=name)

        logging.info(f"Waiting for operation to complete: {operation.operation.name}")
        operation.result() # Wait for completion, result is None for delete
        logging.info(f"Data store '{data_store_id}' deleted successfully.")

    except google_exceptions.NotFound:
        logging.warning(f"Data store '{data_store_id}' not found. Skipping deletion.")
    except Exception as e:
        logging.error(f"Error deleting data store: {e}", exc_info=True)


# --- Run the function ---
if __name__ == "__main__":
    delete_data_store_sample(project_id, location, data_store_id)
    logging.info("Data store deletion script finished.")