# Order web search results  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/order-web-search-results](https://cloud.google.com/generative-ai-app-builder/docs/order-web-search-results)

Home
AI Applications
Documentation
Guides
Send feedback
Order web search results
Stay organized with collections
Save and categorize content based on your preferences.
This page explains how to order the results of a web search query by date.
For data stores that use basic website search, you can order by
Google-inferred page dates.
For data stores that use advanced website indexing, you can order by
custom data attributes or Google-inferred page dates that are added to the
data store schema. For more information, see
Use structured data for advanced website indexing
.
Before you begin
Make sure that you do the following:
Create a data store with website data. For more information, see
Website
URLs
.
Create a search app and connect it to the data store. For more information,
see
Create a search app
.
Order search results for basic website search
To order the search results for a website data store with
basic website search, follow these steps:
REST
The following sample shows how to to order your web search results for an app
with basic website search. This sample uses the
engines.servingConfigs.search
method:
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
Make a search query and include the
orderBy
field.
curl
-X
POST
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
"orderBy": "
ORDER_BY
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY
: the query text to search.
ORDER_BY
: the order in which the results are arranged. For
example, to order chronologically, specify
date
to return web pages
sorted by Google-inferred page date. For more information on
the Google-inferred page date, see the
Help Google Search know the best date for your web page
blog post.
The default sort order is descending, in which the pages with the
most recent dates are returned first. To get ascending sort order,
append
:a
to the
date
value—
date:a
.
Order search results for advanced website indexing
To order the search results for a website data store with
advanced website indexing, follow these steps:
REST
The following sample shows how to order your web search results for an app
with advanced website indexing. This sample uses the
engines.servingConfigs.search
method:
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
Make a search query and include the
orderBy
field.
curl
-X
POST
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
"orderBy": "
ORDER_BY
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY
: the query text to search.
ORDER_BY
: the order in which the results are arranged. The
field can have values that are of the following data types: datetime,
integer, or number. To order chronologically, specify the custom date
attribute specified in the schema or the Google-inferred page date to
return web pages sorted by date. For example, to order by a
date_edited
PageMap attribute, you can specify the
orderBy
field
as
"orderBy": "date_edited"
. The default sort order is ascending, in
which older pages are returned first. To get the results in descending
order, append
desc
to the custom attribute value—for example,
"orderBy":"date_edited desc"
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
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
-d '{
"servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"orderBy": "ORDER_BY"
}'

```

### Code Example 2 (text)

```text
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
-d '{
"servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"orderBy": "ORDER_BY"
}'

```

