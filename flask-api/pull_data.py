#This function pulls data from the Database(soon to come) 
#Data is stored (for now) in a json file that has all the inputs from devices separated into blocks 
#Format is as follow 
"""
[
    {
        "device_id": string,
        "type": string,
        "measurement": string,
        "timestamp": string
    },
    {
        "device_id": string,
        "type": string,
        "measurement": string,
        "timestamp": string
    }
]
"""

import json

#just using it for testing flask api, this data will come from the db later on
devices = [
    {
        "device_id": "abcd",
        "type": "temp",
        "measurement": 98.3,
        "timestamp": "2022-02-13T18:25:43.511Z"
    },
    {
        "type": "temp",
        "device_id": "abcd",
        "measurement": 98.3,
        "timestamp": "2022-02-13T18:25:43.511Z"
    }
]

#this function will retreive data given a device id 
def pull_data(device_id):
    #list that will be returned
    retrieved_devices = []
    
    #match all entries with given device_id
    #check that a device_id was provided
    if device_id != "":
        for entry in devices:
            if entry["device_id"] == device_id:
                retrieved_devices.append(entry) 
    else:
        print("A device id must be provided")
  
    
    return(retrieved_devices)
