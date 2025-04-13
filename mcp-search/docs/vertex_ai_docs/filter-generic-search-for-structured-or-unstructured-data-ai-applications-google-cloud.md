# Filter generic search for structured or unstructured data  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)

Home
AI Applications
Documentation
Guides
Send feedback
Filter generic search for structured or unstructured data
Stay organized with collections
Save and categorize content based on your preferences.
If you have a search app that uses structured data, or unstructured data with
metadata, you can use the metadata to filter your search queries. This page
explains how use metadata fields to restrict your search to a specific set of
documents.
Before you begin
Make sure you have created an app and ingested structured data, or unstructured
data with metadata. For more information, see
Create a search app
.
Metadata example
Review this example of metadata for four PDF files (
document_1.pdf
,
document_2.pdf
,
document_3.pdf
, and
document_4.pdf
). This metadata would
be in a JSON file in a Cloud Storage bucket, along with the PDF files. You can
refer back to this example as you read through this page.
{
"id"
:
"1"
,
"structData"
:
{
"title"
:
"Policy on accepting corrected claims"
,
"category"
:
[
"persona_A"
]},
"content"
:
{
"mimeType"
:
"application/pdf"
,
"uri"
:
"gs://bucketname_87654321/data/document_1.pdf"
}}
{
"id"
:
"2"
,
"structData"
:
{
"title"
:
"Claims documentation and reporting guidelines for commercial members"
,
"category"
:
[
"persona_A"
,
"persona_B"
]},
"content"
:
{
"mimeType"
:
"application/pdf"
,
"uri"
:
"gs://bucketname_87654321/data/document_2.pdf"
}}
{
"id"
:
"3"
,
"structData"
:
{
"title"
:
"Claims guidelines for bundled services and supplies for commercial members"
,
"category"
:
[
"persona_B"
,
"persona_C"
]},
"content"
:
{
"mimeType"
:
"application/pdf"
,
"uri"
:
"gs://bucketname_87654321/data/document_3.pdf"
}}
{
"id"
:
"4"
,
"structData"
:
{
"title"
:
"Advantage claims submission guidelines"
,
"category"
:
[
"persona_A"
,
"persona_C"
]},
"content"
:
{
"mimeType"
:
"application/pdf"
,
"uri"
:
"gs://bucketname_87654321/data/document_4.pdf"
}}
Filter expression syntax
Make sure you understand the syntax of the filter expression that you'll use to
define your search filter. The filter expression syntax can be summarized by the following
Extended Backus–Naur form
:
# A single expression or multiple expressions that are joined by "AND" or "OR".
filter
=
expression
,
{
" AND "
|
"OR"
,
expression
}
;
# Expressions can be prefixed with "-" or "NOT" to express a negation.
expression
=
[
"-"
|
"NOT "
]
,
# A parenthetical expression.
|
"("
,
expression,
")"
# A simple expression applying to a text field.
# Function "ANY" returns true if the field exactly matches any of the literals.
(
text_field
,
":"
,
"ANY"
,
"("
,
literal
,
{
","
,
literal
}
,
")"
# A simple expression applying to a numerical field. Function "IN" returns true
# if a field value is within the range. By default, lower_bound is inclusive and
# upper_bound is exclusive.
|
numerical_field
,
":"
,
"IN"
,
"("
,
lower_bound
,
","
,
upper_bound
,
")"
# A simple expression that applies to a numerical field and compares with a double value.
|
numerical_field
,
comparison
,
double
# An expression that applies to a geolocation field with text/street/postal address.
|
geolocation_field
,
":"
,
"GEO_DISTANCE("
,
literal,
","
,
distance_in_meters,
")"
# An expression that applies to a geolocation field with latitude and longitude.
|
geolocation_field
,
":"
,
"GEO_DISTANCE("
,
latitude_double,
","
,
longitude_double,
","
,
distance_in_meters,
")"
# Datetime field
|
datetime_field
,
comparison
,
literal_iso_8601_datetime_format
)
;
# A lower_bound is either a double or "*", which represents negative infinity.
# Explicitly specify inclusive bound with the character 'i' or exclusive bound
# with the character 'e'.
lower_bound
=
(
double,
[
"e"
|
"i"
]
)
|
"*"
;
# An upper_bound is either a double or "*", which represents infinity.
# Explicitly specify inclusive bound with the character 'i' or exclusive bound
# with the character 'e'.
upper_bound
=
(
double,
[
"e"
|
"i"
]
)
|
"*"
;
# Supported comparison operators.
comparison
=
"<="
|
"<"
|
">="
|
">"
|
"="
;
# A literal is any double quoted string. You must escape backslash (\) and
# quote (") characters.
literal
=
double
quoted
string
;
text_field
=
text
field
-
for
example,
category
;
numerical_field
=
numerical
field
-
for
example,
score
;
geolocation_field
=
field
of
geolocation
data
type
-
for
example
home_address,
location
;
datetime_field
=
field
of
datetime
data
type
-
for
example
creation_date,
expires_on
;
literal_iso_8601_datetime_format
=
either
a
double
quoted
string
representing
ISO
8601
datetime
or
a
numerical
field
representing
microseconds
from
unix
epoch.
Search using a metadata filter
To search using a metadata filter, follow these steps:
Determine the metadata field to use for filtering your search queries. For
example, for the metadata in
Before you begin
, you could
use the
category
field as a search filter. Your users could filter on
persona_A
,
persona_B
, or
persona_C
, so their search is restricted to
the documents associated with the persona that they're interested in.
Make the metadata field indexable:
In the Google Cloud console, go to the
AI Applications
page and
in the navigation menu, click
Apps
.
Go to the Apps page
Click your search app.
In the navigation menu, click
Data
.
Click the
Schema
tab. This tab shows current field settings.
Click
Edit
.
Select the
Indexable
checkbox for the field that you want to make
indexable.
Click
Save
. For more information, see
Configure field settings
.
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
Get search results.
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
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/servingConfigs/default_search:search"
\
-d
'{
"query": "
QUERY
",
"filter": "
FILTER
"
}'
Replace the following:
PROJECT_ID
: the ID of your project.
DATA_STORE_ID
: the ID your data store.
QUERY
: the query text to search.
FILTER
: optional. A text field that lets you to filter on a
specified set of fields, using
filter expression
syntax
. The default value is an empty
string, which means no filter is applied.
For example, say that you imported the four PDF files with metadata from
Before you begin
. You want to search for documents that
contain the word "claims", and only query documents with a
category
value of
persona_A
. You would do that by including the following statements with your
call:
"query"
:
"claims"
,
"filter"
:
"category: ANY(\"persona_A\")"
For more information, see the REST tab at
Get search results for an app with structured or unstructured data
.
Click for an example response.
If you perform a search like the one in the preceding procedure, you
can expect to get a response similar to the following. Notice that the
response includes the three documents that have a
category
value of
persona_A
.
{
"results": [
{
"id": "2",
"document": {
"name": "projects/abcdefg/locations/global/collections/default_collection/dataStores/search_store_id/branches/0/documents/2",
"id": "2",
"structData": {
"title": "Claims documentation and reporting guidelines for commercial members",
"category": [
"persona_A",
"persona_B"
]
},
"derivedStructData": {
"link": "gs://bucketname_87654321/data/document_2.pdf",
"extractive_answers": [
{
"pageNumber": "1",
"content": "lorem ipsum"
}
]
}
}
},
{
"id": "1",
"document": {
"name": "projects/abcdefg/locations/global/collections/default_collection/dataStores/search_store_id/branches/0/documents/1",
"id": "1",
"structData": {
"title": "Policy on accepting corrected claims",
"category": [
"persona_A"
]
},
"derivedStructData": {
"extractive_answers": [
{
"pageNumber": "2",
"content": "lorem ipsum"
}
],
"link": "gs://bucketname_87654321/data/document_1.pdf"
}
}
},
{
"id": "4",
"document": {
"name": "projects/abcdefg/locations/global/collections/default_collection/dataStores/search_store_id/branches/0/documents/4",
"id": "4",
"structData": {
"title": "Advantage claims submission guidelines",
"category": [
"persona_A",
"persona_C"
]
},
"derivedStructData": {
"extractive_answers": [
{
"pageNumber": "47",
"content": "lorem ipsum"
}
],
"link": "gs://bucketname_87654321/data/document_4.pdf"
}
}
}
],
"totalSize": 330,
"attributionToken": "UvBRCgsI26PxpQYQs7vQZRIkNjRiYWY1MTItMDAwMC0yZWIwLTg3MTAtMTQyMjNiYzYzMWEyIgdHRU5FUklDKhSOvp0VpovvF8XL8xfC8J4V1LKdFQ",
"guidedSearchResult": {},
"summary": {}
}
Examples of filter expressions
The following table provides examples of filter expressions.
Filter
Only returns results for documents where:
category: ANY("persona_A")
the text field
category
is
persona_A
score: IN(*, 100.0e)
the numerical field
score
is greater than negative infinity and less than 100.0
non-smoking = "true"
the boolean
non-smoking
is true
pet-friendly = "false"
the boolean
pet-friendly
is false
manufactured_date = "2023"
the
manufactured date
is any time in 2023
manufactured_date >= "2024-04-16"
the
manufactured_date
is on or after April 16, 2024
manufactured_date < "2024-04-16T12:00:00-07:00"
the
manufactured_date
is before noon Pacific Daylight Time on April 16, 2024
office.location:GEO_DISTANCE("1600 Amphitheater Pkwy, Mountain View, CA, 94043", 500)
the geolocation field
office.location
is within a 500 m distance of 1600 Amphitheater Pkwy
NOT office.location:GEO_DISTANCE("Palo Alto, CA", 1000)
the geolocation field
office.location
is not within a 1 km radius of Palo Alto, California.
office.location:GEO_DISTANCE(34.1829, -121.293, 500)
the geolocation field
office.location
is within a 500 m radius of latitude 34.1829 and longitude -121.293
category: ANY("persona_A") AND score: IN(*, 100.0e)
category
is
persona_A
and
score
is less than 100
office.location:GEO_DISTANCE("Mountain View, CA", 500) OR office.location:GEO_DISTANCE("Palo Alto, CA", 500)
office.location
is within a 500 m distance of either Mountain View or Palo Alto.
(price<175 AND pet-friendly = "true") OR (price<125 AND pet-friendly = "false")
price
is less than 175 and I can bring my pet, or
price
is less than 125 and I can't bring my pet
What's next
To understand the impact of filters on the search quality,
evaluate the search quality. For more information, see
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
{"id": "1", "structData": {"title": "Policy on accepting corrected claims", "category": ["persona_A"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_1.pdf"}}
{"id": "2", "structData": {"title": "Claims documentation and reporting guidelines for commercial members", "category": ["persona_A", "persona_B"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_2.pdf"}}
{"id": "3", "structData": {"title": "Claims guidelines for bundled services and supplies for commercial members", "category": ["persona_B", "persona_C"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_3.pdf"}}
{"id": "4", "structData": {"title": "Advantage claims submission guidelines", "category": ["persona_A", "persona_C"]}, "content": {"mimeType": "application/pdf", "uri": "gs://bucketname_87654321/data/document_4.pdf"}}

```

### Code Example 2 (text)

```text
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/default_search:search" \
-d '{
"query": "QUERY",
"filter": "FILTER"
}'

```

### Code Example 3 (text)

```text
"query": "claims",
"filter": "category: ANY(\"persona_A\")"

```

