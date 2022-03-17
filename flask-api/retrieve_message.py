'''
This function retreives messages from the DB (soon to come) given a receiver id:
I chose receiver ID because when you open a chat window you look for who you sent a message to.
Inputs to this function: receiver_id
'''

import string 
import json

#For testing without the DB 
USERS = [
    {
        "name": "Carmen Hurtado",
        "user_id": "abcd",
        "roles": ["mp"],
        "devices": []
    }, 
    {
        "name": "Andreas Papadkis",
        "user_id": "defg",
        "roles": ["p"],
        "devices": []
    }, 
    {
        "name": "Estela Hurtado",
        "user_id": "ghtd",
        "roles": ["a"],
        "devices": []
    }, 
    {
        "name": "Alicia Garcia",
        "user_id": "yupe",
        "roles": ["p"],
        "devices": []
        
    }, 
]

def retrieve_message(receiver_id):

    #list of messages to return, unformatted
    receiver_messages = []

    #error check that user is registered in our system
    user_ids = []
    for user in USERS:
        user_ids.append(user["user_id"])
    if receiver_id not in user_ids:
        return False, json.loads('{"response": "User is not registered in our system"}')
    else:
        #load json file that has the info, will come from DB later on
        messages_list_handler = open("test_data/text_messages.json")
        # returns JSON object as a dictionary
        messages_list= json.load(messages_list_handler)
        #close file
        messages_list_handler.close()

        for message in messages_list:
            if message["receiver_id"] == receiver_id:
                receiver_messages.append(message)
        
        return True, receiver_messages

    
    
    