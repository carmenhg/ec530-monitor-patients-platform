
'''
This function retreives messages from the DB (soon to come) that contain a keyword given a receiver id and keyword
Inputs to this function: receiver_id, keyword
This function would be called from inside a chat window 
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

# JUST THINKING: this might be a dumb way of doing it. Having all messages for all users together in the same DB struct will
# mean that I have to loop through all messages when I only want for 1 user
# better idea could be to add messages to the USERS db??? How exactly to do this that makes the most sense????

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

def search_by_keyword(receiver_id, keyword):

    #list of messages to return, unformatted
    filtered_messages = []

    #error check that user is registered in our system
    user_ids = []
    for user in USERS:
        user_ids.append(user["user_id"])
    if receiver_id not in user_ids:
        return False, json.loads('{"response": "User is not registered in our system"}')
    else:
        #load json file that has the info, will come from DB later on
        messages_list_handler = open("data/messages.json")
        # returns JSON object as a dictionary
        messages_list= json.load(messages_list_handler)
        #close file
        messages_list_handler.close()

        for message in messages_list:
            if message["receiver_id"] == receiver_id:
                if keyword in message["data_string"]:
                    filtered_messages.append(message)
    
        return True, filtered_messages

    
    
    