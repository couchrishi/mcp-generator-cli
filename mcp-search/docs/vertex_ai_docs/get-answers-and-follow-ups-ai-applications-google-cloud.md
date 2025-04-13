# Get answers and follow-ups  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/answer#search-answer-basic-python](https://cloud.google.com/generative-ai-app-builder/docs/answer#search-answer-basic-python)

Home
AI Applications
Documentation
Guides
Send feedback
Get answers and follow-ups
Stay organized with collections
Save and categorize content based on your preferences.
This page introduces search with answer and follow-ups for Vertex AI Search and
shows you how to implement it for generic search apps using method calls.
Search with answer and follow-ups is based on the answer method. The answer method
replaces the summarization features of the older
search
method
and all of the features of the deprecated
converse
method.
The answer method also has some important additional features, such as the
ability to handle complex queries.
Features of the answer method
Key features of the answer method are as follows:
The ability to generate answers to complex queries. For example, the answer
method can break down compound queries, such as the following,
into multiple, smaller queries to return better results that are used to
power better answers:
"What is Google Cloud and Google Ads respective revenue in 2024?"
"After how many years since its founding, did Google reach 1 billion USD
revenue?"
The ability to combine search and answer generation in a multi-turn
conversation by calling the answer method in each turn.
The ability to pair with the search method to reduce search latency. You
can call the search method and the answer method separately and render
the search results and answers in different iframes at different times. This
means that you can show your users search results (the 10 blue links) within
milliseconds. You don't need to wait for answers to be generated before you
can show search results.
The features of answer and follow-ups can be divided into three phases of the query,
search and answer:
Query phase features
Search phase features
Answer phase features
When to use answer and when to use search
Vertex AI Search has two methods that are used for querying apps. They have different but
overlapping features.
Use the
answer
method when:
You want an AI generated answer (or summary) of the search results.
You want multi-turn searching, that is, searches that hold context so allow
for follow-up questions.
Use the
search
method when:
You only need search results; not a generated answer.
You have any of the following:
Media or healthcare data
Your own embeddings
Synonym or redirect controls
Facets
User country codes
Use the answer and search methods together when:
You want to return more than ten search results,
and
you want a generated
answer.
You have latency issues and want to return and display search results quickly
before the generated answer is returned.
Query phase features
The answer and follow-ups feature supports natural language query processing.
This section describes and illustrates the various options for query rephrasing and classification.
Query rephrasing
Query rephrasing is on by default. This feature chooses the best way to rephrase
queries automatically to improve search results. This feature can also handle
queries that don't require rephrasing.
Break down complex queries into multiple queries and perform synchronous
sub-querying.
For example: A complex query is broken down into four smaller, simpler
queries.
User input
Sub-queries created from the complex query
What jobs and hobbies do Andie Ram and Arnaud
Clément have in common?
Andie Ram occupation
Arnaud Clément occupation
Andie Ram hobby
Arnaud Clément hobby
Synthesize multi-turn queries, to make follow-up questions context aware
and stateful.
For example: Queries synthesized from user input at each turn might look
like this:
User input
Query synthesized
Turn 1: laptops for school
laptops for school
Turn 2: not mac
laptops for school not mac
Turn 3: bigger screen and i also need wireless keyboard and
mouse
bigger screen laptops for school not mac with wireless keyboard and
mouse
Turn 4: and a backpack for it
bigger screen laptops for school not mac with wireless keyboard and
mouse and a backpack for it
Simplify long queries to improve retrieval.
For example: A long query is shortened to a simple query.
User input
Query simplified
I am trying to find out why the \"Add to Cart\"
button on our website is not working properly. It seems that when a
user clicks the button, the item is not added to the cart and they
receive an error message. I have checked the code and it seems to be
correct, so I am not sure what the issue could be. Can you help me
troubleshoot this problem?
"Add to Cart" button not working on website.
Perform multi-step reasoning
Multi-step reasoning is based on the ReAct (reason + act) paradigm which
enables LLMs to solve complex tasks using natural language reasoning.
By default, the maximum number of steps is five.
For example:
User input
Two steps to generate the answer
After how many years since its founding, did Google reach 1
billion USD revenue?
Step 1:
[Thought]: I need to know when Google was founded, then I can query it is revenue since then.
[Act] Search: When was Google founded?[Observe Search Results]: "1998"
Step 2:
[Thought]: Now I need to Google's yearly revenue
since 1998, and find out when it exceeded 1 billion for the first time.
[Act] Search: Google revenue since 1998
[Observe Search Results] Google revenue in 1998, Google revenue in 1999…..
[Answer]: Google reached more than 1 billion USD
revenue in 2003 [1], 5 years after its founding in 1998[2].
Query classification
Query classification options are to identify adversarial queries and non-answer
seeking queries. By default, query classification options are off.
For more information about adversarial and non-answer seeking queries, see
Ignore adversarial
queries
and
Ignore non-summary seeking
queries
.
Search phase features
For searching, the answer method has the same options as the search method. For
example:
Applying filters to restrict search to specific documents. For more
information, see
Filter generic search for structured or unstructured data
.
Applying SafeSearch to filter out explicit content, such as violence and
pornography. For more
information, see
Safety settings for Vertex AI Search
.
Specifying boost conditions to promote or demote documents returned by search. For more
information, see
Boost search results
.
Answer phase features
During the answer phase, when answers are generated from the search results, you
can enable the same features as in the search method. For example:
Getting citations to indicate a
source for each sentence in the answer. For more
information, see
Include citations
.
Use the prompt preamble to customize the answer for such things as tone, style,
and verbosity.
For more information, see
Specify a custom preamble
.
Choose which Vertex AI model to use for answer generation.
For more information, see
Answer generation model versions and
lifecycle
.
Choose whether to ignore queries that have been classified as adversarial or
non-answer seeking.
For more information about adversarial and non-answer seeking queries, see
Ignore adversarial queries
and
Ignore
non-summary seeking queries
. Non-answer
seeking queries are also called non-summary seeking queries.
Additional answer phase features that are not available in the search method
are:
Getting a support score for each claim (sentence in the generated answer).
A support score is a floating point value in the range [0,1] that
indicates how grounded the claim is in the data in data store. For more
information, see
Return grounding support scores
.
Getting an aggregated support score for the answer. The support score
indicates how well the answer is grounded in the data in the data store. For
more information, see
Return grounding support
scores
.
Return only well-grounded answers. You can choose to return only those
answers that meet a certain support-score threshold. For more information,
see
Show only well-grounded answers
.
Add personalization information to queries so that the answers can be
customized for individual users. For more information, see
Personalize
answers
.
To receive multimodal answers that include charts or images in addition to text,
the following options are available:
Getting answers that include charts and graphs that plot the data contained in
the answers. For more information, see
Generate charts for
answers
.
Retrieving images from the data store. If the data store contains images,
then the answer method can return an image in the answer. Images from the
data store can also be returned in references if citations are
requested. For more information, see
Retrieve existing images from the data
store
.
Before you begin
Depending on the type of app you have, complete the following requirements:
If you have a structured or unstructured search app, make sure the following
is turned on:
Advanced LLM features
If you have a website search app, make sure the following are turned on:
Enterprise edition features
Advanced LLM features
Advanced website indexing
If you have a blended search app (that is, an app that is connected to more
than one data store), contact your Google account team and ask to be added to
the allowlist for the answer API with blended search.
Search and answer (basic)
The following command shows how to call the
answer
method and
return a generated answer and a list of search results, with links to the
sources.
This command shows the required input only. The options are left at their
defaults.
REST
To search and get results with a generated answer, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query. For example, "Compare the BigQuery and Spanner
databases?".
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "Which database is faster, bigquery or spanner?"}}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "The provided sources do not directly compare the speed of BigQuery and Spanner. However, they do highlight the performance capabilities of each database. BigQuery is described as having strong query performance, particularly for short and complex queries. It also offers a serverless architecture that provides consistent performance regardless of query complexity. Spanner is described as having high performance at virtually unlimited scale, with single-digit millisecond latency for strongly-consistent reads and writes. It also offers a five-nines availability SLA. Ultimately, the best database for a particular use case will depend on the specific requirements of the application. \n",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "
What is the performance of BigQuery?
"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/9ab3ef91bcfde1fcd091efe9df7c699c",
"uri": "https://cloud.google.com/bigquery/docs/best-practices-performance-overview",
"title": "Introduction to optimizing query performance | BigQuery | Google Cloud",
"snippetInfo": [
{
"snippet": "After a query begins execution, \u003cb\u003eBigQuery\u003c/b\u003e calculates how many slots each query stage uses based on the stage size and complexity and the number of slots ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/4e545c5cb69b06b251265114d9099cb4",
"uri": "https://cloud.google.com/bigquery/docs/query-insights",
"title": "Get query performance insights | BigQuery | Google Cloud",
"snippetInfo": [
{
"snippet": "This document describes how to use the query execution graph to diagnose query \u003cb\u003eperformance\u003c/b\u003e issues, and to see query \u003cb\u003eperformance\u003c/b\u003e insights. \u003cb\u003eBigQuery\u003c/b\u003e offers ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d34672d877eefe596f9c7d1a3d7076b1",
"uri": "https://cloud.google.com/bigquery/docs/best-practices-performance-compute",
"title": "Optimize query computation | BigQuery | Google Cloud",
"snippetInfo": [
{
"snippet": "After addressing the query \u003cb\u003eperformance\u003c/b\u003e insights, you can further optimize your query by performing the following tasks: Reduce data that is to be processed ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/75ce2f05833683e60ddc21a11ce0466f",
"uri": "https://cloud.google.com/blog/products/data-analytics/troubleshoot-and-optimize-your-bigquery-analytics-queries-with-query-execution-graph/",
"title": "Troubleshoot and optimize your BigQuery analytics queries with query execution graph | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "Since query \u003cb\u003eperformance\u003c/b\u003e is multi-faceted, \u003cb\u003eperformance\u003c/b\u003e insights might only provide a partial picture of the overall query \u003cb\u003eperformance\u003c/b\u003e. Execution graph. When ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
},
{
"searchAction": {
"query": "
What is the performance of Spanner?
"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f3d036b60379873acf7c73081c5e5b5c",
"uri": "https://cloud.google.com/spanner/docs/performance",
"title": "Performance overview | Spanner | Google Cloud",
"snippetInfo": [
{
"snippet": "These \u003cb\u003eperformance\u003c/b\u003e improvements should result in higher throughput and better latency in \u003cb\u003eSpanner\u003c/b\u003e nodes in both regional and multi-region instance configurations.",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/422496248ade354c73b4c906b8eb9b5f",
"uri": "https://cloud.google.com/blog/products/databases/announcing-cloud-spanner-price-performance-updates",
"title": "Announcing Cloud Spanner price-performance updates | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "Alongside lower costs, Cloud \u003cb\u003eSpanner\u003c/b\u003e provides single-digit ms latencies and strong consistency across multiple availability zones in the same region.",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/53c2a1a6990480ba4aa05cc6b4404562",
"uri": "https://cloud.google.com/blog/topics/developers-practitioners/understanding-cloud-spanner-performance-metrics-scale-key-visualizer",
"title": "Understanding Cloud Spanner performance metrics at scale with Key Visualizer | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "Designed for \u003cb\u003eperformance\u003c/b\u003e tuning and instance sizing, you can use Key Visualizer today in the web-based Cloud Console for all \u003cb\u003eSpanner\u003c/b\u003e databases at no additional ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/a6501ecd5d6391e3ade49097bab0ad3a",
"uri": "https://cloud.google.com/blog/products/databases/a-technical-overview-of-cloud-spanners-query-optimizer",
"title": "A technical overview of Cloud Spanner's query optimizer | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "... performance. Typically, a join will ... Google is continuously improving out-of-the-box \u003cb\u003eperformance of Spanner\u003c/b\u003e and reducing the need for manual tuning.",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "NMwKDAj1_d62BhC72_X_AhIkNjZkN2I4YWEtMDAwMC0yYTdiLWIxMmMtMDg5ZTA4MjhlNzY0"
}
In this example, the query is decomposed into parts: "What is the
performance of Spanner?" and "What is the performance of BigQuery?"
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Query phase commands
This section shows how to specify options for the query phase of the
answer
method call.
Search and answer (rephrasing disabled)
Search and answer (specify maximum steps)
Search and answer with query classification
Search and answer (rephrasing disabled)
The following command shows how to call the
answer
method and
return a generated answer and a list of search results. The answer could be
different from the preceding answer because the rephrasing option is disabled.
REST
To search and get results with a generated answer without applying query
rephrasing, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"queryUnderstandingSpec": {
"queryRephraserSpec": {
"disable": true
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY
: a free-text string that contains the
question or search query. For example, "Compare the BigQuery and Spanner
databases?".
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "Which database is faster, bigquery or spanner?"},
"queryUnderstandingSpec": { "queryRephraserSpec": {
"disable": true
} }
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "The sources provided do not directly compare the speed of BigQuery and Spanner. They do mention that Spanner is optimized for transactional workloads and BigQuery is optimized for analytical workloads. Spanner is a fully managed relational database that provides seamless replication across regions in Google Cloud. BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse. Spanner is designed to scale horizontally across multiple regions and continents. BigQuery is designed for business agility. \n",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "
Which database is faster, bigquery or spanner?
"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/ecc0e7547253f4ca3ff3328ce89995af",
"uri": "https://cloud.google.com/blog/topics/developers-practitioners/how-spanner-and-bigquery-work-together-handle-transactional-and-analytical-workloads",
"title": "How Spanner and BigQuery work together to handle transactional and analytical workloads | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "A federated \u003cb\u003equery\u003c/b\u003e might not be as \u003cb\u003efast\u003c/b\u003e as querying local \u003cb\u003eBigQuery tables\u003c/b\u003e. There may be higher latency because of the small wait time for the source \u003cb\u003edatabase\u003c/b\u003e to ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d7e238f73608a860e00b752ef80e2941",
"uri": "https://cloud.google.com/blog/products/databases/cloud-spanner-gets-stronger-with-bigquery-federated-queries",
"title": "Cloud Spanner gets stronger with BigQuery-federated queries | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "... \u003cb\u003equick\u003c/b\u003e lookup on \u003cb\u003edata\u003c/b\u003e that's in \u003cb\u003eSpanner\u003c/b\u003e -- you can ... Set up an external \u003cb\u003edata\u003c/b\u003e source for the \u003cb\u003eSpanner\u003c/b\u003e shopping \u003cb\u003edatabase\u003c/b\u003e in \u003cb\u003eBigQuery\u003c/b\u003e. ... The \u003cb\u003equery\u003c/b\u003e is executed in ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f3d036b60379873acf7c73081c5e5b5c",
"uri": "https://cloud.google.com/spanner/docs/performance",
"title": "Performance overview | Spanner | Google Cloud",
"snippetInfo": [
{
"snippet": "The information on this page applies to both GoogleSQL and PostgreSQL \u003cb\u003edatabases\u003c/b\u003e. Note: We are in the process of rolling out \u003cb\u003eperformance\u003c/b\u003e and storage changes that ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/47b09cb5ad5e3ab3b1eb93d99ecb0896",
"uri": "https://cloud.google.com/blog/products/databases/rewe-uses-cloud-spanner-to-optimize-for-speed-and-performance",
"title": "REWE uses Cloud Spanner to optimize for speed and performance | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "As a fully managed relational \u003cb\u003edatabase\u003c/b\u003e, \u003cb\u003eSpanner\u003c/b\u003e provides unlimited scale, strong consistency, and up to 99.999% availability. By choosing this approach to ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "M8gKCwjp_t62BhC7wOFMEiQ2NmQ3YjhhZS0wMDAwLTJhN2ItYjEyYy0wODllMDgyOGU3NjQ"
}
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Search and answer (specify maximum steps)
The following command shows how to call the
answer
method and
return a generated answer and a list of search results. The answer is
different from the preceding answers because the number of rephrasing steps has
been increased.
REST
To search and get results with a generated answer allowing up to five rephrasing
steps, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"queryUnderstandingSpec": {
"queryRephraserSpec": {
"maxRephraseSteps":
MAX_REPHRASE
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query. For example, "Compare the BigQuery and Spanner
databases?".
MAX_REPHRASE
: the maximum number of rephrase
steps. The largest value allowed is
5
.
If not set or if set to less than
1
the value is the default,
1
.
Example command
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "How much longer does it take to train a recommendations model than a search model"},
"queryUnderstandingSpec": {
"queryRephraserSpec": {
"maxRephraseSteps": 5
}
}
}'
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Search and answer with query classification
The following command shows how to call the
answer
method to
inquire whether a query is adversarial, non-answer seeking, or neither.
The response includes the classification type for the query, but the answer itself is not affected by the classification.
If you want to change the answer behavior according to the query type, you can
do this in the answer phase. See
Ignore adversarial
queries
and
Ignore non-summary seeking
queries
.
REST
To determine if a query is adversarial or non-answer seeking, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"queryUnderstandingSpec": {
"queryClassificationSpec": {
"types": ["
QUERY_CLASSIFICATION_TYPE
"]
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query. For example, "hello".
QUERY_CLASSIFICATION_TYPE
: the query types
that you want to identify:
ADVERSARIAL_QUERY
,
NON_ANSWER_SEEKING_QUERY
, or both.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": {
"text": "Hello!"},
"queryUnderstandingSpec": {
"queryClassificationSpec": {
"types": ["ADVERSARIAL_QUERY", "NON_ANSWER_SEEKING_QUERY"]
}
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "A user reported that their Google Voice account was randomly sending \"Hello!\" replies to incoming texts. The user was frustrated because they did not want to send these replies and found the behavior random. The user was unable to find any linked accounts, Google extensions, or other settings that could be causing the issue. The user confirmed that Google Voice does not have auto-reply functions. The user was seeking help to stop the automatic replies. \n",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "Hello!"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/69e92e5b1de5b1e583fbe95f94dd4cbf",
"uri": "https://support.google.com/voice/thread/152245405/google-voice-is-randomly-automatically-sending-hello-replies-to-incoming-texts?hl=en",
"title": "Google voice is randomly/automatically sending \"Hello!\" replies to incoming texts",
"snippetInfo": [
{
"snippet": "There IS a new "Smart reply" feature on the Android or iOS client apps, but you'd have to a) receive a SMS/MMS, b) open it up, c) look at the three suggested ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/44fb313bcc09877e7239f3810ddb132b",
"uri": "https://support.google.com/mail/thread/58174131/gmail-sends-random-email-saying-hello-to-my-emails-without-me-touching-it?hl=en",
"title": "Gmail sends random email saying \"Hello!!\" to my emails without me touching it",
"snippetInfo": [
{
"snippet": "Gmail sends random email saying "\u003cb\u003eHello\u003c/b\u003e!!" to my emails without me touching it. Whenever I email somebody and they reply, a random email from my Gmail is sent to ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/16d65e2af7fa854d1a00995525646dc3",
"uri": "https://support.google.com/voice/thread/112990484/google-voice-sending-hello-in-response-to-text-messages?hl=en",
"title": "Google Voice sending \"Hello,\" in response to text messages",
"snippetInfo": [
{
"snippet": "When I receive text messages, a reply is instantly sent out reading "\u003cb\u003eHello\u003c/b\u003e," and I cannot figure out how this is happening. I have no linked accounts, ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/a828eb8f442f1dfbdda06dbeb52841b0",
"uri": "https://support.google.com/a/thread/161821861/hello-hello-the-lost-phone?hl=en",
"title": "Hello.Hello the lost phone - Google Workspace Admin Community",
"snippetInfo": [
{
"snippet": "\u003cb\u003eHello\u003c/b\u003e the lost phone. My wife lost her phone but she cannot remember her emails pasward to help track .",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
],
"queryUnderstandingInfo": {
"queryClassificationInfo": [
{
"type": "ADVERSARIAL_QUERY"
},
{
"type": "NON_ANSWER_SEEKING_QUERY",
"positive": true
}
]
}
},
"answerQueryToken": "NMwKDAjVloK3BhCdt8u9AhIkNjZkYmFhNWItMDAwMC0yZTBkLTg0ZDAtMDg5ZTA4MmRjYjg0"
}
In this example, the query "hello" is not adversarial but it is classified as
non-answer-seeking.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Search phase commands: Search and answer with search result options
This section shows how to specify options for the search phase portion of the
answer
method call, options such as setting the maximum number
of documents returned, boosting, and filtering, and how to get an answer when
you supply your own search results.
The following command shows how to call the
answer
method and
specify various options for how the search result is returned. (The search
results are independent of the answer.)
REST
To set various options related to which and how search results are returned, do
the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"searchSpec": {
"searchParams": {
"maxReturnResults":
MAX_RETURN_RESULTS
,
"filter": "
FILTER
",
"boostSpec":
BOOST_SPEC
,
"orderBy": "
ORDER_BY
",
"searchResultMode":
SEARCH_RESULT_MODE
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query. For example, "Compare the BigQuery and Spanner
databases?"
MAX_RETURN_RESULTS
: the number of search
results to return. The default value is
10
. The maximum value
is
25
.
FILTER
: the filter specifies which documents
are queried. If a document's metadata meets the filter specification, then
the document will be queried. For more information, including filter
syntax, see
Filter
generic search for structured or unstructured data
.
BOOST_SPEC
: the boost specification lets you
boost certain documents in search results, which can affect the answer.
For more information, including the syntax for the boost specification, see
Boost search results
.
ORDER_BY
: the order in which documents are
returned. Documents can be ordered by a field in a
Document
object. The
orderBy
expression is case-sensitive.
If this field is unrecognizable, an
INVALID_ARGUMENT
is
returned.
SEARCH_RESULT_MODE
: it specifies the search
result mode:
DOCUMENTS
or
CHUNKS
. For more
information, see
Parse and
chunk documents
and
ContentSearchSpec
.
This field is only available in the v1alpha version of the API.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": {
"text": "Does spanner database have an API?"},
"searchSpec": {
"searchParams": { "maxReturnResults": 3 }
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "Spanner database has an API that provides programmatic access to the database. The API is available through client libraries, RPC, and REST. The client libraries allow you to interact with Spanner in your preferred language. The RPC API and REST API provide programmatic access to Spanner. The Cloud Spanner API is a managed, mission-critical, globally consistent and scalable relational database service. \n",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "Does spanner database have an API?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d135b46c4a44d0cc6b652538c1887f4d",
"uri": "https://cloud.google.com/spanner/docs/apis",
"title": "APIs & reference | Spanner | Google Cloud",
"snippetInfo": [
{
"snippet": "The client libraries, the RPC \u003cb\u003eAPI\u003c/b\u003e, and the REST \u003cb\u003eAPI\u003c/b\u003e provide programmatic access to \u003cb\u003eSpanner\u003c/b\u003e. \u003cb\u003eSpanner\u003c/b\u003e client libraries. \u003cb\u003eGet\u003c/b\u003e started with \u003cb\u003eSpanner\u003c/b\u003e in your language ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/7a744d43e61ccd33539de74d5c1f6313",
"uri": "https://cloud.google.com/spanner/docs/reference/rest",
"title": "Cloud Spanner API",
"snippetInfo": [
{
"snippet": "Returns permissions that the caller \u003cb\u003ehas\u003c/b\u003e on the specified \u003cb\u003edatabase\u003c/b\u003e or backup resource. updateDdl, PATCH /v1/{\u003cb\u003edatabase\u003c/b\u003e=projects/*/instances/*/\u003cb\u003edatabases\u003c/b\u003e/*}/ddl",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/70834ebf4b72b6dc69e06c44ee80f90b",
"uri": "https://cloud.google.com/spanner/docs/reference/rpc",
"title": "Cloud Spanner API",
"snippetInfo": [
{
"snippet": "ChangeQuorum \u003cb\u003eis\u003c/b\u003e strictly restricted to \u003cb\u003edatabases\u003c/b\u003e ... Returns the schema of a Cloud \u003cb\u003eSpanner database\u003c/b\u003e ... Returns permissions that the caller \u003cb\u003ehas\u003c/b\u003e on the specified ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "NMwKDAj2l4K3BhCqiv66ARIkNjZkYmFhNmMtMDAwMC0yZTBkLTg0ZDAtMDg5ZTA4MmRjYjg0"
}
In this example, the number of documents returned is capped at three.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Answer phase commands
This section shows how to customize the
answer
method call.
You can combine the following options as needed.
Ignore adversarial queries and non-answer-seeking queries
Show only relevant answers
Return grounding support scores
Show only well-grounded answers
Specify the answer model
Specify a custom preamble
Include citations
Set the answer language code
Personalize answers
Generate charts for answers
Retrieve existing images from the data store
Ignore adversarial queries and non-answer-seeking queries
The following command shows how to avoid answering adversarial queries and
non-answer-seeking queries when calling the
answer
method.
REST
To skip answering queries that are adversarial or non-answer-seeking, do the
following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"ignoreAdversarialQuery": true,
"ignoreNonAnswerSeekingQuery": true
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "Hello"},
"answerGenerationSpec": {
"ignoreAdversarialQuery": true
,
"ignoreNonAnswerSeekingQuery": true
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "
A summary could not be generated for your search query. Here are some search results.
",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "Hello"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/69e92e5b1de5b1e583fbe95f94dd4cbf",
"uri": "https://support.google.com/voice/thread/152245405/google-voice-is-randomly-automatically-sending-hello-replies-to-incoming-texts?hl=en",
"title": "Google voice is randomly/automatically sending \"Hello!\" replies to incoming texts",
"snippetInfo": [
{
"snippet": "There IS a new "Smart reply" feature on the Android or iOS client apps, but you'd have to a) receive a SMS/MMS, b) open it up, c) look at the three suggested ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/16d65e2af7fa854d1a00995525646dc3",
"uri": "https://support.google.com/voice/thread/112990484/google-voice-sending-hello-in-response-to-text-messages?hl=en",
"title": "Google Voice sending \"Hello,\" in response to text messages",
"snippetInfo": [
{
"snippet": "When I receive text messages, a reply is instantly sent out reading "\u003cb\u003eHello\u003c/b\u003e," and I cannot figure out how this is happening. I have no linked accounts, ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/b3bdde4957f588a1458c533269626d09",
"uri": "https://support.google.com/voice/thread/4307458/lately-an-automatic-text-response-saying-hello-is-going-out-how-do-i-stop-this?hl=en",
"title": "Lately an automatic text response saying, \"Hello\" is going out. How do I stop this? - Google Voice Community",
"snippetInfo": [
{
"snippet": "You need to find out what app is causing it and deactivate or delete it. Last edited Apr 16, 2019.",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/a828eb8f442f1dfbdda06dbeb52841b0",
"uri": "https://support.google.com/a/thread/161821861/hello-hello-the-lost-phone?hl=en",
"title": "Hello.Hello the lost phone - Google Workspace Admin Community",
"snippetInfo": [
{
"snippet": "\u003cb\u003eHello\u003c/b\u003e the lost phone. My wife lost her phone but she cannot remember her emails pasward to help track .",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
],
"answerSkippedReasons": [
"NON_ANSWER_SEEKING_QUERY_IGNORED"
]
},
"answerQueryToken": "NMwKDAjFgN-2BhDlsKaZARIkNjZkN2I0NmItMDAwMC0yZmQ5LTkwMDktZjQwMzA0M2E5YTg4"
}
In this example, the query is determined to be non-answer-seeking and so no
answer is generated.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Show only relevant answers
Vertex AI Search can assess how relevant the results are to a
query. If no results are determined to be sufficiently relevant, then instead
of generating an answer from non-relevant or minimally-relevant results, you can
choose to return a fallback answer: "
We do not have a summary for your query.
"
The following command shows how to return the fallback answer in the case of
irrelevant results when calling the
answer
method.
REST
To return a fallback answer if no relevant results are found, do the
following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"ignoreLowRelevantContent": true
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "foobar"}, "answerGenerationSpec": {
"ignoreLowRelevantContent": true
} }'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "We do not have a summary for your query.",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "foobar"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/719b79786f0c143717c569eade5305d9",
"uri": "https://support.google.com/websearch/thread/261714267/google-foobar-bug-console-disappeared?hl=en",
"title": "Google Foobar Bug - Console Disappeared",
"snippetInfo": [
{
"snippet": "Google \u003cb\u003eFoobar\u003c/b\u003e Bug - Console Disappeared. After I logged in today the top bar says "The \u003cb\u003eFoobar\u003c/b\u003e Challenge will be turned down on 1 April 2024. If you run out of ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/932369826585ff45f6ab3eba01ba6933",
"uri": "https://support.google.com/websearch/thread/95251114/unable-to-contact-foobar-recruiter?hl=en",
"title": "Unable to contact Foobar Recruiter - Google Search Community",
"snippetInfo": [
{
"snippet": "Access is by invitation only so you will need to have the proper credentials to login. You can always reach out using the contact us button, but there is no ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/fb736a30ff90d058be755f0a04a522a8",
"uri": "https://support.google.com/websearch/thread/121151780/foobar-challenge-appeared-to-me-then-disappeared?hl=en",
"title": "Foobar challenge appeared to me then disappeared - Google Search Community",
"snippetInfo": [
{
"snippet": "Hi. I got the \u003cb\u003efoobar\u003c/b\u003e challenge some months ago. But then it disappeared immediately, maybe by misclick (though I don't think I misclicked).",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f56f2656b0d02b839509d0e67e60c1c9",
"uri": "https://support.google.com/chrome/thread/159931759/cannot-access-google-foobar-challenge?hl=en",
"title": "Cannot Access Google FooBar Challenge",
"snippetInfo": [
{
"snippet": "I knew I wouldn't have time for it today, so I just kept the tab in the background. Tonight, I went to go close all my tabs, but the page had changed. It said " ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
],
"answerSkippedReasons": [
"NO_RELEVANT_CONTENT"
]
},
"answerQueryToken": "M8gKCwiokvy2BhDtv8EDEiQ2NmQ5NDQxZC0wMDAwLTIxMGQtOWU2Yi1mNDAzMDQ1ZGJkMzA"
}
In this example, the results were determined to be not sufficiently relevant
to the query, and so the fallback answer was returned instead of a generated
answer and results.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Return grounding support scores
The following command shows how to return grounding support scores for answers
and claims.
For general information about grounding in Vertex AI, see
Check
grounding with RAG
. The
groundingConfigs.check
method is called by the
answer method.
REST
To return a support score for each claim (sentence in the answer) and an
aggregated support score for the answer, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"groundingSpec": {
"includeGroundingSupports": true,
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer"
-d '{
"query": { "text": "What is SQL?"},
"groundingSpec": {
"includeGroundingSupports": true,
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "SQL stands for Structured Query Language. It is a database management programming language that is used to access and manage data in a database. SQL is used to create, update, and delete data in a database. It can also be used to query data and retrieve information. SQL is a standard language that is used by many different database systems.",
"groundingScore" 0.9
"groundingSupports": [
{
"endIndex": "41",
"sources": [
{
"referenceId": "1"
}
]
"groundingScore": 0.9
"groundingCheckRequired": true
},
{
"startIndex": "42",
"endIndex": "144",
"sources": [
{
"referenceId": "1"
}
]
"groundingScore": 0.8
"groundingCheckRequired": true
},
{
"startIndex": "267",
"endIndex": "342",
"sources": [
{
"referenceId": "2"
}
]
"groundingScore": 0.6
"groundingCheckRequired": true
}
],
"references": [
{
"chunkInfo": {
"content": "There are a lot of Databases available in the market such as MS Access, Oracle and many others.For you to write programs that interact with these databases easily, there has to be a way where you could get information from all these databases using the same method.For this purpose SQL was developed.It is a kind of language (simple when compared to the likes of C or C++) which enables you to ask all your queries to a database without bothering about the exact type of database.When you use this Query the database engine would first find the table called people.Then it would find a column called firstname.Next it would compare all the values in that column with 'Reena'.Finally it would return all the details wherever it finds a match for the firstname.When you write a database program in VC++ or Java or any other language for that matter, you would make a database connection to your database and then you would query the database using SQL queries.When you query the database with any SQL query the database returns a recordset.A recordset is basically a set of records (all the entries that your query returns).This recordset is received in your program and all languages have a data structure which represents a recordset.",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d993d922043374f5ef7ba297c158b106",
"uri": "gs://my-bucket-123/documents/058dee0ec23a3e92f9bfd7cd29840e8f.txt"
"structData": {
"fields": [
{
"key": "cdoc_url"
"value": { "stringValue": "058dee0ec23a3e92f9bfd7cd29840e8f" }
},
{
"key": "doc_id"
"value": { "stringValue": "d993d922043374f5ef7ba297c158b106" }
}
]
}
}
}
},
{
"chunkInfo": {
"content": "The Structured Query Language (SQL) is a database management programming language.SQL is a tool for accessing databases, and more specifically, relational databases, and can be used with different database products.This chapter will prepare you to learn basic database management using this language.SQLite – To implement SQL as a library, you need SQLite.SQLite is intended to provide users and programs a way to store data using a SQL interface within the program.SQLite3 can be used to manipulate SQLite databases for major Linux distros.SQL is used to access relational databases.Each database contains more or less tables which in turn contain more or less rows and columns.Hereby a single row is seen as a separate object with features represented by the tables' columns.To access a table's data you first have to connect to its database.With the same table, the query SELECT * FROM T WHERE C1 = 1 will result in all the elements of all the rows where the value of column C1 is '1' being shown.A WHERE clause specifies that a SQL statement should only affect rows that meet specified criteria.The criteria are expressed in the form of predicates.WHERE clauses are not mandatory clauses of SQL statements, but should be used to limit the number of rows affected by a SQL DML statement or returned by a query.",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/3825eac51ef9e934bbc558faa42f4c71",
"uri": "gs://my-bucket-123/documents/26f5872b0719790cb966a697bfa1ea27.txt"
"structData": {
"fields": [
{
"key": "cdoc_url"
"value": { "stringValue": "26f5872b0719790cb966a697bfa1ea27" }
},
{
"key": "doc_id"
"value": { "stringValue": "3825eac51ef9e934bbc558faa42f4c71" }
}
]
}
}
}
},
{
"chunkInfo": {
"content": "This chapter focuses on using Paradox as a client/server development tool.It does not talk about connecting; it is assumed you have already connected.If you are having trouble connecting to a particular SQL server, then refer to the Connection Guide for that particular server.This chapter does review what a user can do interactively with Paradox and how to use ObjectPAL with SQL servers.Structured Query Language (SQL) was developed to create a standard for accessing database information.The ANSI standard for SQL allows a user to become familiar with the commands needed to query many different types of data.After you learn ANSI SQL, you then can query many different databases.Is SQL a solid standard?Yes and no.Yes, the core ANSI SQL commands are solid and consistent from vendor to vendor.Every vendor, however, adds capability to its version of SQL.These improvements are expected because ANSI SQL does not go far enough to cover every feature of every high-end DBMS.The SQL standard is used by many companies for their high-end products.They include Oracle, Sybase, Microsoft SQL, Informix, and Interbase.Paradox also provides the capability to use standard ANSI SQL commands on local Paradox and dBASE tables.Although SQL by definition is a standard, various flavors are on the market.",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/b3e88db8676b87b99af1e6ecc7d8757f",
"uri": "gs://my-bucket-123/documents/073c21335d37d8d14982cb3437a721c0.txt"
"structData": {
"fields": [
{
"key": "cdoc_url"
"value": { "stringValue": "073c21335d37d8d14982cb3437a721c0" }
},
{
"key": "doc_id"
"value": { "stringValue": "b3e88db8676b87b99af1e6ecc7d8757f" }
}
]
}
}
}
}
],
...
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "What is SQL?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d993d922043374f5ef7ba297c158b106",
"uri": "gs://my-bucket-123/documents/058dee0ec23a3e92f9bfd7cd29840e8f.txt",
"chunkInfo": [
{
"content": "There are a lot of Databases available in the market such as MS Access, Oracle and many others.For you to write programs that interact with these databases easily, there has to be a way where you could get information from all these databases using the same method.For this purpose SQL was developed.It is a kind of language (simple when compared to the likes of C or C++) which enables you to ask all your queries to a database without bothering about the exact type of database.When you use this Query the database engine would first find the table called people.Then it would find a column called firstname.Next it would compare all the values in that column with 'Reena'.Finally it would return all the details wherever it finds a match for the firstname.When you write a database program in VC++ or Java or any other language for that matter, you would make a database connection to your database and then you would query the database using SQL queries.When you query the database with any SQL query the database returns a recordset.A recordset is basically a set of records (all the entries that your query returns).This recordset is received in your program and all languages have a data structure which represents a recordset."
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/3825eac51ef9e934bbc558faa42f4c71",
"uri": "gs://my-bucket-123/documents/26f5872b0719790cb966a697bfa1ea27.txt",
"chunkInfo": [
{
"content": "The Structured Query Language (SQL) is a database management programming language.SQL is a tool for accessing databases, and more specifically, relational databases, and can be used with different database products.This chapter will prepare you to learn basic database management using this language.SQLite – To implement SQL as a library, you need SQLite.SQLite is intended to provide users and programs a way to store data using a SQL interface within the program.SQLite3 can be used to manipulate SQLite databases for major Linux distros.SQL is used to access relational databases.Each database contains more or less tables which in turn contain more or less rows and columns.Hereby a single row is seen as a separate object with features represented by the tables' columns.To access a table's data you first have to connect to its database.With the same table, the query SELECT * FROM T WHERE C1 = 1 will result in all the elements of all the rows where the value of column C1 is '1' being shown.A WHERE clause specifies that a SQL statement should only affect rows that meet specified criteria.The criteria are expressed in the form of predicates.WHERE clauses are not mandatory clauses of SQL statements, but should be used to limit the number of rows affected by a SQL DML statement or returned by a query."
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/b3e88db8676b87b99af1e6ecc7d8757f",
"uri": "gs://my-bucket-123/documents/073c21335d37d8d14982cb3437a721c0.txt",
"chunkInfo": [
{
"content": "This chapter focuses on using Paradox as a client/server development tool.It does not talk about connecting; it is assumed you have already connected.If you are having trouble connecting to a particular SQL server, then refer to the Connection Guide for that particular server.This chapter does review what a user can do interactively with Paradox and how to use ObjectPAL with SQL servers.Structured Query Language (SQL) was developed to create a standard for accessing database information.The ANSI standard for SQL allows a user to become familiar with the commands needed to query many different types of data.After you learn ANSI SQL, you then can query many different databases.Is SQL a solid standard?Yes and no.Yes, the core ANSI SQL commands are solid and consistent from vendor to vendor.Every vendor, however, adds capability to its version of SQL.These improvements are expected because ANSI SQL does not go far enough to cover every feature of every high-end DBMS.The SQL standard is used by many companies for their high-end products.They include Oracle, Sybase, Microsoft SQL, Informix, and Interbase.Paradox also provides the capability to use standard ANSI SQL commands on local Paradox and dBASE tables.Although SQL by definition is a standard, various flavors are on the market."
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/3dd4014e41044c5dd6a0fe380847f369",
"uri": "gs://my-bucket-123/documents/76245cb33a66f4fbd9030a2a11eea00d.txt",
"chunkInfo": [
{
"content": "SQL injection is a code injection technique that might destroy your database.You can read more here OWASP sql injection testing sheet.Description: SQL injection ( second order) SQL injection vulnerabilities arise when user- controllable data is incorporated sheet into database SQL queries in an unsafe manner.This sheet cheat wiki assumes you have a basic understanding of SQL injection, please go here for an introduction if you are unfamiliar.Bypass login page with sql SQL injection [ closed].Gone are the days when knowledge sheet of just sql SQL Injection or XSS could help you land a lucrative high- paying InfoSec job.There is many sheet differnet variations you would login have probably have to try to make this exploit work ( sql especially if it is sql a blind SQL exploit).SQL injection usually occurs when you ask a user for input, like their.ゲストブック/ コメントの例.Submit Text Post.Get an ad- free experience with special benefits, and directly support Reddit.get reddit premium.SQL Injection Cheat.Many web applications have an authentication system: a user provides a user name and password, the web application checks them and stores the corresponding user id in the session hash.Login # 1 Login # 2 Login # 3 Login # 4."
}
]
}
]
}
}
]
}
]
}
}
In this example, a support score (`groundingScore`) is returned for each
citation.
Show only well-grounded answers
The following command shows how to return only those answers that are deemed to
be well grounded in the
corpus
, the information in the data store.
Poorly-grounded answers are filtered out.
You choose a low or high level threshold for the grounding support score. Then, the answer
is only returned if it meets or exceeds that level. You can experiment with the two
filter thresholds and with no threshold to determine what level of filter is
likely to provide the best results for your users.
For general information about grounding in Vertex AI, see
Check
grounding with RAG
. The
groundingConfigs.check
method is called by the
answer method.
REST
To return an answer only if it meets a support-score threshold, do the
following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"groundingSpec": {
"filteringLevel": "
FILTER_LEVEL
"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
FILTER_LEVEL
: an enumeration for filtering
answers based on grounding support score. Options are:
FILTERING_LEVEL_LOW
and
FILTERING_LEVEL_HIGH
. If
filteringLevel
is not included, then no
support-score filter is applied to the answer.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "When can an NCD be made?"},
"groundingSpec": {
"filtering_level": "FILTERING_LEVEL_HIGH"
}
}'
{
answer {
state: SUCCEEDED
answer_text: "We do not have a summary for your query."
steps {
state: SUCCEEDED
description: "Rephrase the query and search."
actions {
search_action {
query: "test?"
}
observation {
search_results {
document: "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7f5cfde02"
uri: "gs://my-bucket-123/data/CoverageDocumentation.pdf"
title: "ABC345_0101"
chunk_info {
content: "This notice implements part of section 731 of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 by describing a method of developing, and making available to the public, guidance documents under the Medicare program… "
}
...
search_results {
document: "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7f5cfde02"
uri: "gs://my-bucket-123/data/CoverageDocumentation.pdf"
title: "ABC345_0101"
chunk_info {
content: "For the purposes of this notice, the term guidance documents means documents prepared for our staff, potential requestors of National Coverage Determinations, and other interested parties explaining the NCD process… "
}
}
}
}
}
answer_skipped_reasons: LOW_GROUNDED_CONTENT
}
In this example, no answer is returned because the high threshold wasn't met.
Specify the answer model
The following command shows how to change the model version used to generate
answers.
For information about the supported models, see
Answer generation model versions and lifecycle
.
REST
To generate an answer using a model different from the default model, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"modelSpec": {
"modelVersion": "
MODEL_VERSION
",
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
MODEL_VERSION
: the model version that you want to use to generate the
answer. For more
information, see
Answer
generation model versions and lifecycle
.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "Compare bigquery with spanner database?"}, "answerGenerationSpec": {
"modelSpec": {
"modelVersion": "preview",
}
} }'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "Cloud Spanner is a fully managed relational database optimized for transactional workloads. BigQuery is a serverless, highly scalable, and cost-effective multi-cloud data warehouse designed for business agility. BigQuery is optimized for ad-hoc analysis and reporting. Both Spanner and BigQuery are built on Google's distributed storage system, Colossus, and their internal cluster management system, Borg. They are also built on Jupiter, Google's in-house custom network hardware and software.\n\nBigQuery can query data stored in Spanner in real time without moving or copying the data. This is possible with BigQuery's query federation support. To run a federated query, you need to configure an external data source in BigQuery that points to the intended Spanner instance. You can then write queries that can be used to populate a BigQuery table on demand or scheduled to run as needed. You can also join the query with another BigQuery result set dynamically.\n\nYou can also use Dataflow to copy data from Spanner to BigQuery. Dataflow is a service that can be used to ingest Spanner data into BigQuery. This is useful for more complex transformations or external dependencies. For example, an online gaming company might use Spanner to store game data and BigQuery to perform analytics on player behavior. They can replicate data from Spanner into BigQuery and perform analytics against local data, or they can use federated queries to retrieve data from Spanner on-demand.\n",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "Compare bigquery with spanner database?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/ecc0e7547253f4ca3ff3328ce89995af",
"uri": "https://cloud.google.com/blog/topics/developers-practitioners/how-spanner-and-bigquery-work-together-handle-transactional-and-analytical-workloads",
"title": "How Spanner and BigQuery work together to handle transactional and analytical workloads | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "Using Cloud \u003cb\u003eSpanner\u003c/b\u003e and \u003cb\u003eBigQuery\u003c/b\u003e also allows customers to build their \u003cb\u003edata\u003c/b\u003e clouds using Google Cloud, a unified, open approach to \u003cb\u003edata\u003c/b\u003e-driven transformation ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d7e238f73608a860e00b752ef80e2941",
"uri": "https://cloud.google.com/blog/products/databases/cloud-spanner-gets-stronger-with-bigquery-federated-queries",
"title": "Cloud Spanner gets stronger with BigQuery-federated queries | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "As enterprises compete for market share, their need for real-time insights has given rise to increased demand for transactional \u003cb\u003edatabases\u003c/b\u003e to support \u003cb\u003edata\u003c/b\u003e ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/e10a5a3c267dc61579e7c00fefe656eb",
"uri": "https://cloud.google.com/blog/topics/developers-practitioners/replicating-cloud-spanner-bigquery-scale",
"title": "Replicating from Cloud Spanner to BigQuery at scale | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "... \u003cb\u003eSpanner data\u003c/b\u003e into \u003cb\u003eBigQuery\u003c/b\u003e for analytics. In this post, you will learn how to efficiently use this feature to replicate large tables with high throughput ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/648c220055c1d2ac369165007d9f6650",
"uri": "https://cloud.google.com/blog/products/databases/choosing-cloud-spanner-for-game-development",
"title": "Choosing Cloud Spanner for game development | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "To get started with \u003cb\u003eSpanner\u003c/b\u003e, create a \u003cb\u003edatabase\u003c/b\u003e, or try it out with a \u003cb\u003eSpanner\u003c/b\u003e Qwiklab. ... AlloyDB \u003cb\u003evs\u003c/b\u003e. ... SQL for SQL Server to \u003cb\u003eBigQuery\u003c/b\u003e. By Alexander ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "NMwKDAivmvy2BhCxnsqdARIkNjZkOTQ0NWEtMDAwMC0yMTBkLTllNmItZjQwMzA0NWRiZDMw"
}
In this example, the preview version of the model is used instead of the default model.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Specify a custom preamble
The following command shows how to set a preamble for the generated answer. A
preamble contains natural language instructions for customizing the answer. You
can request customizations such as length, level of detail, style of output
(such as "simple"), language of output, focus of answer, and format (such as
tables, bullets, and XML). For example, a preamble might be "Explain like you
are a ten years old kid."
The preamble can have a significant effect on the quality of the generated
answer. For information about what to write in preambles and examples of good
preambles, see
About custom preambles
.
REST
To generate an answer using a model different from the default model, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"promptSpec": {
"preamble": "
PREAMBLE
",
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
PREAMBLE
: a natural-language instruction for
customizing the answer. For example, try
show the answer format in
an ordered list
or
give a very detailed answer
.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "what is bigquery?"},
"answerGenerationSpec": {
"promptSpec": {
"preamble": "
Explain like you are a ten years old
kid
",
}
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "
BigQuery is like a super-powered storage space for your data, but it's in the cloud, not on your computer. It's like a giant warehouse for all your information, but you don't have to build or manage it yourself. You can use BigQuery to find patterns and insights in your data, like figuring out what people like to buy or how many people visited your website. It's like having a super-smart assistant that can help you understand your data better. BigQuery is really good at working with lots of data, even billions of pieces of information. \n",
"steps
": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "What is BigQuery?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/2d032dc582689e8c0ecea7fc7bfa3189",
"uri": "https://cloud.google.com/bigquery",
"title": "BigQuery enterprise data warehouse | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eBigQuery\u003c/b\u003e is a fully managed, AI-ready data analytics platform that helps you maximize value from your data and is designed to be multi-engine, multi-format, ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/4474f4a5a18ecd611dedfe323dfe55d9",
"uri": "https://cloud.google.com/bigquery/docs/introduction",
"title": "BigQuery overview | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eBigQuery\u003c/b\u003e is a fully managed, AI-ready data platform that helps you manage and analyze your data with built-in features like machine learning, search, ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/c840fdef90d86328f13bbedbdbf0ac10",
"uri": "https://cloud.google.com/bigquery/docs/query-overview",
"title": "Overview of BigQuery analytics | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eBigQuery\u003c/b\u003e lets you save queries and share queries with others. When you save a query, it can be private (visible only to you), shared at the project level ( ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/5cbfab8ce1d5f6ffe45fef22900c9a00",
"uri": "https://cloud.google.com/curated-resources/bigquery",
"title": "Guides BigQuery | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eBigQuery\u003c/b\u003e is Google Cloud's fully managed and serverless enterprise data warehouse solution, designed to help you make informed decisions quickly, so you can ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "NMwKDAi8hN-2BhC0jMCPARIkNjZkN2I4MzItMDAwMC0yMTliLTkxN2EtMDg5ZTA4MjA0YjFj"
}
In this example, the preamble requests a simpler answer than the default
might provide.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Include citations
The following command shows how to request citations to be included with the
answer.
REST
To generate an answer using a model different from the default model, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"includeCitations":
INCLUDE_CITATIONS
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
INCLUDE_CITATIONS
: specifies whether to include
citation metadata in the answer. The default value is
false
.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "What is SQL"}, "answerGenerationSpec": {
"includeCitations": true
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "SQL stands for Structured Query Language and is a programming language used to manage, query, and retrieve data in a relational database. It is the standard language used by relational database management systems (RDBMS) such as PostgreSQL, SQL Server, MySQL, and Oracle Database. SQL statements are written in a statement format for queries and other database operations, allowing users to manipulate data in relational database tables. SQL is used to create and update the structure of tables, read and write data, manage user permissions, and perform administrative tasks. While originally created for relational databases, SQL is now a foundation for many technology capabilities, making SQL knowledge essential for many technology roles. \n",
"citations": [
{
"endIndex": "137",
"sources": [
{
"referenceId": "0"
},
{
"referenceId": "1"
}
]
},
{
"startIndex": "138",
"endIndex": "437",
"sources": [
{
"referenceId": "3"
}
]
},
{
"startIndex": "438",
"endIndex": "575",
"sources": [
{
"referenceId": "2"
}
]
},
{
"startIndex": "576",
"endIndex": "742",
"sources": [
{
"referenceId": "3"
}
]
}
],
"references": [
{
"chunkInfo": {
"content": "There may be a second table that stores visit information. A relational database uses a unique ID for each row to maintain the linked patient information across the two tables. This way, you can quickly look up the visits of each patient. Sign up for a free trial for any of Google Cloud's SQL databases, which include AlloyDB, Cloud SQL, and Spanner. Get started for free What is SQL? SQL (Structured Query Language) is a programming language used to store, retrieve, and manage data in a relational database. SQL statements are English-like, making the language accessible to software developers, data analysts, and other practitioners. Benefits of SQL databases Enterprises choose SQL databases for being: Efficient. Relational databases are incredibly efficient in managing complex queries. Fast. SQL databases can retrieve large amounts of data, quickly. This makes them highly desirable for real-time transactional data. Reliable. SQL databases provide a high degree of data integrity and are ACID-compliant. SQL database engines There are numerous SQL database engines (products) used to build software applications. Some of the most popular include PostgreSQL, MySQL, SQL Server, and Oracle. Some database engines are open source while others are commercial offerings. ",
"relevanceScore": 0.9,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
"uri": "https://cloud.google.com/discover/what-are-sql-databases",
"title": "SQL Databases | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "PostgreSQL vs. SQL Server: What's the difference? | Google Cloud Page Contents Topics PostgreSQL vs. SQL PostgreSQL vs SQL Server: What are the key differences? Trying to find the right database for your applications? When it comes to choosing a database technology, the most common SQL options to consider are PostgreSQL vs. SQL Server. While both systems share many core features, there are some key differences—the major one being that PostgreSQL is open source and SQL Server is owned by Microsoft. Today, it is more vital than ever for companies to be able to manage, store, and activate data for modern business operations. With the growing assortment of databases available to choose from, it can be overwhelming to pick the right one for your applications. The most important thing to remember is that no single database will be a good match for every project requirement, so it's critical to understand the option that will work best for your specific use case. So, what is PostgreSQL vs. SQL Server? In this short guide, we'll discuss the basic differences between PostgreSQL and SQL Server. Get started for freeStay informed What is SQL? Structured Query Language or SQL, as it's more commonly known, is a programming language used to manage, query, and retrieve data in a relational database. ",
"relevanceScore": 0.8,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
"uri": "https://cloud.google.com/learn/postgresql-vs-sql",
"title": "PostgreSQL vs. SQL Server: What's the difference? | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "SQL Databases | Google Cloud Page Contents Topics What are SQL databases? What are SQL databases? A SQL database, also known as a relational database, is a system that stores and organizes data into highly structured tables of rows and columns. These databases offer Structured Query Language (SQL) to read and write the data, and are categorized as relational database management systems (RDBMS). SQL statements are used to create and update the structure of tables, read and write data, manage user permissions, and perform administrative tasks. For example, a CREATE statement is used to create a table, an INSERT statement adds a new row to a table, and a SELECT statement performs a database query. Statements that make structural or administrative changes are usually reserved for software developers and administrators, while read and write operations are performed by end-user applications. A relational database maintains the ability to link information across multiple tables. This format makes it easy to quickly gain insights about the relationships between various columns or data points in these tables. A relational database can create indexes for particular columns for faster lookups. For example, a healthcare facility might maintain a table containing rows of patient information, where each row is one patient and the columns contain data points, such as the patient's name, insurance information, and contact details. ",
"relevanceScore": 0.8,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
"uri": "https://cloud.google.com/discover/what-are-sql-databases",
"title": "SQL Databases | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "It is the standard language used by relational database management systems (RDBMS), including PostgreSQL, SQL Server, MySQL, and Oracle Database. SQL typically uses commands written in statement format for queries and other database operations, which allow users to manipulate data in relational database tables. While originally created for relational databases, SQL acts as a foundation for many of today's technology capabilities, making SQL knowledge an essential skill for many technology roles today, including data analysts, database engineers, and even backend programming. However, you will find that there are different variants of SQL depending on the database or database management system that you choose. What is Microsoft SQL Server? SQL Server is a leading RDBMS that is built on top of SQL and developed by Microsoft. It is used to manage and store data to support numerous enterprise use cases for business intelligence, transaction processing, data analytics, and machine learning services. SQL Server has a row-based table structure that allows you to connect related data elements from different tables without having to store data multiple times in a database. In general, Microsoft SQL Server is known for its high availability, fast performance when handling large workloads, and easy integration with other applications to gain business intelligence across your entire data estate. For more information, we recommend reviewing the official SQL Server documentation. ",
"relevanceScore": 0.8,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
"uri": "https://cloud.google.com/learn/postgresql-vs-sql",
"title": "PostgreSQL vs. SQL Server: What's the difference? | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "Send feedback The GoogleSQL language in Spanner bookmark_borderbookmark Stay organized with collections Save and categorize content based on your preferences. Dismiss Got it GoogleSQL is the new name for Google Standard SQL! New name, same great SQL dialect. This page provides an overview of supported statements in GoogleSQL. GoogleSQL is an ANSI compliant Structured Query Language (SQL) which includes the following types of supported statements: Query statements, also known as Data Query Language (DQL) statements, are the primary method to analyze data in Spanner. They scan one or more tables or expressions and return the computed result rows. Data Definition Language (DDL) statements let you create and modify database objects such as tables, views, and database roles. Data Manipulation Language (DML) statements enable you to update, insert, and delete data from your Spanner tables. Data Access Control statements let you grant and revoke access privileges at the table and column level. Transaction Control statements allow you to manage transactions for data modifications. Was this helpful? Send feedback Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates. ",
"relevanceScore": 0.7,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/0c5c094170756eeb6bdfec6eb5c7d081",
"uri": "https://cloud.google.com/spanner/docs/reference/standard-sql/overview",
"title": "The GoogleSQL language in Spanner | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "FAQ Expand all What is Cloud SQL? Cloud SQL is a service that delivers fully managed relational databases in the cloud. It offers MySQL, PostgreSQL, and SQL Server database engines. How is Cloud SQL different from other cloud databases? Cloud SQL is valued for its openness, ease of use, security, cost-efficiency, and Google Cloud integration—in fact, more than 95% of Google Cloud's top 100 customers use it. If you're comparing PostgreSQL options on Google Cloud, view our comparison chart. What's the difference between the Enterprise and Enterprise Plus editions? For PostgreSQL, the Enterprise Plus edition brings enhanced availability, performance, and data protection capabilities. Specifically, it provides a 99.99% availability SLA with near-zero downtime maintenance, optimized hardware and software configurations, intelligent data caching for read-intensive transactional workloads, a configurable data cache option and 35 days of log retention. For MySQL, the Enterprise Plus edition brings enhanced availability, performance, and data protection capabilities. Specifically, it provides a 99.99% availability SLA with near-zero downtime maintenance, optimized hardware and software configurations, intelligent data caching for read-intensive transactional workloads, a configurable data cache option, 35 days of log retention and advanced disaster recovery capabilities like orchestrated failover and switchback. ",
"relevanceScore": 0.7,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/931f2c8e19ed54a407857f1cad3b5aaa",
"uri": "https://cloud.google.com/sql",
"title": "Cloud SQL for MySQL, PostgreSQL, and SQL Server | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "PostgreSQL versus SQL PostgreSQL is an open-source, object-relational database (ORDBMS) designed for enterprise-level performance and is valued for its reliability and robust features. Its long history of development and its use of SQL makes it one of the most popular open source databases worldwide. Its default procedural language is an extension of pgSQL (PL/pgSQL), with procedural language extensions of Tcl, Perl, and Python included in the standard distribution (written as PL/Tcl, PL/Perl, and PL/Python). Many more languages are supported through extensions, including Java, Ruby, C, C++, Delphi, and JavaScript. For a more in-depth comparison, visit our PostgreSQL versus SQL guide. MySQL versus SQL MySQL is a popular open source relational database created in 1995 and currently sponsored by Oracle. It supports SQL queries and can be administered either through a graphical user interface (GUI) or a command line. MySQL can be deployed manually on a physical machine or through a cloud service provider. Enterprises are increasingly choosing fully managed services to reduce the maintenance burden of their databases. What is SQL Server? SQL Server is a Microsoft-owned database that runs SQL queries. Dive into the differences between PostgreSQL and SQL Server. ",
"relevanceScore": 0.6,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
"uri": "https://cloud.google.com/discover/what-are-sql-databases",
"title": "SQL Databases | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "Send feedback On this page BigQuery SQL dialects Changing from the default dialect What's next Introduction to SQL in BigQuery bookmark_borderbookmark Stay organized with collections Save and categorize content based on your preferences. Dismiss Got it GoogleSQL is the new name for Google Standard SQL! New name, same great SQL dialect. This document provides an overview of supported statements and SQL dialects in BigQuery. GoogleSQL is an ANSI compliant Structured Query Language (SQL) which includes the following types of supported statements: Query statements, also known as Data Query Language (DQL) statements, are the primary method to analyze data in BigQuery. They scan one or more tables or expressions and return the computed result rows. Procedural language statements are procedural extensions to GoogleSQL that allow you to execute multiple SQL statements in one request. Procedural statements can use variables and control-flow statements, and can have side effects. Data Definition Language (DDL) statements let you create and modify database objects such as tables, views, functions, and row-level access policies. Data Manipulation Language (DML) statements enable you to update, insert, and delete data from your BigQuery tables. Data Control Language (DCL) statements let you control BigQuery system resources such as access and capacity. Transaction Control Language (TCL) statements allow you to manage transactions for data modifications. ",
"relevanceScore": 0.6,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/2f6fc3e29873518196cb50195d7ded45",
"uri": "https://cloud.google.com/bigquery/docs/introduction-sql",
"title": "Introduction to SQL in BigQuery | Google Cloud"
}
}
},
{
"chunkInfo": {
"content": "Database administration Cloud SQL pricing Connect to a Cloud SQL managed database Cloud SQL updates Configuration updates System updates What's next Home Cloud SQL Documentation Guides Was this helpful? Send feedback Cloud SQL overview bookmark_borderbookmark Stay organized with collections Save and categorize content based on your preferences. Dismiss Got it On this page Database configurations with Cloud SQL Use cases for Cloud SQL What Cloud SQL provides What is a Cloud SQL instance? Database administration Cloud SQL pricing Connect to a Cloud SQL managed database Cloud SQL updates Configuration updates System updates What's next Cloud SQL is a fully managed relational database service for MySQL, PostgreSQL, and SQL Server. This frees you from database administration tasks so that you have more time to manage your data. This page discusses basic concepts and terminology for Cloud SQL, which provides SQL data storage for Google Cloud. For a more in-depth explanation of key concepts, see the key terms and features pages. For information about how Cloud SQL databases compare with one another, see Cloud SQL feature support by database engine. Database configurations with Cloud SQL The following video shows you the benefits of using Cloud SQL. ",
"relevanceScore": 0.6,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/4098ae11bfa400e8f1b8e9ba59d2b71b",
"uri": "https://cloud.google.com/sql/docs/introduction",
"title": "Cloud SQL overview"
}
}
},
{
"chunkInfo": {
"content": "Cloud SQL documentation View all product documentation Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases on Google Cloud Platform. You can use Cloud SQL with MySQL, PostgreSQL, or SQL Server. Not sure what database option is right for you? Learn more about our database services. Learn more about Cloud SQL. Documentation resources Find quickstarts and guides, review key references, and get help with common issues. format_list_numbered Guides Cloud SQL overview Database engine feature support MySQL PostgreSQL SQL Server find_in_page Reference gcloud commands REST API Client libraries info Resources Pricing Release notes Resources Try Cloud SQL for yourself Create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. Try Cloud SQL free Was this helpful? Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates. Last updated 2024-08-29 UTC. ",
"relevanceScore": 0.5,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/37935181d99a6ad3b4897e673a7a7986",
"uri": "https://cloud.google.com/sql/docs",
"title": "Cloud SQL documentation"
}
}
}
],
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "What is SQL?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
"uri": "https://cloud.google.com/discover/what-are-sql-databases",
"title": "SQL Databases | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eSQL\u003c/b\u003e (Structured Query Language) is a programming language used to store, retrieve, and manage data in a relational database. \u003cb\u003eSQL\u003c/b\u003e statements are English-like, ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
"uri": "https://cloud.google.com/learn/postgresql-vs-sql",
"title": "PostgreSQL vs. SQL Server: What's the difference? | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eSQL\u003c/b\u003e typically uses commands written in statement format for queries and other database operations, which allow users to manipulate data in relational database ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/3afdede140d0906c2146a2f2b3a7821e",
"uri": "https://cloud.google.com/blog/topics/developers-practitioners/what-cloud-sql",
"title": "What is Cloud SQL? | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "It is a fully managed relational database for MySQL, PostgreSQL and \u003cb\u003eSQL\u003c/b\u003e Server. It reduces maintenance cost and automates database provisioning, storage ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/0c5c094170756eeb6bdfec6eb5c7d081",
"uri": "https://cloud.google.com/spanner/docs/reference/standard-sql/overview",
"title": "The GoogleSQL language in Spanner | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eGoogleSQL\u003c/b\u003e is the new name for Google Standard \u003cb\u003eSQL\u003c/b\u003e! New name, same great \u003cb\u003eSQL\u003c/b\u003e dialect. This page provides an overview of supported statements in \u003cb\u003eGoogleSQL\u003c/b\u003e.",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "NMwKDAiFm_y2BhC_nfrYAxIkNjZkYjg3NjItMDAwMC0yZTBkLTg0ZDAtMDg5ZTA4MmRjYjg0"
}
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Set the answer language code
The following command shows how to set the language code for answers.
REST
To generate an answer using a model different from the default model, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"answerLanguageCode": "
ANSWER_LANGUAGE_CODE
"
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
ANSWER_LANGUAGE_CODE
: a language code for the
answer. Use language tags defined by
BCP47: Tags for
Identifying Languages
.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "What is SQL"}, "answerGenerationSpec": {
"answerLanguageCode": "es"
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "SQL, que significa Structured Query Language, es un lenguaje de programación utilizado para almacenar, recuperar y administrar datos en una base de datos relacional. Las instrucciones de SQL son similares al inglés, lo que hace que el lenguaje sea accesible para desarrolladores de software, analistas de datos y otros profesionales. Las bases de datos SQL se utilizan para administrar y almacenar datos para apoyar numerosos casos de uso empresariales, como la inteligencia empresarial, el procesamiento de transacciones, el análisis de datos y los servicios de aprendizaje automático. SQL es el lenguaje estándar utilizado por los sistemas de gestión de bases de datos relacionales (RDBMS), incluidos PostgreSQL, SQL Server, MySQL y Oracle Database. SQL se utiliza para crear y actualizar la estructura de las tablas, leer y escribir datos, administrar los permisos de los usuarios y realizar tareas administrativas. \n",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "What is SQL?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
"uri": "https://cloud.google.com/discover/what-are-sql-databases",
"title": "SQL Databases | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eSQL\u003c/b\u003e (Structured Query Language) is a programming language used to store, retrieve, and manage data in a relational database. \u003cb\u003eSQL\u003c/b\u003e statements are English-like, ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
"uri": "https://cloud.google.com/learn/postgresql-vs-sql",
"title": "PostgreSQL vs. SQL Server: What's the difference? | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eSQL\u003c/b\u003e typically uses commands written in statement format for queries and other database operations, which allow users to manipulate data in relational database ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/3afdede140d0906c2146a2f2b3a7821e",
"uri": "https://cloud.google.com/blog/topics/developers-practitioners/what-cloud-sql",
"title": "What is Cloud SQL? | Google Cloud Blog",
"snippetInfo": [
{
"snippet": "It is a fully managed relational database for MySQL, PostgreSQL and \u003cb\u003eSQL\u003c/b\u003e Server. It reduces maintenance cost and automates database provisioning, storage ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/0c5c094170756eeb6bdfec6eb5c7d081",
"uri": "https://cloud.google.com/spanner/docs/reference/standard-sql/overview",
"title": "The GoogleSQL language in Spanner | Google Cloud",
"snippetInfo": [
{
"snippet": "\u003cb\u003eGoogleSQL\u003c/b\u003e is the new name for Google Standard \u003cb\u003eSQL\u003c/b\u003e! New name, same great \u003cb\u003eSQL\u003c/b\u003e dialect. This page provides an overview of supported statements in \u003cb\u003eGoogleSQL\u003c/b\u003e.",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
]
},
"answerQueryToken": "NMwKDAjim_y2BhDftIjEAhIkNjZkOTQ0NWQtMDAwMC0yMTBkLTllNmItZjQwMzA0NWRiZDMw"
}
In this example, although the source documents are in English, the answer is
provided in Spanish.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
def
answer_query_sample
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
AnswerQueryResponse
:
# For more information, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
client_options
=
(
ClientOptions
(
api_endpoint
=
f
"
{
location
}
-discoveryengine.googleapis.com"
)
if
location
!=
"global"
else
None
)
# Create a client
client
=
discoveryengine
.
ConversationalSearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the Search serving config
serving_config
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/servingConfigs/default_serving_config"
# Optional: Options for query phase
# The `query_understanding_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
query_understanding_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
(
query_rephraser_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryRephraserSpec
(
disable
=
False
,
# Optional: Disable query rephraser
max_rephrase_steps
=
1
,
# Optional: Number of rephrase steps
),
# Optional: Classify query types
query_classification_spec
=
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
(
types
=
[
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
ADVERSARIAL_QUERY
,
discoveryengine
.
AnswerQueryRequest
.
QueryUnderstandingSpec
.
QueryClassificationSpec
.
Type
.
NON_ANSWER_SEEKING_QUERY
,
]
# Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
),
)
# Optional: Options for answer phase
# The `answer_generation_spec` below includes all available query phase options.
# For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
answer_generation_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
(
ignore_adversarial_query
=
False
,
# Optional: Ignore adversarial query
ignore_non_answer_seeking_query
=
False
,
# Optional: Ignore non-answer seeking query
ignore_low_relevant_content
=
False
,
# Optional: Return fallback answer when content is not relevant
model_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
ModelSpec
(
model_version
=
"gemini-2.0-flash-001/answer_gen/v1"
,
# Optional: Model to use for answer generation
),
prompt_spec
=
discoveryengine
.
AnswerQueryRequest
.
AnswerGenerationSpec
.
PromptSpec
(
preamble
=
"Give a detailed answer."
,
# Optional: Natural language instructions for customizing the answer.
),
include_citations
=
True
,
# Optional: Include citations in the response
answer_language_code
=
"en"
,
# Optional: Language code of the answer
)
# Initialize request argument(s)
request
=
discoveryengine
.
AnswerQueryRequest
(
serving_config
=
serving_config
,
query
=
discoveryengine
.
Query
(
text
=
"What is Vertex AI Search?"
),
session
=
None
,
# Optional: include previous session ID to continue a conversation
query_understanding_spec
=
query_understanding_spec
,
answer_generation_spec
=
answer_generation_spec
,
)
# Make the request
response
=
client
.
answer_query
(
request
)
# Handle the response
print
(
response
)
return
response
Personalize answers
If there is specific information about the user available—for example, data in
a profile, you can specify that information in the
endUserMetadata
object so that the query results can be
personalized for the user.
For example, if a signed-in user is searching for information about upgrading a
mobile phone, information from their profile, such as current phone model and
cellular plan provides information that can personalize the generated answer.
To add personal information about the user making a query and to generate an
answer that takes into account the personal information, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"endUserSpec": {
"endUserMetadata": [
{
"chunkInfo": {
"content": "
PERSONALIZED_INFO
",
"documentMetadata": { "title": "
INFO_DESCRIPTION
"}
}
}
]
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string that contains the
question or search query.
PERSONALIZATION_INFO
: a string that contains
information specific to the user who is making the query. For example,
This customer has a
Pixel 6 Pro
purchased over a period of
24-months
starting
2023-01-15
. This customer is on the
Business Plus International
plan. No payment is due at this
time.
The length limit for this string is 8,000 characters.
INFO_DESCRIPTION
: a string that briefly
describes the personalization information—for example,
Customer
profile data, including model, plan, and billing status.
The model
makes use of both this description and the personalization information
when generating a customized answer to the query.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "Can I upgrade my phone now?"},
"answerGenerationSpec": { "includeCitations": true }
"endUserSpec": {
"endUserMetadata": [
{
"chunkInfo": {
"content": "This customer has a Pixel 6 Pro purchased over a period of 24-months starting 2023-01-15. This customer is on the Business Plus International plan. No payment is due at this time.",
"documentMetadata": { "title": "Customer profile data, including model, plan, and billing status."}
}
}
]
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "Yes, you qualify for the yearly device upgrade because you've completed your 24-month payment plan.[1,3] Since your account is fully paid you will not need to pay any additional monthly fees… \n",
"citations": [
{
"end_index": 99
"sources": [
{
"reference_id": "0"
}
]
},
{
"start_index": "100"
"end_index": "240"
"sources": [
{
"reference_id": "0"
}
]
},
...
]
"references": [
{
"chunk_info": {
"content":
"+ "This customer has a Pixel 6 Pro purchased over a period of 24-months starting 2023-01-15. This customer is on the Business Plus International plan. No payment is due at this time.",
"relevance_score": 0.3
"documentMetadata": {
"title": "Customer profile data, including model, plan, and billing status."
}
{
"chunk_info": {
"content":
"+ "For Cymbal Mobile upgrades, you can upgrade when you've paid off at least half of your current device's cost and have had it for 8 months…",
"relevance_score": 0.8
"documentMetadata": {
"document":
"projects/123456/locations/us/collections/default_collection/dataStores/my-data-store/branches/0/documents/abcd1234567890"
"uri": "https://www.example.com/help/device-upgrade"
"title": "Upgrade eligibility"
}
}
}
...
In this example, the model uses the
endUserMetadata
to customize
the answer. For illustration, this example includes citations so that you can
see the importance of the
endUserMetadata
; it's always the first
reference cited.
Generate charts for answers
The
answer
method can generate charts and return them as part of
the answer to a query.
You can specifically request that an answer include a chart, for example, "Plot
the year-on-year growth rate of small business payments over years with
available data". If the system determines that sufficient data is present, a
chart is returned. Usually, some answer text is returned along with
the chart.
Also, if there is sufficient data to create a chart, the answer method can
return a chart even if the query didn't explicitly request a chart. For example,
"What was the improvement in HDI scores associated with more access to clean
drinking water in the decade between 2010 and 2020?"
Only one chart is generated per answer. However, the chart might be a composite
chart, containing other smaller charts. An example of a composite chart:
Limitation
Queries must be in English.
Common failure scenarios
You won't always get an image returned with your answer. If there isn't
sufficient data, a figure can't be generated.
Other failure scenarios include code execution failures and timeouts. If either
of these happen, rephrase your query and try again.
Before you begin
Before you run a query that asks for generated charts, do the following:
Make sure that you are using a Gemini 2.0
or later model. For information about the models, see
Answer generation
model versions and lifecycle
.
If you have an unstructured data store that includes documents with lots of
tables and images, turn on the
Layout parser
. Although
this isn't strictly necessary, it gives better quality results.
Procedure
REST
Call the
answer
method as follows to return an answer that can
include a chart generated from the data in the data store:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"model_spec": {
"model_version": "
MODEL_VERSION
"
},
"multimodalSpec": {
"imageSource": "
IMAGE_SOURCE
"
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string in English that
contains the question or search query.
MODEL_VERSION
: Model version
gemini-2.0-flash-001/answer_gen/v1
or later. For more
information, see
Answer
generation model versions and lifecycle
.
IMAGE_SOURCE
: an enumeration to request that
the answer include a generated chart,
FIGURE_GENERATION_ONLY
,
or that the answer can include either a generated chart or an
existing
image from the data stores
,
ALL_AVAILABLE_SOURCES
.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "Plot composition of net cash used in investing activities"},
"answerGenerationSpec": {
"model_spec": {
"model_version": "gemini-2.0-flash-001/answer_gen/v1"
},
"multimodalSpec": {
"image_source": "FIGURE_GENERATION_ONLY"
}
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "The composition of net cash used in investing activities for the nine months ended September 30, 2020 and 2019 includes several categories. These categories are purchases of property and equipment, purchases of marketable securities, maturities and sales of marketable securities, purchases of non-marketable investments, maturities and sales of non-marketable investments, acquisitions net of cash acquired and purchases of intangible assets, and other investing activities. For the nine months ended September 30, 2020, the net cash used in investing activities totaled $(25,492). For the nine months ended September 30, 2019, the net cash used in investing activities totaled $(24,788).\n\nHere's a breakdown of the specific cash flows for investing activities (in millions):\n\n* **Purchases of property and equipment:** $(16,802) in 2020 and $(17,496) in 2019\n* **Purchases of marketable securities:** $(104,932) in 2020 and $(80,968) in 2019\n* **Maturities and sales of marketable securities:** $97,751 in 2020 and $74,783 in 2019\n* **Purchases of non-marketable investments:** $(1,864) in 2020 and $(1,499) in 2019\n* **Maturities and sales of non-marketable investments:** $598 in 2020 and $297 in 2019\n* **Acquisitions, net of cash acquired, and purchases of intangible assets:** $(368) in 2020 and $(373) in 2019\n* **Other investing activities:** $125 in 2020 and $468 in 2019",
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "Plot composition of net cash used in investing activities"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/b3133a895e0404984959736488992b53",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/boa-tabular/Testing_20201030-alphabet-cash flow statement.pdf",
"title": "Testing_20201030-alphabet-cash flow statement",
"snippetInfo": [
{
"snippet": "... \u003cb\u003eNet cash provided by operating activities\u003c/b\u003e 42,447 | 40,093 | | \u003cb\u003eInvesting activities\u003c/b\u003e | | | (16,802) Purchases of property and equipment | (17,496) ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
],
"blobAttachments": [
{
"data": {
"mimeType": "image/png",
"data": "iVBORw0KGgoAAAANSUhEUgAACvAAZd8AEZFKHDp0CE5OTgCAZcuWYfr06QonIqIMXIGXiIhUITY2Vq4tLCxyNdbMzEyuk5OTtZaJiEgfZd5aMj4+Xq4zr1rztm3SMs/fXIGXiOjDGRgYyLWpqalcJyUlyfW/V7rJULVqVbl++PChDtIREemXr7766oPHPnr0CK1bt9ZeGCIiPXXlypWPGr9lyxYtJSEi0k9ly5bFzZs30bNnT0iSBEmS8PLlS1y6dAlHjhzBpUuX8PLlS/lcjx49cOPGDZQtW1bp6EREquHv7w9JkgAALVq0UDgNEWXGBl4iIlIFc3NzuY6MjMzV2ICAALkuVqyY1jIREemjzDdVb926JdeWlpZynXlr98z8/f3lunDhwtoPR0SkJzLPuYGBgXKd+bOun5/fG8dmXjE9PT1dB+mIiPTL8uXLP2hVm19++QV169aFt7e3DlIREemXDh06wMfHJ9fjwsLC0K1bN4wePVoHqYiI9EuRIkXwxx9/4MSJE3BycoKFhYXcsCtJEiwsLNC/f38cP34chw4dyrJQBBERfbxChQrJde...PrTn86//Mu/5Jhjjql1NACAAeP/AX0CwI314+qiAAAAAElFTkSuQmCC"
},
"attributionType": "GENERATED"
}
]
},
"answerQueryToken": "NMwKDAjEjOe-BhD-meX6ARIkNjdkNjBhM2QtMDAwMC0yYzU4LTgxYjctMDg5ZTA4MmNhZDgw"
In this example, a generated chart is included in the answer because the
query requested a plot and there was enough data to generate the chart.
The charts images are returned in the
blobAttachments
output with the
attributionType
of
GENERATED
.
Retrieve existing images from the data store
You can choose to have images from the data store returned with the answer and
in
citation
references. The data store must be an unstructured
data store with the layout parser turned on.
When
imageSource
is
CORPUS_IMAGE_ONLY
or
ALL_AVAILABLE_SOURCES
, then the
answer
method can retrieve images from the data store as
appropriate. However, turning this on doesn't mean that images are always
returned.
You get one image (maximum) per answer. Citations can contain multiple images.
Limitations
The app that you're using must be connected to an unstructured data store.
Images can't be returned from websites or from structured data stores.
Queries must be in English.
Before you begin
Before you run a query to retrieve images, do the following:
Contact your Google account team and ask to be added to the allowlist for
image identification and annotation.
Turn on
Enable image annotation
for the unstructured data store from
which you want to retrieve images:
On the
Data
page for the data store, click
Processing config
.
Set the
Default document parser
to
Layout Parser
.
Select
Enable image annotation
.
Procedure
REST
Call the
answer
method as follows to return an answer that can
include an image from the data store in the answer:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer" \
-d '{
"query": { "text": "
QUERY
"},
"answerGenerationSpec": {
"model_spec": {
"model_version": "
MODEL_VERSION
"
},
includeCitations: true,
"multimodalSpec": {
"imageSource": "
IMAGE_SOURCE
"
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app that you
want to query.
QUERY
: a free-text string in English that
contains the question or search query.
MODEL_VERSION
: Model version
gemini-2.0-flash-001/answer_gen/v1
or later. For more
information, see
Answer
generation model versions and lifecycle
.
IMAGE_SOURCE
: an enumeration to request that
the answer include an image from the data store,
CORPUS_IMAGE_ONLY
, or that the answer can include either an
image from the data store or a
generated chart
,
ALL_AVAILABLE_SOURCES
.
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/my-project-123//locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer" -d '{
"query": { "text": "Display the ranking of generations from highest to lowest based on their spending on holiday items using cards."},
"answerGenerationSpec": {"includeCitations": true,
"model_spec": {
"model_version": "gemini-2.0-flash-001/answer_gen/v1"
},
"multimodalSpec": {
"imageSource": "CORPUS_IMAGE_ONLY"
}
},
"searchSpec": {
"searchParams": {
"maxReturnResults": 5
}
}
}'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "Holiday spending over November-December was weakest among Gen Xers, followed by Millennials, while Baby Boomer spending was relatively more solid. In November, Baby Boomers saw solid spending growth. Both Millennials and Gen X consumers had lower holiday spending than in the same 30-day period last year. Baby Boomers' holiday spending started to pick up from the start of November and continued to rise throughout the month. Meanwhile, Millennials started to ramp up their holiday spending much later in the month. Gen X consumers consistently outspent other generations from late October through the end of November.\n",
"citations": [
{
"endIndex": "146",
"sources": [
{
"referenceId": "3"
}
]
},
{
"startIndex": "147",
"endIndex": "199",
"sources": [
{
"referenceId": "2"
}
]
},
{
"startIndex": "200",
"endIndex": "305",
"sources": [
{
"referenceId": "2"
}
]
},
{
"startIndex": "306",
"endIndex": "426",
"sources": [
{
"referenceId": "2"
}
]
},
{
"startIndex": "427",
"endIndex": "516",
"sources": [
{
"referenceId": "2"
}
]
},
{
"startIndex": "517",
"endIndex": "619",
"sources": [
{
"referenceId": "2"
}
]
}
],
"references": [
{
"chunkInfo": {
"content": "Bank of America aggregated credit/debit card spending per household includes spending from active US households only. Only.., Consumer and Small Business Mel Roasa Vice President, Digital and MarketingBANK OF AMERICA INSTITUTE09 November 20237",
"relevanceScore": 0.5,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f8d7887862167c5daf6c7a30e1d464e0",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1WkoquhDpqHphSnqIVKX45iers7kvmGjZ.pdf",
"title": "1WkoquhDpqHphSnqIVKX45iers7kvmGjZ",
"pageIdentifier": "6"
}
}
},
{
"chunkInfo": {
"content": "Bank of America aggregated credit/debit card spending per household includes spending from active US households only. Only... Digital and Marketing Riley Fillius Vice President, Digital and MarketingBANK OF AMERICA INSTITUTE08 February 2024 7",
"relevanceScore": 0.4,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/c4308d8610bcae3b3d2bb916090ef28b",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1B3MJqELqk_S26aWb-KnLdSWwmpuB32os.pdf",
"title": "1B3MJqELqk_S26aWb-KnLdSWwmpuB32os",
"pageIdentifier": "6"
}
}
},
...
{
"chunkInfo": {
"content": "Bank of America aggregated credit/debit card spending per household includes spending from active US households only. Only consumer card holders making a minimum of five transactions a month are included in the dataset. Spending from corporate cards are excluded. Data regarding merchants who receive payments are identified and classified by the Merchant Categorization Code (MCC) defined by financial services companies. The data are mapped using proprietary methods from the MCCs to the North American Industry Classification System (NAICS), which is also used by the Census Bureau, in order to classify spending data by subsector. Spending data may also be classified by other proprietary methods not using MCCs. Generations, if discussed, are defined as follows: 1. Gen Z, born after 1995 2. Younger Millennials: born between 1989-1995 3. Older Millennials: born between 1978-19886 11 March 2024BANK OF AMERICA INSTITUTE4. Gen Xers: born between 1965-1977 5. Baby Boomer: 1946-1964 6. Traditionalists: pre-1946 Any reference to card spending per household on gasoline includes all purchases at gasoline stations and might include purchases of non-gas items. Additional information about the methodology used to aggregate the data is available upon request.\n\n## Contributors\n\nDavid Michael Tinsley Senior Economist, Bank of America Institute Joe Wadford Economist, Bank of America Institute Taylor Bowley Economist, Bank of America Institute Liz Everett Krisberg Head of Bank of America Institute\n\n## Sources\n\nLi Wei Director, Global Risk Analytics Kimberly Warren Director, Global Risk Analytics Ana Maxim Senior Vice President, Consumer and Small Business Mel Roasa Vice President, Digital and MarketingBANK OF AMERICA INSTITUTE11 March 2024 7",
"relevanceScore": 0.3,
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/719bfb7c1c0cde3888debd43542aabfe",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1odEo6QRllsURLZRDwHNruCXK9bsWmhtR.pdf",
"title": "1odEo6QRllsURLZRDwHNruCXK9bsWmhtR",
"pageIdentifier": "6"
}
}
}
],
"steps": [
{
"state": "SUCCEEDED",
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": "Rank generations from highest to lowest based on their spending on holiday items using cards."
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/935c4e1f18ccff2b5fa51d6d00e40dc4",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1baMNJuizoK7u3P2-gYRwpVz_46-uOhn4.pdf",
"title": "1baMNJuizoK7u3P2-gYRwpVz_46-uOhn4",
"snippetInfo": [
{
"snippet": "## Exhibit 6: Credit and debit \u003cb\u003ecard spending\u003c/b\u003e per household on \u003cb\u003eholiday items\u003c/b\u003e by \u003cb\u003egeneration\u003c/b\u003e (index, Aug-Sep average=100 for each year, 7- day moving average) ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/0b4c8cfb6f5ed9ef0df70ffcd79fe2c0",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1pVkzcMDNAy-p7AlrE0LRlhpbbDzCNndJ.pdf",
"title": "1pVkzcMDNAy-p7AlrE0LRlhpbbDzCNndJ",
"snippetInfo": [
{
"snippet": "Consumer \u003cb\u003espending\u003c/b\u003e finished solidly in 2023, \u003cb\u003ewith\u003c/b\u003e total \u003cb\u003ecard spending\u003c/b\u003e per household increasing by 0.2% year-over-year (YoY) in December, according to Bank of ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f8d7887862167c5daf6c7a30e1d464e0",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1WkoquhDpqHphSnqIVKX45iers7kvmGjZ.pdf",
"title": "1WkoquhDpqHphSnqIVKX45iers7kvmGjZ",
"snippetInfo": [
{
"snippet": "This could be due to an increasing customer \u003cb\u003ebase\u003c/b\u003e or inactive customers \u003cb\u003eusing their cards\u003c/b\u003e more frequently. Per household \u003cb\u003ecard spending\u003c/b\u003e growth only looks at ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/719bfb7c1c0cde3888debd43542aabfe",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1odEo6QRllsURLZRDwHNruCXK9bsWmhtR.pdf",
"title": "1odEo6QRllsURLZRDwHNruCXK9bsWmhtR",
"snippetInfo": [
{
"snippet": "This could be due to an increasing customer \u003cb\u003ebase\u003c/b\u003e or inactive customers \u003cb\u003eusing their cards\u003c/b\u003e more frequently. Per household \u003cb\u003ecard spending\u003c/b\u003e growth only looks at ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/c4308d8610bcae3b3d2bb916090ef28b",
"uri": "gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806/Document Understanding Evaluation Dataset/Bank of America/1B3MJqELqk_S26aWb-KnLdSWwmpuB32os.pdf",
"title": "1B3MJqELqk_S26aWb-KnLdSWwmpuB32os",
"snippetInfo": [
{
"snippet": "This could be due to an increasing customer \u003cb\u003ebase\u003c/b\u003e or inactive customers \u003cb\u003eusing their cards\u003c/b\u003e more frequently. Per household \u003cb\u003ecard spending\u003c/b\u003e growth only looks at ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
}
]
}
],
"blobAttachments": [
{
"data": {
"mimeType": "image/png",
"data": "iVBORw0KGgoAAAANSUhEUgAABcwAAAIjCAIAAACxms+ZAAAgAElEQVR42uzdd1xTV/...Vv/F0NDQ4NOp3+waz94PJ5Op7+/ibro6fRiWPX/AaZ6/dAGW00gAAAAAElFTkSuQmCC"
},
"attributionType": "CORPUS"
}
]
},
"answerQueryToken": "M8gKCwiPuOe-BhDyhpgIEiQ2N2Q2MWI0Mi0wMDAwLTJjNTgtODFiNy0wODllMDgyY2FkODA"
}
The images are returned in the
blobAttachments
portion of the
output. The image that is returned with the answer is always in the first
blobAttachments
. If present, other
blobAttachments
would contain images returned in citation references. The image returned with
the answer can also be (in fact often is) also returned with a citation. The
blobAttachmentIndexes
is the index that associates the
blobAttachment
to the answer or citation text.
The
attributionType
for returned images is always
CORPUS
to indicate that the image is from the data store.
Commands for follow-up questions
Follow-ups are multi-turn queries. After the first query in a follow-up session, subsequent
"turns" take into account prior interactions. With follow-ups, the answer method
can also suggest related questions, which your users can choose instead of
entering their own follow-up questions.
All the answer and follow-ups features described in the preceding sections, such as
citations, filters, SafeSearch, ignoring certain types of queries, and using a
preamble to customize answers can be applied along with follow-ups.
Example of a follow-up session
The following is an example of a session with follow-ups. Suppose that you want
to know about vacationing in Mexico:
Turn 1:
You:
When is the best time of the year to vacation in Mexico?
Answer with follow-ups:
The best time to vacation in Mexico is during the dry
season, which runs from November to April.
Turn 2:
You:
What is the exchange rate?
Answer with follow-ups:
1 USD is equal to approximately 17.65 Mexican pesos.
Turn 3:
You:
What's the average temperature in December?
Answer with follow-ups:
The average temperature varies from 70-78°F.
Cancun's average is ~ 77°F.
Without follow-ups, your question "What is the exchange rate?" wouldn't be
answerable because regular search wouldn't know that you wanted the Mexican
exchange rate. Similarly, without follow-ups, there wouldn't be the context
needed to give you temperatures specifially for Mexico.
Examples of related questions
When you ask "What is the best time of the year to vacation in
Mexico?", in addition to answering your question, answer and follow-ups can suggest other
questions that you might ask, such as "What is the cheapest month
to vacation in Mexico?" and "What are the tourist months in Mexico?".
After the related questions feature is enabled, questions are returned as
strings in the
ConverseConversationResponse
.
About sessions
To understand how follow-ups work in Vertex AI Search, you need
to understand about sessions.
A session is made up of text queries provided by a
user and responses provided by Vertex AI Search.
These query and response pairs are sometimes referred to as
turns
. In the
preceding example, the second turn is made up of "What is the exchange rate?"
and "1 USD is equal to approximately 17.65 Mexican pesos."
Sessions are stored with the app.
In the app, a session is represented by the
session
resource
.
In addition to containing the query and response messages, the session
resource has:
A unique name (the session ID).
A state (in-progress or completed).
A user pseudo ID, which is a visitor ID that tracks the user. It can be
assigned programmatically.
A start time and an end time.
A turn, which is a query answer pair.
Store session information and get responses
You can use the command line to generate search responses and answers
and to store these, along with each query in a session.
REST
To use the command line to create a session and generate responses from the
user's input, follow these steps:
Specify the app where you want to store the session:
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions"
\
-d
'{
"userPseudoId": "
USER_PSEUDO_ID
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
USER_PSEUDO_ID
: This is a unique identifier for
tracking a search visitor. For example, you can implement this with an
HTTP cookie, which uniquely identifies a visitor on a single device.
Example command and result
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
-H
"Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/sessions"
-d
'{
"userPseudoId": "test_user"
}'
{
"name"
:
"projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943"
,
"state"
:
"IN_PROGRESS"
,
"userPseudoId"
:
"test_user"
,
"startTime"
:
"2024-09-13T18:47:10.465311Z"
,
"endTime"
:
"2024-09-13T18:47:10.465311Z"
}
Note down the session ID, the numbers at the end of the
name:
field in the
JSON response. In the example result, the ID is
5386462384953257772
.
You need this ID in the next step.
Generate an answer and add it to a session in your app:
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
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:answer"
\
-d
'{
"query": { "text": "
QUERY
"},
"session": "projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions/
SESSION_ID
",
"searchSpec":{ "searchParams": {"filter": "
FILTER
"} }
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY
: a free-text string that contains the
question or search query.
SESSION_ID
: the ID for the session that you
created in step 1. These are the digits at the end of the
name:
field, noted step 2. For a session, use the same
session ID in every turn.
FILTER
: a text field for filtering search
using a filter expression. The default value is an empty string. The
way you construct your filter varies depending on whether you have
unstructured data with metadata, structured data, or
website data. For more information,
see
Filter
generic search for structured or unstructured data
and
Filter
website search
.
Example command and result
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
-H
"Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:answer"
-d
'{
"query": { "text": "Compare bigquery with spanner database?"},
"session": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943",
}'
{
"answer"
:
{
"name"
:
"projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943/answers/4861507376861383072"
,
"state"
:
"SUCCEEDED"
,
"answerText"
:
"BigQuery and Spanner are both powerful tools that can be used together to handle transactional and analytical workloads. Spanner is a fully managed relational database optimized for transactional workloads, while BigQuery is a serverless data warehouse designed for business agility. Spanner provides seamless replication across regions in Google Cloud and processes over 1 billion requests per second at peak. BigQuery analyzes over 110 terabytes of data per second. Users can leverage federated queries to read data from Spanner and write to a native BigQuery table. \n"
,
"steps"
:
[
{
"state"
:
"SUCCEEDED"
,
"description"
:
"Rephrase the query and search."
,
"actions"
:
[
{
"searchAction"
:
{
"query"
:
"Compare bigquery with spanner database?"
}
,
"observation"
:
{
"searchResults"
:
[
{
"document"
:
"projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/ecc0e7547253f4ca3ff3328ce89995af"
,
"uri"
:
"https://cloud.google.com/blog/topics/developers-practitioners/how-spanner-and-bigquery-work-together-handle-transactional-and-analytical-workloads"
,
"title"
:
"How Spanner and BigQuery work together to handle transactional and analytical workloads | Google Cloud Blog"
,
"snippetInfo"
:
[
{
"snippet"
:
"Using Cloud \u003cb\u003eSpanner\u003c/b\u003e and \u003cb\u003eBigQuery\u003c/b\u003e also allows customers to build their \u003cb\u003edata\u003c/b\u003e clouds using Google Cloud, a unified, open approach to \u003cb\u003edata\u003c/b\u003e-driven transformation ..."
,
"snippetStatus"
:
"SUCCESS"
}
]
}
,
{
"document"
:
"projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/d7e238f73608a860e00b752ef80e2941"
,
"uri"
:
"https://cloud.google.com/blog/products/databases/cloud-spanner-gets-stronger-with-bigquery-federated-queries"
,
"title"
:
"Cloud Spanner gets stronger with BigQuery-federated queries | Google Cloud Blog"
,
"snippetInfo"
:
[
{
"snippet"
:
"As enterprises compete for market share, their need for real-time insights has given rise to increased demand for transactional \u003cb\u003edatabases\u003c/b\u003e to support \u003cb\u003edata\u003c/b\u003e ..."
,
"snippetStatus"
:
"SUCCESS"
}
]
}
,
{
"document"
:
"projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/e10a5a3c267dc61579e7c00fefe656eb"
,
"uri"
:
"https://cloud.google.com/blog/topics/developers-practitioners/replicating-cloud-spanner-bigquery-scale"
,
"title"
:
"Replicating from Cloud Spanner to BigQuery at scale | Google Cloud Blog"
,
"snippetInfo"
:
[
{
"snippet"
:
"... \u003cb\u003eSpanner data\u003c/b\u003e into \u003cb\u003eBigQuery\u003c/b\u003e for analytics. In this post, you will learn how to efficiently use this feature to replicate large tables with high throughput ..."
,
"snippetStatus"
:
"SUCCESS"
}
]
}
,
...
{
"document"
:
"projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/8100ad36e1cac149eb9fc180a41d8f25"
,
"uri"
:
"https://cloud.google.com/blog/products/gcp/from-nosql-to-new-sql-how-spanner-became-a-global-mission-critical-database"
,
"title"
:
"How Spanner became a global, mission-critical database | Google Cloud Blog"
,
"snippetInfo"
:
[
{
"snippet"
:
"... SQL \u003cb\u003evs\u003c/b\u003e. NoSQL dichotomy may no longer be relevant."
The
\u
003cb
\u
003eSpanner
\u
003c/b
\u
003e
SQL
query
processor,
while
recognizable
as
a
standard
implementation,
has
unique ...
",
"
snippetStatus
": "
SUCCESS
"
}
]
}
]
}
}
]
}
]
},
"
session
": {
"
name
": "
projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943
",
"
state
": "
IN_PROGRESS
",
"
userPseudoId
": "
test_user
",
"
turns
": [
{
"
query
": {
"
queryId
": "
projects/123456/locations/global/questions/741830
",
"
text
": "
Compare
bigquery
with
spanner
database?
"
},
"
answer
": "
projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943/answers/4861507376861383072
"
}
],
"
startTime
": "
2024
-09-13T18:47:10.465311Z
",
"
endTime
": "
2024
-09-13T18:47:10.465311Z
"
},
"
answerQueryToken
": "
NMwKDAjFkpK3BhDU24uZAhIkNjZlNDIyZWYtMDAwMC0yMjVmLWIxMmQtZjQwMzA0M2FkYmNj
"
}
Repeat step 3 for each new query in the session.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
def
create_session
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
user_pseudo_id
:
str
,
)
-
>
discoveryengine
.
Session
:
"""Creates a session.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
user_pseudo_id: A unique identifier for tracking visitors. For example, this
could be implemented with an HTTP cookie, which should be able to
uniquely identify a visitor on a single device.
Returns:
discoveryengine.Session: The newly created Session.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
session
=
client
.
create_session
(
# The full resource name of the engine
parent
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
"
,
session
=
discoveryengine
.
Session
(
user_pseudo_id
=
user_pseudo_id
),
)
# Send Session name in `answer_query()`
print
(
f
"Session:
{
session
.
name
}
"
)
return
session
Get a session from the data store
The following command shows how to call the
get
method and
get a session from the data store.
REST
To get a session from a data store, do the following:
Run the following curl command:
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions/
SESSION_ID
"
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
SESSION_ID
: the ID of the session that you
want to get.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
def
get_session
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
session_id
:
str
,
)
-
>
discoveryengine
.
Session
:
"""Retrieves a session.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
session_id: The ID of the session.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
# The full resource name of the session
name
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/sessions/
{
session_id
}
"
session
=
client
.
get_session
(
name
=
name
)
print
(
f
"Session details:
{
session
}
"
)
return
session
Delete a session from the app
The following command shows how to call the
delete
method and
delete a session from the data store.
By default, sessions older than 60 days are automatically deleted.
However, if you want to delete a particular session—for example, if it
contains sensitive content, then use this API call to delete it.
REST
To delete a session from an app, do the following:
Run the following curl command:
curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions/
SESSION_ID
"
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
SESSION_ID
: the ID of the session that you
want to delete.
Example command and result
curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943"
{}
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
def
delete_session
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
session_id
:
str
,
)
-
>
None
:
"""Deletes a session.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
session_id: The ID of the session.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
# The full resource name of the session
name
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/sessions/
{
session_id
}
"
client
.
delete_session
(
name
=
name
)
print
(
f
"Session
{
name
}
deleted."
)
Update a session
There are various reasons that you might want to update a session. For example,
to do one of the following:
Mark a session as completed
Merge the messages from one session into another
Change a user's pseudo ID
The following command shows how to call the
patch
method and
update a session in the data store.
REST
To update a session from an app, do the following:
Run the following curl command:
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions/
SESSION_ID
?updateMask=state" \
-d '{
"state": "
NEW_STATE
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
SESSION_ID
: the ID of the session that you
want to update.
NEW_STATE
: the new value for the state—for
example,
IN_PROGRESS
.
Example command and result
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943?updateMask=state"
-d '{
"state": "IN_PROGRESS"
}'
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943",
"state": "IN_PROGRESS",
"userPseudoId": "test_user",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/741830",
"text": "Compare bigquery with spanner database?"
},
"answer": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943/answers/4861507376861383072"
}
],
"startTime": "2024-09-13T18:47:10.465311Z",
"endTime": "2024-09-13T18:49:41.579151Z"
}
This example changes the state of the session to open (in progress). Follow a similar pattern to update the
userPseudoId
.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
from
google.protobuf
import
field_mask_pb2
def
update_session
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
session_id
:
str
,
)
-
>
discoveryengine
.
Session
:
"""Updates a session.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
session_id: The ID of the session.
Returns:
discoveryengine.Session: The updated Session.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
# The full resource name of the session
name
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
/sessions/
{
session_id
}
"
session
=
discoveryengine
.
Session
(
name
=
name
,
state
=
discoveryengine
.
Session
.
State
.
IN_PROGRESS
,
# Options: IN_PROGRESS, STATE_UNSPECIFIED
)
# Fields to Update
update_mask
=
field_mask_pb2
.
FieldMask
(
paths
=
[
"state"
])
session
=
client
.
update_session
(
session
=
session
,
update_mask
=
update_mask
)
print
(
f
"Updated session:
{
session
.
name
}
"
)
return
session
List all sessions
The following command shows how to call the
list
method and
list the sessions in the data store.
REST
To list the sessions for an app, do the following:
Run the following curl command:
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions"
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
Example command and result
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/sessions"
{
"sessions": [
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/10000135306311111817",
"state": "IN_PROGRESS",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/10000135306311114276",
"text": "bugs reported by tiktok on grounding"
}
}
],
"startTime": "2024-09-03T00:38:40.338623Z",
"endTime": "2024-09-03T00:38:40.338623Z"
},
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/10000827040519035859",
"state": "IN_PROGRESS",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/10000827040519033518",
"text": "GDM models"
}
}
],
"startTime": "2024-07-19T15:53:06.521775Z"
},
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/10003910515245149877",
"state": "IN_PROGRESS",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/10003910515245148378",
"text": "gyorgyattila"
},
"answer": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/10003910515245149877/answers/17036357111873257990"
}
],
"startTime": "2024-08-08T11:40:04.632463Z",
"endTime": "2024-08-08T11:40:04.632463Z"
},
...
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/10198752942940073431",
"state": "IN_PROGRESS",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/10198752942940071818",
"text": "hello"
},
"answer": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/10198752942940073431/answers/13411441797796265380"
}
],
"startTime": "2024-08-14T17:30:21.203439Z",
"endTime": "2024-08-14T17:30:21.203439Z"
}
],
"nextPageToken": "IDEDgIwL_vuieLC"
}
The response contains a list of sessions and the nextPageToken. If no
nextPageToken is returned, there are no more sessions to list. Default page
size is 50.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
def
list_sessions
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
ListSessionsResponse
:
"""Lists all sessions associated with a data store.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
Returns:
discoveryengine.ListSessionsResponse: The list of sessions.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
# The full resource name of the engine
parent
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
"
response
=
client
.
list_sessions
(
request
=
discoveryengine
.
ListSessionsRequest
(
parent
=
parent
,
filter
=
'state="IN_PROGRESS"'
,
# Optional: Filter requests by userPseudoId or state
order_by
=
"update_time"
,
# Optional: Sort results
)
)
print
(
"Sessions:"
)
for
session
in
response
.
sessions
:
print
(
session
)
return
response
List sessions for a user
The following command shows how to call the
list
method to
list sessions associated with a user or visitor.
REST
To list sessions associated with a user or visitor, do the following:
Run the following curl command:
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions?filter=userPseudoId=
USER_PSEUDO_ID
"
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
USER_PSEUDO_ID
: the pseudo ID of the user
whose sessions you want to list.
Example command and result
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/sessions?filter=userPseudoId=test_user"
{
"sessions": [
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943",
"state": "IN_PROGRESS",
"userPseudoId": "test_user",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/741830",
"text": "Compare bigquery with spanner database?"
},
"answer": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943/answers/4861507376861383072"
}
],
"startTime": "2024-09-13T18:47:10.465311Z",
"endTime": "2024-09-13T18:49:41.579151Z"
}
]
}
In this example, there is one session associated with the test_user. The
queries and answers in the session are listed.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
def
list_sessions
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
ListSessionsResponse
:
"""Lists all sessions associated with a data store.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
Returns:
discoveryengine.ListSessionsResponse: The list of sessions.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
# The full resource name of the engine
parent
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
"
response
=
client
.
list_sessions
(
request
=
discoveryengine
.
ListSessionsRequest
(
parent
=
parent
,
filter
=
'state="IN_PROGRESS"'
,
# Optional: Filter requests by userPseudoId or state
order_by
=
"update_time"
,
# Optional: Sort results
)
)
print
(
"Sessions:"
)
for
session
in
response
.
sessions
:
print
(
session
)
return
response
List sessions for a user and state
The following command shows how to call the
list
method to
list sessions in a given state for a particular user.
REST
To list sessions for a user that are open or closed and associated with a given
user or visitor, do the following:
Run the following curl command:
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/sessions?filter=userPseudoId=
USER_PSEUDO_ID
%20AND%20state=
STATE
"
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
USER_PSEUDO_ID
: the pseudo ID of the user
whose sessions you want to list.
STATE
: the state of the session:
STATE_UNSPECIFIED
(closed or unknown) or
IN_PROGRESS
(open).
Example command and result
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/engines/my-app/sessions?filter=userPseudoId=test_user%20AND%20state=IN_PROGRESS"
{
"sessions": [
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943",
"state": "IN_PROGRESS",
"userPseudoId": "test_user",
"turns": [
{
"query": {
"queryId": "projects/123456/locations/global/questions/741830",
"text": "Compare bigquery with spanner database?"
},
"answer": "projects/123456/locations/global/collections/default_collection/engines/my-app/sessions/16002628354770206943/answers/4861507376861383072"
}
],
"startTime": "2024-09-13T18:47:10.465311Z",
"endTime": "2024-09-13T18:49:41.579151Z"
}
]
}
The expected result is an empty response.
Python
For more information, see the
AI Applications
Python
API
reference documentation
.
To authenticate to AI Applications, set up Application Default Credentials.
For more information, see
Set up authentication for a local development environment
.
from
google.cloud
import
discoveryengine_v1
as
discoveryengine
def
list_sessions
(
project_id
:
str
,
location
:
str
,
engine_id
:
str
,
)
-
>
discoveryengine
.
ListSessionsResponse
:
"""Lists all sessions associated with a data store.
Args:
project_id: The ID of your Google Cloud project.
location: The location of the app.
engine_id: The ID of the app.
Returns:
discoveryengine.ListSessionsResponse: The list of sessions.
"""
client
=
discoveryengine
.
ConversationalSearchServiceClient
()
# The full resource name of the engine
parent
=
f
"projects/
{
project_id
}
/locations/
{
location
}
/collections/default_collection/engines/
{
engine_id
}
"
response
=
client
.
list_sessions
(
request
=
discoveryengine
.
ListSessionsRequest
(
parent
=
parent
,
filter
=
'state="IN_PROGRESS"'
,
# Optional: Filter requests by userPseudoId or state
order_by
=
"update_time"
,
# Optional: Sort results
)
)
print
(
"Sessions:"
)
for
session
in
response
.
sessions
:
print
(
session
)
return
response
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
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 2 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 3 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 4 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 5 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 6 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 7 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 8 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 9 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 10 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 11 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"


def answer_query_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.AnswerQueryResponse:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # The full resource name of the Search serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_serving_config"

    # Optional: Options for query phase
    # The `query_understanding_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/QueryUnderstandingSpec
    query_understanding_spec = discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec(
        query_rephraser_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec(
            disable=False,  # Optional: Disable query rephraser
            max_rephrase_steps=1,  # Optional: Number of rephrase steps
        ),
        # Optional: Classify query types
        query_classification_spec=discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec(
            types=[
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.ADVERSARIAL_QUERY,
                discoveryengine.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type.NON_ANSWER_SEEKING_QUERY,
            ]  # Options: ADVERSARIAL_QUERY, NON_ANSWER_SEEKING_QUERY or both
        ),
    )

    # Optional: Options for answer phase
    # The `answer_generation_spec` below includes all available query phase options.
    # For more details, refer to https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/AnswerGenerationSpec
    answer_generation_spec = discoveryengine.AnswerQueryRequest.AnswerGenerationSpec(
        ignore_adversarial_query=False,  # Optional: Ignore adversarial query
        ignore_non_answer_seeking_query=False,  # Optional: Ignore non-answer seeking query
        ignore_low_relevant_content=False,  # Optional: Return fallback answer when content is not relevant
        model_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec(
            model_version="gemini-2.0-flash-001/answer_gen/v1",  # Optional: Model to use for answer generation
        ),
        prompt_spec=discoveryengine.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec(
            preamble="Give a detailed answer.",  # Optional: Natural language instructions for customizing the answer.
        ),
        include_citations=True,  # Optional: Include citations in the response
        answer_language_code="en",  # Optional: Language code of the answer
    )

    # Initialize request argument(s)
    request = discoveryengine.AnswerQueryRequest(
        serving_config=serving_config,
        query=discoveryengine.Query(text="What is Vertex AI Search?"),
        session=None,  # Optional: include previous session ID to continue a conversation
        query_understanding_spec=query_understanding_spec,
        answer_generation_spec=answer_generation_spec,
    )

    # Make the request
    response = client.answer_query(request)

    # Handle the response
    print(response)

    return response


```

### Code Example 12 (text)

```text
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions" \
  -d '{
        "userPseudoId": "USER_PSEUDO_ID"
      }'

```

### Code Example 13 (text)

```text
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:answer" \
  -d '{
        "query": { "text": "QUERY"},
        "session": "projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions/SESSION_ID",
          "searchSpec":{ "searchParams": {"filter": "FILTER"} }
}'

```

### Code Example 14 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine


def create_session(
    project_id: str,
    location: str,
    engine_id: str,
    user_pseudo_id: str,
) -> discoveryengine.Session:
    """Creates a session.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
        user_pseudo_id: A unique identifier for tracking visitors. For example, this
          could be implemented with an HTTP cookie, which should be able to
          uniquely identify a visitor on a single device.
    Returns:
        discoveryengine.Session: The newly created Session.
    """

    client = discoveryengine.ConversationalSearchServiceClient()

    session = client.create_session(
        # The full resource name of the engine
        parent=f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}",
        session=discoveryengine.Session(user_pseudo_id=user_pseudo_id),
    )

    # Send Session name in `answer_query()`
    print(f"Session: {session.name}")
    return session


```

### Code Example 15 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine


def get_session(
    project_id: str,
    location: str,
    engine_id: str,
    session_id: str,
) -> discoveryengine.Session:
    """Retrieves a session.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
        session_id: The ID of the session.
    """

    client = discoveryengine.ConversationalSearchServiceClient()

    # The full resource name of the session
    name = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/sessions/{session_id}"

    session = client.get_session(name=name)

    print(f"Session details: {session}")
    return session


```

### Code Example 16 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine


def delete_session(
    project_id: str,
    location: str,
    engine_id: str,
    session_id: str,
) -> None:
    """Deletes a session.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
        session_id: The ID of the session.
    """

    client = discoveryengine.ConversationalSearchServiceClient()

    # The full resource name of the session
    name = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/sessions/{session_id}"

    client.delete_session(name=name)

    print(f"Session {name} deleted.")


```

### Code Example 17 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine
from google.protobuf import field_mask_pb2


def update_session(
    project_id: str,
    location: str,
    engine_id: str,
    session_id: str,
) -> discoveryengine.Session:
    """Updates a session.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
        session_id: The ID of the session.
    Returns:
        discoveryengine.Session: The updated Session.
    """
    client = discoveryengine.ConversationalSearchServiceClient()

    # The full resource name of the session
    name = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/sessions/{session_id}"

    session = discoveryengine.Session(
        name=name,
        state=discoveryengine.Session.State.IN_PROGRESS,  # Options: IN_PROGRESS, STATE_UNSPECIFIED
    )

    # Fields to Update
    update_mask = field_mask_pb2.FieldMask(paths=["state"])

    session = client.update_session(session=session, update_mask=update_mask)
    print(f"Updated session: {session.name}")
    return session


```

### Code Example 18 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine


def list_sessions(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.ListSessionsResponse:
    """Lists all sessions associated with a data store.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
    Returns:
        discoveryengine.ListSessionsResponse: The list of sessions.
    """

    client = discoveryengine.ConversationalSearchServiceClient()

    # The full resource name of the engine
    parent = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}"

    response = client.list_sessions(
        request=discoveryengine.ListSessionsRequest(
            parent=parent,
            filter='state="IN_PROGRESS"',  # Optional: Filter requests by userPseudoId or state
            order_by="update_time",  # Optional: Sort results
        )
    )

    print("Sessions:")
    for session in response.sessions:
        print(session)

    return response


```

### Code Example 19 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine


def list_sessions(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.ListSessionsResponse:
    """Lists all sessions associated with a data store.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
    Returns:
        discoveryengine.ListSessionsResponse: The list of sessions.
    """

    client = discoveryengine.ConversationalSearchServiceClient()

    # The full resource name of the engine
    parent = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}"

    response = client.list_sessions(
        request=discoveryengine.ListSessionsRequest(
            parent=parent,
            filter='state="IN_PROGRESS"',  # Optional: Filter requests by userPseudoId or state
            order_by="update_time",  # Optional: Sort results
        )
    )

    print("Sessions:")
    for session in response.sessions:
        print(session)

    return response


```

### Code Example 20 (text)

```text
from google.cloud import discoveryengine_v1 as discoveryengine


def list_sessions(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.ListSessionsResponse:
    """Lists all sessions associated with a data store.

    Args:
        project_id: The ID of your Google Cloud project.
        location: The location of the app.
        engine_id: The ID of the app.
    Returns:
        discoveryengine.ListSessionsResponse: The list of sessions.
    """

    client = discoveryengine.ConversationalSearchServiceClient()

    # The full resource name of the engine
    parent = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}"

    response = client.list_sessions(
        request=discoveryengine.ListSessionsRequest(
            parent=parent,
            filter='state="IN_PROGRESS"',  # Optional: Filter requests by userPseudoId or state
            order_by="update_time",  # Optional: Sort results
        )
    )

    print("Sessions:")
    for session in response.sessions:
        print(session)

    return response


```

