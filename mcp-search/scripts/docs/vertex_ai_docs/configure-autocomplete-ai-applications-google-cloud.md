# Configure autocomplete  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete](https://cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete)

Home
AI Applications
Documentation
Guides
Send feedback
Configure autocomplete
Stay organized with collections
Save and categorize content based on your preferences.
This page describes Vertex AI Search's basic autocomplete feature.
Autocomplete generates query suggestions based on the first few characters
entered for the query.
The suggestions that autocomplete generates vary depending on the type of data
that the search app uses:
Structured and unstructured data.
By default, autocomplete
generates suggestions based on the content of documents in the data store.
After document import, by default, autocomplete doesn't start generating
suggestions until there is sufficient quality data, typically a couple of
days. If you make autocomplete requests through the API, autocomplete can
generate suggestions that are based on the search history or user events.
Website data.
By default, autocomplete generates suggestions
from the search history. Autocomplete requires real search traffic. After
search traffic begins, autocomplete takes a day or two before generating
suggestions. Suggestions can be generated from web-crawled data from public
sites with the experimental
advanced document data model
.
Healthcare data.
By default, a canonical medical data source is used to
generate autocomplete suggestions for healthcare data stores.
The query suggestions model determines what type of data autocomplete uses to
generate suggestions. There are four query suggestions models:
Document.
The document model generates suggestions from
user-imported documents. This model isn't available for website data or
healthcare data.
Completable Fields.
The completable fields model suggests text taken
directly from structured data fields. Only those fields that are annotated
with
completable
are used for autocomplete suggestions. This model is only
available for structured data.
Search history.
The search history model generates suggestions from the
history of
SearchService.search
API calls. Don't use
this model if there is no traffic available for the
servingConfigs.search
method. This model isn't
available for healthcare data.
User event.
The user event model generates suggestions from
user-imported search events. This model isn't
available for healthcare data.
Autocomplete requests are sent using the
dataStores.completeQuery
method.
Alternatively, if you don't want to use a query suggestions model, you can use
Imported suggestions
that provide autocomplete
suggestions based on an imported list of suggestions. For more information,
see
Use an imported list of autocomplete suggestions
.
Model types available according to data type
The following table shows the query suggestions model types available for each
data type.
Query
suggestions
model
Data
source
Website
data
Structured
data
Unstructured
data
Document
Imported
by user
✔*
(default)
✔ (default)
Completable
fields
Imported
by user
✔
Search
history
Automatically
collected
✔
(default)
✔
✔
User
events
Imported
by user or
automatically
collected
by widget
✔
✔
✔
Web-crawled
content
Crawled from
content from
public
websites
specified by
user
✔
†
* : The document schema must contain
title
or
description
fields, or there
must be fields that have been specified as
title
or
description
key
properties. See
Update a schema for structured data
.
†
: Web-crawled content can only be used as a data source if the
experimental advanced document data model for autocomplete is enabled. See
Advanced document data model
.
If you don't want to use the default model for your data type, you can
specify a different model when you send your autocomplete request. Autocomplete
requests are sent using the
dataStores.completeQuery
method. For
information, see
API instructions: Send an autocomplete request to choose a
different model
.
Autocomplete features
Vertex AI Search supports the following autocomplete features to show
the most helpful predictions when searching:
Feature
Description
Example or more information
Correct typos
Correct word spellings that are typos.
Milc
→
Milk
.
Remove unsafe terms
Powered by Google Safe Search.
Remove inappropriate queries.
Supported in English (
en
), French (
fr
),
German (
de
), Italian (
it
), Polish
(
pl
), Portuguese (
pt
), Russian (
ru
),
Spanish (
es
), and Ukranian (
uk
).
Text that's offensive, such as porn, racy, vulgar, violence.
Denylist
Remove terms that are listed in the denylist.
For more information, see
Use an autocomplete denylist
.
Deduplicate Terms
Powered by AI-driven semantic understanding.
For near-identical terms, either term matches, but only the more
popular one is suggested.
Shoes for Women
,
Womens Shoes
, and
Womans Shoes
are deduplicated,
and only the most popular one is suggested.
Tail match suggestions
Not available in US and EU multi-regions.
Optional setting.
If there are no autocomplete matches for the entire query, suggest
matches for only the trailing word of the query.
Not available for healthcare search.
For more information, see
Tail match suggestions
.
Tail match suggestions
Tail match suggestions are made using exact prefix matching against the last
word in a query string.
For example, say the query "songs with he" is sent in an autocomplete request.
When tail matching is enabled, autocomplete might find that the full prefix
"songs with he" does not have any matches. However, the last word in the query,
"he", has an exact prefix match with "hello world" and "hello kitty". In that
case, the returned suggestions are "songs with hello world" and "songs with
hello kitty" because there are no full match suggestions.
You can use this feature to reduce empty suggestion results and increase
suggestion diversity, making this especially useful in cases where data sources
(user event count, search history, and document topic coverage) is limited.
However, enabling tail match suggestions can reduce the overall quality of
suggestions. Because tail match only matches the trailing word of the prefix,
some returned suggestions might not make sense. For example, a query such as
"songs with he" might get a tail match suggestion like "songs with helpers
guides".
Tail match suggestions are only returned if:
include_tail_suggestions
is set to
true
in the
dataStores.completeQuery
request.
There are no full prefix match suggestions for the query.
Turn autocomplete on or off for a widget
To turn autocomplete on or off for a widget, follow these steps:
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit.
Click
Configurations
.
Click the
UI
tab.
Toggle the
Show autocomplete suggestions
option to turn autocomplete
suggestions for the widget on or off. When you enable autocomplete,
expect to wait a day or two before suggestions start.
Update autocomplete settings
To configure the autocomplete settings, follow these steps:
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit.
Click
Configurations
.
Click the
Autocomplete
tab.
Enter or select new values for the autocomplete settings you want to update:
Maximum number of suggestions:
The maximum number of
autocomplete suggestions that can be offered for a query.
Minimum length to trigger:
The minimum number of characters
that can be typed before autocomplete suggestions are offered.
Matching order
: The location in a query string that
autocomplete can start matching its suggestions from.
Query suggestions model
: The query suggestions model used to
generate the retrieved suggestions. This can be overridden in the
dataStores.completeQuery
using the
queryModel
parameter.
Enable autocomplete
: By default, autocomplete doesn't start making
suggestions until it has sufficient quality data, typically a couple
of days. If you want to override this default and start getting some
autocomplete suggestions sooner, select
Now
.
Even when you select
Now
, it can take a day for suggestions to be
generated and still some autocomplete suggestions will be missing
or poor quality until there is sufficient good data.
Click
Save and publish.
Changes take effect within a few minutes for
engines where autocomplete has already been turned on.
Update completable field annotations in schema
To turn on autocomplete for fields in structured data schema, follow these
steps:
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit. It must use structured
data.
Click
Data
.
Click the
Schema
tab.
Click
Edit
to select the schema fields to mark as
completable
.
Click
Save
to save the updated field configurations. These suggestions take around
a day to be generated and returned.
Send autocomplete requests
The following samples show how to send autocomplete requests.
REST
To send an autocomplete request using the API, follow these steps:
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
Call the
dataStores.completeQuery
method.
curl
-H
"Authorization: Bearer
$(
gcloud
auth
print-access-token
)
"
\
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
:completeQuery?query=
QUERY_STRING
"
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the data store that is associated
with your app.
QUERY_STRING
: the typeahead input used to
fetch suggestions.
Send an autocomplete request to a different model
To send an autocomplete request with a different query suggestions model, follow
these steps:
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
Call the
dataStores.completeQuery
method.
curl
-H
"Authorization: Bearer
$(
gcloud
auth
print-access-token
)
"
\
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
:completeQuery?query=
QUERY_STRING
&query_model=
QUERY_SUGGESTIONS_MODEL
"
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the unique ID of the data store that is
associated with your app.
QUERY_STRING
: the typeahead input used to
fetch suggestions.
AUTOCOMPLETE_MODEL
: the autocomplete data
QUERY_SUGGESTIONS_MODEL
: the query suggestions
model to use for the request:
document
,
document-completable
,
search-history
, or
user-event
. For healthcare data, use
healthcare-default
.
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
using
Google.Cloud.DiscoveryEngine.V1
;
public
sealed
partial
class
GeneratedCompletionServiceClientSnippets
{
/// <summary>Snippet for CompleteQuery</summary>
/// <remarks>
/// This snippet has been automatically generated and should be regarded as a code template only.
/// It will require modifications to work:
/// - It may require correct/in-range values for request initialization.
/// - It may require specifying regional endpoints when creating the service client as shown in
/// https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
/// </remarks>
public
void
CompleteQueryRequestObject
()
{
// Create client
CompletionServiceClient
completionServiceClient
=
CompletionServiceClient
.
Create
();
// Initialize request argument(s)
CompleteQueryRequest
request
=
new
CompleteQueryRequest
{
DataStoreAsDataStoreName
=
DataStoreName
.
FromProjectLocationDataStore
(
"[PROJECT]"
,
"[LOCATION]"
,
"[DATA_STORE]"
),
Query
=
""
,
QueryModel
=
""
,
UserPseudoId
=
""
,
IncludeTailSuggestions
=
false
,
};
// Make the request
CompleteQueryResponse
response
=
completionServiceClient
.
CompleteQuery
(
request
);
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
NewCompletionClient
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
CompleteQueryRequest
{
// TODO: Fill request struct fields.
// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CompleteQueryRequest.
}
resp
,
err
:=
c
.
CompleteQuery
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
import
com.google.cloud.discoveryengine.v1.CompleteQueryRequest
;
import
com.google.cloud.discoveryengine.v1.CompleteQueryResponse
;
import
com.google.cloud.discoveryengine.v1.CompletionServiceClient
;
import
com.google.cloud.discoveryengine.v1.DataStoreName
;
public
class
SyncCompleteQuery
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
syncCompleteQuery
();
}
public
static
void
syncCompleteQuery
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
CompletionServiceClient
completionServiceClient
=
CompletionServiceClient
.
create
())
{
CompleteQueryRequest
request
=
CompleteQueryRequest
.
newBuilder
()
.
setDataStore
(
DataStoreName
.
ofProjectLocationDataStoreName
(
"[PROJECT]"
,
"[LOCATION]"
,
"[DATA_STORE]"
)
.
toString
())
.
setQuery
(
"query107944136"
)
.
setQueryModel
(
"queryModel-184930495"
)
.
setUserPseudoId
(
"userPseudoId-1155274652"
)
.
setIncludeTailSuggestions
(
true
)
.
build
();
CompleteQueryResponse
response
=
completionServiceClient
.
completeQuery
(
request
);
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
/**
* This snippet has been automatically generated and should be regarded as a code template only.
* It will require modifications to work.
* It may require correct/in-range values for request initialization.
* TODO(developer): Uncomment these variables before running the sample.
*/
/**
* Required. The parent data store resource name for which the completion is
* performed, such as
* `projects/* /locations/global/collections/default_collection/dataStores/default_data_store`.
*/
// const dataStore = 'abc123'
/**
* Required. The typeahead input used to fetch suggestions. Maximum length is
* 128 characters.
*/
// const query = 'abc123'
/**
* Specifies the autocomplete data model. This overrides any model specified
* in the Configuration > Autocomplete section of the Cloud console. Currently
* supported values:
* * `document` - Using suggestions generated from user-imported documents.
* * `search-history` - Using suggestions generated from the past history of
* SearchService.Search google.cloud.discoveryengine.v1.SearchService.Search
* API calls. Do not use it when there is no traffic for Search API.
* * `user-event` - Using suggestions generated from user-imported search
* events.
* * `document-completable` - Using suggestions taken directly from
* user-imported document fields marked as completable.
* Default values:
* * `document` is the default model for regular dataStores.
* * `search-history` is the default model for site search dataStores.
*/
// const queryModel = 'abc123'
/**
* A unique identifier for tracking visitors. For example, this could be
* implemented with an HTTP cookie, which should be able to uniquely identify
* a visitor on a single device. This unique identifier should not change if
* the visitor logs in or out of the website.
* This field should NOT have a fixed value such as `unknown_visitor`.
* This should be the same identifier as
* UserEvent.user_pseudo_id google.cloud.discoveryengine.v1.UserEvent.user_pseudo_id
* and
* SearchRequest.user_pseudo_id google.cloud.discoveryengine.v1.SearchRequest.user_pseudo_id.
* The field must be a UTF-8 encoded string with a length limit of 128
* characters. Otherwise, an `INVALID_ARGUMENT` error is returned.
*/
// const userPseudoId = 'abc123'
/**
* Indicates if tail suggestions should be returned if there are no
* suggestions that match the full query. Even if set to true, if there are
* suggestions that match the full query, those are returned and no
* tail suggestions are returned.
*/
// const includeTailSuggestions = true
// Imports the Discoveryengine library
const
{
CompletionServiceClient
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
CompletionServiceClient
();
async
function
callCompleteQuery
()
{
// Construct request
const
request
=
{
dataStore
,
query
,
};
// Run request
const
response
=
await
discoveryengineClient
.
completeQuery
(
request
);
console
.
log
(
response
);
}
callCompleteQuery
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
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in:
# https://googleapis.dev/python/google-api-core/latest/client_options.html
from
google.cloud
import
discoveryengine_v1
def
sample_complete_query
():
# Create a client
client
=
discoveryengine_v1
.
CompletionServiceClient
()
# Initialize request argument(s)
request
=
discoveryengine_v1
.
CompleteQueryRequest
(
data_store
=
"data_store_value"
,
query
=
"query_value"
,
)
# Make the request
response
=
client
.
complete_query
(
request
=
request
)
# Handle the response
print
(
response
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
require
"google/cloud/discovery_engine/v1"
##
# Snippet for the complete_query call in the CompletionService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::CompletionService::Client#complete_query.
#
def
complete_query
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
CompletionService
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
CompleteQueryRequest
.
new
# Call the complete_query method.
result
=
client
.
complete_query
request
# The returned object is of type Google::Cloud::DiscoveryEngine::V1::CompleteQueryResponse.
p
result
end
Use an autocomplete denylist
You can use a denylist to prevent specific terms from appearing as autocomplete
suggestions.
For example, take a pharmaceutical company. If a medication is no longer
FDA-approved but is mentioned in documents in their data store, they might want
to prevent that medication from appearing as a suggested query. The company
could add the name of that medication to a denylist to prevent it from being
suggested.
The following limits apply:
One denylist per data store
Uploading a denylist overwrites any existing denylist for that data store
Up to 1000 terms per denylist
Terms are case-insensitive
After importing a denylist, it takes 1-2 days to take effect
Each entry of your denylist consists of a
blockPhrase
and
matchOperator
:
blockPhrase
: Enter a string as your denylist term. Terms are
case-insensitive.
matchOperator
: Accepts the following values:
EXACT_MATCH
: Prevents an exact match of the denylist term from appearing
as a suggested query.
CONTAINS
: Prevents any suggestion that contains the denylist term from
appearing.
The following is an example of a denylist with four entries:
{
"entries"
:
[
{
"blockPhrase"
:
"Oranges"
,
"matchOperator"
:
"CONTAINS"
},
{
"blockPhrase"
:
"bAd apples"
,
"matchOperator"
:
"EXACT_MATCH"
},
{
"blockPhrase"
:
"Cool as A Cucumber"
,
"matchOperator"
:
"EXACT_MATCH"
},
{
"blockPhrase"
:
"cherry pick"
,
"matchOperator"
:
"CONTAINS"
}
]
}
Prior to importing a denylist, verify that the necessary
access controls
are set for Discovery Engine editor access.
Denylists can be imported either
from local JSON data
or
from Cloud Storage
. To remove a denylist from a data store,
purge the denylist
.
Import a denylist from local JSON data
To import a denylist from a local JSON file containing your denylist, do the following:
Create your denylist in a local JSON file with the following format. Make
sure each denylist entry is in a new line with no line breaks.
{
"inlineSource"
:
{
"entries"
:
[
{
"blockPhrase"
:
"
TERM_1
"
,
"matchOperator"
:
"
MATCH_OPERATOR_1
"
},
{
"blockPhrase"
:
"
TERM_2
"
,
"matchOperator"
:
"
MATCH_OPERATOR_2
"
}
]
}
}
Make a POST request to the
suggestionDenyListEntries:import
method, providing the name
of your JSON file.
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
"Content-Type: application/json; charset=utf-8"
\
--data
@
DENYLIST_FILE
\
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/dataStores/
DATA_STORE_ID
/suggestionDenyListEntries:import"
Replace the following:
DENYLIST_FILE
: the local path of the JSON file
containing the denylist terms.
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the data store that is
associated with your app.
After importing your denylist, it takes 1-2 days to start filtering suggestions.
Import a denylist from Cloud Storage
To import a denylist from a JSON file in Cloud Storage, do the following:
Create your denylist in a JSON file with the following format and import to
a Cloud Storage bucket. Make sure each denylist entry is in a new line
with no line breaks.
{
"blockPhrase"
:
"
TERM_1
"
,
"matchOperator"
:
"
MATCH_OPERATOR_1
"
}
{
"blockPhrase"
:
"
TERM_2
"
,
"matchOperator"
:
"
MATCH_OPERATOR_2
"
}
Create a local JSON file containing the
gcsSource
object. Use
this to point to your denylist file's location in a Cloud Storage
bucket.
{
"gcsSource"
:
{
"inputUris"
:
[
"
DENYLIST_STORAGE_LOCATION
"
]
}
}
Replace
DENYLIST_STORAGE_LOCATION
with the
location of your denylist in Cloud Storage. You can enter only one
URI. The URI must be entered in this format:
gs://
BUCKET
/
FILE_PATH
.
Make a POST request to the
suggestionDenyListEntries:import
method, including the
gcsSource
object.
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
"Content-Type: application/json; charset=utf-8"
\
--data
@
GCS_SOURCE_FILE
\
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/dataStores/
DATA_STORE_ID
/suggestionDenyListEntries:import"
Replace the following:
GCS_SOURCE_FILE
: the local path of the file containing
the
gcsSource
object that points to your denylist.
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the data store that is
associated with your app.
After importing your denylist, it takes 1-2 days to start filtering suggestions.
Purge a denylist
To purge a denylist from your data store, do the following:
Make a POST request to the
suggestionDenyListEntries:purge
method.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/dataStores/
DATA_STORE_ID
/suggestionDenyListEntries:purge"
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the data store that is
associated with your app.
Use an imported list of autocomplete suggestions
You can choose to provide your own list of autocomplete suggestions instead of
using autocomplete suggestions generated from an autocomplete data model.
For most applications, using generated suggestions from one of autocomplete data
models yields better results. However, there might be some rare situations
where the model's suggestions don't match your needs and providing a discrete
list of suggestions gives your users a better autocomplete experience.
For example, a small online bookstore imports their list of book titles as the
autocomplete suggestions. When a customer begins to type in the search bar, the
autocomplete suggestion will always be a book title from the imported list. When
the list of books changes, the bookstore purges the current list and imports the
new list. An excerpt from the list might look something like:
{
"suggestion"
:
"Wuthering Heights"
,
"globalScore"
:
"0.52"
},
{
"suggestion"
:
"The Time Machine"
,
"globalScore"
:
"0.26"
},
{
"suggestion"
:
"Nicholas Nickleby"
,
"globalScore"
:
"0.38"
},
{
"suggestion"
:
"A Little Princess"
,
"globalScore"
:
"0.71"
},
{
"suggestion"
:
"The Scarlet Letter"
,
"globalScore"
:
"0.32"
}
The
globalScore
is a floating point number in the range [0, 1] that's used
to rank the suggestion. Alternatively, you can use a
frequency
score which is
an integer greater than one. The
frequency
score is used to rank suggestions
when the
globalScore
is not available (set as null).
Set up and import autocomplete suggestions
To set up and import a list of autocomplete suggestions from a
BigQuery, follow these steps:
Create your list of suggestions and load it into a BigQuery table.
At minimum you need to provide each suggestion as a string and either a
global score or a frequency.
Use the following table schema for your list of suggestions:
[
{
"description"
:
"The suggestion text"
,
"mode"
:
"REQUIRED"
,
"name"
:
"suggestion"
,
"type"
:
"STRING"
},
{
"description"
:
"Global score of this suggestion. Control how this suggestion would be scored and ranked. Set global score or frequency; not both."
,
"mode"
:
"NULLABLE"
,
"name"
:
"globalScore"
,
"type"
:
"FLOAT"
},
{
"description"
:
"Frequency of this suggestion. Used to rank suggestions when the global score is not available."
,
"mode"
:
"NULLABLE"
,
"name"
:
"frequency"
,
"type"
:
"INTEGER"
}
]
See the
BigQuery documentation
for instructions on
how to
create a BigQuery table
and
load the
table
with your autocomplete suggestion list.
Import the list from BigQuery.
Make a POST request to the
completionSuggestions:import
method, including
the
bigquerySource
object.
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-H "X-Goog-User-Project:
PROJECT_ID
" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/dataStores/
DATA_STORE_ID
/completionSuggestions:import" \
-d '{
"bigquery_source": {"project_id": "
PROJECT_ID_SOURCE
", "dataset_id": "
DATASET_ID
", "table_id": "
TABLE_ID
"}
}'
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store.
PROJECT_ID_SOURCE
: the project that contains
the dataset that you want to import.
DATASET_ID
: the dataset ID for the suggestion
list that you want to import
TABLE_ID
: the table ID for the suggestion
list that you want to import
Example command and result
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/dataStores/my-data-store/completionSuggestions:import" \
-d '{
"bigquery_source": {"project_id": "my-project-123", "dataset_id": "autocomplete", "table_id": "import_suggestion2"}
}'
{
"name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/operations/import-completion-suggestion-7659310803143180509",
"metadata": {
"@type": "type.googleapis.com/google.cloud.discoveryengine.v1.ImportCompletionSuggestionsMetadata"
}
}
Optional: Make note of the
name
value returned, and follow the
instructions in
Get details about a long-running
operation
to see when the import operation is complete.
If you haven't enabled autocomplete for the app, follow the procedure
Update autocomplete settings
. Make sure to set
Enable autocomplete
to
Now
.
Wait a couple of days for indexing to complete and the imported suggestions
to become available.
Send an autocomplete request
To send an autocomplete request that returns an imported suggestion instead of a
suggestion from an autocomplete model:
Follow the procedure to
send an autocomplete request to a different
model
and set
AUTOCOMPLETE_MODEL
to
imported-suggestion
.
Example command and result
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store:completeQuery?query=t&query_model=imported-suggestion"
Response:
{
"querySuggestions": [
{
"suggestion": "The Time Machine"
},
{
"suggestion": "The Scarlet Letter"
}
]
}
Purge the list of imported autocomplete suggestions
Before importing a new list of autocomplete suggestions, remove the existing
one.
To purge an existing list of autocomplete suggestions, follow this step:
Make a POST request to the
completionSuggestions:purge
method.
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/dataStores/
DATA_STORE_ID
/completionSuggestions:purge"
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the data store that is
associated with your app.
Example command and result
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/dataStores/my-data-store/completionSuggestions:purge"
{
"name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/operations/purge-customer-imported_suggestions-3197526711414652502",
"metadata": {
"@type": "type.googleapis.com/google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsMetadata",
"createTime": "2024-06-27T17:07:09.551726728Z",
"updateTime": "2024-06-27T17:07:09.551726728Z"
},
"done": true,
"response": {
"@type": "type.googleapis.com/google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsResponse",
"purgeSucceeded": true
}
}
Advanced document data model
AI Applications provides an advanced data model for autocomplete. Based on
the documents you import, this data model generates high-quality autocomplete
suggestions by leveraging Google large language models (LLMs).
This feature is experimental. If you're interested in using this feature,
contact your Google Cloud account team and ask to be added to the allowlist.
The advanced document data model is not available for healthcare search or in
the US and EU multi-regions.
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
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID:completeQuery?query=QUERY_STRING"

```

### Code Example 2 (text)

```text
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID:completeQuery?query=QUERY_STRING&query_model=QUERY_SUGGESTIONS_MODEL"

```

### Code Example 3 (text)

```text
using Google.Cloud.DiscoveryEngine.V1;

public sealed partial class GeneratedCompletionServiceClientSnippets
{
    /// <summary>Snippet for CompleteQuery</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void CompleteQueryRequestObject()
    {
        // Create client
        CompletionServiceClient completionServiceClient = CompletionServiceClient.Create();
        // Initialize request argument(s)
        CompleteQueryRequest request = new CompleteQueryRequest
        {
            DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
            Query = "",
            QueryModel = "",
            UserPseudoId = "",
            IncludeTailSuggestions = false,
        };
        // Make the request
        CompleteQueryResponse response = completionServiceClient.CompleteQuery(request);
    }
}
```

### Code Example 4 (text)

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
	c, err := discoveryengine.NewCompletionClient(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &discoveryenginepb.CompleteQueryRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CompleteQueryRequest.
	}
	resp, err := c.CompleteQuery(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}

```

### Code Example 5 (text)

```text
import com.google.cloud.discoveryengine.v1.CompleteQueryRequest;
import com.google.cloud.discoveryengine.v1.CompleteQueryResponse;
import com.google.cloud.discoveryengine.v1.CompletionServiceClient;
import com.google.cloud.discoveryengine.v1.DataStoreName;

public class SyncCompleteQuery {

  public static void main(String[] args) throws Exception {
    syncCompleteQuery();
  }

  public static void syncCompleteQuery() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (CompletionServiceClient completionServiceClient = CompletionServiceClient.create()) {
      CompleteQueryRequest request =
          CompleteQueryRequest.newBuilder()
              .setDataStore(
                  DataStoreName.ofProjectLocationDataStoreName(
                          "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                      .toString())
              .setQuery("query107944136")
              .setQueryModel("queryModel-184930495")
              .setUserPseudoId("userPseudoId-1155274652")
              .setIncludeTailSuggestions(true)
              .build();
      CompleteQueryResponse response = completionServiceClient.completeQuery(request);
    }
  }
}
```

### Code Example 6 (text)

```text
/**
 * This snippet has been automatically generated and should be regarded as a code template only.
 * It will require modifications to work.
 * It may require correct/in-range values for request initialization.
 * TODO(developer): Uncomment these variables before running the sample.
 */
/**
 *  Required. The parent data store resource name for which the completion is
 *  performed, such as
 *  `projects/* /locations/global/collections/default_collection/dataStores/default_data_store`.
 */
// const dataStore = 'abc123'
/**
 *  Required. The typeahead input used to fetch suggestions. Maximum length is
 *  128 characters.
 */
// const query = 'abc123'
/**
 *  Specifies the autocomplete data model. This overrides any model specified
 *  in the Configuration > Autocomplete section of the Cloud console. Currently
 *  supported values:
 *  * `document` - Using suggestions generated from user-imported documents.
 *  * `search-history` - Using suggestions generated from the past history of
 *  SearchService.Search google.cloud.discoveryengine.v1.SearchService.Search 
 *  API calls. Do not use it when there is no traffic for Search API.
 *  * `user-event` - Using suggestions generated from user-imported search
 *  events.
 *  * `document-completable` - Using suggestions taken directly from
 *  user-imported document fields marked as completable.
 *  Default values:
 *  * `document` is the default model for regular dataStores.
 *  * `search-history` is the default model for site search dataStores.
 */
// const queryModel = 'abc123'
/**
 *  A unique identifier for tracking visitors. For example, this could be
 *  implemented with an HTTP cookie, which should be able to uniquely identify
 *  a visitor on a single device. This unique identifier should not change if
 *  the visitor logs in or out of the website.
 *  This field should NOT have a fixed value such as `unknown_visitor`.
 *  This should be the same identifier as
 *  UserEvent.user_pseudo_id google.cloud.discoveryengine.v1.UserEvent.user_pseudo_id 
 *  and
 *  SearchRequest.user_pseudo_id google.cloud.discoveryengine.v1.SearchRequest.user_pseudo_id.
 *  The field must be a UTF-8 encoded string with a length limit of 128
 *  characters. Otherwise, an `INVALID_ARGUMENT` error is returned.
 */
// const userPseudoId = 'abc123'
/**
 *  Indicates if tail suggestions should be returned if there are no
 *  suggestions that match the full query. Even if set to true, if there are
 *  suggestions that match the full query, those are returned and no
 *  tail suggestions are returned.
 */
// const includeTailSuggestions = true

// Imports the Discoveryengine library
const {CompletionServiceClient} = require('@google-cloud/discoveryengine').v1;

// Instantiates a client
const discoveryengineClient = new CompletionServiceClient();

async function callCompleteQuery() {
  // Construct request
  const request = {
    dataStore,
    query,
  };

  // Run request
  const response = await discoveryengineClient.completeQuery(request);
  console.log(response);
}

callCompleteQuery();
```

### Code Example 7 (text)

```text
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import discoveryengine_v1


def sample_complete_query():
    # Create a client
    client = discoveryengine_v1.CompletionServiceClient()

    # Initialize request argument(s)
    request = discoveryengine_v1.CompleteQueryRequest(
        data_store="data_store_value",
        query="query_value",
    )

    # Make the request
    response = client.complete_query(request=request)

    # Handle the response
    print(response)

```

### Code Example 8 (text)

```text
require "google/cloud/discovery_engine/v1"

##
# Snippet for the complete_query call in the CompletionService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::CompletionService::Client#complete_query.
#
def complete_query
  # Create a client object. The client can be reused for multiple calls.
  client = Google::Cloud::DiscoveryEngine::V1::CompletionService::Client.new

  # Create a request. To set request fields, pass in keyword arguments.
  request = Google::Cloud::DiscoveryEngine::V1::CompleteQueryRequest.new

  # Call the complete_query method.
  result = client.complete_query request

  # The returned object is of type Google::Cloud::DiscoveryEngine::V1::CompleteQueryResponse.
  p result
end
```

### Code Example 9 (text)

```text
curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    --data @DENYLIST_FILE \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataStores/DATA_STORE_ID/suggestionDenyListEntries:import"

```

### Code Example 10 (text)

```text
curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    --data @GCS_SOURCE_FILE \
   "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataStores/DATA_STORE_ID/suggestionDenyListEntries:import"

```

### Code Example 11 (text)

```text
curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataStores/DATA_STORE_ID/suggestionDenyListEntries:purge"

```

### Code Example 12 (text)

```text
{"suggestion": "Wuthering Heights", "globalScore": "0.52" },
{"suggestion": "The Time Machine", "globalScore": "0.26" },
{"suggestion": "Nicholas Nickleby", "globalScore": "0.38" },
{"suggestion": "A Little Princess", "globalScore": "0.71" },
{"suggestion": "The Scarlet Letter", "globalScore": "0.32" }

```

### Code Example 13 (text)

```text
[
  {
    "description": "The suggestion text",
    "mode": "REQUIRED",
    "name": "suggestion",
    "type": "STRING"
  },
  {
    "description": "Global score of this suggestion. Control how this suggestion would be scored and ranked. Set global score or frequency; not both.",
    "mode": "NULLABLE",
    "name": "globalScore",
    "type": "FLOAT"
  },
  {
    "description": "Frequency of this suggestion. Used to rank suggestions when the global score is not available.",
    "mode": "NULLABLE",
    "name": "frequency",
    "type": "INTEGER"
  }
]

```

### Code Example 14 (text)

```text
curl -X POST \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json; charset=utf-8" \
 -H "X-Goog-User-Project: PROJECT_ID" \
 "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataStores/DATA_STORE_ID/completionSuggestions:import" \
 -d '{
      "bigquery_source": {"project_id": "PROJECT_ID_SOURCE", "dataset_id": "DATASET_ID", "table_id": "TABLE_ID"}
 }'

```

### Code Example 15 (text)

```text
curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataStores/DATA_STORE_ID/completionSuggestions:purge"

```

