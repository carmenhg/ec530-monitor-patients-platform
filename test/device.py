import json
# DEVICE INTERFACE

# add data. Funct will be called by 3rd party device. More than one device data input at a time?
#for now I will pass a json to mock incoming data 
def add_data(device_input_data):
    # dict to hold temp data 
    to_append = {}

    # device info I need: did, type, measurement, from which patient, time it was taken
    f = open(device_input_data)
 
    # returns JSON object as a dictionary
    data = json.load(f)

    #extract needed data
    to_append["did"] = data["did"]
    to_append["type"] = data["type"]
    to_append["uid"] = data["uid"]
    to_append["measurement"] = data["measurement"]
    to_append["timestamp"] = data["timestamp"]

    f.close()

    #once I get this info add to a json file to save 
    with open("device_table/devices.json") as fp:
        listObj = json.load(fp)

    listObj.append(to_append)
    print(listObj)

    with open("device_table/devices.json", "r+") as file:
        json.dump(listObj, file, indent=4,  separators=(',',': '))

#this function will retreive any data given a user id or a device id
def get_data(user_id, device_id):
    retrieved_users = []
    retrieved_devices = []
    #load json file that has the info
    with open("device_table/devices.json") as file:
        all_data = json.load(file)

        #match all entries with gives uid
        if user_id != "":
            for entry in all_data:
                if entry["uid"] == user_id:
                    retrieved_users.append(entry)
        
        #match all entries with gives did
        if device_id != "":
            for entry in all_data:
                if entry["did"] == device_id:
                    retrieved_devices.append(entry)
    
    print(retrieved_users)
    print(retrieved_devices)





# if __name__ == "__main__":
#     get_data("1234", "")


