# Get snippets and extracted content  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/snippets](https://cloud.google.com/generative-ai-app-builder/docs/snippets)

Home
AI Applications
Documentation
Guides
Send feedback
Get snippets and extracted content
Stay organized with collections
Save and categorize content based on your preferences.
Vertex AI Search can provide search snippets, extractive answers, and
extractive segments with each search response to enhance your results.
Snippets
: A snippet is a brief extract of text from the
search result document that provides a preview of a search result's content.
It includes hit highlighting that you can render in your UI. Snippets are
typically displayed under each search result to help end users assess the
relevance and usefulness of that result. Snippets are available for data
stores with unstructured data and website data (both basic website search and advanced website indexing).
Extractive answers
: An extractive answer
is verbatim text that is returned with each search result. It is extracted
directly from the original document. Extractive answers are typically
displayed near the top of web pages to provide an end user with a brief answer
that is contextually relevant to their query. Extractive answers are available
for data stores with unstructured data and with advanced website indexing.
Extractive segments
: An extractive
segment is verbatim text that is returned with each search result. An
extractive segment is usually more verbose than an extractive answer.
Extractive segments can be displayed as an answer to a query, and can be used
to perform post-processing tasks and as input for large language models to
generate answers or new text. Extractive segments are available
for data stores with unstructured data and with advanced website indexing.
Examples
The following examples help illustrate the differences between snippets,
extractive answers, and extractive segments.
Query:
"what is ai applications?"
Snippet:
To enable this, we are announcing our new
AI Applications
,
the fastest way for developers to jumpstart the creation of
gen
apps such as bots, ...
Extractive answer:
AI Applications allows developers to quickly ship new
experiences including bots, chat interfaces, custom search engines, digital
assistants, and more. Developers have API access to Google's foundation
models and can use out-of-the-box templates to jumpstart the creation of gen
apps in minutes or hours.
Extractive segment:
Businesses and governments also want to make customer, partner, and employee
interactions more effective and helpful with this new AI technology. To
enable this, we are announcing our new AI Applications.
AI Applications allows developers to quickly ship new
experiences including bots, chat interfaces, custom search engines, digital
assistants, and more. Developers have API access to Google's foundation
models and can use out-of-the-box templates to jumpstart the creation of gen
apps in minutes or hours. With AI Applications, developers
will also:
Combine organizational data and information retrieval techniques to provide relevant answers.
Search and respond with more than just text.
Combine natural conversations with structured flows.
Don't just inform — transact.
Before you begin
Depending on the type of app you have, complete the following prerequisites:
Unstructured app:
For
snippets
there is no requirement.
For
extractive answers
and
extractive segments
, turn on
Enterprise edition features
.
Website app:
For snippets, turn on:
Enterprise edition features
.
For extractive answers, turn on:
Enterprise edition features
.
Advanced website indexing
.
Snippets
Snippets are short pieces of extracted verbatim from each search result
document. They include hit highlighting in bold HTML tags for rendering previews
of search results in a UI. Typically, snippets are rendered as preview text
underneath a search result to help end users decide if clicking that search
result will be useful.
Snippets are available for website and unstructured search.
Get snippets
To get snippets:
Send a search request that includes
ContentSearchSpec.SnippetSpec
and sets
returnSnippet
to true.
The following example of
SnippetSpec
specifies that a
snippet can be returned for each search result.
"contentSearchSpec"
:
{
"snippetSpec"
:
{
"returnSnippet"
:
true
}
}
returnSnippet
: If set to
true
, return a snippet.
Get snippets from the search response. Snippets are returned with each search
result in
derivedStructData.snippets
.
In this example of a document that was returned as one of the results in a
search response, a snippet with bold hit highlighting is included with the
result:
{
"id"
:
"54321"
,
"document"
:
{
"name"
:
"projects/123/locations/global/collections/default_collection/dataStores/example-datastore/branches/0/documents/54321"
,
"id"
:
"54321"
,
"derivedStructData"
:
{
"link"
:
"gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2008_google_annual_report.pdf"
,
"snippets"
:
[
{
"snippet"
:
"Google Chrome. Google Chrome is an open-source
browser
that combines a minimal design with technologies to make the web faster, safer, and easier to navigate."
,
"snippet_status"
:
"SUCCESS"
}
]
}
}
}
snippet
: Contains a snippet generated for the document search result.
Hit highlighting is included in bold HTML tags.
snippet_status
: If a snippet is generated, this field is returned
as
SUCCESS
. If no snippet is generated, this field is returned as
NO_SNIPPET_AVAILABLE
.
Extractive answers
An extractive answer is a section of text derived verbatim from a document. When
a document is returned as a search result in a search response, a
relevant extractive answer can be returned with that result.
An extractive answer can be text such as a paragraph, table, or bulleted list
that is extracted from the search result document. Extractive answers are
shorter than
extractive segments
.
Extractive answers can be used as an alternative to summarized responses in
cases where precise, verbatim answers are preferable to rephrased summaries.
Extractive answers are available for data stores with unstructured data and with
advanced website indexing.
Get extractive answers
To get extractive answers:
Send a search request that uses
ContentSearchSpec.extractiveContentSpec
to specify
maxExtractiveAnswerCount
.
The following example of
extractiveContentSpec
specifies that an
answer can be returned for each search result.
"contentSearchSpec"
:
{
"extractiveContentSpec"
:
{
"maxExtractiveAnswerCount"
:
1
}
}
maxExtractiveAnswerCount
: The number of extractive answers to return
for each search result. The default value is 0 and the maximum is 5.
Get extractive answers from the search response. Extractive answers are
returned with each search result in
extractive_answers
.
In this example of a document that was returned as one of the results in a
search response, an extractive answer was included with the result:
{
"id"
:
"54321"
,
"document"
:
{
"name"
:
"projects/123/locations/global/collections/default_collection/dataStores/example-datastore/branches/0/documents/54321"
,
"id"
:
"54321"
,
"derivedStructData"
:
{
"extractive_answers"
:
[
{
"pageNumber"
:
"2"
,
"content"
:
"Google saw growth throughout the year both in our domestic business and internationally, both on Google owned sites and on the Google Network. Specifically, revenues from Google owned sites increased 101% on a year over year basis, from $792 million to $1.6 billion."
}
],
"link"
:
"gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2004Q4_earnings_google.pdf"
}
}
}
pageNumber
: If page numbers can be extracted from the document, this
field indicates where the answer was extracted from.
content
: The content of the extractive answer.
Extractive segments
An extractive segment is a section of text that is extracted verbatim from a
search result document. Extractive segments are similar to
extractive
answers
, but extractive segments usually more complete and
verbose. Typically, extractive segments are used as input for your own LLMs to
generate answers or new text.
Extractive segments can be multiple paragraphs, including formatted text such
as tables and bulleted lists.
Extractive segments are available for data stores with unstructured data
and with advanced website indexing.
Extractive segment options
The following options are available for extractive segments:
Number of segments
: You can specify up to 10 extractive segments to
return for each search result.
Relevance scores
: Relevance scores are based on the similarity of the
query to the extracted segment. You can specify that extractive segments be
returned with relevance scores. Scores range from -1.0 (less relevant) to 1.0
(more relevant). Turning on relevance scores can increase latency.
Adjacent segments
: You can set
numPreviousSegments
and
numNextSegments
to get up to 3 segments from immediately before and
after the relevant segment. Adjacent segments can add context and accuracy to
the relevant segment.
Turning on adjacent segments can increase latency.
Get extractive segments
The following steps show how to get extractive segments for unstructured data.
You can follow similar steps to get extractive segments for website data.
Send a search request that uses
ContentSearchSpec.extractiveContentSpec
to specify
maxExtractiveSegmentCount
.
The following example of
extractiveContentSpec
specifies that one
segment can be returned for each search result.
"contentSearchSpec"
:
{
"extractiveContentSpec"
:
{
"maxExtractiveSegmentCount"
:
1
}
}
maxExtractiveSegmentCount
: The number of extractive segments to return
for each search result. The default value is 0 and the maximum is 10.
Additional options:
returnExtractiveSegmentScore
: Set to
true
to return
a relevance score with each segment returned.
numPreviousSegments
: The number of adjacent segments
to return before the relevant segment. The default value is 0 and the
maximum is 3. Using adjacent segments can increase latency.
numNextSegments
: The number of adjacent segments to
return after the relevant segment. The default value is 0 and the
maximum is 3. Using adjacent segments can increase latency.
For more information about these options, see
Extractive segment
options
.
Get segments from the search response. Segments are returned with each search
result in
extractive_segments
.
In this example of a document that was returned as one of the results in a
search response, a segment was included with the result:
{
"id"
:
"54321"
,
"document"
:
{
"name"
:
"projects/123/locations/global/collections/default_collection/dataStores/example-datastore/branches/0/documents/54321"
,
"id"
:
"54321"
,
"derivedStructData"
:
{
"extractive_segments"
:
[
{
"pageNumber"
:
"2"
,
"content"
:
"Client\nGoogle Toolbar. Google Toolbar is a free application that adds a Google search box to web browsers (Internet\nExplorer and Firefox) and improves user web experience through features such as a pop-up blocker that blocks\npop-up advertising, an autofill feature that completes web forms with information saved on a user's computer, and\ncustomizable buttons that let users search their favorite web sites and stay updated on their favorite feeds.\n\nGoogle Chrome. Google Chrome is an open-source browser that combines a minimal design with\ntechnologies to make the web faster, safer, and easier to navigate.\nGoogle Pack. Google Pack is a free collection of safe, useful software programs from Google and other\ncompanies that improve the user experience online and on the desktop. It includes programs that help users\nbrowse the web faster, remove spyware and viruses.\n\nPicasa. Picasa is a free service that allows users to view, manage and share their photos. Picasa enables users\nto import, organize and edit their photos, and upload them to Picasa Web Albums where the photos can be shared\nwith others on the internet.\n\nGoogle Desktop. Google Desktop lets people perform a full-text search on the contents of their own\ncomputer, including email, files, instant messenger chats and web browser history. Users can view web pages they\nhave visited even when they are not online. Google Desktop also includes a customizable Sidebar that includes\nmodules for weather, stock tickers and news.\n\n5"
}
],
"link"
:
"gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs/2004Q4_earnings_google.pdf"
}
}
}
pageNumber
: If page numbers can be extracted from the document, this
field indicates where the answer was extracted from.
content
: The content of the extractive segment.
What's next
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

