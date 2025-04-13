# Connect a third-party data source  |  AI Applications  |  Google Cloud

Source: [https://cloud.google.com/generative-ai-app-builder/docs/connect-third-party-data-source](https://cloud.google.com/generative-ai-app-builder/docs/connect-third-party-data-source)

Home
AI Applications
Documentation
Guides
Send feedback
Connect a third-party data source
Stay organized with collections
Save and categorize content based on your preferences.
This page describes how to connect third-party data sources to
Vertex AI Search.
When you connect a third-party data source, Vertex AI Search
creates a
data connector
, and associates data stores (called
entity
data stores) with it for the entities that you specify. Entity
types are specific to the data source that you're connecting to. For example,
Jira Cloud entities include issues, attachments, comments, and worklogs.
Third-party data sources are available only for generic search apps.
Chat, recommendations, and agent apps can't use third-party data sources.
To import data from a Google data source instead, see
Create a search data
store
.
If you use customer-managed encryption keys, see
About single-region keys
for third-party connectors
in the Google Agentspace
documentation.
Before you begin
Contact your Google account team and ask to be added to the allowlist for
third-party data source connectors.
Go to the section for the source you plan to use:
Connect Adobe Experience Manager
Connect AODocs
(Additional allowlist)
Connect Asana
Connect Box
Connect Coda
Connect Confluence Cloud
Connect Confluence Data Center On-premises
Connect DocuSign
Connect Dropbox
Connect Entra ID
Connect GitHub
Connect GitLab
Connect Jira Cloud
Connect Jira Data Center On-premises
Connect Marketo
Connect Microsoft Outlook
(Additional allowlist)
Connect Microsoft Teams
(Additional allowlist)
Connect Monday
Connect Notion
(Additional allowlist)
Connect Okta
Connect OneDrive
Connect Salesforce
Connect ServiceNow
Connect SharePoint Data Center On-premises
Connect SharePoint Online
Connect Slack
Connect WordPress
Connect Zendesk
(Additional allowlist)
Connect Adobe Experience Manager
Use the following procedure to sync data from Adobe Experience Manager to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
In addition to the third-party connector allowlist, this connector requires
that your project is added to an additional allowlist. To be added to this
allowlist, contact your Vertex AI Search account team.
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
An Adobe Experience Manager administrator must generate or obtain the
following for integrating with Vertex AI Search:
Service credentials of your Adobe Experience Manager instance
Instance URL of your Adobe Experience Manager site
Create a Adobe Experience Manager connector
Console
To use the Google Cloud console to sync data from Adobe Experience Manager to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Adobe Experience Manager
to connect your third-party source.
Enter your Adobe Experience Manager authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your data store to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect AODocs
Use the following procedure to sync data from AODocs to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
In addition to the third-party connector allowlist, this connector requires
that your project is added to an additional allowlist. To be added to this
allowlist, contact your Vertex AI Search account team.
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
An AODocs administrator must generate or obtain the
following for integrating with Vertex AI Search:
Instance ID (Domain URL of your AODocs instance)
Client ID
Client secret
Create a AODocs connector
Console
To use the Google Cloud console to sync data from AODocs to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
AODocs
to connect your third-party source.
Enter your AODocs authentication information and click
Authenticate
. A
new window appears.
Authenticate your account and confirm that it
succeeded before returning to the
Specify the AODocs source for
your data store
page.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get search results
. If you used third-party access control, see
Preview results for apps with third-party access control
.
Connect Asana
Use the following procedure to sync data from Asana to Vertex AI Search.
After you set up your data source and import data the first time, the data store syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information about setting up access control, see
Use data source access control
.
An Asana administrator must generate or obtain the personal access token (PAT) following for authentication. For more information, see
Personal access token
in the Asana documentation.
To invite a member to an Asana workspace, do the following:
Sign in to
Asana
application with your administrator account.
Select the relevant project.
In the
Share visitors
dialog, under
Invite with email
:
Click
Invite
.
Enter the user's email address.
Choose the permission level as
Viewer
.
To generate a PAT, do the following:
Open the
Asana Developer Console
.
Click
My apps
.
Click
add
Create token
.
In the
Create new token
dialog, fill the required information.
Click
Create token
.
Copy the token for later use.
Click
Done
.
Create an Asana cloud connector
Console
To use the Google Cloud console to sync data from Asana to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, select
Data Stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Asana
to connect your third-party source.
Enter authentication details, including the generated PAT.
Select the entities to synchronize and click
Continue
.
Choose a region for the data store.
Provide a name for the data store.
Set a synchronization frequency for the data store.
Click
Create
. Vertex AI Search creates your data store and displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are set up, see
Get search results
. If you used third-party access control, see
Preview results for apps with third-party access control
.
Connect Box
Use the following procedure to sync data from Box to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
You must have administrator access to the Box instance with 2FA enabled. All
the set up instructions can only be performed from the administrator account.
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
Read
Setup with JWT
in the Box documentation for an overview of the setup with screenshots.
Create a Box app
Sign in to the
Box Developer Console
with your administrator account.
Click
Create platform app
.
Select
App type
as
Custom app
.
Enter the
App name
.
Set the following properties:
Purpose:
Integration
Categories:
AI
External system:
Google Cloud AI Applications
Select
Authentication method
as
Server authentication (with JWT)
.
Click
Create app
.
Configure the Box app
In the
Box Developer Console
, choose the
Platform app
and then go to the
Configuration
tab.
In the
App access level
section, select
App + Enterprise access
.
In the
Application scopes
section, select the following scopes:
Read all files and folders stored in Box
Write all files and folders stored in Box
Manage users
Manage groups
Manage enterprise properties
In the
Advanced features
section, select
Make API calls using the as-user header
.
In the
Add and manage public keys
section, click
Generate a public/private keypair
.
The
public key
is automatically uploaded to the console with an
ID. This ID is used when creating a connection.
You can download a configuration file with the private key and passphrase. Make sure to keep this file for later use.
Optionally, to generate your own key, see the
Box keypair setup guide
.
Click
Save changes
.
Authorize the Box app
In the
Box Developer Console
, choose the
Platform app
and then go to the
Authorization
tab.
Click
Review and submit
.
In the
Review app authorization submission
dialog, click
Submit
.
Sign in to the
Box admin platform apps manager
with your administrator account.
Choose the
Platform app
that you have configured.
Click the three dots (
...
) in the corresponding row.
Select
Authorize app
from the drop-down list.
In the
Authorize app
dialog, click
Authorize
to complete the
authorization process.
Have the following Box authentication information ready:
Enterprise ID
: Obtain it from the
General settings
tab.
Client ID
and
Client secret
: Obtain it from the
Configuration
tab under
OAuth 2.0 credentials
.
Private key
,
Key ID
, and
Passphrase
: These parameters were
already generated and downloaded to a local file from the
Configuration
tab under
Add and manage public keys
while
configuring the app.
Create a Box connector
Console
To use the Google Cloud console to sync data from Box to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data
store
.
On the
Select a data source
page, scroll or search for
Box
to connect
your third-party source.
Enter your authentication information.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency for your data store.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are
set up, see
Get search results
. If you used
third-party access control, see
Preview results for apps with third-party
access control
.
Connect Coda
Use the following procedure to sync data from Coda to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
A Coda administrator must generate or obtain the Coda API token to
integrate with Vertex AI Search.
Create a Coda connector
Console
To use the Google Cloud console to sync data from Coda to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Coda
to connect your third-party source.
Enter your Coda authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Confluence Cloud
Use the following procedure to sync data from Confluence Cloud to
Vertex AI Search.
After you set up your data source and import data the first time, you can choose how often the data store syncs with that source.
Before you begin
Before setting up your connection:
Verify that you have administrator access to the Confluence instance and project.
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
Set up authentication and permissions in Confluence
Make sure that you have the necessary authentication details and administrator access to your Confluence instance. Use the following instructions to create a client ID and client secret through the
Atlassian Developer Console
, configure the required OAuth 2.0 scopes, set up permissions for users, retrieve your instance URL and ID, configure roles, and authenticate to sync data between Confluence Cloud and Vertex AI Search. To enable OAuth 2.0 and obtain the client ID and secret, see
OAuth 2.0 (3LO) apps
in the Atlassian Developer documentation.
Make sure that you have the necessary authentication details and administrator access to your Confluence instance. Use the following instructions to create a client ID and client secret through the
Atlassian Developer Console
, configure the required OAuth 2.0 scopes, set up permissions for users, retrieve your instance URL and ID, configure roles, and authenticate to sync data between Confluence Cloud and Vertex AI Search. To enable OAuth 2.0 and obtain the client ID and secret, see
OAuth 2.0 (3LO) apps
in the Atlassian Developer documentation.
Create an OAuth 2.0 integration in the Atlassian Developer Console:
Sign in to
Atlassian Developer Console
.
Click the profile icon and select
Developer console
.
Figure 1.
Select Developer console
Click the profile icon and select
Developer console
.
Figure 1.
Select Developer console
Click
Create
and select
OAuth 2.0 Integration
.
Figure 2.
Select OAuth 2.0 Integration
Figure 2.
Select OAuth 2.0 Integration
Enter a name for the app and do the following:
Check the terms and conditions checkbox.
Click
Create
.
Figure 3.
Create a new OAuth 2.0 Integration
Figure 3.
Create a new OAuth 2.0 Integration
Click
Authorization
.
In the
Authorization type
table, select
Add
for
OAuth 2.0 (3LO)
.
Figure 4.
Add authorization type
Figure 4.
Add authorization type
In the
Callback URL
field, enter
https://vertexaisearch.cloud.google.com/console/oauth/confluence_oauth.html
.
Click
Save changes
.
Figure 5.
Save changes
If you see the warning:
Your app doesn't have any APIs. Add APIs to your app
,
proceed to step 2 under the next section and complete all the remaining steps.
Otherwise, skip ahead to step 4 in that same section.
To configure OAuth 2.0 and retrieve the required credentials for your
Confluence connector setup, do the following:
Enable OAuth 2.0:
Click
Permissions
.
Figure 6.
Select permissions
Figure 6.
Select permissions
Go to
Confluence API
.
Click
Add
.
Click
Configure
.
Go to the
Granular scopes
tab and click
Edit scopes
.
Figure 7.
Edit scopes
Figure 7.
Edit scopes
Select the following scopes.
View Scopes
read:attachment:confluence
read:configuration:confluence
read:content.metadata:confluence
read:content-details:confluence
read:group:confluence
read:space:confluence
read:user:confluence
Confirm that seven scopes are selected and save your changes.
Obtain the client ID and client secret:
Click
Distribution
.
Select
Edit
.
Figure 8.
Edit distribution
Figure 8.
Edit distribution
Select
Sharing
to enable editing other fields.
Fill out the remaining fields. Make sure to set
Vendor
to
Google
and
Privacy policy
to
policies.google.com
.
Select
Yes
when you see `Does your app store personal data?.
Select
Settings
to copy your
Client ID
and
Client secret
.
Figure 9.
Copy your client ID and client secret
Figure 9.
Copy your client ID and client secret
Obtain the instance URL:
Go to
atlassian.net
and sign in with your
administrator account.
Go to
atlassian.net
and sign in with your
administrator account.
Select the app you want to sync. For example, sync the first app.
Find the instance URL. It appears as the subdomain in the address bar.
Obtain the instance ID:
Open a new tab, copy the instance URL, and append
/_edge/tenant_info
to the instance URL. For example,
https://<var>YOUR-INSTANCE</var>.atlassian.net/_edge/tenant_info
.
Open a new tab, copy the instance URL, and append
/_edge/tenant_info
to the instance URL. For example,
https://<var>YOUR-INSTANCE</var>.atlassian.net/_edge/tenant_info
.
Navigate to the link to find the
cloudId
value. The
cloudId
is your instance ID.
Figure 10.
Obtain instance ID
Figure 10.
Obtain instance ID
Set up permissions and roles
To set the user visibility, do the following:
Click the user profile icon and go to
Manage account
.
Figure 11.
Manage account
Navigate to the
Profile and visibility
.
Figure 12.
Profile and visibility
Go to
Contact
and set the
Who can see this
as
Anyone
.
Figure 13.
Contact
To grant Confluence administrator with Discovery Engine Editor role in the
Google Cloud console, do the following:
In the Google Cloud console, go to the
AI Applications
page.
Navigate to
IAM
.
Locate the
Confluence administrator
account.
Grant the Discovery Engine Editor role to the administrator.
To grant a user with an administrator role in Atlassian, do the following:
Sign in to
Atlassian
using an administrator account.
Click the menu icon and select your organization.
Alternatively, you can go to
admin.atlassian.com
.
On the
Admin
page, click the product and select the
Manage users
button.
Figure 14.
Manage users
Click
Groups
under
User management
.
On the
Groups
page:
Click
Create group
.
Enter a name for the group.
Figure 15.
Create group
This group receives permissions required by the connector. Users added to this
group inherit these permissions.The connector uses this group to authenticate
and fetch documents.
On the
group page
, click
Add product
.
Select
User access admin
as the product role.
Click
Add
.
Figure 16.
Confluence user access administrator
Click
Add group members
to add the user account or group members the connector authenticates as.
Figure 17.
Add group members
Create a Confluence Cloud connector
Console
To use the Google Cloud console to sync data from Confluence Cloud to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Confluence
to connect your third-party source.
Enter your authentication information and click
Authenticate
.
Figure 18.
Authentication details
Figure 18.
Authentication details
A new window appears. Enter the instance username and password.
Check that the authentication succeeded before returning to the
Specify
the Confluence source for your data store
page.
Select which entities to sync and click
Continue
.
Select a region for your data connector.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data Stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
See
Preview results for apps with third-party access control
.
Connect Confluence Data Center On-premises
Use this procedure to create a Confluence Data Center data store and search app in
AI Applications
, syncing on-premises Confluence data with Vertex AI Search.
After you set up your data source and import data the first time, you can choose how often the data store syncs with that source.
Before you begin
Before setting up your connection, make sure that you have the following:
Service attachment (required for private destination type only)
: Configure a service attachment for secure data transfer.
Username and password
: Obtain valid credentials for authentication from your Confluence administrator.
Optional for private destination type:
Domain URL
: Specify the URL of the Confluence Data Center instance.
Optional:
Base domain name
: Provide the base domain name for the Confluence instance.
Optional:
Destination port
: Identify the port used for communication with the Confluence Data Center.
Use the following configuration guidelines to establish connections with Private Service Connect(PSC). Adjust or add resources as needed. Make sure the PSC service attachment is properly configured to connect to the private instance and meets the requirements for a published service.
Configure network settings:
Place the PSC service attachment and load balancer in different subnets within the same Virtual Private Cloud network.
The backend system must remain closed to the public network for security reasons. However, ensure it can accept traffic from the following sources:
For proxy-based/HTTP(s) load balancers (L4 proxy ILB, L7 ILB), configure the backend to accept requests from the proxy subnet in the Virtual Private Cloud network.
For more information, see the
Proxy-only subnets for Envoy-based load balancers
documentation.
Adjust firewall rules:
Ingress rules:
Allow traffic from the PSC service attachment subnet to the internal load balancer (ILB) subnet.
Make sure that the ILB can send traffic to the backend.
Permit health check probes to reach the backend.
Egress rules: Enable egress traffic by default, unless specific deny rules apply.
Additional considerations: Make sure to keep all the components, including the PSC service attachment and load balancer, in the same region.
Generate a service attachment
Use the following steps to generate a service attachment:
Decide endpoint type
: Select
Public
or
Private
endpoint.
For
Public
endpoint: If the Confluence Data Center
Destination type
is
Public
, you are not required to create the setup for service attachment. Instead, you can use your public URL in the
Domain URL
field of the Google Cloud console when creating your connector.
For
Private
endpoint:
Use
private service connect (PSC)
to enable connections from private instances to Google Cloud.
Create a Virtual Private Cloud network and required subnets.
Create a virtual machine (VM) instance and install the backend service.
Optional: Set up a
health check
probe to monitor backend health.
Add a load balancer to route traffic to the VM or backend.
Define firewall rules to allow traffic between the PSC endpoint and the backend.
Publish the endpoint
by creating a PSC service attachment.
Create a Confluence Data Center user and set up permissions
To enable Vertex AI Search to obtain data from Confluence, you need to create a new user with the minimum permissions necessary. Follow these steps to create the user and set up the required permissions.
Sign in as an administrator:
Go to your Atlassian domain site and open the Confluence Data Center instance.
Enter the admin username and password.
Click
Log In
.
Create a new user:
When creating a data store, you must create a user to obtain data from the third-party instance.
Click the settings icon.
Select
User management
.
Enter the administrator credentials, if prompted.
In the
Administration
page, click
Create user
.
Enter the email address, full name, username, and password.
Click
Create user
.
Assign user to a group:
In the
Confluence administration
page, navigate to the Users and security tab and click
Groups
.
Click
Add group
. Enter a name for the group and create it.
In the
Find group
field, enter the group name to find the group.
Click the settings icon.
Select the profile account and navigate to
User management
.
In the
Users
page, under
List users
, search for the newly created user in the
Find user
field.
Click the user to open the
View users
page.
Click
Edit groups
to open the
Edit user group
page.
Select the checkbox for the created user group.
Click
Save
to assign the user to the newly created group.
The added user is assigned in the
Group members
section.
Configure user permissions:
In the
Confluence administration
page, navigate to the
Issues
tab.
Locate
Permissions
.
Select
View global permissions
.
Select
Edit permissions
.
In the
Edit global permissions
page, search for the group assigned to the user, and enable the
can use
option.
Configure the documentation space
Click the
Confluence
icon to navigate to the
Dashboard
page.
Click
Create space
.
Select
Documentation space
and click
Next
.
Enter all the necessary details and click
Create
to create the documentation space.
Under
My spaces
, click the newly created space.
Navigate to
Pages
, and open the menu (three dots).
Select
Restrictions
.
From the
Restrictions
drop-down menu, select the
Viewing and editing restricted
option.
Search for the group and assign the
can view
permission.
Click
Apply
.
The user is created with minimum access and permissions are set for spaces. You can also assign permissions to the blogs.
Create a Confluence Data Center On-premises connector
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Confluence data center
to connect your third-party source.
Enter your authentication information and click
Continue
.
From the
Destination type
drop-down list, select
Public
or
Private
.
For
Public
destination type, you are not required to create the setup for service attachment. Instead, you can use your public URL in the Domain URL field of the Google Cloud console.
For
Private
destination type, enter all the required information:
If your instance has a domain URL:
Service attachment
: Enter your service attachment.
Optional:
Base domain name
: Enter your base domain.
Domain URL
: Enter your domain URL.
Optional:
Destination port
: Enter your destination port.
If your instance does not have a domain URL:
Service attachment
: Enter your service attachment.
Optional:
Destination port
: Enter your destination port.
Click
Continue
.
Optional:
Advanced options
: Select and enable
Proxy settings
and
SSL settings
, if required.
Under the
Entities to sync
, select all the required entities to sync and click
Continue
.
Select a region for your data connector and enter a name for your data connector.
Select a synchronization frequency.
For
Private
destination type, after you submit the details for the connector, VAIS sends a connection request to your PSC. Navigate to your connector to see a message to allowlist a
projectId
in the PSC. The connector remains in the
Error
state until you allow the connection in PSC. When you accept the connection request, the connector moves to the
Active
state during the next sync run. If you configure your PSC to accept all connections, the connector automatically moves to the
Active
state after creation.
For
Public
destination type, the connector automatically enters the
Active
state after submission.
To verify the state of the data store and the ingestion activity, do the following:
Navigate to the connector in the data store list and monitor its state until it changes to
Active
.
After the connector state changes to
Active
, click the required entity and confirm that all selected entities are ingested.
The data store state transitions from
Creating
to
Running
when synchronization begins and changes to
Active
once ingestion completes, indicating that the data store is set up. Depending on the size of your data, ingestion can take several hours.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
See
Preview results for apps with third-party access control
.
Connect DocuSign
Use the following procedure to sync data from DocuSign to Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up a connection for the DocuSign connector, make sure that you have
the following credentials for authentication:
Consumer key
Private key
Username
Generate keys and user credentials
Create a user in the DocuSign instance, assign the user to a group, and grant
the required permissions to generate the consumer key, private key, and username
needed for integration and authentication.
Register a DocuSign user: If you are a new user, use the following steps to
create a DocuSign developer account. If you are an existing user, go to the
access account details section.
Go to the
DocuSign developer account
.
Expand the
Developer account
drop-down and click
Create account
.
On the
Get your free developer account
page, enter the required information:
First name
Last name
Email
Company
Country
DocuSign account status
(if applicable)
Click
Get started
.
A
Check your email
window appears. Check your email for a verification
code, enter it, and click
Next
.
The
Verify your mobile number
window appears. Select the country code,
enter your mobile number, and click
Send code
.
Enter the temporary code received and click
Verify
.
On the
Set your password
window, enter your password and click
Next
.
The user is logged into the
Sandbox environment
.
Access account details:
Click the
User profile
icon and select
My apps & keys
.
The
Account
dashboard and
Apps and keys
page is displayed, showing
the
User ID
,
Account ID
, and
App base URL
.
Generate apps and integration keys:
Click
Add app and integration key
.
In the
Add integration key
dialog, enter the app name and click
Create app
.
The user is redirected to the app page. In the Authentication section,
select
Yes
for the question "Is your application able to securely
store a client secret?" and click
Add secret key
. A secret key is added.
In the
Service integration
section, click
Generate RSA
.
The
RSA key pair
dialog displays the keypair ID, public key, and
private key. Copy both, as they are not displayed again.
Add user to production:
Sign in to the
DocuSign production instance
.
Click
Admin
.
Navigate to
Users and groups
>
Users
.
On the
Seats & users
page, under
Seat usage
, click
Assign a seat
.
In the
Add user
page, enter the email address.
Click
Next
.
Complete the mandatory fields in the
Profile information
section.
Click
Next
.
In the
Security
section, add the
Access code
.
Click
Next
.
In the
Permission profile and groups
section, select the permission
as
Viewer
.
Click
Add user
.
The
Seats and users
page is displayed, and the user appears under
All users
.
Open the user email account and activate the account using the
Account activation
email.
Click
Activate
, enter the
Access code
, and activate the account.
Generate RSA keypair:
Navigate to
Admin
>
Integrations
>
Apps and keys
.
On the
Apps and keys
page, click
Actions
and choose
Edit
for
an existing app name from the
Apps and integration keys
section.
On the
App details
page, go to the
Service integration
section
and click
Generate RSA
.
The
RSA keypair
dialog displays the keypair ID, public key, and
private key. Copy all the details and click
Close
.
Click the
Profile
icon and sign out.
Sign in to production instance: Sign in to the
DocuSign production instance
using minimum access user credentials. The
Admin
menu option is not
displayed for the minimum access user account.
Create a DocuSign cloud connector
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
Create data store
.
On the
Select a data source
page, scroll or search for
DocuSign
to
connect your third-party source.
Enter your authentication information.
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency for your data store.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page.
The
Connector state
changes from
Creating
to
Running
when it
starts synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up,
see
Get search results
. If you used third-party
access control, see
Preview results for apps with third-party access control
.
Connect Dropbox
Use the following procedure to sync data from Dropbox to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For more information,
see
Use data source access control
.
Have the following Dropbox authentication information ready. For information
about setting up these parameters, see the
OAuth Guide
in the Dropbox documentation.
Client ID
Client secret
Create a Dropbox connector
Console
To use the Google Cloud console to sync data from Dropbox to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data Stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Dropbox
to connect your third-party source.
Enter your Dropbox authentication information and click
Authenticate
. A new window appears.
Authenticate your account and confirm that it
succeeded before returning to the
Specify the Dropbox source for
your data store
page.
Select which entities to sync and click
Continue
.
Select a location for your data store.
Enter a name for your data store.
Select a synchronization frequency for your data store.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization. Check the
Documents
tab to
make sure your entities have been ingested correctly.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are set up, see
Get search results
. If you used third-party access control, see
Preview results for apps with third-party access control
.
Connect Entra ID
Use the following procedure to sync data from Entra ID to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
To obtain the client ID and client secret, do the following:
Create an Entra ID application:
Sign in to
Microsoft Entra administrator center
and click
Application
.
In the
Application
drop-down list, click
App registrations
.
In the
App registrations
page, click
New registration
.
Click
Add new registration
and do the following:
Enter a name for the application.
Under
Supported account types
, select
Accounts in the
organizational directory only
.
Under
Redirect URI
, add a web redirect URI pointing
to:
https://login.microsoftonline.com/common/oauth2/nativeclient
.
Click
Register
.
Save credentials:
On your registered application window, save the following values
for later use:
Use the
Application (client) ID
to set the
Client ID
parameter.
Use the
Directory (tenant) ID
to set the
Azure Tenant
parameter.
Create client secret:
Navigate to
Certificates & secrets
and create a new client secret:
Click
New client secret
and specify the required duration.
Save the client secret and copy the
key value
for later use.
Configure Entra ID API permissions
On your registered application window, click
API permissions
.
Under
Configured permissions
, select
Microsoft Graph
and configure
the following permission:
View permissions
User.Read.All (Application)
If you want to ingest
profileCardAttributes
, then configure the following
permissions:
View permissions
People.Read.All (Application)
PeopleSettings.Read.All (Application)
Grant
admin consent
for all the added permissions. An administrator's consent
is required to use client credentials in the authentication flow.
Create a Entra ID connector
Console
To use the Google Cloud console to sync data from Entra ID to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Entra ID
to connect your third-party source.
Under
Authentication settings
, enter the client ID and client secret.
Skip the
Destinations
option and click
Continue
.
Under
Advanced options
, enter the Azure tenant ID.
Select
Enable realtime sync for all entities
if you want the data updated
in near real-time.
Enter a string value in the
Client state
field.
The client state is used to authenticate change notifications.
For webhook authentication on the third-party app, the credentials passed
during connector creation are re-used.
Click
Continue
.
Under
Entities to sync
, select
User profiles
.
Click
Continue
.
In
Configure your data connector
, select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
When the connector state changes to
Active
, navigate to the
Entity
tab.
Click
userprofiles
entity.
Check the number of ingested documents and ensure it matches the number of
users in Entra ID.
If the Entra ID app has the required permissions to ingest custom attributes,
it ingests up to
15 profile card attributes
per record. By default, the custom attributes are not searchable.
To make the custom attributes searchable, do the following:
In the
userprofiles
page, navigate to the
Schema
tab.
Click
Edit
.
Deselect the attributes, such as
address
, from being
retrievable,
searchable, and indexable
, then click
Save
.
The
Edit
button remains inactive for a few minutes before reactivating.
When the
Edit
button is in
Active
state, click
Edit
.
Select the
retrievable, searchable, and indexable
boxes for the required
custom attributes.
Enable search.
Click
Save
.
Test the search engine
After configuring your search engine, test its capabilities. This ensures it returns accurate results based on user access.
Enable web app:
Go to the app integration configurations and toggle to
Enable the web app
.
Test web app:
Click
Open
next to the web app link and sign in as a user.
Verify that search results are restricted to items accessible by the user.
Preview people search results
In the search app, navigate to
Preview
and start searching within the
console when using Google IdP.
Alternatively, navigate to the provided link and sign in with your IdP to
start searching.
The search results appear as
people cards
, displaying user details such
as
Name, Job title, Email, and Profile picture
.
Click a
people card
to view a detailed profile page, which includes
the following:
Name
Profile picture
Job title
Department
Management chain
Direct reports
If custom attributes (profile card properties) are
ingested and made indexable, searchable, and retrievable
:
Searching by a custom attribute value returns only person profiles
containing those attributes.
Custom attributes appear in search results, but can only be accessed
through the
API
, not the
Vertex Search user interface
.
Configure the workforce pool for non-Google IdP without SSO
If your employees use a non-Google IdP, lack SSO with Google,
or are not Google Workspace customers, set up a workforce pool as described
in
Use data source access control
to enable the employee search.
The workforce pool lets you to manage and authenticate users from external
identity providers, such as Azure or Okta, within Google Cloud console.
To configure your workforce pool and enable the web app for seamless user
access, do the following:
Create workforce pool at the organization level in Google Cloud by following the appropriate setup manual:
Azure OIDC setup
Azure SAML setup
Okta & OIDC setup
Okta & SAML setup
Configure the workforce pool in
AI Applications
>
Settings
for the region where you create your app.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
See
Preview results for apps with third-party access control
.
Connect GitHub
Use the following procedure to sync data from GitHub to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
A GitHub administrator must obtain the GitHub instance personal access token to integrate with
Vertex AI Search.
Create a GitHub connector
Console
To use the Google Cloud console to sync data from GitHub to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
GitHub
to connect your third-party source.
Enter your GitHub authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect GitLab
Use the following procedure to sync data from GitLab to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
A GitLab administrator must obtain the GitLab instance personal access
token to integrate with Vertex AI Search.
Create a GitLab connector
Console
To use the Google Cloud console to sync data from GitLab to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
GitLab
to connect your third-party source.
Enter your GitLab authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Jira Cloud
Use the following procedure to sync data from Jira Cloud to
Vertex AI Search.
After you set up your data source and import data the first time, you can choose how often the data store syncs with that source.
Before you begin
Before setting up your connection:
Set up access control. Ensure that access control is properly configured for your data source. This step ensures that only authorized users can access and manage the data. For more information, see
Use data source access control
documentation.
For user permissions to apply correctly, Jira Cloud users must provide sharing consent.
Make sure that you have an Atlassian account, Jira instance, and project.
Verify that you have administrator access to the Jira instance, and project.
Set up authentication and permissions in Jira
Using the instructions in the following sections, ensure you have the necessary authentication details and administrator access to your Jira instance. Create a client ID and client secret through the Atlassian Developer Console, configure the required OAuth 2.0 scopes, set up permissions for users, retrieve your instance URL and ID, configure roles, and authenticate to sync data between Jira Cloud and Vertex AI Search.
Create client ID and client secret
Create an OAuth 2.0 integration in the Atlassian Developer Console:
Sign in to the
Atlassian Developer Console
.
Click the profile icon and select
Developer console
.
Figure 1.
Select Developer console
Click the profile icon and select
Developer console
.
Figure 1.
Select Developer console
Click
Create
and select
OAuth 2.0 Integration
.
Figure 2.
Select OAuth 2.0 Integration
Figure 2.
Select OAuth 2.0 Integration
Enter a name for the app and do the following:
Check the terms and conditions checkbox.
Click
Create
.
Figure 3.
Create a new OAuth 2.0 Integration
Figure 3.
Create a new OAuth 2.0 Integration
Click
Authorization
.
In the
Authorization type
table, select
Add
for
OAuth 2.0 (3LO)
.
Figure 4.
Add authorization type
Figure 4.
Add authorization type
In the
Callback URL
field, enter
https://vertexaisearch.cloud.google.com/console/oauth/jira_oauth.html
.
Click
Save changes
.
Figure 5.
Save changes
If you see the warning:
Your app doesn't have any APIs. Add APIs to your app
,
proceed to step 2 under the next section and complete all the remaining steps.
Otherwise, skip ahead to step 4 in that same section.
Enable OAuth 2.0:
Click
Permissions
.
Figure 6.
Select permissions
Click
Permissions
.
Figure 6.
Select permissions
Go to
Jira API
.
Click
Add
.
Click
Configure
.
Go to the
Classic scopes
tab and click
Edit scopes
.
Figure 7.
Edit Classic scopes
Select the following scopes:
Go to
Jira API
.
Click
Add
.
Click
Configure
.
Go to the
Classic scopes
tab and click
Edit scopes
.
Figure 7.
Edit Classic scopes
Select the following scopes:
View Scopes
read:avatar:jira
read:audit-log:jira
read:group:jira
read:issue-security-level:jira
read:issue-security-scheme:jira
read:jira-user
read:jira-work
read:user:jira
Confirm that eight scopes are selected, then save your changes.
Go to the
Granular scopes
tab and click
Edit scopes
.
Figure 8.
Edit Granular scopes
Select the following scopes:
View Scopes
read:issue-security-level:jira
read:issue-security-scheme:jira
read:group:jira
read:user:jira
read:avatar:jira
read:audit-log:jira
Confirm that six scopes are selected, then save your changes.
Go to the
Granular scopes
tab and click
Edit scopes
.
Figure 8.
Edit Granular scopes
Select the following scopes:
View Scopes
read:issue-security-level:jira
read:issue-security-scheme:jira
read:group:jira
read:user:jira
read:avatar:jira
read:audit-log:jira
Confirm that six scopes are selected, then save your changes.
Obtain the client ID and client secret:
Click
Distribution
.
Select
Edit
, and do the following:
Figure 9.
Edit distribution
Figure 9.
Edit distribution
Select
Sharing
to enable editing other fields.
Fill out the remaining fields. Make sure to set
Vendor
to
Google
and
Privacy policy
to
policies.google.com
.
Fill out the remaining fields. Make sure to set
Vendor
to
Google
and
Privacy policy
to
policies.google.com
.
Select
Yes
when you see
Does your app store personal data?
Select
Settings
to copy your
Client ID
and
Client secret
.
Figure 10.
Copy your client ID and client secret
Select
Settings
to copy your
Client ID
and
Client secret
.
Figure 10.
Copy your client ID and client secret
Obtain the instance URL:
Go to
atlassian.net
and sign in with your administrator account.
Select the app you want to sync. For example, sync the first app.
Find the instance URL, which is the subdomain in the address bar.
Obtain the instance ID:
Open a new tab, copy the instance URL, and append
/_edge/tenant_info
to the instance URL. For example,
https://<var>YOUR-INSTANCE</var>.atlassian.net/_edge/tenant_info
.
Open a new tab, copy the instance URL, and append
/_edge/tenant_info
to the instance URL. For example,
https://<var>YOUR-INSTANCE</var>.atlassian.net/_edge/tenant_info
.
Navigate to the link to find the
cloudId
value. The
cloudId
is your instance ID.
Figure 11.
Obtain instance ID
Figure 11.
Obtain instance ID
Set up permissions and roles
To set the user visibility, do the following:
Click the user profile icon and go to
Manage account
.
Figure 12.
Manage account
Navigate to the
Profile and visibility
.
Figure 13.
Profile and visibility
Go to
Contact
and set the
Who can see this
as
Anyone
.
Figure 14.
Contact
To grant Jira administrator with Discovery Engine Editor role in the
Google Cloud console, do the following:
In the Google Cloud console, go to the
AI Applications
page.
Navigate to
IAM
.
Locate the
Jira administrator
account.
Grant the Discovery Engine Editor role to the administrator.
To grant a user with an administrator role in Atlassian, do the following:
Sign in to
Atlassian
using an administrator account.
Click the menu icon and select your organization.
Alternatively, you can go to
admin.atlassian.com
.
On the
Admin
page, click the product and select the
Manage users
button.
Figure 15.
Manage users
Click
Groups
under
User management
.
On the
Groups
page:
Click
Create group
.
Enter a name for the group.
Figure 16.
Create group
This group receives permissions required by the connector. Users added to this
group inherit these permissions.The connector uses this group to authenticate
and fetch documents.
On the
group page
, click
Add product
.
Select
User access admin
as the product role.
Figure 17.
Jira user access administrator
Select
Product admin
as the product roles.
Click
Add
.
Click
Add group members
to add a user account or group members that the
connector authenticates as.
Figure 18.
Add group members
Create a Jira Cloud connector
Console
To use the Google Cloud console to sync data from Jira Cloud to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data Stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Jira Cloud
to connect your third-party source.
Enter your authentication information and click
Authenticate
.
Figure 19.
Authentication details
Figure 19.
Authentication details
Enter the instance username and password.
Verify that the authentication succeeded before returning to the
Specify the Jira source for your data store
page.
Select which entities to sync, then click
Continue
.
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data Stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
See
Preview results for apps with third-party access
control
.
Connect Jira Data Center On-premises
Use this procedure to create a Jira Data Center data store and search app in
AI Applications
, syncing on-premises Jira data with Vertex AI Search.
After you set up your data source and import data the first time, you can choose how often the data store syncs with that source.
Before you begin
Before setting up your connection, make sure that you have the following:
Service attachment (Required for private destination type only)
: Configure a service attachment for secure data transfer.
Username and password
: Obtain valid credentials for authentication from your Jira administrator.
Optional for private destination type:
Domain URL
: Specify the URL of the Jira Data Center instance.
Optional:
Base domain name
: Provide the base domain name for the Jira instance.
Optional:
Destination port
: Identify the port used for communication with the Jira Data Center.
Use the following configuration guidelines to establish connections with Private Service Connect(PSC). Adjust or add resources as needed. Make sure the PSC service attachment is properly configured to connect to the private instance and meets the requirements for a published service.
Configure network settings:
Place the PSC service attachment and load balancer in different subnets within the same Virtual Private Cloud network.
The backend system must remain closed to the public network for security reasons. However, ensure it can accept traffic from the following sources:
For proxy-based/HTTP(s) load balancers (L4 proxy ILB, L7 ILB), configure the backend to accept requests from the proxy subnet in the Virtual Private Cloud network.
For more information, see the
Proxy-only subnets for Envoy-based load balancers
documentation.
Adjust firewall rules:
Ingress rules:
Allow traffic from the PSC service attachment subnet to the internal load balancer (ILB) subnet.
Make sure that the ILB can send traffic to the backend.
Permit health check probes to reach the backend.
Egress rules: Enable egress traffic by default, unless specific deny rules apply.
Additional considerations: Make sure to keep all the components, including the PSC service attachment and load balancer, in the same region.
Generate a service attachment
Use the following steps to generate a service attachment:
Decide endpoint type
: Select
Public
or
Private
endpoint.
For
Public
endpoint: If the Jira Data Center
Destination type
is
Public
, you are not required to create the setup for service attachment. Instead, you can use your public URL in the
Domain URL
field of the Google Cloud console.
For
Private
endpoint:
Use
PSC
to enable connections from private instances to Google Cloud.
Create a Virtual Private Cloud network and required subnets.
Create a virtual machine (VM) instance and install the backend service.
Optional: Set up a
health check
probe to monitor backend health.
Add a load balancer to route traffic to the VM or backend.
Define firewall rules to allow traffic between the PSC endpoint and the backend.
Publish the endpoint
by creating a PSC service attachment.
Create a Jira Data Center user and set up permissions
To enable Vertex AI Search to obtain data from Jira, you need to create a new user with the minimum permissions necessary. Follow these steps to create the user and set up the required permissions.
Sign in as an administrator:
Go to your Atlassian domain site and open Jira Data Center instance.
Enter the administrator username and password.
Click
Log In
.
Create a new user:
When creating a data store, you must create a user to obtain data from the third-party instance.
Click the settings icon.
Select
User management
.
Enter the administrator credentials, if prompted.
In the
Administration
page, click
Create user
.
Enter the email address, full name, username, and password.
Click
Create user
.
Assign user to a group:
In the
Administration
page, under
User management
, click
Groups
.
Create a group by entering a name and clicking
Add group
.
Select the newly created group.
Click
Add/Remove users
.
Click the member icon located next to the
Add members to selected groups
box.
Select the newly created user and click
Save the selection
.
Click
Add selected user
to see new users in the group members section.
You can see the added user is assigned in the
Group members
section.
Configure user permissions:
In the
Administration
page, navigate to the
Issues
tab.
Select
Permission schemes
.
Click
Add permission scheme
.
Enter a name for the scheme and click
Add
.
Select the scheme and click the
Permission
icon.
Click
Grant permission
.
Add the following permissions, assign these permissions to the group created earlier, and click
Grant
:
Browse projects.
Browse projects archive.
Add this scheme to projects where users in the group need access to view the project, issues, comments, worklogs, and attachments.
You can add this scheme to the projects where the users in that group need access to view that project and issues, comments, worklogs, and attachments in that project.
Configure application access
In the
Administration
page, navigate to the
Applications
tab.
Under the
Applications
tab, select
Application access
.
Search for the created group and select it.
Verify that the group appears in the access list.
The user is created with minimum access. This schema is added to the projects. The Jira administrator can add more members to that group or add users to that project.
Create a Jira Data Center On-premises connector
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Jira data center
to connect your third-party source.
Enter your authentication information and click
Continue
.
From the
Destination type
drop-down list, select
Public
or
Private
.
For
Public
destination type, you are not required to create the setup for service attachment. Instead, you can use your public URL in the Domain URL field of the Google Cloud console.
For
Private
destination type, enter all the required information:
If your instance has a domain URL:
Service attachment
: Enter your service attachment.
Optional:
Base domain name
: Enter your base domain.
Domain URL
: Enter your domain URL.
Optional:
Destination port
: Enter your destination port.
If your instance does not have a domain URL:
Service attachment
: Enter your service attachment.
Optional:
Destination port
: Enter your destination port.
Click
Continue
.
Optional:
Advanced options
: Select and enable
Proxy settings
and
SSL settings
, if required.
Under the
Entities to sync
, select all the required entities to sync and click
Continue
.
Select a region for your data connector and enter a name for your data connector.
Select a synchronization frequency.
For
Private
destination type, after you submit the details for the connector, VAIS sends a connection request to your PSC. Navigate to your connector to see a message to allowlist a
projectId
in the PSC. The connector remains in the
Error
state until you allow the connection in PSC. When you accept the connection request, the connector moves to the
Active
state during the next sync run. If you configure your PSC to accept all connections, the connector automatically moves to the
Active
state after creation.
For
Public
destination type, the connector automatically enters the
Active
state after submission.
To verify the state of the data store and the ingestion activity, do the following:
Navigate to the connector in the data store list and monitor its state until it changes to
Active
.
After the connector state changes to
Active
, click the required entity and confirm that all selected entities are ingested.
The data store state transitions from
Creating
to
Running
when synchronization begins and changes to
Active
once ingestion completes, indicating that the data store is set up. Depending on the size of your data, ingestion can take several hours.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Marketo Cloud
Use the following procedure to sync data from Marketo Cloud to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up the connection, make sure that you have the authentication
credentials, including a client ID and client secret.
Generate authentication credentials
Create a Marketo administrator user:
Sign in to
Marketo
with the administrator
user instance.
From the
Home
tab, click
Admin
.
Navigate to
Security
>
Users & roles
and click
Go to admin console
.
In the Adobe console, under
Quick links
, click
Add users
.
In the
Add users to your team
dialog:
Enter your email address.
Select the product subscription as
Marketo Engage – googledevsandbox
.
Click
Save
.
Return to
Marketo admin
>
Security
>
Users & roles
and locate the newly created user.
Select the user and click
Edit
.
Remove the
Standard user
role and assign the
Admin
role.
Click
Save
.
Create a Marketo client ID and secret key:
Go to the
Marketo auth services
instance.
Enter the administrator credentials and then click
Continue
.
Click
Admin
.
In the Admin dashboard, go to
Security
>
Users & roles
.
Click
Create API only user
.
In the
Create new API only user
window, do the following:
Fill in the required fields:
Email
First name
Last name
Select the required roles, and click
Create API only user
.
Click
Admin
and then navigate to
Integration
>
LaunchPoint
.
Click
New
>
New services
.
In the
New services
window, do the following:
Enter a
Display name
for identification.
In the
Service
field, select
Custom
.
Enter a description.
In the
API only user
field, select the previously created
API user.
Click
Create
. The API user appears in the
Installed services
page.
In the
Installed services
page, navigate to the API user row.
Under the
Details
column, click
View details
to retrieve the
Client ID
and
Secret key
.
Create a Marketo Cloud connector
Console
To use the Google Cloud console to sync data from Marketo to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Marketo
to connect your third-party source.
Enter your authentication information.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Microsoft Outlook
Use the following procedure to sync data from Microsoft Outlook to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
A Microsoft Outlook administrator must generate or obtain the
following for integrating with Vertex AI Search:
Client ID
Client secret
Tenant ID
Configure the following scopes:
View scopes
Calendars.Read
Calendars.ReadBasic.All
Contacts.Read
Mail.Read
Mail.ReadBasic
Mail.ReadBasic.All
User.Read.All
User.ReadBasic.All
Create a Microsoft Outlook connector
Console
To use the Google Cloud console to sync data from Microsoft Outlook to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Microsoft Outlook
to connect your third-party source.
Enter your Microsoft Outlook authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Microsoft Teams
Use the following procedure to sync data from Microsoft Teams to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
A Microsoft Teams administrator must generate or obtain the
following for integrating with Vertex AI Search:
Client ID
Client secret
Tenant ID
Configure the following Microsoft Graph (Application) permissions with the
consent of a Microsoft Teams administrator:
View scopes
TeamSettings.Read.All
GroupMember.Read.All
User.Read.All
Directory.Read.All
ChannelSettings.Read.All
Chat.ReadBasic.All
ChannelMessage.Read.All
Chat.Read.All
Files.Read.All
ChannelMember.Read.All
Create a Microsoft Teams connector
Console
To use the Google Cloud console to sync data from Microsoft Teams to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Microsoft Teams
to connect your third-party source.
Enter your Microsoft Teams authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get search results
. If you used third-party access control, see
Preview results for apps with third-party access control
.
Connect Monday
Use the following procedure to sync data from Monday to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection, make sure that you have the domain URL,
administrator access, and API token.
To generate the account URL and API token, do the following:
Sign in to the
Monday
application with your
administrator account.
Click the
Profile
icon.
Select
Administration
.
Navigate to the
General
tab and enter the
Account name
and
Account URL
.
Return to the
Profile
icon and select
Developers
.
On the
Monday developer center
page, click
My access tokens
.
Click
Show
to display the token.
Copy the token for use in authentication.
Create a Monday connector
Console
To use the Google Cloud console to sync data from Monday to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
On the
Data stores
page, click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Monday
to connect your third-party source.
Enter your Monday authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Notion
Use the following procedure to sync data from Notion to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connector:
In addition to the third-party connector allowlist, this connector requires
that your project is added to an additional allowlist. To be added to this
allowlist, contact your Vertex AI Search account team.
A Notion administrator must generate or obtain the following for integrating
with Vertex AI Search:
API token of the Notion instance
Workspace ID
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
Create a Notion connector
Console
To use the Google Cloud console to sync data from Notion to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Notion
to connect your third-party source.
Enter your Notion authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get search results
. If you used third-party access control, see
Preview results for apps with third-party access control
.
Connect Okta
Use the following procedure to sync data from Okta to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connector, make sure that you have the domain URL
and administrator access to the Okta instance. Use the following steps to obtain
the Okta instance URL, client ID, and API token.
To obtain the Okta instance URL, do the following:
Sign in to the
Okta
login page with
your administrator credentials.
Click your profile icon or navigate directly to the
Admin console
.
Your Okta instance URL appears as the subdomain in the address bar.
To generate the client ID and API token, do the following:
Sign in to your Okta instance URL with your administrator account.
Navigate to the
Admin dashboard
.
Click the
Applications
icon and select
Applications
.
Click
Create app integration
.
Select
OIDC - OpenID Connect
.
Select
Web application
as the application type, and then click
Next
.
Enter a name in the
App integration name
field.
Scroll to see
Assignments
, select
Skip group assignment for now
.
Click
Save
.
In the
Client credentials
window, click
Edit
.
Select
Public key / Private key
.
Under
Public key
, click
Add key
.
Click
Generate new key
, and then click
Done
and
Save
.
A dialog appears; click
Save
.
Under
General settings
, click
Edit
.
Select
Client credentials
, and then click
Save
.
Create a Okta connector
Console
To use the Google Cloud console to sync data from Okta to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Okta
to connect
your third-party source.
Enter your Okta authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up,
see
Get search results
. If you used third-party
access control,
see
Preview results for apps with third-party access control
.
Connect OneDrive
Use the following procedure to sync data from OneDrive to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
Have the following OneDrive authentication information ready:
Client ID, client secret, and tenant ID. For information about setting up
these parameters, see
Quickstart: Register an application with the
Microsoft identity platform
in the Microsoft
documentation.
Specify scopes for access. An administrator role is required. For more
information, see
Quickstart: Configure a client application to access a
web API
in the Microsoft documentation.
Configure the following scopes:
View scopes
Files.Read.All (Application)
Group.Read.All (Application)
User.Read.All (Application)
Create a OneDrive connector
Console
To use the Google Cloud console to sync data from OneDrive to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
OneDrive
to connect your third-party source.
Enter your OneDrive authentication information.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency for your data store.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
To preview how your search results appear after your app and data store are set up, see
Get search results
. If you used third-party access control, see
Preview results for apps with third-party access control
.
Connect Salesforce
Use the following procedure to sync data from Salesforce to Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
Have the following authentication information ready. For information about
setting up client ID and client secret in Salesforce, see
Configure a connected
app for the OAuth 2.0 client credentials
flow
in the Salesforce documentation.
Instance URL
Consumer ID
Consumer secret
The following limitations apply:
Use either an Enterprise or Developer plan. Trial accounts are not supported.
Make sure that you are using Sales Cloud. Service Cloud is not supported.
Add Google Cloud to Salesforce CORS allowlist. Go the next step if you have already completed this task.
Follow the instructions in the Salesforce documentation to configure the CORS allowlist.
Enter
https://console.cloud.google.com/
as an origin URL and save your configuration.
Create a Salesforce connector
Console
To use the Google Cloud console to sync data from Salesforce to
Vertex AI Search
, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Salesforce
to connect your third-party source.
Enter your Salesforce authentication information.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency.
Click
Create
. Vertex AI Search
creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page.
The
Connector state
changes from
Creating
to
Running
when it
starts synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
See
Preview results for apps with third-party access control
.
Connect ServiceNow
Use the following procedure to sync data from ServiceNow to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection, ensure you have the following in place:
ServiceNow instance
: Create a ServiceNow instance by following the instructions on the
ServiceNow Developer
documentation.
Google Cloud project
: Set up a Google Cloud project with an admin account capable of managing organization-level configurations, ensuring the organization can set up a workforce pool.
Workforce pool
: Make sure your organization is set up to manage a workforce pool.
Set up ServiceNow
ServiceNow offers two primary sites:
Main ServiceNow site
: The site for your ServiceNow instance.
Manages users, groups, and system administration tasks.
URL: The URL for your ServiceNow instance.
Sign in using your administrator credentials.
Developer site
:
Configures the knowledge base, sets up workflows, and develops custom applications.
URL:
https://developer.service-now.com
.
Sign in using your ServiceNow ID.
To create an OAuth endpoint, do the following:
Sign into the main ServiceNow instance with administrator privileges.
Navigate to
All
>
System OAuth
>
Application registry
.
Figure 1.
Select application registry
Click
New
.
Figure 2.
Click the New button
Select
Create an OAuth API endpoint for external clients
.
Figure 3.
Select the option to create an OAuth API endpoint for external clients
Figure 1.
Select application registry
Click
New
.
Figure 2.
Click the New button
Select
Create an OAuth API endpoint for external clients
.
Figure 3.
Select the option to create an OAuth API endpoint for external clients
Fill in the required information:
Name
: Unique name.
Redirect URL
: Enter the redirect URL.
Redirect URL
: Enter the redirect URL.
Click
Submit
to create the credential.
Figure 4.
Enter the redirect URL and click the Submit button
After submission, click the name to view the
Client ID
.
Figure 5.
View the client ID
The secret is masked. Click the
lock
icon next to it to unmask and view
client secret.
Figure 6.
View the client secret
Save the
Client ID
and
Client secret
for later use.
Figure 7.
Copy the client ID and client secret
To retrieve ServiceNow instance credentials, do the following:
<figure id="servicenow">
<img src="images/servicenow-connector-images/redirect-url.png" alt="select">
<figcaption>
<b>Figure 4.</b> Enter the redirect URL and click the Submit button
</figcaption>
</figure>
After submission, click the name to view the
Client ID
.
Figure 5.
View the client ID
The secret is masked. Click the
lock
icon next to it to unmask and view
client secret.
Figure 6.
View the client secret
Save the
Client ID
and
Client secret
for later use.
Figure 7.
Copy the client ID and client secret
To retrieve ServiceNow instance credentials, do the following:
Go to
developer.service-now.com
and click
Manage instance password
.
Figure 8.
Click the Manage instance password button
Keep a copy of the instance URL, username, and password to use when required.
At this stage, all five pieces of information needed to set up a ServiceNow
data store are available. If there are no concerns with using the administrator
role to pull data, proceed to creating a data store.
<figure id="servicenow">
<img src="images/servicenow-connector-images/manage-instance.png" alt="select">
<figcaption>
<b>Figure 8.</b> Click the Manage instance password button
</figcaption>
</figure>
Keep a copy of the instance URL, username, and password to use when required.
At this stage, all five pieces of information needed to set up a ServiceNow
data store are available. If there are no concerns with using the administrator
role to pull data, proceed to creating a data store.
Set up roles and permissions
Elevate the administrator role to
security_admin
to manage users and roles.
Click your profile icon and then select
Elevate role
.
Figure 9.
Click the Elevate role button
Select
security_admin
and then click
Update
. The
security_admin
role helps to create roles and manage users.
Figure 10.
Select the `security_admin` role and then click the Update button
Use administrator role: You can use an administrator role to pull data.
You can either use the default administrator role configured with the instance,
or create a new user with an administrator role using the following
instructions.
Go to
All
>
User administration
>
Users
.
Figure 11.
Select users
Create a new user with a name.
Figure 12.
Select username
Enable
Web service access only
. When you select
Web service access only
, you create a non-interactive user.
Interactive users vs. non-interactive users
: Interactive users can
sign in to the ServiceNow UI or service portal using their username and
password. They can access an instance through a URL that points to a
UI page, form, or list. They can also connect using single sign-on
methods such as digest authentication or security assertion markup
language (SAML). Additionally, they can use their credentials to
authorize SOAP connections if permitted by strict security settings,
and they have unrestricted access to other API connections such as
WSDL, JSON, XML, or XSD.
Whereas, non-interactive users can only use their credentials to
authorize API connections like JSON, SOAP, and WSDL. They cannot sign in
to the ServiceNow UI and can only access the instance through API
protocols.
After user creation, select the user from the users list.
Figure 13.
Pick a user
Click
Roles
>
Edit
.
Figure 14.
Edit roles
Add
Admin
.
Click
Save
to add a list of roles to the user.
Figure 15.
Add list of roles to the user
Add
admin
.
Click
Set password
, auto-generate, and save it.
Figure 16.
Set password
Custom role (
Recommended
): Using the administrator role may not suit teams
or organizations that want to avoid assigning overly powerful permissions.
This option provides a role with three specific permissions that grant the
required access.
Go to
All
>
System security
>
Users and groups
>
Roles
.
Figure 17.
Add roles
Select
New
, enter a name.
Figure 18.
Click the New button
Click
Submit
.
Figure 19.
Click the Submit button
Find the created role in the list.
Figure 20.
Click the Submit button
Navigate to
Contains roles
>
Edit
.
Figure 21.
Click the Edit button
Add the following roles to the newly created role, and then click
Save
.
catalog_admin
knowledge_admin
incident_manager
Figure 22.
Add roles and click the Save button
Confirm updates.
Figure 23.
Confirm updates
The following figure shows the custom role that include three roles:
Figure 24.
Custom roles
Custom role with ACL rules: This option requires
category_admin
and
knowledge_admin
roles. It provides the minimal set of permissions.
Go to
All
>
User administration
>
Roles
.
Figure 25.
Select roles
Click
New
.
Figure 26.
Click the New button
Provide a name and
Submit
.
Figure 27.
Select a name and click the Submit button
Go to
System security
>
Access control (ACL)
.
Figure 28.
Select access control (ACL)
Click
New
.
Figure 29.
Click the New button
Repeat the following two steps until you grant access to all required tables.
The connector needs access to these tables for each entity to run successfully.
Use
sys_user_role
as an example to see how table access is granted.
Figure 30.
Select `sys_user_role`
Click
Submit
and select the role.
The connector needs access to these tables for each entity to run
successfully.
Table name
Description
incident
Show incidents in search results.
sc_cat_item
Show catalog items in search results.
sc_cat_item_user_criteria_mtom
Enforce ACL by accessing catalog item user criteria.
sc_cat_item_user_criteria_no_mtom
Enforce ACL by accessing catalog item user criteria.
sc_cat_item_user_mtom
Enforce ACL by accessing catalog item user criteria.
sc_cat_item_user_no_mtom
Enforce ACL by accessing catalog item user criteria.
kb_knowledge
Show knowledge items in search results.
kb_knowledge_base
Show knowledge base in search results.
kb_uc_can_contribute_mtom
Enforce ACL by accessing who can contribute to knowledge base.
kb_uc_can_read_mtom
Enforce ACL by accessing knowledge user criteria.
sys_user_role
Enforce ACL by accessing user roles.
sys_user_has_role
Enforce ACL by accessing role information of users.
sys_user_group
Enforce ACL by accessing user group segments.
sys_user_grmember
Enforce ACL by accessing group membership of users.
sys_user
Enforce ACL by accessing user table.
core_company
Enforce ACL by accessing company attributes.
cmn_location
Enforce ACL by accessing location attribute.
cmn_department
Enforce ACL by accessing department attributes.
user_criteria
Enforce ACL by accessing user criteria.
To
run
successfully
,
the
catalog
item
entity
connector
also
requires
explicit
access
to
all
fields
of
the
`sc_cat_item`
table
.
To grant and verify the ACL access, do the following:
Grant explicit access by creating a new ACL rule and manually entering
sc_cat_item.*
in the
Name
field of the form.
Figure 31.
Enter `sc_cat_item.*`
Verify that all the ACLs are updated.
Go to
sys_security_acl_role_list.do
in the search bar.
Figure 32.
Enter `sys_security_acl_role_list.do`
Select
Role
with the role that you want to verify.
Figure 33.
Select role to verify
Verify that all the required ACLs are assigned to the role.
Grant role to a user
Go to
All
>
User administration
>
Users
.
Figure 34.
Select users
Find or create a new user.
Figure 35.
Find or create a new user
If no user is available, go to
System security
>
Users and groups
>
Users
.
Figure 36.
Select users
Click
New
.
Figure 37.
Create a new service account
Create a new service account in the user table. Make sure to click
Web service access only
.
Figure 38.
Create a new service account
Scroll to
Roles
.
Figure 39.
Navigate to Roles
Click
Edit
.
Figure 40.
Edit Roles
Grant the role you created and assign it to the user. Based on the type of
role you created in the previous step, select the appropriate one and assign
it to the user. Click
Save
.
Figure 41.
Select and assign the role
OR
Figure 42.
Assign the role and save
View the custom role with ACL.
Figure 43.
Custom role with ACL
Obtain the username and password for the user and click
Set password
.
Figure 44.
Set password
Auto-generate a password and keep it for later use.
Figure 45.
Auto-generate a password
Elevate the administrator role to
security_admin
to manage users and roles.
Click your profile icon and then select
Elevate role
.
Figure 9.
Click the Elevate role button
Select
security_admin
and then click
Update
. The
security_admin
role helps to create roles and manage users.
Figure 10.
Select the `security_admin` role and then click the Update button
Use administrator role: You can use an administrator role to pull data.
You can either use the default administrator role configured with the instance,
or create a new user with an administrator role using the following
instructions.
Go to
All
>
User administration
>
Users
.
Figure 11.
Select users
Create a new user with a name.
Figure 12.
Select username
Enable
Web service access only
. When you select
Web service access only
, you create a non-interactive user.
Interactive users vs. non-interactive users
: Interactive users can
sign in to the ServiceNow UI or service portal using their username and
password. They can access an instance through a URL that points to a
UI page, form, or list. They can also connect using single sign-on
methods such as digest authentication or security assertion markup
language (SAML). Additionally, they can use their credentials to
authorize SOAP connections if permitted by strict security settings,
and they have unrestricted access to other API connections such as
WSDL, JSON, XML, or XSD.
Whereas, non-interactive users can only use their credentials to
authorize API connections like JSON, SOAP, and WSDL. They cannot sign in
to the ServiceNow UI and can only access the instance through API
protocols.
After user creation, select the user from the users list.
Figure 13.
Pick a user
Click
Roles
>
Edit
.
Figure 14.
Edit roles
Add
Admin
.
Click
Save
to add a list of roles to the user.
Figure 15.
Add list of roles to the user
Add
admin
.
Click
Set password
, auto-generate, and save it.
Figure 16.
Set password
Custom role (
Recommended
): Using the administrator role may not suit teams
or organizations that want to avoid assigning overly powerful permissions.
This option provides a role with three specific permissions that grant the
required access.
Go to
All
>
System security
>
Users and groups
>
Roles
.
Figure 17.
Add roles
Select
New
, enter a name.
Figure 18.
Click the New button
Click
Submit
.
Figure 19.
Click the Submit button
Find the created role in the list.
Figure 20.
Click the Submit button
Navigate to
Contains roles
>
Edit
.
Figure 21.
Click the Edit button
Add the following roles to the newly created role, and then click
Save
.
catalog_admin
knowledge_admin
incident_manager
Figure 22.
Add roles and click the Save button
Confirm updates.
Figure 23.
Confirm updates
The following figure shows the custom role that include three roles:
Figure 24.
Custom roles
Custom role with ACL rules: This option requires
category_admin
and
knowledge_admin
roles. It provides the minimal set of permissions.
Go to
All
>
User administration
>
Roles
.
Figure 25.
Select roles
Click
New
.
Figure 26.
Click the New button
Provide a name and
Submit
.
Figure 27.
Select a name and click the Submit button
Go to
System security
>
Access control (ACL)
.
Figure 28.
Select access control (ACL)
Click
New
.
Figure 29.
Click the New button
Repeat the following two steps until you grant access to all required tables.
The connector needs access to these tables for each entity to run successfully.
Use
sys_user_role
as an example to see how table access is granted.
Figure 30.
Select `sys_user_role`
Click
Submit
and select the role.
The connector needs access to these tables for each entity to run
successfully.
Table name
Description
incident
Show incidents in search results.
sc_cat_item
Show catalog items in search results.
sc_cat_item_user_criteria_mtom
Enforce ACL by accessing catalog item user criteria.
sc_cat_item_user_criteria_no_mtom
Enforce ACL by accessing catalog item user criteria.
sc_cat_item_user_mtom
Enforce ACL by accessing catalog item user criteria.
sc_cat_item_user_no_mtom
Enforce ACL by accessing catalog item user criteria.
kb_knowledge
Show knowledge items in search results.
kb_knowledge_base
Show knowledge base in search results.
kb_uc_can_contribute_mtom
Enforce ACL by accessing who can contribute to knowledge base.
kb_uc_can_read_mtom
Enforce ACL by accessing knowledge user criteria.
sys_user_role
Enforce ACL by accessing user roles.
sys_user_has_role
Enforce ACL by accessing role information of users.
sys_user_group
Enforce ACL by accessing user group segments.
sys_user_grmember
Enforce ACL by accessing group membership of users.
sys_user
Enforce ACL by accessing user table.
core_company
Enforce ACL by accessing company attributes.
cmn_location
Enforce ACL by accessing location attribute.
cmn_department
Enforce ACL by accessing department attributes.
user_criteria
Enforce ACL by accessing user criteria.
To
run
successfully
,
the
catalog
item
entity
connector
also
requires
explicit
access
to
all
fields
of
the
`sc_cat_item`
table
.
To grant and verify the ACL access, do the following:
Grant explicit access by creating a new ACL rule and manually entering
sc_cat_item.*
in the
Name
field of the form.
Figure 31.
Enter `sc_cat_item.*`
Verify that all the ACLs are updated.
Go to
sys_security_acl_role_list.do
in the search bar.
Figure 32.
Enter `sys_security_acl_role_list.do`
Select
Role
with the role that you want to verify.
Figure 33.
Select role to verify
Verify that all the required ACLs are assigned to the role.
Grant role to a user
Go to
All
>
User administration
>
Users
.
Figure 34.
Select users
Find or create a new user.
Figure 35.
Find or create a new user
If no user is available, go to
System security
>
Users and groups
>
Users
.
Figure 36.
Select users
Click
New
.
Figure 37.
Create a new service account
Create a new service account in the user table. Make sure to click
Web service access only
.
Figure 38.
Create a new service account
Scroll to
Roles
.
Figure 39.
Navigate to Roles
Click
Edit
.
Figure 40.
Edit Roles
Grant the role you created and assign it to the user. Based on the type of
role you created in the previous step, select the appropriate one and assign
it to the user. Click
Save
.
Figure 41.
Select and assign the role
OR
Figure 42.
Assign the role and save
View the custom role with ACL.
Figure 43.
Custom role with ACL
Obtain the username and password for the user and click
Set password
.
Figure 44.
Set password
Auto-generate a password and keep it for later use.
Figure 45.
Auto-generate a password
Create a ServiceNow connector
Console
To use the Google Cloud console to sync data from ServiceNow to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
ServiceNow
to connect your third-party source.
Enter your ServiceNow authentication information.
Instance URI
Client ID
Client secret
User account
Password
Figure 46.
ServiceNow authentication information
Fill in a unique name for your data store and click
Create
.
Instance URI
Client ID
Client secret
User account
Password
Figure 46.
ServiceNow authentication information
Fill in a unique name for your data store and click
Create
.
Select which entities to sync and click
Continue
.
Select a region for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data connector name to see details about it on its
Data
page.
The
Connector state
changes from
Creating
to
Running
when it
starts synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several minutes or several hours.
Configure the workforce pool
The workforce pool lets you to manage and authenticate users from external
identity providers, such as Azure or Okta, within Google Cloud console. To
configure your workforce pool and enable the web app for seamless user access,
do the following:
Create workforce pool at the organization level in Google Cloud by following
the appropriate setup manual:
Azure OIDC setup
Azure SAML setup
Okta & OIDC setup
Okta & SAML setup
Configure the workforce pool in
AI Applications
>
Settings
for the region where you create your app.
Configure the workforce pool
The workforce pool lets you to manage and authenticate users from external
identity providers, such as Azure or Okta, within Google Cloud console. To
configure your workforce pool and enable the web app for seamless user access,
do the following:
Create workforce pool at the organization level in Google Cloud by following
the appropriate setup manual:
Azure OIDC setup
Azure SAML setup
Okta & OIDC setup
Okta & SAML setup
Configure the workforce pool in
AI Applications
>
Settings
for the region where you create your app.
Next steps
To attach your data store to an app, create an app and select your data store
following the steps in
Create a search app
.
See
Preview results for apps with third-party access control
.
Connect SharePoint Data Center On-premises
This section describes the process to create a SharePoint Data Center on-premises
connector.
Sync data from SharePoint Data Center on-premises
Use the following procedure to sync data from SharePoint Data Center on-premises.
After setting up your data source and importing data for the first time,
the data store synchronizes data from the source at the frequency specified
during configuration.
Before you begin
Before setting up your connection, do the following:
Service attachment (required for private destination type only)
:
Use the following steps to generate a service attachment for secure data transfer.
Decide endpoint type
: Select
Public
or
Private
endpoint.
For
Public
endpoint: If the SharePoint Data Center
Destination type
is
Public
, you are not required to create the setup for service
attachment. Instead, you can use your public URL in the
Domain URL
field of the Google Cloud console when creating your connector.
For
Private
endpoint:
Use
private service connect (PSC)
to enable connections from private instances to Google Cloud
Create a Virtual Private Cloud network and required subnets.
Create a virtual machine (VM) instance and install the backend service.
Optional: Set up a
health check
probe to monitor backend health.
Add a load balancer to route traffic to the VM or backend.
Define firewall rules to allow traffic between the PSC endpoint and the backend
Publish the endpoint
by creating a PSC service attachment.
Username and password
: Obtain valid credentials for authentication from
your SharePoint administrator.
Optional for the private destination type:
Domain URL
: Keep the domain
URL of the SharePoint Data Center instance if the instance is behind a proxy
or SSL-based connection.
Optional:
Base domain name
: Provide the base domain name for the
SharePoint instance.
Optional:
Destination port
: Identify the port used for communication
with the SharePoint Data Center.
Use the following configuration guidelines to establish connections with
Private Service Connect(PSC). Adjust or add resources as needed.
Make sure the PSC service attachment is properly configured to connect to
the private instance and meets the requirements for a published service.
Configure network settings:
Place the PSC service attachment and load balancer in different subnets
within the same Virtual Private Cloud network.
The backend system must remain closed to the public network for
security reasons. However, ensure it can accept traffic from the
following sources:
For proxy-based/HTTP(s) load balancers (L4 proxy ILB, L7 ILB),
configure the backend to accept requests from the proxy subnet in
the Virtual Private Cloud network.
For more information, see the
Proxy-only subnets for Envoy-based load balancers
documentation.
Adjust firewall rules:
Ingress rules:
Allow traffic from the PSC service attachment subnet to the internal
load balancer (ILB) subnet.
Make sure that the ILB can send traffic to the backend.
Permit health check probes to reach the backend.
Egress rules: Enable egress traffic by default, unless specific deny
rules apply.
Additional considerations: Make sure to keep all the components, including the
PSC service attachment and load balancer, in the same region.
Create a SharePoint minimum access permission user and set up permissions
To create a SharePoint minimum access permission user, obtain a username and
password from an administrator. The administrator must sign in and follow these
steps to create a new user in the SharePoint Data Center instance:
Click the
Start
menu and navigate to
Windows administrative tools
>
Active directory users and computers
.
Launch the
Active directory users and computers
application.
Expand the organization unit and navigate to the
Users
container where
the new user is added.
Right-click on
Users
and select
New
>
User
.
In the
New object:User
window, enter the following details:
First name (do not use a comma or dot)
Full name
User logon name
Click
Next
.
Enter and confirm the password, then select:
User cannot change password
Password never expires
Click
Next
, then
Finish
.
Locate the created user in the
Users
section, double-click on it, and
select
Properties
.
In the
Properties
window, add an email for the user and click
Apply
.
Assign minimum access permissions to the SharePoint user
Navigate to the
Site collection
.
Click
Settings
(gear icon menu).
Go to
Site Permissions
.
Select
Advanced permissions settings
.
Locate and select the
SiteName visitors
group (this group is automatically
created when the site is set up and has default read access).
Add the user to the
SiteName visitors
group to grant them read-only access.
Note:
This access inherits all permissions for lists, libraries, pages,
and events that have read permissions.
Configure the site collection in SharePoint
Sign in to the
SharePoint admin console
using the administrator username
and password.
In the
Central administration
page, navigate to
Application management
.
Click
Create site collections
.
In the
Create site collection
page:
Enter the required details in the
Title
and
Description
fields.
In the
Web site address
section, enter the URL name for the site.
In the
Primary site collection administrator
section:
Click the
Browse
button next to the
User name
field.
In the
Select people
dialog, enter the administrator username and click
the search icon.
Select the user and click
Ok
.
The
Site successfully created
page appears, displaying the site URL.
Copy the URL and open it in a new tab to access the site.
Sign in with the created user
Use the created user's credentials to sign in to the SharePoint site.
Verify access and permissions for the user.
Create a SharePoint Data Center On-premises connector
Console
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
SharePoint data center
to connect your third-party source.
Enter your authentication information and click
Continue
.
From the
Destination type
drop-down list, select
Public
or
Private
.
For
Public
destination type, you are not required to create the setup
for service attachment. Instead, you can use your public URL in the
Domain URL
field of the Google Cloud console.
For
Private
destination type, enter all the required information:
If your instance has a domain URL:
Service attachment
: Enter your service attachment.
Optional:
Base domain name
: Enter your base domain.
Domain URL
: Enter your domain URL.
Optional:
Destination port
: Enter your destination port.
If your instance does not have a domain URL:
Service attachment
: Enter your service attachment.
Optional:
Destination port
: Enter your destination port.
Click
Continue
.
Optional:
Advanced options
: Select and enable
Proxy settings
and
SSL settings
, if required.
Under the
Entities to sync
, select all the required entities to sync
and click
Continue
.
Select a region for your data connector and enter a name for your data connector.
Select a synchronization frequency.
To manage connector states, do the following:
For private destination type:
Submit the connector details.
VAIS sends a connection request to your PSC.
Navigate to your connector to see a message to allowlist a
projectId
in the PSC.
Allow the connection in PSC:
The connector remains in the
Error
state until you approve the request.
After approval, the connector moves to the
Active
state
during the next sync run.
If your PSC is configured to accept all connections, the connector
automatically moves to the
Active
state after creation.
For public destination type:
Submit the connector details.
The connector automatically enters the
Active
state after submission.
To verify the state of the data store and the ingestion activity, do the following:
Navigate to the connector in the data store list and monitor its state
until it changes to
Active
.
After the connector state changes to
Active
, click the required entity
and confirm that all selected entities are ingested. The data store state
transitions from
Creating
to
Running
when synchronization begins
and changes to
Active
once ingestion completes, indicating that the
data store is set up. Depending on the size of your data, ingestion
can take several hours.
Next steps
To attach your data store to an app, create an app and select your data store following the steps in
Create a search app
.
See
Preview results for apps with third-party access control
.
Connect SharePoint Online
Use the following procedure to sync data from SharePoint Online.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
Grant administrator consent. For information about how to grant consent, see
Grant tenant-wide administrator consent to an application
in the Microsoft Entra documentation.
Prepare the following Sharepoint Online authentication information to use
during setup:
Instance URL. In the form
http://
DOMAIN_OR_SERVER
/[sites/]
WEBSITE
—for example,
mydomain.sharepoint.com/sites/sample-site
.
Federated authentication requires the tenant ID and client ID, while
OAuth requires the tenant ID, client ID, and client secret. To register
the application, select
Accounts in this organizational directory
only
for the sign-in audience, and then locate this authentication
information. For more information, see
Quickstart: Register an application with the Microsoft identity platform
in the Microsoft Entra documentation.
When registering the application, use
https://vertexaisearch.cloud.google.com/console/oauth/sharepoint_oauth.html
as the web callback URL.
The following table describes the roles that are recommended for
configuration and their limitations.
View roles
Roles
Client application registration
Fetch content of all entities
Fetch ACL
Fetch identity
Notes
Site Admins
No
Yes
Yes
Yes
Site Collection administrator
No
Yes
Yes
Yes
Global administrator
Yes
No
Yes
No
Limitation: The global administrator cannot fetch identity or comment and attachment entities.
Site owner
No
Yes
Yes
No
Limitation: The Site owner relates to Microsoft 365 administrator center / Entra administrator center, not specific to SharePoint.
Application administrator
Yes
N/A
N/A
N/A
The application administrator role is related to Microsoft 365 administrator
center / Entra administrator center. It is not specific to Sharepoint.
Use this method for granular control over SharePoint REST API permissions,
allowing you to restrict resource access on the user account. Make sure to
create a new SharePoint user, which might add licensing costs. Use the
OAuth 2.0 refresh token method to set up an Entra
application registration and enable secure access to SharePoint.
Permissions required for this task
These permissions are needed to set up the Sharepoint connector in Step 1.d.
in the following task.
Add and grant admin consent for the following Microsoft Graph permissions:
Permission
Description
GroupMember.Read.All
Read all group memberships
Sites.FullControl.All
Full control over all sites
Sites.Read.All
Read all sites
User.Read.All
Read all users' full profiles
Add and grant admin consent for the following Sharepoint permissions:
Permission
Description
AllSites.FullControl
Have full control of all site collections
AllSites.Read
Read items in all site collections
Configure Entra application registration
Set up an Entra application registration to enable secure access to SharePoint.
Choose between
Federated credentials for token-based access
or
OAuth 2.0
refresh token for granular control
. Use the following steps to configure the
app registration, grant permissions, and establish authentication.
Federated credentials: Set up federated credentials to securely allow Google
to access SharePoint using cryptographically signed tokens, avoiding the need
for a real user principal. To configure permissions and grant access, do the
following:
Obtain service account client ID:
In the Google Cloud console, go to the
AI Applications
page.
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
SharePoint Online
to connect your third-party source.
Note the
Subject identifier
. Don't click
Continue
yet.
Perform the next steps in this task and then complete the steps in
the Google Cloud console by following the instructions in
Create a SharePoint Online connector
.
Note the subject ID but don't click Continue yet
Register app in Microsoft Entra:
Navigate to
Microsoft Entra admin center
.
In the menu, expand the
Applications
section and select
App registrations
.
On the
App registrations
page, select
New registration
.
Register a new app in Microsoft Entra admin center
Create an app registration on the
Register an application
page:
In the
Supported account types
section, select
Accounts in the
organizational directory only
.
In the
Redirect URI
section, select
Web
and enter the redirect URI.
Keep other settings default and click
Register
.
Select the account type and enter the redirect URI
Note the
Client ID
and
Tenant ID
.
App details page
Add federated credentials:
Go to
Certificates & secrets
>
Federated credentials
>
Add credential
.
Add federated credentials in Microsoft Entra
Use the following settings:
Federated credential scenario
:
Other issuer
Issuer
:
https://accounts.google.com
Subject identifier
: Use the value of
Subject identifier
that
you noted in Google Cloud console in Step 1.a.v.
Name
: Provide a unique name.
Click
Add
to grant access.
Connect your Google Account to Microsoft Entra ID
Set API permissions:
Select the app to set API permissions
Add and grant admin consent for the following Microsoft Graph permissions
with the type set to Application:
GroupMember.Read.All
: Read all group memberships.
Sites.FullControl.All
: Full control over all sites.
Sites.Read.All
: Read all sites. Use
Sites.Selected
to assign
specific site permissions instead of
Sites.FullControl.All
.
Sites.Selected
can't be directly configured through the UI.
After selecting
Sites.Selected
, you must call the
Microsoft Graph API
to explicitly grant the fullcontrol role to the application for
the sites you want to crawl.
User.Read.All
: Read all users' full profiles.
Request the API permissions (Application) for Microsoft Graph
Add and grant admin consent for the following SharePoint permissions
with the type set to Delegated:
AllSites.FullControl
: Have full control of all site collections
AllSites.Read
: Read items in all site collections
Select the API permissions
OAuth 2.0 refresh token: Configure OAuth 2.0 authentication using a client secret and a refresh token from the SharePoint user to enable granular control over SharePoint API access. To set up app registration, add a client secret, and assign API permissions, do the following:
Create app registration:
Navigate to
Entra administrator center
.
Create an app registration:
Supported account types:
Accounts in the organizational directory only
.
Redirect URI:
https://vertexaisearch.cloud.google.com/console/oauth/sharepoint_oauth.html
.
Note the
Client ID
and
Tenant ID
.
Copy the Client ID and the Tenant ID
Add client secret:
Go to
Certificates & secrets
>
New client secret
.
Create a new client secret
Note the secret string.
Copy the secret ID
Set API permissions:
Add and grant administrator consent for the following permissions:
GroupMember.Read.All
: Read all group memberships.
Sites.FullControl.All
: Full control of all site collections.
User.Read.All
: Read all users' full profiles.
AllSites.FullControl
: Full control over all sites.
Use a dedicated user account with limited access to specific sites.
Make sure the account has
Owner
access to the selected sites.
Create a SharePoint Online connector
Console
To use the Google Cloud console to sync data from Slack to
Vertex AI Search
, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
SharePoint Online
to connect your third-party source.
Search for and select Sharepoint as the data source
Enter your Sharepoint Online authentication information and click
Continue
.
Add the authentication information
Enter the SharePoint site URL:
For a single site:
https://domain_name.sharepoint.com/sites/<site_name>
.
For all first-level sites:
https://domain_name.sharepoint.com
.
Select the entities to sync and click
Continue
.
Select the entities to sync and the sync frequency
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency for your data store.
Data synchronization frequencies range from three hours to seven days
Identity synchronization frequencies range from 30 minutes to seven days
Click
Create
. Vertex AI Search
creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Connector status on the data store details page
Depending on the size of your data, ingestion can take minutes or hours.
Test the search engine
After configuring your search engine, test its capabilities. This ensures it returns accurate results based on user access.
Enable web app:
Go to the app integration configurations and toggle to
Enable the web app
.
Test web app:
Click
Open
next to the web app link and sign in with a user in your workforce pool.
Verify that search results are restricted to items accessible by the logged-in user.
Configure the workforce pool
The workforce pool lets you to manage and authenticate users from external identity providers, such as Azure or Okta, within Google Cloud console. To configure your workforce pool and enable the web app for seamless user access, do the following:
Create workforce pool at the organization level in Google Cloud by following the appropriate setup manual:
Azure OIDC setup
Azure SAML setup
Okta & OIDC setup
Okta & SAML setup
Configure the workforce pool in
AI Applications
>
Settings
for the region where you create your app.
Next steps
To attach your connector to an app, create an app and select your connector following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Slack
Use the following procedure to sync data from Slack.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
Set up access control for your data source. For information about setting up
access control, see
Use data source access control
.
To follow the steps in
Configure your Slack app
, you must
have the permissions to install new apps in your workspace, that's included
in the
Workspace Owner
role. Contact your
Workspace Primary Owner
to be assigned as a
Workspace Owner
.
Understand that by default, Slack restricts crawling and syncing content
from private channels, group messages, and direct messages.
Permissions required for this task
These permissions are needed to generate a bot token
users:read.email
channels:history
channels:read
groups:history
groups:read
im:history
im:read
mpim:history
mpim:read
team:read
users:read
files:read
These permissions are needed to generate a user token
users:read.email
channels:history
channels:read
groups:history
groups:read
im:history
im:read
mpim:history
mpim:read
users:read
files:read
Configure the Slack app
The Slack connector requires an access token to be able to ingest documents from
your Slack workspace. To obtain an access token to allow
Vertex AI Search
to ingest documents from your Slack workspace.
For more information, see
Quickstart
and
How to quickly get and use a Slack API token
in the Slack
documentation.
There are two different types of tokens you can use:
Bot token
Benefits:
It's not tied to a specific user.
It can have a more secure access to private Slack channels, instant
messages (IM), and multi-person instant messages (MPIM). The members
involved in those channels and messages can invite the bot.
The bot can also be invited to public channels. When configuring the
bot token, you can add the
channels:join
permission for the
crawler to automatically attempt to join all public channels.
Limitations:
When the bot attempts to join public channels, a join message is sent
to the channel.
User token
Benefits:
It can access all public channels without the need to join them
beforehand.
Limitations:
It's tied to a specific user.
With user token, users can't crawl private channels, IMs, and MPIMs
that they're not a part of.
Configure bot token
The following steps show you how to configure a bot token:
Sign in to
Slack API Apps
.
Click
Create new app
.
Create new app in Slack App
Select
From scratch
. This option lets you configure the app's
information, scopes, settings, and features.
Start creating the app from scratch
Enter a name for your app.
The name you select is visible to all Slack users.
Select the workspace for integration.
Because you can't change an app's workspace later, ensure that you select the
correct workspace.
Enter a name and select the correct workspace
Click
Create app
.
In the sidebar, select
OAuth & permissions
.
OAuth & Permissions in the Slack app's sidebar
Under
Bot token scopes
, add the following required scopes:
class="showalways">View scopes
channels:history
channels:read
files:read
groups:history
groups:read
im:history
im:read
mpim:history
mpim:read
team:read
users:read
users:read.email
By default, the bot reads from the
#general
and
#random
channels.
Select the scopes for the bot token
To enable the bot to crawl the channels, do the following:
For public channels, do one of the following:
Invite the bot manually.
Grant the
channels:join
scope to allow the bot to attempt join
automatically.
For private channels, invite the bot manually.
On the same page, click
Install to
WORKSPACE_NAME
.
Install the app in your workspace
Follow the on-screen instructions to install the app and after the app is
installed, copy and note the bot's OAuth token.
Copy the bot's OAuth token
Configure a user token
The following steps show you how to configure a bot token:
Sign in to
Slack API Apps
.
Click
Create new app
.
Create new app in Slack App
Select
From scratch
. This option lets you configure the app's
information, scopes, settings, and features.
Start creating the app from scratch
Enter a name for your app.
The name you select is visible to all Slack users.
Select the workspace for integration.
Because you can't change an app's workspace later, ensure that you select the
correct workspace.
Enter a name and select the correct workspace
Click
Create app
.
In the sidebar, select
OAuth & permissions
.
OAuth & Permissions in the Slack app's sidebar
Under
User token scopes
, add the following required scopes:
class="showalways">View scopes
channels:history
channels:read
files:read
groups:history
groups:read
im:history
im:read
mpim:history
mpim:read
team:read
users:read
users:read.email
Select the scopes for the user token
On the same page, click
Install to
WORKSPACE_NAME
.
Install the app in your workspace
Follow the on-screen instructions to install the app and after the app is
installed, copy and note your user OAuth token.
Copy the user's OAuth token
Create a Slack Cloud connector
Console
To use the Google Cloud console to sync data from Slack to
Vertex AI Search
, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
In the Google Cloud console, create a data store
On the
Select a data source
page, scroll or search for
Slack
to
connect your third-party source.
Enter your Slack authentication information.
Instance ID (Workspace ID)
:
To obtain your workspace ID, sign in to your Slack workspace using a
web browser. Don't use the Slack app. For more information, see
Specify the Slack source for your data store
.
In the URL, note the unique workspace ID, which is the string after
/client
beginning with
T
.
Obtain the instance ID (workspace ID)
Auth token
: Use the token obtained from the last when you generated
the
bot token
or the
user token
.
Select which entities to sync and click
Continue
.
To crawl all channels, retain the default selections.
To crawl specific channels, click
Filter
and select the channels.
The following image shows an example configuration that allows crawling
of channels named
general
and
random
.
Select the channels to crawl
Select a region for your data store.
Enter a name for your data store.
Select a synchronization frequency for your data store.
Click
Create
. Vertex AI Search
creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your data store name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take minutes or hours.
Next steps
To attach your connector to an app, create an app and select your connector following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect WordPress
Use the following procedure to sync data from WordPress to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up the connection, ensure you have the following:
Username and password
: Obtain the credentials from the WordPress administrator.
Site URL
: Use this URL for data store creation.
Create a WordPress user
To create a WordPress user, obtain a username and password from an administrator.
The administrator must sign in and follow these steps to create a new user in
the WordPress instance.
Sign in as an administrator:
Navigate to your hosting platform and sign in with your administrator
credentials to access your WordPress website.
Click the
Website
icon.
Click
WordPress admin
for your site.
Create a new user:
On the
WordPress admin
page, navigate to the
Users
tab.
Click
Add new
.
Fill in all the required details, including:
Username
Email address
Optional: First and last name
Role
Password (if prompted)
Click
Add new user
to save the changes.
Create a WordPress connector
Console
To use the Google Cloud console to sync data from WordPress to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create
data store
.
On the
Select a data source
page, scroll or search for
WordPress
to
connect your third-party source.
Enter your WordPress authentication information and click
Continue
.
In the
URL
field, enter your WordPress site URL and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
.
Connect Zendesk
Use the following procedure to sync data from Zendesk to
Vertex AI Search.
After you set up your data source and import data the first time, the data store
syncs data from that source at a frequency that you select during setup.
Before you begin
Before setting up your connection:
In addition to the third-party connector allowlist, this connector requires
that your project is added to an additional allowlist. To be added to this
allowlist, contact your Vertex AI Search account team.
Set up access control for your data source. For information
about setting up access control, see
Use data source access control
.
A Zendesk administrator must generate or obtain the
following for integrating with Vertex AI Search:
Access token. API Token of your Zendesk instance.
Instance URI.
Create a Zendesk connector
Console
To use the Google Cloud console to sync data from Zendesk to
Vertex AI Search, follow these steps:
In the Google Cloud console, go to the
AI Applications
page.
AI Applications
In the navigation menu, click
Data stores
.
Click
add
Create data store
.
On the
Select a data source
page, scroll or search for
Zendesk
to
connect your third-party source.
Enter your Zendesk authentication information and click
Continue
.
Select which entities to sync and click
Continue
.
Select a region for your data store.
Enter a name for your data connector.
Select a synchronization frequency.
Click
Create
. Vertex AI Search creates your data store and
displays your data stores on the
Data stores
page.
To check the status of your ingestion, go to the
Data stores
page and
click your connector name to see details about it on its
Data
page. The
Connector state
changes from
Creating
to
Running
when it starts
synchronizing data. When ingestion is complete, the state changes to
Active
to indicate that the connection to your data source is set up and
awaiting the next scheduled synchronization.
Depending on the size of your data, ingestion can take several
minutes or several hours.
Next steps
To attach your connector to an app, create an app and select your connector
following the steps in
Create a search app
.
To preview how your search results appear after your app is set up, see
Get
search results
. If you used third-party access
control, see
Preview results for apps with third-party access
control
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
<figure id="servicenow">
<img src="images/servicenow-connector-images/redirect-url.png" alt="select">
<figcaption>
<b>Figure 4.</b> Enter the redirect URL and click the Submit button
</figcaption>
</figure>

```

### Code Example 2 (text)

```text
<figure id="servicenow">
<img src="images/servicenow-connector-images/manage-instance.png" alt="select">
<figcaption>
<b>Figure 8.</b> Click the Manage instance password button
</figcaption>
</figure>

```

### Code Example 3 (text)

```text
To run successfully, the catalog item entity connector also requires
explicit access to all fields of the `sc_cat_item` table.

```

### Code Example 4 (text)

```text
To run successfully, the catalog item entity connector also requires
explicit access to all fields of the `sc_cat_item` table.

```

