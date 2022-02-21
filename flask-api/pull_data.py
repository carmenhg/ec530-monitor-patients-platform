#This function pulls data from the Database(soon to come) 
#Data is stored (for now) in a json file that has all the inputs from devices separated into blocks 
#Input: device ID, function will retreive any data block that matches this device id 

#Output Format is as follow 
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

#this function will retreive data given a device id 
def pull_data(device_id):
    #list that will be returned
    retrieved_measurements = []

    #load json file that has the info, will come from DB later on
    all_data_f = open("saved_data/push_data_output.json")
    # returns JSON object as a dictionary
    all_data = json.load(all_data_f)
    #close file
    all_data_f.close()
    
    #match all entries with given device_id
    #check that a device_id was provided, flask api args already does this
    
    for entry in all_data:
        if entry["device_id"] == device_id:
            retrieved_measurements.append(entry) 
    
    return(retrieved_measurements)
