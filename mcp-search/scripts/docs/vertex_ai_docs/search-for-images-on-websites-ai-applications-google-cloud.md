# Search for images on websites  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/image-search](https://cloud.google.com/generative-ai-app-builder/docs/image-search)

Home
AI Applications
Documentation
Guides
Send feedback
Search for images on websites
Stay organized with collections
Save and categorize content based on your preferences.
With Vertex AI Search, you can search for images using a app with
website data. You supply a query in the form of a text string or an image, and
the
default_config.search
method returns images for that query.
Before you begin
Make sure you satisfy the following prerequisites. Requirements vary depending
on whether you search using a text query or an image query.
If you search using a text query in your website search app, make sure the
following is turned on:
Enterprise edition features
If you search using an image query in your website search app, make sure the
following are turned on:
Enterprise edition features
Advanced website indexing
Preview image search
To use the command line to preview image results for a website,
use the
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
Call the
engines.servingConfigs.search
method, specifying
1
for the
search_type
. Choose the method syntax
depending on whether your query is
text or image bytes.
Query is a text string
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
/servingConfigs/default_config:search"
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
"pageSize": "
PAGE_SIZE
",
"offset": "
OFFSET
",
"params": {"search_type": 1}
}'
Query is an image
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
"imageQuery": {"imageBytes":"
IMAGE_BYTES
"},
"pageSize": "
PAGE_SIZE
",
"offset": "
OFFSET
",
"params": {"search_type": 1}
}'
Replace the following:
PROJECT_ID
: the ID of your project.
APP_ID
: the ID of your app.
QUERY
: the search query text. For example, "Round headlight
cars" or "show me dress with stripes."
IMAGE_BYTES
: the image in Base64 encoded bytes. Supported
formats are JPEG, PNG, and BMP.
PAGE_SIZE
: optional. The number of results returned by the
search. The default value is 10 for website search.
Values below 0 cause an error.
Values above 100 cause the value to be set to 100.
OFFSET
: optional. The starting index of the results.
The default value is 0.
For example, if the offset is 2 and the page size is 10, results 2
through 11 are returned.
Review the response. See the following table for field descriptions:
Field
Description
title
The plain text title of the web page that contains the image
htmlTitle
The title, in HTML, of the web page that contains the image
displayLink
An abridged version of this search's result URL, usually the
domain name—for example,
www.example.com
link
The URL of the image
image.contextLink
Context link: A URL pointing to the web page that contains the image
image.byteSize
The size of the image, in bytes
image.width
The width of the image, in pixels
image.height
The height of the image, in pixels
image.thumbnailWidth
The width of the thumbnail image, in pixels
image.thumbnailHeight
The height of the thumbnail image, in pixels
image.thumbnailLink
The URL of the thumbnail image
mime
The MIME type of the image
fileFormat
The file format of the image
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
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_config:search" \
-d '{
"servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"pageSize": "PAGE_SIZE",
"offset": "OFFSET",
"params": {"search_type": 1}
}'

```

### Code Example 2 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
-d '{
"servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
"imageQuery": {"imageBytes":"IMAGE_BYTES"},
"pageSize": "PAGE_SIZE",
"offset": "OFFSET",
"params": {"search_type": 1}
}'

```

