gae-proto-polymer
=================

Starter polymer web app project  (https://www.polymer-project.org) statically hosted on Google App Engine consuming Google Cloud Endpoint from the same GAE instance.

This is the result of a GDG DevFest session to introduce newbies to the Google Cloud and provides with a very simple view into the world of Cloud Endpoints build using endpoints-proto-datastore (https://github.com/GoogleCloudPlatform/endpoints-proto-datastore) which takes the drudge out of creating RPC messages for Datastore models.

The source code is also association with a Google Spreadsheet that contains some sample code to update and retrieve data using the endpoints.

https://docs.google.com/spreadsheets/d/1UUM2SHCgTFYnzA4D71G4c7t5WWqC1RK5iJAAw7T4pDI

Usage
=====

1. Create a project from the developer console https://console.developers.google.com/project

2. Clone the project in your environment.  Update the project id in the app.yaml as well as \static\post-service\post-service.html

3. Add the project to the Google App Engine Launcher and deploy it ( remember to do step 2 before )

4. Make a copy of the spreadsheet, go to the code editor and change the project id to your App Engine project.  The use the menu to upload the data to GAE using the endpoint

