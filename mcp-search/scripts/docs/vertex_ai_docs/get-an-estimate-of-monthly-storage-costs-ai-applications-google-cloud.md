# Get an estimate of monthly storage costs  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/estimate-size-web-data](https://cloud.google.com/generative-ai-app-builder/docs/estimate-size-web-data)

Home
AI Applications
Documentation
Guides
Send feedback
Get an estimate of monthly storage costs
Stay organized with collections
Save and categorize content based on your preferences.
Advanced website indexing
incurs monthly data
storage charges based on the size of the web data that you import into your data
store. To get an estimate of the size of your web data before importing it, you
can call the
estimateDataSize
method and specify the web
pages that you want to import. The
estimateDataSize
method is a
long-running
operation
that runs until the process for estimating
the data size is complete. This can take from a few minutes to over an hour,
depending on the number of web pages that you specify. After you have an
estimate of the size of your web data, you can get an estimate of your monthly
data storage costs using the AI Applications pricing page (see the
Data Index
pricing
section) or the
Google Cloud's pricing
calculator
(search for AI Applications).
Before you begin
Determine the URL patterns for the websites that you intend to include (and
optionally exclude) when you import web data into your data store. You
specify these URL patterns when you call the
estimateDataSize
method.
Procedure
To get an estimate of the size of your web data, follow these steps:
Call the
estimateDataSize
method.
curl
-X
POST
\
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
"https://discoveryengine.googleapis.com/v1alpha/projects/
PROJECT_ID
/locations/global:estimateDataSize"
\
-d
'{
"website_data_source": {
"estimator_uri_patterns": {
provided_uri_pattern: "
URI_PATTERN_TO_INCLUDE
",
exact_match:
EXACT_MATCH_BOOLEAN
},
"estimator_uri_patterns": {
provided_uri_pattern: "
URI_PATTERN_TO_EXCLUDE
",
exact_match:
EXACT_MATCH_BOOLEAN
,
exclusive:
EXCLUSIVE_BOOLEAN
}
}
}'
Replace the following:
PROJECT_ID
: the ID of your project.
URI_PATTERN_TO_INCLUDE
: the URL patterns for the websites that
you want to include in your data size estimate.
URI_PATTERN_TO_EXCLUDE
: (Optional) The URL patterns for the
websites that you want to exclude from your data size estimate.
For
URI_PATTERN_TO_INCLUDE
and
URI_PATTERN_TO_EXCLUDE
, you can use patterns similar to the
following:
Entire website:
www.mysite.com
Parts of a website:
www.mysite.com/faq
Entire domain:
mysite.com
or
*.mysite.com
EXCLUSIVE_BOOLEAN
: (Optional) If
true
, then the provided URI
pattern represents web pages that are excluded from your data size
estimate. The default is
false
, which means that the provided URI
pattern represents web pages that are included in your data size estimate.
EXACT_MATCH_BOOLEAN
: (Optional) If
true
, then the provided
URI pattern represents a single web page, instead of the web page and all
of its children. The default is
false
, which means that the provided URI
pattern represents the web page and all of its children.
The output is similar to the following:
{
"name"
:
"projects/
PROJECT_ID
/locations/global/operations/estimate-data-size-01234567890123456789"
,
"metadata"
:
{
"@type"
:
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata"
}
}
This output includes the
name
field, which is the name of the long-running
operation. Save the
name
value to use in the following step.
Poll the
operations.get
method.
curl
-X
GET
\
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
"https://discoveryengine.googleapis.com/v1/
OPERATION_NAME
"
Replace
OPERATION_NAME
with the
name
value that you saved in the
previous step. You can also get the operation name by
listing long-running
operations
.
Evaluate each response.
If a response does not contain
"done": true
, then the process for
estimating the data size is not complete. Continue polling.
The output is similar to the following:
{
"name"
:
"projects/
PROJECT_ID
/locations/global/operations/estimate-data-size-01234567890123456789"
,
"metadata"
:
{
"@type"
:
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata"
}
}
If a response contains
"done": true
, then the process for estimating the
data size is complete. Save the
DATA_SIZE_BYTES
value from the
response to use in the following step.
The output is similar to the following:
{
"name"
:
"projects/
PROJECT_ID
/locations/global/operations/estimate-data-size-01234567890123456789"
,
"metadata"
:
{
"@type"
:
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata"
,
"createTime"
:
"2023-12-08T19:54:06.911248Z"
},
"done"
:
true
,
"response"
:
{
"@type"
:
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeResponse"
,
"dataSizeBytes"
:
DATA_SIZE_BYTES
,
"documentCount"
:
DOCUMENT_COUNT
}
}
This output includes the following values:
DATA_SIZE_BYTES
: the estimated size of your web data, in
bytes.
DOCUMENT_COUNT
: the estimated number of web pages in your web
data.
Divide the
DATA_SIZE_BYTES
value from the previous step by 1,000,000,000 to get gigabytes. Save this
value for the following step.
To get an estimate for your monthly data storage costs:
Go
Google Cloud's pricing calculator
.
Click
Add to estimate
.
Search for
AI Applications
and then click the
AI Applications
box.
In the
Data Index
box, enter the estimated size of your web data, in
gigabytes, from the previous step.
See the
Estimated cost
box for your estimated data storage cost.
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
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global:estimateDataSize" \
-d '{
  "website_data_source": {
    "estimator_uri_patterns": {
      provided_uri_pattern: "URI_PATTERN_TO_INCLUDE",
      exact_match: EXACT_MATCH_BOOLEAN
    },
    "estimator_uri_patterns": {
      provided_uri_pattern: "URI_PATTERN_TO_EXCLUDE",
      exact_match: EXACT_MATCH_BOOLEAN,
      exclusive: EXCLUSIVE_BOOLEAN
    }
  }
}'

```

### Code Example 2 (text)

```text
{
  "name": "projects/PROJECT_ID/locations/global/operations/estimate-data-size-01234567890123456789",
  "metadata": {
    "@type":  "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata"
  }
}

```

### Code Example 3 (text)

```text
curl -X GET \
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
"https://discoveryengine.googleapis.com/v1/OPERATION_NAME"

```

### Code Example 4 (text)

```text
{
  "name": "projects/PROJECT_ID/locations/global/operations/estimate-data-size-01234567890123456789",
  "metadata": {
    "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata"
  }
}

```

### Code Example 5 (text)

```text
{
  "name": "projects/PROJECT_ID/locations/global/operations/estimate-data-size-01234567890123456789",
  "metadata": {
    "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata",
    "createTime": "2023-12-08T19:54:06.911248Z"
  },
  "done": true,
  "response": {
    "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeResponse",
    "dataSizeBytes": DATA_SIZE_BYTES,
    "documentCount": DOCUMENT_COUNT
  }
}

```

