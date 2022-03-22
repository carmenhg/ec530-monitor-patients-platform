#Here are all the functions that are related to the device module 
import json
import string
import random

#############################################################################################################################

#This function registers a device into the systems DB (soon to come)
#Data is built in the form of a json file with specified parameters
#After registration device will have some info in the following format
#All the data we need at registration time is what type of device it is and its key

def register_device(device_type, device_identifier): # identifier has to be an id from the manufactirer, MAC address maybe?

    #check if device was previously registered, no need to check for device identifier is empty because api does that already 

    #load json file that has the info, will come from DB later on
    regist_dev_f = open("saved_data/registered_devices_output.json")
    # returns JSON object as a dictionary
    regist_devices = json.load(regist_dev_f)
    #close file
    regist_dev_f.close()

    #extract all keys for comparison
    temp_device_identifiers = []

    for element in regist_devices:
        temp_device_identifiers.append(element["device_identifier"])

    #see if any of the keys match the input key
    if device_identifier in temp_device_identifiers:
        return False, json.loads('{"response": "Device was previously registered"}')
    #if device is not registered yet
    else:
        #register the device
        #and create a device_id for it. How to create this? Random string? Fixed length?
        reg_device_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        new_device = {"reg_device_id" : reg_device_id, "device_identifier" : device_identifier, "type" : device_type}
        #add new device in list 
        #save info to json output file
        with open("saved_data/registered_devices_output.json") as fp:
            listObj = json.load(fp)

        fp.close() 

        listObj.append(new_device)

        with open("saved_data/registered_devices_output.json", "r+") as file:
            json.dump(listObj, file, indent=4,  separators=(',',': '))

        file.close()
        return True, new_device


#############################################################################################################################

#This function assigns a device to a patient
#Data is built in the form of a json file with specified parameters device_key and user_id
#After assigning, the device id will be added to the USER DB (in this case for patients)

#Output: returns True of False if operation succeeded, should also return patient id? or name? 
'''The following json format dict is used for testing only before the addition of the DB, 
    this will be later changed to read from the DB itself '''

USERS = [
    {
        "name": "Carmen Hurtado",
        "user_id": "abcd",
        "roles": ["mp"],
        "devices": []
    }, 
    {
        "name": "Andreas Papadkis",
        "user_id": "defg",
        "roles": ["p"],
        "devices": []
    }, 
    {
        "name": "Estela Hurtado",
        "user_id": "ghtd",
        "roles": ["a"],
        "devices": []
    }, 
    {
        "name": "Alicia Garcia",
        "user_id": "yupe",
        "roles": ["p"],
        "devices": []
        
    }, 
]

def assign_device(device_id, user_id): 

    #saved info will be in USERS db table 

    #Check that role of user is PATIENT, otherwise devices cannot be assigned to user 
    for user in USERS:
        if user_id == user["user_id"]:
            roles = user["roles"]
            if "p" not in roles:
                return False, json.loads('{"response": "User is not a patient, cannot be assigned device."}')
            else:
                user["devices"].append(device_id)
                #last is to add to the list of registered devices a new field that says to which user this device is assigned to
                with open("saved_data/registered_devices_output.json") as fp:
                    listObj = json.load(fp)

                fp.close() 

                for entry in listObj:
                    if entry["device_id"] == device_id:
                        entry["user_id"] = user_id

                with open("saved_data/registered_devices_output.json", "r+") as file:
                    json.dump(listObj, file, indent=4,  separators=(',',': '))

                file.close()
                
                return True, json.loads('{"success"}')

    # the device id is added to the list of devices aasigned to a patient, when pulling info about the patient then i can look 
    # for device id in reg devices table and see what "type" of device it is 

    #last is to add to the list of registered devices a new field that says to which user this device is assigned to 


#############################################################################################################################
#This function pushes data into Database(soon to come) 
#Data is received in the form of a json dict with specified parameters
#Format is as follow 
"""
{
    "device_id": string,
    "user_id": string,
    "type": string,
    "measurement": string,
    "timestamp": string
}
"""

#Output: dict with values confirming that the data was saved 

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
                return False, json.loads('{"response": "Device is not assigned to any user"}')
            #check if it is the correct patient 
            elif user_id != element["user_id"]:
                return False, json.loads('{"response": "Device is not assigned to this patient "}')
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
                return True, to_append

#############################################################################################################################

'''
This function pulls data from the Database(soon to come) 
Data is stored (for now) in a json file that has all the inputs from devices separated into blocks 
Optional Inputs: 
    device ID, function will retreive any data block that matches this device id 
    user_id, function will retriove all measurements from any device that belong to user 
Output:
    List of entries withy measurements  
'''

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