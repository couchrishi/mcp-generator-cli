# Answer generation model versions and lifecycle  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/answer-generation-models](https://cloud.google.com/generative-ai-app-builder/docs/answer-generation-models)

Home
AI Applications
Documentation
Guides
Send feedback
Answer generation model versions and lifecycle
Stay organized with collections
Save and categorize content based on your preferences.
Vertex AI Search offers multiple model versions for you to choose when
generating answers. You can choose the model versions when using
search
summaries
and
answers and
follow-ups
.
Available models
Vertex AI Search uses two types of models for question and answering
use cases:
Vertex AI LLM models that have been tested on question and
answering tasks
Vertex AI Search models that are based on Vertex AI LLM
models and further trained to address question and answering tasks
Vertex AI Search models share the same discontinuation date as their
base Vertex AI LLM models. The base LLM model is available for six
months after the release date of the next version of the model, per the
Vertex
AI model lifecycle
policy
.
Leave enough time to migrate to new models before the discontinuation dates.
The following table lists model version specifications. When you set a model
specification, the API uses the specified model to generate answers.
Model version
Generic
Healthcare
Description
Context window
Discontinuation date
Description
Context window
Discontinuation date
stable
The default model choice if the model version is not set.
The
stable
model specification points to
gemini-2.0-flash-001/answer_gen/v1
.
The model designated as
stable
changes periodically as new
models and versions become available.
128K
N/A
The default model choice if the model version is not set.
The
stable
model specification points to
gemini-2.0-flash-001/answer_gen/v1
.
The model designated as
stable
changes periodically as new
models and versions become available.
128K
N/A
gemini-2.0-flash-001/answer_gen/v1
A Vertex AI Search model based on the
gemini-2.0-flash-001
model with additional tuning to address question and answering tasks.
The model is frozen after release.
128K
Feb 5, 2026
A Vertex AI Search model based on the
gemini-2.0-flash-001
model with additional tuning to address question and answering tasks.
The model is frozen after release.
128K
Feb 5, 2026
gemini-1.5-flash-002/answer_gen/v1
A Vertex AI Search model based on the
gemini-1.5-flash-002
model with additional tuning to address question and answering tasks.
The model is frozen after release.
128K
Sept 24, 2025
Not Available
gemini-1.5-flash-001/answer_gen/v2
A Vertex AI Search model based on the
gemini-1.5-flash-001
model with additional tuning (version 2) on blended structured and unstructured data to address question and answering tasks.
The model is frozen after release.
128K
May 24, 2025
A Vertex AI Search model based on the
gemini-1.5-flash-001
model with additional tuning (version 2) on blended structured and unstructured data to address question and answering tasks.
The model is frozen after release.
128K
May 24, 2025
gemini-1.5-flash-001/answer_gen/v1
A Vertex AI Search model based on the
gemini-1.5-flash-001
model with additional tuning to address question and answering tasks.
The model is frozen after release.
128K
May 24, 2025
A Vertex AI Search model based on the
gemini-1.5-flash-001
model with additional tuning to address question and answering tasks.
The model is frozen after release.
128K
May 24, 2025
gemini-1.0-pro-002/answer_gen/v1
A Vertex AI Search based on the
gemini-1.0-pro-002
model with additional training to address question and answering tasks.
The model is frozen after release.
32K
April 9, 2025
A Vertex AI Search model based on the
gemini-1.0-pro-002 model
with additional training to address question and answering tasks.
The model is frozen after release.
32K
April 9, 2025
gemini-1.0-pro-001/answer_gen/v1
Points to the
gemini-1.0-pro-001
model.
The model is frozen after release.
32K
April 9, 2025
Not Available
preview
The preview model specification points to the latest
gemini-1.5-pro-002
model. The preview model is subject to change without notification. If
you use
preview
as the model, you might see changes in the responses when the
model changes. If you want consistency in the responses, select a
specific model.
128K
N/A
The preview model specification points to the latest
gemini-1.5-pro-002
model. The preview model is subject to change without notification. If
you use
preview
as the model, you might see changes in the responses when the
model changes. If you want consistency in the responses, select a
specific model.
128K
N/A
What's next
Get search summaries
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-12 UTC.

