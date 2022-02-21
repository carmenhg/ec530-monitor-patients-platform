#This function pushes data into Database(soon to come) 
#Data is received in the form of a json dict with specified parameters
#Format is as follow 
"""
{
    "device_id": string,
    "device_key": string,
    "type": string,
    "measurement": string,
    "timestamp": string
}
"""

#Output: dict with values confirming that the data was saved 
"""
{
    "device_id": string,
    "type": string,
    "measurement": string,
    "timestamp": string
}
"""

import json

def push_data(device_id, device_key, device_type, measurement, timestamp):

    # dict to hold data to save which is coming from args input, so they get checked for missing data already
    to_append = {"device_id": device_id, "type" : device_type, "measurement" : measurement, "timestamp" : timestamp}


    #Check that device is valid using 'device_key'
    #When a device is registered their 'key' will be added to a list 
    #list is preset for now, change later when DB is up
    devices_f = open('saved_data/registered_devices_output.json')
    registered_devices = json.load(devices_f)
    #close the file
    input_f.close()

    if(device_key not in registered_devices.values()):
        return print("The device is not registered in our systems. We cannot accept your data. Please register your device")
    else:
        #extract needed data: type, measurement, timestamp
        #check for errors
        """
        1. Missing values -> flask args already checks for this 
        2. incorrect type (str, float, etc) -> flask args already checks for this 
        3. measurement that makes no sense: this would be different for devices of different types. what to do??
        """
        #NEED TO IMPLEMENT POINT 3
    
        #finally save the data into our DB(soon to come), json output file for now
        #open file to read
        temp_f = open("saved_data/push_data_output.json")
        # returns JSON object as a dictionary
        temp_data = json.load(temp_f)
        #close file
        temp_f.close()

        temp_data.append(to_append)


        with open("saved_data/push_data_output.json", "r+") as file:
            json.dump(temp_data, file, indent=4,  separators=(',',': '))

        file.close()

        #if operation was successful return an okay message
        return print("Data was pushed: " + to_append)