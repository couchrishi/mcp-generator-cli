# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
from google.cloud import discoveryengine_v1alpha as discoveryengine
from google.api_core import exceptions as google_exceptions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_data_store_sample(
    project_id: str, location: str, data_store_id: str, data_store_name: str
) -> str | None:
    """Creates a Discovery Engine datastore with enhanced logging."""
    logging.info(f"Attempting to create data store '{data_store_id}' in project '{project_id}', location '{location}'...")

    try:
        client = discoveryengine.DataStoreServiceClient()

        parent = client.collection_path(
            project=project_id, location=location, collection="default_collection"
        )
        logging.info(f"Parent path constructed: {parent}")

        data_store = discoveryengine.DataStore(
            display_name=data_store_name,
            industry_vertical="GENERIC",
            solution_types=["SOLUTION_TYPE_SEARCH"],
            content_config=discoveryengine.DataStore.ContentConfig.NO_CONTENT, # Explicitly set NO_CONTENT
        )
        logging.info(f"DataStore object configured: {data_store}")

        logging.info("Initiating data store creation operation...")
        operation = client.create_data_store(
            parent=parent, data_store=data_store, data_store_id=data_store_id
        )

        logging.info(f"Waiting for operation to complete: {operation.operation.name}")
        response = operation.result()
        logging.info(f"Operation completed successfully.")

        metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

        logging.info(f"Data store created: {response}")
        logging.info(f"Resource name: {response.name}")
        logging.info(f"Creation time: {metadata.create_time}")

        return response.name

    except google_exceptions.AlreadyExists:
        logging.warning(f"Data store '{data_store_id}' already exists.")
        # Attempt to get the existing datastore details
        try:
            data_store_path = client.data_store_path(project_id, location, data_store_id)
            existing_ds = client.get_data_store(name=data_store_path)
            logging.info(f"Existing data store details: {existing_ds}")
            return existing_ds.name
        except Exception as get_e:
            logging.error(f"Failed to retrieve existing data store details: {get_e}", exc_info=True)
            return None
    except Exception as e:
        logging.error(f"Error creating data store: {e}", exc_info=True) # Log full traceback
        return None


# --- Set your specific values here ---
project_id = "saib-ai-playground"
location = "global"
data_store_id = "mcp-servers-datastore-v5" # Use v5 ID
data_store_name = "mcp-servers-datastore-v5" # Use v5 display name

# --- Run the function ---
if __name__ == "__main__":
    datastore_resource_name = create_data_store_sample(project_id, location, data_store_id, data_store_name)
    if datastore_resource_name:
        logging.info(f"Script finished. Data store resource name: {datastore_resource_name}")
    else:
        logging.error("Script finished with errors.")