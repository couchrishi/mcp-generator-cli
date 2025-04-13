import logging
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.api_core import exceptions as google_exceptions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
project_id = "saib-ai-playground"
location = "global"
data_store_id = "mcp-servers-datastore-v5" # Target v5 data store (Updated to v5)
gcs_uri = "gs://mcp-resolver/search-datastore/mcp_servers_corpus.ndjson" # Path to the NDJSON file in GCS

def import_documents_sample(project_id: str, location: str, data_store_id: str, gcs_uri: str):
    """Imports documents into a Discovery Engine data store from GCS."""
    logging.info(f"Attempting to import documents from '{gcs_uri}' into data store '{data_store_id}'...")

    try:
        client = discoveryengine.DocumentServiceClient()

        # The full resource name of the search engine branch.
        # Format: projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/default_branch
        parent = client.branch_path(
            project=project_id,
            location=location,
            data_store=data_store_id,
            branch="default_branch", # Import to the default branch
        )
        logging.info(f"Target branch path: {parent}")

        request = discoveryengine.ImportDocumentsRequest(
            parent=parent,
            gcs_source=discoveryengine.GcsSource(input_uris=[gcs_uri]), # Removed data_schema="custom" for auto-detect
            # Options: `INCREMENTAL`, `FULL`, `AUTO`
            reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.FULL, # Changed from INCREMENTAL to FULL
            # id_field="id" # Removed: Not allowed when auto-detecting schema from JSONL
        )
        logging.info(f"ImportDocumentsRequest constructed: {request}")


        logging.info("Initiating document import operation...")
        operation = client.import_documents(request=request)

        logging.info(f"Waiting for document import operation to complete: {operation.operation.name}")
        response = operation.result()
        logging.info(f"Operation completed.")

        # Once the operation is complete,
        # get information from operation metadata
        metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

        # Handle the response
        logging.info(f"Import Response: {response}")
        logging.info(f"Total Success Count: {metadata.success_count}")
        logging.info(f"Total Failure Count: {metadata.failure_count}")
        # Log first few error samples if they exist
        if metadata.failure_count > 0:
             error_samples = response.error_samples[:5] # Log up to 5 errors
             logging.warning(f"First few error samples: {error_samples}")


    except Exception as e:
        logging.error(f"Error importing documents: {e}", exc_info=True)


# --- Run the function ---
if __name__ == "__main__":
    import_documents_sample(project_id, location, data_store_id, gcs_uri)
    logging.info("Document import script finished.")