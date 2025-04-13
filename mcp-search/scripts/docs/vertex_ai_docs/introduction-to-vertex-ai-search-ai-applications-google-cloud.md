# Introduction to Vertex AI Search  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction](https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction)

Home
AI Applications
Documentation
Guides
Send feedback
Introduction to Vertex AI Search
Stay organized with collections
Save and categorize content based on your preferences.
This page introduces the key search and recommendations features of
Vertex AI Search.
For information about search and recommendations for media, see
Introduction to
AI Applications for media
.
Information retrieval using AI and LLMs
Vertex AI Search brings together the power of deep information
retrieval, state-of-the-art natural language processing, and the latest in large
language model (LLM) processing to understand user intent and return the most
relevant results for the user.
With Vertex AI Search, you can build a Google-quality search app
on data you control. You also have the option to use the search results that you
retrieve to ground generative AI LLM responses. For more information, see the
blog post
Your RAG powered by Google Search
.
With recommendations, you can build a recommendations app across your data
that suggests content similar to the content that the user is viewing.
An easy experience to get started
Vertex AI Search makes it easy to get started with high-quality search
or recommendations based on data that you provide. As part of the setup
experience, you can:
Use your existing Google Account or sign up for one.
Use your existing Google Cloud project or create one.
Create an app and attach a data store to it. Provide data to search or
recommend by entering the URLs for your website content, importing your data
from BigQuery or Cloud Storage, or importing FHIR R4 data
from Cloud Healthcare API, or uploading through RESTful CRUD APIs. Syncing data
from third-party data sources is available in Preview with allowlist.
Embed JavaScript widgets and API samples to integrate search or
recommendations into your website or applications.
Data stores and apps
With Vertex AI Search, you create a search or recommendations app and
attach it to a data store. You import your data into a data store and index your
data. Apps and data stores have a one-to-one relationship.
There are various kinds of data stores that you can create, based on the type of
data you use. Each data store can contain one type of data:
Website data
: You can provide domains such as
yourexamplewebsite.com/faq
and
yourexamplewebsite.com/events
and enable
search over the content at those domains.
Structured data
: A data store with structured data enables hybrid search
(keyword and semantic) or recommendations over structured data such as a
BigQuery table or NDJSON files. For example, you can enable search
or recommendations over a product catalog for your ecommerce experience, a
movie catalog for movie search or recommendations, or a directory of doctors
for provider search or recommendations.
Structured data for media
: A data store with a structured data schema
that is specific for the media industry. For example, a data store for media
might contain information about videos, news articles, music files, or
podcasts.
Unstructured data
: An unstructured data store enables hybrid search
(keyword and semantic) over data such as documents and images. For example, a
financial institution can enable search over their private corpus (index) of
financial research publications, or a biotech company can enable
search over their private repository of medical research.
Healthcare data
: A healthcare data store enables hybrid search (keyword
and semantic) over healthcare FHIR R4 data imported from Cloud Healthcare API.
For example, a healthcare provider can search over a patient's clinical
history using exploratory queries.
For more information, see
About apps and data stores
.
Google Cloud console or the API?
You can implement Vertex AI Search in any of the following ways:
Use the Google Cloud console.
Use the
AI Applications
page of the console for a
quick-start experience using a web interface. From the
console, you can create your search app, import your data,
test the user experience, and view analytics.
Use the AI Applications API.
Use the AI Applications API when you're ready
to integrate search or recommendations into your website or applications.
Use both the Google Cloud console and the API.
You can set up your app
and import your data using the console, for example, and then
use the API to test the user experience and integrate it into your website
or application.
What's next
About apps and data stores
Get started with generic search
Get started with generic recommendations
Get started with media search
Get started with media recommendations
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-12 UTC.

