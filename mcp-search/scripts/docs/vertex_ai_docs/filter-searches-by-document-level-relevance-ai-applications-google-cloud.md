# Filter searches by document-level relevance  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance](https://cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance)

Home
AI Applications
Documentation
Guides
Send feedback
Filter searches by document-level relevance
Stay organized with collections
Save and categorize content based on your preferences.
When searching in your Vertex AI Search app, you can apply a
relevance threshold so that only the documents that meet this threshold
are returned as results. This page explains how to specify a
relevance threshold in order to reduce the number of documents returned in
queries.
About filtering by document-level relevance
Each document returned by a search query is given a relevance level, which
indicates the relevance of the returned document to the query. When you make a
query through an API call, you can set a relevance threshold. Setting a high
relevance threshold can reduce the number of documents returned by a query.
For example, if you find that search is returning too many documents of
insufficient relevance to your users, set the relevance threshold to high to
narrow the results to only those few that are most relevant. If the high setting
is too restrictive, try the medium setting.
Data types and apps supported for document-level relevance filter
The document-level relevance filter can be applied to data stores with following kinds of data:
Website data with advanced website indexing
Generic unstructured data
Generic structured data
The document-level relevance filter doesn't work for data stores with basic website indexing,
media data, or healthcare data.
Furthermore, the document-level relevance filter can't be used with blended search apps. Blended
search apps are apps that are connected to multiple data stores.
Other kinds of filters
The document-level relevance filter is not the only way you can filter data returned by queries. You
can also use filter expressions to filter results based on metadata (in
advanced website indexing and unstructured data with metadata data stores) and field
values (in structured data stores).
For information, see:
Filter expressions with advanced website indexing
Filter generic search for structured or unstructured data
If you use both a filter expression and the document-level relevance filter, the filter expression
is applied first to the results and then the document-level relevance filter is applied.
Before you begin
Make sure you have created an app and data store and have ingested data
into your data store. For more information, see
Create a search
app
. See also
Data types and apps supported for
document-level relevance filter
.
Search and filter results by document-level relevance
To filter by relevance, follow these steps:
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
To filter search by document-level relevance, use the
relevanceThreshold
field with the
engines.servingConfigs.search
method.
curl
-X
POST
-H
"Authorization: Bearer
$(
gcloud
auth
application-default
print-access-token
)
"
\
-H
"Content-Type: application/json"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:search"
\
-d
'{
"servingConfig": "projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search",
"query": "
QUERY
",
"relevanceThreshold": "
RELEVANCE_THRESHOLD
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: the query text to search.
RELEVANCE_THRESHOLD
: one of the following:
HIGH
,
MEDIUM
,
LOW
,
LOWEST
.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global/collections/default_collection/engines/my-search-app/servingConfigs/default_search:search" \
-d '{
"servingConfig": "projects/my-project-123/locations/global/collections/default_collection/engines/my-search-app/servingConfigs/default_search",
"query": "What is the check grounding API",
"relevanceThreshold": "HIGH"
}'
{
"results": [
{
"id": "a082e70352c073a4443502477255bd2a",
"document": {
"name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/a082e70352c073a4443502477255bd2a",
"id": "a082e70352c073a4443502477255bd2a",
"derivedStructData": {
"displayLink": "cloud.google.com",
"link": "https://cloud.google.com/generative-ai-app-builder/docs/check-grounding",
"htmlTitle": "Check grounding",
"title": "Check grounding"
}
}
}
],
"totalSize": 1,
"attributionToken": "f_B-CgwIidzwswYQyue15gESJDY2N2M1NmJkLTAwMDAtMjk3Ni1iMGI4LTg4M2QyNGZmNTZhOCIHR0VORVJJQypAjr6dFavEii3b7Ygt3o-aIoCymiLC8J4Vo4CXIra3jC3Usp0V24-aIt7tiC3n7YgtrsSKLeTtiC2DspoixsvzFw",
"guidedSearchResult": {},
"summary": {}
}
Here, the relevance threshold is set to high, so only the most
relevant results are returned. In this example, only one document was determined
to be highly relevant.
Test multiple queries with different thresholds to determine the best
threshold settings for your data and application.
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
curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
-d '{
 "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"relevanceThreshold": "RELEVANCE_THRESHOLD"
}'

```

