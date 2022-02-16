import json
#this function will retreive any data given a device id
def get_data(device_id):
    retrieved_users = []
    retrieved_devices = []
    #load json file that has the info
    with open("test/device_table/devices.json") as file:
        all_data = json.load(file)
        
        #match all entries with gives did
        if device_id != "":
            for entry in all_data:
                if entry["did"] == device_id:
                    retrieved_devices.append(entry)
    file.close()
    
    print(retrieved_users)
    print(retrieved_devices)
    print("Updated workflow")