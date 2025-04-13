# Improve search results with search tuning  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/tune-search](https://cloud.google.com/generative-ai-app-builder/docs/tune-search)

Home
AI Applications
Documentation
Guides
Send feedback
Improve search results with search tuning
Stay organized with collections
Save and categorize content based on your preferences.
A tuned search model can give you better quality results than the base search
model.
Search tuning is particularly valuable if you have industry-specific or company-specific
queries that are less well addressed by general LLMs. It can be used to further
train the search model.
Limitations
Search tuning can only be applied to unstructured data stores.
About training data
To tune a search model, you start by putting together training data.
The training data should contain queries that you expect that your end users
will ask and snippets of text, 250 to 500 words long,
that contain relevant information needed to answer the queries.
A query can be associated with multiple snippets as long as each snippet
contains information that answers the query.
The training data should also contain snippets of text that are not paired with
queries, but are otherwise similar to the answers in style and length.
These snippets without associated queries provide random negatives
to tune the model. Google recommends that you provide at least 10,000 of these
snippets.
Here is some terminology to describe the training data that you'll need to
provide:
Training queries:
Queries that you anticipate your end users asking. Make
sure to focus on queries with specific domain or company terminology.
Provide at least 100.
Extractive segments:
Snippets (typically multiple paragraphs)
must be taken verbatim from the
documents in the data store. All the documents together in the data store
are referred to as "the corpus".
You must provide two types of extractive segments:
Segments that contain relevant information needed to answer the training
queries. These are segments that have positive matching with queries.
Segments that are not associated with any training queries. These segments
are used as random negatives in the model tuning.
A sentence or two is not sufficiently long to be an extractive segment; the
segment needs to contain enough context for training. For example, in
response to a query like "who founded Google," a short extract like "Larry
Page" is insufficient. For examples of sufficiently long segments, see the
following table of examples.
Provide at least one extractive segment per query and at least 10,000
additional extractive segments.
Relevance scores:
Relevance scores are non-negative integers that estimate
how relevant the extractive segment is to the query. You provide a
score value for each query and extractive segment pair. A score of 0 means
that the extractive segment isn't relevant to the query at all. A score
greater than zero indicates some relevance. For simple scoring, Google recommends
1 for all relevant segments and 0 for non-relevant ones. Alternatively, if
you want to rank relevance, you can assign relevance scores of 0 to 10 (for example), with 10 for the most relevant segments and 0 for segments that
are not at all relevant.
Provide at least 100 relevant scores and, optionally, additional
non-relevant scores.
Examples of query and extractive segment pairs
The following table provides some examples of query and extractive segment
pairs. These general examples have been taken from Wikipedia. However,
for useful tuning, you'll want to supply documents from proprietary data sets
that contain information specific to your business and that are less easily
found on the web.
The last pair in this table is an example of a zero-score pair, where the
answer is not relevant to the query.
Training query
Extractive segment
Score
who founded Google?
Google was founded on September 4, 1998, by American computer scientists
Larry Page and Sergey Brin while they were PhD students at Stanford University
in California.Together they own about 14% of its publicly listed shares and
control 56% of its stockholder voting power through super-voting stock. The
company went public via an initial public offering (IPO) in 2004. In 2015,
Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is
Alphabet's largest subsidiary and is a holding company for Alphabet's internet
properties and interests. Sundar Pichai was appointed CEO of Google on October
24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3,
2019, Pichai also became the CEO of Alphabet. [...] On the list of most
valuable brands, Google is
ranked second by Forbes and fourth by Interbrand.
1
where is blood pumped after it leaves the right ventricle?
Oxygenated blood leaves the lungs through pulmonary veins, which return it to
the left part of the heart, completing the pulmonary cycle. This blood
then enters the left atrium, which pumps it through the mitral valve into the
left ventricle. From the left ventricle, the blood passes through the
aortic valve to the aorta. The blood is then distributed to the body
through the systemic circulation before returning again to the pulmonary
circulation. Arteries Main article: Pulmonary artery From the right
ventricle, blood is pumped through the semilunar pulmonary valve into the left
and right main pulmonary artery (one for each lung), which branch into smaller
pulmonary arteries that spread throughout the lungs. [...]
Cardiac shunt is an unnatural connection between parts
of the heart that leads to blood flow that bypasses the lungs.
1
where is the bowling hall of fame
located?
The World Bowling Writers ( WBW ) International Bowling Hall
of Fame was established in 1993 and is located in the International Bowling
Museum and Hall of Fame , on the International Bowling Campus in Arlington ,
Texas. History The International Bowling Museum and Hall of Fame was located at
11 Stadium Plaza, St. Louis, Missouri, USA, and shared the same building with
the St. Louis Cardinals Hall of Fame Museum, until November 8, 2008. It moved to
Arlington and reopened in early 2010. In 2012, the WBW was merged with the
International Bowling Media Association. After the merger, the WBW Hall of
Fame inductees became part of the IBMA Luby Hall of Fame.
officers of the World Bowling Writers, which formed the Hall's Board.][...] The
man and woman who receive the most votes are elected.
1
why is the sky blue?
A "Hello, World!" program is generally a simple computer program which
outputs (or displays) to the screen (often the console) a message similar to
"Hello, World!" while ignoring any user input. A small piece of code in most
general-purpose programming languages, this program is used to illustrate a
language's basic syntax. A "Hello, World!" program is often the first written by
a student of a new programming language, but such a program can also be used as
a check to ensure that the computer software intended to compile or run source
code is correctly installed, and that its operator understands how to use it.
[...] The C-language version was preceded by Kernighan's own 1972 A Tutorial
Introduction to the Language B, where the first known version of the program
is found in an example used to illustrate external variables
0
About testing
After training, the tuned search is tested to determine if tuning improved the
results. You can explicitly provide the queries that you want tested. If you
don't provide test queries, then Vertex AI Search uses 20% of the
training queries as test queries.
Training files
The training data needs to be uploaded in three (optionally four) specific
files:
A
corpus file
that contains the extractive segments
A
query file
that contains only the queries
A
training labels file
that connects queries with segments and
contains the relevance scores
Optional: A
test labels file
that is similar to the training labels
files but is used for evaluating the tuned model instead of training it
The three training files (corpus file, query file, and training labels file) and
the (optional) test labels file need to be in Cloud Storage. The paths of the
files are defined by fields in the
trainCustomMethod
call.
Corpus file
The corpus file contains extractive segments:
segments that contain information to answer the queries in the query file and
many additional segments to be used as random negatives when tuning the model.
You should have at least 100 segments that contain query answers; queries can be
answered by multiple segments. You should also have at least 10,000 random
segments.
If the documents in your data store contain fewer than 500 words, you can use
whole documents as segments. Otherwise, programmatically create random segments
of 250–500 words from the documents in your data store and add those to the
corpus file.
The corpus file is a JSONL (JSON lines) file where each line has the fields
_id
and
text
with string values.
For example:
{
"_id"
:
"doc1"
,
"text"
:
"Google was founded on September 4, 1998, by American computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet. [...] On the list of most valuable brands, Google is 105 ranked second by Forbes and fourth by Interbrand."
}
{
"_id"
:
"doc2"
,
"text"
:
"Oxygenated blood leaves the lungs through pulmonary veins, which return it to the left part of the heart, completing the pulmonary cycle. This blood then enters the left atrium, which pumps it through the mitral valve into the left ventricle. From the left ventricle, the blood passes through the aortic valve to the aorta. The blood is then distributed to the body through the systemic circulation before returning again to the pulmonary circulation. Arteries Main article: Pulmonary artery From the right ventricle, blood is pumped through the semilunar pulmonary valve into the left and right main pulmonary artery (one for each lung), which branch into smaller pulmonary arteries that spread throughout the lungs. [...] Cardiac shunt is an unnatural connection between parts of the heart that leads to blood flow that bypasses the lungs."
}
{
"_id"
:
"doc3"
,
"text"
:
"The World Bowling Writers ( WBW ) International Bowling Hall of Fame was established in 1993 and is located in the International Bowling Museum and Hall of Fame , on the International Bowling Campus in Arlington , Texas. History The International Bowling Museum and Hall of Fame was located at 11 Stadium Plaza, St. Louis, Missouri, USA, and shared the same building with the St. Louis Cardinals Hall of Fame Museum, until November 8, 2008. It moved to Arlington and reopened in early 2010. In 2012, the WBW was merged with the International Bowling Media Association. After the merger, the WBW Hall of Fame inductees became part of the IBMA Luby Hall of Fame. officers of the World Bowling Writers, which formed the Hall's Board.][...] The man and woman who receive the most votes are elected."
}
{
"_id"
:
"doc4"
,
"text"
:
"A \"Hello, World!\" program is generally a simple computer program which outputs (or displays) to the screen (often the console) a message similar to "
Hello
,
World!
" while ignoring any user input. A small piece of code in most general-purpose programming languages, this program is used to illustrate a language's basic syntax. A "
Hello
,
World!
" program is often the first written by a student of a new programming language, but such a program can also be used as a check to ensure that the computer software intended to compile or run source code is correctly installed, and that its operator understands how to use it. [...] The C-language version was preceded by Kernighan's own 1972 A Tutorial Introduction to the Language B, where the first known version of the program is found in an example used to illustrate external variables."
}
The maximum size of the file is 500,000 lines.
Query file
The query file contains the example queries that will be used for tuning the
model. Each query should have one or more corresponding extractive segments in
the corpus file. You should provide at least 100 positive match queries. You can
also provide non-relevant queries: these are queries that correspond to
extractive segments with a relevance score of zero.
The query file is in JSONL format and has the same fields as the corpus file.
For example:
{
"_id"
:
"query1"
,
"text"
:
"who founded Google?"
}
{
"_id"
:
"query2"
,
"text"
:
"where is blood pumped after it leaves the right ventricle?"
}
{
"_id"
:
"query3"
,
"text"
:
"where is the bowling hall of fame located?"
}
{
"_id"
:
"query4"
,
"text"
:
"why is the sky blue?"
}
The maximum number of queries allowed in the file is 40,000.
Training labels
The training labels file connects the queries with the extractive segments and
scores each query and segment pair.
If the test labels file is not present, then 20% of
the queries in the training labels file are reserved for evaluating the tuned model after
training.
The file contains the ID of a query and the ID of its matching (or non-matching)
extractive segment and a score for the relevance of the segment to the query.
There must be at least one line per query; if a query is answered by two
segments, then there are two lines for that query.
Score
is a non-negative
integer value. Any score greater than zero indicates that the document is
related to the query. Larger numbers indicate a greater level of relevance. If
the score is omitted, the default value is 1.
The training labels file is a TSV (tab-separated values) file with a header.
The file must have the columns
query-id
,
corpus-id
and
score
. The
query-id
is a string that matches the
_id
key from the query file, and the
corpus-id
is a string that matches the
_id
in the corpus file.
For example:
query-id corpus-id score
query1 doc1 1
query2 doc2 1
query3 doc3 1
query3 doc9 1
query4 doc4 0
The training labels file must include at least 100 unique query IDs. The number
of query IDs in the training labels file combined with the number of queries in
the test labels file must be less than 500,000.
Test labels
Like the training labels file, this optional file contains the IDs of the query
and extractive segment and relevance scores. It contains fewer and different
queries than in the training labels file. If present, the query and extractive
segment pairs in the file are used to evaluate the tuning. If the test labels
file is not present, then query and extractive segment pairs from the training
labels file are used for evaluating.
This file has the same format as the training labels file.
For example:
query-id corpus-id score
query200 doc200 1
query201 doc201 1
query202 doc202 1
Although the test labels file is optional, if you provide it, it must contain
at least three unique query IDs.
Before you begin
Turn on
Enterprise edition features
for the app.
Tune search
To tune a search model with your own training data follow these steps.
Console
To use the Google Cloud console to tune a model, follow these steps:
Prepare your training data and, optionally, your test data files. Use the
formats described in
Training files
.
Upload the files to
Cloud Storage
.
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
On the
Apps
page, click the name of the app that you want a trained
model for.
In the navigation menu, click
Configurations
.
Click the
Tuning
tab.
Click
Tune the base model
.
Specify the corpus, query, training, and, optionally, testing files that you
prepared in the preceding steps 1 and 2.
Click
Start Tuning
.
Refresh the page to see the status in the
Recent tuning activity
table
on the
Tuning
tab.
REST
To use the
trainCustomModel
method to tune a data store,
follow these steps:
Prepare your training data (and optionally, your test data) files. Use the
formats described in
Training files
.
Place the files into a
Cloud Storage
bucket.
Upload the files from the Cloud Storage bucket into
Vertex AI Search by running the following curl command:
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
/locations/global/collections/default_collection/dataStores/
DATA_STORE_ID
:trainCustomModel"
\
-d
'{
"gcsTrainingInput": {
"corpusDataPath": "
CORPUS_JSONL_GCS_PATH
",
"queryDataPath": "
QUERY_JSONL_GCS_PATH
",
"trainDataPath": "
TRAIN_TSV_GCS_PATH
",
"testDataPath": "
TEST_TSV_GCS_PATH
"
},
"modelType": "search-tuning"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
DATA_STORE_ID
: the ID of the data store that you
want to tune.
CORPUS_JSONL_GCS_PATH
: the
corpus JSONL file
path in Cloud Storage—for example,
gs://my-bucket/corpus.jsonl
.
QUERY_JSONL_GCS_PATH
: the
query JSONL file
path in Cloud Storage—for example,
gs://my-bucket/query.jsonl
.
TRAIN_TSV_GCS_PATH
: the
training labels TSV file
path in
Cloud Storage—for example,
gs://my-bucket/train.tsv
.
TEST_TSV_GCS_PATH
: an optional field to
specify the Cloud Storage path for your
test labels TSV
file
—for example,
gs://my-bucket/test.tsv
. If you don't have a
test labels file, remove the
testDataPath
field or leave it empty.
For general information about this method, see
trainCustomModel
.
Tuning begins automatically after the data files are uploaded.
Click for an example curl command and response.
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
"https://discoveryengine.googleapis.com/v1/projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321:trainCustomModel"
-d
'
{
"dataStore"
:
"projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321"
,
"gcsTrainingInput"
:
{
"corpusDataPath"
:
"gs://my-bucket/corpus.jsonl"
,
"queryDataPath"
:
"gs://my-bucket/query.jsonl"
,
"trainDataPath"
:
"gs://my-bucket/train.tsv"
}
,
"modelType"
:
"search-tuning"
}
{
"name"
:
"projects/12345/locations/global/collections/default_collection/dataStores/my-data-store_4321/operations/train-custom-model-6071430366161939774"
,
"metadata"
:
{
"@type"
:
"type.googleapis.com/google.cloud.discoveryengine.v1.TrainCustomModelMetadata"
},
"response"
:
{
"@type"
:
"type.googleapis.com/google.cloud.discoveryengine.v1.TrainCustomModelResponse"
,
"modelStatus"
:
"in-progress"
}
}
Make note of the
name
value returned by the
trainCustomModel
method, and follow the instructions in
Get details
about a long-running operation
to
see when the search-tuning operation is complete.
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
google.api_core.operation
import
Operation
from
google.cloud
import
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# corpus_data_path = "gs://my-bucket/corpus.jsonl"
# query_data_path = "gs://my-bucket/query.jsonl"
# train_data_path = "gs://my-bucket/train.tsv"
# test_data_path = "gs://my-bucket/test.tsv"
def
train_custom_model_sample
(
project_id
:
str
,
location
:
str
,
data_store_id
:
str
,
corpus_data_path
:
str
,
query_data_path
:
str
,
train_data_path
:
str
,
test_data_path
:
str
,
)
-
>
Operation
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
SearchTuningServiceClient
(
client_options
=
client_options
)
# The full resource name of the data store
data_store
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
/collections/default_collection/dataStores/
{
data_store_id
}
"
# Make the request
operation
=
client
.
train_custom_model
(
request
=
discoveryengine
.
TrainCustomModelRequest
(
gcs_training_input
=
discoveryengine
.
TrainCustomModelRequest
.
GcsTrainingInput
(
corpus_data_path
=
corpus_data_path
,
query_data_path
=
query_data_path
,
train_data_path
=
train_data_path
,
test_data_path
=
test_data_path
,
),
data_store
=
data_store
,
model_type
=
"search-tuning"
,
)
)
# Optional: Wait for training to complete
# print(f"Waiting for operation to complete: {operation.operation.name}")
# response = operation.result()
# After the operation is complete,
# get information from operation metadata
# metadata = discoveryengine.TrainCustomModelMetadata(operation.metadata)
# Handle the response
# print(response)
# print(metadata)
print
(
operation
)
return
operation
Test tuned search and use it for individual search queries
After tuning is complete, you can test it out by comparing the results of
queries with the tuned model and the results of the same queries with the
base model.
Console
To use the Google Cloud console to preview the behavior of a tuned model, follow
these steps:
Go to the
Tuning
tab:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to preview.
Click
Configurations
.
Click the
Tuning
tab.
Click
Tuned model
and use the preview panel on the right to make
queries that use the tuned model.
Click
Base model
and use the preview panel on the right to
make queries using the original model.
Compare the quality of the results.
REST
To assess the effect of tuning, you can make queries with the
enableSearchAdaptor
field set to
true
and then
false
and compare the
results. Setting the
enableSearchAdaptor
field to
true
indicates that the
tuned version of search is used for that query.
To make search queries that use the tuned model:
In the query method call, set the
enableSearchAdaptor
field in
the
customFineTuningSpec
field to
true
.
For example:
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
"query": "
QUERY
",
"customFineTuningSpec": { "enableSearchAdaptor": true }
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the app that you want to
query.
For detailed information about search queries, see
Get search
results
and the
servingConfigs.search
method.
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
# search_query = "YOUR_SEARCH_QUERY"
def
search_sample
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
search_query
:
str
,
)
-
>
discoveryengine
.
services
.
search_service
.
pagers
.
SearchPager
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
SearchServiceClient
(
client_options
=
client_options
)
# The full resource name of the search app serving config
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
/servingConfigs/default_config"
# Optional - only supported for unstructured data: Configuration options for search.
# Refer to the `ContentSearchSpec` reference for all supported fields:
# https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
content_search_spec
=
discoveryengine
.
SearchRequest
.
ContentSearchSpec
(
# For information about snippets, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/snippets
snippet_spec
=
discoveryengine
.
SearchRequest
.
ContentSearchSpec
.
SnippetSpec
(
return_snippet
=
True
),
# For information about search summaries, refer to:
# https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
summary_spec
=
discoveryengine
.
SearchRequest
.
ContentSearchSpec
.
SummarySpec
(
summary_result_count
=
5
,
include_citations
=
True
,
ignore_adversarial_query
=
True
,
ignore_non_summary_seeking_query
=
True
,
model_prompt_spec
=
discoveryengine
.
SearchRequest
.
ContentSearchSpec
.
SummarySpec
.
ModelPromptSpec
(
preamble
=
"YOUR_CUSTOM_PROMPT"
),
model_spec
=
discoveryengine
.
SearchRequest
.
ContentSearchSpec
.
SummarySpec
.
ModelSpec
(
version
=
"stable"
,
),
),
)
# Refer to the `SearchRequest` reference for all supported fields:
# https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
request
=
discoveryengine
.
SearchRequest
(
serving_config
=
serving_config
,
query
=
search_query
,
page_size
=
10
,
content_search_spec
=
content_search_spec
,
query_expansion_spec
=
discoveryengine
.
SearchRequest
.
QueryExpansionSpec
(
condition
=
discoveryengine
.
SearchRequest
.
QueryExpansionSpec
.
Condition
.
AUTO
,
),
spell_correction_spec
=
discoveryengine
.
SearchRequest
.
SpellCorrectionSpec
(
mode
=
discoveryengine
.
SearchRequest
.
SpellCorrectionSpec
.
Mode
.
AUTO
),
# Optional: Use fine-tuned model for this request
# custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
# enable_search_adaptor=True
# ),
)
page_result
=
client
.
search
(
request
)
# Handle the response
for
response
in
page_result
:
print
(
response
)
return
page_result
Turn on tuned search
After you have tested the tuned search and decided that you want to use it
for all search queries, you can make it the default search model.
Console
To make the tuned model the default model and apply it to the main Preview page,
the widget, and API calls, follow these steps:
Go to the
Tuning
tab:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app.
Click
Configurations
.
Click the
Tuning
tab.
Click
Tuned model
.
Click
Publish
.
REST
When you set the tuned model to be the default model, you don't need to specify
the
customFineTuningSpec
field in the search query as in the preceding
procedure.
To used the tuned version of search by default for all search queries, follow
these steps:
To set the tuned search to be the default model, run the following curl
command:
curl
-X
PATCH
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
/servingConfigs/default_search?updateMask=customFineTuningSpec.enableSearchAdaptor"
\
-d
'{
"customFineTuningSpec": {
"enableSearchAdaptor": true
}
}'
For general information about this method, see
servingConfigs.patch
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
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1alpha
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# engine_id = "YOUR_DATA_STORE_ID"
def
update_serving_config_sample
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
ServingConfig
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
ServingConfigServiceClient
(
client_options
=
client_options
)
# The full resource name of the serving config
serving_config_name
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
/servingConfigs/default_search"
update_mask
=
"customFineTuningSpec.enableSearchAdaptor"
serving_config
=
client
.
update_serving_config
(
request
=
discoveryengine
.
UpdateServingConfigRequest
(
serving_config
=
discoveryengine
.
ServingConfig
(
name
=
serving_config_name
,
custom_fine_tuning_spec
=
discoveryengine
.
CustomFineTuningSpec
(
enable_search_adaptor
=
True
# Switch to `False` to disable tuned model
),
),
update_mask
=
update_mask
,
)
)
# Handle the response
print
(
serving_config
)
return
serving_config
Turn off tuned search
If you no longer want to use the tuned version of search—for example, if you
find the results no better, or worse, than before tuning, then you
can disable the tuned search.
Console
To revert to using the base model as the default model, follow these steps:
Go to the
Tuning
tab:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app.
Click
Configurations
.
Click the
Tuning
tab.
Click
Base model
.
Click
Publish
.
REST
To stop using the tuned model, run a curl call similar to the preceding one,
but set
enableSearchAdaptor
to
false
:
Run the following curl command:
curl
-X
PATCH
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
/servingConfigs/default_search?updateMask=customFineTuningSpec.enableSearchAdaptor"
\
-d
'{
"customFineTuningSpec": {
"enableSearchAdaptor": false
}
}'
For general information about this method, see
servingConfigs.patch
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
google.api_core.client_options
import
ClientOptions
from
google.cloud
import
discoveryengine_v1alpha
as
discoveryengine
# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# engine_id = "YOUR_DATA_STORE_ID"
def
update_serving_config_sample
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
ServingConfig
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
ServingConfigServiceClient
(
client_options
=
client_options
)
# The full resource name of the serving config
serving_config_name
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
/servingConfigs/default_search"
update_mask
=
"customFineTuningSpec.enableSearchAdaptor"
serving_config
=
client
.
update_serving_config
(
request
=
discoveryengine
.
UpdateServingConfigRequest
(
serving_config
=
discoveryengine
.
ServingConfig
(
name
=
serving_config_name
,
custom_fine_tuning_spec
=
discoveryengine
.
CustomFineTuningSpec
(
enable_search_adaptor
=
True
# Switch to `False` to disable tuned model
),
),
update_mask
=
update_mask
,
)
)
# Handle the response
print
(
serving_config
)
return
serving_config
What's next
To understand the impact of search tuning on the search quality,
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
  {"_id": "doc1", "text": "Google was founded on September 4, 1998, by American computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet. [...] On the list of most valuable brands, Google is 105 ranked second by Forbes and fourth by Interbrand."}
  {"_id": "doc2", "text": "Oxygenated blood leaves the lungs through pulmonary veins, which return it to the left part of the heart, completing the pulmonary cycle. This blood then enters the left atrium, which pumps it through the mitral valve into the left ventricle. From the left ventricle, the blood passes through the aortic valve to the aorta. The blood is then distributed to the body through the systemic circulation before returning again to the pulmonary circulation. Arteries Main article: Pulmonary artery From the right ventricle, blood is pumped through the semilunar pulmonary valve into the left and right main pulmonary artery (one for each lung), which branch into smaller pulmonary arteries that spread throughout the lungs. [...] Cardiac shunt is an unnatural connection between parts of the heart that leads to blood flow that bypasses the lungs."}
  {"_id": "doc3", "text": "The World Bowling Writers ( WBW ) International Bowling Hall of Fame was established in 1993 and is located in the International Bowling Museum and Hall of Fame , on the International Bowling Campus in Arlington , Texas. History The International Bowling Museum and Hall of Fame was located at 11 Stadium Plaza, St. Louis, Missouri, USA, and shared the same building with the St. Louis Cardinals Hall of Fame Museum, until November 8, 2008. It moved to Arlington and reopened in early 2010. In 2012, the WBW was merged with the International Bowling Media Association. After the merger, the WBW Hall of Fame inductees became part of the IBMA Luby Hall of Fame.  officers of the World Bowling Writers, which formed the Hall's Board.][...] The man and woman who receive the most votes are elected."}
  {"_id": "doc4", "text": "A \"Hello, World!\" program is generally a simple computer program which outputs (or displays) to the screen (often the console) a message similar to "Hello, World!" while ignoring any user input. A small piece of code in most general-purpose programming languages, this program is used to illustrate a language's basic syntax. A "Hello, World!" program is often the first written by a student of a new programming language, but such a program can also be used as a check to ensure that the computer software intended to compile or run source code is correctly installed, and that its operator understands how to use it.  [...] The C-language version was preceded by Kernighan's own 1972 A Tutorial Introduction to the Language B, where the first known version of the program is found in an example used to illustrate external variables."}

```

### Code Example 2 (text)

```text
  {"_id": "query1", "text": "who founded Google?"}
  {"_id": "query2", "text": "where is blood pumped after it leaves the right ventricle?"}
  {"_id": "query3", "text": "where is the bowling hall of fame located?"}
  {"_id": "query4", "text": "why is the sky blue?"}

```

### Code Example 3 (text)

```text
query-id    corpus-id   score
query1  doc1    1
query2  doc2    1
query3  doc3    1
query3  doc9    1
query4  doc4    0

```

### Code Example 4 (text)

```text
query-id    corpus-id   score
query200    doc200  1
query201    doc201  1
query202    doc202  1

```

### Code Example 5 (text)

```text
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID:trainCustomModel" \
-d '{
"gcsTrainingInput": {
 "corpusDataPath": "CORPUS_JSONL_GCS_PATH",
 "queryDataPath": "QUERY_JSONL_GCS_PATH",
 "trainDataPath": "TRAIN_TSV_GCS_PATH",
 "testDataPath": "TEST_TSV_GCS_PATH"
},
"modelType": "search-tuning"
}'

```

### Code Example 6 (text)

```text

from google.api_core.client_options import ClientOptions
from google.api_core.operation import Operation
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# data_store_id = "YOUR_DATA_STORE_ID"
# corpus_data_path = "gs://my-bucket/corpus.jsonl"
# query_data_path = "gs://my-bucket/query.jsonl"
# train_data_path = "gs://my-bucket/train.tsv"
# test_data_path = "gs://my-bucket/test.tsv"


def train_custom_model_sample(
    project_id: str,
    location: str,
    data_store_id: str,
    corpus_data_path: str,
    query_data_path: str,
    train_data_path: str,
    test_data_path: str,
) -> Operation:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    # Create a client
    client = discoveryengine.SearchTuningServiceClient(client_options=client_options)

    # The full resource name of the data store
    data_store = f"projects/{project_id}/locations/{location}/collections/default_collection/dataStores/{data_store_id}"

    # Make the request
    operation = client.train_custom_model(
        request=discoveryengine.TrainCustomModelRequest(
            gcs_training_input=discoveryengine.TrainCustomModelRequest.GcsTrainingInput(
                corpus_data_path=corpus_data_path,
                query_data_path=query_data_path,
                train_data_path=train_data_path,
                test_data_path=test_data_path,
            ),
            data_store=data_store,
            model_type="search-tuning",
        )
    )

    # Optional: Wait for training to complete
    # print(f"Waiting for operation to complete: {operation.operation.name}")
    # response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    # metadata = discoveryengine.TrainCustomModelMetadata(operation.metadata)

    # Handle the response
    # print(response)
    # print(metadata)
    print(operation)

    return operation


```

### Code Example 7 (text)

```text
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search:search" \
-d '{
"query": "QUERY",
"customFineTuningSpec": { "enableSearchAdaptor": true }
}'

```

### Code Example 8 (text)

```text
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"          # Values: "global", "us", "eu"
# engine_id = "YOUR_APP_ID"
# search_query = "YOUR_SEARCH_QUERY"


def search_sample(
    project_id: str,
    location: str,
    engine_id: str,
    search_query: str,
) -> discoveryengine.services.search_service.pagers.SearchPager:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # The full resource name of the search app serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"

    # Optional - only supported for unstructured data: Configuration options for search.
    # Refer to the `ContentSearchSpec` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        # For information about snippets, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/snippets
        snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet=True
        ),
        # For information about search summaries, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=5,
            include_citations=True,
            ignore_adversarial_query=True,
            ignore_non_summary_seeking_query=True,
            model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                preamble="YOUR_CUSTOM_PROMPT"
            ),
            model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="stable",
            ),
        ),
    )

    # Refer to the `SearchRequest` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=10,
        content_search_spec=content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
        # Optional: Use fine-tuned model for this request
        # custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
        #     enable_search_adaptor=True
        # ),
    )

    page_result = client.search(request)

    # Handle the response
    for response in page_result:
        print(response)

    return page_result


```

### Code Example 9 (text)

```text
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?updateMask=customFineTuningSpec.enableSearchAdaptor" \
-d '{
"customFineTuningSpec": {
 "enableSearchAdaptor": true
}
}'

```

### Code Example 10 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1alpha as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# engine_id = "YOUR_DATA_STORE_ID"


def update_serving_config_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.ServingConfig:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    # Create a client
    client = discoveryengine.ServingConfigServiceClient(client_options=client_options)

    # The full resource name of the serving config
    serving_config_name = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_search"

    update_mask = "customFineTuningSpec.enableSearchAdaptor"

    serving_config = client.update_serving_config(
        request=discoveryengine.UpdateServingConfigRequest(
            serving_config=discoveryengine.ServingConfig(
                name=serving_config_name,
                custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
                    enable_search_adaptor=True  # Switch to `False` to disable tuned model
                ),
            ),
            update_mask=update_mask,
        )
    )

    # Handle the response
    print(serving_config)

    return serving_config


```

### Code Example 11 (text)

```text
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/servingConfigs/default_search?updateMask=customFineTuningSpec.enableSearchAdaptor" \
-d '{
"customFineTuningSpec": {
 "enableSearchAdaptor": false
}
}'

```

### Code Example 12 (text)

```text

from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1alpha as discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION" # Values: "global"
# engine_id = "YOUR_DATA_STORE_ID"


def update_serving_config_sample(
    project_id: str,
    location: str,
    engine_id: str,
) -> discoveryengine.ServingConfig:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    # Create a client
    client = discoveryengine.ServingConfigServiceClient(client_options=client_options)

    # The full resource name of the serving config
    serving_config_name = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_search"

    update_mask = "customFineTuningSpec.enableSearchAdaptor"

    serving_config = client.update_serving_config(
        request=discoveryengine.UpdateServingConfigRequest(
            serving_config=discoveryengine.ServingConfig(
                name=serving_config_name,
                custom_fine_tuning_spec=discoveryengine.CustomFineTuningSpec(
                    enable_search_adaptor=True  # Switch to `False` to disable tuned model
                ),
            ),
            update_mask=update_mask,
        )
    )

    # Handle the response
    print(serving_config)

    return serving_config


```

