# Configure field settings  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/configure-field-settings](https://cloud.google.com/generative-ai-app-builder/docs/configure-field-settings)

Home
AI Applications
Documentation
Guides
Send feedback
Configure field settings
Stay organized with collections
Save and categorize content based on your preferences.
This page shows you how to configure the fields to set up an app for structured
data or for unstructured data with metadata.
Field settings help determine how Vertex AI Search uses fields in
its results. You can use the
Schema
tab in the
Google Cloud console to configure field settings for structured data and
unstructured data with metadata.
Configuring field settings is available only for apps with data stores that have
either structured data or unstructured data with metadata.
The following field settings are available:
Field setting
Definition
Use case
Indexable
If a field is set to
Indexable
,
Vertex AI Search can filter, order, and facet using this field.
Setting object fields to indexable is not supported.
Search
Searchable
If a field is set to
Searchable
, recall for that
field in Vertex AI Search queries is improved. Only fields with
text values can be set to
Searchable
.
Search
Dynamic facetable
If a field is set to
Dynamic Facetable
,
Vertex AI Search can use that field as a dynamic facet. Dynamic
facets can be automatically added to a search based on previous user
behavior such as facet clicks and views. This setting is applicable only to
fields that are indexable.
Search
Retrievable
If a field is set to
Retrievable
,
Vertex AI Search returns the field in search results.
Search
Completable
If a field is set to
Completable
,
Vertex AI Search uses the field's contents as search query
suggestions. For more information, see
Configure autocomplete
.
Search
Filterable
If a field is set to
Filterable
,
Vertex AI Search recommendations can use that field to filter
recommendations results. For information about filtering recommendations,
see
Filter
recommendations
.
Recommendations
Limitations
Field settings have the following limitations:
You can configure up to 50 fields as indexable, searchable, or
dynamic facetable.
You can configure up to 30 fields as retrievable.
To configure a field as dynamic facetable, it must first be configured as
indexable.
Changing the indexable setting requires re-indexing the data, which can take
hours, especially for large data stores.
If you are configuring fields for a media search app and want detailed
information about the fields in the schema, see
About media documents and data
stores
.
Update field settings
To update field settings:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit.
Click
Data
.
Click the
Schema
tab. This tab shows current field settings.
Click
Edit
.
Select or clear field settings that you need to update. Some field
settings are not supported. For example, numerical fields cannot be set to
Searchable
.
Click
Save
to apply your changes.
What's next
Update a schema for structured data
Configure search results
Preview search results
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-12 UTC.

