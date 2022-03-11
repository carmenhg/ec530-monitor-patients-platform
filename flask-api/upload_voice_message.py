'''
This function uploads to the DB (soon to come) a voice message sent between two users
Inputs to this function: sender_id, receiver_id, timestamp, data_string.
Missing input parameters are checked through the API call.
Error checking within the function:
    1. 
    2. 
    3. 
This function will also call a helper function to store the attachment in a BLOB storage 
'''

import string 
import json
import blob_storage

#json structure for testing without db looks like this
'''
{
    sender_id: string,
    receiver_id: string,
    voice_link: string,
    timestamp: string
}
'''

def upload_voice_message(sender_id, receiver_id, voice, timestamp):

    
    
    