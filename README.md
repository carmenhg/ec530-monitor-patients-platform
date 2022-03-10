# ec530-monitor-patients-patform

Author: Carmen Hurtado 

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
I have a folder that includes all the files with the functions for pull data, push data, and register devices as well as the test python file with the unit tests definitions. All this is under a folder named "test"

## For REST API with Flask
I have created a different folder to hold all the files needed to build the RestFul API with Flask. I have copied the files for pull data, push data, register devices functions to this folder. I did this because importing files from a parent folder is very weird and I decided not to loose time figuring this out since this is just temporary for testing. 
File "flask-api.py" has all the routes and calls to the API. 

## Device Module Design 
User stories (need to think of more scenarios that could happen): 
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


REST API:
- Register_device POST 
- Assign_device POST
- Pull_data GET
- Push_data POST

What info do I need to store?:
- Each device information after registration 
    - Device given key
    - User (device_id) that it is assigned to 
    - CHANGE device_id TO user_id
    - What type of measurements it takes
        - Temp
        - Blood pressure
        - Weight
        - Etc
- When new data is entered
    - User_id
    - Type of measurement
        - Can I get this value from previous saves when registering???
    - Measurement data
    - Timestamp 





