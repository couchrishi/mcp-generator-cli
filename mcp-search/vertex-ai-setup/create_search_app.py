import logging
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.api_core import exceptions as google_exceptions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
project_id = "saib-ai-playground"
location = "global"
# Use a unique ID for the engine/app resource itself
engine_id = "mcp-search-app-v5-id" # Use v5 ID
engine_display_name = "mcp-search-app-v5" # Use v5 name
# ID of the data store to connect
data_store_id_to_connect = "mcp-servers-datastore-v5" # Connect to v5 datastore


def create_search_engine_sample(
    project_id: str,
    location: str,
    engine_id: str,
    engine_display_name: str,
    data_store_ids: list[str],
):
    """Creates a Discovery Engine Search App (Engine)."""
    logging.info(f"Attempting to create Search App (Engine) '{engine_id}' in project '{project_id}', location '{location}'...")

    try:
        client = discoveryengine.EngineServiceClient()

        # The full resource name of the collection parent branch.
        # Format: projects/{project}/locations/{location}/collections/default_collection
        parent = client.collection_path(
            project=project_id, location=location, collection="default_collection"
        )
        logging.info(f"Parent path constructed: {parent}")

        # Construct the Engine object
        engine = discoveryengine.Engine(
            display_name=engine_display_name,
            solution_type=discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH,
            # Specify the data stores to connect
            data_store_ids=data_store_ids,
            # Configuration for search features
            search_engine_config=discoveryengine.Engine.SearchEngineConfig(
                search_tier=discoveryengine.SearchTier.SEARCH_TIER_ENTERPRISE, # Try more explicit Enum value
                search_add_ons=["SEARCH_ADD_ON_LLM"], # Enable LLM add-on for semantic features
            ),
        )
        logging.info(f"Engine object configured: {engine}")


        logging.info("Initiating Search App (Engine) creation operation...")
        operation = client.create_engine(
            parent=parent, engine=engine, engine_id=engine_id
        )

        logging.info(f"Waiting for operation to complete: {operation.operation.name}")
        response = operation.result()
        logging.info(f"Operation completed successfully.")

        metadata = discoveryengine.CreateEngineMetadata(operation.metadata)

        logging.info(f"Search App (Engine) created: {response}")
        logging.info(f"Resource name: {response.name}")
        logging.info(f"Creation time: {metadata.create_time}")

        return response.name

    except google_exceptions.AlreadyExists:
        logging.warning(f"Search App (Engine) '{engine_id}' already exists.")
        # Attempt to get the existing engine details
        try:
            engine_path = client.engine_path(project_id, location, engine_id)
            existing_engine = client.get_engine(name=engine_path)
            logging.info(f"Existing Engine details: {existing_engine}")
            return existing_engine.name
        except Exception as get_e:
            logging.error(f"Failed to retrieve existing Engine details: {get_e}", exc_info=True)
            return None
    except Exception as e:
        logging.error(f"Error creating Search App (Engine): {e}", exc_info=True)
        return None


# --- Run the function ---
if __name__ == "__main__":
    engine_resource_name = create_search_engine_sample(
        project_id,
        location,
        engine_id,
        engine_display_name,
        [data_store_id_to_connect], # Pass the data store ID in a list
    )
    if engine_resource_name:
        logging.info(f"Script finished. Engine resource name: {engine_resource_name}")
    else:
        logging.error("Script finished with errors.")