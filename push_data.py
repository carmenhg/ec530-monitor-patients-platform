import json
# DEVICE INTERFACE

# add data. Funct will be called by 3rd party device. More than one device data input at a time?
#for now I will pass a json to mock incoming data 
def push_data(device_input_data):
    # dict to hold temp data 
    to_append = {}

    # device info I need: did, type, measurement, time it was taken
    f = open(device_input_data)
 
    # returns JSON object as a dictionary
    data = json.load(f)

    #extract needed data
    #error check

    try:
        to_append["did"] = data["did"]
        to_append["type"] = data["type"]
        to_append["measurement"] = data["measurement"]
        to_append["timestamp"] = data["timestamp"]
    except (KeyError):
        print("There is a value missing")

    f.close()

    #once I get this info add to a json file to save 
    with open("test/device_table/devices.json") as fp:
        listObj = json.load(fp)

    fp.close() 

    listObj.append(to_append)
    print(listObj)

    with open("test/device_table/devices.json", "r+") as file:
        json.dump(listObj, file, indent=4,  separators=(',',': '))

    file.close()