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

def push_data(json_input):

    # dict to hold data to save
    to_append = {"device_id": "", "type" : "", "measurement" : "", "timestamp" : ""}

    #open file to read
    input_f = open(json_input)
    # returns JSON object as a dictionary
    input_data = json.load(input_f)
    #close file
    input_f.close()

    #Check that device is valid using 'device_key'
    #When a device is registered their 'key' will be added to a list 
    #list is preset for now, change later when DB is up
    devices_f = open('test/devices_output/regist_devices.json')
    regist_devices = json.load(devices_f)
    #close the file
    input_f.close()

    if("device_key" in input_data.keys()):
        if(input_data["device_key"] not in regist_devices.values()):
            print("The device is not registered in our systems. We cannot accept your data. Please register your device")
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
            temp_f = open("test/devices_output/devices.json")
            # returns JSON object as a dictionary
            temp_data = json.load(temp_f)
            #close file
            temp_f.close()

            temp_data.append(to_append)


            with open("test/devices_output/devices.json", "r+") as file:
                json.dump(temp_data, file, indent=4,  separators=(',',': '))

            file.close()