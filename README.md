# ec530-monitor-patients-patform

Author: Carmen Hurtado 

**API Documentation is made using Flask-restx Swagger**
## Documentation 
To document my API I used Swagger with flask-restx. The functions are documented by route and include any parameters that are needed for the API call. 

![swagger](/images/swagger.png)

## Project Description
A WEB application that uses a restful API to monitor patient data. It is a platform where administrators, medical professionals, and patients can manage device data. 

## USER Interface
This module registers users. All information needed is username, password, and role. The Web appliclation creates a session for each user to authenticate througout the process and populate the user role through the screens to render content conditionally.

Main objectives of this module:
- Register users 
    - Adds a new user to the database 
    ![register](/images/register-screen.png)

- Assign medical professionals to patients
    - assigns a medical professional registered user to a registered patient
    ![assignmp](/images/assign-mp-screen.png)

- Unassign medical professionals to patients
    - assigns a medical professional registered user from a registered patient
    ![unassignmp](/images/unassign-mp-screen.png)

## DEVICE Interface
This module has 3 main objectives:
- Register 3rd party devices in our system
    - Thermomethers
    - Blood Pressure Monitors
    - Pulse
    - Oximeter
    - Scales
    - Glucometer
    - etc
- Push data received from these devices into the system's database
- Pull data from the database for multiple uses

## For testing with pytest and Github Actions
I have a folder that includes all the files with the functions for pull data, push data, and register devices as well as the test python file with the unit tests definitions. All this is under a folder named "test-pytest"

## For REST API with Flask
I have created a different folder to hold all the files needed to build the RestFul API with Flask. 
File "flask-api.py" has all the routes and calls to the API. 
Under the "test-postman" folder is a markdown documentation showing all my testing organization for the API calls as well as an explanation to the unit tests that I used. 

## Device Module Design 
User stories: 
- Devices need to register into our system 
- Devices can add new data from their readings 
- User (MP, potentially patients) can see measurements from devices
    - From a specific device
    - From all devices assigned to a patient 
- MP can see which devices are assigned to patients 

API definitions:
- register_device
    - This function registers a new device that then will be available for assigning and measuring data
        - Devices cannot double register 
        - Device needs to be one of the acceptable devices. For example a phone cannot register 
        - ASSUMPTIONS:
            - None, any 3rd party device that is acceptable can register
- assign_device
    - This function assigns a device to a patient
        - Device needs to be in the list of registered devices to be able to be assigned 
        - Device cannot push_data unless there is a user_id specified to it
        - Can a device be assigned to a patient that already has a device of the same type assigned?
        - ASSUMPTIONS:
            - Only MPs can assign a device, MP_id will be provided when assigning a device. I don’t have to worry about where that id is coming from 

- unassign_device
    - This functions removes the device from a patient and makes it available to assign to a different patient
        - No assumptions needed

- Push_data
    - This function pushes new data (device measurement) to the db 
        - Device needs to have a user_id associated to it to be able to do this 
        - ASSUMPTIONS:
            - None 

## Database Design
I am using MongoDB for this project. I have two databases: *auth* and *device*. 
### *auth* 
This db has 2 Collection 
- users

    Below is an image of the fields that this collection includes. 

    ![users](/images/users.png)

- assigned

    Below is an image of the fields.

    ![assigned-users](/images/users-assigned.png)

### *device* 
This db has 3 Collection 
- registered

    Below is an image of the fields that this collection includes. 

    ![reg](/images/device-registered.png)

- assigned

    Below is an image of the fields.

    ![assigned-dev](/images/device-assigned.png)

- measurements

    Below is an image of the fields.

    ![data](/images/data.png)







