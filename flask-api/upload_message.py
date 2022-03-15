'''
This function uploads to the DB (soon to come) a message sent between two users
Inputs to this function: sender_id, receiver_id, timestamp, content.
Missing input parameters are checked through the API call.
Error checking within the function:
    1. 
    2. 
    3. 
'''

import string 
import json

#json structure OUTPUT for testing without db looks like this
'''
{
    sender_id: string,
    receiver_id: string,
    content: string,
    attachments: link strings,
    timestamp: string
}
'''

def upload_message(sender_id, receiver_id, text, voice, video, timestamp):
    #build new entry to append
    new_entry = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "content" : text,
        "attachments" : {
            "voice" : voice,
            "video" : video
        }
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
    
    