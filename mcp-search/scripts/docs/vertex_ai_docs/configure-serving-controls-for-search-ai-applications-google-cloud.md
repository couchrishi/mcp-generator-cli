# Configure serving controls for search  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls](https://cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls)

Home
AI Applications
Documentation
Guides
Send feedback
Configure serving controls for search
Stay organized with collections
Save and categorize content based on your preferences.
Serving controls (also called controls) change the default
behavior of how a request is served when results are returned. Serving controls
act at a data-store level.
For example, controls can boost and bury results, filter entries from returned
results, associate strings with each other as synonyms, or redirect results to
specified URIs.
This page describes serving controls for search apps. For information about
using serving controls with media recommendations, see
Create and manage media
serving configs
.
About serving controls
To change the results of a request, first create a serving control. Then, attach
that control to the
serving config
of a search app. A
serving config
configures
metadata that's used to generate serving time results, such as search results or
answers. A serving control only affects requests served by the app if the
control is attached to the app's serving config.
Some controls, such as boost controls, have dependencies on data stores. If a
data store is removed from an app, then any data store-dependent controls are
also removed from that app and become inactive, but are not deleted.
Serving control types
The following types of serving controls are available:
Control
Description
Available for
Boost control
Changes the returned order of results
Search apps with data stores that support a schema, such as data stores that contain structured data, websites with structured data (advanced website indexing), unstructured data with metadata, or media data
Filter control
Removes entries from returned results
Search apps with data stores that support a schema, such as data stores that contain structured data, websites (advanced website indexing), unstructured data with metadata, or media data
Synonyms control
Associates queries with each other
Search apps with website (advanced website indexing), structured, unstructured, or media data stores
Redirect control
Redirects to a specified URI
All search apps
Promote control
Promotes a specified link for a query
Only basic website search apps
About conditions
When creating a control, you can optionally define a condition that determines
when the control is applied. Conditions are defined using condition fields. The
following condition fields are available:
queryTerms
. An optional control that's applied when specific queries are
searched for. When the
queryTerms
condition is used, the control
is applied when the value of
queryTerms
matches a term in
SearchRequest.query
. Query terms can only be used when the
Control.searchUseCase
is set as
SOLUTION_TYPE_SEARCH
. Up to 10 different
queryTerms
can be specified on a single
Control.condition
. If no query
terms are specified, the
queryTerms
field is ignored.
For a promote serving control, these additional constraints are applicable:
queryTerms
condition cannot be specified if you're specifying the
queryRegex
condition
fullMatch
must be set to
true
activeTimeRange
. An optional control that's applied when a request
occurs within a specified time range. It checks that the time a request was
received is between
activeTimeRange.startTime
and
activeTimeRange.endTime
.
Up to 10
activeTimeRange
ranges can be specified on a single
Control.condition
. If the
activeTimeRange
field isn't specified, the field
is ignored.
queryRegex
. Only available for a
promote serving control
,
an optional condition that applies the control when the
query matches the specified regular expression. This condition cannot be
specified if you're specifying the
queryTerms
condition.
If multiple conditions are specified for a control, the control is applied
to the search request when both condition types are satisfied. If multiple
values for the same condition are specified, only one of the values needs to
match for that condition to be satisfied.
For example, consider the following condition with two query terms specified:
"queryTerms"
:
[
{
"value"
:
"gShoe"
,
"fullMatch"
:
true
},
{
"value"
:
"gBoot"
,
"fullMatch"
:
true
}
]
The condition will be satisfied for a request with
SearchRequest.query="gShoe"
or a request with
SearchRequest.query="gBoot"
,
but won't be satisfied with
SearchRequest.query="gSandal"
or any other
string.
If no conditions are specified, the control is always applied.
For more information, see the
Condition
field in the API
reference.
Create and attach boost serving controls
A boost serving control is defined as a control with a
boostAction
.
Use the following instructions to create a boost serving control.
For field details, see the
engines.controls
API reference
and the
engines.controls.create
API reference
.
Find your app ID. If you already have your app ID, skip to the next step.
In the Google Cloud console, go to the
AI Applications
page.
Go to Apps
On the
Apps
page, find the name of your app and get the app's ID from
the
ID
column.
Run the following curl commands to create your controls.
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
/locations/global/collections/default_collection/engines/
APP_ID
/controls?controlId=
CONTROL_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"solutionType": "SOLUTION_TYPE_SEARCH",
"useCases": [
"
USE_CASE
"
],
"conditions": {
"queryTerms": [
{
"value": "
VALUE
",
"fullMatch":
FULL_MATCH
}
],
"activeTimeRange": [
{
"startTime": "
START_TIMESTAMP
",
"endTime": "
END_TIMESTAMP
"
}
]
},
"boostAction": {
"boost":
BOOST_VALUE
,
"filter": "
FILTER
",
"dataStore": "
DATA_STORE_RESOURCE_PATH
"
}
}'
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
CONTROL_ID
: a unique identifier for the control.
The ID can contain [1-63] characters that can be letters, digits, hyphens,
and underscores.
DISPLAY_NAME
: the human-readable name for the control.
Google recommends that this name provide an indication of when or why to
use the control. Must be a UTF-8 encoded string with length [1,128].
USE_CASE
: must be either
SEARCH_USE_CASE_SEARCH
or
SEARCH_USE_CASE_BROWSE
. If
SEARCH_USE_CASE_BROWSE
is specified,
then
Condition.queryTerms
can't be used in the condition.
CONDITION
: an optional field that defines when the
control should be applied. Contains the following fields:
VALUE
: the specific query value to match
against. It's a lowercase UTF-8 string with length
[1, 5000]
. If
FULL_MATCH_1
is
true
, this field can have at
most three space-separated terms.
FULL_MATCH
: a boolean that indicates whether
the search query needs to exactly match the query term. When set to
true
, it requires
SearchRequest.query
to completely match the
queryTerm.value
. When set to
false
, it requires
SearchRequest.query
to contain
queryTerm.value
as a substring.
START_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the start of a time range.
END_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the end of a time range.
BOOST_VALUE
:
a floating point number in the range [-1,1]. When the value is
negative, results are demoted (they appear lower down in the
results). When the value is positive, results are promoted
(they appear higher up in the results).
For more information, see
boostAction
.
FILTER
: a string specifying requirements that must
be met by the document. If the document matches all the requirements, the
boost is applied. Otherwise there is no change. If this field is empty, then
the boost is applied to all documents in the data store. For the filtering
syntax, see
Filter expression syntax
.
Note: The document field
title
can't be filtered.
DATA_STORE_RESOURCE_PATH
: the full resource path of
the data store whose documents should be boosted by this control. The
format of the full resource path is
projects/
PROJECT_NUMBER
/locations/
LOCATION_ID
/collections/default_collection/dataStores/
DATA_STORE_ID
.
This data store must be attached to the engine specified in the request.
Attach the control to the app's serving config using the
engines.servingConfigs.patch
method.
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
-H
"X-Goog-User-Project:
PROJECT_ID
"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search?update_mask=boost_control_ids"
\
-d
'{
"boostControlIds": ["
BOOST_ID_1
", "
BOOST_ID_2
"]
}'
Replace
BOOST_ID_N
with the control IDs that you
created in the previous step.
Create and attach filter serving controls
A filter serving control is defined as a control with a
filterAction
.
Use the following instructions to create a filter serving control.
For field details, see the
engines.controls
API reference
and the
engines.controls.create
API reference
.
Find your app ID. If you already have your app ID, skip to the next step.
In the Google Cloud console, go to the
AI Applications
page.
Go to Apps
On the
Apps
page, find the name of your app and get the app's ID from
the
ID
column.
Run the following curl commands to create your controls.
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
/locations/global/collections/default_collection/engines/
APP_ID
/controls?controlId=
CONTROL_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"solutionType": "SOLUTION_TYPE_SEARCH",
"useCases": ["
USE_CASE
"],
"conditions": {
"queryTerms": [
{
"value": "
VALUE
",
"fullMatch":
FULL_MATCH
}
],
"activeTimeRange": [
{
"startTime": "
START_TIMESTAMP
",
"endTime": "
END_TIMESTAMP
"
}
]
},
"filterAction": {
"filter": "
FILTER
"
}
}'
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
CONTROL_ID
: a unique identifier for the control.
The ID can contain [1-63] characters that can be letters, digits, hyphens,
and underscores.
DISPLAY_NAME
: the human-readable name for the control.
Google recommends that this name provide an indication of when or why to
use the control. Must be a UTF-8 encoded string with length [1,128].
USE_CASE
: must be either
SEARCH_USE_CASE_SEARCH
or
SEARCH_USE_CASE_BROWSE
. If
SEARCH_USE_CASE_BROWSE
is specified,
then
Condition.queryTerms
can't be used in the condition.
CONDITION
: an optional field that defines when the
control should be applied. Contains the following fields:
VALUE
: the specific query value to match
against. It's a lowercase UTF-8 string with length
[1, 5000]
. If
FULL_MATCH_1
is
true
, this field can have at
most three space-separated terms.
FULL_MATCH
: a boolean that indicates whether
the search query needs to exactly match the query term. When set to
true
, it requires
SearchRequest.query
to completely match the
queryTerm.value
. When set to
false
, it requires
SearchRequest.query
to contain
queryTerm.value
as a substring.
START_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the start of a time range.
END_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the end of a time range.
FILTER
: a string specifying requirements that must
be met by the document. If the document matches all the requirements, the
document is returned in the results. Otherwise the document is not in the
results.
For the filtering syntax, see
Filter expression syntax
.
For more information, see
filterAction
.
Note: The document field
title
can't be filtered.
Attach the control to the app's serving config using the
engines.servingConfigs.patch
method.
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
-H
"X-Goog-User-Project:
PROJECT_ID
"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search?update_mask=filter_control_ids"
\
-d
'{
"filterControlIds": ["
FILTER_ID_1
", "
FILTER_ID_2
"]
}'
Replace
FILTER_ID_N
with the control IDs that you
created in the previous step.
Create and attach synonyms serving controls
A synonyms serving control is defined as a control with a
synonymsAction
.
Use the following instructions to create a synonyms serving control.
For field details, see the
engines.controls
API reference
and the
engines.controls.create
API reference
.
Find your app ID. If you already have your app ID, skip to the next step.
In the Google Cloud console, go to the
AI Applications
page.
Go to Apps
On the
Apps
page, find the name of your app and get the app's ID from
the
ID
column.
Run the following curl commands to create your controls.
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
/locations/global/collections/default_collection/engines/
APP_ID
/controls?controlId=
CONTROL_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"solutionType": "SOLUTION_TYPE_SEARCH",
"useCases": ["
USE_CASE
"],
"conditions": {
"queryTerms": [
{
"value": "
VALUE
",
"fullMatch":
FULL_MATCH
}
],
"activeTimeRange": [
{
"startTime": "
START_TIMESTAMP
",
"endTime": "
END_TIMESTAMP
"
}
]
},
"synonymsAction": {
"synonyms": ["
SYNONYMS_1
","
SYNONYMS_2
"]
}
}'
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
CONTROL_ID
: a unique identifier for the control.
The ID can contain [1-63] characters that can be letters, digits, hyphens,
and underscores.
DISPLAY_NAME
: the human-readable name for the control.
Google recommends that this name provide an indication of when or why to
use the control. Must be a UTF-8 encoded string with length [1,128].
USE_CASE
: must be either
SEARCH_USE_CASE_SEARCH
or
SEARCH_USE_CASE_BROWSE
. If
SEARCH_USE_CASE_BROWSE
is specified,
then
Condition.queryTerms
can't be used in the condition.
CONDITION
: an optional field that defines when the
control should be applied. Contains the following fields:
VALUE
: the specific query value to match
against. It's a lowercase UTF-8 string with length
[1, 5000]
. If
FULL_MATCH_1
is
true
, this field can have at
most three space-separated terms.
FULL_MATCH
: a boolean that indicates whether
the search query needs to exactly match the query term. When set to
true
, it requires
SearchRequest.query
to completely match the
queryTerm.value
. When set to
false
, it requires
SearchRequest.query
to contain
queryTerm.value
as a substring.
START_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the start of a time range.
END_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the end of a time range.
SYNONYMS_N
: a list of strings that are associated
with each other, making it more likely for each to show similar results.
While it's more likely that you get similar results, when you
search for each of the synonym entries, you might not receive all the
relevant results for all the associated synonyms.
You must specify at least two synonyms and you can specify up to 100
synonyms. Each synonym must be UTF-8 encoded and in lowercase. No duplicate
strings are allowed. For example, you can add "pixel", "android phone", and
"google phone" as synonyms.
For more information, see
synonymsAction
.
Attach the control to the app's serving config using the
engines.servingConfigs.patch
method.
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
-H
"X-Goog-User-Project:
PROJECT_ID
"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search?update_mask=synonyms_control_ids"
\
-d
'{
"synonymsControlIds": ["
SYNONYMS_ID_1
", "
SYNONYMS_ID_2
"]
}'
Replace
SYNONYMS_ID_N
with the control IDs that you
created in the previous step.
Create and attach redirect serving controls
A redirect serving control allows redirecting users to a provided URI.
Redirect controls are defined as a control with a
redirectAction
.
Use the following instructions to create a redirect serving control.
For field details, see the
engines.controls
API reference
and the
engines.controls.create
API reference
.
Find your app ID. If you already have your app ID, skip to the next step.
In the Google Cloud console, go to the
AI Applications
page.
Go to Apps
On the
Apps
page, find the name of your app and get the app's ID from
the
ID
column.
Run the following curl commands to create your controls.
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
/locations/global/collections/default_collection/engines/
APP_ID
/controls?controlId=
CONTROL_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"solutionType": "SOLUTION_TYPE_SEARCH",
"useCases": ["
USE_CASE
"],
"conditions": {
"queryTerms": [
{
"value": "
VALUE
",
"fullMatch":
FULL_MATCH
}
],
"activeTimeRange": [
{
"startTime": "
START_TIMESTAMP
",
"endTime": "
END_TIMESTAMP
"
}
]
},
"redirectAction": {
"redirectURI": "
REDIRECT_URI
"
}
}'
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
CONTROL_ID
: a unique identifier for the control.
The ID can contain [1-63] characters that can be letters, digits, hyphens,
and underscores.
DISPLAY_NAME
: the human-readable name for the control.
Google recommends that this name provide an indication of when or why to
use the control. Must be a UTF-8 encoded string with length [1,128].
USE_CASE
: must be either
SEARCH_USE_CASE_SEARCH
or
SEARCH_USE_CASE_BROWSE
. If
SEARCH_USE_CASE_BROWSE
is specified,
then
Condition.queryTerms
can't be used in the condition.
CONDITION
: an optional field that defines when the
control should be applied. Contains the following fields:
VALUE
: the specific query value to match
against. It's a lowercase UTF-8 string with length
[1, 5000]
. If
FULL_MATCH_1
is
true
, this field can have at
most three space-separated terms.
FULL_MATCH
: a boolean that indicates whether
the search query needs to exactly match the query term. When set to
true
, it requires
SearchRequest.query
to completely match the
queryTerm.value
. When set to
false
, it requires
SearchRequest.query
to contain
queryTerm.value
as a substring.
START_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the start of a time range.
END_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the end of a time range.
REDIRECT_URI_N
: a URI where you are redirected. Can
have a maximum length of 2000 characters. For example, if the value of the
query term is "support", you can set a redirect to your technical support
page instead of returning (or failing to return) search results for
"support". In this example, the redirect URI becomes
"https://www.example.com/support"
.
For more information, see
redirectAction
.
Attach the control to the app's serving config using the
engines.servingConfigs.patch
method.
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
-H
"X-Goog-User-Project:
PROJECT_ID
"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search?update_mask=redirect_control_ids"
\
-d
'{
"redirectControlIds": ["
REDIRECT_ID_1
", "
REDIRECT_ID_2
"]
}'
Replace
REDIRECT_ID_N
with the control IDs that you
created in the previous step.
Create and attach promote serving controls
A promote serving control lets you display a link as a promoted result.
This control is available only for website data stores with
basic website search.
Unlike other serving controls, you don't need to attach a promote control to the
serving config of the app. Creating and enabling a promote control for an app
activates the promote control. Additionally, unlike other serving controls, you
can turn a promotion control on or off by enabling or disabling it.
Promote controls are defined using a
promoteAction
.
To successfully create a promote control, one of the following fields is
required in the creation request:
The
queryTerms
field with
fullMatch
set to
true
The
queryRegex
field
Use the following instructions to create a promote serving control.
For field details, see the
engines.controls
API reference
and the
engines.controls.create
API reference
.
Find your app ID. If you already have your app ID, skip to the next step.
In the Google Cloud console, go to the
AI Applications
page.
Go to Apps
On the
Apps
page, find the name of your app and get the app's ID from
the
ID
column.
Run the following curl commands to create your controls.
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
/locations/global/collections/default_collection/engines/
APP_ID
/controls?controlId=
CONTROL_ID
"
\
-d
'{
"displayName": "
DISPLAY_NAME
",
"solutionType": "SOLUTION_TYPE_SEARCH",
"useCases": ["
USE_CASE
"],
"conditions": {
"queryTerms": [
{
"value": "
VALUE
",
"fullMatch": true
}
],
"activeTimeRange": [
{
"startTime": "
START_TIMESTAMP
",
"endTime": "
END_TIMESTAMP
"
}
],
"queryRegex": "
VALUE_REGEX
"
},
"promoteAction": {
"dataStore": "
DATA_STORE_RESOURCE_PATH
",
"searchLinkPromotion": {
"title": "
URI_TITLE
",
"uri": "
URI
",
"description": "
URI_DESCRIPTION
",
"enabled":
ENABLED_TRUE|FALSE
,
}
}
}'
Replace the following:
PROJECT_ID
: the number or ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
CONTROL_ID
: a unique identifier for the control.
The ID can contain [1-63] characters that can be letters, digits, hyphens,
and underscores.
DISPLAY_NAME
: the human-readable name for the control.
Google recommends that this name provide an indication of when or why to
use the control. Must be a UTF-8 encoded string with length [1,128].
USE_CASE
: must be either
SEARCH_USE_CASE_SEARCH
or
SEARCH_USE_CASE_BROWSE
. If
SEARCH_USE_CASE_BROWSE
is specified,
then
Condition.queryTerms
can't be used in the condition.
Condition
: an optional object that defines when the
control should be applied. Contains the following fields:
queryTerms
: Cannot be used with the
queryRegex
field.
VALUE
: the specific query value to match
against. It's a lowercase UTF-8 string with length
[1, 5000]
.
activeTimeRange
:
START_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the start of a time range.
END_TIMESTAMP
: a timestamp in RFC 3339 UTC
"Zulu" format to indicate the end of a time range.
queryRegex
: Cannot be used with the
queryTerms
field.
VALUE_REGEX
: a regular expression to match
the query against. This is only available for the promote serving
control.
DATA_STORE_RESOURCE_PATH
: the full resource path of
the data store whose search results contain the promoted URL. The
format of the full resource path is
projects/
PROJECT_NUMBER
/locations/
LOCATION_ID
/collections/default_collection/dataStores/
DATA_STORE_ID
.
This data store must be attached to the engine specified in the request.
URI_TITLE
: a required field to specify the title
of the URI, which is displayed in the search result.
URI
: a required field to specify the URI link where
the search result leads the user. This URI need not be included in the
data store.
URI_DESCRIPTION
: an optional field to describe the
URI, which is displayed in the search result.
ENABLED_TRUE|FALSE
: an optional boolean field to
indicate whether the promote control is turned on and attached to the app.
When you set this field to
false
, the promote serving control is turned
off and for the control to take effect, you must update the control by
enabling it, as explained in the next step.
For more information, see
promoteAction
.
Response
You should receive a JSON response similar to the following:
{
"name": "projects/
PROJECT_NUMBER
/locations/global/collections/default_collection/engines/
APP_ID
/controls/
PROMOTE_CONTROL_ID
",
"displayName": "
PROMOTE_CONTROL_NAME
",
"solutionType": "SOLUTION_TYPE_SEARCH",
"conditions": [
{
"queryTerms": [
{
"value": "
VALUE
",
"fullMatch": true
}
]
}
],
"useCases": [
"SEARCH_USE_CASE_SEARCH"
],
"promoteAction": {
"dataStore": "projects/
PROJECT_NUMBER
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
",
"searchLinkPromotion": {
"title": "
URI_TITLE
",
"uri": "
URI
",
"description": "
URI_DESCRIPTION
",
"enabled":
ENABLED_TRUE|FALSE
}
}
}
Optional: To turn a promote control on or off after the control is created,
call the
engines.control.patch
method.
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
-H
"X-Goog-User-Project:
PROJECT_ID
"
\
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/controls/
CONTROL_ID
?updateMask=promoteAction.searchLinkPromotion.enabled"
\
-d
'{
"promoteAction": {
"searchLinkPromotion": {
"enabled":
ENABLED_TRUE|FALSE
,
}
}
}'
Example
When you send a search request to the app with a query that matches the query
or query regular expression specified for the promote control, the promoted link appears in
the response.
For example, suppose that you create a promote control with the following
configuration:
{
"conditions": [
{
"queryTerms": [
{
"value": "artificial intelligence",
"fullMatch": true
}
]
}
]"
...
promoteAction": {
"dataStore": "https://discoveryengine.googleapis.com/v1alpha/projects/123456/locations/us/collections/default_collection/dataStores/basic-website-data-store" \
"searchLinkPromotion": {
"title": "What is AI?",
"uri": "https://cloud.google.com/learn/what-is-artificial-intelligence",
"description": "Explain what is AI"
"enabled": true
}
}
}
Then, you send the following
search
request:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/123456/locations/us/collections/default_collection/engines/basic-website-app/servingConfigs/default_search:search" \
-d '{
"query": "artificial intelligence"
}'
You should receive a JSON response similar to the following truncated response.
The response contains the
searchLinkPromotions
field that contains the
promoted link.
{
"results": [...],
"totalSize": 3,
"attributionToken": "_gHw_QoMCMSbhboGELuI1qwCEiQ2NzQwYmYzYi0wMDAwLTJmYTctYTk1OC0yNDA1ODg4MzZmYjgiB0dFTkVSSUMqvAGrxIotzua1L5neqC_n7YgtxPzLMIOymiK0kq4wxPi8MPn2sy3LmrQw6d3EMNSynRWc1rctnN3YMOuCsS3ogrEto4CXIsLwnhX89rMtkKS0MJbeqC-jibMtkPeyMMTGsTCZ3dgw5O2ILa7Eii2NpLQw5t3EMN6PmiKOvp0VwfzLMICymiKq-LMt0ea1L634sy3Fy_MXtreMLbeSrjDHxrEwzpq0MMH4vDCgibMtn9a3LZSSxTCOkckw24-aIjAB",
"guidedSearchResult": {},
"summary": {},
"searchLinkPromotions": [
{
"title": "What is AI?",
"uri": "https://cloud.google.com/learn/what-is-artificial-intelligence",
"description": "Explain what is AI"
}
]
}
What's next
To understand the impact of a serving control on the search quality of a
generic search app, evaluate the search quality. For more information, see
Evaluate search quality
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
"queryTerms": [
  {
    "value": "gShoe",
    "fullMatch": true
  },
  {
    "value": "gBoot",
    "fullMatch": true
  }
]

```

