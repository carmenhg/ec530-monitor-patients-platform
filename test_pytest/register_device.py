#This function registers a device into the systems DB (soon to come)
#Data is built in the form of a json file with specified parameters
#After registration device will have some info in the following format
#All the data we need at registration time is what type of device it is and its key

#Output: the following json dict will be returned as confirmation. It will include a device id generated by the function to be used later. FOR NOW: it is a random str
"""
{
    "reg_device_id": string,
    "device_identifier" : string,
    "type": string
}
"""

import json
import string
import random

def register_device(device_type, device_identifier): # identifier has to be an id from the manufactirer, MAC address maybe?

    #check if device was previously registered, no need to check for device identifier is empty because api does that already 

    #check if device was previously registered
    #load json file that has the info, will come from DB later on
    regist_dev_f = open("test_pytest/devices_output/regist_devices.json")
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
        with open("test_pytest/devices_output/regist_devices.json") as fp:
            listObj = json.load(fp)

        fp.close() 

        listObj.append(new_device)

        with open("test_pytest/devices_output/regist_devices.json", "r+") as file:
            json.dump(listObj, file, indent=4,  separators=(',',': '))

        file.close()
        return True, new_device

        