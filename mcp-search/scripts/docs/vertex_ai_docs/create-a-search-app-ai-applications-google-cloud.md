# Create a search app  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/create-engine-es#genappbuilder_create_app-python](https://cloud.google.com/generative-ai-app-builder/docs/create-engine-es#genappbuilder_create_app-python)

Home
AI Applications
Documentation
Guides
Send feedback
Create a search app
Stay organized with collections
Save and categorize content based on your preferences.
This page describes how to create a search app.
Create an app
Console
To create a search app using the Google Cloud console, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
On the
Apps
page, click
add
Create app
.
On the
add
Create
app
page, under
Search for your website
, click
Create
.
Decide if you want Enterprise features for this app and then click the
toggle on or off. Turning on Enterprise edition features is required to get features such as
website search and choosing a region for your app. Enterprise edition
features incur additional cost. For more information, see
Enterprise edition features
.
Decide if you want advanced LLM features for this app and then click the
toggle on or off. Activating the advanced LLM features is required to get
features such as
search summaries
or
search with
follow-ups
. For more information, see
Advanced LLM
features
.
In the
Your app name
field, enter a name for your app.
In the
External name of your company or organization
field, enter the
common name for your company or organization. Avoid suffixes like Inc or LLC.
This field helps the LLM identify the company that the app represents.
Select a location for your app. Enterprise features must be turned on to
pick a location. Google recommends that you use the default,
global
(Global)
, unless you have a reason to restrict your data to a particular
geography.
Click
Continue
.
To connect to a data store, on the
Data stores
page, select a data store
that you previously created or create a new data store.
Choose one of the following options:
Select an existing data store: If you attach only one data store, you
cannot remove it or add other data stores to the app later. Attaching
multiple data stores lets you update the attached data stores later, but
the app always requires at least two data stores.
Create a new data store and ingest data into it:
Click
add
Create
data store
and follow the steps in the
Create a new data store
page.
Choose your new data store and click
Select
. For more
information, see
Create a search data store
.
REST
Before you use the command line to create an app, you must have an existing data
store. If you don't have a data store, create one following the steps in
Create a data store and ingest data for Vertex AI Search
.
To use the
engines.create
method to create a search app from
the command line, follow these steps:
Find your data store ID. If you already have your data store
ID, skip to the next step.
In the Google Cloud console, go to the
AI Applications
page and
in the navigation menu, click
Data Stores
.
Go to the Data Stores page
Click the name of your data store.
On the
Data
page for your data store, get the data store ID.
Create a search app and connect it to a data store. A data store
can be attached to only one app and can't be removed from the app later.
curl
-X
POST
\
-H
"Authorization: Bearer
$(
gcloud
auth
print-access-token
)
"
\
-H
"Content-Type: application/json"
\
-H
"X-Goog-User-Project:
PROJECT_ID
"
\
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines?engineId=
APP_ID
"
\
-d
'{
"displayName": "
APP_DISPLAY_NAME
",
"dataStoreIds": ["
DATA_STORE_ID
"],
"solutionType": "SOLUTION_TYPE_SEARCH",
"industryVertical": "
INDUSTRY_VERTICAL
",
"searchEngineConfig": {
"searchTier": "
SEARCH_TIER
",
"searchAddOns": ["
SEARCH_ADD_ON
"]
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you want to create.
APP_DISPLAY_NAME
: the display name of the Vertex AI Search app that you want to create.
DATA_STORE_ID
: the ID of an existing Vertex AI Search data store
that you want to add to the Vertex AI Search app.
INDUSTRY_VERTICAL
: the industry vertical that
the app is associated with. This field can take the values specified
in
IndustryVertical
.
For search apps with multiple data stores, also called
blended
search apps, you must specify this field as
GENERIC
.
SEARCH_TIER
: the search tier can be
SEARCH_TIER_STANDARD
or
SEARCH_TIER_ENTERPRISE
.
SEARCH_TIER_ENTERPRISE
is required to get features such
as website search and choosing a region for your app. Enterprise edition
features incur additional cost. For more information, see
Enterprise
edition features
.
SEARCH_ADD_ON
: if you want Advanced LLM features
for this app, then specify
SEARCH_ADD_ON_LLM
.
Advanced LLM features include
search summaries
and
search with follow-ups
.
If you don't want Advanced LLM features, then either specify
SEARCH_ADD_ON_UNSPECIFIED
or remove the
searchAddOns
field.
For more information, see
Advanced LLM features
.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
typing
import
List
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# engine_id = "YOUR_ENGINE_ID"
# data_store_ids = ["YOUR_DATA_STORE_ID"]
def
create_engine_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
data_store_ids
:
List
[
str
]
)
-
>
str
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
EngineServiceClient
(
client_options
=
client_options
)
# The full resource name of the collection
# e.g. projects/{project}/locations/{location}/collections/default_collection
parent
=
client
.
collection_path
(
project
=
project_id
,
location
=
location
,
collection
=
"default_collection"
,
)
engine
=
discoveryengine
.
Engine
(
display_name
=
"Test Engine"
,
# Options: GENERIC, MEDIA, HEALTHCARE_FHIR
industry_vertical
=
discoveryengine
.
IndustryVertical
.
GENERIC
,
# Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
solution_type
=
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
,
# For search apps only
search_engine_config
=
discoveryengine
.
Engine
.
SearchEngineConfig
(
# Options: SEARCH_TIER_STANDARD, SEARCH_TIER_ENTERPRISE
search_tier
=
discoveryengine
.
SearchTier
.
SEARCH_TIER_ENTERPRISE
,
# Options: SEARCH_ADD_ON_LLM, SEARCH_ADD_ON_UNSPECIFIED
search_add_ons
=
[
discoveryengine
.
SearchAddOn
.
SEARCH_ADD_ON_LLM
],
),
# For generic recommendation apps only
# similar_documents_config=discoveryengine.Engine.SimilarDocumentsEngineConfig,
data_store_ids
=
data_store_ids
,
)
request
=
discoveryengine
.
CreateEngineRequest
(
parent
=
parent
,
engine
=
engine
,
engine_id
=
engine_id
,
)
# Make the request
operation
=
client
.
create_engine
(
request
=
request
)
print
(
f
"Waiting for operation to complete:
{
operation
.
operation
.
name
}
"
)
response
=
operation
.
result
()
# After the operation is complete,
# get information from operation metadata
metadata
=
discoveryengine
.
CreateEngineMetadata
(
operation
.
metadata
)
# Handle the response
print
(
response
)
print
(
metadata
)
return
operation
.
operation
.
name
Terraform
To learn how to apply or remove a Terraform configuration, see
Basic Terraform commands
.
For more information, see the
Terraform
provider reference documentation
.
To create a search app using Terraform, see
discovery_engine_search_engine
.
What's next
Get search results
Add the search widget to a web page
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-12 UTC.

## Code Examples

### Code Example 1 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines?engineId=APP_ID" \
-d '{
  "displayName": "APP_DISPLAY_NAME",
  "dataStoreIds": ["DATA_STORE_ID"],
  "solutionType": "SOLUTION_TYPE_SEARCH",
  "industryVertical": "INDUSTRY_VERTICAL",
  "searchEngineConfig": {
     "searchTier": "SEARCH_TIER",
     "searchAddOns": ["SEARCH_ADD_ON"]
   }
}'

```

### Code Example 2 (text)

```text
from typing import List

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# engine_id = "YOUR_ENGINE_ID"
# data_store_ids = ["YOUR_DATA_STORE_ID"]


def create_engine_sample(
    project_id: str, location: str, engine_id: str, data_store_ids: List[str]
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.EngineServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    engine = discoveryengine.Engine(
        display_name="Test Engine",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_type=discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH,
        # For search apps only
        search_engine_config=discoveryengine.Engine.SearchEngineConfig(
            # Options: SEARCH_TIER_STANDARD, SEARCH_TIER_ENTERPRISE
            search_tier=discoveryengine.SearchTier.SEARCH_TIER_ENTERPRISE,
            # Options: SEARCH_ADD_ON_LLM, SEARCH_ADD_ON_UNSPECIFIED
            search_add_ons=[discoveryengine.SearchAddOn.SEARCH_ADD_ON_LLM],
        ),
        # For generic recommendation apps only
        # similar_documents_config=discoveryengine.Engine.SimilarDocumentsEngineConfig,
        data_store_ids=data_store_ids,
    )

    request = discoveryengine.CreateEngineRequest(
        parent=parent,
        engine=engine,
        engine_id=engine_id,
    )

    # Make the request
    operation = client.create_engine(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateEngineMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

