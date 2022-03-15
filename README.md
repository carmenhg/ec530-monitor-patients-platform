# ec530-monitor-patients-platform

Author: Carmen Hurtado 

For a more detailed documentation of each api method please visit this repo's Wiki page [here](https://github.com/carmenhg/ec530-monitor-patients-platform/wiki)A

# Chat Module Design 
## User stories (need to think of more scenarios that could happen): 
- MP can chat with patients using text, voice or videos
- MP can search for keywords in messages and chats
- Patient can write a text or upload video or voice message to the MP

## API definitions: 
- Upload_text_message
    - This function will push any new message to the db as the messages are being sent
        - Checks that it is a text message meaning it is a string with no attachments
        - Needs as input, sender, receiver, timestamp of when it is sent
        - ASSUMPTIONS:
            - none

- Retrieve_message
    - This function will pull messages from the db to be displayed for chat history 
        - Input: receiver and sender ids to build a conversation
        - ASSUMPTIONS:
        - None 

- Search_by_keyword
    - This function will filter the messages in the db through a user inputted keyword and return the list of messages (in chronological order) to the requester. If the message includes attachments it will also return this attachment.
        - Inputs: keyword, requester_id
        - ASSUMPTIONS:
            - none

- Upload_video_message
    - This function will be called when the message includes a video attachment. Functionality is the same as Upload_text_message
        - Not sure if I need a separate function for this
        - Inputs: sender, receiver, timestamp
        - ASSUMPTIONS:
            - Video is saved already in some sort of blob storage (this would be a functionality of this module or of another module? I think this module)
            - This function only needs the link to this video to save the data in the db 

- Upload_voice_message
    - This function will be called when the message includes a voice attachment. Functionality is the same as Upload_text_message
        - Not sure if I need a separate function for this
        - Inputs: sender, receiver, timestamp
        - ASSUMPTIONS:
            - Voice  is saved already in some sort of blob storage (this would be a functionality of this module or of another module? I think this module)
            - This function only needs the link to this video to save the data in the db 


## REST API
- Upload_text_message POST
- Retrieve_message GET
- Search_by_keyword GET
- Upload_video_message POST
- Upload_voice_message POST

## What info do I need to store?
1. Session Id: I can use this to retrieve a whole conversation and which messages go in that conversation. 
2. Sender info
    - Name
    - Role: patient or MP. not sure if I would need this 
3. Receiver info
    - Name 
    - Role: patient or MP. Not sure if I would need this 
4. All chat text conversations
    - Time of sent 
    - If it was received 
    - Content
    - Message Id: would this be useful in any way?
5. All attachments: this includes video as chat. Files. Voice messages
    - Time of sent 
    - If it was received 
    - Store as link to the actual attachment
    - Attachment will be stored in blob storage 

## Data Saving:
- Attachments: videos, images, voice recordings
    - Document can be used to store link of the media
        - Performance wise you don’t want to store the actual attachment
    - Do attachments come alongside text or by themselves?
        - Yes the message could have multiple types. I would have to go through the db of the message first and also save the attachments in like a blob storage. 
- Text
    - Strings are def easier to save 
    - Schema would work fine with these fields in it:
        - Sender info
        - Receiver info
        - Text
        - Timestamps and so on about the message 

## Data Retrieve:
- Need to be able to retrieve all this data (chat history) for when users log back in and want to see the previous conversation 
- Need to be able to easily search through all data for the keyword search and pull entire messages with attachments. I might want the DB to have an easy structure for this?
    - Would I want the attachments to be stored separately from the rest of the messages? Yes, because I would only save the link of the attachment alongside the message and have the actual attachments saved in a blob storage

## DB decision: Document or SQL?
For text messages SQL db will put a restriction on how long the message text could be. Document db will be better for this. 
Document is also more dynamic so if a message has attachments or not then the fields of the document will change. Better to do this. 



