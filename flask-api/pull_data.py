'''
This function pulls data from the Database(soon to come) 
Data is stored (for now) in a json file that has all the inputs from devices separated into blocks 
Optional Inputs: 
    device ID, function will retreive any data block that matches this device id 
    user_id, function will retriove all measurements from any device that belong to user 
Output:
    List of entries withy measurements  
'''

import json

#this function will retreive data given a device id or user id
def pull_data(device_id, user_id):
    #list that will be returned
    retrieved_measurements = []

    #load json file that has the info, will come from DB later on
    all_data_f = open("saved_data/push_data_output.json")
    # returns JSON object as a dictionary
    all_data = json.load(all_data_f)
    #close file
    all_data_f.close()
    
    #match all entries with given device_id or user_id
    #one of the inputs needs to be null, check that this is true 
    #check that a device_id was provided, flask api args already does this
    if device_id and not user_id:
        for entry in all_data:
            if entry["device_id"] == device_id:
                retrieved_measurements.append(entry) 
        return True, retrieved_measurements

    elif user_id and not device_id:
        #once the db is set up need to check that this is patient user meaning that it is valid to have measurements for them
        for entry in all_data:
            if entry["user_id"] == user_id:
                retrieved_measurements.append(entry) 
        return True, retrieved_measurements

    else:
        return False, json.loads('{"response": "Cannot retrive data for both inputs"}')
    
    
