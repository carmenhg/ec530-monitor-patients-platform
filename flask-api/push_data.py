#This function pushes data into Database(soon to come) 
#Data is received in the form of a json file with specified parameters
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
import json

#for testing rest api, I will have the list of registered devices in this file
registered_devices = [
    {
    "device_id": "abcd",
    "device_key": "test1",
    "type": "bp"
    },
    {
    "device_id": "defg",
    "device_key": "test2",
    "type": "temp"
    },
    {
    "device_id": "hijk",
    "device_key": "tes3",
    "type": "weight"
    }
]

def push_data(input_data):

    # dict to hold data to save
    to_append = {"device_id": "", "type" : "", "measurement" : "", "timestamp" : ""}


    #Check that device is valid using 'device_key'
    #When a device is registered their 'key' will be added to a list 
    #list is preset for now, change later when DB is up
    if("device_key" in input_data.keys()):
        if(input_data["device_key"] not in registered_devices.values()):
            return print("The device is not registered in our systems. We cannot accept your data. Please register your device")
        else:
            #extract needed data: type, measurement, timestamp
            #check for errors
            """
            1. Missing values
            2. incorrect type (str, float, etc)
            3. measurement that makes no sense: this would be different for devices of different types. what to do??
            """
            for key in to_append:
                if (input_data[key] == "") or (type(input_data[key]) != str) :
                    print("Value is missing or has incorrect format")
                else:
                    to_append[key] = input_data[key]
        
            #finally save the data into our DB(soon to come), json output file for now
            #open file to read
            temp_f = open("saved_data/push_data_output.json")
            # returns JSON object as a dictionary
            temp_data = json.load(temp_f)
            #close file
            temp_f.close()

            temp_data.append(to_append)


            with open("tsaved_data/push_data_output.json", "r+") as file:
                json.dump(temp_data, file, indent=4,  separators=(',',': '))

            file.close()

            #if operation was successful return an okay message
            return print("Data was pushed: " + to_append)