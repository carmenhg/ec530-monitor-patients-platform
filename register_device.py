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

def register_device(device_type, device_key):
    #check if device was previously registered
    #load json file that has the info, will come from DB later on
    regist_dev_f = open("test/devices_output/regist_devices.json")
    # returns JSON object as a dictionary
    regist_devices = json.load(regist_dev_f)
    #close file
    regist_dev_f.close()

    if(device_key != "" and regist_devices[device_key]):
        print("Device is already registered")
    else:
        #register the device is all info is provided
        #and create a device_id for it. How to create this? Random string? Fixed length?
        device_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        if(device_type != ""):
            new_device = {"device_id" : device_id, "device_key" : device_key, "type" : device_type}

        #save info to json output file
        with open("test/devices_output/regist_devices.json") as fp:
            listObj = json.load(fp)

        fp.close() 

        listObj.append(new_device)

        with open("test/devices_output/devices.json", "r+") as file:
            json.dump(listObj, file, indent=4,  separators=(',',': '))

        file.close()