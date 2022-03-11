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

#json structure for testing without db looks like this
'''
{
    sender_id: string,
    receiver_id: string,
    content: string,
    attachments: list of link strings,
    timestamp: string
}
'''

def upload_message(sender_id, receiver_id, content, timestamp):

    #WORK IN PROGRESS
    
    