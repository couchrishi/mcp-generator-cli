# Configure results for the search widget  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes](https://cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes)

Home
AI Applications
Documentation
Guides
Send feedback
Configure results for the search widget
Stay organized with collections
Save and categorize content based on your preferences.
This section describes how to configure results for the search widget, depending
on the type of search app you have.
If you use third-party access control for your data sources, these configuration
settings also apply to the web app.
Search widget concepts
Here are some concepts to help you understand how to use the controls on
the
UI
tab.
Snippet
: A short section of text, typically a sentence, under the
document title. By default, a snippet is displayed for each search result for
website and unstructured data.
Search with an answer
: This feature provides a paragraph of information
(the answer) synthesized from the top results of website or unstructured data.
You can customize the number of top results that the answer is based on. By
default, the top five results are summarized to create the answer. Search with
an answer cannot be combined with Search with follow-ups.
Search with follow-ups
: This feature for website and unstructured data
allows for follow-up questions that keep the context of the initial search
query.
Autocomplete
: Suggests search queries based on the first letters that
users enter into the search bar. For more information, see
Configure
autocomplete
.
Feedback
: Provides buttons
thumb_up
and
thumb_down
so that users can rate
the quality of the search results. This information is sent only to Google.
For more information, see
Configure widget feedback
.
Metadata
: If the data is structured or contains metadata, you
can configure which metadata fields to include in the search results. You can also map
fields to display names for facets. For more information, see
Configure facets for the search widget
.
Turning off Advanced LLM features
: If you turn off Advanced
LLM features for a search widget that is using search with follow-ups or
search with an answer, the widget stops working for all users. See
Turn
Advanced LLM features on or off
.
Image in answers
: This feature returns the following kinds of images with
the answers:
Charts generated from information in the answer
Images selected from an unstructured data store that a layout parser
parses
Use this feature with
Search with an answer
or
Search with
follow-ups
and the stable large language model or any Gemini
model 2.0 or later. To return images from the corpus in the answer,
enable snippets or extractive content. For more information, see
Generate
charts for answer
and
Retrieve existing images from the data
store
.
Search-as-you-type
: Available only for media apps. This feature performs a
search after each keystroke. You don't need to press
Enter
to get a search result. For more information, see
Get search-as-you-type
results for a media app
.
Configure search results for unstructured or website data
The search widget for unstructured and website data offers the following search
customizations:
Search (single-turn)
Search with an answer (single-turn search with summarization)
Search with follow-ups (multi-turn search)
For search with an answer and search with follow-ups, you need turn on some
advanced settings:
For search apps with unstructured data:
Advanced LLM
features
For website search apps:
Advanced LLM features
and
Advanced website indexing
To configure how the widget displays search results for unstructured data:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit.
In the navigation menu, click
Configurations
.
Click the
UI
tab.
Edit the fields on the tab.
Use the
Preview
pane to make sure your changes are displayed
as expected.
Click
Save and publish
to apply your changes.
Configure search results for healthcare data
The search widget for healthcare data offers the following search customizations:
Search
Search with an answer
For search with an answer, turn on
advanced LLM features
.
To configure how the widget displays search results for healthcare data:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the app that you want to edit.
In the navigation menu, click
Configurations
.
Click the
UI
tab.
In the Search type list, select one of the following:
Search
: to perform a single-turn search
Search with an answer
: to perform a single-turn search with a generative AI generated answer
In the
Large language models for summarization
section, select one of
the following:
Stable
: a stable, generally available model that points to the
Gemini 2.0 Flash 1
model, which is based on the
gemini-2.0-flash-001
model.
Gemini 1.0 Pro 2
: a generally available model that's based on
the
gemini-1.0-pro-002
model.
Gemini 1.5 Flash 1
: a stable, generally available model that's based
on the
gemini-1.5-flash-001
model.
For more information, see
Generally available (GA) models
.
Gemini 2.0 Flash 1
: a stable, generally available model that's based
on the
gemini-2.0-flash-001
model.
For more information, see
Generally available (GA) models
.
Click
Save and publish
to apply your changes.
Configure search results for structured data
For structured data, by default, the widget displays all of the name-value
pairs for each item in the search results. You can use the
Configurations
page in the Google Cloud console to customize how the widget displays search
results.
The following list shows the primary fields for displaying search results:
Title.
An item title that a user can click to select that item in a
search result.
Thumbnail.
The URL of an image to be shown next to the item title in a
search result.
URL.
A URL that the user is taken to when they click the item's title.
You can display up to three additional fields in your search results and
configure how they appear.
In addition, you can select facets to filter search results on and set display
names for them. For more about configuring widget facets, see
Configure facets
for the search widget
.
To configure how the widget displays search results for structured data:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
Click the name of the search app that you want to edit.
Click
Configurations
.
Click the
UI
tab.
If you have multiple data stores connected to your app, select the data
store to configure results for.
Expand the
Configure fields in results
section.
In the
Preview
pane, type a query and press
Enter
to view how search
results are displayed with your current settings. The preview updates
automatically when you enter new settings.
Optional: Click a device icon to see the preview in desktop or mobile
format.
To configure the primary fields (
Title
,
Thumbnail
, and
URL
) in
your search results:
Click the
Title
box and select a field to map to the titles of your
search results. Or, select
None
if you don't want titles to appear
in search results.
Click the
Thumbnail
box and select a field to map to the thumbnail
images in your search results. Or, select
None
if you don't want
thumbnail images to appear in search results.
Click the
URL
box and select a field that maps to the items that
open when users click item titles in search results. Or, select
None
if you don't want item titles in your search results to link to
items.
To add additional fields to your search results:
Click the
Text 1
box and select a field that you want to display in
your search results. By default, only the field value is displayed in
search results.
Click the arrow next to the
Text 1
box to display the
Template
box. The
{value}
field in
Template
box represents the field
value to display in the search result. Add text before or after the
{value}
field (or both) to give context to the value in the search
results. For example, suppose you selected
price
in the
Text 1
box, and the price value for a particular item is 42. If you update the
Template
field to
"Total
Price: {value} USD"
, then "Total Price: 42 USD" is displayed in the
search results for that item.
To add additional fields, repeat these steps for the
Text 2
and
Text 3
boxes.
To configure facet settings:
Expand the
Facet settings
section.
Select a field to set as a facet and enter a display name.
To add more facets, click
Add facet
.
Check the
Preview
pane to make sure your changes display correctly.
Click
Save and publish
to apply your changes.
Next steps
Get search results
Add the search widget to a web page
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-12 UTC.

