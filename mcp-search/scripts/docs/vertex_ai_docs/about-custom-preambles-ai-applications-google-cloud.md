# About custom preambles  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/preamble](https://cloud.google.com/generative-ai-app-builder/docs/preamble)

Home
AI Applications
Documentation
Guides
Send feedback
About custom preambles
Stay organized with collections
Save and categorize content based on your preferences.
This page discusses custom preambles and how you can write preambles to improve
the quality of generated answers.
The preamble sets the initial context and expectations for the LLM before
it processes your input document. The preamble influences the
quality of the generated summaries. There is a default preamble supplied
whenever you call the
answer
method. However, you have the option
to specify your own preamble instead of using the default.
For instructions on how to specify the preamble in the answer method call, see
Specify a custom preamble
.
For example, you can use the preamble to do the following:
Specify words that the model can and can't use.
Specify topics to focus on or avoid.
Specify the style, tone, and format of the response.
Tailoring the preamble can significantly improve the quality of
summaries.
The preamble should have two parts:
The task description
that describes the task you are asking the LLM to
perform. See
Examples of task descriptions
.
Additional instructions
that the LLM should follow. See
Examples and
tips for additional instructions
.
Examples of task descriptions
Here are some examples of task descriptions. The scenario is that your
employees want answers from a data store that contains many company documents.
Example 1
Task description to comprehensively cite sources:
Given a user query and a list of sources, write a response that cites individual
sources as comprehensively as possible.
Example 2
Task description to understand the user and focus on helpfulness:
You are an enterprise LLM summarization tool. Your task is to understand the
true intent of a user question in the context of enterprise search and
summarization, and provide a helpful answer to the user's question.
Example 3
Task description to summarize a conversation between a customer and an
assistant:
Given the conversation between a customer and a helpful assistant with some
search results, create a final answer for the assistant.
Examples and tips for additional instructions
The additional instructions should capture your specific key requirements.
The following table gives examples of additional instructions that you might
provide after the task description, what kind of problems each example
addresses, and why the preamble solves the problem.
Problem to solve
Solution
Examples
The answers need to be more tailored to the business needs
Provide additional context and instructions to ensure that the summary is
tailored to the specific use case and target audience.
Example 1
Utilize the specific context of the workspace (e.g. meeting notes, public
guidance, FAQ) to provide more accurate and relevant summaries.
Example 2
Summarize customer feedback, focusing on their pain points, feature
request and overall satisfaction. Highlight any actionable insights that
can help improve our product or service.
Example 3
For input documents of troubleshooting website, please summary the
problem statement, step-by-step solutions and any relevant tips or
warnings.
Example 4
"XYZ" is an internal forum for engineers to discuss technical problems,
you can use it to summarize technical issues, proposed solutions and any
unresolved challenges or next steps identified in the discussion.
Answer needs to be in a specific style
Clearly specify the style or tone and the intended audience.
Example 1
Summarize troubleshooting guide for customer support agent in a clear and
concise manner. The summary should be easy for a non-technical user to
understand.
Example 2
Summarize the technical documents for engineers. Focus on the core
functionality, system architecture, and potential challenges.
Answer needs to be in a specific format
Specify output format
Example 1
Use bullet points for steps, numbered lists for rankings, tables for
comparisons, code block for coding example
Example 2
Summarize the key takeaways in a numbered lists
Answer needs to be short
Explicitly instruct the LLM to generate "concise" or "brief" summaries.
You can also specify the word or sentence count if applicable.
Example 1
Please keep summaries concise and focused, providing only the most
essential information to address the user's query.
Example 2
The answer should be less than 200 words.
Answer needs to be more comprehensive
Encourage the LLM to include key details and important points.
Example
Please ensure key details are included.
Inclusion of prohibited topics
Define how the model should respond in certain situations.
Example
For political questions, the most helpful way is to politely refuse to
answer the question.
Reduce Hallucination (incorrect information)
Emphasize the importance of accuracy and instruct the LLM to strictly adhere to the information presented in the text.
Example 1
Keep the summary accurate, ensuring all claims are verifiable within the given context.
Example 2
Use exact words from the context if possible.
Examples of complete preambles
Here are some more examples of complete preambles, made up of the task
description and the additional instructions.
Example 1
Request a concise, accurate, and relevant summary and present it in a
user-friendly format.
You are an enterprise LLM summarization tool. Your task is to understand the
true intent of a user question in the context of enterprise search and
summarization, and provide a helpful answer to the user's question. Please keep
summaries concise and focused, providing only the most essential information to
address the user's query.
Please also structure and format the summary by
1) prioritize most relevant and accurate information to user's question
2) highlight critical information
3) structure the response and adapt the formatting to be user friendly (e.g.,
use bullet points for steps, numbered lists for rankings, tables for
comparisons, code block for coding example, etc).
Example 2
Provide a concise, friendly, and helpful final answer to a customer's query
based on a conversation.
Given the conversation between a customer and a helpful assistant with some
search results, create a final answer for the assistant.
The answer should addresses the query accurately and concisely (less than 10
sentences), while also being friendly and helpful. If the search results don't
provide enough information to fully answer the question, suggest additional
resources or steps the customer can take.
Example 3
Provide comprehensive and understandable answers and cite given sources.
Politely decline to answer any political questions.
Given a user query and a list of sources, write a response that cites individual
sources as comprehensively as possible.
The response should be suitable for a non-expert audience.
For political questions, the response should be a polite refusal to answer the
question.
Best practices
The following are some best practices for writing and tuning preambles:
Iterative Refinement:
Experiment with different preamble
variations and observe the impact on the answer quality.
User Feedback:
Gather feedback from users to identify recurring issues
and areas for improvement.
Stay Updated:
The effectiveness of preamble tuning can vary
depending on the model version and the nature of your documents. Continuously
experiment and refine your approach to achieve optimal results.
Thorough Evaluation:
Verifying modified preambles across all intended use
cases helps identify and mitigate potential biases or unexpected behavior
that may negatively impact summary quality in certain scenarios.
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
Given a user query and a list of sources, write a response that cites individual
sources as comprehensively as possible.

```

### Code Example 2 (text)

```text
You are an enterprise LLM summarization tool. Your task is to understand the
true intent of a user question in the context of enterprise search and
summarization, and provide a helpful answer to the user's question.

```

### Code Example 3 (text)

```text
Given the conversation between a customer and a helpful assistant with some
search results, create a final answer for the assistant.

```

### Code Example 4 (text)

```text
You are an enterprise LLM summarization tool. Your task is to understand the
true intent of a user question in the context of enterprise search and
summarization, and provide a helpful answer to the user's question.  Please keep
summaries concise and focused, providing only the most essential information to
address the user's query.

Please also structure and format the summary by

1) prioritize most relevant and accurate information to user's question

2) highlight critical information

3) structure the response and adapt the formatting to be user friendly (e.g.,
use bullet points for steps, numbered lists for rankings, tables for
comparisons, code block for coding example, etc).

```

### Code Example 5 (text)

```text
Given the conversation between a customer and a helpful assistant with some
search results, create a final answer for the assistant.

The answer should addresses the query accurately and concisely (less than 10
sentences), while also being friendly and helpful. If the search results don't
provide enough information to fully answer the question, suggest additional
resources or steps the customer can take.

```

### Code Example 6 (text)

```text
Given a user query and a list of sources, write a response that cites individual
sources as comprehensively as possible.

The response should be suitable for a non-expert audience.

For political questions, the response should be a polite refusal to answer the
question.

```

