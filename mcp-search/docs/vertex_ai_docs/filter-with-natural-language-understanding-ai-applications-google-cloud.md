# Filter with natural-language understanding  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/natural-language-queries](https://cloud.google.com/generative-ai-app-builder/docs/natural-language-queries)

Home
AI Applications
Documentation
Guides
Send feedback
Filter with natural-language understanding
Stay organized with collections
Save and categorize content based on your preferences.
This page explains how to apply natural-language understanding to automatically
make filters for search queries and, therefore, to improve the quality of the
results returned.
You can use this feature with search apps that are connected to structured data
stores.
About natural-language query understanding
If you have a generic search app with structured data,
your users' natural-language queries can be reformatted as filtered
queries. This can lead to better quality search results than searching for words
in the query string.
Using natural-language query understanding is easier and more flexible than writing your own filter
expressions. For information about writing filter expressions, see
Filter generic search for structured or unstructured data
.
This feature is best explained through examples:
Example: Field extraction from queries
shows the field filters
extracted from the query.
Example: With a geolocation filter
includes the special case of the
geolocation filter.
Example: Field extraction from queries
This natural-language query understanding feature is explained through the example of searching for a
hotel.
Take the following query made to a structured data store for a hotel site:
"Find me a family-friendly hotel with at least four stars that costs less
than 300 a night, lets me bring my dog, and has free Wi-Fi."
Without natural-language query understanding, the search app looks for documents that contain the words
in the query.
With natural-language query understanding and appropriately structured data, the search is made more
effective by replacing some of the natural language in the query with filters.
If the structured data has fields for
star_rating
(numbers),
price
(numbers), and
amenities
(strings), then the query can be rewritten as the
following filters plus a residual query:
Filters extracted from the natural-language query:
{
"star_rating": &ge;4,
"price": &le;300,
"amenities": "Wifi", "Pets Allowed"
}
Residual query, reformulated after filters are extracted:
family-friendly
Example: With a geolocation filter
This example is similar to the preceding one except that it includes a
geolocation
filter, which is special kind of extracted filter.
Vertex AI Search has the ability to recognize locations in a query and
create proximity filters for the locations.
Take the following query made to a state-wide business site:
"Find me a chic and stylish hotel with at least 4 stars that is in San
Francisco."
With natural-language query understanding and the geolocation filter, the search is reformulated as
filters and a residual query:
Filters extracted from the natural-language query, for at least a 4-star
rating and within a 10 km radius of San Francisco:
{
"star_rating": &ge;4,
"location": GEO_DISTANCE(\"San Francisco, CA\", 10000)
}
In this example, the
GEO_DISTANCE
is an address, but in other queries, it
might be written as a latitude and longitude, even though the original query
contained an address.
Residual query, reformulated after filters are extracted:
chic and stylish in San Francisco
Although the geolocation filter is made, the place name remains in the
residual query. This is different from the other filters, such as the
star_rating
.
Limitations
The following limitations apply to natural-language query understanding:
Natural-language query understanding can't be applied to
blended search apps
. You
get an error if you try to use natural-language query understanding with a blended search app.
Natural-language query understanding works only for generic search apps that use structured data
stores.
Using natural-language query understanding increases latency, so you might choose not to use it
if latency is a problem.
For geolocation, the location must be explicitly described. You
can't use locations such as "near me" or "home".
The radius for geolocation is 10 km and isn't configurable.
Before you begin
Before you start using natural-language query understanding, you have to enable it for the structured
data stores connected to the apps that you plan to use.
To enable natural-language query understanding, follow these steps:
REST
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
Run the following curl command:
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
?update_mask=natural_language_query_understanding_config.mode"
\
-d
'{
"naturalLanguageQueryUnderstandingConfig": {
"mode": "ENABLED"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the Vertex AI Search data store.
Example command and response
curl -X PATCH
-H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
-H "X-Goog-User-Project: my-project-123"
"https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store?update_mask=natural_language_query_understanding_config.mode"
-d '{
"naturalLanguageQueryUnderstandingConfig": {
"mode": "ENABLED"
}
}'
{
"name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store",
"displayName": "test_data_store",
"industryVertical": "GENERIC",
"createTime": "2024-07-10T18:50:01.673414Z",
"solutionTypes": [
"SOLUTION_TYPE_SEARCH"
],
"defaultSchemaId": "default_schema",
"documentProcessingConfig": {
"name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/documentProcessingConfig",
"defaultParsingConfig": {
"digitalParsingConfig": {}
}
},
"servingConfigDataStore": {},
"naturalLanguageQueryUnderstandingConfig": {
"mode": "ENABLED"
}
}
Repeat steps 1 and 2 for each data store.
Wait approximately 24 hours.
If you try to use natural-language query understanding before the data store is ready, the response
you get is the same as if
filterExtractionCondition
was set to
DISABLED
.
Search, converting natural-language queries into filters
To search on a query in natural language and get results that are optimized for
natural-language queries, do the following:
REST
Run the following curl command, which calls the
search
method:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:search" \
-d '{
"query": "
QUERY
",
"naturalLanguageQueryUnderstandingSpec": {
"filterExtractionCondition": "ENABLED"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query. The app must be
connected to a data store that contains structured data. The app can't be
a blended search app.
QUERY
: the query is in written in a natural
language.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1beta/projects/123456
/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search"
-d '{
"query": "Find me a family-friendly hotel with at least four stars that costs less than 300 a night, lets me bring my dog, and has free Wi-Fi.",
"naturalLanguageQueryUnderstandingSpec": {
"filterExtractionCondition": "ENABLED"}
}'
{
"results": [
{
"id": "b2617d862",
"document": {
"name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/b2617d862",
...
}
},
{
"id": "a51841841",
"document": {
"name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/a51841841",
...
}
}
],
"naturalLanguageQueryUnderstandingInfo": {
"extractedFilters": "(amenities: ANY(\"Pets Allowed\") AND amenities: ANY(\"Wifi\") AND star_rating: >= 4 AND price: < 300)",
"rewrittenQuery": "family-friendly",
"extractedFilterStructured": {
"expression": {
"andExpr": {
"expressions": [
{
"numberConstraint": {
"fieldName": "star_rating",
"value": 4,
"comparison": "GREATER_THAN_EQUALS",
}
},
{
"numberConstraint": {
"fieldName": "price",
"value": 300,
"comparison": "LESS_THAN",
}
},
{
"stringConstraint": {
"fieldName": "amenities",
"any": ["Pets Allowed"]
}
},
{
"stringConstraint": {
"fieldName": "amenities",
"any": ["Wifi"]
}
},
]
}
Search, converting locations in queries to geolocation filters
To search on a query in natural language and get results that are optimized for
natural-language queries including proximity to locations, do the following:
REST
Run the following curl command, which calls the
search
method:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:search" \
-d '{
"query": "
QUERY
",
"naturalLanguageQueryUnderstandingSpec": {
"filterExtractionCondition": "ENABLED",
"geoSearchQueryDetectionFieldNames": ["
GEO_FIELD_NAME_1
", "
GEO_FIELD_NAME_N
"]"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query. The app must be
connected to a data store that contains structured data. The app can't be
a blended search app.
QUERY
: the query is in written in a natural
language.
GEO_FIELD_NAME_1, GEO_FIELD_NAME_N
: a list of
values of type
geolocation
. If the value type isn't
geolocation
, then this field is ignored.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1beta/projects/123456
/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:search"
-d '{
"query": "Find me a chic and stylish hotel with at least 4 stars that is in San Francisco.",
"naturalLanguageQueryUnderstandingSpec": {
"filterExtractionCondition": "ENABLED",
"geoSearchQueryDetectionFieldNames": ["location"]}
}'
{
"results": [
{
"id": "b2617d862",
"document": {
"name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/b2617d862",
...
}
},
{
"id": "a51841841",
"document": {
"name": "projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/a51841841",
...
}
}
],
"naturalLanguageQueryUnderstandingInfo": {
"extractedFilters": "(star_rating: >= 4 AND GEO_DISTANCE("location", "San Francisco", 10000))",
"rewrittenQuery": "chic and stylish",
"extractedFilterStructured": {
"expression": {
"andExpr": {
"expressions": [
{
"numberConstraint": {
"fieldName": "star_rating",
"value": 4,
"comparison": "GREATER_THAN_EQUALS",
}
},
{
"geolocationConstraint": {
"fieldName": "location",
"address": "San Francisco",
"radius_in_meters": 10000,
}
},
]
}
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
{
    "star_rating": &ge;4,
    "price": &le;300,
    "amenities": "Wifi", "Pets Allowed"
}

```

### Code Example 2 (text)

```text
{
    "star_rating": &ge;4,
    "location": GEO_DISTANCE(\"San Francisco, CA\", 10000)
}

```

### Code Example 3 (text)

```text
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID?update_mask=natural_language_query_understanding_config.mode" \
-d '{
      "naturalLanguageQueryUnderstandingConfig": {
        "mode": "ENABLED"
      }
    }'

```

