# Prepare data for ingesting  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/prepare-data](https://cloud.google.com/generative-ai-app-builder/docs/prepare-data)

Home
AI Applications
Documentation
Guides
Send feedback
Prepare data for ingesting
Stay organized with collections
Save and categorize content based on your preferences.
How you prepare data depends on the kind of data you're importing and the way
you choose to import it. Start with what kind of data you plan to import:
Website data
Unstructured data
Structured data
Third-party data sources
Structured media data
Healthcare FHIR data
For information about blended search, where multiple data stores can be
connected to a single generic search app, see
About connecting multiple data
stores
.
Website data
When you create a data store for website data, you provide the URLs of web
pages that Google should crawl and index for searching or recommending.
Before indexing your website data:
Decide which URL patterns to include in your indexing and which to exclude.
Exclude the patterns for dynamic URLs
. Dynamic URLs are URLs that
change at the time of serving depending on the request.
For example, the URL patterns for the web pages that serve the search
results, such as
www.example.com/search/*
. Suppose, a user searches for
the phrase
Nobel prize
, the dynamic search URL might be a unique URL:
www.example.com/search?q=nobel%20prize/
UNIQUE_STRING
.
If the URL pattern
www.example.com/search/*
is not excluded, then all
such unique, dynamic search URLs that follow this pattern are indexed.
This results in a bloated index and a diluted search quality.
Eliminate duplicate URLs using canonical URL patterns
. This provides
a single canonical URL for Google Search when crawling the website and
removes ambiguity. For examples of canonicalization and more
information, see
What is URL canonicalization
and
How to specify a canonical URL with rel="canonical" and other methods
.
You can include URL patterns either from the same or different domains that
need to be indexed and exclude patterns that must not be indexed. The number of
URL patterns that you can include and exclude differs in the following way:
Indexing type
Included sites
Excluded sites
Basic website search
Maximum of 50 URL patterns
Maximum of 50 URL patterns
Advanced website indexing
Maximum of 500 URL patterns
Maximum of 500 URL patterns
Check that the web pages you plan to provide are not using robots.txt to block
indexing. For more information, see
Introduction to robot.txt
.
If you plan to use
Advanced website indexing
, you
must be able to
verify the domains
for the URL patterns
in your data store.
Add structured data in the form of
meta
tags and PageMaps to your
data store schema to enrich your indexing as explained in
Use structured data for advanced website indexing
.
Unstructured data
Vertex AI Search supports search over documents that are in HTML,
PDF with embedded text, and TXT format. PPTX and DOCX formats are available in
Preview.
You import your documents from a
Cloud Storage
bucket. You can import using Google Cloud console, by the
ImportDocuments
method, or by streaming ingestion
through CRUD methods.
For API reference information, see
DocumentService
and
documents
.
The following table lists the file size limits of each file type with different
configurations (for more information, see
Parse and chunk documents
). You can
import up to 100,000 files at a time.
File type
Default import
Import with layout-aware document chunking
Import with layout parser
Text-based files such as HTML, TXT, JSON, XHTML, and XML
< 2.5 MB
< 10 MB
< 10 MB
PPTX, DOCX, and XLSX
< 200 MB
< 200 MB
< 200 MB
PDF
< 200 MB
< 200 MB
< 40 MB
If you plan to include embeddings in your unstructured data, see
Use custom embeddings
.
If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images,
such as infographics) we recommend turning on optical character recognition
(OCR) processing during data store creation. This allows
Vertex AI Search to extract elements such as text blocks and
tables. If you have searchable PDFs that are mostly composed of machine-readable
text and contain many tables, you can consider turning on OCR processing with
the option for machine-readable text enabled in order to improve detection and
parsing. For more information, see
Parse and chunk
documents
.
If you want to use Vertex AI Search for retrieval-augmented generation
(RAG), turn on document chunking when you create your data store. For more
information, see
Parse and chunk documents
.
You can import unstructured data from the following sources:
Cloud Storage
BigQuery
Google Drive
Cloud Storage
You can import data from Cloud Storage with or without metadata.
Data import is not recursive. That is, if there are folders within the bucket or
folder that you specify, files within those folders are not imported.
If you plan to import documents from Cloud Storage without metadata, put your
documents directly into a Cloud Storage bucket. The document ID is an example
of metadata.
For testing, you can use the following publicly available Cloud Storage
folders, which contain PDFs:
gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs
gs://cloud-samples-data/gen-app-builder/search/CUAD_v1
gs://cloud-samples-data/gen-app-builder/search/kaiser-health-surveys
gs://cloud-samples-data/gen-app-builder/search/stanford-cs-224
If you plan to import data from Cloud Storage with metadata, put a JSON file
that contains the metadata into a Cloud Storage bucket whose location you
provide during import.
Your unstructured documents can be in the same Cloud Storage bucket as your
metadata or a different one.
The metadata file must be a
JSON Lines
or an NDJSON file. The document ID is an
example of metadata. Each row of the metadata file must follow one of the
following JSON formats:
Using
jsonData
:
{ "id": "<your-id>", "jsonData": "<JSON string>", "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }
Using
structData
:
{ "id": "<your-id>", "structData": { <JSON object> }, "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }
Use the
uri
field in each row to point to the Cloud Storage location of
the document.
Here is an example of an NDJSON metadata file for an unstructured document. In
this example, each line of the metadata file points to a PDF document and
contains the metadata for that document. The first two lines use
jsonData
and
the second two lines use
structData
. With
structData
you don't need to
escape quotation marks that appear within quotation marks.
{"id":"doc-0","jsonData":"{\"title\":\"test_doc_0\",\"description\":\"This document uses a blue color theme\",\"color_theme\":\"blue\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_0.pdf"}}
{"id":"doc-1","jsonData":"{\"title\":\"test_doc_1\",\"description\":\"This document uses a green color theme\",\"color_theme\":\"green\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_1.pdf"}}
{"id":"doc-2","structData":{"title":"test_doc_2","description":"This document uses a red color theme","color_theme":"red"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_3.pdf"}}
{"id":"doc-3","structData":{"title":"test_doc_3","description":"This is document uses a yellow color theme","color_theme":"yellow"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_4.pdf"}}
To create your data store, see
Create a search data store
.
BigQuery
If you plan to import metadata from BigQuery, create a
BigQuery table that contains metadata. The document ID is an example
of metadata.
Put your unstructured documents into a Cloud Storage bucket.
Use the following BigQuery schema. Use the
uri
field in
each record to point to the Cloud Storage location of the document.
[
{
"name": "id",
"mode": "REQUIRED",
"type": "STRING",
"fields": []
},
{
"name": "jsonData",
"type": "STRING",
"fields": []
},
{
"name": "content",
"type": "RECORD",
"mode": "NULLABLE",
"fields": [
{
"name": "mimeType",
"type": "STRING",
"mode": "NULLABLE"
},
{
"name": "uri",
"type": "STRING",
"mode": "NULLABLE"
}
]
}
]
For more information, see
Create and use tables
in the BigQuery documentation.
To create your data store, see
Create a search data store
.
Google Drive
Syncing data from Google Drive is supported for generic search.
If you plan to import data from Google Drive, you must set up Google Identity
as your identity provider in AI Applications. For information about
setting up access control, see
Use data source access
control
.
To create your data store, see
Create a search data store
.
Structured data
Prepare your data according to the import method that you plan to use. If you
plan to ingest media data, also see
Structured media data
.
You can import structured data from the following sources:
Cloud Storage
Local JSON data
Third-party data sources
(Preview with allowlist)
When you import structured data from BigQuery or from Cloud Storage,
you are given the option to import the data with metadata. (Structured with
metadata is also referred to as
enhanced structured data
.)
BigQuery
You can import structured data from BigQuery datasets.
Your schema is auto-detected. After importing, Google recommends that you
edit the auto-detected schema to map key properties, such as titles. If you
import using the API instead of the Google Cloud console, you have the option
to provide your own schema as a JSON object. For more information, see
Provide or auto-detect a schema
.
For examples of publicly available structured data, see the
BigQuery public datasets
.
If you plan to include embeddings in your structured data, see
Use custom embeddings
.
If you select to import structured data with metadata, you include two fields in
your BigQuery tables:
An
id
field to identify the document. If you import structured data
without metadata, then the
id
is generated for you. Including metadata
lets you specify the value of
id
.
A
jsonData
field that contains the data. For examples of
jsonData
strings,
see the preceding section
Cloud Storage
.
Use the following BigQuery schema for structured data with metadata
imports:
[
{
"name": "id",
"mode": "REQUIRED",
"type": "STRING",
"fields": []
},
{
"name": "jsonData",
"mode": "NULLABLE",
"type": "STRING",
"fields": []
}
]
For instructions on creating your data store, see
Create a search data store
or
Create a recommendations data store
.
Cloud Storage
Structured data in Cloud Storage must be in either
JSON
Lines
or
NDJSON format. Each file must be 2 GB or smaller. You can import up to 100 files
at a time.
For examples of publicly available structured data, refer to the following
folders in Cloud Storage, which contain NDJSON files:
gs://cloud-samples-data/gen-app-builder/search/kaggle_movies
gs://cloud-samples-data/gen-app-builder/search/austin_311
If you plan to include embeddings in your structured data, see
Use custom embeddings
.
Here is an example of an NDJSON metadata file of structured data. Each line of
the file represents a document and is made up of a set of fields.
{"hotel_id": 10001, "title": "Hotel 1", "location": {"address": "1600 Amphitheatre Parkway, Mountain View, CA 94043"}, "available_date": "2024-02-10", "non_smoking": true, "rating": 3.7, "room_types": ["Deluxe", "Single", "Suite"]}
{"hotel_id": 10002, "title": "Hotel 2", "location": {"address": "Manhattan, New York, NY 10001"}, "available_date": "2023-07-10", "non_smoking": false, "rating": 5.0, "room_types": ["Deluxe", "Double", "Suite"]}
{"hotel_id": 10003, "title": "Hotel 3", "location": {"address": "Moffett Park, Sunnyvale, CA 94089"}, "available_date": "2023-06-24", "non_smoking": true, "rating": 2.5, "room_types": ["Double", "Penthouse", "Suite"]}
To create your data store, see
Create a search data store
or
Create a recommendations data store
.
Local JSON data
You can directly upload a JSON document or object using the API.
Google recommends providing your own schema as a JSON object for better results. If
you don't provide your own schema, the schema is auto-detected. After
importing, we recommend that you edit the auto-detected schema to map key
properties, such as titles. For more information, see
Provide or auto-detect a schema
.
If you plan to include embeddings in your structured data, see
Use custom embeddings
.
To create your data store, see
Create a search data store
or
Create a recommendations data store
.
Structured media data
If you plan to ingest structured media data, such as videos, news, or music,
review the following:
Information about your import method (BigQuery or
Cloud Storage):
Structured data
Required schemas and fields for media documents and data stores:
About media documents and data stores
User event requirements and schemas:
About user events
Information about media recommendations types:
About media recommendations types
Third-party data sources
Ingesting from third-party data sources is a preview with allowlist feature.
Third-party data source connections are supported for generic search.
When you connect a third-party data source, the data is initially ingested and
then is synced to Vertex AI Search at a frequency that you specify.
Before setting up your data source connection, you must set up access control
for your data source. For information about setting up access control, see
Use data source access control
.
For required credentials to connect a data source, go to the documentation for
connecting the third-party data source that you plan to ingest from:
Connect Confluence
Connect Jira Cloud
Connect Salesforce
Connect ServiceNow
Connect Slack
Healthcare FHIR data
If you plan to ingest FHIR data from Cloud Healthcare API, ensure the following:
Location: The source FHIR store must be in a Cloud Healthcare API dataset that's
in the
us-central1
,
us
, or
eu
location. For more information, see
Create and manage datasets in Cloud Healthcare API
.
FHIR store type: The source FHIR store must be an R4 data store. You can
check the versions of your FHIR stores by
listing the FHIR stores in your dataset
.
To create a FHIR R4 store, see
Create FHIR stores
.
Import quota: The source FHIR store must have fewer than 1 million FHIR resources.
If there are more than 1 million FHIR resources, the import process stops
after this limit is reached. For more information, see
Quotas and limits
.
The files referenced in a
DocumentReference
resource
must be PDF, RTF,
or image files that are stored in Cloud Storage.
The link to the referenced files must be in the
content[].attachment.url
field
of the resource in the standard Cloud Storage path format:
gs://
BUCKET_NAME
/
PATH_TO_REFERENCED_FILE
.
Review the list of FHIR R4 resources that Vertex AI Search
supports. For more information, see
Healthcare FHIR R4 data schema reference
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
{"id":"doc-0","jsonData":"{\"title\":\"test_doc_0\",\"description\":\"This document uses a blue color theme\",\"color_theme\":\"blue\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_0.pdf"}}
{"id":"doc-1","jsonData":"{\"title\":\"test_doc_1\",\"description\":\"This document uses a green color theme\",\"color_theme\":\"green\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_1.pdf"}}
{"id":"doc-2","structData":{"title":"test_doc_2","description":"This document uses a red color theme","color_theme":"red"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_3.pdf"}}
{"id":"doc-3","structData":{"title":"test_doc_3","description":"This is document uses a yellow color theme","color_theme":"yellow"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_4.pdf"}}

```

### Code Example 2 (text)

```text
[
  {
    "name": "id",
    "mode": "REQUIRED",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "jsonData",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "content",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "mimeType",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "uri",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  }
]

```

### Code Example 3 (text)

```text
[
  {
    "name": "id",
    "mode": "REQUIRED",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "jsonData",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  }
]

```

### Code Example 4 (text)

```text
{"hotel_id": 10001, "title": "Hotel 1", "location": {"address": "1600 Amphitheatre Parkway, Mountain View, CA 94043"}, "available_date": "2024-02-10", "non_smoking": true, "rating": 3.7, "room_types": ["Deluxe", "Single", "Suite"]}
{"hotel_id": 10002, "title": "Hotel 2", "location": {"address": "Manhattan, New York, NY 10001"}, "available_date": "2023-07-10", "non_smoking": false, "rating": 5.0, "room_types": ["Deluxe", "Double", "Suite"]}
{"hotel_id": 10003, "title": "Hotel 3", "location": {"address": "Moffett Park, Sunnyvale, CA 94089"}, "available_date": "2023-06-24", "non_smoking": true, "rating": 2.5, "room_types": ["Double", "Penthouse", "Suite"]}

```

