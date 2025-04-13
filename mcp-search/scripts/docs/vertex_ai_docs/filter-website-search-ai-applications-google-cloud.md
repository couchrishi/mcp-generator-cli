# Filter website search  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/filter-website-search](https://cloud.google.com/generative-ai-app-builder/docs/filter-website-search)

Home
AI Applications
Documentation
Guides
Send feedback
Filter website search
Stay organized with collections
Save and categorize content based on your preferences.
This page explains how to filter search queries for a search app with
website
data
.
Before you begin
Make sure you have created an app and data store and have ingested website data
into your data store. For more information, see
Create a search
app
.
About filter expressions
Use filter expressions to construct your website search filters. How you
construct your filters varies depending on whether you have turned on
advanced website indexing
. See one of the following sections,
depending on whether you have basic website search or advanced website indexing:
Filter expressions for basic website search
Filter expressions for advanced website indexing
Filter expressions for basic website search
This section explains filter expression behavior with basic website search
(advanced website indexing is turned off).
Syntax for basic website search
The following
Extended Backus–Naur form
summarizes filter expression
syntax for constructing a website search filter when you have basic website search. Double quotes after the colon in a filter are strictly enforced.
# A single expression or multiple expressions that are joined by "AND".
filter
=
expression
,
{
"AND"
,
expression
}
;
expression
=
# A simple expression applying to a text url string.
|
filter_key,
":"
,
\"
text_value
\"
filter_key
=
(
cr
|
highRange
|
lowRange
|
fileType
|
lr
|
rights
|
siteSearch
)
;
text_value
=
string
value
to
filter
on
;
Available fields for basic website search
Here are the fields that are available for filtering your website search when
you have basic website search:
cr
(string) Restricts search results to documents from a specific country.
For a list of supported values, see
Country Collection
Values
.
highRange
(string) Specifies the upper limit of the search range. If a
document contains a number, the number must be at or below the value of
highRange
for that document to be included in the response. Specify both
highRange
and
lowRange
to create a search query within the range of
these parameters.
lowRange
(string) Specifies the lower limit of the search range. If a
document contains a number, the number must be at or above the value of
lowRange
for that document to be included in the response. Specify both
lowRange
and
highRange
to create a search query within the range of
these parameters.
fileType
(string) Restricts search results to documents with a specified
extension. For a list of supported file types, see
File types indexable by
Google
.
lr
(string) Restricts search results to documents written in a specified
language. For a list of supported languages, see
Query parameters
(lr)
.
rights
(string) Filters search results based on licensing. For supported
values, see
Query parameters
(rights)
.
siteSearch
(string) Specifies A URL pattern for the web pages that your
query should search through.
Examples for basic website search
Here are some filter examples for basic website search:
{"filter": "cr:\"countryUS\" AND
siteSearch:\"https://example.com/example_domain\""}
Filters for documents that are: (1) From the US, and (2) In the domain
https://example.com/example_domain
.
{"filter": "fileType:\".pdf\" AND lr:\"lang_en\""}
Filters for documents that are: (1) PDF files, and (2) In English.
{"filter": "rights:\"cc_publicdomain\""}
Filters for documents that are in the public domain.
Filter expressions with advanced website indexing
This section explains filter expression behavior with advanced website indexing
(advanced website indexing is turned on).
Available fields for advanced website indexing
When you have advanced website indexing, you can filter your website search
using these fields:
siteSearch
(string): A URL pattern for the web pages that your
query should search through.
meta
tag names and PageMap Attribute names: Structured data from your
web pages that can be added to your data store's schema to make the fields
searchable, retrievable, and indexable. For more information, see
Use structured data for advanced website indexing
.
Syntax for advanced website indexing
The following
Extended Backus–Naur form
summarizes filter expression
syntax for constructing a website search filter when you have
advanced website indexing. Double quotes after the colon in a filter are strictly enforced.
When filtering for
siteSearch
the EBNF syntax is:
# A single expression or multiple expressions that are joined by "OR".
filter
=
expression
,
{
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
# A simple expression applying to a text url string.
|
filter_key,
":"
,
\"
url_string
\"
filter_key
=
siteSearch
;
url_string
=
double
quoted
string
representing
a
URL
;
When filtering for
meta
tag names and PageMap Attribute names, the EBNF syntax is:
# A single expression or multiple expressions that are joined by "OR".
filter
=
expression
,
{
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
# Function "ANY" returns true if the field exactly matches any of the literals.
|
text_field,
":"
,
"ANY"
,
"("
,
literal,
{
","
,
literal
}
,
")"
literal
=
double
quoted
string
;
# text_field corresponds to the meta tag or PageMap Attribute name, for example, category
text_field
=
text
field
;
Examples for advanced website indexing
Here are some filter examples for advanced website indexing with
siteSearch
:
{"filter": "siteSearch:\"https://example.com/example_domain\""}
Filters for documents that are in the domain
https://example.com/example_domain
. For example,
https://example.com/example_domain/index.html
.
{"filter": "siteSearch:\"https://example.com/subdomains/*\""}
Filters for documents that are in any domains matching
https://example.com/subdomains/*
. For example,
https://example.com/subdomains/example_subdomain_page
.
{"filter": "siteSearch:\"https://altostrat.com/subdomain/pages/*\" OR
siteSearch:\"http://cymbalgroup.com/pages/*\""}
Filters for documents that are in any domains matching the first or second
URL pattern. For example,
https://altostrat.com/subdomain/pages/title_page
,
https://cymbalgroup.com/subdomain/pages/title_page
, or
https://altostrat.com/subdomain/pages/INFO
.
Here are some examples for
meta
or PageMap Attribute name filtering:
{"filter": "product: ANY(\"networking\",\"compute\")"}
Filters for documents which contain the
meta
tag or PageMap attribute named
product
, with its value as either
networking
or
compute
.
{"filter": "NOT product: ANY(\"storage\")"}
Filters for documents which don't contain the
meta
tag or PageMap Attribute name
product
with its value as
storage
.
For more information on
meta
tag names and PageMap Attribute names used for indexing,
see
Example use case for
meta
tags
and
Example use case for PageMaps
.
Filter a website search
To filter a website search, follow these steps:
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
To filter a website search, use the
filter
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
"filter": "
FILTER
"
}'
Replace the following:
PROJECT_ID
: the ID of your project.
APP_ID
: the ID of your app.
QUERY
: the query text to search.
FILTER
: a text field for filtering your search using a
filter expression. The default value is an empty string.
For information about constructing a filter for basic website search, see
Filter expressions with basic website search
.
For information about constructing a filter for advanced website indexing, see
Filter expressions with advanced website indexing
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
curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
-d '{
 "servingConfig": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"filter": "FILTER"
}'

```

