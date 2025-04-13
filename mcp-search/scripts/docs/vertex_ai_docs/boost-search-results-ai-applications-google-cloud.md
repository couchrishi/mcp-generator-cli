# Boost search results  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/boost-search-results](https://cloud.google.com/generative-ai-app-builder/docs/boost-search-results)

Home
AI Applications
Documentation
Guides
Send feedback
Boost search results
Stay organized with collections
Save and categorize content based on your preferences.
You can specify boost conditions in your search request to promote or demote
certain documents in your search results. When a document fulfills the specified
conditions, boost values are applied to it and the results are ordered
accordingly. You can also specify custom numerical values and timestamp values
that let you order the results based on parameters such as popularity and
freshness.
The boost specification in a search request is different from a boost control
that's attached to a serving config. The boost specification in the
boostSpec
field overrides the boost control defined in the
boostAction
field of a serving config. For more information about boost controls, see
About boost controls
.
This page describes the following types of boost specifications:
Boost with a fixed condition
Boost using custom numerical attributes
Boost according to freshness
You can apply these boost specifications to query media search apps and
generic search apps that contain structured, unstructured, and website data.
These specifications are not applicable to healthcare search apps.
Boost with a fixed condition
To boost results by a fixed amount based on whether they satisfy a condition,
do the following:
Specify the boost specification in the
boostSpec
field when you send a
servingConfigs.search
request.
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": "
BOOST_CONDITION
",
"boost":
BOOST_VALUE
}
}
}
The specification contains the following parameters:
BOOST_CONDITION
:
a
text filter expression
to select the documents to which boost is applied. The filter must evaluate
to a boolean value.
BOOST_VALUE
:
a floating point number in the range [-1,1]. When the value is
negative, results are demoted (they appear lower down in the
results). When the value is positive, results are promoted
(they appear higher up in the results).
Example use case
Suppose your data store contains data about hotels and their star ratings. You want to
boost hotels with star ratings greater than or equal to three. The star rating is
available in the
star_rating
numerical field. You can specify the
condition
in the
boostSpec
as
star_rating >= 3.0
and a boost value of 0.7 to boost
all hotels with
star_rating
of 3.0 or higher by an equal amount.
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": "star_rating>=3.0",
"boost": 0.7
}
}
}
Boost using custom numerical attributes
You can boost results based on custom numerical attributes in a
piecewise linear
manner by specifying control points and their corresponding boost values.
To specify a boost specification using custom numerical attributes,
do the following:
Specify the boost specification in the
boostSpec
field when you send a
servingConfigs.search
request.
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": "
BOOST_CONDITION
",
"boostControlSpec": {
"attributeType": "NUMERICAL",
"interpolationType": "LINEAR",
"fieldName": "
CUSTOM_ATTRIBUTE_FIELD_NAME
",
"controlPoints": [
{
"attributeValue": "
CUSTOM_ATTRIBUTE_VALUE_1
",
"boostAmount":
BOOST_AMOUNT_1
},
{
"attributeValue": "
CUSTOM_ATTRIBUTE_VALUE_2
",
"boostAmount":
BOOST_AMOUNT_2
}
]
}
}
}
}
The specification contains the following parameters:
BOOST_CONDITION
:
a
text filter expression
to select the documents to which boost is applied. The filter must evaluate
to a boolean value.
CUSTOM_ATTRIBUTE_FIELD_NAME
: the field name of the
custom numerical attribute whose value decides the boost amount.
CUSTOM_ATTRIBUTE_VALUE
: the numerical value of the
custom attribute for a given control point with a string data type. For
example,
"3.3"
or
"12"
. For more information, see
ControlPoint
.
BOOST_AMOUNT
:
a floating point number in the range [-1,1]. When the value is
negative, results are demoted (they appear lower down in the
results). When the value is positive, results are promoted
(they appear higher up in the results).
Indicates the boost
amount mapped to the custom attribute for a given control point.
When a document in the search result meets the specified condition, a boost amount is
applied as follows:
Attribute value
Boost amount
Less than the first control point
Is equal to the boost amount of the first control point
Equal to control point
Is equal to the mapped boost amount
Between control points
Is calculated by
linear interpolation
Greater than the last control point
Is equal to the boost amount of the last control point
Example use case
Suppose your data store contains data about hotels and their star ratings. You want to
boost the hotel search results in proportion to their star
ratings. You can define the boost specification as follows:
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": "star_rating >= 3.0",
"boostControlSpec": {
"attributeType": "NUMERICAL",
"interpolationType": "LINEAR",
"fieldName": "star_rating",
"controlPoints": [
{
"attributeValue": "3.5",
"boostAmount": 0.25
},
{
"attributeValue": "4.0",
"boostAmount": 0.30
},
{
"attributeValue": "4.5",
"boostAmount": 0.32
}
]
}
}
}
}
For this scenario, the search results are boosted as follows:
Star rating
Boost amount
less than or equal to 3.5
0.25
between 3.5 and 4.0
between 0.25 and 0.30, calculated using linear interpolation
equal to 4.0
0.30
between 4.0 and 4.5
between 0.30 and 0.32, calculated using linear interpolation
greater than or equal to 4.5
0.32
Boost according to freshness
You can boost results based on datetime attributes in a
piecewise linear
manner by specifying control points and their corresponding boost values.
To specify a boost specification using custom datetime attributes,
do the following:
Specify the boost specification in the
boostSpec
field when you send a
servingConfigs.search
request.
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": "
BOOST_CONDITION
",
"boostControlSpec": {
"fieldName": "
DATETIME_FIELD_NAME
",
"attributeType": "FRESHNESS",
"interpolationType": "LINEAR",
"controlPoints": [
{
"attributeValue": "
DURATION_VALUE_1
",
"boostAmount":
BOOST_AMOUNT_1
},
{
"attributeValue": "
DURATION_VALUE_2
",
"boostAmount":
BOOST_AMOUNT_2
}
]
}
}
}
}
The specification contains the following parameters:
BOOST_CONDITION
:
a
text filter expression
to select the documents to which boost is applied. The filter must evaluate
to a boolean value.
DATETIME_FIELD_NAME
: the field name of a custom
DATETIME
attribute, such as date of publication or date of last update,
or a predefined Google-inferred attribute, such as
datePublished
.
DURATION_VALUE
: the duration value in
dayTimeDuration
data type
that decides the freshness of a document. This is calculated as the
duration between the datetime when the search is performed and the datetime
of the custom datetime attribute of a document. The duration value must be
specified according to the ISO 8601 format in the pattern
[nD][T[nH][nM][nS]]
. For example, the duration between January 1, 2024
and March 1, 2024 can be expressed as
59D
. Similarly, the duration of two
and a half days can be expressed as
2DT12H
. For more information, see
ControlPoint
.
BOOST_AMOUNT
:
a floating point number in the range [-1,1]. When the value is
negative, results are demoted (they appear lower down in the
results). When the value is positive, results are promoted
(they appear higher up in the results).
Indicates the boost
amount mapped to the custom datetime attribute for a given control point.
When a document in the search result meets the specified condition, a boost amount is
applied as follows:
Duration value
Boost amount
Less than the first control point
Is equal to the boost amount of the first control point
Equal to a given control point
Is equal to the mapped boost amount
Between control points
Is calculated by linear interpolation
Greater than the last control point
Is equal to the boost amount of the last control point
Example use case using a custom datetime attribute
Suppose your data store contains structured data where each document has a
publication date. You want to boost the search results in proportion to
their freshness. You can define the boost specification as follows:
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": true,
"boostControlSpec": {
"fieldName": "publication_date",
"attributeType": "FRESHNESS",
"interpolationType": "LINEAR",
"controlPoints": [
{
"attributeValue": "7D",
"boostAmount": 0.40
},
{
"attributeValue": "30D",
"boostAmount": 0.37
},
{
"attributeValue": "60D",
"boostAmount": 0.32
},
{
"attributeValue": "90D",
"boostAmount": 0
}
]
}
}
}
}
For this scenario, the search results are boosted as follows:
Freshness
Boost amount
less than or equal to 7 days
0.40
between 7 and 30 days
between 0.40 and 0.37, calculated using linear interpolation
equal to 30 days
0.37
between 30 and 60 days
between 0.37 and 0.32, calculated using linear interpolation
equal to 60 days
0.32
between 60 and 90 days
between 0.32 and 0.0, calculated using linear interpolation
greater than or equal to 90 days
0.0
Example use case using a Google-inferred page date
When crawling through the web pages in your website data store, Google infers
page data using the properties that apply to your content.
Vertex AI Search adds these inferred page data properties to your
schema. This inferred data
includes the following predefined date properties:
datePublished
: the date and time when the page was first published
dateModified
: the date and time when the page was most recently modified
These properties are indexed automatically. You can directly use these date
properties to enrich your search without adding them to your schema.
You can use these predefined properties to boost your page. For example, you can
define the boost specification by setting the
fieldName
field to
pageModified
as follows:
{
"boostSpec": {
"conditionBoostSpecs": {
"condition": true,
"boostControlSpec": {
"fieldName": "dateModified",
"attributeType": "FRESHNESS",
"interpolationType": "LINEAR",
"controlPoints": [
{
"attributeValue": "7D",
"boostAmount": 0.35
},
{
"attributeValue": "30D",
"boostAmount": 0.30
}
]
}
}
}
}
Google infers these dates on a best-effort basis and the inferred dates
might not match the actual dates. These fields are populated only when Google
has high confidence. When these date values are missing, these fields become
nullable.
As a best practice, Google recommends that your domain owner or website
administrator updates these properties for your web pages and
that you
manually refresh
your Vertex AI Search website data
store after the update. For more information, see the
Help
Google Search know the best date for your web
page
blog post and learn
How structured data works in Google
Search
.
To add custom structured data attributes to enrich your index, see
Add custom structured data attributes to the data store schema
Boost amount adjustment
In addition to factors that influence the ranking of a result, such as keyword
matching, context matching, and relevance, the boost condition impacts the
ranking of a result significantly. Therefore, you must carefully calibrate the
boost amount. Google recommends that you start with a low and precise boost
amount, such as 0.1 or less, and adjust it based on the search output.
Example use case with relevance filter
The regulation of boost amount is especially important when using the
boostSpec
field with relevance filter. For more information on relevance
filter, see
Filter searches by document-level relevance
.
Suppose you have different documents with different published dates. For a
particular query, the following table represents the absolute ranking without
implementing any boost condition or relevance filter and indicates the relevance
of the documents to query.
Document
Published date
Relevance
Ranking
A
Feb 1, 2024
High
#1
B
Mar 1, 2024
High
#2
C
Apr 1, 2024
Lowest
#3
D
May 1, 2024
Medium
#4
E
Jun 1, 2024
Low
#5
On Jun 6, 2024, you add the following search conditions in your search request:
Relevance filter set to
LOW
.
Boost value such that documents published during the last 31 days are boosted
by a value of 0.7 and documents older than a week but fresher than 60 days are
boosted by value of 0.6.
In your search output, the results are first filtered by relevance and then the
boost amount is applied. Therefore, the applied conditions alter the
ranking of the pages in the results in the following manner:
Document
Published date
Relevance
Ranking
E
Jun 1, 2024
Low
#1
D
May 1, 2024
Medium
#2
A
Feb 1, 2024
High
#3
B
Mar 1, 2024
High
#4
The result with the lowest relevance is filtered out because of the relevance filter.
The documents that are less relevant to a query are ranked as top results
because they are boosted by a large boost amount. The more relevant results
are ranked lower.
Therefore, Google recommends that you start the boost amount from a low, precise
value and adjust the value depending on the search output. In this example,
starting with boost amounts of 0.1 or less might fetch more relevant results on
the top.
What's next
Make a search request
with the boost specification
in the
boostSpec
field.
To understand the impact of boost on the search quality of a
generic search app,
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
{
  "boostSpec": {
    "conditionBoostSpecs": {
      "condition": "BOOST_CONDITION",
      "boost": BOOST_VALUE
    }
  }
}

```

### Code Example 2 (text)

```text
{
  "boostSpec": {
    "conditionBoostSpecs": {
      "condition": "star_rating>=3.0",
      "boost": 0.7
    }
  }
}

```

### Code Example 3 (text)

```text
{
  "boostSpec": {
    "conditionBoostSpecs": {
        "condition": "BOOST_CONDITION",
        "boostControlSpec": {
          "attributeType": "NUMERICAL",
          "interpolationType": "LINEAR",
          "fieldName": "CUSTOM_ATTRIBUTE_FIELD_NAME",
          "controlPoints": [
            {
              "attributeValue": "CUSTOM_ATTRIBUTE_VALUE_1",
              "boostAmount": BOOST_AMOUNT_1
            },
            {
              "attributeValue": "CUSTOM_ATTRIBUTE_VALUE_2",
              "boostAmount": BOOST_AMOUNT_2
            }
          ]
        }
    }
  }
}

```

### Code Example 4 (text)

```text
{
  "boostSpec": {
    "conditionBoostSpecs": {
        "condition": "star_rating >= 3.0",
        "boostControlSpec": {
          "attributeType": "NUMERICAL",
          "interpolationType": "LINEAR",
          "fieldName": "star_rating",
          "controlPoints": [
            {
              "attributeValue": "3.5",
              "boostAmount": 0.25
            },
            {
              "attributeValue": "4.0",
              "boostAmount": 0.30
            },
            {
              "attributeValue": "4.5",
              "boostAmount": 0.32
            }
          ]
        }
    }
  }
}

```

### Code Example 5 (text)

```text
{
  "boostSpec": {
    "conditionBoostSpecs": {
        "condition": "BOOST_CONDITION",
        "boostControlSpec": {
          "fieldName": "DATETIME_FIELD_NAME",
          "attributeType": "FRESHNESS",
          "interpolationType": "LINEAR",
          "controlPoints": [
            {
              "attributeValue": "DURATION_VALUE_1",
              "boostAmount": BOOST_AMOUNT_1
            },
            {
              "attributeValue": "DURATION_VALUE_2",
              "boostAmount": BOOST_AMOUNT_2
            }
          ]
        }
    }
  }
}

```

### Code Example 6 (text)

```text
{
  "boostSpec": {
    "conditionBoostSpecs": {
        "condition": true,
        "boostControlSpec": {
          "fieldName": "publication_date",
          "attributeType": "FRESHNESS",
          "interpolationType": "LINEAR",
          "controlPoints": [
            {
              "attributeValue": "7D",
              "boostAmount": 0.40
            },
            {
              "attributeValue": "30D",
              "boostAmount": 0.37
            },
            {
              "attributeValue": "60D",
              "boostAmount": 0.32
            },
            {
              "attributeValue": "90D",
              "boostAmount": 0
            }
          ]
        }
    }
  }
}

```

### Code Example 7 (text)

```text
{
  "boostSpec": {
    "conditionBoostSpecs": {
        "condition": true,
        "boostControlSpec": {
          "fieldName": "dateModified",
          "attributeType": "FRESHNESS",
          "interpolationType": "LINEAR",
          "controlPoints": [
            {
              "attributeValue": "7D",
              "boostAmount": 0.35
            },
            {
              "attributeValue": "30D",
              "boostAmount": 0.30
            }
          ]
        }
    }
  }
}

```

