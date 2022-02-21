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

NEED TO DO A SUMMARY OF DOCUMENTATION HERE AND ABOUT UNIT TESTS I USED 



