# Verify website domains  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/domain-verification](https://cloud.google.com/generative-ai-app-builder/docs/domain-verification)

Home
AI Applications
Documentation
Guides
Send feedback
Verify website domains
Stay organized with collections
Save and categorize content based on your preferences.
You need to verify the domains for the URL patterns that you have included
in your data store in these cases:
When you create a data store for website search and you turn on
advanced website indexing
When you upgrade your data store from basic website search to advanced website indexing
Domain verification approaches
You can use one of the following approaches to verify your domain:
Domain verification using domain association
: to associate your
Vertex AI Search data store to the specified domain.
This is useful when you're not the owner of the specified domain or when you
don't have access to the Google Search console needed to verify the domain.
In this approach, you need not contact the domain owner yourself, you can send
an association request to the domain owner through the Google Cloud console. The
domain owner can approve the association request through the Google Search
console.
Domain ownership verification
: to verify the domain in the following
cases:
When you're the domain owner of the specified domain
When you can contact the domain owner for verification through the
Google Search console
When you have access to the Google Search console to verify the domain
Domain ownership is the ownership of the domain to which your URL patterns
belong. This is different from being the owner of a Google Cloud project, which is
an Identity and Access Management (IAM) role.
When you turn on advanced website indexing to create a data store, you can
verify the domain for the websites you are indexing after
creating the data store. If you don't verify your domain ownership, your website
can't be indexed using advanced website indexing.
Domain verification behavior
Understand the following domain-verification behavior:
When you verify the domains for your URL patterns, you are verifying the entire domain.
For example, suppose if you verify the domain for
www.mysite.com/abc
and later add
www.mysite.com/def
to your data store, you won't need to verify the domain
for
www.mysite.com/def
. This is because
www.mysite.com/def
is within the domain
mysite.com
, which is already verified.
When you verify a domain, that domain is automatically verified
for all data stores in that project. This persists even if in the future you
no longer own the domain.
If you encounter challenges verifying your domain ownership, contact your
customer engineer (CE) or Google account team. After verifying that your
organization owns the specified domains, the CE or your Google account team
submit a domain-verification exemption request to unblock you.
Verify your domains
When you create a data store specifying the URL patterns for advanced website indexing, you must verify the domains in the data store. You
can verify any time and the advanced website indexing is activated only after
the domain verification.
To verify the domains specified in a data store with
advanced website indexing
using the
Google Cloud console, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data Stores
.
Click the name of the data store with websites for which you want to enable
advanced website indexing.
In the navigation menu, select
Data
.
From the
Website
tab, click
Verify
to verify all the domains in the
data store in the message prompting you to verify the domains.
Alternatively, click
Verify
in the
Status
column for the
URL pattern whose domain you want to verify. The
Verify
button is only
available after the indexing is complete.
In the
Domain verification
pane, expand the
Verify the
DOMAIN_NAME
domain
section.
Verify the domain in one of the following ways.
Verification using domain association:
In the
Initiate association request
section,
click
Send association request
.
A preview of the email containing the association request that'll be sent
to the domain owner is displayed.
Click
Send request
to send the email to the domain owner. A
confirmation of your request is emailed to you.
If the domain owner for a domain is not found in Google Search, you
must reach out to the domain owner yourself and use the domain ownership
verification method to verify the domain.
If you don't get a response to your request within a week, you can resend
the verification request.
If you're the owner of the domain, the domain is automatically
verified after you send the verification request.
When the domain owner approves the association request, you receive an
email confirming the approval.
Domain ownership verification:
Click
Verify in Search Console
.
The
Welcome to the Google Search console
page appears.
Follow the on-screen instructions in the Google Search console to
verify a domain or a URL prefix, depending on whether you are verifying an
entire domain or a URL prefix that is part of a domain. For more information,
see
Verify your site ownership
in the Search Console
Help Center.
When you have finished the domain verification workflow, the
Data
page
for your data store appears. The
Status
column indicates that
indexing is in progress for the website.
Repeat for every URL pattern in your data store that requires domain
verification.
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-04-12 UTC.

