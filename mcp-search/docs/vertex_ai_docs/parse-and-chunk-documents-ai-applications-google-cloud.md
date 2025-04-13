# Parse and chunk documents  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents](https://cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents)

Home
AI Applications
Documentation
Guides
Send feedback
Parse and chunk documents
Stay organized with collections
Save and categorize content based on your preferences.
This page describes how to use Vertex AI Search to parse and chunk your
documents.
You can configure parsing or chunking settings in order to:
Specify how Vertex AI Search parses content.
You can specify how
to parse unstructured content when you upload it to Vertex AI Search.
Vertex AI Search provides a digital parser, OCR parser for
PDFs, and a layout parser. You can also bring your own parsed
documents. The layout parser is recommended when you have rich content and
structural elements like sections, paragraphs, tables, lists to be extracted
from documents for search and answer generation.
See
Improve content detection with parsing
.
Use Vertex AI Search for retrieval-augmented generation (RAG).
Improve the output of LLMs with relevant data that you've uploaded to your
Vertex AI Search app. To do this, you'll turn on document chunking,
which indexes your data as chunks to improve relevance and decrease
computational load for LLMs. You'll also turn on the layout parser, which
detects document elements such as headings and lists, to improve how documents
are chunked.
For information about chunking for RAG and how to return chunks in search
requests, see
Chunk documents for RAG
.
Parse documents
You can control content parsing in the following ways:
Specify parser type.
You can specify the type of parsing to apply
depending on file type:
Digital parser.
The digital parser is on by default for all file types
unless a different parser type is specified. The digital parser processes
ingested documents if no other default parser is specified for the data
store or if the specified parser doesn't support the file type of an
ingested document.
OCR parsing for PDFs
. If you plan to upload scanned PDFs or PDFs with
text inside images, you can turn on the OCR parser to improve PDF indexing.
See the
OCR parser for PDFs
section of this document.
Layout parser.
Turn on the layout parser for HTML, PDF,
or DOCX files if you plan to use Vertex AI Search for RAG. See
Chunk documents for RAG
for information about this
parser and how to turn it on.
Bring your own parsed document.
(Preview with allowlist) If you've already
parsed your unstructured documents, you can import that pre-parsed content
into Vertex AI Search. See
Bring your own parsed
document
.
Parser availability comparison
The following table lists the availability of each parser by document file
types and shows which elements each parser can detect and parse.
File type
Digital parser
OCR parser
Layout parser
HTML
Detects paragraph elements
Not applicable
Detects paragraph, table, list, title, and heading elements
PDF
Detects paragraph (digital text) elements
Detects paragraph elements
Detects paragraph, table, title, and heading elements
DOCX (
Preview
)
Detects paragraph elements
Not applicable
Detects paragraph, table, list, title, heading elements
PPTX (
Preview
)
Detects paragraph elements
Not applicable
Detects paragraph, table, list, title, heading elements
TXT
Detects paragraph elements
Not applicable
Not applicable
XLSX (
Preview
)
Detects paragraph elements
Not applicable
Detects paragraph, table, title, heading elements
Digital parser
The digital parser extracts machine-readable text from documents. It detects
text blocks, but not document elements such as tables, lists, and headings.
The digital parser is used as the default if you don't specify a different
parser as the default during data store creation or if a specified parser
doesn't support a file type that's being uploaded.
OCR parser for PDFs
If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images,
such as infographics) Google recommends turning on optical character recognition
(OCR) processing during data store creation. This allows
Vertex AI Search to extract paragraph elements.
If you have searchable PDFs or other digital formats that are mostly composed of
machine-readable text, you typically don't need to use the OCR parser. However,
if you have PDFs that have both non-searchable text (such as scanned text or
infographics) and machine-readable text, you can set the field
useNativeText
to true when specifying the OCR parser. In this case, machine-readable text is
merged with OCR parsing outputs to improve text extraction quality.
OCR processing features are available for generic search apps with
unstructured data stores.
The OCR processor can parse a maximum of 500 pages per PDF file. For longer
PDFs, the OCR processor parses the first 500 pages and the default parser parses
the rest.
Layout parser
Layout parsing lets Vertex AI Search detect layouts for PDF and HTML.
Support for DOCX files is in Preview. Vertex AI Search can then
identify content elements like text blocks, tables, lists, and structural
elements such as titles and headings and use them to define the organization and
hierarchy of a document.
You can either turn on layout parsing for all file types or specify which file
types to turn it on for. The layout parser detects content elements like
paragraphs, tables, lists, and structural elements like titles, headings,
headers, footnotes.
The layout parser is available only when using document chunking for RAG. When
document chunking is turned on, Vertex AI Search breaks documents up
into chunks at ingestion time and can return documents as chunks. Detecting
document layout enables content-aware chunking and enhances search and answer
generation related to document elements. For more information about chunking
documents for RAG, see
Chunk documents for RAG
.
Specify a default parser
By including the
documentProcessingConfig
object
when you create a data store, you can specify a default parser for that data
store. If you don't include
documentProcessingConfig.defaultParsingConfig
, the
digital parser is used. The digital parser is also used if the specified parser
is not available for a file type.
REST
To specify a default parser:
When
creating a search data store
using the API,
include
documentProcessingConfig.defaultParsingConfig
in the data store
creation request. You can specify the OCR parser, the layout parser, or the
digital parser:
To specify the OCR parser for PDFs:
"documentProcessingConfig"
:
{
"defaultParsingConfig"
:
{
"ocrParsingConfig"
:
{
"useNativeText"
:
"
NATIVE_TEXT_BOOLEAN
"
}
}
}
NATIVE_TEXT_BOOLEAN
is optional. Set it only if
you're ingesting PDFs. If set to
true
, this turns on machine-readable
text processing for the OCR parser. The default is
false
.
To specify the layout parser:
"documentProcessingConfig"
:
{
"defaultParsingConfig"
:
{
"layoutParsingConfig"
:
{}
}
}
To specify the digital parser:
"documentProcessingConfig"
:
{
"defaultParsingConfig"
:
{
"digitalParsingConfig"
:
{}
}
}
Example
The following example specifies during data store creation that the OCR parser
will be the default parser. Because the OCR parser only applies to PDF files,
all PDF files that are ingested will be processed by the OCR parser, and any
other file types will be processed by the digital parser.
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
"X-Goog-User-Project: exampleproject"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/exampleproject/locations/global/collections/default_collection/dataStores?dataStoreId=datastore123"
\
-d
'{
"displayName": "exampledatastore",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
"contentConfig": "CONTENT_REQUIRED",
"documentProcessingConfig": {
"defaultParsingConfig": {
"ocrParsingConfig": {
"useNativeText": "false"
}
}
}
}'
Specify parser overrides for file types
You can specify that a particular file type (PDF, HTML, or DOCX) should be parsed
by a different parser than the default parser. To do so, include the
documentProcessingConfig
field
in your data store creation request and specify the override parser. If you
don't specify a default parser, then the digital parser is the default.
REST
To specify a file-type-specific parser override:
When
creating a search data store
using the API,
include
documentProcessingConfig.defaultParsingConfig
in the data store
creation request.
You can specify a parser for
pdf
,
html
, or
docx
:
"documentProcessingConfig"
:
{
"parsingConfigOverrides"
:
{
"
FILE_TYPE
"
:
{
PARSING_CONFIG
},
}
}
Replace the following:
FILE_TYPE
: Accepted values are
pdf
,
html
, and
docx
.
PARSING_CONFIG
: Specify the configuration for the parser
that you want to apply to the file type. You can specify the OCR parser, the
layout parser, or the digital parser:
To specify the OCR parser for PDFs:
"ocrParsingConfig"
:
{
"useNativeText"
:
"
NATIVE_TEXT_BOOLEAN
"
}
NATIVE_TEXT_BOOLEAN
: Optional. Set only if you're
ingesting PDFs. If set to
true
, this turns on machine-readable
text processing for the OCR parser. The default is
false
.
To specify the layout parser:
"layoutParsingConfig"
:
{}
To specify the digital parser:
"documentProcessingConfig"
:
{
"defaultParsingConfig"
:
{
"digitalParsingConfig"
:
{}
}
}
Example
The following example specifies during data store creation that PDF files should
be processed by the OCR parser and that HTML files should be processed by the
layout parser. In this case, any files other than PDF and HTML files would be
processed by the digital parser.
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
"X-Goog-User-Project: exampleproject"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/exampleproject/locations/global/collections/default_collection/dataStores?dataStoreId=datastore123"
\
-d
'{
"displayName": "exampledatastore",
"industryVertical": "GENERIC",
"solutionTypes": ["SOLUTION_TYPE_SEARCH"],
"contentConfig": "CONTENT_REQUIRED",
"documentProcessingConfig": {
"parsingConfigOverrides": {
"pdf": {
"ocrParsingConfig": {
"useNativeText": "false"
},
},
"html": {
"layoutParsingConfig": {}
}
}
}
}'
Get parsed documents in JSON
You can get a parsed document in JSON format by calling the
getProcessedDocument
method and specifying
PARSED_DOCUMENT
as the processed
document type. Getting parsed documents in JSON can be helpful if you need to
upload the parsed document elsewhere or if you decide to re-import parsed
documents to AI Applications using the
bring your own parsed
document
feature.
REST
To get parsed documents in JSON, follow this step:
Call the
getProcessedDocument
method:
curl
-X
GET
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents/
DOCUMENT_ID
:getProcessedDocument?processed_document_type=PARSED_DOCUMENT"
Replace the following:
PROJECT_ID
: The ID of your project.
DATA_STORE_ID
: The ID your data store.
DOCUMENT_ID
: The ID of the document to get.
Bring your own parsed document
You can import pre-parsed, unstructured documents into
Vertex AI Search data stores. For example, instead of importing a raw
PDF document, you can parse the PDF yourself and import the parsing result
instead. This lets you import your documents in a structured way, ensuring
that search and answer generation have information about the document's layout
and elements.
A parsed, unstructured document is represented by JSON that describes the
unstructured document using a sequence of text, table, and list blocks. You
import JSON files with your parsed unstructured document data in the same way
that you import other types of unstructured documents, such as PDFs. When this
feature is turned on, whenever a JSON file is uploaded and identified by either
an
application/json
MIME type or a .JSON extension, it is treated as a
parsed document.
To turn on this feature and for information about how to use it, contact your
Google account team.
Chunk documents for RAG
By default, Vertex AI Search is optimized for document retrieval, where
your search app returns a document such as a PDF or web page with each search
result.
Document chunking features are available for generic search apps with
unstructured data stores.
Vertex AI Search can instead be optimized for RAG, where your search
app is primarily used to augment LLM output with your custom data. When document
chunking is turned on, Vertex AI Search breaks up your documents into
chunks. In search results, your search app can return relevant chunks of data
instead of full documents. Using chunked data for RAG increases relevance for
LLM answers and reduces computational load for LLMs.
To use Vertex AI Search for RAG:
Turn on document chunking
when you create your data
store.
Alternatively,
upload your own chunks
(Preview with
allowlist) if you've already chunked your own documents.
Retrieve and view chunks in the following ways:
List chunks from a document
Get chunks in JSON from a processed document
Get specific chunks
Return chunks in search requests
.
Limitations
The following limitations apply to chunking:
Document chunking can't be turned on or off after data store creation.
You can make search requests for documents instead of chunks from a data store
with document chunking turned on. However, data stores with document chunking
turned on aren't optimized for returning documents. Documents are returned by
aggregating chunks into documents.
When document chunking is turned on, search summaries and search with
follow-ups are supported in Public preview but not supported as GA.
Document chunking options
This section describes the options that you specify in order to turn on
document chunking.
During data store creation, turn on the following options so that
Vertex AI Search can index your documents as chunks.
Layout-aware document chunking.
To turn this option on, include the
documentProcessingConfig
field in your data store creation request and specify
ChunkingConfig.LayoutBasedChunkingConfig
.
When layout-aware document chunking is turned on, Vertex AI Search
detects a document's layout and take it into account during chunking. This
improves semantic coherence and reduces noise in the content when it's used
for retrieval and LLM generation. All text in a chunk will come from the
same layout entity, such as headings, subheadings, and lists.
Layout parsing.
To turn this option on, specify
ParsingConfig.LayoutParsingConfig
during data store creation.
The layout parser detect layouts for PDF, HTML, and DOCX files. It identifies
elements like text blocks, tables, lists, titles, and headings, and uses them
to define the organization and hierarchy of a document.
For more about layout parsing, see
Layout parsing
.
Turn on document chunking
You can turn on document chunking by including
the
documentProcessingConfig
object
in your data store creation request and turning on layout-aware document
chunking and layout parsing.
REST
To turn on document chunking:
When
creating a search data store
using the API,
include the
documentProcessingConfig.chunkingConfig
object in the data store
creation request.
"documentProcessingConfig"
:
{
"chunkingConfig"
:
{
"layoutBasedChunkingConfig"
:
{
"chunkSize"
:
CHUNK_SIZE_LIMIT
,
"includeAncestorHeadings"
:
HEADINGS_BOOLEAN
,
}
},
"defaultParsingConfig"
:
{
"layoutParsingConfig"
:
{}
}
}
Replace the following:
CHUNK_SIZE_LIMIT
: Optional. The token size limit for
each chunk. The default value is 500. Supported values are 100-500
(inclusive).
HEADINGS_BOOLEAN
: Optional. Determines whether headings
are included in each chunk. The default value is
false
. Appending title
and headings at all levels to chunks from the middle of the document can
help prevent context loss in chunk retrieval and ranking.
Bring your own chunks (Preview with allowlist)
If you've already chunked your own documents, you can upload those to
Vertex AI Search instead of turning on document chunking options.
Bringing your own chunks is a Preview with allowlist feature. To use this
feature, contact your Google account team.
List a document's chunks
To list all chunks for a specific document, call the
Chunks.list
method.
REST
To list chunks for a document, follow this step:
Call the
Chunks.list
method:
curl
-X
GET
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents/
DOCUMENT_ID
/chunks"
Replace the following:
PROJECT_ID
: The ID of your project.
DATA_STORE_ID
: The ID your data store.
DOCUMENT_ID
: The ID of the document to list chunks from.
Get chunks in JSON from a processed document
You can get all the chunks from a specific document in JSON format by calling
the
getProcessedDocument
method. Getting chunks in JSON can be helpful if you
need to upload chunks elsewhere or if you decide to re-import chunks to
AI Applications using the
bring your own chunks
feature.
REST
To get JSON chunks for a document, follow this step:
Call the
getProcessedDocument
method:
curl
-X
GET
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents/
DOCUMENT_ID
/chunks:getProcessedDocument?processed_document_type=CHUNKED_DOCUMENT"
Replace the following:
PROJECT_ID
: The ID of your project.
DATA_STORE_ID
: The ID your data store.
DOCUMENT_ID
: The ID of the document to get chunks
from.
Get specific chunks
To get a specific chunk, call the
Chunks.get
method.
REST
To get a specific chunk, follow this step:
Call the
Chunks.get
method:
curl
-X
GET
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
/branches/0/documents/
DOCUMENT_ID
/chunks/
CHUNK_ID
"
Replace the following:
PROJECT_ID
: The ID of your project.
DATA_STORE_ID
: The ID your data store.
DOCUMENT_ID
: The ID of the document that the chunk is from.
CHUNK_ID
: The ID of the chunk to return.
Return chunks in search requests
After you've confirmed that your data has been chunked correctly, your
Vertex AI Search can return chunked data in its search results.
The response returns a chunk that is relevant to the search query. In addition,
you can choose to return adjacent chunks that appear before and after the
relevant chunk in the source document. Adjacent chunks can add context and
accuracy.
REST
To get chunked data:
When making a search request, specify
ContentSearchSpec.SearchResultMode
as
chunks
.
co
ntent
SearchSpec
": {
"
searchResul
t
Mode
": "
RESULT_MODE
",
"
chu
n
kSpec
": {
"
nu
mPreviousChu
n
ks
":
NUMBER_OF_PREVIOUS_CHUNKS
,
"
nu
mNex
t
Chu
n
ks":
NUMBER_OF_NEXT_CHUNKS
}
}
RESULT_MODE
: Determines whether search results are returned
as full documents or in chunks. To get chunks, the data store must
have document chunking turned on. Accepted values are
documents
and
chunks
. If document chunking is turned on for your data store, the
default value is
chunks
.
NUMBER_OF_PREVIOUS_CHUNKS
: The number of chunks to return
that immediately preceded the relevant chunk. The maximum allowed value
is 5.
NUMBER_OF_NEXT_CHUNKS
: The number of chunks to return
that immediately follow the relevant chunk. The maximum allowed value is
5.
Example
The following example of a search query request sets
SearchResultMode
to
chunks
, requests one previous chunk and one next chunk, and limits the number
of results to a single relevant chunk using
pageSize
.
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
"X-Goog-User-Project: exampleproject"
\
"https://discoveryengine.googleapis.com/v1alpha/projects/exampleproject/locations/global/collections/default_collection/dataStores/datastore123/servingConfigs/default_search:search"
\
-d
'{
"query": "animal",
"pageSize": 1,
"contentSearchSpec": {
"searchResultMode": "CHUNKS",
"chunkSpec": {
"numPreviousChunks": 1,
"numNextChunks": 1
}
}
}'
The following example shows the response that is returned for the example query.
The response contains the relevant chunks, the previous and next chunks, the
original document's metadata, and the span of document pages that each chunk was
derived from.
Response
{
"results"
:
[
{
"chunk"
:
{
"name"
:
"projects/961309680810/locations/global/collections/default_collection/dataStores/allie-pdf-adjacent-chunks_1711394998841/branches/0/documents/0d8619f429d7f20b3575b14cd0ad0813/chunks/c17"
,
"id"
:
"c17"
,
"content"
:
"\n# ESS10: Stakeholder Engagement and Information Disclosure\nReaders should also refer to ESS10 and its guidance notes, plus the template available for a stakeholder engagement plan. More detail on stakeholder engagement in projects with risks related to animal health is contained in section 4 below. The type of stakeholders (men and women) that can be engaged by the Borrower as part of the project's environmental and social assessment and project design and implementation are diverse and vary based on the type of intervention. The stakeholders can include: Pastoralists, farmers, herders, women's groups, women farmers, community members, fishermen, youths, etc. Cooperatives members, farmer groups, women's livestock associations, water user associations, community councils, slaughterhouse workers, traders, etc. Veterinarians, para-veterinary professionals, animal health workers, community animal health workers, faculties and students in veterinary colleges, etc. 8 \n# 4. Good Practice in Animal Health Risk Assessment and Management\n\n# Approach\nRisk assessment provides the transparent, adequate and objective evaluation needed by interested parties to make decisions on health-related risks associated with project activities involving live animals. As the ESF requires, it is conducted throughout the project cycle, to provide or indicate likelihood and impact of a given hazard, identify factors that shape the risk, and find proportionate and appropriate management options. The level of risk may be reduced by mitigation measures, such as infrastructure (e.g., diagnostic laboratories, border control posts, quarantine stations), codes of practice (e.g., good animal husbandry practices, on-farm biosecurity, quarantine, vaccination), policies and regulations (e.g., rules for importing live animals, ban on growth hormones and promotors, feed standards, distance required between farms, vaccination), institutional capacity (e.g., veterinary services, surveillance and monitoring), changes in individual behavior (e.g., hygiene, hand washing, care for animals). Annex 2 provides examples of mitigation practices. This list is not an exhaustive one but a compendium of most practiced interventions and activities. The cited measures should take into account social, economic, as well as cultural, gender and occupational aspects, and other factors that may affect the acceptability of mitigation practices by project beneficiaries and other stakeholders. Risk assessment is reviewed and updated through the project cycle (for example to take into account increased trade and travel connectivity between rural and urban settings and how this may affect risks of disease occurrence and/or outbreak). Projects monitor changes in risks (likelihood and impact) b by using data, triggers or indicators. "
,
"documentMetadata"
:
{
"uri"
:
"gs://table_eval_set/pdf/worldbank/AnimalHealthGoodPracticeNote.pdf"
,
"title"
:
"AnimalHealthGoodPracticeNote"
},
"pageSpan"
:
{
"pageStart"
:
14
,
"pageEnd"
:
15
},
"chunkMetadata"
:
{
"previousChunks"
:
[
{
"name"
:
"projects/961309680810/locations/global/collections/default_collection/dataStores/allie-pdf-adjacent-chunks_1711394998841/branches/0/documents/0d8619f429d7f20b3575b14cd0ad0813/chunks/c16"
,
"id"
:
"c16"
,
"content"
:
"\n# ESS6: Biodiversity Conservation and Sustainable Management of Living Natural Resources\nThe risks associated with livestock interventions under ESS6 include animal welfare (in relation to housing, transport, and slaughter); diffusion of pathogens from domestic animals to wildlife, with risks for endemic species and biodiversity (e.g., sheep and goat plague in Mongolia affecting the saiga, an endemic species of wild antelope); the introduction of new breeds with potential risk of introducing exotic or new diseases; and the release of new species that are not endemic with competitive advantage, potentially putting endemic species at risk of extinction. Animal welfare relates to how an animal is coping with the conditions in which it lives. An animal is in a good state of welfare if it is healthy, comfortable, well nourished, safe, able to express innate behavior, 7 Good Practice Note - Animal Health and related risks and is not suffering from unpleasant states such as pain, fear or distress. Good animal welfare requires appropriate animal care, disease prevention and veterinary treatment; appropriate shelter, management and nutrition; humane handling, slaughter or culling. The OIE provides standards for animal welfare on farms, during transport and at the time of slaughter, for their welfare and for purposes of disease control, in its Terrestrial and Aquatic Codes. The 2014 IFC Good Practice Note: Improving Animal Welfare in Livestock Operations is another example of practical guidance provided to development practitioners for implementation in investments and operations. Pastoralists rely heavily on livestock as a source of food, income and social status. Emergency projects to restock the herds of pastoralists affected by drought, disease or other natural disaster should pay particular attention to animal welfare (in terms of transport, access to water, feed, and animal health) to avoid potential disease transmission and ensure humane treatment of animals. Restocking also entails assessing the assets of pastoralists and their ability to maintain livestock in good conditions (access to pasture and water, social relationship, technical knowledge, etc.). Pastoralist communities also need to be engaged by the project to determine the type of animals and breed and the minimum herd size to be considered for restocking. \n# Box 5. Safeguarding the welfare of animals and related risks in project activities\nIn Haiti, the RESEPAG project (Relaunching Agriculture: Strengthening Agriculture Public Services) financed housing for goats and provided technical recommendations for improving their welfare, which is critical to avoid the respiratory infections, including pneumonia, that are serious diseases for goats. To prevent these diseases, requires optimal sanitation and air quality in herd housing. This involves ensuring that buildings have adequate ventilation and dust levels are reduced to minimize the opportunity for infection. Good nutrition, water and minerals are also needed to support the goats' immune function. The project paid particular attention to: (i) housing design to ensure good ventilation; (ii) locating housing close to water sources and away from human habitation and noisy areas; (iii) providing mineral blocks for micronutrients; (iv) ensuring availability of drinking water and clean food troughs. "
,
"documentMetadata"
:
{
"uri"
:
"gs://table_eval_set/pdf/worldbank/AnimalHealthGoodPracticeNote.pdf"
,
"title"
:
"AnimalHealthGoodPracticeNote"
},
"pageSpan"
:
{
"pageStart"
:
13
,
"pageEnd"
:
14
}
}
],
"nextChunks"
:
[
{
"name"
:
"projects/961309680810/locations/global/collections/default_collection/dataStores/allie-pdf-adjacent-chunks_1711394998841/branches/0/documents/0d8619f429d7f20b3575b14cd0ad0813/chunks/c18"
,
"id"
:
"c18"
,
"content"
:
"\n# Scoping of risks\nEarly scoping of risks related to animal health informs decisions to initiate more comprehensive risk assessment according to the type of livestock interventions and activities. It can be based on the following considerations: • • • • Type of livestock interventions supported by the project (such as expansion of feed resources, improvement of animal genetics, construction/upgrading and management of post-farm-gate facilities, etc. – see also Annex 2); Geographic scope and scale of the livestock interventions; Human and animal populations that are likely to be affected (farmers, women, children, domestic animals, wildlife, etc.); and Changes in the project or project context (such as emerging disease outbreak, extreme weather or climatic conditions) that would require a re-assessment of risk levels, mitigation measures and their likely effect on risk reduction. Scenario planning can also help to identify project-specific vulnerabilities, country-wide or locally, and help shape pragmatic analyses that address single or multiple hazards. In this process, some populations may be identified as having disproportionate exposure or vulnerability to certain risks because of occupation, gender, age, cultural or religious affiliation, socio-economic or health status. For example, women and children may be the main caretakers of livestock in the case of 9 Good Practice Note - Animal Health and related risks household farming, which puts them into close contact with animals and animal products. In farms and slaughterhouses, workers and veterinarians are particularly exposed, as they may be in direct contact with sick animals (see Box 2 for an illustration). Fragility, conflict, and violence (FCV) can exacerbate risk, in terms of likelihood and impact. Migrants new to a geographic area may be immunologically naïve to endemic zoonotic diseases or they may inadvertently introduce exotic diseases; and refugees or internally displaced populations may have high population density with limited infrastructure, leaving them vulnerable to disease exposure. Factors such as lack of access to sanitation, hygiene, housing, and health and veterinary services may also affect disease prevalence, contributing to perpetuation of poverty in some populations. Risk assessment should identify populations at risk and prioritize vulnerable populations and circumstances where risks may be increased. It should be noted that activities that seem minor can still have major consequences. See Box 6 for an example illustrating how such small interventions in a project may have large-scale consequences. It highlights the need for risk assessment, even for simple livestock interventions and activities, and how this can help during the project cycle (from concept to implementation). "
,
"documentMetadata"
:
{
"uri"
:
"gs://table_eval_set/pdf/worldbank/AnimalHealthGoodPracticeNote.pdf"
,
"title"
:
"AnimalHealthGoodPracticeNote"
},
"pageSpan"
:
{
"pageStart"
:
15
,
"pageEnd"
:
16
}
}
]
}
}
}
],
"totalSize"
:
61
,
"attributionToken"
:
"jwHwjgoMCICPjbAGEISp2J0BEiQ2NjAzMmZhYS0wMDAwLTJjYzEtYWQxYS1hYzNlYjE0Mzc2MTQiB0dFTkVSSUMqUMLwnhXb7Ygtq8SKLa3Eii3d7Ygtj_enIqOAlyLm7Ygtt7eMLduPmiKN96cijr6dFcXL8xfdj5oi9-yILdSynRWCspoi-eyILYCymiLk7Ygt"
,
"nextPageToken"
:
"ANxYzNzQTMiV2MjFWLhFDZh1SMjNmMtADMwATL5EmZyMDM2YDJaMQv3yagQYAsciPgIwgExEgC"
,
"guidedSearchResult"
:
{},
"summary"
:
{}
}
What's next
Create a search data store
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
"documentProcessingConfig": {
  "defaultParsingConfig": {
    "ocrParsingConfig": {
      "useNativeText": "NATIVE_TEXT_BOOLEAN"
    }
  }
}

```

### Code Example 2 (text)

```text
"documentProcessingConfig": {
  "defaultParsingConfig": {
    "layoutParsingConfig": {}
  }
}

```

### Code Example 3 (text)

```text
 "documentProcessingConfig": {
    "defaultParsingConfig": { "digitalParsingConfig": {} }
 }

```

### Code Example 4 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: exampleproject" \
"https://discoveryengine.googleapis.com/v1alpha/projects/exampleproject/locations/global/collections/default_collection/dataStores?dataStoreId=datastore123" \
-d '{
  "displayName": "exampledatastore",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
  "contentConfig": "CONTENT_REQUIRED",
  "documentProcessingConfig": {
    "defaultParsingConfig": {
      "ocrParsingConfig": {
        "useNativeText": "false"
      }
    }
  }
}'

```

### Code Example 5 (text)

```text
"documentProcessingConfig": {
  "parsingConfigOverrides": {
    "FILE_TYPE": { PARSING_CONFIG },
  }
 }

```

### Code Example 6 (text)

```text
"ocrParsingConfig": {
  "useNativeText": "NATIVE_TEXT_BOOLEAN"
}

```

### Code Example 7 (text)

```text
"layoutParsingConfig": {}

```

### Code Example 8 (text)

```text
"documentProcessingConfig": {
  "defaultParsingConfig": { "digitalParsingConfig": {} }
}

```

### Code Example 9 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: exampleproject" \
"https://discoveryengine.googleapis.com/v1alpha/projects/exampleproject/locations/global/collections/default_collection/dataStores?dataStoreId=datastore123" \
-d '{
  "displayName": "exampledatastore",
  "industryVertical": "GENERIC",
  "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
  "contentConfig": "CONTENT_REQUIRED",
  "documentProcessingConfig": {
    "parsingConfigOverrides": {
      "pdf": {
        "ocrParsingConfig": {
            "useNativeText": "false"
          },
      },
      "html": {
         "layoutParsingConfig": {}
      }
    }
  }
}'

```

### Code Example 10 (text)

```text
curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID:getProcessedDocument?processed_document_type=PARSED_DOCUMENT"

```

### Code Example 11 (text)

```text
 "documentProcessingConfig": {
   "chunkingConfig": {
       "layoutBasedChunkingConfig": {
           "chunkSize": CHUNK_SIZE_LIMIT,
           "includeAncestorHeadings": HEADINGS_BOOLEAN,
       }
   },
   "defaultParsingConfig": {
     "layoutParsingConfig": {}
   }
 }

```

### Code Example 12 (text)

```text
curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID/chunks"

```

### Code Example 13 (text)

```text
curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID/chunks:getProcessedDocument?processed_document_type=CHUNKED_DOCUMENT"

```

### Code Example 14 (text)

```text
curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID/chunks/CHUNK_ID"

```

### Code Example 15 (text)

```text
contentSearchSpec": {
  "searchResultMode": "RESULT_MODE",
  "chunkSpec": {
       "numPreviousChunks": NUMBER_OF_PREVIOUS_CHUNKS,
       "numNextChunks": NUMBER_OF_NEXT_CHUNKS
   }
}

```

### Code Example 16 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: exampleproject" \
"https://discoveryengine.googleapis.com/v1alpha/projects/exampleproject/locations/global/collections/default_collection/dataStores/datastore123/servingConfigs/default_search:search" \
-d '{
  "query": "animal",
  "pageSize": 1,
  "contentSearchSpec": {
    "searchResultMode": "CHUNKS",
    "chunkSpec": {
           "numPreviousChunks": 1,
           "numNextChunks": 1
       }
  }
}'

```

