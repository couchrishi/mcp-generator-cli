# Configure advanced autocomplete  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/configure-advanced-autocomplete](https://cloud.google.com/generative-ai-app-builder/docs/configure-advanced-autocomplete)

Documentation
Guides
Configure advanced autocomplete
Stay organized with collections
Save and categorize content based on your preferences.
This page describes Vertex AI Search's advanced autocomplete feature.
In the same way as basic autocomplete, advanced autocomplete generates query
suggestions based on the first few characters entered for the query.
Before reading this page, become familiar with Vertex AI Search's
basic autocomplete. See
Configure autocomplete
.
Key features of advanced autocomplete
The key features of advanced autocomplete that distinguish it from the basic
autocomplete are as follows:
Blended search:
Advanced autocomplete can be used with
blended search
apps
, those are generic search apps that are
connected to more than one data store.
Access control:
Advanced autocomplete respects access controls. (Access
controls are also referred to ACLs, access control lists.) Advanced
autocomplete only suggest searches that are related to documents that the
searcher has access to. For information about access control, see
Use data
source access control
.
Language boost:
Advanced autocomplete can be set to boost suggestions in one or more
languages. For example, if the browser language is Dutch, autocomplete
suggestions in that language could be boosted. For more information, see
Send an autocomplete request with a language boost
.
Recent queries:
With advanced autocomplete, instead of regular
autocomplete query suggestions, users can get their recent queries that
prefix-match the letters that they type. For more information, see
Send an
autocomplete request and return recent queries
.
Before you begin
Review and optionally edit the autocomplete settings for your app. See
Update autocomplete settings
.
Particularly when testing, for smaller data stores, we recommend setting
Enable autocomplete
to
Now
. This is
because small data stores might not contain sufficient data to
provide accurate suggestions.
Send autocomplete requests
The following shows how to send advanced autocomplete requests using the
completionConfig.completeQuery
method.
REST
To send an autocomplete request using the API, follow these steps:
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
Call the
completionConfig.completeQuery
method.
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
/locations/global/collections/default_collection/engines/
APP_ID
/completionConfig:completeQuery"
\
-d
'{
"query":"
QUERY_STRING
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY_STRING
: the typeahead input used to fetch suggestions.
Send an autocomplete request with a language boost
You can boost bury autocomplete suggestions according to language code, for
example, make autocomplete suggestions in some languages more or less likely to appear.
The boost value must be between -1 and 1. Setting a negative number "buries"
autocomplete suggestions in that language and a positive number boosts the
language.
Use two-letter language tags defined by BCP 47—for example,
en
,
fr
,
hi
,
and
zh
.
REST
To send an autocomplete request that includes a language boost value,
follow these steps:
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
Call the
completionConfig.completeQuery
method.
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
/locations/global/collections/default_collection/engines/
APP_ID
/completionConfig:completeQuery"
\
-d
'{
"query":"
QUERY_STRING
",
"boostSpec": {
"conditionBoostSpecs": [{
"condition": "(langCode: ANY(
LANG_CODE
))",
"boost":
BOOST_VALUE
}]
}
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY_STRING
: the typeahead input used to fetch suggestions.
LANG_CODE
: the two-letter code for one or more languages,
in escaped quotes. For example,
\"fr\", \"es\"
to apply
the boost value to Spanish and French.
BOOST_VALUE
: a floating point number between -1 and 1. When
the value is negative, autosuggestions in the language are demoted (they
appear lower down in the list of suggestions). When the value is
positive, suggestions are promoted (they appear higher up in the list).
Example command
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/completionConfig:completeQuery" \
-d '{
"query": { "text": "Co"}
"boostSpec": {
"conditionBoostSpecs": [{
"condition": "(langCode: ANY(\"es\", \"fr\"))",
"boost": 0.75 }, {
"condition": "(langCode: ANY(\"en\"))",
"boost": -1
}]
}
}'
In this example, the autocomplete suggestions for the query
Co
are
boosted (placed higher in the autosuggestion list) if they are in French
or Spanish and buried (placed lower in the autosuggestion list) if
they are in English.
Send an autocomplete request and return recent queries
Returns as suggestions a list of the user's most recent queries that
prefix-match the query on the request.
The matching query suggestions are listed from the most recent to the oldest. To
use recent search, the user pseudo ID must be provided.
Example
An employee is querying their company intranet site to get information about
taking vacations. The employee has performed the following queries, listed from
most recent to oldest:
PTO
,
Vacation blackout periods
,
How much vacation time do I have?
,
Time
off
,
Vacation policy
,
covering a vacant position during absences
, and
Can I
take unpaid time off?
.
Now, in response to the employee typing
vac
in the search box, the
autocomplete suggestions would be as follows:
Vacation blackout periods
How much vacation time do I have?
Vacation policy
Covering a vacant position during absences
Procedure
To send an autocomplete request that returns the user's most recent queries,
follow these steps:
REST
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
Call the
completionConfig.completeQuery
method.
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
/locations/global/collections/default_collection/engines/
APP_ID
/completionConfig:completeQuery"
\
-d
'{
"query":"
QUERY_STRING
",
"suggestionTypes": ["RECENT_SEARCH"],
"userPseudoId": "
USER_PSEUDO_ID
"
}'
Replace the following:
PROJECT_ID
: the ID of your Google Cloud project.
APP_ID
: the ID of the Vertex AI Search app.
QUERY_STRING
: the typeahead input used to fetch suggestions.
USER_PSEUDO_ID
: a pseudonymized identifier of the user. You
can use an HTTP cookie for this field, which uniquely identifies a
visitor on a single device. Don't set this field to the same identifier
for multiple users. This would combine their query histories. Don't
include personally identifiable information (PII) in this field.
Example command and result
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/my-project-123/locations/global/collections/default_collection/engines/my-app/completionConfig:completeQuery" \
-d '{
"query": "hol",
"suggestionTypes": ["RECENT_SEARCH"],
"userPseudoId": "test_user"
}'
{
"recentSearchSuggestions": [
{
"suggestion": "holiday readiness",
"recentSearchTime": "2024-11-19T18:27:07.261698Z"
},
{
"suggestion": "holiday freeze",
"recentSearchTime": "2024-11-19T18:25:45.744021Z"
},
{
"suggestion": "holiday",
"recentSearchTime": "2024-11-19T18:20:08.916884Z"
}
]
}
Use an autocomplete denylist
You can use a denylist to prevent specific terms from appearing as autocomplete
suggestions.
Although advanced autocomplete is at the app-level, denylists are at the
data-store-level. This is significant if your app is a blended search app.
Create a denylist for each data store connected to the app.
For information about creating and using denylists, see
Use an autocomplete
denylist
.
Use an imported list of autocomplete suggestions
You can choose to provide your own list of autocomplete suggestions instead of
using autocomplete suggestions generated from an autocomplete data model.
For information about how import a list, see
Use an imported list of
autocomplete suggestions
.
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
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
-d '{
      "query":"QUERY_STRING"
    }'

```

### Code Example 2 (text)

```text
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
-d '{
      "query":"QUERY_STRING",
      "boostSpec": {
         "conditionBoostSpecs": [{
           "condition": "(langCode: ANY(LANG_CODE))",
           "boost": BOOST_VALUE
         }]
      }
    }'


```

### Code Example 3 (text)

```text

curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/completionConfig:completeQuery" \
-d '{
      "query":"QUERY_STRING",
      "suggestionTypes": ["RECENT_SEARCH"],
      "userPseudoId": "USER_PSEUDO_ID"
    }'


```

