#This function assigns a device to a patient
#Data is built in the form of a json file with specified parameters device_key and user_id
#After assigning, the device id will be added to the USER DB (in this case for patients)

#Output: returns True of False if operation succeeded, should also return patient id? or name? 

import json
import string

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
                with open("test_pytest/devices_output/regist_devices.json") as fp:
                    listObj = json.load(fp)

                fp.close() 

                for entry in listObj:
                    if entry["device_id"] == device_id:
                        entry["user_id"] = user_id

                with open("test_pytest/devices_output/regist_devices.json", "r+") as file:
                    json.dump(listObj, file, indent=4,  separators=(',',': '))

                file.close()
                
                return True, json.loads('{"success"}')

    # the device id is added to the list of devices aasigned to a patient, when pulling info about the patient then i can look 
    # for device id in reg devices table and see what "type" of device it is 

    #last is to add to the list of registered devices a new field that says to which user this device is assigned to 