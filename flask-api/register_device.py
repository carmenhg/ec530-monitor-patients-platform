#This function registers a device into the systems DB (soon to come)
#Data is built in the form of a json file with specified parameters
#After registration device will have some info in the following format
#All the data we need at registration time is what type of device it is
"""
{
    "device_id": string,
    "device_key": string,
    "type": string
}
"""
#input to the function is device_type and device_key
import json
import string
import random

#list of registered devices included here to test api, actual values will come from db later 
regist_devices = [
    {
    "device_id": "abcd",
    "device_key": "test1",
    "type": "bp"
    },
    {
    "device_id": "defg",
    "device_key": "test2",
    "type": "temp"
    },
    {
    "device_id": "hijk",
    "device_key": "tes3",
    "type": "weight"
    }
]

def register_device(device_type, device_key):
    #check if device was previously registered, no need to check for device key empty because api does that already 
    for key in regist_devices:
        if key["device_key"] == device_key:
            print("Device is already registered")
        else:
            #register the device is all info is provided
            #and create a device_id for it. How to create this? Random string? Fixed length?
            device_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            if(device_type != ""):
                new_device = {"device_id" : device_id, "device_key" : device_key, "type" : device_type}
                #add new device in list 
                regist_devices.append(new_device)
        