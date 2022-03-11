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

def push_data(device_id, user_id, device_type, measurement, timestamp):

    # dict to hold data to save which is coming from args input, so they get checked for missing data already
    to_append = {"user_id": user_id, "device_id": device_id, "type" : device_type, "measurement" : measurement, "timestamp" : timestamp}

    #need to check that both device_id and user_id are valid, meaning the user exists and that the device is assigned to this user

    devices_f = open('saved_data/registered_devices_output.json')
    registered_devices = json.load(devices_f)
    devices_f.close()

    for element in registered_devices:
        if(device_id == element["device_id"]):
            #check if device is assigned to a patient
            if user_id not in element:
                return False
            #check if it is the correct patient 
            elif user_id != element["user_id"]:
                return False
            else:
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
                return to_append
    
    