'''
This function uploads to the DB (soon to come) a text message sent between two users
Inputs to this function: sender_id, receiver_id, timestamp, data_string.
Missing input parameters are checked through the API call.
Error checking within the function:
    1. 
    2. 
    3. 
'''

import string 
import json

#json structure for testing without db looks like this
'''
{
    sender_id: string,
    receiver_id: string,
    data_string: string,
    timestamp: string
}
'''

def upload_text_message(sender_id, receiver_id, data_string, timestamp):

    #build new entry to append
    new_entry = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "data_string" : data_string,
        "timestamp": timestamp
    }

    #I just need to add the new entry, no need to go through past entries because they are all individual
    with open("test_data/text_messages.json") as fp:
        listObj = json.load(fp)

    fp.close() 

    listObj.append(new_entry)

    with open("test_data/text_messages.json", "r+") as file:
        json.dump(listObj, file, indent=4,  separators=(',',': '))

    file.close()
    
    