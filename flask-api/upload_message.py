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

def upload_message(sender_id, receiver_id, text, voice, video, timestamp):
    #voive and video input parameters can be null
    #voice and video input parameters are links to where the actual attachments are stored
    #to store the attachments first call the blob_storage function 

    #build new entry to append
    new_entry = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "content" : text,
        "attachments" : {
            "voice_link" : voice,
            "video_link" : video
        },
        "timestamp": timestamp
    }

    #I just need to add the new entry, no need to go through past entries because they are all individual
    with open("data/messages.json") as fp:
        listObj = json.load(fp)

    fp.close() 

    listObj.append(new_entry)

    with open("data/messages.json", "r+") as file:
        json.dump(listObj, file, indent=4,  separators=(',',': '))

    file.close()
    
    return True, new_entry
    
    