# ec530-monitor-patients-patform

Author: Carmen Hurtado 

**API Documentation is made using Flask-restx Swagger**

## Project Description
A WEB application that uses a restful API to monitor patient data. It is a platform where administrators, medical professionals, and patients can manage device data. 

## USER Interface
This module registers users. All information needed is username, password, and role. The Web appliclation creates a session for each user to authenticate througout the process. 

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
- Register_device
    - This function registers a new device that then will be available for assigning and measuring data
        - Devices cannot double register 
        - Device needs to be one of the acceptable devices. For example a phone cannot register 
        - ASSUMPTIONS:
            - None, any 3rd party device that is acceptable can register
- Assign_device
    - This function assigns a device to a patient
        -cDevice needs to be in the list of registered devices to be able to be assigned 
        - Device cannot push_data unless there is a user_id specified to it
        - Can a device be assigned to a patient that already has a device of the same type assigned?
        - ASSUMPTIONS:
            - Only MPs can assign a device, MP_id will be provided when assigning a device. I don’t have to worry about where that id is coming from 

- Pull_data
    - This function pulls data from the db given a device id 
    - ASSUMPTIONS:
        - None
- Push_data
    - This function pushes new data (device measurement) to the db 
        - Device needs to have a user_id associated to it to be able to do this 
        - ASSUMPTIONS:
            - None 

## Database Design






