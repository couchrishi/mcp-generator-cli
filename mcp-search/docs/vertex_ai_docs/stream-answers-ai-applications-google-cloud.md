# Stream answers  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/stream-answer](https://cloud.google.com/generative-ai-app-builder/docs/stream-answer)

Home
AI Applications
Documentation
Guides
Send feedback
Stream answers
Stay organized with collections
Save and categorize content based on your preferences.
This page introduces the streaming answer method.
The streaming answer method has many of the same features as the
answer
method plus one additional feature:
streaming
. When you
stream an answer, the generated answer is broken into multiple parts that are
sent in sequence.
Streaming answers is particularly useful if the generated answers are long, so
that sending the entire answer at once causes a delay. Streaming answers reduces
the appearance of latency.
Limitations
The streaming answer method has the same features as the answer method with the
following exceptions:
The number of rephrase steps is one. You can't disable rephrasing, nor can
you change the maximum number of steps.
Only Gemini models can be used with the streaming answer method.
For a list of models, see
Available models
.
Stream an answer
The following command shows how to call the
streaming
answer
method and return a generated answer in the form of
a series of JSON responses. Typically, each response contains one sentence of
the answer.
This basic command shows the required input only. The options are left at their
defaults.
For examples of other options, see
Get answers and
follow-ups
. Some answer options aren't available for
answer streaming; see the
limitations
on this page.
REST
To search and get results with a streamed generated answer, do the following:
Run the following curl command:
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/
PROJECT_ID
/locations/global/collections/default_collection/engines/
APP_ID
/servingConfigs/default_search:streamAnswer" \
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
question or search query. For example, "Which database is faster, bigquery
or spanner?".
Example command and partial result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/servingConfigs/default_search:streamAnswer" \
-d '{
"query":{"text":"Which database is faster, bigquery or spanner?"}
}'
[{
"answer": {
"state": "
STREAMING
",
"steps": [
{
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": " What is the performance of Spanner?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/answer",
"title": "Get answers and follow-ups",
"snippetInfo": [
{
"snippet": "QUERY : a free-text string that contains the question or search query. For example, "Compare the BigQuery and \u003cb\u003eSpanner\u003c/b\u003e databases?". Example command and result.",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/b95bb201a0adb24f769627f56cf34405",
"uri": "https://abc.xyz/assets/investor/static/pdf/2017_Q1_Earnings_Transcript.pdf",
"title": "\u200b \u200b",
"snippetInfo": [
{
"snippet": "well as Hardware related costs, reflecting the continued strong \u003cb\u003eperformance\u003c/b\u003e of our new Made by ... We introduced dozens of new products, including \u003cb\u003eSpanner\u003c/b\u003e, a ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
},
{
"searchAction": {
"query": " What is the performance of BigQuery?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/18bcc727bfd6a3d1be0aa4bd49fe2c50",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality",
"title": "Evaluate search quality",
"snippetInfo": [
{
"snippet": "You can evaluate the \u003cb\u003eperformance\u003c/b\u003e of generic search apps that contain structured, unstructured, and website data. ... Import from \u003cb\u003eBigQuery\u003c/b\u003e: import \u003cb\u003eBigQuery\u003c/b\u003e data ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/answer",
"title": "Get answers and follow-ups",
"snippetInfo": [
{
"snippet": "QUERY : a free-text string that contains the question or search query. For example, "Compare the \u003cb\u003eBigQuery\u003c/b\u003e and Spanner databases?". Example command and result.",
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
}
}
,
{
"answer": {
"state": "
STREAMING
",
"references": [
{
"chunkInfo": {
"content": "Example command and partial result curl -X POST -H \"Authorization: Bearer $(gcloud auth print-access-token)\" -H \"Content-Type: application/json\" \"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/servingConfigs/default_search:answer\" -d '{ \"query\": { \"text\": \"Compare bigquery with spanner database?\"} \"queryUnderstandingSpec\": { \"queryRephraserSpec\": { \"disable\": true } } }' { \"answer\": { \"state\": \"SUCCEEDED\", \"answerText\": \"You can compare BigQuery and Spanner databases using the following criteria:\\n\\n* **Pricing:** BigQuery is priced per GB of data processed, while Spanner is priced per hour of compute time.\\n* **Performance:** BigQuery is designed for fast analytics, while Spanner is designed for high availability and scalability.\\n* **Features:** BigQuery supports a wide range of features, including SQL, machine learning, and streaming. ",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/answer",
"title": "Get answers and follow-ups"
}
}
},
...
{
"chunkInfo": {
"content": "Here is an example of a summary, with citations and citation metadata, returned at the end of a search response: See more code actions. Dismiss View Light code theme Dark code theme \"summary\": { \"summaryText\": \"BigQuery is Google Cloud's fully managed and completely serverless enterprise data warehouse [1]. BigQuery supports all data types, works across clouds, and has built-in machine learning and business intelligence, all within a unified platform [2, 3].\", \"summaryWithMetadata\": { \"summary\": \"BigQuery is Google Cloud's fully managed and completely serverless enterprise data warehouse. ",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7ba2e8666f5514b5bc14f5e300d7678",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries",
"title": "Get search summaries"
}
}
}
]
}
}
,
{
"answer": {
"state": "
STREAMING
",
"answerText": "Span"
}
}
,
{
"answer": {
"state": "
STREAMING
",
"answerText": "ner is Google's large-scale database that scales 20 times better than"
}
}
,
...
{
"answer": {
"state": "
STREAMING
",
"answerText": " Web Services, and on-premises data sources. "
}
}
,
{
"answer": {
"state": "
STREAMING
",
"answerText": "Spanner is a distributed, strongly consistent, SQL database designed to scale to 10 million servers. \n"
}
}
,
{
"answer": {
"state": "
SUCCEEDED
",
"answerText": "Spanner is Google's large-scale database that scales 20 times better than any competitor. Spanner is designed for high availability and scalability, while BigQuery is designed for fast analytics. BigQuery is a serverless, highly scalable, and cost-effective cloud data warehouse that enables businesses to analyze all their data very quickly. BigQuery is a very powerful tool that can be used to analyze data from many different sources, including Google Cloud Platform, Amazon Web Services, and on-premises data sources. Spanner is a distributed, strongly consistent, SQL database designed to scale to 10 million servers. \n",
"references": [
{
"chunkInfo": {
"content": "Example command and partial result curl -X POST -H \"Authorization: Bearer $(gcloud auth print-access-token)\" -H \"Content-Type: application/json\" \"https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/servingConfigs/default_search:answer\" -d '{ \"query\": { \"text\": \"Compare bigquery with spanner database?\"} \"queryUnderstandingSpec\": { \"queryRephraserSpec\": { \"disable\": true } } }' { \"answer\": { \"state\": \"SUCCEEDED\", \"answerText\": \"You can compare BigQuery and Spanner databases using the following criteria:\\n\\n* **Pricing:** BigQuery is priced per GB of data processed, while Spanner is priced per hour of compute time.\\n* **Performance:** BigQuery is designed for fast analytics, while Spanner is designed for high availability and scalability.\\n* **Features:** BigQuery supports a wide range of features, including SQL, machine learning, and streaming. ",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/answer",
"title": "Get answers and follow-ups"
}
}
},
{
"chunkInfo": {
"content": "Second, we also give them the ability to build applications using a set of technology that can run on any environment that they have. When we say on any environment - at their premise, on our cloud or on any other cloud. So, in other words, they can learn once, write once, deploy anywhere; and we make money no matter where they deploy. An example of that is a recent product we introduced called AlloyDB. It's the fastest-performing relational database in the market. We run it in all four environments: Our cloud, on-premise and on other clouds. And it's the only relational database that can run in any of those configurations. You see that in our adoption, both at the top end of the market where a system - for example, like Spanner, which is our large-scale database - scales 20 times better than the largest scalable system of any competitor. So for high-end, we work extremely well. And, also, because we made it so easy to use, startups and small businesses are growing very quickly in their adoption of our platform. When we introduced our AI systems, we introduced a platform called Vertex AI. ",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/8ad08d0844d601733e135381512e2a16",
"uri": "http://abc.xyz/thomas-kurian-ceo-google-cloud-at-the-goldman-sachs-2023-communacopia-technology-conference-on-september-7th-2023",
"title": "Thomas Kurian, CEO, Google Cloud at the Goldman Sachs 2023 Communacopia + Technology Conference on September 7th, 2023 - Alphabet Investor Relations"
}
}
},
...
{
"chunkInfo": {
"content": "BigQuery is also integrated with other Google Cloud services, such as Google Kubernetes Engine, Cloud Data Fusion, and Cloud Dataproc, making it easy to build and deploy data pipelines. Here are some of the benefits of using BigQuery: * **Fast and scalable:** BigQuery can process petabytes of data very quickly, and it can scale to handle even the most demanding workloads. * **Cost-effective:** BigQuery is a very cost-effective way to store and analyze data. You only pay for the data that you use, and there are no upfront costs or commitments. * **Secure:** BigQuery is a secure platform that meets the needs of even the most security-conscious organizations. * **Easy to use:** BigQuery is easy to use, even for non-technical users. It has a simple and intuitive user interface, and it supports a variety of data sources. * **Integrated with other Google Cloud services:** BigQuery is integrated with other Google Cloud services, making it easy to build and deploy data pipelines. If you are looking for a fast, scalable, and cost-effective way to analyze your data, then BigQuery is a great option. ",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7ba2e8666f5514b5bc14f5e300d7678",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries",
"title": "Get search summaries"
}
}
},
{
"chunkInfo": {
"content": "Here is an example of a summary, with citations and citation metadata, returned at the end of a search response: See more code actions. Dismiss View Light code theme Dark code theme \"summary\": { \"summaryText\": \"BigQuery is Google Cloud's fully managed and completely serverless enterprise data warehouse [1]. BigQuery supports all data types, works across clouds, and has built-in machine learning and business intelligence, all within a unified platform [2, 3].\", \"summaryWithMetadata\": { \"summary\": \"BigQuery is Google Cloud's fully managed and completely serverless enterprise data warehouse. ",
"documentMetadata": {
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/f7ba2e8666f5514b5bc14f5e300d7678",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries",
"title": "Get search summaries"
}
}
}
],
"steps": [
{
"description": "Rephrase the query and search.",
"actions": [
{
"searchAction": {
"query": " What is the performance of Spanner?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/answer",
"title": "Get answers and follow-ups",
"snippetInfo": [
{
"snippet": "QUERY : a free-text string that contains the question or search query. For example, "Compare the BigQuery and \u003cb\u003eSpanner\u003c/b\u003e databases?". Example command and result.",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/9d022f7bdf24bac6714a9cf61a5458c7",
"uri": "https://abc.xyz/assets/87/4c/162ca71d4178a3f4d39002467439/thomas-kurian-goldman-sachs-090723.pdf",
"title": "Thomas Kurian Goldman Sachs 090723",
"snippetInfo": [
{
"snippet": "2X better training \u003cb\u003eperformance\u003c/b\u003e per dollar1 compared to a leading cloud alternative. More than 70% of gen AI unicorns are Google Cloud customers. Best ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/20641e370fa86c78f1c81f3dab22efe1",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/release-notes",
"title": "AI Applications release notes | Google Cloud",
"snippetInfo": [
{
"snippet": "Generative answers have been updated with \u003cb\u003eperformance\u003c/b\u003e improvements. ... This lets you assess your search engine's \u003cb\u003eperformance\u003c/b\u003e ... Importing data from \u003cb\u003eSpanner\u003c/b\u003e, Cloud ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/b95bb201a0adb24f769627f56cf34405",
"uri": "https://abc.xyz/assets/investor/static/pdf/2017_Q1_Earnings_Transcript.pdf",
"title": "\u200b \u200b",
"snippetInfo": [
{
"snippet": "well as Hardware related costs, reflecting the continued strong \u003cb\u003eperformance\u003c/b\u003e of our new Made by ... We introduced dozens of new products, including \u003cb\u003eSpanner\u003c/b\u003e, a ...",
"snippetStatus": "SUCCESS"
}
]
}
]
}
},
{
"searchAction": {
"query": " What is the performance of BigQuery?"
},
"observation": {
"searchResults": [
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/18bcc727bfd6a3d1be0aa4bd49fe2c50",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality",
"title": "Evaluate search quality",
"snippetInfo": [
{
"snippet": "You can evaluate the \u003cb\u003eperformance\u003c/b\u003e of generic search apps that contain structured, unstructured, and website data. ... Import from \u003cb\u003eBigQuery\u003c/b\u003e: import \u003cb\u003eBigQuery\u003c/b\u003e data ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/2a3221d40533a4bdaf35778962a2a079",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality",
"title": "Check data quality for media recommendations",
"snippetInfo": [
{
"snippet": "... model that will result in \u003cb\u003eperformance\u003c/b\u003e issue if not met for all media recommendations models and all business objectives.", "condition": { "expression ...",
"snippetStatus": "SUCCESS"
}
]
},
...
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/18c258b9c770f4d762e6233d1a1bc81c",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/user-events",
"title": "About user events",
"snippetInfo": [
{
"snippet": "This section provides the data formats for each event type supported by media recommendations. Examples for JavaScript Pixel are provided. For \u003cb\u003eBigQuery\u003c/b\u003e, the ...",
"snippetStatus": "SUCCESS"
}
]
},
{
"document": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
"uri": "https://cloud.google.com/generative-ai-app-builder/docs/answer",
"title": "Get answers and follow-ups",
"snippetInfo": [
{
"snippet": "QUERY : a free-text string that contains the question or search query. For example, "Compare the \u003cb\u003eBigQuery\u003c/b\u003e and Spanner databases?". Example command and result.",
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
}
}
In this example, the answer to the query "Which database is faster, bigquery
or spanner?" appears in a series of JSON outputs. The final output is given the
state
SUCCEEDED
and includes the complete answer.
In this example, the
steps
and
references
streaming
responses appear before the
AnswerText
streaming responses. This
might not always be the case. If you're parsing the output, don't assume that
the
steps
and
references
responses come before the
AnswerText
responses.
Other examples
The basic command shown in
Stream an answer
is the
simplest command with no options specified. However, you can apply the same
options available with the
answer
method, with the exception of the
limitations
listed on this page.
Streaming answers can also used with
follow-up sessions
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

