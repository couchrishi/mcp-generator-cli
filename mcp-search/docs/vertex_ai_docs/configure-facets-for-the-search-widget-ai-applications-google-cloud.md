# Configure facets for the search widget  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets](https://cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets)

Home
AI Applications
Documentation
Guides
Send feedback
Configure facets for the search widget
Stay organized with collections
Save and categorize content based on your preferences.
Facets can be shown next to results in the search widget to help users filter
the results. You can use the
Configurations
page in the Google Cloud console to
specify which fields to use as facets on your widget for apps with structured
data or unstructured data with metadata.
Facet configuration is not supported for widgets for apps with website data or
unstructured data without metadata.
If you use access control for your data sources, these configuration
settings also apply to the web app.
Before setting a field as a facet, make sure that the field is set to
Retrievable
and
Indexable
. For more information, see
Configure field
settings
.
To set a field as a facet:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit.
Click
Configurations
.
Click the
UI
tab.
If you have multiple data stores connected to your app, select the data
store to configure facet settings for.
Expand the
Facet settings
section.
Click
Add facet
.
Select a field to use as a facet.
Enter a display name for the facet.
Click
Save and publish
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

