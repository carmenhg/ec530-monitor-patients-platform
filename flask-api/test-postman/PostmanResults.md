# Testing my API with Postman GUI
This file describes my organization, automation, and results from testing performed with the Postman application.

I have created a collection inside the Postman GUI for the DEVICE module. Under this collection I saved the unit tests for the DEVICE API calls. 

## Individual Requests Test
I am able to test each request separately and see the response in the console as well as the status code. 

I have built as least two unit tests for each API method. As an example of how I am conducting these tests I have the below screenshots of the request for the register_device method that registers a device into my (soon to come db) system and checks that this device was not previously registered and that it meets the right criteria and it is not missing any input parameters. 

<img src="/screenshots/InvalidRegustration.png" style="height: 200px; width:200px;"/>

*In the above image we can see an Invalid request that returns to the user a message saying that this device is already registered. Th efunction in the backend did not add this device to the list of registered devices again.*


<img src="/screenshots/ValidRegestration.png" style="height: 200px; width:200px;"/>

*In the above image we can see an Valid request that returns to the user the new entry for the newly registered device and the gived device_id that was assigned to it. This id is later used for assigning to a patient.*

## Testing Automation with Postman 

Postman has the ability to run all the requests in a collection for as many iterations as I would like. For this Postamn will run my requests and tell me what it returns; but also there needs to be TESTS added to the collection. These tests are scripts that postman runs for each request and can be modified to test for various things. As of now I am using their scripts templates to check that all my request return 200 OK response. 

In the below image we can see how Postman organizes the results from these tests. This is somehow similar to Github Actions workflow and I will be exploring more to see if there are ways to automate this even further by maybe integrating it with my push commands on the Github Repo. 

<img src="/screenshots/DeviceCollectionTestResults.png" style="height: 200px; width:200px;"/>