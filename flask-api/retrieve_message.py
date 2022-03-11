'''
This function retreives messages from the DB (soon to come) given a receiver id:
I chose receiver ID because when you open a chat window you look for who you sent a message to.
Inputs to this function: receiver_id
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

def retrieve_message(receiver_id):

    #list of messages to return, unformatted
    receiver_messages = []

    #load json file that has the info, will come from DB later on
    messages_list_handler = open("test_data/text_messages.json")
    # returns JSON object as a dictionary
    messages_list= json.load(messages_list_handler)
    #close file
    messages_list_handler.close()

    for message in messages_list:
        if message["receiver_id"] == receiver_id:
            receiver_messages.append(message)
    
    return receiver_messages

    
    
    