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
    - A device key is given to it to keep track of registration
- Pull_data
    - This function pulls data from the db given a device id 
- Push_data
    - This function pushes new data (device measurement) to the db 

REST API:
- Register_device POST 
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





