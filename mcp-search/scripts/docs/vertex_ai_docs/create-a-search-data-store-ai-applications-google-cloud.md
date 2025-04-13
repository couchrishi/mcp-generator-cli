# Create a search data store  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/create-data-store-es](https://cloud.google.com/generative-ai-app-builder/docs/create-data-store-es)

Home
AI Applications
Documentation
Guides
Send feedback
Create a search data store
Stay organized with collections
Save and categorize content based on your preferences.
To create a data store and ingest data for search, go to the section for the
source you plan to use:
Create a data store using website content
Import from BigQuery
Import from Cloud Storage
Sync from Google Drive
Sync from Gmail
(Public preview)
Sync from Google Sites
(Public preview)
Sync from Google Calendar
(Public preview)
Sync from Google Groups
(Public preview)
Sync people data
(Public preview)
Import from Cloud SQL
Import from Spanner
(Public preview)
Import from Firestore
Import from Bigtable
(Public Preview)
Import from AlloyDB for PostgreSQL
(Public Preview)
Upload structured JSON data with the API
Create a data store using Terraform
To sync data from a third-party data source instead, see
Connect a third-party data source
.
Create a data store using website content
Use the following procedure to create a data store and index websites.
To use a website data store after creating it, you must attach it to an app that
has Enterprise features turned on. You can turn on Enterprise Edition for an app
when you create it. This incurs additional costs. See
Create a search app
and
About advanced features
.
Console
To use the Google Cloud console to make a data store and index websites, follow
these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data Stores
.
Click
Create data store
.
On the
Source
page, select
Website Content
.
Choose whether to turn on
Advanced website indexing
for this data store.
This option can't be turned on or off later.
Advanced website indexing provides additional features such as search
summarization, search with follow-ups, and extractive answers. Advanced
website indexing incurs additional cost, and requires that you verify domain
ownership for any website that you index. For more information, see
Advanced website indexing
and
Pricing
.
In the
Sites to include
field, enter the URL patterns matching the
websites that you want to include in your data store. Include one URL
pattern per line, without comma separators. For example,
www.example.com/docs/*
Optional: In the
Sites to exclude
field, enter URL patterns that you
want to exclude from your data store.
To see the number of URL patterns you can include or exclude, see
Website data
.
Click
Continue
.
Select a location for your data store.
When you create a basic website search data store, this is always set
to
global (Global)
.
When you create a data store with advanced website indexing, you
can select a location. Because the websites that are indexed must be
public, Google strongly recommends that you select
global (Global)
as your location. This ensures maximum availability of
all search and answering services and eliminates the limitations of
regional data stores.
Enter a name for your data store.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data Stores
page.
To view information about your data store, click the name of your data store
in the
Name
column. Your data store page appears.
If you turned on
Advanced website indexing
, a warning appears prompting
you to verify the domains in your data store.
If you have a quota shortfall (the number of pages in the websites that
you specified exceeds the "Number of documents per project"
quota
for your project), an additional warning
appears prompting you to upgrade your quota.
To verify the domains for the URL patterns in your data store, follow the
instructions on the
Verify website domains
page.
To upgrade your quota, follow these steps:
Click
Upgrade quota
. The
IAM and Admin
page of the Google Cloud console appears.
Follow the instructions at
Request a higher quota
limit
in the Google Cloud documentation. The
quota to increase is
Number of documents
in the
Discovery Engine
API
service.
After submitting your request for a higher quota limit, go back to the
AI Applications
page and click
Data Stores
in the navigation menu.
Click the name of your data store in the
Name
column. The
Status
column indicates that indexing is in progress for the websites that had surpassed the quota. When the
Status
column for a URL shows
Indexed
,
advanced website indexing
features are available for that URL or URL pattern.
For more information, see
Quota for web page
indexing
in the "Quotas and limits" page.
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import websites
# from google.api_core.client_options import ClientOptions
#
# from google.cloud import discoveryengine_v1 as discoveryengine
#
# # TODO(developer): Uncomment these variables before running the sample.
# # project_id = "YOUR_PROJECT_ID"
# # location = "YOUR_LOCATION" # Values: "global"
# # data_store_id = "YOUR_DATA_STORE_ID"
# # NOTE: Do not include http or https protocol in the URI pattern
# # uri_pattern = "cloud.google.com/generative-ai-app-builder/docs/*"
#
# # For more information, refer to:
# # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
# client_options = (
# ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
# if location != "global"
# else None
# )
#
# # Create a client
# client = discoveryengine.SiteSearchEngineServiceClient(
# client_options=client_options
# )
#
# # The full resource name of the data store
# # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}
# site_search_engine = client.site_search_engine_path(
# project=project_id, location=location, data_store=data_store_id
# )
#
# # Target Site to index
# target_site = discoveryengine.TargetSite(
# provided_uri_pattern=uri_pattern,
# # Options: INCLUDE, EXCLUDE
# type_=discoveryengine.TargetSite.Type.INCLUDE,
# exact_match=False,
# )
#
# # Make the request
# operation = client.create_target_site(
# parent=site_search_engine,
# target_site=target_site,
# )
#
# print(f"Waiting for operation to complete: {operation.operation.name}")
# response = operation.result()
#
# # After the operation is complete,
# # get information from operation metadata
# metadata = discoveryengine.CreateTargetSiteMetadata(operation.metadata)
#
# # Handle the response
# print(response)
# print(metadata)
Next steps
To attach your website data store to an app, create an app with Enterprise
features enabled and select your data store following the steps in
Create a search app
.
If you've turned on advanced website indexing, you can
use structured data to update your schema
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from BigQuery
You can create data stores from BigQuery tables in two ways:
One-time ingestion
: You import data from a BigQuery table into a
data store. The data in the data store does not change unless you manually
refresh the data
.
Periodic ingestion
: You import data from one or more BigQuery
tables, and you set a sync frequency that determines how often the data
stores are updated with the most recent data from the BigQuery
dataset.
The following table compares the two ways that you can import BigQuery
data into Vertex AI Search data stores.
One-time ingestion
Periodic ingestion
Generally available (GA).
Public preview.
Data must be refreshed manually.
Data updates automatically every 1, 3, or 5 days. Data cannot be
manually refreshed.
Vertex AI Search creates a single data store from one
table
in a BigQuery.
Vertex AI Search creates a
data connector
for
a BigQuery
dataset
and a data store (called an
entity
data store) for each table specified. For each data
connector, the tables must have the same data type (for example,
structured) and be in the same BigQuery dataset.
Data from multiple tables can be combined in one data store by first
ingesting data from one table and then more data from another source or
BigQuery table.
Because manual data import is not supported, the data in an entity
data store can only be sourced from one BigQuery table.
Data source access control is supported.
Data source access control is not supported. The imported data can
contain access controls but these controls won't be respected.
You can create a data store using either the
Google Cloud console or the API.
You must use the console to create data connectors and their entity
data stores.
CMEK-compliant.
Not CMEK-compliant.
Import once from BigQuery
To ingest data from a BigQuery table, use the following steps to create
a data store and ingest data using either the Google Cloud console or the API.
Before importing your data, review
Prepare data for ingesting
.
Console
To use the Google Cloud console to ingest data from BigQuery, follow
these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
BigQuery
.
Select
what kind of data you are importing
.
Click
One time
.
In the
BigQuery path
field, click
Browse
, select a table that you
have
prepared for ingesting
, and then click
Select
.
Alternatively, enter the table location directly in the
BigQuery path
field.
Click
Continue
.
If you are doing one-time import of structured data:
Map fields to key properties.
If there are important fields missing from the schema, use
Add new
field
to add them.
For more information, see
About auto-detect and
edit
.
Click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
To check the status of your ingestion, go to the
Data Stores
page
and click your data store name to see details about it on its
Data
page.
When the status column on the
Activity
tab changes from
In progress
to
Import completed
, the ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes to several hours.
REST
To use the command line to create a data store and import data from
BigQuery, follow these steps.
Create a data store.
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
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DATA_STORE_DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"]
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store that you want to create. This ID can contain only lowercase
letters, digits, underscores, and hyphens.
DATA_STORE_DISPLAY_NAME
: the display name of the Vertex AI
Search data store that you want to create.
Optional: If you're uploading unstructured data and want to configure document
parsing or to turn on document chunking for RAG, specify the
documentProcessingConfig
object and include it in your data store creation request. Configuring an
OCR parser for PDFs is recommended if you're ingesting scanned PDFs. For how
to configure parsing or chunking options, see
Parse and chunk
documents
.
Import data from BigQuery.
If you defined a schema, make sure the data conforms to that schema.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"bigquerySource": {
"projectId": "
PROJECT_ID
",
"datasetId":"
DATASET_ID
",
"tableId": "
TABLE_ID
",
"dataSchema": "
DATA_SCHEMA
",
"aclEnabled": "
BOOLEAN
"
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
"errorConfig": {
"gcsPrefix": "
ERROR_DIRECTORY
"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store.
DATASET_ID
: the ID of the BigQuery
dataset.
TABLE_ID
: the ID of the BigQuery table.
If the BigQuery table is not under
PROJECT_ID
, you need to give the service account
service-<project
number>@gcp-sa-discoveryengine.iam.gserviceaccount.com
"BigQuery Data Viewer" permission for the
BigQuery table. For example, if you are importing
a BigQuery table from source project "123" to
destination project "456", give
service-456@gcp-sa-discoveryengine.iam.gserviceaccount.com
permissions for the BigQuery table under
project "123".
DATA_SCHEMA
: optional. Values are
document
and
custom
. The default is
document
.
document
: the BigQuery table
that you use must conform to the default BigQuery
schema provided in
Prepare data for ingesting
.
You can define the ID of each document yourself,
while wrapping all the data in the jsonData string.
custom
: Any BigQuery table
schema is accepted, and Vertex AI Search automatically
generates the IDs for each document that is imported.
ERROR_DIRECTORY
: optional. A Cloud Storage directory
for error information about the import—for example,
gs://<your-gcs-bucket>/directory/import_errors
. Google recommends
leaving this field empty to let Vertex AI Search
automatically create a temporary directory.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from BigQuery
to your data store. This does an upsert operation, which adds new
documents and replaces existing documents with updated documents
with the same ID. Specifying
FULL
causes a full rebase of the
documents in your data store. In other words, new and updated
documents are added to your data store, and documents that are not
in BigQuery are removed from your data store. The
FULL
mode is helpful if you want to automatically delete documents
that you no longer need.
AUTO_GENERATE_IDS
: optional. Specifies whether to
automatically generate document IDs. If set to
true
, document IDs
are generated based on a hash of the payload. Note that generated
document IDs might not remain consistent over multiple imports. If
you auto-generate IDs over multiple imports, Google highly
recommends setting
reconciliationMode
to
FULL
to maintain
consistent document IDs.
Specify
autoGenerateIds
only when
bigquerySource.dataSchema
is
set to
custom
. Otherwise an
INVALID_ARGUMENT
error is
returned. If you don't specify
autoGenerateIds
or set it to
false
, you must specify
idField
. Otherwise the documents fail to
import.
ID_FIELD
: optional. Specifies which fields are the
document IDs. For BigQuery source files,
idField
indicates the name of the column in the BigQuery
table that contains the document IDs.
Specify
idField
only when: (1)
bigquerySource.dataSchema
is set
to
custom
, and (2)
auto_generate_ids
is set to
false
or is
unspecified. Otherwise an
INVALID_ARGUMENT
error is returned.
The value of the BigQuery column name must be of
string type, must be between 1 and 63 characters, and must conform
to
RFC-1034
. Otherwise, the
documents fail to import.
C#
For more information, see the
AI Applications
C#
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
using
Google.Cloud.DiscoveryEngine.V1
;
using
Google.LongRunning
;
public
sealed
partial
class
GeneratedDataStoreServiceClientSnippets
{
/// <summary>Snippet for CreateDataStore</summary>
/// <remarks>
/// This snippet has been automatically generated and should be regarded as a code template only.
/// It will require modifications to work:
/// - It may require correct/in-range values for request initialization.
/// - It may require specifying regional endpoints when creating the service client as shown in
/// https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
/// </remarks>
public
void
CreateDataStoreRequestObject
()
{
// Create client
DataStoreServiceClient
dataStoreServiceClient
=
DataStoreServiceClient
.
Create
();
// Initialize request argument(s)
CreateDataStoreRequest
request
=
new
CreateDataStoreRequest
{
ParentAsCollectionName
=
CollectionName
.
FromProjectLocationCollection
(
"[PROJECT]"
,
"[LOCATION]"
,
"[COLLECTION]"
),
DataStore
=
new
DataStore
(),
DataStoreId
=
""
,
CreateAdvancedSiteSearch
=
false
,
SkipDefaultSchemaCreation
=
false
,
};
// Make the request
Operation<DataStore
,
CreateDataStoreMetadata
>
response
=
dataStoreServiceClient
.
CreateDataStore
(
request
);
// Poll until the returned long-running operation is complete
Operation<DataStore
,
CreateDataStoreMetadata
>
completedResponse
=
response
.
PollUntilCompleted
();
// Retrieve the operation result
DataStore
result
=
completedResponse
.
Result
;
// Or get the name of the operation
string
operationName
=
response
.
Name
;
// This name can be stored, then the long-running operation retrieved later by name
Operation<DataStore
,
CreateDataStoreMetadata
>
retrievedResponse
=
dataStoreServiceClient
.
PollOnceCreateDataStore
(
operationName
);
// Check if the retrieved long-running operation has completed
if
(
retrievedResponse
.
IsCompleted
)
{
// If it has completed, then access the result
DataStore
retrievedResult
=
retrievedResponse
.
Result
;
}
}
}
Import documents
using
Google.Cloud.DiscoveryEngine.V1
;
using
Google.LongRunning
;
using
Google.Protobuf.WellKnownTypes
;
public
sealed
partial
class
GeneratedDocumentServiceClientSnippets
{
/// <summary>Snippet for ImportDocuments</summary>
/// <remarks>
/// This snippet has been automatically generated and should be regarded as a code template only.
/// It will require modifications to work:
/// - It may require correct/in-range values for request initialization.
/// - It may require specifying regional endpoints when creating the service client as shown in
/// https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
/// </remarks>
public
void
ImportDocumentsRequestObject
()
{
// Create client
DocumentServiceClient
documentServiceClient
=
DocumentServiceClient
.
Create
();
// Initialize request argument(s)
ImportDocumentsRequest
request
=
new
ImportDocumentsRequest
{
ParentAsBranchName
=
BranchName
.
FromProjectLocationDataStoreBranch
(
"[PROJECT]"
,
"[LOCATION]"
,
"[DATA_STORE]"
,
"[BRANCH]"
),
InlineSource
=
new
ImportDocumentsRequest
.
Types
.
InlineSource
(),
ErrorConfig
=
new
ImportErrorConfig
(),
ReconciliationMode
=
ImportDocumentsRequest
.
Types
.
ReconciliationMode
.
Unspecified
,
UpdateMask
=
new
FieldMask
(),
AutoGenerateIds
=
false
,
IdField
=
""
,
ForceRefreshContent
=
false
,
};
// Make the request
Operation<ImportDocumentsResponse
,
ImportDocumentsMetadata
>
response
=
documentServiceClient
.
ImportDocuments
(
request
);
// Poll until the returned long-running operation is complete
Operation<ImportDocumentsResponse
,
ImportDocumentsMetadata
>
completedResponse
=
response
.
PollUntilCompleted
();
// Retrieve the operation result
ImportDocumentsResponse
result
=
completedResponse
.
Result
;
// Or get the name of the operation
string
operationName
=
response
.
Name
;
// This name can be stored, then the long-running operation retrieved later by name
Operation<ImportDocumentsResponse
,
ImportDocumentsMetadata
>
retrievedResponse
=
documentServiceClient
.
PollOnceImportDocuments
(
operationName
);
// Check if the retrieved long-running operation has completed
if
(
retrievedResponse
.
IsCompleted
)
{
// If it has completed, then access the result
ImportDocumentsResponse
retrievedResult
=
retrievedResponse
.
Result
;
}
}
}
Go
For more information, see the
AI Applications
Go
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
package
main
import
(
"context"
discoveryengine
"cloud.google.com/go/discoveryengine/apiv1"
discoveryenginepb
"cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)
func
main
()
{
ctx
:=
context
.
Background
()
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in:
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
c
,
err
:=
discoveryengine
.
NewDataStoreClient
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
defer
c
.
Close
()
req
:=
&
discoveryenginepb
.
CreateDataStoreRequest
{
// TODO: Fill request struct fields.
// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CreateDataStoreRequest.
}
op
,
err
:=
c
.
CreateDataStore
(
ctx
,
req
)
if
err
!=
nil
{
// TODO: Handle error.
}
resp
,
err
:=
op
.
Wait
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
// TODO: Use resp.
_
=
resp
}
Import documents
package
main
import
(
"context"
discoveryengine
"cloud.google.com/go/discoveryengine/apiv1"
discoveryenginepb
"cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)
func
main
()
{
ctx
:=
context
.
Background
()
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in:
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
c
,
err
:=
discoveryengine
.
NewDocumentClient
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
defer
c
.
Close
()
req
:=
&
discoveryenginepb
.
ImportDocumentsRequest
{
// TODO: Fill request struct fields.
// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#ImportDocumentsRequest.
}
op
,
err
:=
c
.
ImportDocuments
(
ctx
,
req
)
if
err
!=
nil
{
// TODO: Handle error.
}
resp
,
err
:=
op
.
Wait
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
// TODO: Use resp.
_
=
resp
}
Java
For more information, see the
AI Applications
Java
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
import
com.google.cloud.discoveryengine.v1.CollectionName
;
import
com.google.cloud.discoveryengine.v1.CreateDataStoreRequest
;
import
com.google.cloud.discoveryengine.v1.DataStore
;
import
com.google.cloud.discoveryengine.v1.DataStoreServiceClient
;
public
class
SyncCreateDataStore
{
public
static
void
main
(
String
[]
args
)
throws
Exception
{
syncCreateDataStore
();
}
public
static
void
syncCreateDataStore
()
throws
Exception
{
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in
// https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
try
(
DataStoreServiceClient
dataStoreServiceClient
=
DataStoreServiceClient
.
create
())
{
CreateDataStoreRequest
request
=
CreateDataStoreRequest
.
newBuilder
()
.
setParent
(
CollectionName
.
of
(
"[PROJECT]"
,
"[LOCATION]"
,
"[COLLECTION]"
).
toString
())
.
setDataStore
(
DataStore
.
newBuilder
().
build
())
.
setDataStoreId
(
"dataStoreId929489618"
)
.
setCreateAdvancedSiteSearch
(
true
)
.
setSkipDefaultSchemaCreation
(
true
)
.
build
();
DataStore
response
=
dataStoreServiceClient
.
createDataStoreAsync
(
request
).
get
();
}
}
}
Import documents
import
com.google.cloud.discoveryengine.v1.BranchName
;
import
com.google.cloud.discoveryengine.v1.DocumentServiceClient
;
import
com.google.cloud.discoveryengine.v1.ImportDocumentsRequest
;
import
com.google.cloud.discoveryengine.v1.ImportDocumentsResponse
;
import
com.google.cloud.discoveryengine.v1.ImportErrorConfig
;
import
com.google.protobuf.FieldMask
;
public
class
SyncImportDocuments
{
public
static
void
main
(
String
[]
args
)
throws
Exception
{
syncImportDocuments
();
}
public
static
void
syncImportDocuments
()
throws
Exception
{
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in
// https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
try
(
DocumentServiceClient
documentServiceClient
=
DocumentServiceClient
.
create
())
{
ImportDocumentsRequest
request
=
ImportDocumentsRequest
.
newBuilder
()
.
setParent
(
BranchName
.
ofProjectLocationDataStoreBranchName
(
"[PROJECT]"
,
"[LOCATION]"
,
"[DATA_STORE]"
,
"[BRANCH]"
)
.
toString
())
.
setErrorConfig
(
ImportErrorConfig
.
newBuilder
().
build
())
.
setUpdateMask
(
FieldMask
.
newBuilder
().
build
())
.
setAutoGenerateIds
(
true
)
.
setIdField
(
"idField1629396127"
)
.
build
();
ImportDocumentsResponse
response
=
documentServiceClient
.
importDocumentsAsync
(
request
).
get
();
}
}
}
Node.js
For more information, see the
AI Applications
Node.js
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
/**
* This snippet has been automatically generated and should be regarded as a code template only.
* It will require modifications to work.
* It may require correct/in-range values for request initialization.
* TODO(developer): Uncomment these variables before running the sample.
*/
/**
* Required. The parent resource name, such as
* `projects/{project}/locations/{location}/collections/{collection}`.
*/
// const parent = 'abc123'
/**
* Required. The DataStore google.cloud.discoveryengine.v1.DataStore to
* create.
*/
// const dataStore = {}
/**
* Required. The ID to use for the
* DataStore google.cloud.discoveryengine.v1.DataStore, which will become
* the final component of the
* DataStore google.cloud.discoveryengine.v1.DataStore's resource name.
* This field must conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
* standard with a length limit of 63 characters. Otherwise, an
* INVALID_ARGUMENT error is returned.
*/
// const dataStoreId = 'abc123'
/**
* A boolean flag indicating whether user want to directly create an advanced
* data store for site search.
* If the data store is not configured as site
* search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will
* be ignored.
*/
// const createAdvancedSiteSearch = true
/**
* A boolean flag indicating whether to skip the default schema creation for
* the data store. Only enable this flag if you are certain that the default
* schema is incompatible with your use case.
* If set to true, you must manually create a schema for the data store before
* any documents can be ingested.
* This flag cannot be specified if `data_store.starting_schema` is specified.
*/
// const skipDefaultSchemaCreation = true
// Imports the Discoveryengine library
const
{
DataStoreServiceClient
}
=
require
(
'@google-cloud/discoveryengine'
).
v1
;
// Instantiates a client
const
discoveryengineClient
=
new
DataStoreServiceClient
();
async
function
callCreateDataStore
()
{
// Construct request
const
request
=
{
parent
,
dataStore
,
dataStoreId
,
};
// Run request
const
[
operation
]
=
await
discoveryengineClient
.
createDataStore
(
request
);
const
[
response
]
=
await
operation
.
promise
();
console
.
log
(
response
);
}
callCreateDataStore
();
Import documents
/**
* This snippet has been automatically generated and should be regarded as a code template only.
* It will require modifications to work.
* It may require correct/in-range values for request initialization.
* TODO(developer): Uncomment these variables before running the sample.
*/
/**
* The Inline source for the input content for documents.
*/
// const inlineSource = {}
/**
* Cloud Storage location for the input content.
*/
// const gcsSource = {}
/**
* BigQuery input source.
*/
// const bigquerySource = {}
/**
* FhirStore input source.
*/
// const fhirStoreSource = {}
/**
* Spanner input source.
*/
// const spannerSource = {}
/**
* Cloud SQL input source.
*/
// const cloudSqlSource = {}
/**
* Firestore input source.
*/
// const firestoreSource = {}
/**
* AlloyDB input source.
*/
// const alloyDbSource = {}
/**
* Cloud Bigtable input source.
*/
// const bigtableSource = {}
/**
* Required. The parent branch resource name, such as
* `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
* Requires create/update permission.
*/
// const parent = 'abc123'
/**
* The desired location of errors incurred during the Import.
*/
// const errorConfig = {}
/**
* The mode of reconciliation between existing documents and the documents to
* be imported. Defaults to
* ReconciliationMode.INCREMENTAL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL.
*/
// const reconciliationMode = {}
/**
* Indicates which fields in the provided imported documents to update. If
* not set, the default is to update all fields.
*/
// const updateMask = {}
/**
* Whether to automatically generate IDs for the documents if absent.
* If set to `true`,
* Document.id google.cloud.discoveryengine.v1.Document.id s are
* automatically generated based on the hash of the payload, where IDs may not
* be consistent during multiple imports. In which case
* ReconciliationMode.FULL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.FULL
* is highly recommended to avoid duplicate contents. If unset or set to
* `false`, Document.id google.cloud.discoveryengine.v1.Document.id s have
* to be specified using
* id_field google.cloud.discoveryengine.v1.ImportDocumentsRequest.id_field,
* otherwise, documents without IDs fail to be imported.
* Supported data sources:
* * GcsSource google.cloud.discoveryengine.v1.GcsSource.
* GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
* BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
* * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
* * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
* * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
*/
// const autoGenerateIds = true
/**
* The field indicates the ID field or column to be used as unique IDs of
* the documents.
* For GcsSource google.cloud.discoveryengine.v1.GcsSource it is the key of
* the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`.
* For others, it may be the column name of the table where the unique ids are
* stored.
* The values of the JSON field or the table column are used as the
* Document.id google.cloud.discoveryengine.v1.Document.id s. The JSON field
* or the table column must be of string type, and the values must be set as
* valid strings conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
* with 1-63 characters. Otherwise, documents without valid IDs fail to be
* imported.
* Only set this field when
* auto_generate_ids google.cloud.discoveryengine.v1.ImportDocumentsRequest.auto_generate_ids
* is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.
* If it is unset, a default value `_id` is used when importing from the
* allowed data sources.
* Supported data sources:
* * GcsSource google.cloud.discoveryengine.v1.GcsSource.
* GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
* BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
* * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
* * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
* * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
*/
// const idField = 'abc123'
/**
* Optional. Whether to force refresh the unstructured content of the
* documents.
* If set to `true`, the content part of the documents will be refreshed
* regardless of the update status of the referencing content.
*/
// const forceRefreshContent = true
// Imports the Discoveryengine library
const
{
DocumentServiceClient
}
=
require
(
'@google-cloud/discoveryengine'
).
v1
;
// Instantiates a client
const
discoveryengineClient
=
new
DocumentServiceClient
();
async
function
callImportDocuments
()
{
// Construct request
const
request
=
{
parent
,
};
// Run request
const
[
operation
]
=
await
discoveryengineClient
.
importDocuments
(
request
);
const
[
response
]
=
await
operation
.
promise
();
console
.
log
(
response
);
}
callImportDocuments
();
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# bigquery_dataset = "YOUR_BIGQUERY_DATASET"
# bigquery_table = "YOUR_BIGQUERY_TABLE"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
bigquery_source
=
discoveryengine
.
BigQuerySource
(
project_id
=
project_id
,
dataset_id
=
bigquery_dataset
,
table_id
=
bigquery_table
,
data_schema
=
"custom"
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Ruby
For more information, see the
AI Applications
Ruby
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
require
"google/cloud/discovery_engine/v1"
##
# Snippet for the create_data_store call in the DataStoreService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store.
#
def
create_data_store
# Create a client object. The client can be reused for multiple calls.
client
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
DataStoreService
::
Client
.
new
# Create a request. To set request fields, pass in keyword arguments.
request
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
CreateDataStoreRequest
.
new
# Call the create_data_store method.
result
=
client
.
create_data_store
request
# The returned object is of type Gapic::Operation. You can use it to
# check the status of an operation, cancel it, or wait for results.
# Here is how to wait for a response.
result
.
wait_until_done!
timeout
:
60
if
result
.
response?
p
result
.
response
else
puts
"No response received."
end
end
Import documents
require
"google/cloud/discovery_engine/v1"
##
# Snippet for the import_documents call in the DocumentService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#import_documents.
#
def
import_documents
# Create a client object. The client can be reused for multiple calls.
client
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
DocumentService
::
Client
.
new
# Create a request. To set request fields, pass in keyword arguments.
request
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
ImportDocumentsRequest
.
new
# Call the import_documents method.
result
=
client
.
import_documents
request
# The returned object is of type Gapic::Operation. You can use it to
# check the status of an operation, cancel it, or wait for results.
# Here is how to wait for a response.
result
.
wait_until_done!
timeout
:
60
if
result
.
response?
p
result
.
response
else
puts
"No response received."
end
end
Connect to BigQuery with periodic syncing
Before importing your data, review
Prepare data for ingesting
.
The following procedure describes how to create a data connector that associates
a BigQuery dataset with a Vertex AI Search data
connector and how to specify a table on the dataset for each data store you want
to create. Data stores that are children of data connectors are called
entity
data stores.
Data from the dataset is synced periodically to the entity data stores. You can
specify synchronization daily, every three days, or every five days.
Console
To use the Google Cloud console to create a connector that periodically syncs data
from a BigQuery dataset to Vertex AI Search, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data Stores
.
Click
Create data store
.
On the
Source
page, select
BigQuery
.
Select the kind of data that you are importing.
Click
Periodic
.
Select the
Sync frequency
, how often you want the
Vertex AI Search connector to sync with the BigQuery
dataset. You can change the frequency later.
In the
BigQuery dataset path
field, click
Browse
, select the dataset
that contains the tables that you have
prepared for
ingesting
. Alternatively, enter the table location directly
in the
BigQuery path
field. The format for the path is
projectname.datasetname
.
In the
Tables to sync
field, click
Browse
, and then select a table
that contains the data that you want for your data store.
If there are additional tables in the dataset that that you want to use for
data stores, click
Add table
and specify those tables too.
Click
Continue
.
Choose a region for your data store, enter a name for your data connector,
and click
Create
.
You have now created a data connector, which will periodically sync data
with the BigQuery dataset. And, you have created one or more entity
data stores. The data stores have the same names as the BigQuery
tables.
To check the status of your ingestion, go to the
Data Stores
page
and click your data connector name to see details about it on its
Data
page >
Data ingestion activity
tab. When the status column on the
Activity
tab changes from
In progress
to
succeeded
, the first
ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes to several hours.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
About an hour after the data connector is created, the first sync occurs.
The next sync then occurs around 24 hours, 72 hours,
or 120 hours later.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from Cloud Storage
You can create data stores from Cloud Storage tables in two ways:
One-time ingestion
: You import data from a Cloud Storage folder or file
into a data store. The data in the data store doesn't change unless you
manually
refresh the data
.
Periodic ingestion
: You import data from a Cloud Storage folder or
file, and you set a sync frequency that determines how often the data
store is updated with the most recent data from that Cloud Storage
location.
The following table compares the two ways that you can import Cloud Storage
data into Vertex AI Search data stores.
One-time ingestion
Periodic ingestion
Generally available (GA).
Public preview.
Data must be refreshed manually.
Data updates automatically every one, three, or five days. Data cannot be
manually refreshed.
Vertex AI Search creates a single data store from one
folder or file in Cloud Storage.
Vertex AI Search creates a
data connector
, and
associates a data store (called an
entity
data store) with it for
the file or folder that is specified. Each Cloud Storage data connector
can have a single entity data store.
Data from multiple files, folders, and buckets can be combined in one
data store by first ingesting data from one Cloud Storage location and
then more data from another location.
Because manual data import is not supported, the data in an entity
data store can only be sourced from one Cloud Storage file or folder.
Data source access control is supported. For more information, see
Data source access control
.
Data source access control is not supported. The imported data can
contain access controls but these controls won't be respected.
You can create a data store using either the
Google Cloud console or the API.
You must use the console to create data connectors and their entity
data stores.
CMEK-compliant
.
Not CMEK-compliant.
Import once from Cloud Storage
To ingest data from Cloud Storage, use the following steps to create
a data store and ingest data using either the Google Cloud console or the API.
Before importing your data, review
Prepare data for ingesting
.
Console
To use the console to ingest data from a Cloud Storage bucket, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Cloud Storage
.
In the
Select a folder or file you want to import
section, select
Folder
or
File
.
Click
Browse
and choose the data you have
prepared for ingesting
, and then click
Select
.
Alternatively, enter the location directly in the
gs://
field.
Select what kind of data you are importing.
Click
Continue
.
If you are doing one-time import of structured data:
Map fields to key properties.
If there are important fields missing from the schema, use
Add new
field
to add them.
For more information, see
About auto-detect and
edit
.
Click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Optional: If you selected unstructured documents, you can select parsing and
chunking options for your documents. To compare parsers, see
Parse
documents
. For information about chunking see
Chunk documents for
RAG
.
The OCR parser and layout parser can incur additional costs. See
Document
AI feature pricing
.
To select a parser, expand
Document processing options
and specify the
parser options that you want to use.
Click
Create
.
To check the status of your ingestion, go to the
Data Stores
page
and click your data store name to see details about it on its
Data
page.
When the status column on the
Activity
tab changes from
In progress
to
Import completed
, the ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes or several hours.
REST
To use the command line to create a data store and ingest data from
Cloud Storage, follow these steps.
Create a data store.
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
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DATA_STORE_DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
"contentConfig": "CONTENT_REQUIRED",
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store that you want to create. This ID can contain only lowercase
letters, digits, underscores, and hyphens.
DATA_STORE_DISPLAY_NAME
: the display name of the Vertex AI
Search data store that you want to create.
Optional: To configure document parsing or to turn on document
chunking for RAG, specify the
documentProcessingConfig
object and include it in your data store creation request. Configuring an
OCR parser for PDFs is recommended if you're ingesting scanned PDFs. For how
to configure parsing or chunking options, see
Parse and chunk
documents
.
Import data from Cloud Storage.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"gcsSource": {
"inputUris": ["
INPUT_FILE_PATTERN_1
", "
INPUT_FILE_PATTERN_2
"],
"dataSchema": "
DATA_SCHEMA
",
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
"errorConfig": {
"gcsPrefix": "
ERROR_DIRECTORY
"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store.
INPUT_FILE_PATTERN
: a file pattern in Cloud Storage
containing your documents.
For structured data or for unstructured data with metadata,
an example of the input file pattern is
gs://<your-gcs-bucket>/directory/object.json
and an example of
pattern matching one or more files is
gs://<your-gcs-bucket>/directory/*.json
.
For unstructured documents, an example is
gs://<your-gcs-bucket>/directory/*.pdf
. Each file that is matched
by the pattern becomes a document.
If
<your-gcs-bucket>
is not under
PROJECT_ID
, you
need to give the service account
service-<project
number>@gcp-sa-discoveryengine.iam.gserviceaccount.com
"Storage
Object Viewer" permissions for the Cloud Storage bucket. For
example, if you are importing a Cloud Storage bucket from
source project "123" to destination project "456", give
service-456@gcp-sa-discoveryengine.iam.gserviceaccount.com
permissions on the Cloud Storage bucket under project "123".
DATA_SCHEMA
: optional. Values are
document
,
custom
,
csv
, and
content
. The default is
document
.
document
: Upload unstructured data with metadata for
unstructured documents. Each line of the file has to follow one
of the following formats. You can define the ID of each document:
{ "id": "<your-id>", "jsonData": "<JSON string>",
"content": { "mimeType": "<application/pdf or text/html>", "uri":
"gs://<your-gcs-bucket>/directory/filename.pdf" } }
{ "id": "<your-id>", "structData": <JSON object>,
"content": { "mimeType": "<application/pdf or text/html>", "uri":
"gs://<your-gcs-bucket>/directory/filename.pdf" } }
custom
: Upload JSON for structured documents. The data is
organized according to a schema. You can specify the schema;
otherwise it is auto-detected. You can put the JSON string of the
document in a consistent format directly in each line, and
Vertex AI Search automatically generates the IDs
for each document imported.
content
: Upload unstructured documents (PDF, HTML, DOC, TXT,
PPTX). The ID of each document is automatically generated as the
first 128 bits of SHA256(GCS_URI) encoded as a hex string. You can
specify multiple input file patterns as long as the matched files
don't exceed the 100K files limit.
csv
: Include a header row in your CSV file,
with each header mapped to a document field. Specify the path to
the CSV file using the
inputUris
field.
ERROR_DIRECTORY
: optional. A Cloud Storage directory
for error information about the import—for example,
gs://<your-gcs-bucket>/directory/import_errors
. Google recommends
leaving this field empty to let Vertex AI Search
automatically create a temporary directory.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from Cloud Storage to your
data store. This does an upsert operation, which adds new documents
and replaces existing documents with updated documents with the same
ID. Specifying
FULL
causes a full rebase of the documents in your
data store. In other words, new and updated documents are added to
your data store, and documents that are not in Cloud Storage are
removed from your data store. The
FULL
mode is helpful if you want
to automatically delete documents that you no longer need.
AUTO_GENERATE_IDS
: optional. Specifies whether to
automatically generate document IDs. If set to
true
, document IDs
are generated based on a hash of the payload. Note that generated
document IDs might not remain consistent over multiple imports. If
you auto-generate IDs over multiple imports, Google highly
recommends setting
reconciliationMode
to
FULL
to maintain
consistent document IDs.
Specify
autoGenerateIds
only when
gcsSource.dataSchema
is set to
custom
or
csv
. Otherwise an
INVALID_ARGUMENT
error is
returned. If you don't specify
autoGenerateIds
or set it to
false
, you must specify
idField
. Otherwise the documents fail to
import.
ID_FIELD
: optional. Specifies which fields are the
document IDs. For Cloud Storage source documents,
idField
specifies the name in the JSON fields that are document IDs. For
example, if
{"my_id":"some_uuid"}
is the document ID field in one
of your documents, specify
"idField":"my_id"
. This identifies all
JSON fields with the name
"my_id"
as document IDs.
Specify this field only when: (1)
gcsSource.dataSchema
is set to
custom
or
csv
, and (2)
auto_generate_ids
is set to
false
or
is unspecified. Otherwise an
INVALID_ARGUMENT
error is returned.
Note that the value of the Cloud Storage JSON field must be of
string type, must be between 1-63 characters, and must conform to
RFC-1034
. Otherwise, the
documents fail to import.
Note that the JSON field name specified by
id_field
must be of
string type, must be between 1 and 63 characters, and must conform
to
RFC-1034
. Otherwise, the
documents fail to import.
C#
For more information, see the
AI Applications
C#
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
using
Google.Cloud.DiscoveryEngine.V1
;
using
Google.LongRunning
;
public
sealed
partial
class
GeneratedDataStoreServiceClientSnippets
{
/// <summary>Snippet for CreateDataStore</summary>
/// <remarks>
/// This snippet has been automatically generated and should be regarded as a code template only.
/// It will require modifications to work:
/// - It may require correct/in-range values for request initialization.
/// - It may require specifying regional endpoints when creating the service client as shown in
/// https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
/// </remarks>
public
void
CreateDataStoreRequestObject
()
{
// Create client
DataStoreServiceClient
dataStoreServiceClient
=
DataStoreServiceClient
.
Create
();
// Initialize request argument(s)
CreateDataStoreRequest
request
=
new
CreateDataStoreRequest
{
ParentAsCollectionName
=
CollectionName
.
FromProjectLocationCollection
(
"[PROJECT]"
,
"[LOCATION]"
,
"[COLLECTION]"
),
DataStore
=
new
DataStore
(),
DataStoreId
=
""
,
CreateAdvancedSiteSearch
=
false
,
SkipDefaultSchemaCreation
=
false
,
};
// Make the request
Operation<DataStore
,
CreateDataStoreMetadata
>
response
=
dataStoreServiceClient
.
CreateDataStore
(
request
);
// Poll until the returned long-running operation is complete
Operation<DataStore
,
CreateDataStoreMetadata
>
completedResponse
=
response
.
PollUntilCompleted
();
// Retrieve the operation result
DataStore
result
=
completedResponse
.
Result
;
// Or get the name of the operation
string
operationName
=
response
.
Name
;
// This name can be stored, then the long-running operation retrieved later by name
Operation<DataStore
,
CreateDataStoreMetadata
>
retrievedResponse
=
dataStoreServiceClient
.
PollOnceCreateDataStore
(
operationName
);
// Check if the retrieved long-running operation has completed
if
(
retrievedResponse
.
IsCompleted
)
{
// If it has completed, then access the result
DataStore
retrievedResult
=
retrievedResponse
.
Result
;
}
}
}
Import documents
using
Google.Cloud.DiscoveryEngine.V1
;
using
Google.LongRunning
;
using
Google.Protobuf.WellKnownTypes
;
public
sealed
partial
class
GeneratedDocumentServiceClientSnippets
{
/// <summary>Snippet for ImportDocuments</summary>
/// <remarks>
/// This snippet has been automatically generated and should be regarded as a code template only.
/// It will require modifications to work:
/// - It may require correct/in-range values for request initialization.
/// - It may require specifying regional endpoints when creating the service client as shown in
/// https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
/// </remarks>
public
void
ImportDocumentsRequestObject
()
{
// Create client
DocumentServiceClient
documentServiceClient
=
DocumentServiceClient
.
Create
();
// Initialize request argument(s)
ImportDocumentsRequest
request
=
new
ImportDocumentsRequest
{
ParentAsBranchName
=
BranchName
.
FromProjectLocationDataStoreBranch
(
"[PROJECT]"
,
"[LOCATION]"
,
"[DATA_STORE]"
,
"[BRANCH]"
),
InlineSource
=
new
ImportDocumentsRequest
.
Types
.
InlineSource
(),
ErrorConfig
=
new
ImportErrorConfig
(),
ReconciliationMode
=
ImportDocumentsRequest
.
Types
.
ReconciliationMode
.
Unspecified
,
UpdateMask
=
new
FieldMask
(),
AutoGenerateIds
=
false
,
IdField
=
""
,
ForceRefreshContent
=
false
,
};
// Make the request
Operation<ImportDocumentsResponse
,
ImportDocumentsMetadata
>
response
=
documentServiceClient
.
ImportDocuments
(
request
);
// Poll until the returned long-running operation is complete
Operation<ImportDocumentsResponse
,
ImportDocumentsMetadata
>
completedResponse
=
response
.
PollUntilCompleted
();
// Retrieve the operation result
ImportDocumentsResponse
result
=
completedResponse
.
Result
;
// Or get the name of the operation
string
operationName
=
response
.
Name
;
// This name can be stored, then the long-running operation retrieved later by name
Operation<ImportDocumentsResponse
,
ImportDocumentsMetadata
>
retrievedResponse
=
documentServiceClient
.
PollOnceImportDocuments
(
operationName
);
// Check if the retrieved long-running operation has completed
if
(
retrievedResponse
.
IsCompleted
)
{
// If it has completed, then access the result
ImportDocumentsResponse
retrievedResult
=
retrievedResponse
.
Result
;
}
}
}
Go
For more information, see the
AI Applications
Go
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
package
main
import
(
"context"
discoveryengine
"cloud.google.com/go/discoveryengine/apiv1"
discoveryenginepb
"cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)
func
main
()
{
ctx
:=
context
.
Background
()
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in:
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
c
,
err
:=
discoveryengine
.
NewDataStoreClient
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
defer
c
.
Close
()
req
:=
&
discoveryenginepb
.
CreateDataStoreRequest
{
// TODO: Fill request struct fields.
// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CreateDataStoreRequest.
}
op
,
err
:=
c
.
CreateDataStore
(
ctx
,
req
)
if
err
!=
nil
{
// TODO: Handle error.
}
resp
,
err
:=
op
.
Wait
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
// TODO: Use resp.
_
=
resp
}
Import documents
package
main
import
(
"context"
discoveryengine
"cloud.google.com/go/discoveryengine/apiv1"
discoveryenginepb
"cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)
func
main
()
{
ctx
:=
context
.
Background
()
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in:
// https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
c
,
err
:=
discoveryengine
.
NewDocumentClient
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
defer
c
.
Close
()
req
:=
&
discoveryenginepb
.
ImportDocumentsRequest
{
// TODO: Fill request struct fields.
// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#ImportDocumentsRequest.
}
op
,
err
:=
c
.
ImportDocuments
(
ctx
,
req
)
if
err
!=
nil
{
// TODO: Handle error.
}
resp
,
err
:=
op
.
Wait
(
ctx
)
if
err
!=
nil
{
// TODO: Handle error.
}
// TODO: Use resp.
_
=
resp
}
Java
For more information, see the
AI Applications
Java
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
import
com.google.cloud.discoveryengine.v1.CollectionName
;
import
com.google.cloud.discoveryengine.v1.CreateDataStoreRequest
;
import
com.google.cloud.discoveryengine.v1.DataStore
;
import
com.google.cloud.discoveryengine.v1.DataStoreServiceClient
;
public
class
SyncCreateDataStore
{
public
static
void
main
(
String
[]
args
)
throws
Exception
{
syncCreateDataStore
();
}
public
static
void
syncCreateDataStore
()
throws
Exception
{
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in
// https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
try
(
DataStoreServiceClient
dataStoreServiceClient
=
DataStoreServiceClient
.
create
())
{
CreateDataStoreRequest
request
=
CreateDataStoreRequest
.
newBuilder
()
.
setParent
(
CollectionName
.
of
(
"[PROJECT]"
,
"[LOCATION]"
,
"[COLLECTION]"
).
toString
())
.
setDataStore
(
DataStore
.
newBuilder
().
build
())
.
setDataStoreId
(
"dataStoreId929489618"
)
.
setCreateAdvancedSiteSearch
(
true
)
.
setSkipDefaultSchemaCreation
(
true
)
.
build
();
DataStore
response
=
dataStoreServiceClient
.
createDataStoreAsync
(
request
).
get
();
}
}
}
Import documents
import
com.google.cloud.discoveryengine.v1.BranchName
;
import
com.google.cloud.discoveryengine.v1.DocumentServiceClient
;
import
com.google.cloud.discoveryengine.v1.ImportDocumentsRequest
;
import
com.google.cloud.discoveryengine.v1.ImportDocumentsResponse
;
import
com.google.cloud.discoveryengine.v1.ImportErrorConfig
;
import
com.google.protobuf.FieldMask
;
public
class
SyncImportDocuments
{
public
static
void
main
(
String
[]
args
)
throws
Exception
{
syncImportDocuments
();
}
public
static
void
syncImportDocuments
()
throws
Exception
{
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in
// https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
try
(
DocumentServiceClient
documentServiceClient
=
DocumentServiceClient
.
create
())
{
ImportDocumentsRequest
request
=
ImportDocumentsRequest
.
newBuilder
()
.
setParent
(
BranchName
.
ofProjectLocationDataStoreBranchName
(
"[PROJECT]"
,
"[LOCATION]"
,
"[DATA_STORE]"
,
"[BRANCH]"
)
.
toString
())
.
setErrorConfig
(
ImportErrorConfig
.
newBuilder
().
build
())
.
setUpdateMask
(
FieldMask
.
newBuilder
().
build
())
.
setAutoGenerateIds
(
true
)
.
setIdField
(
"idField1629396127"
)
.
build
();
ImportDocumentsResponse
response
=
documentServiceClient
.
importDocumentsAsync
(
request
).
get
();
}
}
}
Node.js
For more information, see the
AI Applications
Node.js
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
/**
* This snippet has been automatically generated and should be regarded as a code template only.
* It will require modifications to work.
* It may require correct/in-range values for request initialization.
* TODO(developer): Uncomment these variables before running the sample.
*/
/**
* Required. The parent resource name, such as
* `projects/{project}/locations/{location}/collections/{collection}`.
*/
// const parent = 'abc123'
/**
* Required. The DataStore google.cloud.discoveryengine.v1.DataStore to
* create.
*/
// const dataStore = {}
/**
* Required. The ID to use for the
* DataStore google.cloud.discoveryengine.v1.DataStore, which will become
* the final component of the
* DataStore google.cloud.discoveryengine.v1.DataStore's resource name.
* This field must conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
* standard with a length limit of 63 characters. Otherwise, an
* INVALID_ARGUMENT error is returned.
*/
// const dataStoreId = 'abc123'
/**
* A boolean flag indicating whether user want to directly create an advanced
* data store for site search.
* If the data store is not configured as site
* search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will
* be ignored.
*/
// const createAdvancedSiteSearch = true
/**
* A boolean flag indicating whether to skip the default schema creation for
* the data store. Only enable this flag if you are certain that the default
* schema is incompatible with your use case.
* If set to true, you must manually create a schema for the data store before
* any documents can be ingested.
* This flag cannot be specified if `data_store.starting_schema` is specified.
*/
// const skipDefaultSchemaCreation = true
// Imports the Discoveryengine library
const
{
DataStoreServiceClient
}
=
require
(
'@google-cloud/discoveryengine'
).
v1
;
// Instantiates a client
const
discoveryengineClient
=
new
DataStoreServiceClient
();
async
function
callCreateDataStore
()
{
// Construct request
const
request
=
{
parent
,
dataStore
,
dataStoreId
,
};
// Run request
const
[
operation
]
=
await
discoveryengineClient
.
createDataStore
(
request
);
const
[
response
]
=
await
operation
.
promise
();
console
.
log
(
response
);
}
callCreateDataStore
();
Import documents
/**
* This snippet has been automatically generated and should be regarded as a code template only.
* It will require modifications to work.
* It may require correct/in-range values for request initialization.
* TODO(developer): Uncomment these variables before running the sample.
*/
/**
* The Inline source for the input content for documents.
*/
// const inlineSource = {}
/**
* Cloud Storage location for the input content.
*/
// const gcsSource = {}
/**
* BigQuery input source.
*/
// const bigquerySource = {}
/**
* FhirStore input source.
*/
// const fhirStoreSource = {}
/**
* Spanner input source.
*/
// const spannerSource = {}
/**
* Cloud SQL input source.
*/
// const cloudSqlSource = {}
/**
* Firestore input source.
*/
// const firestoreSource = {}
/**
* AlloyDB input source.
*/
// const alloyDbSource = {}
/**
* Cloud Bigtable input source.
*/
// const bigtableSource = {}
/**
* Required. The parent branch resource name, such as
* `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
* Requires create/update permission.
*/
// const parent = 'abc123'
/**
* The desired location of errors incurred during the Import.
*/
// const errorConfig = {}
/**
* The mode of reconciliation between existing documents and the documents to
* be imported. Defaults to
* ReconciliationMode.INCREMENTAL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL.
*/
// const reconciliationMode = {}
/**
* Indicates which fields in the provided imported documents to update. If
* not set, the default is to update all fields.
*/
// const updateMask = {}
/**
* Whether to automatically generate IDs for the documents if absent.
* If set to `true`,
* Document.id google.cloud.discoveryengine.v1.Document.id s are
* automatically generated based on the hash of the payload, where IDs may not
* be consistent during multiple imports. In which case
* ReconciliationMode.FULL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.FULL
* is highly recommended to avoid duplicate contents. If unset or set to
* `false`, Document.id google.cloud.discoveryengine.v1.Document.id s have
* to be specified using
* id_field google.cloud.discoveryengine.v1.ImportDocumentsRequest.id_field,
* otherwise, documents without IDs fail to be imported.
* Supported data sources:
* * GcsSource google.cloud.discoveryengine.v1.GcsSource.
* GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
* BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
* * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
* * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
* * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
*/
// const autoGenerateIds = true
/**
* The field indicates the ID field or column to be used as unique IDs of
* the documents.
* For GcsSource google.cloud.discoveryengine.v1.GcsSource it is the key of
* the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`.
* For others, it may be the column name of the table where the unique ids are
* stored.
* The values of the JSON field or the table column are used as the
* Document.id google.cloud.discoveryengine.v1.Document.id s. The JSON field
* or the table column must be of string type, and the values must be set as
* valid strings conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
* with 1-63 characters. Otherwise, documents without valid IDs fail to be
* imported.
* Only set this field when
* auto_generate_ids google.cloud.discoveryengine.v1.ImportDocumentsRequest.auto_generate_ids
* is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.
* If it is unset, a default value `_id` is used when importing from the
* allowed data sources.
* Supported data sources:
* * GcsSource google.cloud.discoveryengine.v1.GcsSource.
* GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
* BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema
* must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
* * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
* * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
* * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
* * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
*/
// const idField = 'abc123'
/**
* Optional. Whether to force refresh the unstructured content of the
* documents.
* If set to `true`, the content part of the documents will be refreshed
* regardless of the update status of the referencing content.
*/
// const forceRefreshContent = true
// Imports the Discoveryengine library
const
{
DocumentServiceClient
}
=
require
(
'@google-cloud/discoveryengine'
).
v1
;
// Instantiates a client
const
discoveryengineClient
=
new
DocumentServiceClient
();
async
function
callImportDocuments
()
{
// Construct request
const
request
=
{
parent
,
};
// Run request
const
[
operation
]
=
await
discoveryengineClient
.
importDocuments
(
request
);
const
[
response
]
=
await
operation
.
promise
();
console
.
log
(
response
);
}
callImportDocuments
();
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# Examples:
# - Unstructured documents
# - `gs://bucket/directory/file.pdf`
# - `gs://bucket/directory/*.pdf`
# - Unstructured documents with JSONL Metadata
# - `gs://bucket/directory/file.json`
# - Unstructured documents with CSV Metadata
# - `gs://bucket/directory/file.csv`
# gcs_uri = "YOUR_GCS_PATH"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
gcs_source
=
discoveryengine
.
GcsSource
(
# Multiple URIs are supported
input_uris
=
[
gcs_uri
],
# Options:
# - `content` - Unstructured documents (PDF, HTML, DOC, TXT, PPTX)
# - `custom` - Unstructured documents with custom JSONL metadata
# - `document` - Structured documents in the discoveryengine.Document format.
# - `csv` - Unstructured documents with CSV metadata
data_schema
=
"content"
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Ruby
For more information, see the
AI Applications
Ruby
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
Create a data store
require
"google/cloud/discovery_engine/v1"
##
# Snippet for the create_data_store call in the DataStoreService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store.
#
def
create_data_store
# Create a client object. The client can be reused for multiple calls.
client
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
DataStoreService
::
Client
.
new
# Create a request. To set request fields, pass in keyword arguments.
request
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
CreateDataStoreRequest
.
new
# Call the create_data_store method.
result
=
client
.
create_data_store
request
# The returned object is of type Gapic::Operation. You can use it to
# check the status of an operation, cancel it, or wait for results.
# Here is how to wait for a response.
result
.
wait_until_done!
timeout
:
60
if
result
.
response?
p
result
.
response
else
puts
"No response received."
end
end
Import documents
require
"google/cloud/discovery_engine/v1"
##
# Snippet for the import_documents call in the DocumentService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#import_documents.
#
def
import_documents
# Create a client object. The client can be reused for multiple calls.
client
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
DocumentService
::
Client
.
new
# Create a request. To set request fields, pass in keyword arguments.
request
=
Google
::
Cloud
::
DiscoveryEngine
::
V1
::
ImportDocumentsRequest
.
new
# Call the import_documents method.
result
=
client
.
import_documents
request
# The returned object is of type Gapic::Operation. You can use it to
# check the status of an operation, cancel it, or wait for results.
# Here is how to wait for a response.
result
.
wait_until_done!
timeout
:
60
if
result
.
response?
p
result
.
response
else
puts
"No response received."
end
end
Connect to Cloud Storage with periodic syncing
Before importing your data, review
Prepare data for ingesting
.
The following procedure describes how to create a data connector that associates
a Cloud Storage location with a Vertex AI Search data
connector and how to specify a folder or file in that location for the data
store that you want to create. Data stores that are children of data connectors
are called
entity
data stores.
Data is synced periodically to the entity data store. You can specify
synchronization daily, every three days, or every five days.
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
Create data store
.
On the
Source
page, select
Cloud Storage
.
Select what kind of data you are importing.
Click
Periodic
.
Select the
Synchronization frequency
, how often you want the
Vertex AI Search connector to sync with the Cloud Storage
location. You can change the frequency later.
In the
Select a folder or file you want to import
section, select
Folder
or
File
.
Click
Browse
and choose the data you have
prepared for ingesting
, and then click
Select
.
Alternatively, enter the location directly in the
gs://
field.
Click
Continue
.
Choose a region for your data connector.
Enter a name for your data connector.
Optional: If you selected unstructured documents, you can select parsing and
chunking options for your documents. To compare parsers, see
Parse
documents
. For information about chunking see
Chunk documents for
RAG
.
The OCR parser and layout parser can incur additional costs. See
Document
AI feature pricing
.
To select a parser, expand
Document processing options
and specify the
parser options that you want to use.
Click
Create
.
You have now created a data connector, which will periodically sync data
with the Cloud Storage location. You have also created an entity
data store, which is named
gcs_store
.
To check the status of your ingestion, go to the
Data Stores
page and
click your data connector name to see details about it on its
Data
page
Data ingestion activity
tab. When the status column on the
Data
ingestion activity
tab changes from
In progress
to
succeeded
, the
first ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes to several hours.
After you set up your data source and import data the first time, data is
synced from that source at a frequency that you select during setup.
About an hour after the data connector is created, the first sync occurs.
The next sync then occurs around 24 hours, 72 hours,
or 120 hours later.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Connect to Google Drive
To search data from Google Drive, use the following steps to create
a connector using the Google Cloud console.
Before you begin:
You must be signed into the Google Cloud console with the
same account that you use for the Google Drive instance that you plan to
connect. Vertex AI Search uses your Google Workspace customer ID
to connect to Google Drive.
Set up access control for Google Drive. For information
about setting up access control, see
Use data source access control
.
Advanced Google Drive search is in Private preview. This feature is a
prerequisite for using search summarization and search with follow-ups with a
Google Drive data store. To use this feature, follow the steps in
Use
advanced drive indexing
instead.
If you have enabled
Access Transparency
, note that
Access Transparency only logs when Google personnel take action on the
Google Cloud project. You'll also need to review the
Access Transparency logs created by Google Workspace. For more information,
see
Access Transparency log events
in the Google Workspace
Admin Help documentation.
Console
To use the console to make Google Drive data searchable, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Google Drive
.
Choose a region for your data store.
Enter a name for your data store.
. Click
Create
.
Use advanced drive indexing (Private preview)
Advanced drive indexing is in Private preview.
Follow this procedure if you plan to use Google Drive with search
summarization and search with follow-ups.
Before you begin:
You must be a Google Workspace super administrator to turn on advanced drive
indexing. This is because with advanced drive indexing,
Vertex AI Search indexes Google Drive data.
You must be added to an allowlist to use this feature. Contact your Google
account team and ask to be added to the allowlist for advanced drive indexing.
Console
To use the console to create a Google Drive data store with advanced
Google Drive indexing, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Google Drive
.
Select
Advanced drive indexing
.
Enter your Google Workspace administrator email address.
In the
Set up domain wide delegation
section, review the instructions
and take note of the service account client ID provided in step 4 of that
section.
Set up domain wide delegation:
Go to the
Domain-wide delegation
page of Google Workspace
Admin Console and sign with your super administrator account.
Click
Add new
.
Enter the service account client ID that you took note of. (This ID is
provided in the instructions in the AI Applications
console in the
Set up domain wide delegation
section.)
Enter the following OAuth scopes.
https://www.googleapis.com/auth/drive.readonly,
https://www.googleapis.com/auth/admin.directory.user.readonly,
https://www.googleapis.com/auth/admin.directory.group.readonly,
https://www.googleapis.com/auth/admin.directory.domain.readonly,
https://www.googleapis.com/auth/admin.reports.audit.readonly
Click
Authorize
.
In the AI Applications console, click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
. Depending on the size of your data, ingestion can take
several minutes to several hours. Wait at least an hour before using your
data store for searching.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Connect to Gmail
To search data from Gmail, use the following steps to create
a data store and ingest data using the Google Cloud console.
Before you begin:
You must be signed into the Google Cloud console with the same account that you
use for the Google Workspace instance that you plan to connect.
Vertex AI Search uses your Google Workspace customer ID to connect
to Gmail.
Set up access control for Gmail. For information
about setting up access control, see
Use data source access control
.
Console
To use the console to make Gmail data searchable, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Google Gmail
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Connect to Google Sites
To search data from Google Sites, use the following steps to create
a connector using the Google Cloud console.
Before you begin:
You must be signed into the Google Cloud console with the same account that you
use for the Google Workspace instance that you plan to connect.
Vertex AI Search uses your Google Workspace customer ID to connect
to Google Sites.
Set up access control for Google Sites. For information
about setting up access control, see
Use data source access control
.
Console
To use the console to make Google Sites data searchable, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Google Sites
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Connect to Google Calendar
To search data from Google Calendar, use the following steps to create
a connector using the Google Cloud console.
Before you begin:
You must be signed into the Google Cloud console with the same account that you
use for the Google Workspace instance that you plan to connect.
Vertex AI Search uses your Google Workspace customer ID to connect
to Google Calendar.
Set up access control for Google Calendar. For information
about setting up access control, see
Use data source access control
.
Console
To use the console to make Google Calendar data searchable, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Google Calendar
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Connect to Google Groups
To search data from Google Groups, use the following steps to create
a connector using the Google Cloud console.
Before you begin:
You must be signed into the Google Cloud console with the same account that you
use for the Google Workspace instance that you plan to connect.
Vertex AI Search uses your Google Workspace customer ID to connect
to Google Groups.
Set up access control for Google Groups. For information
about setting up access control, see
Use data source access control
.
Console
To use the console to make Google Groups data searchable, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Google Groups
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
. Depending on the size of your data, ingestion can take
several minutes to several hours. Wait at least an hour before using your
data store for searching.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Sync people data from Google Workspace
You can set up people search for your work teams by syncing people data from
Google Workspace. This data continuously syncs to Vertex AI Search
after you create your data store.
People from your directory appear in search results as cards displaying their
available profile information, such as name, email address, organization, and
profile picture. Click a card to see that person's details page.
Prerequisites
Determine the identity provider for users to sign into the app.
If you use a third-party identity provider, an administrator must federate your
identity provider with Google Workspace. Federation requires planning and
setup. For more information, see
Use data source access control
.
A Google Workspace administrator must enable people search on
Google Workspace data:
Sign in to the
Google Admin console
with an
administrator account.
Go to
Directory
>
Directory settings
.
Turn on
Contact sharing
.
Sign in to the Google Cloud console with the same account you plan to connect
Google Workspace from.
Connect to your identity provider using the steps in
Connect your identity
provider
, and specify
Google
Identity
as your provider.
For information about Google Workspace Directory, see
Overview: Set up and manage the Directory
in the Google Workspace documentation.
Sync people data with advanced Google Identity connector
Advanced Google Identity connector syncs people data from
Google Workspace. The existing connector does not copy data into the
Vertex AI Search index and delegates the search request to
PeopleAPI
.
The Google Identity Cloud connector copies data into the Vertex AI Search
index, enabling features like Knowledge Graph and Natural Language Processing.
The connector is
cloud-native
as it copies data, similar to
the
advanced drive connector
. Make sure to complete the
tasks in the prerequisites section before you start the following procedures.
Set up the service account
Create a service account
in a
Google Cloud project within the organization.
Skip the
Grant this service account access to project (optional)
step and the
Grant
users access to this service account (optional)
step and then click
Save
.
After the service account is created, click the service account and go to the
Permissions
tab.
Grant the Discovery Engine service account
(
service-
PROJECT_NUMBER
@gcp-sa-discoveryengine.iam.gserviceaccount.com
)
access as a
Service account token creator
(
roles/iam.serviceAccountTokenCreator
)
and click
Save
.
In the
Details
tab of the service account, click
Advanced settings
.
Copy the client ID for domain-wide delegation.
Set up domain-wide delegation
Sign in to the
Google administrator workspace
.
Navigate to
Security
>
Access and data control
>
API controls
.
Click
Manage domain wide delegation
.
Click
Add new
.
In the
Add a new client ID
dialog, do the following:
Client ID
: Enter the client ID.
OAuth scopes
: Enter
https://www.googleapis.com/auth/directory.readonly
.
Click
Authorize
.
Create a People Search data store
To use the console to ingest people data, follow these steps:
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data stores
page.
Click
add
Create data store
.
On the
Source
page, select
People search
.
Choose a region for your data store.
Enter a name for your data store.
Optional
: For advanced People Search, under
Specify the people source for your data store
, click
Advanced people indexing
.
If you are using the advanced indexing, enter authentication details:
Sync account email
: Enter the email of the account used to obtain data.
You can also create a dedicated user account through the administration workspace.
Service account email
: Enter the previously created service account.
Click
Create
. Syncing may take several minutes to hours, depending on data size.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from Cloud SQL
To ingest data from Cloud SQL, use the following steps to set up
Cloud SQL access, create a data store, and ingest data.
Set up staging bucket access for Cloud SQL instances
When ingesting data from Cloud SQL, data is first staged to a
Cloud Storage bucket. Follow these steps to give a Cloud SQL
instance access to
Cloud Storage buckets.
In the Google Cloud console, go to the
SQL
page.
SQL
Click the Cloud SQL instance that you plan to import from.
Copy the identifier for the instance's service account, which looks like an
email address—for example,
p9876-abcd33f@gcp-sa-cloud-sql.iam.gserviceaccount.com
.
Go to the
IAM & Admin
page.
IAM & Admin
Click
Grant access
.
For
New principals
, enter the instance's service account identifier and
select the
Cloud Storage > Storage Admin
role.
Click
Save
.
Next:
If your Cloud SQL data is in the same project as Vertex AI Search:
Go to
Import data from Cloud SQL
.
If your Cloud SQL data is in a different project than your
Vertex AI Search project: Go to
Set up Cloud SQL
access from a different project
.
Set up Cloud SQL access from a different project
To give Vertex AI Search access to Cloud SQL data that's in a
different project, follow these steps:
Replace the following
PROJECT_NUMBER
variable with your
Vertex AI Search project number, and then copy the contents of the
code block. This is your Vertex AI Search service account
identifier:
service-
PROJECT_NUMBER
@gcp-sa-discoveryengine.iam.gserviceaccount.com`
Go to the
IAM & Admin
page.
IAM & Admin
Switch to your Cloud SQL project on the
IAM & Admin
page
and click
Grant Access
.
For
New principals
, enter the identifier for the service account and
select the
Cloud SQL > Cloud SQL Viewer
role.
Click
Save
.
Next, go to
Import data from Cloud SQL
.
Import data from Cloud SQL
Console
To use the console to ingest data from Cloud SQL, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Cloud SQL
.
Specify the project ID, instance ID, database ID, and table ID of the data
that you plan to import.
Click
Browse
and choose an intermediate Cloud Storage location to
export data to, and then click
Select
. Alternatively, enter the location
directly in the
gs://
field.
Select whether to turn on serverless export. Serverless export incurs
additional cost. For information about serverless export, see
Minimize the
performance impact of exports
in
the Cloud SQL documentation.
Click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
To check the status of your ingestion, go to the
Data Stores
page
and click your data store name to see details about it on its
Data
page.
When the status column on the
Activity
tab changes from
In progress
to
Import completed
, the ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes or several hours.
REST
To use the command line to create a data store and ingest data from
Cloud SQL, follow these steps:
Create a data store.
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'
Replace the following:
PROJECT_ID
: the ID of your project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
DISPLAY_NAME
: the display name of the data store. This might
be displayed in the Google Cloud console.
Import data from Cloud SQL.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"cloudSqlSource": {
"projectId": "
SQL_PROJECT_ID
",
"instanceId": "
INSTANCE_ID
",
"databaseId": "
DATABASE_ID
",
"tableId": "
TABLE_ID
",
"gcsStagingDir": "
STAGING_DIRECTORY
"
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
}'
Replace the following:
PROJECT_ID
: the ID of your Vertex AI Search
project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
SQL_PROJECT_ID
: the ID of your Cloud SQL
project.
INSTANCE_ID
: the ID of your Cloud SQL instance.
DATABASE_ID
: the ID of your Cloud SQL database.
TABLE_ID
: the ID of your Cloud SQL table.
STAGING_DIRECTORY
: optional. A Cloud Storage
directory—for example,
gs://<your-gcs-bucket>/directory/import_errors
.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from Cloud SQL to your
data store. This does an upsert operation, which adds new documents and
replaces existing documents with updated documents with the same ID.
Specifying
FULL
causes a full rebase of the documents in your data
store. In other words, new and updated documents are added to your data
store, and documents that are not in Cloud SQL are removed
from your data store. The
FULL
mode is helpful if you want to
automatically delete documents that you no longer need.
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# sql_project_id = "YOUR_SQL_PROJECT_ID"
# sql_instance_id = "YOUR_SQL_INSTANCE_ID"
# sql_database_id = "YOUR_SQL_DATABASE_ID"
# sql_table_id = "YOUR_SQL_TABLE_ID"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
cloud_sql_source
=
discoveryengine
.
CloudSqlSource
(
project_id
=
sql_project_id
,
instance_id
=
sql_instance_id
,
database_id
=
sql_database_id
,
table_id
=
sql_table_id
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from Spanner
To ingest data from Spanner, use the following steps to create
a data store and ingest data using either the Google Cloud console or the API.
Set up Spanner access from a different project
If your Spanner data is in the same project as
Vertex AI Search, skip to
Import data from
Spanner
.
To give Vertex AI Search access to Spanner data that is
in a different project, follow these steps:
Replace the following
PROJECT_NUMBER
variable with your
Vertex AI Search project number, and then copy the contents of this
code block. This is your Vertex AI Search service account
identifier:
service-
PROJECT_NUMBER
@gcp-sa-discoveryengine.iam.gserviceaccount.com
Go to the
IAM & Admin
page.
IAM & Admin
Switch to your Spanner project on the
IAM & Admin
page
and click
Grant Access
.
For
New principals
, enter the identifier for the service account and
select one of the following:
If you won't use data boost during import, select the
Cloud Spanner >
Cloud Spanner Database Reader
role.
If you plan to use data boost during import, select the
Cloud Spanner >
Cloud Spanner Database Admin
role, or a custom role with the permissions of
Cloud Spanner Database Reader
and
spanner.databases.useDataBoost
.
For information about Data Boost, see
Data Boost overview
in the
Spanner documentation.
Click
Save
.
Next, go to
Import data from Spanner
.
Import data from Spanner
Console
To use the console to ingest data from Spanner, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Cloud Spanner
.
Specify the project ID, instance ID, database ID, and table ID of the data
that you plan to import.
Select whether to turn on Data Boost. For information about Data Boost, see
Data Boost overview
in the
Spanner documentation.
Click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
To check the status of your ingestion, go to the
Data Stores
page
and click your data store name to see details about it on its
Data
page.
When the status column on the
Activity
tab changes from
In progress
to
Import completed
, the ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes or several hours.
REST
To use the command line to create a data store and ingest data from
Spanner, follow these steps:
Create a data store.
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
"contentConfig": "CONTENT_REQUIRED",
}'
Replace the following:
PROJECT_ID
: the ID of your Vertex AI Search project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
DISPLAY_NAME
: the display name of the data store. This might
be displayed in the Google Cloud console.
Import data from Spanner.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"cloudSpannerSource": {
"projectId": "
SPANNER_PROJECT_ID
",
"instanceId": "
INSTANCE_ID
",
"databaseId": "
DATABASE_ID
",
"tableId": "
TABLE_ID
",
"enableDataBoost": "
DATA_BOOST_BOOLEAN
"
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
}'
Replace the following:
PROJECT_ID
: the ID of your Vertex AI Search project.
DATA_STORE_ID
: the ID of the data store.
SPANNER_PROJECT_ID
: the ID of your Spanner
project.
INSTANCE_ID
: the ID of your Spanner instance.
DATABASE_ID
: the ID of your Spanner database.
TABLE_ID
: the ID of your Spanner table.
DATA_BOOST_BOOLEAN
: optional. Whether to turn on Data Boost.
For information about Data Boost, see
Data Boost
overview
in the
Spanner documentation.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from
Spanner to your data store. This does an upsert
operation, which adds new documents and replaces existing documents
with updated documents with the same ID. Specifying
FULL
causes a
full rebase of the documents in your data store. In other words, new
and updated documents are added to your data store, and documents that
are not in Spanner are removed from your data store. The
FULL
mode is helpful if you want to automatically delete documents
that you no longer need.
AUTO_GENERATE_IDS
: optional. Specifies whether to
automatically generate document IDs. If set to
true
, document IDs
are generated based on a hash of the payload. Note that generated
document IDs might not remain consistent over multiple imports. If
you auto-generate IDs over multiple imports, Google highly
recommends setting
reconciliationMode
to
FULL
to maintain
consistent document IDs.
ID_FIELD
: optional. Specifies which fields are the
document IDs.
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# spanner_project_id = "YOUR_SPANNER_PROJECT_ID"
# spanner_instance_id = "YOUR_SPANNER_INSTANCE_ID"
# spanner_database_id = "YOUR_SPANNER_DATABASE_ID"
# spanner_table_id = "YOUR_SPANNER_TABLE_ID"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
spanner_source
=
discoveryengine
.
SpannerSource
(
project_id
=
spanner_project_id
,
instance_id
=
spanner_instance_id
,
database_id
=
spanner_database_id
,
table_id
=
spanner_table_id
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from Firestore
To ingest data from Firestore, use the following steps to create
a data store and ingest data using either the Google Cloud console or the API.
If your Firestore data is in the same project as
Vertex AI Search, go to
Import data from
Firestore
.
If your Firestore data is in a different project than your
Vertex AI Search project, go to
Set up Firestore
access
.
Set up Firestore access from a different project
To give Vertex AI Search access to Firestore data that's
in a different project, follow these steps:
Replace the following
PROJECT_NUMBER
variable with your
Vertex AI Search project number, and then copy the contents of this
code block. This is your Vertex AI Search service account
identifier:
service-
PROJECT_NUMBER
@gcp-sa-discoveryengine.iam.gserviceaccount.com
Go to the
IAM & Admin
page.
IAM & Admin
Switch to your Firestore project on the
IAM & Admin
page
and click
Grant Access
.
For
New principals
, enter the instance's service account identifier and
select the
Datastore > Cloud Datastore Import Export Admin
role.
Click
Save
.
Switch back to your Vertex AI Search project.
Next, go to
Import data from Firestore
.
Import data from Firestore
Console
To use the console to ingest data from Firestore, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Go to the
Data Stores
page.
Click
New data store
.
On the
Source
page, select
Firestore
.
Specify the project ID, database ID, and collection ID of the data that you
plan to import.
Click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
To check the status of your ingestion, go to the
Data Stores
page
and click your data store name to see details about it on its
Data
page.
When the status column on the
Activity
tab changes from
In progress
to
Import completed
, the ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes or several hours.
REST
To use the command line to create a data store and ingest data from
Firestore, follow these steps:
Create a data store.
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'
Replace the following:
PROJECT_ID
: the ID of your project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
DISPLAY_NAME
: the display name of the data store. This might
be displayed in the Google Cloud console.
Import data from Firestore.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"firestoreSource": {
"projectId": "
FIRESTORE_PROJECT_ID
",
"databaseId": "
DATABASE_ID
",
"collectionId": "
COLLECTION_ID
",
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
}'
Replace the following:
PROJECT_ID
: the ID of your Vertex AI Search project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
FIRESTORE_PROJECT_ID
: the ID of your
Firestore project.
DATABASE_ID
: the ID of your Firestore
database.
COLLECTION_ID
: the ID of your Firestore
collection.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from Firestore to your
data store. This does an upsert operation, which adds new documents and
replaces existing documents with updated documents with the same ID.
Specifying
FULL
causes a full rebase of the documents in your data
store. In other words, new and updated documents are added to your data
store, and documents that are not in Firestore are removed
from your data store. The
FULL
mode is helpful if you want to
automatically delete documents that you no longer need.
AUTO_GENERATE_IDS
: optional. Specifies whether to
automatically generate document IDs. If set to
true
, document IDs
are generated based on a hash of the payload. Note that generated
document IDs might not remain consistent over multiple imports. If
you auto-generate IDs over multiple imports, Google highly
recommends setting
reconciliationMode
to
FULL
to maintain
consistent document IDs.
ID_FIELD
: optional. Specifies which fields are the
document IDs.
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# firestore_project_id = "YOUR_FIRESTORE_PROJECT_ID"
# firestore_database_id = "YOUR_FIRESTORE_DATABASE_ID"
# firestore_collection_id = "YOUR_FIRESTORE_COLLECTION_ID"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
firestore_source
=
discoveryengine
.
FirestoreSource
(
project_id
=
firestore_project_id
,
database_id
=
firestore_database_id
,
collection_id
=
firestore_collection_id
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from Bigtable
To ingest data from Bigtable, use the following steps to create
a data store and ingest data using the API.
Set up Bigtable access
To give Vertex AI Search access to Bigtable data that's
in a different project, follow these steps:
Replace the following
PROJECT_NUMBER
variable with your
Vertex AI Search project number, then copy the contents of this
code block. This is your Vertex AI Search service account
identifier:
service-
PROJECT_NUMBER
@gcp-sa-discoveryengine.iam.gserviceaccount.com`
Go to the
IAM & Admin
page.
IAM & Admin
Switch to your Bigtable project on the
IAM & Admin
page
and click
Grant Access
.
For
New principals
, enter the instance's service account identifier and
select the
Bigtable > Bigtable Reader
role.
Click
Save
.
Switch back to your Vertex AI Search project.
Next, go to
Import data from Bigtable
.
Import data from Bigtable
REST
To use the command line to create a data store and ingest data from
Bigtable, follow these steps:
Create a data store.
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'
Replace the following:
PROJECT_ID
: the ID of your project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
DISPLAY_NAME
: the display name of the data store. This might
be displayed in the Google Cloud console.
Import data from Bigtable.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"bigtableSource ": {
"projectId": "
BIGTABLE_PROJECT_ID
",
"instanceId": "
INSTANCE_ID
",
"tableId": "
TABLE_ID
",
"bigtableOptions": {
"keyFieldName": "
KEY_FIELD_NAME
",
"families": {
"key": "
KEY
",
"value": {
"fieldName": "
FIELD_NAME
",
"encoding": "
ENCODING
",
"type": "
TYPE
",
"columns": [
{
"qualifier": "
QUALIFIER
",
"fieldName": "
FIELD_NAME
",
"encoding": "
COLUMN_ENCODING
",
"type": "
COLUMN_VALUES_TYPE
"
}
]
}
}
...
}
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
}'
Replace the following:
PROJECT_ID
: the ID of your Vertex AI Search
project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
BIGTABLE_PROJECT_ID
: the ID of your
Bigtable project.
INSTANCE_ID
: the ID of your Bigtable
instance.
TABLE_ID
: the ID of your Bigtable
table.
KEY_FIELD_NAME
: optional but recommended. The field name to
use for the row key value after ingesting to Vertex AI Search.
KEY
: required. A string value for the column family key.
ENCODING
: optional. The encoding mode of the values when the
type is not STRING.This can be overridden for a specific column by
listing that column in
columns
and specifying an encoding for it.
COLUMN_TYPE
: optional. The type of values in this column
family.
QUALIFIER
: required. Qualifier of the column.
FIELD_NAME
: optional but recommended. The field name to use
for this column after ingesting to Vertex AI Search.
COLUMN_ENCODING
: optional. The encoding mode of the values
for a specific column when the type is not STRING.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from Bigtable to
your data store. This does an upsert operation, which adds new
documents and replaces existing documents with updated documents with
the same ID. Specifying
FULL
causes a full rebase of the documents in
your data store. In other words, new and updated documents are added to
your data store, and documents that are not in Bigtable
are removed from your data store. The
FULL
mode is helpful if you
want to automatically delete documents that you no longer need.
AUTO_GENERATE_IDS
: optional. Specifies whether to
automatically generate document IDs. If set to
true
, document IDs
are generated based on a hash of the payload. Note that generated
document IDs might not remain consistent over multiple imports. If
you auto-generate IDs over multiple imports, Google highly
recommends setting
reconciliationMode
to
FULL
to maintain
consistent document IDs.
Specify
autoGenerateIds
only when
bigquerySource.dataSchema
is
set to
custom
. Otherwise an
INVALID_ARGUMENT
error is
returned. If you don't specify
autoGenerateIds
or set it to
false
, you must specify
idField
. Otherwise the documents fail to
import.
ID_FIELD
: optional. Specifies which fields are the
document IDs.
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# bigtable_project_id = "YOUR_BIGTABLE_PROJECT_ID"
# bigtable_instance_id = "YOUR_BIGTABLE_INSTANCE_ID"
# bigtable_table_id = "YOUR_BIGTABLE_TABLE_ID"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
bigtable_options
=
discoveryengine
.
BigtableOptions
(
families
=
{
"family_name_1"
:
discoveryengine
.
BigtableOptions
.
BigtableColumnFamily
(
type_
=
discoveryengine
.
BigtableOptions
.
Type
.
STRING
,
encoding
=
discoveryengine
.
BigtableOptions
.
Encoding
.
TEXT
,
columns
=
[
discoveryengine
.
BigtableOptions
.
BigtableColumn
(
qualifier
=
"qualifier_1"
.
encode
(
"utf-8"
),
field_name
=
"field_name_1"
,
),
],
),
"family_name_2"
:
discoveryengine
.
BigtableOptions
.
BigtableColumnFamily
(
type_
=
discoveryengine
.
BigtableOptions
.
Type
.
INTEGER
,
encoding
=
discoveryengine
.
BigtableOptions
.
Encoding
.
BINARY
,
),
}
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
bigtable_source
=
discoveryengine
.
BigtableSource
(
project_id
=
bigtable_project_id
,
instance_id
=
bigtable_instance_id
,
table_id
=
bigtable_table_id
,
bigtable_options
=
bigtable_options
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Import from AlloyDB for PostgreSQL
To ingest data from AlloyDB for PostgreSQL, use the following steps to create
a data store and ingest data using either the Google Cloud console or the API.
If your AlloyDB for PostgreSQL data is in the same project as
Vertex AI Search project, go to
Import data from
AlloyDB for PostgreSQL
.
If your AlloyDB for PostgreSQL data is in a different project than your
Vertex AI Search project, go to
Set up AlloyDB for PostgreSQL
access
.
Set up AlloyDB for PostgreSQL access from a different project
To give Vertex AI Search access to AlloyDB for PostgreSQL data that's
in a different project, follow these steps:
Replace the following
PROJECT_NUMBER
variable with your
Vertex AI Search project number, and then copy the contents of this
code block. This is your Vertex AI Search service account
identifier:
service-
PROJECT_NUMBER
@gcp-sa-discoveryengine.iam.gserviceaccount.com
Switch to the Google Cloud project where your AlloyDB for PostgreSQL data
resides.
Go to the
IAM
page.
IAM
Click
Grant Access
.
For
New principals
, enter the Vertex AI Search service account
identifier and
select the
Cloud AlloyDB > Cloud AlloyDB Admin
role.
Click
Save
.
Switch back to your Vertex AI Search project.
Next, go to
Import data from AlloyDB for PostgreSQL
.
Import data from AlloyDB for PostgreSQL
Console
To use the console to ingest data from AlloyDB for PostgreSQL, follow these
steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data Stores
.
Click
Create data store
.
On the
Source
page, select
AlloyDB
.
Specify the project ID, location ID, cluster ID, database ID, and table ID
of the data that you plan to import.
Click
Continue
.
Choose a region for your data store.
Enter a name for your data store.
Click
Create
.
To check the status of your ingestion, go to the
Data Stores
page
and click your data store name to see details about it on its
Data
page.
When the status column on the
Activity
tab changes from
In progress
to
Import completed
, the ingestion is complete.
Depending on the size of your data, ingestion can take several
minutes or several hours.
REST
To use the command line to create a data store and ingest data from
AlloyDB for PostgreSQL, follow these steps:
Create a data store.
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'
Replace the following:
PROJECT_ID
: the ID of your project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
DISPLAY_NAME
: the display name of the data store. This might
be displayed in the Google Cloud console.
Import data from AlloyDB for PostgreSQL.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents:import"
\
-d
'{
"alloydbSource": {
"projectId": "
ALLOYDB_PROJECT_ID
",
"locationId": "
LOCATION_ID
",
"clusterId": "
CLUSTER_ID
",
"databaseId": "
DATABASE_ID
",
"tableId": "
TABLE_ID
",
},
"reconciliationMode": "
RECONCILIATION_MODE
",
"autoGenerateIds": "
AUTO_GENERATE_IDS
",
"idField": "
ID_FIELD
",
}'
Replace the following:
PROJECT_ID
: the ID of your Vertex AI Search project.
DATA_STORE_ID
: the ID of the data store. The ID can
contain only lowercase letters, digits, underscores, and hyphens.
ALLOYDB_PROJECT_ID
: the ID of your
AlloyDB for PostgreSQL project.
LOCATION_ID
: the ID of your AlloyDB for PostgreSQL
location.
CLUSTER_ID
: the ID of your AlloyDB for PostgreSQL
cluster.
DATABASE_ID
: the ID of your AlloyDB for PostgreSQL
database.
TABLE_ID
: the ID of your AlloyDB for PostgreSQL
table.
RECONCILIATION_MODE
: optional. Values are
FULL
and
INCREMENTAL
. Default is
INCREMENTAL
. Specifying
INCREMENTAL
causes an incremental refresh of data from AlloyDB for PostgreSQL to your
data store. This does an upsert operation, which adds new documents and
replaces existing documents with updated documents with the same ID.
Specifying
FULL
causes a full rebase of the documents in your data
store. In other words, new and updated documents are added to your data
store, and documents that are not in AlloyDB for PostgreSQL are removed
from your data store. The
FULL
mode is helpful if you want to
automatically delete documents that you no longer need.
AUTO_GENERATE_IDS
: optional. Specifies whether to
automatically generate document IDs. If set to
true
, document IDs
are generated based on a hash of the payload. Note that generated
document IDs might not remain consistent over multiple imports. If
you auto-generate IDs over multiple imports, Google highly
recommends setting
reconciliationMode
to
FULL
to maintain
consistent document IDs.
ID_FIELD
: optional. Specifies which fields are the
document IDs.
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
Create a data store
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
def
create_data_store_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
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
DataStoreServiceClient
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
data_store
=
discoveryengine
.
DataStore
(
display_name
=
"My Data Store"
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
solution_types
=
[
discoveryengine
.
SolutionType
.
SOLUTION_TYPE_SEARCH
],
# TODO(developer): Update content_config based on data store type.
# Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
content_config
=
discoveryengine
.
DataStore
.
ContentConfig
.
CONTENT_REQUIRED
,
)
request
=
discoveryengine
.
CreateDataStoreRequest
(
parent
=
parent
,
data_store_id
=
data_store_id
,
data_store
=
data_store
,
# Optional: For Advanced Site Search Only
# create_advanced_site_search=True,
)
# Make the request
operation
=
client
.
create_data_store
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
CreateDataStoreMetadata
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
Import documents
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
# data_store_id = "YOUR_DATA_STORE_ID"
# alloy_db_project_id = "YOUR_ALLOY_DB_PROJECT_ID"
# alloy_db_location_id = "YOUR_ALLOY_DB_LOCATION_ID"
# alloy_db_cluster_id = "YOUR_ALLOY_DB_CLUSTER_ID"
# alloy_db_database_id = "YOUR_ALLOY_DB_DATABASE_ID"
# alloy_db_table_id = "YOUR_ALLOY_DB_TABLE_ID"
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
DocumentServiceClient
(
client_options
=
client_options
)
# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent
=
client
.
branch_path
(
project
=
project_id
,
location
=
location
,
data_store
=
data_store_id
,
branch
=
"default_branch"
,
)
request
=
discoveryengine
.
ImportDocumentsRequest
(
parent
=
parent
,
alloy_db_source
=
discoveryengine
.
AlloyDbSource
(
project_id
=
alloy_db_project_id
,
location_id
=
alloy_db_location_id
,
cluster_id
=
alloy_db_cluster_id
,
database_id
=
alloy_db_database_id
,
table_id
=
alloy_db_table_id
,
),
# Options: `FULL`, `INCREMENTAL`
reconciliation_mode
=
discoveryengine
.
ImportDocumentsRequest
.
ReconciliationMode
.
INCREMENTAL
,
)
# Make the request
operation
=
client
.
import_documents
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
ImportDocumentsMetadata
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
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Upload structured JSON data with the API
To directly upload a JSON document or object using the API, follow these steps.
Before importing your data,
Prepare data for ingesting
.
REST
To use the command line to create a data store and import structured JSON data,
follow these steps.
Create a data store.
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores?dataStoreId=
DATA_STORE_ID
"
\
-d
'{
"displayName": "
DATA_STORE_DISPLAY_NAME
",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"]
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store that you want to create. This ID can contain only lowercase
letters, digits, underscores, and hyphens.
DATA_STORE_DISPLAY_NAME
: the display name of the Vertex AI
Search data store that you want to create.
Import structured data.
There are a few approaches that you can use to upload data, including:
Upload a JSON document.
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents?documentId=
DOCUMENT_ID
"
\
-d
'{
"jsonData": "
JSON_DOCUMENT_STRING
"
}'
Replace the following:
DOCUMENT_ID
: a unique ID for the document.
This ID can be up to 63 characters long and contain only lowercase
letters, digits, underscores, and hyphens.
JSON_DOCUMENT_STRING
: the JSON document as a
single string. This must conform to the JSON schema that you
provided in the previous step—for example:
{ \"title\": \"test title\", \"categories\": [\"cat_1\", \"cat_2\"], \"uri\": \"test uri\"}
Upload a JSON object.
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents?documentId=
DOCUMENT_ID
"
\
-d
'{
"structData":
JSON_DOCUMENT_OBJECT
}'
Replace
JSON_DOCUMENT_OBJECT
with the JSON document as a
JSON object. This must conform to the JSON schema that you provided
in the previous step—for example:
```json
{
"title": "test title",
"categories": [
"cat_1",
"cat_2"
],
"uri": "test uri"
}
```
Update with a JSON document.
curl
-X
PATCH
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents/
DOCUMENT_ID
"
\
-d
'{
"jsonData": "
JSON_DOCUMENT_STRING
"
}'
Update with a JSON object.
curl
-X
PATCH
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents/
DOCUMENT_ID
"
\
-d
'{
"structData":
JSON_DOCUMENT_OBJECT
}'
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
.
Troubleshoot data ingestion
If you are having problems with data ingestion, review these tips:
If you're using
customer-managed encryption keys
and data import fails
(with error message
The caller does not have permission
), then make sure
that the CryptoKey Encrypter/Decrypter IAM role
(
roles/cloudkms.cryptoKeyEncrypterDecrypter
) on the key has been granted to
the Cloud Storage service agent. For more information, see
Before you begin
in "Customer-managed encryption
keys".
If you are using advanced website indexing and the
Document usage
for the
data store is much lower than you expect, then review the URL patterns that you
specified for indexing and make sure that the URL patterns specified cover the
pages that you want to index and expand them if needed. For example, if
you used
*.en.example.com/*
, you might need to add
*.example.com/*
to the
sites you want indexed.
Create a data store using Terraform
You can use Terraform to create an empty data store. After the empty data store
is created, you can ingest data into the data store using the Google Cloud console
or API commands.
To learn how to apply or remove a Terraform configuration, see
Basic Terraform commands
.
To create an empty data store using Terraform, see
google_discovery_engine_data_store
.
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

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 2 (text)

```text
#     from google.api_core.client_options import ClientOptions
#
#     from google.cloud import discoveryengine_v1 as discoveryengine
#
#     # TODO(developer): Uncomment these variables before running the sample.
#     # project_id = "YOUR_PROJECT_ID"
#     # location = "YOUR_LOCATION" # Values: "global"
#     # data_store_id = "YOUR_DATA_STORE_ID"
#     # NOTE: Do not include http or https protocol in the URI pattern
#     # uri_pattern = "cloud.google.com/generative-ai-app-builder/docs/*"
#
#     #  For more information, refer to:
#     # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
#     client_options = (
#         ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
#         if location != "global"
#         else None
#     )
#
#     # Create a client
#     client = discoveryengine.SiteSearchEngineServiceClient(
#         client_options=client_options
#     )
#
#     # The full resource name of the data store
#     # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}
#     site_search_engine = client.site_search_engine_path(
#         project=project_id, location=location, data_store=data_store_id
#     )
#
#     # Target Site to index
#     target_site = discoveryengine.TargetSite(
#         provided_uri_pattern=uri_pattern,
#         # Options: INCLUDE, EXCLUDE
#         type_=discoveryengine.TargetSite.Type.INCLUDE,
#         exact_match=False,
#     )
#
#     # Make the request
#     operation = client.create_target_site(
#         parent=site_search_engine,
#         target_site=target_site,
#     )
#
#     print(f"Waiting for operation to complete: {operation.operation.name}")
#     response = operation.result()
#
#     # After the operation is complete,
#     # get information from operation metadata
#     metadata = discoveryengine.CreateTargetSiteMetadata(operation.metadata)
#
#     # Handle the response
#     print(response)
#     print(metadata)
```

### Code Example 3 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DATA_STORE_DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"]
}'

```

### Code Example 4 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
-d '{
  "bigquerySource": {
    "projectId": "PROJECT_ID",
    "datasetId":"DATASET_ID",
    "tableId": "TABLE_ID",
    "dataSchema": "DATA_SCHEMA",
    "aclEnabled": "BOOLEAN"
  },
  "reconciliationMode": "RECONCILIATION_MODE",
  "autoGenerateIds": "AUTO_GENERATE_IDS",
  "idField": "ID_FIELD",
  "errorConfig": {
    "gcsPrefix": "ERROR_DIRECTORY"
  }
}'

```

### Code Example 5 (text)

```text
using Google.Cloud.DiscoveryEngine.V1;
using Google.LongRunning;

public sealed partial class GeneratedDataStoreServiceClientSnippets
{
    /// <summary>Snippet for CreateDataStore</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void CreateDataStoreRequestObject()
    {
        // Create client
        DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.Create();
        // Initialize request argument(s)
        CreateDataStoreRequest request = new CreateDataStoreRequest
        {
            ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
            DataStore = new DataStore(),
            DataStoreId = "",
            CreateAdvancedSiteSearch = false,
            SkipDefaultSchemaCreation = false,
        };
        // Make the request
        Operation<DataStore, CreateDataStoreMetadata> response = dataStoreServiceClient.CreateDataStore(request);

        // Poll until the returned long-running operation is complete
        Operation<DataStore, CreateDataStoreMetadata> completedResponse = response.PollUntilCompleted();
        // Retrieve the operation result
        DataStore result = completedResponse.Result;

        // Or get the name of the operation
        string operationName = response.Name;
        // This name can be stored, then the long-running operation retrieved later by name
        Operation<DataStore, CreateDataStoreMetadata> retrievedResponse = dataStoreServiceClient.PollOnceCreateDataStore(operationName);
        // Check if the retrieved long-running operation has completed
        if (retrievedResponse.IsCompleted)
        {
            // If it has completed, then access the result
            DataStore retrievedResult = retrievedResponse.Result;
        }
    }
}
```

### Code Example 6 (text)

```text
using Google.Cloud.DiscoveryEngine.V1;
using Google.LongRunning;
using Google.Protobuf.WellKnownTypes;

public sealed partial class GeneratedDocumentServiceClientSnippets
{
    /// <summary>Snippet for ImportDocuments</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void ImportDocumentsRequestObject()
    {
        // Create client
        DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
        // Initialize request argument(s)
        ImportDocumentsRequest request = new ImportDocumentsRequest
        {
            ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
            InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
            ErrorConfig = new ImportErrorConfig(),
            ReconciliationMode = ImportDocumentsRequest.Types.ReconciliationMode.Unspecified,
            UpdateMask = new FieldMask(),
            AutoGenerateIds = false,
            IdField = "",
            ForceRefreshContent = false,
        };
        // Make the request
        Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = documentServiceClient.ImportDocuments(request);

        // Poll until the returned long-running operation is complete
        Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = response.PollUntilCompleted();
        // Retrieve the operation result
        ImportDocumentsResponse result = completedResponse.Result;

        // Or get the name of the operation
        string operationName = response.Name;
        // This name can be stored, then the long-running operation retrieved later by name
        Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = documentServiceClient.PollOnceImportDocuments(operationName);
        // Check if the retrieved long-running operation has completed
        if (retrievedResponse.IsCompleted)
        {
            // If it has completed, then access the result
            ImportDocumentsResponse retrievedResult = retrievedResponse.Result;
        }
    }
}
```

### Code Example 7 (text)

```text

package main

import (
	"context"

	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)

func main() {
	ctx := context.Background()
	// This snippet has been automatically generated and should be regarded as a code template only.
	// It will require modifications to work:
	// - It may require correct/in-range values for request initialization.
	// - It may require specifying regional endpoints when creating the service client as shown in:
	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
	c, err := discoveryengine.NewDataStoreClient(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &discoveryenginepb.CreateDataStoreRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CreateDataStoreRequest.
	}
	op, err := c.CreateDataStore(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}

	resp, err := op.Wait(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}

```

### Code Example 8 (text)

```text

package main

import (
	"context"

	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)

func main() {
	ctx := context.Background()
	// This snippet has been automatically generated and should be regarded as a code template only.
	// It will require modifications to work:
	// - It may require correct/in-range values for request initialization.
	// - It may require specifying regional endpoints when creating the service client as shown in:
	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
	c, err := discoveryengine.NewDocumentClient(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &discoveryenginepb.ImportDocumentsRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#ImportDocumentsRequest.
	}
	op, err := c.ImportDocuments(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}

	resp, err := op.Wait(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}

```

### Code Example 9 (text)

```text
import com.google.cloud.discoveryengine.v1.CollectionName;
import com.google.cloud.discoveryengine.v1.CreateDataStoreRequest;
import com.google.cloud.discoveryengine.v1.DataStore;
import com.google.cloud.discoveryengine.v1.DataStoreServiceClient;

public class SyncCreateDataStore {

  public static void main(String[] args) throws Exception {
    syncCreateDataStore();
  }

  public static void syncCreateDataStore() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
      CreateDataStoreRequest request =
          CreateDataStoreRequest.newBuilder()
              .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
              .setDataStore(DataStore.newBuilder().build())
              .setDataStoreId("dataStoreId929489618")
              .setCreateAdvancedSiteSearch(true)
              .setSkipDefaultSchemaCreation(true)
              .build();
      DataStore response = dataStoreServiceClient.createDataStoreAsync(request).get();
    }
  }
}
```

### Code Example 10 (text)

```text
import com.google.cloud.discoveryengine.v1.BranchName;
import com.google.cloud.discoveryengine.v1.DocumentServiceClient;
import com.google.cloud.discoveryengine.v1.ImportDocumentsRequest;
import com.google.cloud.discoveryengine.v1.ImportDocumentsResponse;
import com.google.cloud.discoveryengine.v1.ImportErrorConfig;
import com.google.protobuf.FieldMask;

public class SyncImportDocuments {

  public static void main(String[] args) throws Exception {
    syncImportDocuments();
  }

  public static void syncImportDocuments() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
      ImportDocumentsRequest request =
          ImportDocumentsRequest.newBuilder()
              .setParent(
                  BranchName.ofProjectLocationDataStoreBranchName(
                          "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                      .toString())
              .setErrorConfig(ImportErrorConfig.newBuilder().build())
              .setUpdateMask(FieldMask.newBuilder().build())
              .setAutoGenerateIds(true)
              .setIdField("idField1629396127")
              .build();
      ImportDocumentsResponse response = documentServiceClient.importDocumentsAsync(request).get();
    }
  }
}
```

### Code Example 11 (text)

```text
/**
 * This snippet has been automatically generated and should be regarded as a code template only.
 * It will require modifications to work.
 * It may require correct/in-range values for request initialization.
 * TODO(developer): Uncomment these variables before running the sample.
 */
/**
 *  Required. The parent resource name, such as
 *  `projects/{project}/locations/{location}/collections/{collection}`.
 */
// const parent = 'abc123'
/**
 *  Required. The DataStore google.cloud.discoveryengine.v1.DataStore  to
 *  create.
 */
// const dataStore = {}
/**
 *  Required. The ID to use for the
 *  DataStore google.cloud.discoveryengine.v1.DataStore, which will become
 *  the final component of the
 *  DataStore google.cloud.discoveryengine.v1.DataStore's resource name.
 *  This field must conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
 *  standard with a length limit of 63 characters. Otherwise, an
 *  INVALID_ARGUMENT error is returned.
 */
// const dataStoreId = 'abc123'
/**
 *  A boolean flag indicating whether user want to directly create an advanced
 *  data store for site search.
 *  If the data store is not configured as site
 *  search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will
 *  be ignored.
 */
// const createAdvancedSiteSearch = true
/**
 *  A boolean flag indicating whether to skip the default schema creation for
 *  the data store. Only enable this flag if you are certain that the default
 *  schema is incompatible with your use case.
 *  If set to true, you must manually create a schema for the data store before
 *  any documents can be ingested.
 *  This flag cannot be specified if `data_store.starting_schema` is specified.
 */
// const skipDefaultSchemaCreation = true

// Imports the Discoveryengine library
const {DataStoreServiceClient} = require('@google-cloud/discoveryengine').v1;

// Instantiates a client
const discoveryengineClient = new DataStoreServiceClient();

async function callCreateDataStore() {
  // Construct request
  const request = {
    parent,
    dataStore,
    dataStoreId,
  };

  // Run request
  const [operation] = await discoveryengineClient.createDataStore(request);
  const [response] = await operation.promise();
  console.log(response);
}

callCreateDataStore();
```

### Code Example 12 (text)

```text
/**
 * This snippet has been automatically generated and should be regarded as a code template only.
 * It will require modifications to work.
 * It may require correct/in-range values for request initialization.
 * TODO(developer): Uncomment these variables before running the sample.
 */
/**
 *  The Inline source for the input content for documents.
 */
// const inlineSource = {}
/**
 *  Cloud Storage location for the input content.
 */
// const gcsSource = {}
/**
 *  BigQuery input source.
 */
// const bigquerySource = {}
/**
 *  FhirStore input source.
 */
// const fhirStoreSource = {}
/**
 *  Spanner input source.
 */
// const spannerSource = {}
/**
 *  Cloud SQL input source.
 */
// const cloudSqlSource = {}
/**
 *  Firestore input source.
 */
// const firestoreSource = {}
/**
 *  AlloyDB input source.
 */
// const alloyDbSource = {}
/**
 *  Cloud Bigtable input source.
 */
// const bigtableSource = {}
/**
 *  Required. The parent branch resource name, such as
 *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
 *  Requires create/update permission.
 */
// const parent = 'abc123'
/**
 *  The desired location of errors incurred during the Import.
 */
// const errorConfig = {}
/**
 *  The mode of reconciliation between existing documents and the documents to
 *  be imported. Defaults to
 *  ReconciliationMode.INCREMENTAL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL.
 */
// const reconciliationMode = {}
/**
 *  Indicates which fields in the provided imported documents to update. If
 *  not set, the default is to update all fields.
 */
// const updateMask = {}
/**
 *  Whether to automatically generate IDs for the documents if absent.
 *  If set to `true`,
 *  Document.id google.cloud.discoveryengine.v1.Document.id s are
 *  automatically generated based on the hash of the payload, where IDs may not
 *  be consistent during multiple imports. In which case
 *  ReconciliationMode.FULL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.FULL 
 *  is highly recommended to avoid duplicate contents. If unset or set to
 *  `false`, Document.id google.cloud.discoveryengine.v1.Document.id s have
 *  to be specified using
 *  id_field google.cloud.discoveryengine.v1.ImportDocumentsRequest.id_field,
 *  otherwise, documents without IDs fail to be imported.
 *  Supported data sources:
 *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
 *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
 *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
 *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
 *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
 *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
 */
// const autoGenerateIds = true
/**
 *  The field indicates the ID field or column to be used as unique IDs of
 *  the documents.
 *  For GcsSource google.cloud.discoveryengine.v1.GcsSource  it is the key of
 *  the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`.
 *  For others, it may be the column name of the table where the unique ids are
 *  stored.
 *  The values of the JSON field or the table column are used as the
 *  Document.id google.cloud.discoveryengine.v1.Document.id s. The JSON field
 *  or the table column must be of string type, and the values must be set as
 *  valid strings conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
 *  with 1-63 characters. Otherwise, documents without valid IDs fail to be
 *  imported.
 *  Only set this field when
 *  auto_generate_ids google.cloud.discoveryengine.v1.ImportDocumentsRequest.auto_generate_ids 
 *  is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  If it is unset, a default value `_id` is used when importing from the
 *  allowed data sources.
 *  Supported data sources:
 *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
 *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
 *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
 *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
 *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
 *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
 */
// const idField = 'abc123'
/**
 *  Optional. Whether to force refresh the unstructured content of the
 *  documents.
 *  If set to `true`, the content part of the documents will be refreshed
 *  regardless of the update status of the referencing content.
 */
// const forceRefreshContent = true

// Imports the Discoveryengine library
const {DocumentServiceClient} = require('@google-cloud/discoveryengine').v1;

// Instantiates a client
const discoveryengineClient = new DocumentServiceClient();

async function callImportDocuments() {
  // Construct request
  const request = {
    parent,
  };

  // Run request
  const [operation] = await discoveryengineClient.importDocuments(request);
  const [response] = await operation.promise();
  console.log(response);
}

callImportDocuments();
```

### Code Example 13 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 14 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# bigquery_dataset = "YOUR_BIGQUERY_DATASET"
# bigquery_table = "YOUR_BIGQUERY_TABLE"

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    bigquery_source=discoveryengine.BigQuerySource(
        project_id=project_id,
        dataset_id=bigquery_dataset,
        table_id=bigquery_table,
        data_schema="custom",
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 15 (text)

```text
require "google/cloud/discovery_engine/v1"

##
# Snippet for the create_data_store call in the DataStoreService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store.
#
def create_data_store
  # Create a client object. The client can be reused for multiple calls.
  client = Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client.new

  # Create a request. To set request fields, pass in keyword arguments.
  request = Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest.new

  # Call the create_data_store method.
  result = client.create_data_store request

  # The returned object is of type Gapic::Operation. You can use it to
  # check the status of an operation, cancel it, or wait for results.
  # Here is how to wait for a response.
  result.wait_until_done! timeout: 60
  if result.response?
    p result.response
  else
    puts "No response received."
  end
end
```

### Code Example 16 (text)

```text
require "google/cloud/discovery_engine/v1"

##
# Snippet for the import_documents call in the DocumentService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#import_documents.
#
def import_documents
  # Create a client object. The client can be reused for multiple calls.
  client = Google::Cloud::DiscoveryEngine::V1::DocumentService::Client.new

  # Create a request. To set request fields, pass in keyword arguments.
  request = Google::Cloud::DiscoveryEngine::V1::ImportDocumentsRequest.new

  # Call the import_documents method.
  result = client.import_documents request

  # The returned object is of type Gapic::Operation. You can use it to
  # check the status of an operation, cancel it, or wait for results.
  # Here is how to wait for a response.
  result.wait_until_done! timeout: 60
  if result.response?
    p result.response
  else
    puts "No response received."
  end
end
```

### Code Example 17 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DATA_STORE_DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
  "contentConfig": "CONTENT_REQUIRED",
}'

```

### Code Example 18 (text)

```text
  curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
  -d '{
    "gcsSource": {
      "inputUris": ["INPUT_FILE_PATTERN_1", "INPUT_FILE_PATTERN_2"],
      "dataSchema": "DATA_SCHEMA",
    },
    "reconciliationMode": "RECONCILIATION_MODE",
    "autoGenerateIds": "AUTO_GENERATE_IDS",
    "idField": "ID_FIELD",
    "errorConfig": {
      "gcsPrefix": "ERROR_DIRECTORY"
    }
  }'

```

### Code Example 19 (text)

```text
using Google.Cloud.DiscoveryEngine.V1;
using Google.LongRunning;

public sealed partial class GeneratedDataStoreServiceClientSnippets
{
    /// <summary>Snippet for CreateDataStore</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void CreateDataStoreRequestObject()
    {
        // Create client
        DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.Create();
        // Initialize request argument(s)
        CreateDataStoreRequest request = new CreateDataStoreRequest
        {
            ParentAsCollectionName = CollectionName.FromProjectLocationCollection("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
            DataStore = new DataStore(),
            DataStoreId = "",
            CreateAdvancedSiteSearch = false,
            SkipDefaultSchemaCreation = false,
        };
        // Make the request
        Operation<DataStore, CreateDataStoreMetadata> response = dataStoreServiceClient.CreateDataStore(request);

        // Poll until the returned long-running operation is complete
        Operation<DataStore, CreateDataStoreMetadata> completedResponse = response.PollUntilCompleted();
        // Retrieve the operation result
        DataStore result = completedResponse.Result;

        // Or get the name of the operation
        string operationName = response.Name;
        // This name can be stored, then the long-running operation retrieved later by name
        Operation<DataStore, CreateDataStoreMetadata> retrievedResponse = dataStoreServiceClient.PollOnceCreateDataStore(operationName);
        // Check if the retrieved long-running operation has completed
        if (retrievedResponse.IsCompleted)
        {
            // If it has completed, then access the result
            DataStore retrievedResult = retrievedResponse.Result;
        }
    }
}
```

### Code Example 20 (text)

```text
using Google.Cloud.DiscoveryEngine.V1;
using Google.LongRunning;
using Google.Protobuf.WellKnownTypes;

public sealed partial class GeneratedDocumentServiceClientSnippets
{
    /// <summary>Snippet for ImportDocuments</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void ImportDocumentsRequestObject()
    {
        // Create client
        DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
        // Initialize request argument(s)
        ImportDocumentsRequest request = new ImportDocumentsRequest
        {
            ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
            InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
            ErrorConfig = new ImportErrorConfig(),
            ReconciliationMode = ImportDocumentsRequest.Types.ReconciliationMode.Unspecified,
            UpdateMask = new FieldMask(),
            AutoGenerateIds = false,
            IdField = "",
            ForceRefreshContent = false,
        };
        // Make the request
        Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = documentServiceClient.ImportDocuments(request);

        // Poll until the returned long-running operation is complete
        Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = response.PollUntilCompleted();
        // Retrieve the operation result
        ImportDocumentsResponse result = completedResponse.Result;

        // Or get the name of the operation
        string operationName = response.Name;
        // This name can be stored, then the long-running operation retrieved later by name
        Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = documentServiceClient.PollOnceImportDocuments(operationName);
        // Check if the retrieved long-running operation has completed
        if (retrievedResponse.IsCompleted)
        {
            // If it has completed, then access the result
            ImportDocumentsResponse retrievedResult = retrievedResponse.Result;
        }
    }
}
```

### Code Example 21 (text)

```text

package main

import (
	"context"

	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)

func main() {
	ctx := context.Background()
	// This snippet has been automatically generated and should be regarded as a code template only.
	// It will require modifications to work:
	// - It may require correct/in-range values for request initialization.
	// - It may require specifying regional endpoints when creating the service client as shown in:
	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
	c, err := discoveryengine.NewDataStoreClient(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &discoveryenginepb.CreateDataStoreRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CreateDataStoreRequest.
	}
	op, err := c.CreateDataStore(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}

	resp, err := op.Wait(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}

```

### Code Example 22 (text)

```text

package main

import (
	"context"

	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)

func main() {
	ctx := context.Background()
	// This snippet has been automatically generated and should be regarded as a code template only.
	// It will require modifications to work:
	// - It may require correct/in-range values for request initialization.
	// - It may require specifying regional endpoints when creating the service client as shown in:
	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
	c, err := discoveryengine.NewDocumentClient(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &discoveryenginepb.ImportDocumentsRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#ImportDocumentsRequest.
	}
	op, err := c.ImportDocuments(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}

	resp, err := op.Wait(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}

```

### Code Example 23 (text)

```text
import com.google.cloud.discoveryengine.v1.CollectionName;
import com.google.cloud.discoveryengine.v1.CreateDataStoreRequest;
import com.google.cloud.discoveryengine.v1.DataStore;
import com.google.cloud.discoveryengine.v1.DataStoreServiceClient;

public class SyncCreateDataStore {

  public static void main(String[] args) throws Exception {
    syncCreateDataStore();
  }

  public static void syncCreateDataStore() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
      CreateDataStoreRequest request =
          CreateDataStoreRequest.newBuilder()
              .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
              .setDataStore(DataStore.newBuilder().build())
              .setDataStoreId("dataStoreId929489618")
              .setCreateAdvancedSiteSearch(true)
              .setSkipDefaultSchemaCreation(true)
              .build();
      DataStore response = dataStoreServiceClient.createDataStoreAsync(request).get();
    }
  }
}
```

### Code Example 24 (text)

```text
import com.google.cloud.discoveryengine.v1.BranchName;
import com.google.cloud.discoveryengine.v1.DocumentServiceClient;
import com.google.cloud.discoveryengine.v1.ImportDocumentsRequest;
import com.google.cloud.discoveryengine.v1.ImportDocumentsResponse;
import com.google.cloud.discoveryengine.v1.ImportErrorConfig;
import com.google.protobuf.FieldMask;

public class SyncImportDocuments {

  public static void main(String[] args) throws Exception {
    syncImportDocuments();
  }

  public static void syncImportDocuments() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (DocumentServiceClient documentServiceClient = DocumentServiceClient.create()) {
      ImportDocumentsRequest request =
          ImportDocumentsRequest.newBuilder()
              .setParent(
                  BranchName.ofProjectLocationDataStoreBranchName(
                          "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                      .toString())
              .setErrorConfig(ImportErrorConfig.newBuilder().build())
              .setUpdateMask(FieldMask.newBuilder().build())
              .setAutoGenerateIds(true)
              .setIdField("idField1629396127")
              .build();
      ImportDocumentsResponse response = documentServiceClient.importDocumentsAsync(request).get();
    }
  }
}
```

### Code Example 25 (text)

```text
/**
 * This snippet has been automatically generated and should be regarded as a code template only.
 * It will require modifications to work.
 * It may require correct/in-range values for request initialization.
 * TODO(developer): Uncomment these variables before running the sample.
 */
/**
 *  Required. The parent resource name, such as
 *  `projects/{project}/locations/{location}/collections/{collection}`.
 */
// const parent = 'abc123'
/**
 *  Required. The DataStore google.cloud.discoveryengine.v1.DataStore  to
 *  create.
 */
// const dataStore = {}
/**
 *  Required. The ID to use for the
 *  DataStore google.cloud.discoveryengine.v1.DataStore, which will become
 *  the final component of the
 *  DataStore google.cloud.discoveryengine.v1.DataStore's resource name.
 *  This field must conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
 *  standard with a length limit of 63 characters. Otherwise, an
 *  INVALID_ARGUMENT error is returned.
 */
// const dataStoreId = 'abc123'
/**
 *  A boolean flag indicating whether user want to directly create an advanced
 *  data store for site search.
 *  If the data store is not configured as site
 *  search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will
 *  be ignored.
 */
// const createAdvancedSiteSearch = true
/**
 *  A boolean flag indicating whether to skip the default schema creation for
 *  the data store. Only enable this flag if you are certain that the default
 *  schema is incompatible with your use case.
 *  If set to true, you must manually create a schema for the data store before
 *  any documents can be ingested.
 *  This flag cannot be specified if `data_store.starting_schema` is specified.
 */
// const skipDefaultSchemaCreation = true

// Imports the Discoveryengine library
const {DataStoreServiceClient} = require('@google-cloud/discoveryengine').v1;

// Instantiates a client
const discoveryengineClient = new DataStoreServiceClient();

async function callCreateDataStore() {
  // Construct request
  const request = {
    parent,
    dataStore,
    dataStoreId,
  };

  // Run request
  const [operation] = await discoveryengineClient.createDataStore(request);
  const [response] = await operation.promise();
  console.log(response);
}

callCreateDataStore();
```

### Code Example 26 (text)

```text
/**
 * This snippet has been automatically generated and should be regarded as a code template only.
 * It will require modifications to work.
 * It may require correct/in-range values for request initialization.
 * TODO(developer): Uncomment these variables before running the sample.
 */
/**
 *  The Inline source for the input content for documents.
 */
// const inlineSource = {}
/**
 *  Cloud Storage location for the input content.
 */
// const gcsSource = {}
/**
 *  BigQuery input source.
 */
// const bigquerySource = {}
/**
 *  FhirStore input source.
 */
// const fhirStoreSource = {}
/**
 *  Spanner input source.
 */
// const spannerSource = {}
/**
 *  Cloud SQL input source.
 */
// const cloudSqlSource = {}
/**
 *  Firestore input source.
 */
// const firestoreSource = {}
/**
 *  AlloyDB input source.
 */
// const alloyDbSource = {}
/**
 *  Cloud Bigtable input source.
 */
// const bigtableSource = {}
/**
 *  Required. The parent branch resource name, such as
 *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
 *  Requires create/update permission.
 */
// const parent = 'abc123'
/**
 *  The desired location of errors incurred during the Import.
 */
// const errorConfig = {}
/**
 *  The mode of reconciliation between existing documents and the documents to
 *  be imported. Defaults to
 *  ReconciliationMode.INCREMENTAL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL.
 */
// const reconciliationMode = {}
/**
 *  Indicates which fields in the provided imported documents to update. If
 *  not set, the default is to update all fields.
 */
// const updateMask = {}
/**
 *  Whether to automatically generate IDs for the documents if absent.
 *  If set to `true`,
 *  Document.id google.cloud.discoveryengine.v1.Document.id s are
 *  automatically generated based on the hash of the payload, where IDs may not
 *  be consistent during multiple imports. In which case
 *  ReconciliationMode.FULL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.FULL 
 *  is highly recommended to avoid duplicate contents. If unset or set to
 *  `false`, Document.id google.cloud.discoveryengine.v1.Document.id s have
 *  to be specified using
 *  id_field google.cloud.discoveryengine.v1.ImportDocumentsRequest.id_field,
 *  otherwise, documents without IDs fail to be imported.
 *  Supported data sources:
 *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
 *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
 *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
 *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
 *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
 *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
 */
// const autoGenerateIds = true
/**
 *  The field indicates the ID field or column to be used as unique IDs of
 *  the documents.
 *  For GcsSource google.cloud.discoveryengine.v1.GcsSource  it is the key of
 *  the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`.
 *  For others, it may be the column name of the table where the unique ids are
 *  stored.
 *  The values of the JSON field or the table column are used as the
 *  Document.id google.cloud.discoveryengine.v1.Document.id s. The JSON field
 *  or the table column must be of string type, and the values must be set as
 *  valid strings conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
 *  with 1-63 characters. Otherwise, documents without valid IDs fail to be
 *  imported.
 *  Only set this field when
 *  auto_generate_ids google.cloud.discoveryengine.v1.ImportDocumentsRequest.auto_generate_ids 
 *  is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  If it is unset, a default value `_id` is used when importing from the
 *  allowed data sources.
 *  Supported data sources:
 *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
 *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
 *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
 *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
 *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
 *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
 *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
 *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
 */
// const idField = 'abc123'
/**
 *  Optional. Whether to force refresh the unstructured content of the
 *  documents.
 *  If set to `true`, the content part of the documents will be refreshed
 *  regardless of the update status of the referencing content.
 */
// const forceRefreshContent = true

// Imports the Discoveryengine library
const {DocumentServiceClient} = require('@google-cloud/discoveryengine').v1;

// Instantiates a client
const discoveryengineClient = new DocumentServiceClient();

async function callImportDocuments() {
  // Construct request
  const request = {
    parent,
  };

  // Run request
  const [operation] = await discoveryengineClient.importDocuments(request);
  const [response] = await operation.promise();
  console.log(response);
}

callImportDocuments();
```

### Code Example 27 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 28 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"

# Examples:
# - Unstructured documents
#   - `gs://bucket/directory/file.pdf`
#   - `gs://bucket/directory/*.pdf`
# - Unstructured documents with JSONL Metadata
#   - `gs://bucket/directory/file.json`
# - Unstructured documents with CSV Metadata
#   - `gs://bucket/directory/file.csv`
# gcs_uri = "YOUR_GCS_PATH"

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    gcs_source=discoveryengine.GcsSource(
        # Multiple URIs are supported
        input_uris=[gcs_uri],
        # Options:
        # - `content` - Unstructured documents (PDF, HTML, DOC, TXT, PPTX)
        # - `custom` - Unstructured documents with custom JSONL metadata
        # - `document` - Structured documents in the discoveryengine.Document format.
        # - `csv` - Unstructured documents with CSV metadata
        data_schema="content",
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 29 (text)

```text
require "google/cloud/discovery_engine/v1"

##
# Snippet for the create_data_store call in the DataStoreService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store.
#
def create_data_store
  # Create a client object. The client can be reused for multiple calls.
  client = Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client.new

  # Create a request. To set request fields, pass in keyword arguments.
  request = Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest.new

  # Call the create_data_store method.
  result = client.create_data_store request

  # The returned object is of type Gapic::Operation. You can use it to
  # check the status of an operation, cancel it, or wait for results.
  # Here is how to wait for a response.
  result.wait_until_done! timeout: 60
  if result.response?
    p result.response
  else
    puts "No response received."
  end
end
```

### Code Example 30 (text)

```text
require "google/cloud/discovery_engine/v1"

##
# Snippet for the import_documents call in the DocumentService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#import_documents.
#
def import_documents
  # Create a client object. The client can be reused for multiple calls.
  client = Google::Cloud::DiscoveryEngine::V1::DocumentService::Client.new

  # Create a request. To set request fields, pass in keyword arguments.
  request = Google::Cloud::DiscoveryEngine::V1::ImportDocumentsRequest.new

  # Call the import_documents method.
  result = client.import_documents request

  # The returned object is of type Gapic::Operation. You can use it to
  # check the status of an operation, cancel it, or wait for results.
  # Here is how to wait for a response.
  result.wait_until_done! timeout: 60
  if result.response?
    p result.response
  else
    puts "No response received."
  end
end
```

### Code Example 31 (text)

```text
https://www.googleapis.com/auth/drive.readonly,
https://www.googleapis.com/auth/admin.directory.user.readonly,
https://www.googleapis.com/auth/admin.directory.group.readonly,
https://www.googleapis.com/auth/admin.directory.domain.readonly,
https://www.googleapis.com/auth/admin.reports.audit.readonly

```

### Code Example 32 (text)

```text
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`

```

### Code Example 33 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'

```

### Code Example 34 (text)

```text
  curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
  -d '{
    "cloudSqlSource": {
      "projectId": "SQL_PROJECT_ID",
      "instanceId": "INSTANCE_ID",
      "databaseId": "DATABASE_ID",
      "tableId": "TABLE_ID",
      "gcsStagingDir": "STAGING_DIRECTORY"
    },
    "reconciliationMode": "RECONCILIATION_MODE",
    "autoGenerateIds": "AUTO_GENERATE_IDS",
    "idField": "ID_FIELD",
  }'

```

### Code Example 35 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 36 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# sql_project_id = "YOUR_SQL_PROJECT_ID"
# sql_instance_id = "YOUR_SQL_INSTANCE_ID"
# sql_database_id = "YOUR_SQL_DATABASE_ID"
# sql_table_id = "YOUR_SQL_TABLE_ID"

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    cloud_sql_source=discoveryengine.CloudSqlSource(
        project_id=sql_project_id,
        instance_id=sql_instance_id,
        database_id=sql_database_id,
        table_id=sql_table_id,
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 37 (text)

```text
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com

```

### Code Example 38 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
  "contentConfig": "CONTENT_REQUIRED",
}'

```

### Code Example 39 (text)

```text
  curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
  -d '{
    "cloudSpannerSource": {
      "projectId": "SPANNER_PROJECT_ID",
      "instanceId": "INSTANCE_ID",
      "databaseId": "DATABASE_ID",
      "tableId": "TABLE_ID",
      "enableDataBoost": "DATA_BOOST_BOOLEAN"
    },
    "reconciliationMode": "RECONCILIATION_MODE",
    "autoGenerateIds": "AUTO_GENERATE_IDS",
    "idField": "ID_FIELD",
  }'

```

### Code Example 40 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 41 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# spanner_project_id = "YOUR_SPANNER_PROJECT_ID"
# spanner_instance_id = "YOUR_SPANNER_INSTANCE_ID"
# spanner_database_id = "YOUR_SPANNER_DATABASE_ID"
# spanner_table_id = "YOUR_SPANNER_TABLE_ID"

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    spanner_source=discoveryengine.SpannerSource(
        project_id=spanner_project_id,
        instance_id=spanner_instance_id,
        database_id=spanner_database_id,
        table_id=spanner_table_id,
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 42 (text)

```text
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com

```

### Code Example 43 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'

```

### Code Example 44 (text)

```text
  curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
  -d '{
    "firestoreSource": {
      "projectId": "FIRESTORE_PROJECT_ID",
      "databaseId": "DATABASE_ID",
      "collectionId": "COLLECTION_ID",
    },
    "reconciliationMode": "RECONCILIATION_MODE",
    "autoGenerateIds": "AUTO_GENERATE_IDS",
    "idField": "ID_FIELD",
  }'

```

### Code Example 45 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 46 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# firestore_project_id = "YOUR_FIRESTORE_PROJECT_ID"
# firestore_database_id = "YOUR_FIRESTORE_DATABASE_ID"
# firestore_collection_id = "YOUR_FIRESTORE_COLLECTION_ID"

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    firestore_source=discoveryengine.FirestoreSource(
        project_id=firestore_project_id,
        database_id=firestore_database_id,
        collection_id=firestore_collection_id,
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 47 (text)

```text
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`

```

### Code Example 48 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'

```

### Code Example 49 (text)

```text
  curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
  -d '{
    "bigtableSource ": {
      "projectId": "BIGTABLE_PROJECT_ID",
      "instanceId": "INSTANCE_ID",
      "tableId": "TABLE_ID",
      "bigtableOptions": {
        "keyFieldName": "KEY_FIELD_NAME",
        "families": {
          "key": "KEY",
          "value": {
            "fieldName": "FIELD_NAME",
            "encoding": "ENCODING",
            "type": "TYPE",
            "columns": [
              {
                "qualifier": "QUALIFIER",
                "fieldName": "FIELD_NAME",
                "encoding": "COLUMN_ENCODING",
                "type": "COLUMN_VALUES_TYPE"
              }
            ]
          }
         }
         ...
      }
    },
    "reconciliationMode": "RECONCILIATION_MODE",
    "autoGenerateIds": "AUTO_GENERATE_IDS",
    "idField": "ID_FIELD",
  }'

```

### Code Example 50 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 51 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# bigtable_project_id = "YOUR_BIGTABLE_PROJECT_ID"
# bigtable_instance_id = "YOUR_BIGTABLE_INSTANCE_ID"
# bigtable_table_id = "YOUR_BIGTABLE_TABLE_ID"

#  For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

bigtable_options = discoveryengine.BigtableOptions(
    families={
        "family_name_1": discoveryengine.BigtableOptions.BigtableColumnFamily(
            type_=discoveryengine.BigtableOptions.Type.STRING,
            encoding=discoveryengine.BigtableOptions.Encoding.TEXT,
            columns=[
                discoveryengine.BigtableOptions.BigtableColumn(
                    qualifier="qualifier_1".encode("utf-8"),
                    field_name="field_name_1",
                ),
            ],
        ),
        "family_name_2": discoveryengine.BigtableOptions.BigtableColumnFamily(
            type_=discoveryengine.BigtableOptions.Type.INTEGER,
            encoding=discoveryengine.BigtableOptions.Encoding.BINARY,
        ),
    }
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    bigtable_source=discoveryengine.BigtableSource(
        project_id=bigtable_project_id,
        instance_id=bigtable_instance_id,
        table_id=bigtable_table_id,
        bigtable_options=bigtable_options,
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 52 (text)

```text
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com

```

### Code Example 53 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'

```

### Code Example 54 (text)

```text
  curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
  -d '{
    "alloydbSource": {
      "projectId": "ALLOYDB_PROJECT_ID",
      "locationId": "LOCATION_ID",
      "clusterId": "CLUSTER_ID",
      "databaseId": "DATABASE_ID",
      "tableId": "TABLE_ID",
    },
    "reconciliationMode": "RECONCILIATION_MODE",
    "autoGenerateIds": "AUTO_GENERATE_IDS",
    "idField": "ID_FIELD",
  }'

```

### Code Example 55 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"


def create_data_store_sample(
    project_id: str,
    location: str,
    data_store_id: str,
) -> str:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DataStoreServiceClient(client_options=client_options)

    # The full resource name of the collection
    # e.g. projects/{project}/locations/{location}/collections/default_collection
    parent = client.collection_path(
        project=project_id,
        location=location,
        collection="default_collection",
    )

    data_store = discoveryengine.DataStore(
        display_name="My Data Store",
        # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
        # TODO(developer): Update content_config based on data store type.
        # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
        content_config=discoveryengine.DataStore.ContentConfig.CONTENT_REQUIRED,
    )

    request = discoveryengine.CreateDataStoreRequest(
        parent=parent,
        data_store_id=data_store_id,
        data_store=data_store,
        # Optional: For Advanced Site Search Only
        # create_advanced_site_search=True,
    )

    # Make the request
    operation = client.create_data_store(request=request)

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.CreateDataStoreMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return operation.operation.name


```

### Code Example 56 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# alloy_db_project_id = "YOUR_ALLOY_DB_PROJECT_ID"
# alloy_db_location_id = "YOUR_ALLOY_DB_LOCATION_ID"
# alloy_db_cluster_id = "YOUR_ALLOY_DB_CLUSTER_ID"
# alloy_db_database_id = "YOUR_ALLOY_DB_DATABASE_ID"
# alloy_db_table_id = "YOUR_ALLOY_DB_TABLE_ID"

# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options = (
    ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    if location != "global"
    else None
)

# Create a client
client = discoveryengine.DocumentServiceClient(client_options=client_options)

# The full resource name of the search engine branch.
# e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
parent = client.branch_path(
    project=project_id,
    location=location,
    data_store=data_store_id,
    branch="default_branch",
)

request = discoveryengine.ImportDocumentsRequest(
    parent=parent,
    alloy_db_source=discoveryengine.AlloyDbSource(
        project_id=alloy_db_project_id,
        location_id=alloy_db_location_id,
        cluster_id=alloy_db_cluster_id,
        database_id=alloy_db_database_id,
        table_id=alloy_db_table_id,
    ),
    # Options: `FULL`, `INCREMENTAL`
    reconciliation_mode=discoveryengine.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL,
)

# Make the request
operation = client.import_documents(request=request)

print(f"Waiting for operation to complete: {operation.operation.name}")
response = operation.result()

# After the operation is complete,
# get information from operation metadata
metadata = discoveryengine.ImportDocumentsMetadata(operation.metadata)

# Handle the response
print(response)
print(metadata)
```

### Code Example 57 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
-d '{
  "displayName": "DATA_STORE_DISPLAY_NAME",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"]
}'

```

### Code Example 58 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents?documentId=DOCUMENT_ID" \
-d '{
  "jsonData": "JSON_DOCUMENT_STRING"
}'

```

### Code Example 59 (text)

```text
{ \"title\": \"test title\", \"categories\": [\"cat_1\", \"cat_2\"], \"uri\": \"test uri\"}

```

### Code Example 60 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents?documentId=DOCUMENT_ID" \
-d '{
  "structData": JSON_DOCUMENT_OBJECT
}'

```

### Code Example 61 (text)

```text
```json
{
  "title": "test title",
  "categories": [
    "cat_1",
    "cat_2"
  ],
  "uri": "test uri"
}
```

```

### Code Example 62 (text)

```text
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID" \
-d '{
  "jsonData": "JSON_DOCUMENT_STRING"
}'

```

### Code Example 63 (text)

```text
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID" \
-d '{
  "structData": JSON_DOCUMENT_OBJECT
}'

```

